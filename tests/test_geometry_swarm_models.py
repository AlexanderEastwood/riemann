"""Local fake-server tests; no model endpoint or download is required."""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import replace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import socket
import tempfile
import threading
import time
from typing import Iterator
import unittest
from unittest.mock import patch

from tools.geometry_swarm.models import Endpoint, Job, LocalEndpointError, discover_models, run_jobs


class FakeHandler(BaseHTTPRequestHandler):
    authorization: list[str | None] = []
    paths: list[str] = []
    requests: list[dict[str, object]] = []
    active = 0
    maximum_active = 0
    lock = threading.Lock()

    def log_message(self, format: str, *args: object) -> None:
        pass

    def reply(self, status: int, body: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_GET(self) -> None:
        self.paths.append(self.path)
        if self.path == "/v1/models":
            self.reply(200, b'{"data":[{"id":"tiny-local"},{"id":"tiny-local"},{"id":"critic"}]}')
        else:
            self.reply(400, b"{}")

    def do_POST(self) -> None:
        self.paths.append(self.path)
        self.authorization.append(self.headers.get("Authorization"))
        request = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        self.requests.append(request)
        model = request["model"]
        with self.lock:
            type(self).active += 1
            type(self).maximum_active = max(self.active, self.maximum_active)
        try:
            self.respond_to_model(model)
        finally:
            with self.lock:
                type(self).active -= 1

    def respond_to_model(self, model: str) -> None:
        if model == "slow-body":
            body = b'{"choices":[{"message":{"content":"late"}}]}'
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            time.sleep(0.4)
            try:
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                pass
        elif model == "invalid-json":
            self.reply(200, b"not json")
        elif model == "nonfinite-json":
            self.reply(200, b'{"choices":NaN}')
        elif model == "missing":
            self.reply(200, b'{"choices":[]}')
        elif model == "empty":
            self.reply(200, b'{"choices":[{"message":{"content":"  "}}]}')
        elif model == "bad-shape":
            self.reply(200, b'[{"choices":[]}]')
        elif model == "error":
            self.reply(503, (self.headers.get("Authorization") or "error").encode())
        elif model == "redirect":
            self.send_response(307)
            self.send_header("Location", "https://example.com/v1/chat/completions")
            self.send_header("Content-Length", "0")
            self.end_headers()
        else:
            if model == "slow":
                time.sleep(0.12)
            if model == "timeout":
                time.sleep(0.4)
            content = self.headers.get("Authorization") if model == "echo-auth" else "A proposal, not a proof."
            answer: dict[str, object] = {"model": model, "choices": [{"message": {"content": content}}]}
            if model not in ("no-usage", "slow", "timeout"):
                answer["usage"] = {"prompt_tokens": 17, "completion_tokens": 6, "total_tokens": 23}
            if model == "partial-usage":
                answer["usage"] = {"prompt_tokens": 17, "completion_tokens": "6", "total_tokens": True}
            self.reply(200, json.dumps(answer).encode())


@contextmanager
def fake_server() -> Iterator[str]:
    FakeHandler.authorization = []
    FakeHandler.paths = []
    FakeHandler.requests = []
    FakeHandler.active = 0
    FakeHandler.maximum_active = 0
    server = ThreadingHTTPServer(("127.0.0.1", 0), FakeHandler)
    thread = threading.Thread(target=server.serve_forever, kwargs={"poll_interval": 0.01}, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/v1"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


class LocalModelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def job(self, base: str, model: str = "tiny-local", job_id: str = "proposal") -> Job:
        return Job(job_id, Endpoint(base, model), "Clearly label unknowns.", "Propose a geometric prerequisite.")

    def test_success_usage_prompts_and_persistence(self) -> None:
        with fake_server() as base:
            result = run_jobs([self.job(base)], self.root / "run")[0]
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["response"], "A proposal, not a proof.")
        self.assertEqual(result["usage"], {"prompt_tokens": 17, "completion_tokens": 6, "total_tokens": 23})
        self.assertEqual(result["prompts"], {"system": "Clearly label unknowns.", "user": "Propose a geometric prerequisite."})
        self.assertIsInstance(result["duration_seconds"], float)
        self.assertEqual(json.loads((self.root / "run/proposal.json").read_text()), result)
        self.assertEqual(json.loads((self.root / "run/results.json").read_text()), [result])

    def test_discovery_uses_existing_server(self) -> None:
        with fake_server() as base:
            self.assertEqual(discover_models(base + "/"), ["tiny-local", "critic"])
        self.assertEqual(FakeHandler.paths, ["/v1/models"])

    def test_thinking_option_is_only_sent_when_explicit(self) -> None:
        with fake_server() as base:
            jobs = [self.job(base, job_id="default"), replace(self.job(base, job_id="off"), endpoint=Endpoint(base, "tiny-local", enable_thinking=False))]
            run_jobs(jobs, self.root / "run", workers=1)
        self.assertNotIn("chat_template_kwargs", FakeHandler.requests[0])
        self.assertEqual(FakeHandler.requests[1]["chat_template_kwargs"], {"enable_thinking": False})

    def test_absent_or_invalid_usage_remains_null(self) -> None:
        with fake_server() as base:
            results = run_jobs([self.job(base, "no-usage", "none"), self.job(base, "partial-usage", "partial")], self.root / "run")
        self.assertEqual(results[0]["usage"], {"prompt_tokens": None, "completion_tokens": None, "total_tokens": None})
        self.assertEqual(results[1]["usage"], {"prompt_tokens": 17, "completion_tokens": None, "total_tokens": None})

    def test_partial_failures_do_not_cancel_success(self) -> None:
        models = ["tiny-local", "missing", "empty", "invalid-json", "bad-shape", "error", "nonfinite-json"]
        with fake_server() as base:
            results = run_jobs([self.job(base, model, f"job-{index}") for index, model in enumerate(models)], self.root / "run")
        self.assertEqual([result["status"] for result in results], ["success"] + ["failed"] * 6)
        self.assertEqual(results[3]["error"], "malformed_json")
        self.assertEqual(results[5]["http_status"], 503)
        self.assertEqual(results[6]["error"], "malformed_json")
        self.assertEqual(len(list((self.root / "run").glob("*.json"))), 8)

    def test_authorization_is_sent_but_never_returned_or_saved(self) -> None:
        secret = "test-private-authorization-value"
        with fake_server() as base, patch.dict(os.environ, {"GEOMETRY_TEST_AUTH": secret}):
            jobs = [replace(self.job(base, model, model), endpoint=Endpoint(base, model, "GEOMETRY_TEST_AUTH")) for model in ("echo-auth", "error")]
            results = run_jobs(jobs, self.root / "run")
        self.assertEqual(FakeHandler.authorization, [f"Bearer {secret}"] * 2)
        self.assertNotIn(secret, json.dumps(results))
        for path in (self.root / "run").glob("*.json"):
            self.assertNotIn(secret, path.read_text())
        self.assertEqual(results[0]["response"], "Bearer [REDACTED]")

    def test_missing_auth_fails_before_network(self) -> None:
        with fake_server() as base, patch.dict(os.environ, {}, clear=True):
            job = replace(self.job(base), endpoint=Endpoint(base, "tiny-local", "GEOMETRY_TEST_MISSING"))
            result = run_jobs([job], self.root / "run")[0]
        self.assertEqual(result["error"], "api_key_unavailable")
        self.assertEqual(FakeHandler.paths, [])

    def test_redirect_is_not_followed(self) -> None:
        with fake_server() as base:
            result = run_jobs([self.job(base, "redirect")], self.root / "run")[0]
        self.assertEqual(result["error"], "redirect_rejected")
        self.assertEqual(FakeHandler.paths, ["/v1/chat/completions"])

    def test_public_and_unsafe_urls_are_rejected(self) -> None:
        urls = ["http://8.8.8.8/v1", "https://[2001:4860:4860::8888]/v1", "file:///v1", "http://user:private@localhost/v1", "http://localhost/v1?key=private", "http://localhost/v1#fragment", "http://localhost/other", "http://localhost:0/v1"]
        with patch("tools.geometry_swarm.models.socket.getaddrinfo") as resolve:
            for index, url in enumerate(urls):
                with self.subTest(url=url), self.assertRaises(LocalEndpointError):
                    run_jobs([self.job(url)], self.root / f"run-{index}")
                self.assertFalse((self.root / f"run-{index}").exists())
            resolve.assert_not_called()

    def test_dns_requires_every_address_to_be_local(self) -> None:
        answers = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (address, 8000)) for address in ("127.0.0.1", "8.8.8.8")]
        with patch("tools.geometry_swarm.models.socket.getaddrinfo", return_value=answers), patch("tools.geometry_swarm.models.socket.create_connection") as connect:
            with self.assertRaisesRegex(LocalEndpointError, "nonlocal_endpoint"):
                discover_models("http://local-name.invalid:8000/v1")
            connect.assert_not_called()

    def test_preexisting_output_is_never_overwritten(self) -> None:
        output = self.root / "run"
        output.mkdir()
        original = output / "untouched.txt"
        original.write_text("original")
        with fake_server() as base, self.assertRaises(FileExistsError):
            run_jobs([self.job(base)], output)
        self.assertEqual(original.read_text(), "original")
        self.assertEqual(FakeHandler.paths, [])

    def test_all_request_bounds_are_checked_before_output(self) -> None:
        job = self.job("http://127.0.0.1:8000/v1")
        cases = [([job] * 33, 2, 60.0), ([], 2, 60.0), ([job], 5, 60.0), ([job], 0, 60.0), ([job], 2, 91.0), ([job], 2, float("nan")), ([replace(job, max_tokens=4097)], 2, 60.0), ([replace(job, max_tokens=0)], 2, 60.0), ([replace(job, temperature=float("nan"))], 2, 60.0), ([replace(job, endpoint=Endpoint(job.endpoint.base_url, ""))], 2, 60.0), ([replace(job, job_id="../escape")], 2, 60.0), ([replace(job, job_id="results")], 2, 60.0), ([job, job], 2, 60.0)]
        for index, (jobs, workers, timeout) in enumerate(cases):
            with self.subTest(index=index), self.assertRaises(ValueError):
                run_jobs(jobs, self.root / f"run-{index}", workers, timeout)
            self.assertFalse((self.root / f"run-{index}").exists())

    def test_parallel_requests_respect_worker_limit_and_preserve_order(self) -> None:
        with fake_server() as base:
            jobs = [self.job(base, "slow", f"job-{index}") for index in range(6)]
            results = run_jobs(jobs, self.root / "run", workers=2)
        self.assertEqual([result["job_id"] for result in results], [job.job_id for job in jobs])
        self.assertEqual(FakeHandler.maximum_active, 2)
        self.assertTrue(all(result["status"] == "success" for result in results))

    def test_timeout_is_failed_without_exception_text(self) -> None:
        with fake_server() as base:
            result = run_jobs([self.job(base, "timeout")], self.root / "run", timeout=0.08)[0]
        self.assertEqual(result["status"], "failed")
        self.assertIn(result["error"], ("request_timeout", "request_failed"))
        self.assertLess(float(str(result["duration_seconds"])), 0.35)

    def test_deadline_interrupts_body_after_connection_detaches(self) -> None:
        with fake_server() as base:
            result = run_jobs([self.job(base, "slow-body")], self.root / "run", timeout=0.08)[0]
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["error"], "request_timeout")
        self.assertLess(float(str(result["duration_seconds"])), 0.35)


if __name__ == "__main__":
    unittest.main()
