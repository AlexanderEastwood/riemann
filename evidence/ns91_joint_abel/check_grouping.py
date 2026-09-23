"""NS91 complete first-primitive grouping certificates; no cofinal gain assertion."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

from flint import arb, ctx


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mobius(size: int) -> list[int]:
    values = [1]*(size+1)
    primes = [True]*(size+1)
    values[0] = 0
    for p in range(2, size+1):
        if primes[p]:
            for k in range(p, size+1, p):
                primes[k] = False
                values[k] *= -1
            for k in range(p*p, size+1, p*p):
                values[k] = 0
    return values


def defects(coeff: list[arb], alpha: arb, stop: int) -> list[arb]:
    delta = [arb(0) for _ in range(stop)]
    delta[1] = alpha
    for k, value in enumerate(coeff, 1):
        for m in range(k, stop, k):
            delta[m] += value
    return delta


def parameters(coeff: list[arb], alpha: arb, stop: int) -> tuple[arb, arb, arb]:
    u = alpha-sum(coeff, arb(0))/2
    v = sum((z*(arb(k)/(2*arb.pi())).log() for k, z in enumerate(coeff, 1)), arb(0))/2
    bound = sum((k*abs(z) for k, z in enumerate(coeff, 1)), arb(0))/6
    return u, u*arb(stop).log()+v, bound


def evaluate(row: dict[str, Any], reference: dict[str, Any], stop: int,
             endpoint_normalize: bool) -> dict[str, Any]:
    n = row["N"]
    assert stop > 2*n and stop & (stop-1) == 0
    c = [arb(z) for z in row["optimal_coefficients"]]
    energy = arb(row["values"]["E_N"])
    logs = [arb(0)]+[arb(k).log() for k in range(1, stop+1)]
    alpha = logs[2]
    mu = mobius(2*n)
    d = [-mu[k]*(alpha if k <= n else logs[2*n]-logs[k]) for k in range(1, 2*n+1)]
    eta = sum((z/k for k, z in enumerate(c, 1)), arb(0))
    s = -sum((z/k for k, z in enumerate(d, 1)), arb(0))
    old_endpoint_shift = n*s
    if endpoint_normalize:
        d[n-1] = -n*sum((z/k for k, z in enumerate(d, 1) if k != n), arb(0))
        assert sum((z/k for k, z in enumerate(d, 1)), arb(0)).contains(0)
        s = arb(0)  # The displayed exact coefficient rule has zero sum d_k/k.
    dr, dd = defects(c, arb(1), stop), defects(d, alpha, stop)
    u, q, bound = parameters(c, arb(1), stop)
    ud, qd, bd = parameters(d, alpha, stop)
    # Exact complete Q_R(T) and D(T), via log Gamma and digamma identities.
    endpoint_q = (logs[stop]+1)/stop
    endpoint_d = alpha*logs[stop]
    for k in range(1, 2*n+1):
        z, m = arb(stop)/k, stop//k
        atom = z-m*z.log()+arb(m+1).lgamma()
        fractional_tail = arb(m+1).digamma()-z.log()+(z-m)/z
        if k <= n:
            endpoint_q -= c[k-1]*(atom/stop+fractional_tail/k)
        endpoint_d -= d[k-1]*atom
    assert endpoint_q.overlaps((q+u)/stop+arb(0, bound/(2*arb(stop)**2)))
    assert endpoint_d.overlaps(qd+arb(0, bd/stop))
    a = sum(dr, arb(0))
    b = sum((dr[m]*logs[m] for m in range(1, stop)), arb(0))
    ad = sum(dd, arb(0))
    potential = endpoint_q
    grouped: dict[int, arb] = {}
    cell_absolute = arb(0)
    for m in range(stop-1, 0, -1):
        lo, hi = logs[m], logs[m+1]
        h, h2 = hi-lo, (hi*hi-lo*lo)/2
        w = arb(1)/(m*(m+1))
        i1 = (lo+1)/m-(hi+1)/(m+1)
        constant = potential-eta*hi-(a*(hi+1)-b)/(m+1)
        integral_q = constant+eta*((m+1)*hi-m*lo-1)+a*(h2+h)-b*h
        integral_q_over_t = constant*h+eta*h2+a*(i1+w)-b*w
        cell = s*integral_q+ad*integral_q_over_t
        if endpoint_normalize and m < n:
            assert cell.contains(0)
            cell = arb(0)  # J is identically zero on this whole interval.
        cell_absolute += abs(cell)
        scale = m.bit_length()-1
        grouped[scale] = grouped.get(scale, arb(0))+cell
        potential += -eta*h+a*i1-b*w
        a -= dr[m]
        b -= dr[m]*lo
        ad -= dd[m]
    grouped[-1] = s*(potential-eta)  # Entire interval 0<t<1.
    cell_absolute += abs(grouped[-1])
    signed = sum(grouped.values(), arb(0))
    grouped_absolute = sum((abs(z) for z in grouped.values()), arb(0))
    # A bounded primitive of J-ud is -sum n*d_n*B2({t/n})/2.
    primitive_bound = bd/2
    absolute_dyadic_tail = abs(ud)*((abs(q+u)+abs(u))/stop+bound/(4*arb(stop)**2))
    absolute_dyadic_tail += primitive_bound*(
        (5*abs(q+u)/3+8*abs(u)*alpha/9+(abs(2*q+u)+abs(u))/2)/arb(stop)**2
        +8*bound/(7*arb(stop)**3))
    lower_numerator = alpha*energy-grouped_absolute-absolute_dyadic_tail
    old = reference["directions"]["linear_log_taper"]
    numerator, cost = arb(old["numerator"]), arb(old["true_projected_cost"])
    # Comparison only: the computed bound above does not use the numerator.
    actual_tail = alpha*energy-numerator-signed
    assert abs(actual_tail) < absolute_dyadic_tail
    assert (alpha*energy-signed+arb(0, absolute_dyadic_tail)).overlaps(numerator)
    assert lower_numerator > 0
    assert lower_numerator < numerator
    guaranteed_gain = lower_numerator**2/cost
    assert guaranteed_gain < numerator**2/cost
    values = {
        "E_N": energy, "alpha_E_N": alpha*energy,
        "old_endpoint_shift": old_endpoint_shift,
        "exact_endpoint_Q": endpoint_q, "exact_endpoint_D": endpoint_d,
        "first_primitive_signed_interior": signed,
        "absolute_unit_cell_allowance": cell_absolute,
        "absolute_dyadic_interior_allowance": grouped_absolute,
        "absolute_all_dyadic_tail_bound": absolute_dyadic_tail,
        "complete_compensator_enclosure": signed+arb(0, absolute_dyadic_tail),
        "complete_numerator_enclosure": alpha*energy-signed+arb(0, absolute_dyadic_tail),
        "positive_lower_numerator": lower_numerator,
        "positive_lower_numerator_over_E": lower_numerator/energy,
        "complete_dyadic_allowance_over_E": (grouped_absolute+absolute_dyadic_tail)/energy,
        "inherited_full_projected_cost": cost,
        "inherited_numerator": numerator,
        "guaranteed_relative_gain": guaranteed_gain/energy,
        "tail_bound_over_E": absolute_dyadic_tail/energy,
    }
    return {"N": n, "endpoint_normalized": endpoint_normalize,
            "values": {k: v.str(65) for k, v in values.items()},
            "signed_dyadic_integrals_over_E": {str(k): (v/energy).str(65) for k, v in sorted(grouped.items())},
            "checks": {"positive_lower_numerator": True, "full_Gram_overlap": True,
                       "complete_tail_inside_analytic_bound": True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--stop", type=int, default=262144)
    parser.add_argument("--cutoff-replay", action="store_true")
    parser.add_argument("--endpoint-normalize", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    suffix = "cutoff-384bits" if args.cutoff_replay else f"{args.bits}bits"
    inp = args.repo/f"evidence/ns89_upper_normalization/check-{suffix}.json"
    ref_suffix = "cutoff-replay-384bits" if args.cutoff_replay else f"{args.bits}bits"
    ref = args.repo/f"evidence/v161/ns73/mobius-{ref_suffix}.json"
    source, references = json.loads(inp.read_text()), json.loads(ref.read_text())
    rows = []
    for row in source["rows"]:
        reference = next(r for r in references["rows"] if r["N"] == row["N"])
        result = evaluate(row, reference, args.stop, args.endpoint_normalize)
        rows.append(result)
        print(json.dumps({"N": row["N"], "bits": args.bits, "T": args.stop,
                          "lower_numerator_over_E": result["values"]["positive_lower_numerator_over_E"],
                          "guaranteed_relative_gain": result["values"]["guaranteed_relative_gain"]}), flush=True)
    output = {"classification": "NS91 certified finite bounds; cofinal estimate unproved",
              "precision_bits": args.bits, "physical_cutoff": args.stop,
              "endpoint_normalized": args.endpoint_normalize,
              "input_path": str(inp.relative_to(args.repo)), "input_sha256": digest(inp),
              "reference_path": str(ref.relative_to(args.repo)), "reference_sha256": digest(ref),
              "source_sha256": digest(Path(__file__)), "python_version": sys.version.split()[0], "rows": rows}
    args.output.write_text(json.dumps(output, indent=2)+"\n")


if __name__ == "__main__":
    main()
