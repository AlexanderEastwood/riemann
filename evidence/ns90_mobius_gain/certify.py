"""Test the signed Mobius gain identity, keeping the full physical tail.

The original optimized interval coefficients and projected costs are reused
from NS89 and NS73; this is a new arithmetic decomposition, not a new solve.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SIEVE = ROOT / "evidence/v160/ns67/certify_cells.py"
sys.path.insert(0, str(SIEVE.parent))
from certify_cells import mobius_sieve


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def defects(c: list[arb], alpha: arb, stop: int) -> list[arb]:
    out = [arb(0) for _ in range(stop)]
    out[1] = alpha
    for n, value in enumerate(c, 1):
        for k in range(n, stop, n):
            out[k] += value
    return out


def tail_data(c: list[arb], alpha: arb, stop: int) -> tuple[arb, arb, arb, arb]:
    u = alpha - sum(c, arb(0))/2
    v = sum((value*(arb(n)/(2*arb.pi())).log()
             for n, value in enumerate(c, 1)), arb(0))/2
    bound = sum((n*abs(value) for n, value in enumerate(c, 1)), arb(0))/6
    q = u*arb(stop).log() + v
    main_energy = (q*q+2*u*q+2*u*u)/stop
    rem_energy = bound*bound/(3*arb(stop)**3)
    return u, q, main_energy, rem_energy


def evaluate(row: dict[str, Any], reference: dict[str, Any], stop: int) -> dict[str, Any]:
    n = row["N"]
    assert stop > 2*n
    c = [arb(s) for s in row["optimal_coefficients"]]
    energy = arb(row["values"]["E_N"])
    prior = reference["directions"]["linear_log_taper"]
    numerator, cost = arb(prior["numerator"]), arb(prior["true_projected_cost"])
    mu = mobius_sieve(2*n)
    log2 = arb(2).log()
    logs = [arb(0)] + [arb(k).log() for k in range(1, stop+1)]
    d = [-mu[k]*(log2 if k <= n else logs[2*n]-logs[k]) for k in range(1, 2*n+1)]
    eta = sum((value/k for k, value in enumerate(c, 1)), arb(0))
    s = -sum((value/k for k, value in enumerate(d, 1)), arb(0))
    dr = defects(c, arb(1), stop)
    dd = defects(d, log2, stop)
    for k in range(1, n+1):
        assert dd[k].contains(0)
        # Replace by its exact algebraic value, not by an interval midpoint.
        dd[k] = arb(0)
    for k in range(n+1, 2*n+1):
        exact = mu[k]*(logs[k]-logs[n])
        assert dd[k].overlaps(exact)
        dd[k] = exact
    j0, j1 = [arb(0)], [arb(0)]
    a, b, ad, bd = arb(0), arb(0), arb(0), arb(0)
    moment = -eta
    cell_pairing = -eta*s  # 0<t<1, with weight dt/t^2.
    for m in range(1, stop):
        lo, hi = logs[m], logs[m+1]
        a += dr[m]
        b += dr[m]*lo
        ad += dd[m]
        bd += dd[m]*lo
        w = arb(1)/(m*(m+1))
        i1 = (lo+1)/m-(hi+1)/(m+1)
        i2 = (lo*lo+2*lo+2)/m-(hi*hi+2*hi+2)/(m+1)
        h, h2 = hi-lo, (hi*hi-lo*lo)/2
        j0.append(-eta*h+a*i1-b*w)
        j1.append(-eta*h2+a*i2-b*i1)
        moment += -eta+a*h2-b*h
        cell_pairing += -eta*s + (-eta*ad+s*a)*h2 + (eta*bd-s*b)*h
        cell_pairing += a*ad*i2-(a*bd+b*ad)*i1+b*bd*w
    acc0, acc1 = arb(0), arb(0)
    local, later, absolute = arb(0), arb(0), arb(0)
    for m in range(stop-1, n, -1):
        acc0 += j0[m]
        acc1 += j1[m]
        term = dd[m]*(acc1-logs[m]*acc0)
        absolute += abs(term)
        if m <= 2*n:
            local += term
        else:
            later += term
    exterior = s*moment
    assert cell_pairing.overlaps(exterior+local+later)
    ur, qr, mr, vr = tail_data(c, arb(1), stop)
    ud, qd, md, vd = tail_data(d, log2, stop)
    tail_main = (qr*qd+ur*qd+ud*qr+2*ur*ud)/stop
    tail_radius = (mr*vd).sqrt()+(md*vr).sqrt()+(vr*vd).sqrt()
    tail = tail_main+arb(0, tail_radius)
    complete = log2*energy-exterior-local-later-tail
    assert complete.overlaps(numerator), (n, complete, numerator)
    assert complete > 0
    # This is a valid, deliberately elementary lower bound, not a sign guess.
    triangle = log2*energy-abs(exterior)-absolute-abs(tail)
    values = {
        "E_N": energy, "log2_times_energy": log2*energy,
        "exterior_pairing": exterior, "divisor_pairing_N_to_2N": local,
        "divisor_pairing_2N_to_T": later, "absolute_divisor_allowance": absolute,
        "tail_main": tail_main, "tail_radius": tail_radius,
        "complete_tail": tail, "complete_compensator": exterior+local+later+tail,
        "complete_numerator": complete, "inherited_numerator": numerator,
        "inherited_projected_cost": cost, "numerator_over_E_N": complete/energy,
        "compensator_over_E_N": (exterior+local+later+tail)/energy,
        "triangle_lower_numerator": triangle,
        "triangle_lower_over_E_N": triangle/energy,
        "omit_divisor_forcing_numerator": log2*energy-exterior-tail,
        "physical_cell_pairing": cell_pairing,
    }
    return {"N": n, "values": {key: value.str(60) for key, value in values.items()},
            "gates": {"complete_numerator_positive": bool(complete > 0),
                      "full_Gram_numerator_overlap": True,
                      "direct_cell_pairing_overlap": True,
                      "triangle_bound_vacuous": bool(triangle < 0)}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--stop", type=int, default=262144)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--sizes", type=int, nargs="+", default=[16, 256])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    source = json.loads(args.input.read_text())
    reference = json.loads(args.reference.read_text())
    rows = []
    for row in source["rows"]:
        if row["N"] not in args.sizes:
            continue
        ref = next(r for r in reference["rows"] if r["N"] == row["N"])
        result = evaluate(row, ref, args.stop)
        rows.append(result)
        print(json.dumps(result), flush=True)
    assert {r["N"] for r in rows} == set(args.sizes)
    result = {"classification": "Certified finite signed numerator decomposition; no cofinal lower gain",
              "precision_bits": args.bits, "cell_stop": args.stop,
              "input": str(args.input.relative_to(ROOT) if args.input.is_absolute() else args.input),
              "reference": str(args.reference.relative_to(ROOT) if args.reference.is_absolute() else args.reference),
              "input_sha256": digest(args.input), "reference_sha256": digest(args.reference),
              "source_sha256": digest(Path(__file__)), "sieve_sha256": digest(SIEVE), "rows": rows}
    args.output.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
