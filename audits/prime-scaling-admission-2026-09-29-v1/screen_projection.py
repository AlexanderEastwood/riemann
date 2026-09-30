"""Pre-admission structural control; diagnostics, not NB certificates.

Run from the workspace root with its .venv Python. The only imported project
source is pinned to the reviewed public commit and its digest is recorded.
The finite positive spectral Grams below are explicit surrogate families,
not the original fractional-part Gram of NS98. They test the structural
projection comparison on xi and Davenport--Heilbronn under matching Hilbert
and dilation hypotheses. No arithmetic cost bound is claimed or tested here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Callable

import mpmath as mp

COMMIT = "f32cadfb7be523a8920b19be57d40d652e39a2ef"
SOURCE = "controls/davenport_heilbronn.py"
REPO = Path("/Users/alex/riemann-worktrees/conclusions-review")
CASES = ((2, 2), (2, 3), (4, 2))


def mobius(n: int) -> int:
    """Exact elementary factorization, used only for the small fixed samples."""
    sign = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            sign = -sign
            if n % factor == 0:
                return 0
        factor += 1
    return -sign if n > 1 else sign


def spectral_gram(function: Callable[[Any], Any], maximum: int) -> Any:
    frequencies = [mp.mpf(k) / 2 for k in range(33)]
    weights = [abs(function(mp.j * t)) ** 2 for t in frequencies]
    total = sum(weights)
    weights = [w / total for w in weights]
    return mp.matrix([
        [sum(w * mp.cos(t * mp.log(mp.mpf(m) / n))
             for t, w in zip(frequencies, weights)) / mp.sqrt(m * n)
         for n in range(1, maximum + 1)]
        for m in range(1, maximum + 1)
    ])


def submatrix(matrix: Any, rows: list[int], cols: list[int]) -> Any:
    return mp.matrix([[matrix[m - 1, n - 1] for n in cols] for m in rows])


def projected_gram(gram: Any, old_indices: list[int], new_indices: list[int]) -> Any:
    old = submatrix(gram, old_indices, old_indices)
    cross = submatrix(gram, old_indices, new_indices)
    solved = mp.matrix(len(old_indices), len(new_indices))
    for column in range(len(new_indices)):
        solution = mp.lu_solve(old, cross[:, column])
        for row in range(len(old_indices)):
            solved[row, column] = solution[row]
    result = submatrix(gram, new_indices, new_indices) - cross.T * solved
    return (result + result.T) / 2


def quadratic(matrix: Any, vector: Any) -> Any:
    return (vector.T * matrix * vector)[0]


def sample(function: Callable[[Any], Any]) -> list[dict[str, Any]]:
    gram = spectral_gram(function, 16)
    rows: list[dict[str, Any]] = []
    tolerance = mp.power(10, -(mp.mp.dps // 2))
    for size, prime in CASES:
        indices = list(range(size + 1, 2 * size + 1))
        old = list(range(1, size + 1))
        prime_old = list(range(1, prime * size + 1))
        scaled_indices = [prime * n for n in indices]
        h = projected_gram(gram, old, indices)
        scaled = prime * projected_gram(gram, prime_old, scaled_indices)
        loss = h - scaled
        minimum_loss = mp.eigsy(loss, eigvals_only=True)[0]
        minimum_scaled = mp.eigsy(scaled, eigvals_only=True)[0]
        raw_error = max(abs(prime * gram[prime * m - 1, prime * n - 1]
                            - gram[m - 1, n - 1])
                        for m in indices for n in indices)
        coefficients = mp.matrix([
            -mobius(n) * mp.log(mp.mpf(2 * size) / n) if n % prime else 0
            for n in indices
        ])
        source_cost = quadratic(h, coefficients)
        loss_cost = quadratic(loss, coefficients)
        zero_direction = all(value == 0 for value in coefficients)
        if not zero_direction and source_cost <= 0:
            raise ArithmeticError("Nonzero diagnostic direction has unresolved positive cost")
        rows.append({
            "N": size, "p": prime,
            "min_eigenvalue_H_minus_scaled_H": mp.nstr(minimum_loss, 30),
            "min_eigenvalue_scaled_H": mp.nstr(minimum_scaled, 30),
            "raw_homogeneity_residual": mp.nstr(raw_error, 8),
            "filtered_direction_zero": zero_direction,
            "filtered_loss_fraction": None if zero_direction else mp.nstr(loss_cost / source_cost, 30),
            "passes_with_diagnostic_tolerance": bool(
                minimum_loss >= -tolerance and minimum_scaled >= -tolerance
                and raw_error <= tolerance
            ),
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = args.dps
    source = subprocess.check_output(["git", "show", f"{COMMIT}:{SOURCE}"], cwd=REPO)
    namespace: dict[str, Any] = {"__name__": "pinned_dh_control"}
    exec(compile(source, f"{COMMIT}:{SOURCE}", "exec"), namespace)
    dh_rows: list[dict[str, Any]] = []

    def candidate(function: Callable[[Any], Any], _kernel: Callable[..., Any]) -> bool:
        dh_rows.extend(sample(function))
        return all(row["passes_with_diagnostic_tolerance"] for row in dh_rows)

    structural = namespace["screen"](
        candidate,
        "0 <= p H_(pN)[pm,pn] <= H_N on finite dilation-Gram controls",
        sample_domain="t=k/2, k=0..32; (N,p)=(2,2),(2,3),(4,2); full finite Schur complements",
        applicability=(
            "Matched structural hypotheses: positive spectral Gram, exact n^(-1/2) "
            "dilation orbit and nested old spaces. Weights are |F(it)|^2 normalized "
            "to sum one. This surrogate is not NS98's physical arithmetic Gram."
        ),
        observations={"claim_scope": "finite diagnostic of the structural comparison only"},
    )
    xi_rows = sample(namespace["F_xi"])
    full_target = namespace["screen"](
        lambda _function, _kernel: None,
        "Independent bounded dyadic-index mean of the actual prime-scaling loss",
        sample_domain="fixed p, all sufficiently large dyadic J; no numerical evaluation",
        applicability=(
            "Not applicable: the original fractional-part atoms with reciprocal-zeta "
            "Mobius coefficients are part of the target. DH has different coefficients "
            "and completion; its positive spectral surrogate does not preserve this pair."
        ),
        applicable=False,
    )
    output = {
        "classification": "diagnostic admission screen, not a certificate",
        "dps": mp.mp.dps,
        "source": {"commit": COMMIT, "path": SOURCE,
                   "sha256": hashlib.sha256(source).hexdigest()},
        "candidate": "Structural projection comparison only; full arithmetic estimate unproved",
        "davenport_heilbronn_structural_screen": structural,
        "davenport_heilbronn_rows": dh_rows,
        "xi_rows": xi_rows,
        "full_arithmetic_target_screen": full_target,
        "NS100_NS101": "Not applicable to the full target: original coefficient/atom pair not preserved.",
        "NS74": "Same complete Gram preserves every H and prime-scaling loss; the unproved cost bound is not marked as passed.",
        "verdict": "Structural samples do not distinguish xi from DH. No independent loss estimate or thaw.",
    }
    with args.output.open("x") as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")
    print(json.dumps({"output": str(args.output), "dps": mp.mp.dps,
                      "DH_outcome": structural["outcome"],
                      "xi_all_pass": all(r["passes_with_diagnostic_tolerance"] for r in xi_rows)}))


if __name__ == "__main__":
    main()
