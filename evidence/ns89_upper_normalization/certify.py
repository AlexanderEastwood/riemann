"""Complete constructive upper certificates with an exactly vanishing exterior.

Ball solves enclose the optimal repair. Rounding only proposes exact rational
coefficients; their full energy is certified again, independently of the solve.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
KERNEL = HERE.parent / "v159/ns61/certify_smoothed.py"
sys.path.insert(0, str(KERNEL.parent))
from certify_smoothed import Kernel, dot


def ball(value: Fraction) -> arb:
    return arb(value.numerator) / value.denominator


def proposed_dyadic(value: arb, scale: int) -> Fraction:
    integer = (value.mid()*scale).floor().unique_fmpz()
    if integer is None:
        raise ArithmeticError("Proposal did not determine an integer")
    return Fraction(int(integer),scale)


def analyze(n: int, kernel: Kernel) -> dict[str, Any]:
    start = time.monotonic()
    gram = arb_mat([[kernel.gram(i,j) for j in range(1,n+1)] for i in range(1,n+1)])
    loads = arb_mat([[kernel.load(i)] for i in range(1,n+1)])
    v = arb_mat([[arb(1)/i] for i in range(1,n+1)])
    c = gram.solve(loads, algorithm="precond")
    inverse_v = gram.solve(v, algorithm="precond")
    energy = 2-dot(loads,c)
    eta = dot(v,c)
    q = dot(v,inverse_v)
    repaired = c-inverse_v*(eta/q)
    cost = eta**2/q
    optimal_upper = energy+cost
    direct_optimal_upper = 2-2*dot(loads,repaired)+dot(repaired,gram*repaired)
    assert 0 < q < 1 and q > 1/gram[0,0]
    assert (direct_optimal_upper-optimal_upper).contains(0)
    assert dot(v,repaired).contains(0)
    assert eta**2 < energy*(1-q)
    assert optimal_upper < energy/q < gram[0,0]*energy
    assert all((gram*repaired-loads+v*(eta/q))[i,0].contains(0) for i in range(n))

    # This is a proposal, not a rounded inverse in a proof: exact rationals
    # are independently substituted into the original full quadratic form.
    scale = 2**64
    tail = [proposed_dyadic(repaired[i,0],scale) for i in range(1,n)]
    rational_coefficients = [-sum((a/i for i,a in enumerate(tail,2)),Fraction(0))]+tail
    assert sum((a/i for i,a in enumerate(rational_coefficients,1)),Fraction(0)) == 0
    trial = arb_mat([[ball(a)] for a in rational_coefficients])
    upper = 2-2*dot(loads,trial)+dot(trial,gram*trial)
    rounding_energy = dot(trial-repaired,gram*(trial-repaired))
    assert (upper-optimal_upper-rounding_energy).contains(0)
    assert 0 < rounding_energy < arb("1e-30")
    assert upper > 0
    values = {"E_N":energy,"eta":eta,"tail_projection_norm_squared":q,
              "optimal_normalization_cost":cost,"normalized_optimal_error":optimal_upper,
              "relative_normalization_cost":cost/energy,
              "rate_transfer_factor":1/q,"uniform_rate_transfer_factor":gram[0,0],
              "explicit_trial_error":upper,"rounding_energy":rounding_energy,
              "scaled_log_error":upper*arb(n).log()}
    return {"N":n,"seconds":round(time.monotonic()-start,3),
            "values":{k:x.str(65) for k,x in values.items()},
            "rational_coefficients":[str(a) for a in rational_coefficients],
            "optimal_coefficients":[c[i,0].str(65) for i in range(n)],
            "gates":{"full_Gram":True,"constrained_normal_equations":True,
                     "sharp_rate_transfer":True,"exact_rational_zero_tail":True,
                     "rational_trial_full_energy":True,"rounding_energy_below_1e_minus_30":True}}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--bits",type=int,required=True)
    parser.add_argument("--cutoff",type=int,default=128)
    parser.add_argument("--sizes",type=int,nargs="+",default=[16,64,256])
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();ctx.prec=args.bits
    kernel=Kernel(max(args.sizes),args.cutoff,24)
    rows=[]
    for n in args.sizes:
        row=analyze(n,kernel);rows.append(row)
        print(json.dumps({"N":n,"seconds":row["seconds"],"values":row["values"]}),flush=True)
    args.output.write_text(json.dumps({
        "classification":"Certified finite constructive upper bounds and rate-transfer identity; no cofinal decay estimate",
        "precision_bits":args.bits,"kernel_cutoff":args.cutoff,"kernel_order":24,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "kernel_sha256":hashlib.sha256(KERNEL.read_bytes()).hexdigest(),"rows":rows},indent=2)+"\n")


if __name__ == "__main__":
    main()
