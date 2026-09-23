"""Rigorous finite NB block enclosures; no asymptotic or RH assertion.

All matrix entries and solves use Arb balls. The Vasyunin formula is the
scaled form of Baez-Duarte--Balazard--Landreau--Saias, math/0306251,
Proposition 89. Positive definiteness is the analytic finite-independence
result in manuscript Proposition ns53-nb-entries.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path
from typing import Any

from flint import arb, arb_mat, ctx


def build_arb(max_index: int) -> tuple[arb_mat, arb_mat]:
    pi = arb.pi()
    gamma = arb.const_euler()
    kappa = (2*pi).log()-gamma
    cots: dict[int, list[arb]] = {
        k: [(arb(m)/k).cot_pi() for m in range(1, (k+1)//2)]
        for k in range(2, max_index+1)
    }
    cache: dict[tuple[int, int], arb] = {}

    def vasyunin(h: int, k: int) -> arb:
        if k == 1:
            return arb(0)
        h %= k
        key = (h, k)
        if key not in cache:
            total = arb(0)
            for m, cotangent in enumerate(cots[k], start=1):
                residue = (m*h) % k
                if residue:
                    total += (2*residue-k)*cotangent
            cache[key] = total/k
        return cache[key]

    gram = arb_mat(max_index, max_index)
    for m in range(1, max_index+1):
        for n in range(m, max_index+1):
            divisor = math.gcd(m,n)
            h, k = m//divisor, n//divisor
            value = (
                kappa/2*(arb(1)/m+arb(1)/n)
                +arb(n-m)/(2*m*n)*(arb(m)/n).log()
                -pi*divisor/(2*m*n)*(vasyunin(h,k)+vasyunin(k,h))
            )
            gram[m-1,n-1] = gram[n-1,m-1] = value
    loads = arb_mat(max_index,1)
    for n in range(1,max_index+1):
        loads[n-1,0] = (arb(n).log()+1-gamma)/n
    return gram,loads


def submatrix(matrix: arb_mat, row0: int, row1: int, col0: int, col1: int) -> arb_mat:
    return arb_mat([[matrix[i,j] for j in range(col0,col1)] for i in range(row0,row1)])


def dot(first: arb_mat, second: arb_mat) -> arb:
    return (first.transpose()*second)[0,0]


def trace(matrix: arb_mat) -> arb:
    return sum((matrix[i,i] for i in range(matrix.nrows())),arb(0))


def mobius_values(limit: int) -> list[int]:
    values = [1]*(limit+1)
    prime = [True]*(limit+1)
    for p in range(2,limit+1):
        if prime[p]:
            for multiple in range(p,limit+1,p):
                values[multiple] *= -1
                prime[multiple] = False
            for multiple in range(p*p,limit+1,p*p):
                values[multiple] = 0
    values[0] = 0
    return values


def difference_data(gram: arb_mat, size: int) -> tuple[arb_mat, arb_mat, arb]:
    """Keep the old rho_N term in the raw difference Gram."""
    transform = arb_mat(size,size)
    raw_map = arb_mat(size+1,size)
    budget = arb(0)
    harmonic = sum((arb(1)/k for k in range(1,size)),arb(0))
    for j,n in enumerate(range(size+1,2*size+1)):
        harmonic += arb(1)/(n-1)
        budget += harmonic/(n*n)
        transform[j,j] = 1
        raw_map[j+1,j] = 1
        raw_map[j,j] = -arb(n-1)/n
        if j:
            transform[j-1,j] = -arb(n-1)/n
    raw_gram = raw_map.transpose()*submatrix(gram,size-1,2*size,size-1,2*size)*raw_map
    return transform,raw_gram,budget


def certify_block(gram: arb_mat, loads: arb_mat, size: int) -> dict[str, Any]:
    old = submatrix(gram,0,size,0,size)
    cross = submatrix(gram,0,size,size,2*size)
    new = submatrix(gram,size,2*size,size,2*size)
    old_load = submatrix(loads,0,size,0,1)
    block_load = submatrix(loads,size,2*size,0,1)
    coefficients = old.solve(old_load)
    h = block_load-cross.transpose()*coefficients
    schur = new-cross.transpose()*old.solve(cross)
    energy = 1-dot(old_load,coefficients)
    optimal_direction = schur.solve(h)
    gain = dot(h,optimal_direction)
    full_gram = submatrix(gram,0,2*size,0,2*size)
    full_load = submatrix(loads,0,2*size,0,1)
    next_energy = 1-dot(full_load,full_gram.solve(full_load))
    norm_h2 = dot(h,h)
    raw_trace, projected_trace = trace(new),trace(schur)
    mu = mobius_values(2*size)
    mobius = arb_mat([[-mu[n]] for n in range(size+1,2*size+1)])
    tapered = arb_mat([[-mu[n]*(arb(2*size)/n).log()] for n in range(size+1,2*size+1)])
    transform,raw_difference_gram,difference_budget = difference_data(gram,size)
    g = transform.transpose()*h
    difference_schur = transform.transpose()*schur*transform
    norm_g2 = dot(g,g)
    difference_trace = trace(difference_schur)
    difference_gain = dot(g,difference_schur.solve(g))
    assert (difference_gain-gain).contains(0)
    assert trace(raw_difference_gram) < difference_budget

    def direction_gain(direction: arb_mat) -> arb:
        denominator = dot(direction,schur*direction)
        assert denominator > 0, 'Unresolved positive direction norm'
        return dot(h,direction)**2/denominator

    quantities = {
        'E_N':energy,'E_M':next_energy,'gain':gain,'gain_relative':gain/energy,
        'h_norm2':norm_h2,'raw_trace':raw_trace,'projected_trace':projected_trace,
        'raw_trace_relative':norm_h2/raw_trace/energy,
        'projected_trace_relative':norm_h2/projected_trace/energy,
        'h_direction_relative':direction_gain(h)/energy,
        'mobius_direction_relative':direction_gain(mobius)/energy,
        'tapered_mobius_relative':direction_gain(tapered)/energy,
        'raw_bound_fraction_of_gain':norm_h2/raw_trace/gain,
        'projected_bound_fraction_of_gain':norm_h2/projected_trace/gain,
        'j_times_raw_relative':arb(size).log()/arb(2).log()*norm_h2/raw_trace/energy,
        'difference_norm2':norm_g2,
        'difference_budget':difference_budget,
        'difference_raw_trace':trace(raw_difference_gram),
        'difference_projected_trace':difference_trace,
        'difference_budget_relative':norm_g2/difference_budget/energy,
        'difference_trace_relative':norm_g2/difference_trace/energy,
        'difference_direction_relative':dot(g,g)**2/dot(g,difference_schur*g)/energy,
        'difference_bound_fraction_of_gain':norm_g2/difference_budget/gain,
    }
    for name,value in quantities.items():
        assert value > 0, (name,value)
        assert value.rel_accuracy_bits() >= 80, (name,value.rel_accuracy_bits())
    difference = gain-(energy-next_energy)
    assert difference.contains(0), difference
    old_residual = old*coefficients-old_load
    schur_residual = schur*optimal_direction-h
    assert all(old_residual[i,0].contains(0) for i in range(size))
    assert all(schur_residual[i,0].contains(0) for i in range(size))
    gates = {
        'exact_gain_exceeds_raw_bound': bool(gain > norm_h2/raw_trace),
        'exact_gain_exceeds_projected_bound': bool(gain > norm_h2/projected_trace),
        'raw_bound_below_one_percent_of_gain': bool(norm_h2/raw_trace < gain/100),
        'raw_bound_below_one_400th_of_gain': bool(norm_h2/raw_trace < gain/400),
        'difference_budget_bound_above_raw_trace_bound': bool(norm_g2/difference_budget > norm_h2/raw_trace),
        'difference_budget_bound_below_raw_trace_bound': bool(norm_g2/difference_budget < norm_h2/raw_trace),
    }
    return {'N':size,'M':2*size,'quantities':{k:v.str(45) for k,v in quantities.items()},
            'minimum_accuracy_bits':min(v.rel_accuracy_bits() for v in quantities.values()),
            'gain_identity_difference':difference.str(12),
            'difference_gain_identity_difference':(difference_gain-gain).str(12),
            'solve_residuals_contain_zero':True,'gates':gates}


def certify_adjacent_norms(gram: arb_mat, limit: int) -> dict[str, Any]:
    harmonic = arb(0)
    margins: list[arb] = []
    for n in range(2,limit+1):
        harmonic += arb(1)/(n-1)
        ratio = arb(n-1)/n
        actual = gram[n-1,n-1]+ratio**2*gram[n-2,n-2]-2*ratio*gram[n-2,n-1]
        lower = harmonic/n**2-arb(n-1)/n**3
        upper = harmonic/n**2
        assert actual > lower and actual < upper, n
        margins.extend([actual-lower,upper-actual])
    return {'n_min':2,'n_max':limit,'strict_lower_and_upper_gates':True,
            'minimum_margin_accuracy_bits':min(v.rel_accuracy_bits() for v in margins)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--max-index',type=int,default=256)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    start = time.monotonic()
    gram,loads = build_arb(args.max_index)
    adjacent_validation = certify_adjacent_norms(gram,args.max_index)
    print(f'Built {args.max_index} entries per side at {args.bits} bits in {time.monotonic()-start:.2f}s',flush=True)
    rows=[]
    size=4
    while 2*size<=args.max_index:
        row=certify_block(gram,loads,size)
        rows.append(row)
        print(size,{k:row['quantities'][k] for k in ['gain_relative','raw_trace_relative','h_direction_relative','mobius_direction_relative','tapered_mobius_relative']},flush=True)
        size *= 2
    result={'classification':'certified finite computation; no asymptotic conclusion','precision_bits':args.bits,
            'max_index':args.max_index,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.monotonic()-start,'adjacent_norm_validation':adjacent_validation,'rows':rows}
    args.output.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
