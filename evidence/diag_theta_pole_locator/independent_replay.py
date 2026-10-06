"""Independent endpoint replay only: direct theta terms and tanh-sinh quadrature.

This is DIAGNOSTIC, not an interval certificate.  No grid, root iteration,
or candidate selection is performed.  Only up to four archived 256-bit
endpoints and the preselected lower-left original grid corner are eligible.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time
from typing import Any

import mpmath as mp


def text(value: Any) -> str:
    """Retain all working-precision decimal digits in the archive."""
    return str(mp.nstr(value, mp.mp.dps))


def packed(value: Any) -> dict[str, str]:
    """Serialize an ordinary complex value without binary64 conversion."""
    return {"re": text(mp.re(value)), "im": text(mp.im(value))}


def unpacked(value: dict[str, str]) -> Any:
    """Parse archived decimal components in the active working context."""
    return mp.mpc(value["re"], value["im"])


def phi_direct(argument: Any, cutoff: int = 36) -> tuple[Any, Any]:
    """Direct kernel/derivative summands, no imported evaluator or recurrence."""
    u = argument if mp.re(argument) >= 0 else -argument
    sign = 1 if mp.re(argument) >= 0 else -1
    t = mp.pi * mp.exp(2 * u)
    exponentials = [mp.exp(-t * n * n) for n in range(1, cutoff + 1)]
    factor = mp.exp(u / 2)
    value = factor * mp.fsum((2 * t * t * n**4 - 3 * t * n**2) * exponentials[n - 1]
                              for n in range(1, cutoff + 1))
    derivative = sign * factor * mp.fsum(
        (-4 * t**3 * n**6 + 15 * t * t * n**4 - mp.mpf(15) / 2 * t * n**2) * exponentials[n - 1]
        for n in range(1, cutoff + 1))
    return value, derivative


def discarded_majorants(z: Any, normalization: Any, radius: Any, cutoff: int) -> dict[str, str]:
    """Uniform analytic truncation formulas; values are NOT interval bounds.

    On the entire registered strip |Im z|<=5/8 put b=pi*cos(5/4),
    d=b/2.  A global envelope K exp(-d exp(2|Re u|)) bounds phi.
    Polynomial-exponential maxima and geometric Gaussian tails bound K
    and the discarded original n-lattice.  Real-s tails retain both ends.
    The unbounded errors remaining are roundoff and finite quadrature.
    """
    b = mp.pi * mp.cos(mp.mpf(5) / 4)
    d = b / 2

    def gaussian_tail(power: int, last: int) -> Any:
        n = mp.mpf(last + 1)
        ratio = ((n + 1) / n) ** power * mp.exp(-b * (2 * n + 1))
        if not 0 <= ratio < 1:
            raise ValueError("Gaussian-tail ratio not contracting")
        return n**power * mp.exp(-b * n * n) / (1 - ratio)

    def maximum(power: Any) -> Any:
        t = max(mp.mpf(1), power / d)
        return t**power * mp.exp(-d * t)

    sums = {
        power: mp.exp(b) * (
            mp.fsum(mp.mpf(n) ** power * mp.exp(-b * n * n) for n in range(1, 41))
            + gaussian_tail(power, 40)
        )
        for power in (2, 4, 6)
    }
    bound_k = 2 * mp.pi**2 * sums[4] * maximum(mp.mpf(9) / 4) + 3 * mp.pi * sums[2] * maximum(mp.mpf(5) / 4)
    bound_k1 = (4 * mp.pi**3 * sums[6] * maximum(mp.mpf(13) / 4)
                + 15 * mp.pi**2 * sums[4] * maximum(mp.mpf(9) / 4)
                + mp.mpf(15) / 2 * mp.pi * sums[2] * maximum(mp.mpf(5) / 4))
    bound_phi = bound_k * mp.exp(-d)
    bound_phi1 = bound_k1 * mp.exp(-d)
    if b * (cutoff + 1) ** 2 <= mp.mpf(13) / 4:
        raise ValueError("Uniform lattice-tail monotonicity unavailable")
    lattice_phi = 2 * mp.pi**2 * gaussian_tail(4, cutoff) + 3 * mp.pi * gaussian_tail(2, cutoff)
    lattice_phi1 = (4 * mp.pi**3 * gaussian_tail(6, cutoff) + 15 * mp.pi**2 * gaussian_tail(4, cutoff)
                    + mp.mpf(15) / 2 * mp.pi * gaussian_tail(2, cutoff))
    product_error = 2 * bound_phi * lattice_phi + lattice_phi**2
    derivative_error = 2 * (bound_phi * lattice_phi1 + bound_phi1 * lattice_phi + lattice_phi * lattice_phi1)
    scale = abs(normalization)
    big_d = d * mp.exp(2 * radius)
    tail_m = bound_k**2 * mp.exp(-big_d) / big_d
    tail_dm = 2 * bound_k * bound_k1 * mp.exp(-big_d) / big_d
    normalization_derivative = abs(4 * mp.pi * mp.exp(2 * z) - 9)
    return {
        "normalized_lattice_m": text(scale * 2 * radius * product_error),
        "normalized_lattice_c": text(scale * 2 * radius**3 / 3 * product_error),
        "normalized_lattice_dm": text(scale * 2 * radius * (derivative_error + normalization_derivative * product_error)),
        "normalized_real_tail_m": text(scale * tail_m),
        "normalized_real_tail_c": text(scale * tail_m * (radius**2 + radius / big_d + 1 / (2 * big_d**2))),
        "normalized_real_tail_dm": text(scale * (tail_dm + normalization_derivative * tail_m)),
        "uniform_strip_height": "5/8",
        "uniform_envelope_K": text(bound_k),
        "uniform_envelope_d": text(d),
        "status": "ordinary-number evaluations of analytic truncation majorants; not outward-rounded intervals",
        "remaining_errors": "roundoff and quadrature are not rigorously bounded",
    }


def independent_evaluate(z: Any, bits: int) -> dict[str, Any]:
    """Two normalized moments by adaptive tanh-sinh, no root location."""
    with mp.workprec(bits):
        z = mp.mpc(z)
        if not (mp.mpf(1) / 8 <= z.real <= 2 and mp.mpf(1) / 8 <= z.imag <= mp.mpf(5) / 8):
            raise ValueError("Point is outside the single registered rectangle")
        cutoff, radius = 36, mp.mpf(5)
        normalization = mp.exp(2 * mp.pi * mp.exp(2 * z) - 9 * z) / (4 * mp.pi**4)
        breakpoints = sorted(set([mp.mpf(0), mp.mpf(1) / 16, mp.mpf(1) / 8,
                                  mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(1),
                                  mp.mpf(3) / 2, mp.mpf(2), mp.mpf(3), mp.mpf(4), radius, z.real]))
        values: dict[Any, tuple[Any, Any]] = {}

        def products(s: Any) -> tuple[Any, Any]:
            if s not in values:
                plus, plus_derivative = phi_direct(s + z, cutoff)
                minus, minus_derivative = phi_direct(s - z, cutoff)
                values[s] = (2 * normalization * plus * minus,
                             2 * normalization * (plus_derivative * minus - plus * minus_derivative))
            return values[s]

        moment_m, error_m = mp.quad(lambda s: products(s)[0], breakpoints, method="tanh-sinh", error=True, maxdegree=8)
        moment_c, error_c = mp.quad(lambda s: s * s * products(s)[0], breakpoints,
                                     method="tanh-sinh", error=True, maxdegree=8)
        integral_dm, error_dm = mp.quad(lambda s: products(s)[1], breakpoints,
                                        method="tanh-sinh", error=True, maxdegree=8)
        log_derivative = 4 * mp.pi * mp.exp(2 * z) - 9
        moment_dm = integral_dm + log_derivative * moment_m
        return {
            "m": packed(moment_m), "c": packed(moment_c), "dm": packed(moment_dm),
            "heuristic_quadrature_error_m": text(error_m),
            "heuristic_quadrature_error_c": text(error_c),
            "heuristic_quadrature_error_dm": text(error_dm + abs(log_derivative) * error_m),
            "integrand_evaluations": len(values),
            "method": "mpmath adaptive tanh-sinh, maxdegree=8; direct original theta terms",
            "bits": bits, "lattice_cutoff": cutoff,
            "positive_half_breakpoints": [text(point) for point in breakpoints],
            "majorants": discarded_majorants(z, normalization, radius, cutoff),
            "classification": "diagnostic; neither approximate agreement nor heuristic error is a certificate",
        }


def compare(reference: dict[str, Any], computed: dict[str, Any]) -> dict[str, str]:
    """Report absolute and reference-relative differences without pass claims."""
    result: dict[str, str] = {}
    for name in ("m", "c", "dm"):
        if name not in reference:
            continue
        old, new = unpacked(reference[name]), unpacked(computed[name])
        difference = abs(new - old)
        result[f"absolute_{name}_difference"] = text(difference)
        result[f"relative_{name}_difference"] = text(difference / abs(new)) if new else "undefined: independent value zero"
    return result


def main() -> None:
    """Require explicit authorization and replay only archived preselected points."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--approved", action="store_true")
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("original.json"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("independent.json"))
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--max-endpoints", type=int, default=4)
    parser.add_argument("--include-corner", action="store_true")
    args = parser.parse_args()
    if not args.approved or not 0 <= args.max_endpoints <= 4 or args.bits < 256:
        parser.error("approval, 0..4 existing endpoints and at least 256 bits required")
    data = args.input.read_bytes()
    original = json.loads(data)
    selected = []
    for index, item in enumerate(original.get("second_refinements", [])[:args.max_endpoints]):
        reference = next(call["values"] for call in reversed(original["calls"])
                         if call["bits"] == 256 and call["z"] == item["endpoint"])
        selected.append({"source": f"second_refinements[{index}]", "z": item["endpoint"], "reference": reference})
    if args.include_corner:
        corner = next(item for item in original["calls"] if item["purpose"] == "grid_0_0")
        selected.append({"source": "calls: grid_0_0 (fixed lower-left corner)", "z": corner["z"], "reference": corner["values"]})
    if not selected:
        parser.error("no eligible archived points")
    payload: dict[str, Any] = {
        "classification": "independent diagnostic replay only; not a scan or certificate",
        "original_sha256": hashlib.sha256(data).hexdigest(), "original_status": original["status"],
        "status": "running", "points": [],
    }
    started = time.monotonic()
    for item in selected:
        point_started = time.monotonic()
        with mp.workprec(args.bits):
            result = independent_evaluate(unpacked(item["z"]), args.bits)
            payload["points"].append({"source": item["source"], "z": item["z"], "result": result,
                                      "comparison": compare(item["reference"], result),
                                      "elapsed_seconds": time.monotonic() - point_started})
        payload["elapsed_seconds"] = time.monotonic() - started
        args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"completed": item["source"], "elapsed_seconds": payload["elapsed_seconds"]}), flush=True)
    payload["status"] = "completed_independent_endpoint_replay"
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
