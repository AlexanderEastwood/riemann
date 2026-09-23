"""Exact cutoff selection and complete scalar tail bounds, not comparator assembly."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any
from flint import arb, ctx


def cutoff(n: int) -> tuple[int, Fraction, int]:
    harmonic = sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    constant = 48*harmonic*n**3*(n+2)
    squares = n*(n+1)*(2*n+1)//6
    threshold = 16*constant*squares/27
    low,high = 0,1
    while high**3 < threshold:
        high *= 2
    while high-low > 1:
        middle = (high+low)//2
        if middle**3 < threshold:
            low = middle
        else:
            high = middle
    assert (high-1)**3 < threshold <= high**3
    return max(n+1,high),constant,squares


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    rows: list[dict[str,Any]] = []
    for n in [16,64,256,512]:
        m,constant,squares = cutoff(n)
        c = arb(constant.numerator)/constant.denominator
        delta_squared = 4*c*squares/(27*m**3)
        assert 0 < delta_squared < arb(1)/4
        delta = delta_squared.sqrt()
        condition = ((1+delta)/(1-delta))**2
        assert 1 < condition < 9
        values = {'coefficient_constant':c,'relative_remainder_squared_upper_bound':delta_squared,
                  'relative_remainder_norm_upper_bound':delta,'projected_condition_upper_bound':condition,
                  'ten_step_gain_fraction_lower_bound':1-(arb(4)/5)**20}
        rows.append({'total_atoms':n,'cutoff':m,'cutoff_selection':'exact rational comparison and integer binary search',
                     'values':{key:value.str(65) for key,value in values.items()},'comparator_assembled':False})
    print(json.dumps({'classification':'certified scalar full-tail bounds; no comparator assembly or cofinal error estimate',
                      'precision_bits':args.bits,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'rows':rows},indent=2))

if __name__ == '__main__':
    main()
