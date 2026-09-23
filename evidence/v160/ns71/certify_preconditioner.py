"""Complete finite gains for a repaired-kernel selected direction, using Arb."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

PREVIOUS = Path(__file__).resolve().parents[2]/'v159'/'ns61'
sys.path.insert(0,str(PREVIOUS))
from certify_smoothed import Kernel


def block(matrix: arb_mat, start: int, stop: int) -> arb_mat:
    return arb_mat([[matrix[i,j] for j in range(start,stop)] for i in range(start,stop)])


def project(full: arb_mat, n: int, difference: arb_mat) -> tuple[arb_mat, arb_mat]:
    old=block(full,0,n)
    cross=arb_mat([[full[i,j] for j in range(n-1,2*n)] for i in range(n)])*difference
    raw=difference.transpose()*block(full,n-1,2*n)*difference
    projection=old.solve(cross,algorithm='precond')
    return raw-cross.transpose()*projection, raw


def run(n: int, kernel: Kernel) -> dict[str,Any]:
    started=time.monotonic()
    full=arb_mat([[kernel.gram(i,j) for j in range(1,2*n+1)] for i in range(1,2*n+1)])
    loads=arb_mat([[kernel.load(i)] for i in range(1,2*n+1)])
    old=block(full,0,n)
    old_load=arb_mat([[loads[i,0]] for i in range(n)])
    coeff=old.solve(old_load,algorithm='precond')
    energy=2-(old_load.transpose()*coeff)[0,0]
    next_coeff=full.solve(loads,algorithm='precond')
    next_energy=2-(loads.transpose()*next_coeff)[0,0]
    full_gain=energy-next_energy
    difference=arb_mat(n+1,n)
    for j,k in enumerate(range(n+1,2*n+1)):
        difference[j+1,j]=1
        difference[j,j]=-arb(k-1)/k
    cross=arb_mat([[full[i,j] for j in range(n-1,2*n)] for i in range(n)])*difference
    tail_load=arb_mat([[loads[i,0]] for i in range(n-1,2*n)])
    target=difference.transpose()*tail_load-cross.transpose()*coeff
    projected,raw=project(full,n,difference)
    model=arb_mat(2*n,2*n)
    for i in range(1,2*n+1):
        for j in range(1,2*n+1):
            h=abs(kernel.logs[j]-kernel.logs[i])
            model[i-1,j-1]=(2*kernel.k1+kernel.k1*h+h*h/4)/max(i,j)
    projected_model,raw_model=project(model,n,difference)
    variants:dict[str,arb_mat]={'actual_correlation':target,
                              'raw_repaired_inverse':raw_model.solve(target,algorithm='precond'),
                              'projected_repaired_inverse':projected_model.solve(target,algorithm='precond')}
    values={}
    for name,direction in variants.items():
        numerator=(target.transpose()*direction)[0,0]
        denominator=(direction.transpose()*projected*direction)[0,0]
        raw_denominator=(direction.transpose()*raw*direction)[0,0]
        model_denominator=(direction.transpose()*projected_model*direction)[0,0]
        assert numerator>0 and denominator>0 and model_denominator>0
        assert raw_denominator>denominator
        gain=numerator*numerator/denominator
        raw_gain=numerator*numerator/raw_denominator
        assert gain>0 and gain<full_gain
        values[name]={'fraction_of_full_gain':gain/full_gain,
                      'relative_gain':gain/energy,'relative_raw_lower_gain':raw_gain/energy,
                      'selected_projected_gram_ratio':denominator/model_denominator,
                      'old_projection_cost_factor':raw_denominator/denominator,
                      'numerator':numerator,'denominator':denominator}
    assert full_gain>0 and next_energy>0
    q={name:{key:value.str(65) for key,value in item.items()} for name,item in values.items()}
    return {'N':n,'seconds':round(time.monotonic()-started,3),
            'energy':energy.str(65),'full_relative_gain':(full_gain/energy).str(65),
            'directions':q,'minimum_accuracy_bits':min(v.rel_accuracy_bits() for item in values.values() for v in item.values()),
            'gates':{'complete_gram_tail':True,'certified_model_and_actual_solves':True,
                     'all_selected_energies_positive':True,'gains_below_full_projection_gain':True,
                     'complete_old_projection_retained':True}}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    parser.add_argument('--cutoff',type=int,default=128)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();ctx.prec=args.bits
    kernel=Kernel(2*max(args.sizes),args.cutoff,24)
    rows=[]
    for n in args.sizes:
        row=run(n,kernel);rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'fractions':{name:values['fraction_of_full_gain'] for name,values in row['directions'].items()}}),flush=True)
    report={'classification':'certified finite selected-direction experiment; no cofinal estimate',
            'precision_bits':args.bits,'finite_series_cutoff':args.cutoff,'bernoulli_order':24,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'kernel_source_sha256':hashlib.sha256((PREVIOUS/'certify_smoothed.py').read_bytes()).hexdigest(),
            'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
