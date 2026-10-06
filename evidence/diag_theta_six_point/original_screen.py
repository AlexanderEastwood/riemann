"""Fixed six-value original theta quotient diagnostic; NOT a certificate.

No original values are evaluated on import. Execution requires explicit parent
admission, the matched successful control record, and the common one-hour budget
start (including controls). No extra spacing, matrix size, or precision is tried.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import signal
import sys
import time
from types import FrameType
from typing import Any

import mpmath as mp

STENCIL = ["0", "1/4", "1/2", "3/4", "1", "5/4"]
BITS = (128, 256)
ROOT = Path(__file__).resolve().parents[2]
EVALUATOR_PATH = ROOT / "evidence/diag_theta_pole_locator/theta_eval.py"


class BudgetExpired(RuntimeError):
    """The preregistered total diagnostic time has elapsed."""


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def parse_utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Budget start must include a UTC offset")
    return parsed.astimezone(timezone.utc)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def serialize(value: Any, digits: int) -> Any:
    """Retain working digits of both real and complex diagnostic values."""
    if isinstance(value, dict):
        return {str(key): serialize(item, digits) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item, digits) for item in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    if isinstance(value, mp.mpc):
        return {"re": mp.nstr(value.real, digits), "im": mp.nstr(value.imag, digits)}
    return mp.nstr(value, digits)


def write_output(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")


def read_controls(path: Path) -> dict[str, Any]:
    """Validate the fixed matrix pipeline's matched-control admission record."""
    data: dict[str, Any] = json.loads(path.read_text())
    if data.get("controls_pass") is not True:
        raise ValueError("Matched controls must report controls_pass=true")
    records = data.get("controls", [])
    if [item.get("name") for item in records] != ["gaussian_positive", "pole_free_non_pd"]:
        raise ValueError("Controls must be the Gaussian and pole-free non-PD pair")
    for item in records:
        if item.get("stencil") != STENCIL:
            raise ValueError("Control stencil is not the preregistered six points")
        if [run.get("bits") for run in item.get("runs", [])] != list(BITS):
            raise ValueError("Controls were not replayed at 128 and 256 bits")
        if item.get("agreement_pass") is not True:
            raise ValueError("Control precision replay did not agree")
    if data.get("gaussian_positive_pass") is not True or data.get("pole_free_non_pd_pass") is not True:
        raise ValueError("Both matched controls must pass individually")
    return data


def _alarm_handler(signum: int, frame: FrameType | None) -> None:
    del signum, frame
    raise BudgetExpired("One-hour diagnostic budget, including controls, expired")


