"""Diagnostic only: the preregistered six-point Toeplitz quotient-PD screen.

Eigendecomposition selects a rational vector; it is never a certificate.
The --input operation consumes archived values and does not evaluate theta.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import mpmath as mp


BITS = (128, 256)
SIZE = 6
DYADIC_BITS = 32
THRESHOLD_BITS = 40


def decimal(value: Any, bits: int) -> str:
    """Retain at least the working binary precision in decimal serialization."""
    return str(mp.nstr(value, n=int(bits * 0.302) + 12))


def nearest_even_integer(value: Any) -> int:
    """Round to nearest integer with an explicit ties-to-even rule."""
    lower = int(mp.floor(value))
    fraction = value - lower
    if fraction < mp.mpf("0.5"):
        return lower
    if fraction > mp.mpf("0.5"):
        return lower + 1
    return lower if lower % 2 == 0 else lower + 1


def matrix_from_values(values: list[str]) -> Any:
    if len(values) != SIZE:
        raise ValueError("The fixed stencil requires exactly six values")
    numbers = [mp.mpf(value) for value in values]
    if any(not mp.isfinite(value) for value in numbers):
        raise ValueError("Nonfinite input is inconclusive and cannot be screened")
    if numbers[0] <= 0:
        raise ValueError("This normalized screen requires positive k(0)")
    return mp.matrix([[numbers[abs(i - j)] for j in range(SIZE)] for i in range(SIZE)])


def rational_witness(eigenvectors: Any) -> list[int]:
    vector = [eigenvectors[j, 0] for j in range(SIZE)]
    norm = max(abs(value) for value in vector)
    pivot = next(j for j, value in enumerate(vector) if abs(value) == norm)
    orientation = 1 if vector[pivot] >= 0 else -1
    return [nearest_even_integer(orientation * value / norm * (1 << DYADIC_BITS))
            for value in vector]


def analyze_pair(name: str, evaluations: list[dict[str, Any]]) -> dict[str, Any]:
    """Apply exactly one fixed rational vector to both prescribed precisions."""
    if len(evaluations) != 2 or tuple(item["bits"] for item in evaluations) != BITS:
        raise ValueError("Require precisely the 128-bit and 256-bit evaluations in order")
    numerator: list[int] | None = None
    runs: list[dict[str, Any]] = []
    for item in evaluations:
        bits = int(item["bits"])
        with mp.workprec(bits):
            matrix = matrix_from_values(item["values"])
            eigenvalues, eigenvectors = mp.eigsy(matrix)
            if numerator is None:
                numerator = rational_witness(eigenvectors)
            vector = mp.matrix([mp.mpf(n) / (1 << DYADIC_BITS) for n in numerator])
            norm_squared = (vector.T * vector)[0]
            quadratic = (vector.T * matrix * vector)[0]
            scale = matrix[0, 0] * norm_squared
            threshold = mp.ldexp(scale, -THRESHOLD_BITS)
            normalized = quadratic / scale
            runs.append({
                "bits": bits,
                "values": [decimal(matrix[0, j], bits) for j in range(SIZE)],
                "matrix": [[decimal(matrix[i, j], bits) for j in range(SIZE)]
                           for i in range(SIZE)],
                "eigenvalues_diagnostic": [decimal(eigenvalues[j], bits) for j in range(SIZE)],
                "minimum_eigenvalue_diagnostic": decimal(eigenvalues[0], bits),
                "fixed_witness_quadratic_form_diagnostic": decimal(quadratic, bits),
                "fixed_witness_norm_squared": decimal(norm_squared, bits),
                "negative_margin_required": decimal(threshold, bits),
                "normalized_quadratic_form_diagnostic": decimal(normalized, bits),
                "negative_beyond_margin": bool(quadratic < -threshold),
                "minimum_eigenvalue_positive_beyond_margin": bool(
                    eigenvalues[0] > mp.ldexp(matrix[0, 0], -THRESHOLD_BITS)),
            })
    with mp.workprec(256):
        tolerance = mp.ldexp(mp.mpf(1), -THRESHOLD_BITS)
        value_scale = max(abs(mp.mpf(run["values"][0])) for run in runs)
        value_discrepancies = [abs(mp.mpf(runs[0]["values"][j]) - mp.mpf(runs[1]["values"][j]))
                               / value_scale for j in range(SIZE)]
        form_discrepancy = abs(mp.mpf(runs[0]["normalized_quadratic_form_diagnostic"])
                               - mp.mpf(runs[1]["normalized_quadratic_form_diagnostic"]))
        agreement = bool(max(value_discrepancies) <= tolerance and form_discrepancy <= tolerance)
        candidate = agreement and all(run["negative_beyond_margin"] for run in runs)
        return {
            "name": name,
            "classification": "diagnostic; not an interval certificate",
            "stencil": ["0", "1/4", "1/2", "3/4", "1", "5/4"],
            "witness_rule": "128-bit minimum eigenvector; maxabs=1; first max positive; nearest dyadic 2^-32, ties to even",
            "witness_numerators": numerator,
            "witness_denominator": 1 << DYADIC_BITS,
            "runs": runs,
            "agreement_tolerance": "2^-40",
            "agreement_rule": "max_j abs(k128_j-k256_j) <= 2^-40*max(abs(k128_0),abs(k256_0)); abs(q128/(k128_0*norm2)-q256/(k256_0*norm2)) <= 2^-40",
            "negative_rule": "The identical fixed rational vector must have q < -2^-40*k(0)*norm2 at both precisions",
            "mpmath_version": mp.__version__,
            "normalized_value_discrepancies": [decimal(value, 256) for value in value_discrepancies],
            "normalized_form_discrepancy": decimal(form_discrepancy, 256),
            "agreement_pass": agreement,
            "negative_diagnostic_candidate": candidate,
            "status": ("negative rational diagnostic witness; complete Arb validation required"
                       if candidate else "inconclusive; no admitted negative diagnostic witness"),
        }


def controls() -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for name in ("gaussian_positive", "pole_free_non_pd"):
        evaluations: list[dict[str, Any]] = []
        for bits in BITS:
            with mp.workprec(bits):
                values: list[str] = []
                for j in range(SIZE):
                    t = mp.mpf(j) / 4
                    value = mp.exp(-t * t)
                    if name == "pole_free_non_pd":
                        value *= 1 + t * t
                    values.append(decimal(value, bits))
                evaluations.append({"bits": bits, "values": values})
        records.append(analyze_pair(name, evaluations))
    positive_ok = records[0]["agreement_pass"] and all(
        run["minimum_eigenvalue_positive_beyond_margin"] for run in records[0]["runs"])
    negative_ok = records[1]["negative_diagnostic_candidate"]
    return {
        "classification": "synthetic diagnostic controls; not interval certificates",
        "controls_pass": bool(positive_ok and negative_ok),
        "gaussian_positive_pass": bool(positive_ok),
        "pole_free_non_pd_pass": bool(negative_ok),
        "controls": records,
        "scope": "Same stencil, eigensolve, dyadic witness, replay, and decision rule. Does not validate theta quadrature or prove original quotient PD.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="Archived original values; omitted means synthetic controls only")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.input is None:
        result = controls()
    else:
        source = json.loads(args.input.read_text())
        result = analyze_pair(source["name"], source["evaluations"])
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key in ("controls_pass", "gaussian_positive_pass", "pole_free_non_pd_pass",
                                 "agreement_pass", "negative_diagnostic_candidate", "status")}))


if __name__ == "__main__":
    main()
