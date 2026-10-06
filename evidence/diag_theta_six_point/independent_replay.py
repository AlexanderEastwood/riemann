"""Independent DIAGNOSTIC replay of exactly the six registered real arguments.

Direct theta summands and adaptive tanh-sinh are independent of the primary
factored evaluator / Gauss-Legendre rule. This script imports no primary code.
Lattice and both real tails are retained as analytic majorants evaluated in
ordinary arithmetic. Quadrature, roundoff and ratio errors are NOT enclosed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time
from typing import Any

import mpmath as mp

BITS = 256
CUTOFF = 36
STENCIL = ("0", "1/4", "1/2", "3/4", "1", "5/4")


def decimal(value: Any) -> str:
    """Write slightly more decimal digits than the active binary precision."""
    return str(mp.nstr(value, 85))


def phi_direct(argument: Any) -> Any:
    """Evaluate the explicit original summands with their even extension."""
    if mp.im(argument) != 0:
        raise ValueError("The registered replay uses real arguments only")
    u = abs(mp.mpf(argument))
    e2 = mp.exp(2 * u)
    e9 = mp.exp(mp.mpf(9) * u / 2)
    e5 = mp.exp(mp.mpf(5) * u / 2)
    return mp.fsum((2 * mp.pi**2 * n**4 * e9 - 3 * mp.pi * n**2 * e5)
                   * mp.exp(-mp.pi * n * n * e2)
                   for n in range(1, CUTOFF + 1))


def truncation_majorants(radius: Any) -> dict[str, str]:
    """Full lattice / two-sided real-tail formulas, NOT interval evaluations.

