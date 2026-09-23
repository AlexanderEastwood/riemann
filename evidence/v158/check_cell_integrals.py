"""Independent positive-cell integral checks of selected cotangent Gram entries."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from flint import arb, ctx

from nb_certify import build_arb


def check_entry(m: int, n: int, cutoff: int, logarithms: list[arb], exact: arb) -> dict[str, Any]:
    # The tail is between zero and 1/cutoff because both fractional parts lie in [0,1].
    partial = arb(1)/(m*n)
    for j in range(1,cutoff):
        a, b = j//m,j//n
        partial += arb(1)/(m*n)-(arb(b)/m+arb(a)/n)*logarithms[j]+arb(a*b)/(j*(j+1))
    lower_margin = exact-partial
    upper_margin = partial+arb(1)/cutoff-exact
    assert lower_margin > 0 and upper_margin > 0,(m,n)
    return {'m':m,'n':n,'partial_integral':partial.str(35),
            'tail_upper_bound':(arb(1)/cutoff).str(35),'cotangent_value':exact.str(35),
            'both_strict_containment_gates':True,
            'minimum_margin_accuracy_bits':min(lower_margin.rel_accuracy_bits(),upper_margin.rel_accuracy_bits())}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=args.bits
    cutoff=65536
    pairs=[(1,1),(1,2),(2,3),(7,11),(64,65),(127,256),(256,512)]
    gram,_=build_arb(512)
    logarithms=[arb(0)]+[(1+arb(1)/j).log() for j in range(1,cutoff)]
    rows=[check_entry(m,n,cutoff,logarithms,gram[m-1,n-1]) for m,n in pairs]
    result={'classification':'certified finite formula cross-check, not convergence',
            'precision_bits':args.bits,'cutoff':cutoff,'rows':rows,
            'cell_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'gram_source_sha256':hashlib.sha256(Path(__file__).with_name('nb_certify.py').read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(rows)} positive-cell integral and complete-tail comparisons at {args.bits} bits')


if __name__=='__main__':
    main()
