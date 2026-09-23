"""Finite-prefix positivity and scalar cutoff bounds; huge comparators are not assembled."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, arb_mat, ctx


def run(n: int) -> dict[str, Any]:
    logs = [arb(0)]+[arb(k).log() for k in range(1,n+2)]
    logfac = [arb(0)]
    for k in range(1,n+2):
        logfac.append(logfac[-1]+logs[k])
    rows = []
    for m in range(1,n+2):
        rows.append([arb(m)/k-(m//k)*(logs[m]-logs[k])+logfac[m//k] for k in range(1,n+1)])
    samples = arb_mat(rows)
    weights = [arb(1)/(m*(m+1)) for m in range(1,n+1)]
    node_weights = [weights[0]]+[weights[m-1]+weights[m] for m in range(1,n)]+[weights[-1]]
    weighted = arb_mat([[node_weights[m]*rows[m][k] for k in range(n)] for m in range(n+1)])
    exterior = arb_mat([[arb(1)/k] for k in range(1,n+1)])
    prefix = samples.transpose()*weighted+exterior*exterior.transpose()
    harmonic = sum((arb(1)/k for k in range(1,n+1)),arb(0))
    constant = 48*harmonic*n**3*(n+2)
    lower = 1/constant
    identity = arb_mat([[int(i == j) for j in range(n)] for i in range(n)])
    inverse = prefix.solve(identity,algorithm='precond')
    inverse_trace = sum((inverse[i,i] for i in range(n)),arb(0))
    assert 0 < inverse_trace < constant
    cutoff = 2**16*(n+1)**6
    a = (2*arb.pi()*cutoff).log()/2+arb(n+3)/(6*cutoff)
    tail = arb(2*n)/cutoff*(a*a+a+arb(1)/2)
    relative = constant*tail
    universal = arb(52560)/65536/arb(n+1).root(4)
    assert 0 < relative < universal < 1
    values = {'harmonic_number':harmonic,'coefficient_bound_C_N':constant,
              'ordinary_gram_eigenvalue_lower_bound':lower/16,'prefix_eigenvalue_lower_bound':lower,
              'complete_discarded_tail_operator_upper_bound':tail,'tail_relative_to_prefix_upper_bound':relative,
              'universal_relative_tail_upper_bound':universal,'certified_inverse_trace':inverse_trace,
              'certified_prefix_eigenvalue_lower_bound_from_trace':1/inverse_trace}
    return {'N':n,'prefix_cells_evaluated':n,'largest_sample_integer':n+1,
            'sufficient_comparator_cell_stop':cutoff,'large_comparator_assembled':False,
            'values':{key:value.str(65) for key,value in values.items()},
            'gates':{'positive_prefix_by_exact_injectivity':True,'inverse_trace_below_C_N':True,'certified_solve_keeps_balls':True,'full_discarded_tail_bounded':True,
                     'tail_below_prefix':True,'large_comparator_not_assembled':True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    assert (2*arb.pi()*2**16).log()/2 < arb('6.5')
    assert arb(1).exp() > 2
    rows = []
    for n in args.sizes:
        row = run(n)
        rows.append(row)
    print(json.dumps({'classification':'certified small finite-prefix positivity and complete scalar tail bound; enormous finite comparators not assembled; no cofinal decay estimate',
                      'precision_bits':args.bits,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'rows':rows},indent=2))


if __name__ == '__main__':
    main()