def load_evaluator() -> Any:
    spec = importlib.util.spec_from_file_location("archived_theta_eval", EVALUATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Archived theta evaluator cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate_six(record: dict[str, Any], output_path: Path, deadline: datetime) -> None:
    evaluator = load_evaluator()
    for bits in BITS:
        digits = int(bits * 0.30103) + 10
        evaluation: dict[str, Any] = {"bits": bits, "values": [], "samples": []}
        record["evaluations"].append(evaluation)
        with mp.workprec(bits):
            realness_tolerance = mp.power(2, -bits // 2)
            for index in range(6):
                if utc_now() >= deadline:
                    raise BudgetExpired("Total diagnostic budget expired before next point")
                t = mp.mpf(index) / 4
                started = time.monotonic()
                raw = evaluator.evaluate(t, bits=bits, replay=(bits == 256))
                m = raw["m"]
                c = raw["c"]
                dm = raw["dm"]
                if not all(mp.isfinite(x) for x in (m, c, dm)):
                    raise ValueError(f"Nonfinite evaluation at index={index}, bits={bits}")
                if mp.re(m) <= 0 or mp.re(c) <= 0:
                    raise ValueError(f"M or C sample not positive at index={index}, bits={bits}")
                quotient = c / m
                relative_imaginary = max(
                    abs(mp.im(m)) / abs(mp.re(m)),
                    abs(mp.im(c)) / abs(mp.re(c)),
                    abs(mp.im(quotient)) / abs(mp.re(quotient)),
                )
                if relative_imaginary > realness_tolerance:
                    raise ValueError(f"Realness check failed at index={index}, bits={bits}")
                normalization = mp.exp(2 * mp.pi * mp.exp(2 * t) - 9 * t) / (4 * mp.pi**4)
                sample = {
                    "index": index,
                    "t": STENCIL[index],
                    "m_normalized": m,
                    "c_normalized": c,
                    "dm_normalized": dm,
                    "M": m / normalization,
                    "C": c / normalization,
                    "normalization_value": normalization,
                    "k": quotient,
                    "checks": {
                        "M_sample_positive": True,
                        "C_sample_positive": True,
                        "largest_relative_imaginary_part": relative_imaginary,
                        "realness_tolerance": realness_tolerance,
                        "finite": True,
                        "sample_checks_only": True,
                    },
                    "elapsed_seconds": time.monotonic() - started,
                    "metadata": raw["metadata"],
                }
                evaluation["samples"].append(serialize(sample, digits))
                evaluation["values"].append(mp.nstr(mp.re(quotient), digits))
                write_output(output_path, record)
                print(f"Completed registered point {STENCIL[index]} at {bits} bits", flush=True)
    with mp.workprec(256):
        first = record["evaluations"][0]["values"]
        second = record["evaluations"][1]["values"]
        record["replay_observed_relative_differences"] = [
            mp.nstr(abs(mp.mpf(a) - mp.mpf(b)) / abs(mp.mpf(b)), 86)
            for a, b in zip(first, second)
        ]
        record["replay_error_status"] = "Observed discrepancies only; NOT error bounds"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--controls", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--deadline-utc", required=True)
    parser.add_argument("--preregistered-pr", required=True)
    parser.add_argument("--authorized-original", action="store_true")
    args = parser.parse_args()
    if not args.authorized_original:
        parser.error("Explicit parent GO is required; pass --authorized-original only after admission")
    if not re.fullmatch(r"https://github\.com/AlexanderEastwood/riemann/pull/[0-9]+", args.preregistered_pr):
        parser.error("A filled preregistration draft PR URL must be recorded")
    if args.output.exists():
        parser.error("Refusing to overwrite a previous original result")
    controls = read_controls(args.controls)
    deadline = parse_utc(args.deadline_utc)
    start = deadline - timedelta(hours=1)
    now = utc_now()
    if start > now:
        parser.error("Deadline must be within one hour and retain prior control time")
    remaining = (deadline - now).total_seconds()
    if remaining <= 0:
        parser.error("The one-hour budget including controls has already expired")
    record: dict[str, Any] = {
        "name": "original_theta_quotient",
        "classification": "DIAGNOSTIC ONLY; NOT a certificate",
        "status": "running",
        "stencil": STENCIL,
        "precisions_bits": list(BITS),
        "evaluations": [],
        "controls_file": str(args.controls),
        "controls_sha256": digest(args.controls),
        "control_names": [item["name"] for item in controls["controls"]],
        "preregistered_pr": args.preregistered_pr,
        "budget_start_utc": start.isoformat(),
        "deadline_utc": deadline.isoformat(),
        "started_utc": now.isoformat(),
        "source_evaluator_sha256": digest(EVALUATOR_PATH),
        "wrapper_sha256": digest(Path(__file__)),
        "normalization_cancellation": "k=(B*C)/(B*M)=C/M; identical nonzero B in both factors",
        "unbounded_errors": ["quadrature", "floating roundoff", "ratio error"],
        "certificate_status": "None; complete Arb validation is conditional on a negative witness",
    }
    old_handler = signal.signal(signal.SIGALRM, _alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, remaining)
    exit_code = 0
    try:
        evaluate_six(record, args.output, deadline)
        record["status"] = "complete"
    except BudgetExpired as exc:
        record["status"] = "inconclusive_budget_expired"
        record["error"] = str(exc)
        exit_code = 2
    except Exception as exc:
        record["status"] = "inconclusive_evaluation_error"
        record["error"] = f"{type(exc).__name__}: {exc}"
        exit_code = 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)
        record["finished_utc"] = utc_now().isoformat()
        write_output(args.output, record)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
