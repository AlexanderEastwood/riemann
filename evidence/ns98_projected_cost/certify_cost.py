"""Complete projected-cost decomposition; finite tests, not a cofinal bound."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

EVIDENCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVIDENCE / "v159/ns61"))
from certify_smoothed import Kernel, dot, mobius, sub


def run(size: int, kernel: Kernel) -> dict[str, Any]:
    started = time.monotonic()
    full = arb_mat([[kernel.gram(i, j) for j in range(1, 2*size+1)]
                    for i in range(1, 2*size+1)])
    old = sub(full, 0, size, 0, size)
    cross = sub(full, 0, size, size, 2*size)
    new = sub(full, size, 2*size, size, 2*size)
    fit = old.solve(cross, algorithm="precond")
    residual = old*fit-cross
    assert all(residual[i, j].contains(0) for i in range(size) for j in range(size))
    removed = cross.transpose()*fit
    projected = new-removed
    weights = arb_mat([[-mobius(n)*(kernel.logs[2*size]-kernel.logs[n])]
                       for n in range(size+1, 2*size+1)])
    raw_cost = dot(weights, new*weights)
    removed_cost = dot(weights, removed*weights)
    cost = dot(weights, projected*weights)
    raw_diagonal = sum((weights[i, 0]**2*new[i, i] for i in range(size)), arb(0))
    diagonal = sum((weights[i, 0]**2*projected[i, i] for i in range(size)), arb(0))
    off_diagonal = 2*sum((weights[i, 0]*weights[j, 0]*projected[i, j]
                         for i in range(size) for j in range(i+1, size)), arb(0))
    assert (cost-raw_cost+removed_cost).contains(0)
    assert (cost-diagonal-off_diagonal).contains(0)
    assert cost > 0 and removed_cost > 0 and diagonal > 0
    assert all(projected[i, i] > 0 for i in range(size))
    alpha = arb(2).log()
    # ||a_1||^2 <= ||J||^2 ||rho_1||^2 = 4*kappa; no fitted constants.
    diagonal_upper = 4*kernel.kappa*alpha**3
    assert diagonal < raw_diagonal and raw_diagonal < diagonal_upper
    endpoint = arb_mat(2*size, 1)
    for i in range(size):
        endpoint[size+i, 0] = weights[i, 0]
    endpoint[size-1, 0] = -size*sum((weights[i, 0]/(size+i+1)
                                                  for i in range(size)), arb(0))
    endpoint_cost = dot(endpoint, full*endpoint)
    endpoint_pairing = sub(full, 0, size, 0, 2*size)*endpoint
    endpoint_fit = old.solve(endpoint_pairing, algorithm="precond")
    endpoint_removed = dot(endpoint_pairing, endpoint_fit)
    assert (endpoint_cost-endpoint_removed-cost).contains(0)
    # Replay the actual correction in the full Gram, with all cross terms.
    correction = arb_mat(2*size, 1)
    old_coeff = -fit*weights
    for i in range(size):
        correction[i, 0] = old_coeff[i, 0]
        correction[size+i, 0] = weights[i, 0]
    assert (dot(correction, full*correction)-cost).contains(0)
    values = {"raw_cost": raw_cost, "removed_old_cost": removed_cost,
              "projected_cost": cost, "raw_diagonal": raw_diagonal,
              "projected_diagonal": diagonal, "projected_signed_off_diagonal": off_diagonal,
              "cost_over_projected_diagonal": cost/diagonal,
              "uniform_diagonal_upper": diagonal_upper,
              "endpoint_cost": endpoint_cost, "endpoint_removed_old_cost": endpoint_removed}
    return {"N": size, "seconds": round(time.monotonic()-started, 3),
            "values": {key: value.str(60) for key, value in values.items()},
            "off_diagonal_sign": "positive" if off_diagonal > 0 else "negative" if off_diagonal < 0 else "unresolved",
            "minimum_accuracy_bits": min(value.rel_accuracy_bits() for value in values.values()),
            "gates": {"full_tail_in_Gram": True, "old_normal_equation_residuals": True,
                      "retained_projection_subtraction": True, "direct_full_correction_cost": True,
                      "independent_off_diagonal_sum": True, "endpoint_correction_invariance": True,
                      "uniform_diagonal_bound": True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--sizes", type=int, nargs="+", required=True)
    parser.add_argument("--cutoff", type=int, default=128)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    kernel = Kernel(2*max(args.sizes), args.cutoff, 24)
    rows = []
    for size in args.sizes:
        row = run(size, kernel)
        rows.append(row)
        print(json.dumps({"N": size, "bits": args.bits, "sign": row["off_diagonal_sign"],
                          "ratio": row["values"]["cost_over_projected_diagonal"],
                          "seconds": row["seconds"]}), flush=True)
    report = {"classification": "Certified finite projected-cost decomposition; no averaged or cofinal bound",
              "precision_bits": args.bits, "series_cutoff": args.cutoff, "bernoulli_order": 24,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "kernel_sha256": hashlib.sha256((EVIDENCE/"v159/ns61/certify_smoothed.py").read_bytes()).hexdigest(),
              "rows": rows}
    args.output.write_text(json.dumps(report, indent=2)+"\n")


if __name__ == "__main__":
    main()
