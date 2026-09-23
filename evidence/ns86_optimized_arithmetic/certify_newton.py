"""Complete finite test of a divisor-convolution correction at size N squared.

All Gram entries include the inherited analytic infinite tail; no midpoint solves.
The local defect-squaring identity is not a full-norm contraction theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
KERNEL_PATH = HERE.parent / "v159/ns61/certify_smoothed.py"
sys.path.insert(0, str(KERNEL_PATH.parent))
from certify_smoothed import Kernel


def dot(a: arb_mat, b: arb_mat) -> arb:
    return (a.transpose() * b)[0, 0]


def correction(coefficients: list[arb]) -> tuple[list[arb], list[arb]]:
    """Return q=2c+1*c*c truncated at N^2 and the coefficient step q-c."""
    n = len(coefficients)
    m = n * n
    convolution = [arb(0) for _ in range(m + 1)]
    for i, ci in enumerate(coefficients, 1):
        for j, cj in enumerate(coefficients, 1):
            convolution[i * j] += ci * cj
    q = [arb(0) for _ in range(m + 1)]
    for k in range(1, m + 1):
        for multiple in range(k, m + 1, k):
            q[multiple] += convolution[k]
    for k, ck in enumerate(coefficients, 1):
        q[k] += 2 * ck
    step = [q[k] - (coefficients[k - 1] if k <= n else 0)
            for k in range(1, m + 1)]
    return q[1:], step


def defects(coefficients: list[arb], m: int) -> list[arb]:
    values = [arb(0) for _ in range(m + 1)]
    values[1] = arb(1)
    for k, ck in enumerate(coefficients, 1):
        for multiple in range(k, m + 1, k):
            values[multiple] += ck
    return values


def analyze(n: int, kernel: Kernel, betas: list[tuple[str, arb]]) -> dict[str, Any]:
    started = time.monotonic()
    m = n * n
    gram = arb_mat([[kernel.gram(i, j) for j in range(1, m + 1)]
                    for i in range(1, m + 1)])
    old = arb_mat([[gram[i, j] for j in range(n)] for i in range(n)])
    old_rows = arb_mat([[gram[i, j] for j in range(m)] for i in range(n)])
    families: dict[str, Any] = {}
    for label, beta in betas:
        slope = (1 - beta) / beta
        constant = (2 * beta - 1) / beta**2
        loads = arb_mat([[slope * kernel.load(k)
                         - constant * (kernel.logs[k] + 2 - arb.const_euler() + 1 / beta) / k]
                        for k in range(1, m + 1)])
        old_loads = arb_mat([[loads[i, 0]] for i in range(n)])
        fitted = old.solve(old_loads, algorithm="precond")
        full_fit = gram.solve(loads, algorithm="precond")
        c = [fitted[i, 0] for i in range(n)]
        q_values, step_values = correction(c)
        q = arb_mat([[v] for v in q_values])
        step = arb_mat([[v] for v in step_values])
        old_padded = arb_mat([[c[k] if k < n else arb(0)] for k in range(m)])
        residual_loads = loads - gram * old_padded
        energy = 2 - dot(old_loads, fitted)
        full_energy = 2 - dot(loads, full_fit)
        proposed_energy = 2 - 2 * dot(loads, q) + dot(q, gram * q)
        numerator = dot(residual_loads, step)
        raw_cost = dot(step, gram * step)
        overlap = old_rows * step
        old_component = old.solve(overlap, algorithm="precond")
        projected_cost = raw_cost - dot(overlap, old_component)
        raw_gain = numerator**2 / raw_cost
        projected_gain = numerator**2 / projected_cost
        full_gain = energy - full_energy
        assert energy > full_energy > 0
        assert raw_cost > projected_cost > 0
        assert 0 < raw_gain < projected_gain < full_gain
        assert proposed_energy > 0
        assert (proposed_energy - energy + 2 * numerator - raw_cost).contains(0)
        assert all(residual_loads[i, 0].contains(0) for i in range(n))
        before = defects(c, m + 1)
        after = defects(q_values, m + 1)
        squared = [arb(0) for _ in range(m + 2)]
        for i in range(1, m + 2):
            for j in range(1, (m + 1) // i + 1):
                squared[i * j] += before[i] * before[j]
        assert all((after[k] - squared[k]).contains(0) for k in range(1, m + 1))
        floor = (2 * beta - 1) * (1 - beta)**2 / beta**6
        assert full_energy > floor
        values = {
            "E_N": energy, "E_N_squared": full_energy,
            "full_gain_relative": full_gain / energy,
            "unit_step_energy": proposed_energy,
            "unit_step_error_ratio": proposed_energy / energy,
            "step_pairing": numerator, "raw_step_cost": raw_cost,
            "projected_step_cost": projected_cost,
            "raw_best_scalar": numerator / raw_cost,
            "projected_best_scalar": numerator / projected_cost,
            "raw_gain_fraction": raw_gain / full_gain,
            "projected_gain_fraction": projected_gain / full_gain,
            "raw_gain_relative": raw_gain / energy,
            "projected_gain_relative": projected_gain / energy,
            "positive_floor": floor,
            "first_post_cutoff_defect_difference": after[m + 1] - squared[m + 1],
        }
        families[label] = {
            "values": {key: value.str(65) for key, value in values.items()},
            "old_coefficients": [v.str(65) for v in c],
            "proposed_coefficients": [v.str(65) for v in q_values],
            "classification": ("original integer atoms" if label == "original" else
                               "NS74 altered atoms; coefficient identity only, not the original physical divisor identity"),
            "gates": {"all_solves_keep_balls": True, "complete_Gram_tail": True,
                      "normal_equations": True, "complete_step_energy_identity": True,
                      "defect_squaring_through_N_squared": True,
                      "unit_step_decreases_error": bool(proposed_energy < energy),
                      "optimized_direction_below_full_gain": True},
        }
    return {"N": n, "M": m, "seconds": round(time.monotonic() - started, 3),
            "families": families}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--sizes", type=int, nargs="+", required=True)
    parser.add_argument("--cutoff", type=int, default=128)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert min(args.sizes) >= 2
    ctx.prec = args.bits
    kernel = Kernel(max(args.sizes)**2, args.cutoff, 24)
    betas = [("original", arb(1) / 2),
             ("altered_beta_half_plus_1e-6", arb(1) / 2 + arb(1) / 1000000)]
    rows = []
    for n in args.sizes:
        row = analyze(n, kernel, betas)
        rows.append(row)
        print(json.dumps({"N": n, "M": n*n, "bits": args.bits,
                          "seconds": row["seconds"],
                          "original": row["families"]["original"]["values"]}), flush=True)
    report = {"classification": "certified finite arithmetic correction; no cofinal gain bound",
              "precision_bits": args.bits, "kernel_cutoff": args.cutoff,
              "kernel_order": 24,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "kernel_sha256": hashlib.sha256(KERNEL_PATH.read_bytes()).hexdigest(),
              "rows": rows}
    args.output.write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
