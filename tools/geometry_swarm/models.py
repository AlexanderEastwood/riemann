"""Bounded local OpenAI-compatible requests; model text is never executed."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import http.client
import ipaddress
import json
import math
import os
from pathlib import Path
import re
import socket
import ssl
import threading
import time
from typing import Any, Sequence
from urllib.parse import urlsplit


@dataclass(frozen=True)
class Endpoint:
    base_url: str
    model: str
    api_key_env: str | None = None
    enable_thinking: bool | None = None


@dataclass(frozen=True)
class Job:
    job_id: str
    endpoint: Endpoint
    system_prompt: str
    user_prompt: str
    max_tokens: int = 1200
    temperature: float = 0.5


class LocalEndpointError(ValueError):
    """A safe, fixed error code, never upstream exception text."""


_NETWORKS = tuple(ipaddress.ip_network(net) for net in (
    "127.0.0.0/8", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16",
    "100.64.0.0/10", "::1/128", "fc00::/7",
))
_MAX_RESPONSE_BYTES = 2 * 1024 * 1024
_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}\Z")
_ENV_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")


def _local_address(address: str) -> bool:
    try:
        ip = ipaddress.ip_address(address)
    except ValueError:
        return False
    if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped is not None:
        ip = ip.ipv4_mapped
    return any(ip.version == network.version and ip in network for network in _NETWORKS)


def _base_parts(base_url: str) -> tuple[str, str, int, str]:
    if not isinstance(base_url, str):
        raise LocalEndpointError("invalid_endpoint")
    try:
        parts = urlsplit(base_url)
        port = parts.port
        host = parts.hostname
    except (ValueError, TypeError):
        raise LocalEndpointError("invalid_endpoint") from None
    if (
        not isinstance(base_url, str) or base_url != base_url.strip()
        or any(ord(char) < 33 for char in base_url)
        or parts.scheme not in ("http", "https")
        or not host or parts.username is not None or parts.password is not None
        or parts.query or parts.fragment or parts.path not in ("/v1", "/v1/")
        or "%" in host or "\\" in host
    ):
        raise LocalEndpointError("invalid_endpoint")
    port = port if port is not None else (443 if parts.scheme == "https" else 80)
    if not 1 <= port <= 65535:
        raise LocalEndpointError("invalid_endpoint")
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        literal = None
    if literal is not None and not _local_address(str(literal)):
        raise LocalEndpointError("nonlocal_endpoint")
    return parts.scheme, host, port, base_url.rstrip("/")


def _resolve_local(host: str, port: int) -> str:
    try:
        answers = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    except OSError:
        raise LocalEndpointError("dns_failed") from None
    addresses = sorted({str(answer[4][0]) for answer in answers})
    if not addresses or not all(_local_address(address) for address in addresses):
        raise LocalEndpointError("nonlocal_endpoint")
    return addresses[0]


def _timeout(value: float, ceiling: float = 90.0) -> None:
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise ValueError("timeout must be a finite positive number")
    if not math.isfinite(value) or not 0 < value <= ceiling:
        raise ValueError(f"timeout must be in (0, {ceiling}]")


class _PinnedConnection(http.client.HTTPConnection):
    """Use a validated IP while preserving the original Host and TLS SNI."""

    def __init__(self, host: str, port: int, address: str, timeout: float, secure: bool) -> None:
        super().__init__(host, port, timeout=timeout)
        self._address = address
        self._secure = secure
        self._stopped = threading.Event()
        self._transport: socket.socket | None = None

    def connect(self) -> None:
        raw = socket.create_connection((self._address, self.port), self.timeout)
        self.sock = raw
        self._transport = raw
        if self._stopped.is_set():
            self.abort()
            raise TimeoutError
        if self._secure:
            self.sock = ssl.create_default_context().wrap_socket(raw, server_hostname=self.host)
            self._transport = self.sock
        if self._stopped.is_set():
            self.abort()
            raise TimeoutError

    def abort(self) -> None:
        self._stopped.set()
        # HTTP/1.0 may detach self.sock while HTTPResponse still reads its file.
        current = self._transport
        if current is not None:
            try:
                current.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
        self.close()


def _request(base_url: str, path: str, timeout: float, payload: dict[str, object] | None = None,
             api_key: str | None = None) -> tuple[object, int]:
    scheme, host, port, _ = _base_parts(base_url)
    address = _resolve_local(host, port)
    connection = _PinnedConnection(host, port, address, timeout, scheme == "https")
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if api_key is not None:
        headers["Authorization"] = f"Bearer {api_key}"
    body = json.dumps(payload, allow_nan=False).encode("utf-8") if payload is not None else None
    timer = threading.Timer(timeout, connection.abort)
    timer.daemon = True
    timer.start()
    try:
        connection.request("POST" if payload is not None else "GET", "/v1" + path, body, headers)
        response = connection.getresponse()
        status = response.status
        if 300 <= status < 400:
            raise LocalEndpointError("redirect_rejected")
        if not 200 <= status < 300:
            raise LocalEndpointError(f"http_{status}")
        raw = response.read(_MAX_RESPONSE_BYTES + 1)
        if connection._stopped.is_set():
            raise LocalEndpointError("request_timeout")
        if len(raw) > _MAX_RESPONSE_BYTES:
            raise LocalEndpointError("response_too_large")
        try:
            def reject_constant(value: str) -> None:
                raise ValueError("nonfinite JSON constant")

            parsed: object = json.loads(raw, parse_constant=reject_constant)
        except (ValueError, UnicodeError):
            raise LocalEndpointError("malformed_json") from None
        return parsed, status
    except LocalEndpointError:
        raise
    except TimeoutError:
        raise LocalEndpointError("request_timeout") from None
    except (OSError, http.client.HTTPException, ValueError):
        code = "request_timeout" if connection._stopped.is_set() else "request_failed"
        raise LocalEndpointError(code) from None
    finally:
        timer.cancel()
        connection.close()


def discover_models(base_url: str, timeout: float = 10.0) -> list[str]:
    """List IDs from a running unauthenticated local /v1/models service."""
    _timeout(timeout)
    parsed, _ = _request(base_url, "/models", timeout)
    if not isinstance(parsed, dict) or not isinstance(parsed.get("data"), list):
        raise LocalEndpointError("invalid_models_response")
    models: list[str] = []
    for item in parsed["data"]:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"].strip():
            raise LocalEndpointError("invalid_models_response")
        models.append(item["id"])
    return list(dict.fromkeys(models))


def _validate_jobs(jobs: Sequence[Job], workers: int, timeout: float) -> None:
    if not 1 <= len(jobs) <= 32:
        raise ValueError("supply 1 to 32 jobs")
    if isinstance(workers, bool) or not isinstance(workers, int) or not 1 <= workers <= 4:
        raise ValueError("workers must be an integer from 1 to 4")
    _timeout(timeout)
    ids: set[str] = set()
    for job in jobs:
        if not _NAME.fullmatch(job.job_id) or job.job_id in ids or job.job_id == "results":
            raise ValueError("job IDs must be unique safe filenames, at most 64 characters")
        ids.add(job.job_id)
        _base_parts(job.endpoint.base_url)
        if not isinstance(job.endpoint.model, str) or not job.endpoint.model.strip():
            raise ValueError("each endpoint needs an explicit model")
        env = job.endpoint.api_key_env
        if env is not None and (not isinstance(env, str) or not _ENV_NAME.fullmatch(env)):
            raise ValueError("invalid API key environment name")
        if job.endpoint.enable_thinking is not None and not isinstance(job.endpoint.enable_thinking, bool):
            raise ValueError("enable_thinking must be a boolean or None")
        if isinstance(job.max_tokens, bool) or not isinstance(job.max_tokens, int) or not 1 <= job.max_tokens <= 4096:
            raise ValueError("max_tokens must be an integer from 1 to 4096")
        if isinstance(job.temperature, bool) or not isinstance(job.temperature, (int, float)) or not math.isfinite(job.temperature) or not 0 <= job.temperature <= 2:
            raise ValueError("temperature must be a finite number from 0 to 2")
        if not isinstance(job.system_prompt, str) or not isinstance(job.user_prompt, str) or not job.user_prompt.strip():
            raise ValueError("prompts must be strings with a nonempty user prompt")
        if len(job.system_prompt) + len(job.user_prompt) > 262144:
            raise ValueError("combined prompt exceeds 262144 characters")


def _redact(value: Any, secrets: Sequence[str]) -> Any:
    if isinstance(value, str):
        for secret in secrets:
            value = value.replace(secret, "[REDACTED]")
        return value
    if isinstance(value, dict):
        return {key: _redact(item, secrets) for key, item in value.items()}
    if isinstance(value, list):
        return [_redact(item, secrets) for item in value]
    return value


def _run_one(job: Job, timeout: float, secrets: Sequence[str]) -> dict[str, object]:
    started = time.monotonic()
    usage: dict[str, object] = {key: None for key in ("prompt_tokens", "completion_tokens", "total_tokens")}
    result: dict[str, object] = {
        "job_id": job.job_id,
        "endpoint": {"base_url": job.endpoint.base_url.rstrip("/"), "model": job.endpoint.model},
        "prompts": {"system": job.system_prompt, "user": job.user_prompt},
        "parameters": {"max_tokens": job.max_tokens, "temperature": job.temperature,
                       "enable_thinking": job.endpoint.enable_thinking},
        "status": "failed", "response": None, "response_model": None,
        "duration_seconds": None, "usage": usage, "http_status": None, "error": None,
    }
    try:
        key = os.environ.get(job.endpoint.api_key_env) if job.endpoint.api_key_env else None
        if job.endpoint.api_key_env and (not key or "\r" in key or "\n" in key):
            raise LocalEndpointError("api_key_unavailable")
        payload: dict[str, object] = {
            "model": job.endpoint.model,
            "messages": [{"role": "system", "content": job.system_prompt}, {"role": "user", "content": job.user_prompt}],
            "max_tokens": job.max_tokens, "temperature": job.temperature, "stream": False,
        }
        if job.endpoint.enable_thinking is not None:
            payload["chat_template_kwargs"] = {"enable_thinking": job.endpoint.enable_thinking}
        parsed, status = _request(job.endpoint.base_url, "/chat/completions", timeout, payload, key)
        result["http_status"] = status
        if not isinstance(parsed, dict):
            raise LocalEndpointError("invalid_chat_response")
        if isinstance(parsed.get("usage"), dict):
            for name in usage:
                count = parsed["usage"].get(name)
                if isinstance(count, int) and not isinstance(count, bool) and count >= 0:
                    usage[name] = count
        if isinstance(parsed.get("model"), str):
            result["response_model"] = parsed["model"]
        choices = parsed.get("choices")
        if not isinstance(choices, list) or not choices or not isinstance(choices[0], dict):
            raise LocalEndpointError("invalid_chat_response")
        message = choices[0].get("message")
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str) or not content.strip() or parsed.get("error") is not None:
            raise LocalEndpointError("empty_or_invalid_content")
        result.update(status="success", response=content)
    except LocalEndpointError as error:
        result["error"] = str(error)
        if str(error).startswith("http_") and str(error)[5:].isdigit():
            result["http_status"] = int(str(error)[5:])
    except Exception:
        # Neither arbitrary exception text nor upstream bodies enter persisted errors.
        result["error"] = "unexpected_request_failure"
    result["duration_seconds"] = round(time.monotonic() - started, 6)
    return _redact(result, secrets)


def run_jobs(jobs: Sequence[Job], output_dir: Path, workers: int = 2,
             timeout: float = 60.0) -> list[dict[str, object]]:
    """Execute <=32 jobs with <=4 workers; save sanitized data to a fresh directory.

    HTTP failures become individual failed results. Invalid configuration and a
    preexisting output directory raise before inference. No retries, downloads,
    tool calls, or execution of model-generated content are performed.
    """
    queued = tuple(jobs)
    _validate_jobs(queued, workers, timeout)
    secrets = tuple(sorted({value for job in queued if job.endpoint.api_key_env
                            if (value := os.environ.get(job.endpoint.api_key_env))}, key=len, reverse=True))
    output_dir.mkdir(parents=True, exist_ok=False)

    def execute(job: Job) -> dict[str, object]:
        result = _run_one(job, timeout, secrets)
        with (output_dir / f"{job.job_id}.json").open("x", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, ensure_ascii=False, allow_nan=False)
            handle.write("\n")
        return result

    with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="local-geometry") as pool:
        results = list(pool.map(execute, queued))
    with (output_dir / "results.json").open("x", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2, ensure_ascii=False, allow_nan=False)
        handle.write("\n")
    return results
