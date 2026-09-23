"""Finite signed/unsigned cost decomposition; no asymptotic inference."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any
from flint import arb, ctx
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'evidence/ns92_arithmetic_cost'))
from certify_cost import mobius


def run(n: int, mu: list[int]) -> dict[str, Any]:
    signed = arb(0)
    unsigned = arb(0)
    square = arb(0)
    absolute = arb(0)
    diagonal = arb(0)
    for k in range(2*n, n, -1):
        w = (arb(2*n)/k).log()/k
        signed += mu[k]*w
        unsigned += abs(mu[k])*w
        square += signed**2
        absolute += unsigned**2
        diagonal += mu[k]**2*w**2*(k-n)
    bound = arb(2).log()**2/4
    lower = n*(arb(4)/3).log()**2/9216
    assert 0 < diagonal < bound
    assert 0 < square < absolute
    if n >= 2048:
        assert absolute > lower
    if n <= 64:
        direct = arb(0)
        for m in range(n+1,2*n+1):
            for k in range(n+1,2*n+1):
                direct += mu[m]*mu[k]*(arb(2*n)/m).log()/m*(arb(2*n)/k).log()/k*(min(m,k)-n)
        assert direct.overlaps(square)
    return {'N':n,'values':{k:v.str(65) for k,v in {
        'signed_square_cost':square,'diagonal':diagonal,
        'signed_off_diagonal':square-diagonal,
        'absolute_product_majorant':absolute,
        'absolute_off_diagonal':absolute-diagonal,
        'absolute_majorant_over_N':absolute/n,
        'proved_diagonal_upper':bound,'proved_absolute_lower_for_N_ge_2048':lower,
    }.items()}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sieve-multiplier',type=int,default=1)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    mu = mobius(args.sieve_multiplier*2**17)
    rows = [run(2**j,mu) for j in range(4,17)]
    blocks=[]
    for j0 in [4,8]:
        selected=[r for r in rows if 2**j0 <= r['N'] < 2**(2*j0)]
        assert len(selected)==j0
        vals={}
        for key in ['signed_square_cost','diagonal','signed_off_diagonal','absolute_product_majorant']:
            vals[key+'_mean']= (sum((arb(r['values'][key]) for r in selected),arb(0))/j0).str(65)
        blocks.append({'first_doubling_index':j0,'last_doubling_index':2*j0-1,'values':vals})
    output={'classification':'Certified finite decomposition only; both averaged arithmetic inputs remain open',
            'bits':args.bits,'sieve_multiplier':args.sieve_multiplier,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'mobius_source_sha256':hashlib.sha256((ROOT/'evidence/ns92_arithmetic_cost/certify_cost.py').read_bytes()).hexdigest(),
            'rows':rows,'blocks':blocks}
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'bits':args.bits,'blocks':blocks,'last':rows[-1]},indent=2))

if __name__=='__main__':
    main()
