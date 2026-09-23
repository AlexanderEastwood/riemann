"""Complete two-precision constants and adjacent-vector Gram comparisons."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

from flint import arb, ctx

PREVIOUS=Path(__file__).resolve().parents[2]/'v159'/'ns61'
sys.path.insert(0,str(PREVIOUS))
from certify_smoothed import Kernel


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--cutoff',type=int,default=128)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=args.bits
    kernel=Kernel(4096,args.cutoff,24)
    d=kernel.k2-2*kernel.k1
    constants={'d':d,'rough_t2':kernel.k2/2-arb(3)/2,
               'rough_t0':kernel.k2/16+kernel.k1/8+arb(1)/8,
               'repaired_t2':kernel.k1-arb(3)/2,
               'repaired_t0':kernel.k1/4+arb(1)/8,
               'diagonal_arithmetic_correction':kernel.s2(1,1),
               'adjacent_repaired_limit':kernel.kappa/(kernel.k1-arb(1)/2)}
    assert all(value>0 for value in constants.values())
    assert d>arb('0.0091604') and d<arb('0.0091605')
    rows=[]
    for n in [256,1024,4096]:
        ratio=arb(n-1)/n
        actual=kernel.gram(n,n)+ratio*ratio*kernel.gram(n-1,n-1)-2*ratio*kernel.gram(n-1,n)
        h=(arb(n)/(n-1)).log()
        background=(kernel.k2-2*kernel.k1*(n-1)*h-(n-1)*h*h/2)/(n*n)
        repaired=background-d/(n*n)
        remainder=actual-background
        repaired_remainder=actual-repaired
        assert actual>0 and background>actual and repaired>0
        assert remainder<0 and repaired_remainder>0
        assert actual<kernel.kappa*h/(n*n)
        quantities={'actual':actual,'background':background,'repaired':repaired,
                    'actual_over_background':actual/background,
                    'correction_over_background':remainder/background,
                    'actual_over_repaired':actual/repaired,
                    'actual_scaled':n**3*actual,'background_scaled':n*n*background,
                    'repaired_scaled':n**3*repaired}
        rows.append({'n':n,'balls':{key:value.str(65) for key,value in quantities.items()},
                     'minimum_accuracy_bits':min(value.rel_accuracy_bits() for value in quantities.values()),
                     'gates':{'complete_actual_gram_positive':True,'rough_correction_negative':True,
                              'repaired_comparison_positive':True,'analytic_norm_budget':True}})
    report:dict[str,Any]={'classification':'certified finite constant and two-vector comparisons',
        'precision_bits':args.bits,'finite_series_cutoff':args.cutoff,'bernoulli_order':24,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'kernel_source_sha256':hashlib.sha256((PREVIOUS/'certify_smoothed.py').read_bytes()).hexdigest(),
        'constants':{key:value.str(65) for key,value in constants.items()},'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'PASS','precision_bits':args.bits,
        'ratios':[{key:row['balls'][key] for key in ['actual_over_background','actual_over_repaired']} for row in rows]}))


if __name__=='__main__':
    main()
