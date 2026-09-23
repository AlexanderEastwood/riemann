"""Certified finite zero-subset constants, not error bounds at finite N."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any
from flint import acb, arb, ctx, fmpq, fmpq_mat


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    rows: list[dict[str,Any]] = []
    last = arb(0)
    sums = {q:arb(0) for q in [1,2,3]}
    for index in range(1,11):
        zero = acb.zeta_zero(index)
        assert zero.real == arb(1)/2 and zero.imag > last > -1
        assert zero.zeta().contains(0)
        height = zero.imag
        values = {f'pair_weight_q{q}':2/(height*height+arb(1)/4)**q for q in [1,2,3]}
        for q in [1,2,3]:
            sums[q] += values[f'pair_weight_q{q}']
        rows.append({'positive_zero_index':index,'real_part':zero.real.str(65),
                     'ordinate':height.str(65),'pair_weights':{k:v.str(65) for k,v in values.items()}})
        last = height
    hilbert = []
    for m in range(1,9):
        matrix = fmpq_mat([[fmpq(1,i+j+1) for j in range(m)] for i in range(m)])
        inverse = matrix.inv()
        assert inverse[0,0] == m*m
        hilbert.append({'multiplicity':m,'inverse_top_left':str(inverse[0,0]),'equals_m_squared':True})
    assert sums[2] > arb('0.000072332433')
    print(json.dumps({'classification':'certified finite zero-subset constants and exact Hilbert blocks; no finite-N error threshold',
                      'precision_bits':args.bits,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'zero_constructor':'python-flint acb.zeta_zero: certified nontrivial zeta zero enclosure',
                      'rows':rows,'partial_constants':{f'q{q}':v.str(65) for q,v in sums.items()},
                      'hilbert_blocks':hilbert,'multiplicity_weights_used':1,'both_conjugates_counted':True,
                      'omitted_terms':'nonnegative; only a lower bound from a finite subset is asserted',
                      'asymptotic_onset_N0':None,'error_upper_bound':False,'RH_proved':False},indent=2))

if __name__ == '__main__':
    main()