Put d=pi/2 and S_j=sum n^j exp(-pi(n^2-1)). Then
abs(phi(u)) <= K exp(-d exp(2 abs(u))), where K is below.
For n>CUTOFF, every polynomial exponential in x=exp(2 abs(u))
decreases for x>=1, allowing a uniform discarded-lattice bound delta.
The discarded product is bounded by 2*P*delta+delta^2 on [-R,R].
For real t>=0, max(abs(s+t),abs(s-t))>=abs(s). Dropping the
other exponential and exp(2(R+a))>=exp(2R)(1+2a) gives both tails.
"""
    d = mp.pi / 2

    def lattice_tail(power: int, last: int) -> Any:
        first = mp.mpf(last + 1)
        ratio = ((first + 1) / first) ** power * mp.exp(-mp.pi * (2 * first + 1))
        if not 0 <= ratio < 1:
            raise ValueError("Geometric tail ratio is not contracting")
        return first**power * mp.exp(-mp.pi * first**2) / (1 - ratio)

    def maximum(power: Any) -> Any:
        x = max(mp.mpf(1), power / d)
        return x**power * mp.exp(-d * x)

    sums = {j: mp.exp(mp.pi) * (mp.fsum(mp.mpf(n)**j * mp.exp(-mp.pi * n * n)
                                      for n in range(1, 41)) + lattice_tail(j, 40))
            for j in (2, 4)}
    bound_k = (2 * mp.pi**2 * sums[4] * maximum(mp.mpf(9) / 4)
               + 3 * mp.pi * sums[2] * maximum(mp.mpf(5) / 4))
    if mp.pi * (CUTOFF + 1)**2 <= mp.mpf(9) / 4:
        raise ValueError("Lattice monotonicity prerequisite failed")
    delta = 2 * mp.pi**2 * lattice_tail(4, CUTOFF) + 3 * mp.pi * lattice_tail(2, CUTOFF)
    product_error = 2 * bound_k * mp.exp(-d) * delta + delta**2
    big_d = d * mp.exp(2 * radius)
    tail_m = bound_k**2 * mp.exp(-big_d) / big_d
    return {
        "lattice_M": decimal(2 * radius * product_error),
        "lattice_C": decimal(2 * radius**3 / 3 * product_error),
        "real_tail_M": decimal(tail_m),
        "real_tail_C": decimal(tail_m * (radius**2 + radius / big_d + 1 / (2 * big_d**2))),
        "uniform_phi_lattice_tail": decimal(delta),
        "envelope_K": decimal(bound_k), "envelope_d": decimal(d),
        "status": "analytic majorants in ordinary arithmetic, not outward-rounded interval bounds",
        "remaining_errors": "quadrature, floating roundoff and ratio error are NOT bounded",
    }


def evaluate(t: Any) -> dict[str, Any]:
    """Replay only one member of the fixed real stencil, without normalization."""
    if mp.im(t) != 0 or t not in tuple(mp.mpf(j) / 4 for j in range(6)):
        raise ValueError("Only the six registered real arguments are allowed")
    radius = mp.mpf(5)
    points = sorted(set([mp.mpf(0), mp.mpf(1) / 16, mp.mpf(1) / 8,
                         mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(1),
                         mp.mpf(3) / 2, mp.mpf(2), mp.mpf(3), mp.mpf(4), radius, t]))
    cache: dict[Any, Any] = {}

    def product(s: Any) -> Any:
        if s not in cache:
            cache[s] = 2 * phi_direct(s + t) * phi_direct(s - t)
        return cache[s]

    moment_m, error_m = mp.quad(product, points, method="tanh-sinh", error=True, maxdegree=8)
    moment_c, error_c = mp.quad(lambda s: s * s * product(s), points,
                               method="tanh-sinh", error=True, maxdegree=8)
    if not all(mp.isfinite(x) and x > 0 for x in (moment_m, moment_c)):
        raise ValueError("Invalid diagnostic moments; stop inconclusive")
    return {
        "M": decimal(moment_m), "C": decimal(moment_c), "k": decimal(moment_c / moment_m),
        "heuristic_error_M": decimal(error_m), "heuristic_error_C": decimal(error_c),
        "bits": BITS, "lattice_cutoff": CUTOFF, "integration_radius": decimal(radius),
        "method": "direct original theta summands; raw unnormalized moments; adaptive tanh-sinh maxdegree=8",
        "positive_half_breakpoints": [decimal(x) for x in points],
        "integrand_evaluations": len(cache), "majorants": truncation_majorants(radius),
    }


def main() -> None:
    """Consume existing primary values and its ONE frozen rational vector."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--approved", action="store_true")
    args = parser.parse_args()
    if not args.approved:
        parser.error("Explicit approved replay required")
    directory = Path(__file__).resolve().parent
    raw = (directory / "original.json").read_bytes()
    screen_raw = (directory / "original-screen.json").read_bytes()
    original, screen = json.loads(raw), json.loads(screen_raw)
    if original["stencil"] != list(STENCIL) or screen["stencil"] != list(STENCIL):
        raise ValueError("Archived stencil changed")
    reference = next(item for item in original["evaluations"] if item["bits"] == BITS)
    reference_screen = next(item for item in screen["runs"] if item["bits"] == BITS)
    result: dict[str, Any] = {
        "classification": "independent diagnostic replay, NOT an interval certificate",
        "original_sha256": hashlib.sha256(raw).hexdigest(),
        "original_screen_sha256": hashlib.sha256(screen_raw).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "status": "running", "stencil": list(STENCIL), "bits": BITS, "points": [],
        "mpmath_version": mp.__version__, "unbounded_errors": ["quadrature", "floating roundoff", "ratio error"],
    }
    started = time.monotonic()
    output = directory / "independent.json"
    with mp.workprec(BITS):
        values = []
        for index, name in enumerate(STENCIL):
            point_started = time.monotonic()
            evaluation = evaluate(mp.mpf(index) / 4)
            values.append(mp.mpf(evaluation["k"]))
            old = reference["samples"][index]
            comparisons: dict[str, str] = {}
            for key in ("M", "C", "k"):
                fresh, previous = mp.mpf(evaluation[key]), mp.mpf(old[key]["re"])
                comparisons[f"absolute_{key}_difference"] = decimal(abs(fresh - previous))
                comparisons[f"relative_{key}_difference"] = decimal(abs(fresh - previous) / abs(fresh))
            result["points"].append({"t": name, "evaluation": evaluation, "comparison": comparisons,
                                     "elapsed_seconds": time.monotonic() - point_started})
            result["elapsed_seconds"] = time.monotonic() - started
            output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
            print(json.dumps({"completed_t": name, "elapsed_seconds": result["elapsed_seconds"]}), flush=True)
        matrix = mp.matrix([[values[abs(i - j)] for j in range(6)] for i in range(6)])
        numerator, denominator = screen["witness_numerators"], screen["witness_denominator"]
        if len(numerator) != 6 or denominator != 2**32:
            raise ValueError("Frozen rational witness has invalid size/denominator")
        vector = [mp.mpf(n) / denominator for n in numerator]
        form = mp.fsum(vector[i] * values[abs(i - j)] * vector[j] for i in range(6) for j in range(6))
        norm = mp.fsum(x * x for x in vector)
        eigenvalues = mp.eigsy(matrix, eigvals_only=True)
        prior_form = mp.mpf(reference_screen["fixed_witness_quadratic_form_diagnostic"])
        result["matrix"] = [[decimal(matrix[i, j]) for j in range(6)] for i in range(6)]
        result["eigenvalues_diagnostic"] = [decimal(eigenvalues[i]) for i in range(6)]
        result["witness_numerators"], result["witness_denominator"] = numerator, denominator
        result["fixed_witness_quadratic_form_diagnostic"] = decimal(form)
        result["normalized_quadratic_form_diagnostic"] = decimal(form / (values[0] * norm))
        result["absolute_form_difference"] = decimal(abs(form - prior_form))
        result["relative_form_difference"] = decimal(abs(form - prior_form) / abs(form))
        result["maximum_absolute_matrix_difference"] = decimal(max(abs(matrix[i, j] - mp.mpf(reference_screen["matrix"][i][j]))
                                                                   for i in range(6) for j in range(6)))
        result["status"] = "completed independent replay; no global PD or finite-matrix certificate"
        result["elapsed_seconds"] = time.monotonic() - started
        output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
