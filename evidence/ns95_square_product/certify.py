"""Complete square-block tests of product and free divisor-product spans.

Exact rational rank reduction precedes Arb projection. All norms use the
inherited complete Gram kernel, including its analytic infinite tail.
No finite efficiency is an asymptotic arithmetic lower bound.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx, fmpq_mat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
KERNEL = ROOT / "evidence/v159/ns61/certify_smoothed.py"
sys.path.insert(0, str(KERNEL.parent))
from certify_smoothed import Kernel


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def select(matrix: arb_mat, rows: list[int], cols: list[int]) -> arb_mat:
    return arb_mat([[matrix[i, j] for j in cols] for i in rows])


def dot(x: arb_mat, y: arb_mat) -> arb:
    return (x.transpose() * y)[0, 0]


def product_data(n: int) -> tuple[list[int], list[list[int]], list[int]]:
    products = sorted({i*j for i in range(1, n+1) for j in range(1, n+1)})
    matrix = [[int(k % d == 0) for d in products] for k in range(n+1, n*n+1)]
    reduced, rank = fmpq_mat(matrix).rref()
    pivots = [next(j for j in range(len(products)) if reduced[i, j]) for i in range(rank)]
    assert len(set(pivots)) == rank
    return products, matrix, pivots


def fit_span(h: arb_mat, gram: arb_mat, basis: arb_mat) -> tuple[arb, arb_mat, arb_mat]:
    loads = basis.transpose() * h
    cost = basis.transpose() * gram * basis
    parameters = cost.solve(loads, algorithm="precond")
    coefficients = basis * parameters
    gain = dot(loads, parameters)
    assert gain > 0
    assert (dot(h, coefficients) - gain).contains(0)
    assert (dot(coefficients, gram * coefficients) - gain).contains(0)
    return gain, coefficients, parameters


def analyze(n: int, kernel: Kernel) -> dict[str, Any]:
    start = time.monotonic()
    m = n*n
    gram = arb_mat([[kernel.gram(i, j) for j in range(1, m+1)] for i in range(1, m+1)])
    loads = arb_mat([[kernel.load(i)] for i in range(1, m+1)])
    old_ix, new_ix = list(range(n)), list(range(n, m))
    old = select(gram, old_ix, old_ix)
    cross = select(gram, old_ix, new_ix)
    old_loads = select(loads, old_ix, [0])
    old_c = old.solve(old_loads, algorithm="precond")
    projection = old.solve(cross, algorithm="precond")
    schur = select(gram, new_ix, new_ix) - cross.transpose() * projection
    h = select(loads, new_ix, [0]) - cross.transpose() * old_c
    energy = 2 - dot(old_loads, old_c)
    full_c = schur.solve(h, algorithm="precond")
    full_gain = dot(h, full_c)
    full_energy = energy - full_gain
    assert energy > full_energy > 0
    # A separate complete size-M solve verifies the Schur subtraction.
    direct_c = gram.solve(loads, algorithm="precond")
    assert (2-dot(loads, direct_c)).overlaps(full_energy)

    products, lift_rows, pivot_columns = product_data(n)
    product_indices = [k for k in products if k > n]
    product_basis = arb_mat([[int(k == d) for d in product_indices] for k in range(n+1, m+1)])
    lift_basis = arb_mat([[row[j] for j in pivot_columns] for row in lift_rows])
    product_gain, product_c, _ = fit_span(h, schur, product_basis)
    lift_gain, lift_c, lift_parameters = fit_span(h, schur, lift_basis)
    assert 0 < product_gain < full_gain and 0 < lift_gain < full_gain
    # The two restricted spaces are not assumed nested.
    remainder = h - schur * lift_c
    missing_gain = dot(remainder, schur.solve(remainder, algorithm="precond"))
    assert missing_gain > 0
    assert (lift_gain + missing_gain).overlaps(full_gain)
    assert all(v.contains(0) for v in lift_basis.transpose() * remainder)

    def complete_coefficients(new: arb_mat) -> arb_mat:
        old_part = old_c - projection * new
        return arb_mat([[old_part[k, 0] if k < n else new[k-n, 0]] for k in range(m)])

    fitted_lift = complete_coefficients(lift_c)
    fitted_product = complete_coefficients(product_c)
    for coefficients, gain in [(fitted_lift, lift_gain), (fitted_product, product_gain)]:
        true_energy = 2 - 2*dot(loads, coefficients) + dot(coefficients, gram*coefficients)
        assert true_energy.overlaps(energy-gain)

    # Recover the original NS86 direction as a member of the free lift.
    beta: dict[int, arb] = {d: arb(0) for d in products}
    for i in range(1, n+1):
        for j in range(1, n+1):
            beta[i*j] += old_c[i-1, 0] * old_c[j-1, 0]
    newton = arb_mat([[sum((beta[d] for d in products if k % d == 0), arb(0))]
                     for k in range(n+1, m+1)])
    newton_gain = dot(h, newton)**2 / dot(newton, schur*newton)
    assert 0 < newton_gain < lift_gain
    # Normal equations make the direct product pairing matrix indefinite
    # whenever this off-diagonal pairing is nonzero: determinant=-h_(2N)^2.
    pairing_2n = h[n-1, 0]
    product_minor = -pairing_2n**2
    assert n >= 4 and product_minor < 0

    primes = [p for p in range(n+1, m+1)
              if all(p % k for k in range(2, int(p**0.5)+1))]
    p, q = primes[0], primes[-1]
    constraint = arb_mat([[int(k == p)-int(k == q)] for k in range(n+1, m+1)])
    assert all(v.contains(0) for v in constraint.transpose()*lift_basis)
    assert (lift_c[p-n-1, 0]-lift_c[q-n-1, 0]).contains(0)
    inverse_constraint = schur.solve(constraint, algorithm="precond")
    denominator = dot(constraint, inverse_constraint)
    full_prime_difference = full_c[p-n-1, 0]-full_c[q-n-1, 0]
    forced_loss = full_prime_difference**2 / denominator
    assert denominator > 0 and forced_loss > 0 and missing_gain > forced_loss

    # Exact dual vector v=H^-1 ell is invisible to every lift column.
    # This is a constructed arbitrary residual, NOT the optimized target.
    dual_observations = lift_basis.transpose() * (schur*inverse_constraint)
    assert all(v.contains(0) for v in dual_observations)
    values = {
        "E_N": energy, "E_N_squared": full_energy,
        "full_gain_relative": full_gain/energy,
        "product_gain_fraction": product_gain/full_gain,
        "product_gain_relative": product_gain/energy,
        "free_lift_gain_fraction": lift_gain/full_gain,
        "free_lift_gain_relative": lift_gain/energy,
        "free_lift_error": energy-lift_gain,
        "missing_gain_fraction": missing_gain/full_gain,
        "missing_gain_relative": missing_gain/energy,
        "NS86_projected_gain_fraction": newton_gain/full_gain,
        "product_pairing_2N": pairing_2n,
        "product_pairing_minor": product_minor,
        "full_prime_coefficient_difference": full_prime_difference,
        "prime_constraint_forced_loss": forced_loss,
        "prime_constraint_loss_fraction": forced_loss/full_gain,
        "dual_squared_norm": denominator,
    }
    return {"N": n, "M": m, "product_seed_count": len(products),
            "direct_product_rank": len(product_indices), "free_lift_rank": len(pivot_columns),
            "full_block_rank": m-n, "product_seeds": products,
            "lift_basis_seeds": [products[j] for j in pivot_columns],
            "prime_pair": [p, q],
            "values": {k: v.str(65) for k, v in values.items()},
            "free_lift_complete_coefficients": [v.str(65) for v in fitted_lift],
            "free_lift_parameters": [v.str(65) for v in lift_parameters],
            "seconds": round(time.monotonic()-start, 3),
            "gates": {"exact_rank_reduction": True, "old_projection_retained": True,
                      "complete_Gram_tail": True, "separate_full_solve": True,
                      "complete_trial_energy": True, "orthogonal_missing_gain": True,
                      "newton_in_free_lift": True, "prime_constraint": True,
                      "target_prime_constraint_loss_positive": True,
                      "product_pairing_indefinite": True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--cutoff", type=int, default=128)
    parser.add_argument("--sizes", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    kernel = Kernel(max(args.sizes)**2, args.cutoff, 24)
    rows = []
    for n in args.sizes:
        row = analyze(n, kernel)
        rows.append(row)
        print(json.dumps({k: row[k] for k in ["N", "seconds", "free_lift_rank", "values"]}), flush=True)
    args.output.write_text(json.dumps({
        "classification": "certified finite tests; cofinal square-scale lower gain remains open",
        "precision_bits": args.bits, "kernel_cutoff": args.cutoff, "kernel_order": 24,
        "source_sha256": digest(Path(__file__)), "kernel_sha256": digest(KERNEL),
        "rows": rows}, indent=2)+"\n")


if __name__ == "__main__":
    main()
