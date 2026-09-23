"""Complete finite arithmetic gains for a local spline-curvature direction."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

PRIOR = Path(__file__).resolve().parents[2]/'v160'/'ns71'
KERNEL = Path(__file__).resolve().parents[2]/'v159'/'ns61'
sys.path.insert(0,str(PRIOR));sys.path.insert(0,str(KERNEL))
from certify_preconditioner import block, project
from certify_smoothed import Kernel


def tridiagonal(diagonal: list[arb], off: list[arb], rhs: list[arb]) -> list[arb]:
    pivots=[diagonal[0]];forward=[rhs[0]];factors=[]
    assert pivots[0]>0
    for i in range(1,len(diagonal)):
        factor=off[i-1]/pivots[i-1]
        factors.append(factor)
        pivots.append(diagonal[i]-factor*off[i-1])
        forward.append(rhs[i]-factor*forward[i-1])
        assert pivots[-1]>0
    result=[x/d for x,d in zip(forward,pivots)]
    for i in range(len(result)-2,-1,-1):
        result[i]-=factors[i]*result[i+1]
    for i,value in enumerate(result):
        residual=diagonal[i]*value-rhs[i]
        if i:residual+=off[i-1]*result[i-1]
        if i+1<len(result):residual+=off[i]*result[i+1]
        assert residual.contains(0)
    return result


def adjoint(n: int, h: list[arb], dual: list[arb]) -> list[arb]:
    values=[arb(0) for _ in range(2*n)]
    for j,z in enumerate(dual):
        values[j]+=z/h[j]
        values[j+1]-=z*(1/h[j]+1/h[j+1])
        values[j+2]+=z/h[j+1]
    result=[arb(0) for _ in range(n)]
    suffix=arb(0)
    for k in range(2*n,n,-1):
        suffix+=values[k-1]/arb(k).sqrt()
        result[k-n-1]=k*suffix
    return result


def run(n: int, kernel: Kernel) -> dict[str,Any]:
    started=time.monotonic()
    full=arb_mat([[kernel.gram(i,j) for j in range(1,2*n+1)] for i in range(1,2*n+1)])
    loads=arb_mat([[kernel.load(i)] for i in range(1,2*n+1)])
    old=block(full,0,n);old_load=arb_mat([[loads[i,0]] for i in range(n)])
    coeff=old.solve(old_load,algorithm='precond')
    energy=2-(old_load.transpose()*coeff)[0,0]
    next_coeff=full.solve(loads,algorithm='precond')
    full_gain=energy-2+(loads.transpose()*next_coeff)[0,0]
    assert energy>full_gain and full_gain>0
    difference=arb_mat(n+1,n)
    for j,k in enumerate(range(n+1,2*n+1)):
        difference[j+1,j]=1;difference[j,j]=-arb(k-1)/k
    cross=arb_mat([[full[i,j] for j in range(n-1,2*n)] for i in range(n)])*difference
    target=difference.transpose()*arb_mat([[loads[i,0]] for i in range(n-1,2*n)])-cross.transpose()*coeff
    projected,raw=project(full,n,difference)
    g=[target[i,0] for i in range(n)]
    values=[arb(0) for _ in range(2*n)];cumulative=arb(0)
    for k in range(n+1,2*n+1):
        cumulative+=k*g[k-n-1]
        values[k-1]=cumulative/arb(k).sqrt()
        direct=loads[k-1,0]-sum((coeff[j,0]*full[j,k-1] for j in range(n)),arb(0))
        assert (values[k-1]-arb(k).sqrt()*direct).contains(0)
    h=[kernel.logs[i+1]-kernel.logs[i] for i in range(1,2*n)]
    slopes=[(values[i+1]-values[i])/h[i] for i in range(2*n-1)]
    curvature=[slopes[i+1]-slopes[i] for i in range(2*n-2)]
    diagonal=[(h[i]+h[i+1])/3 for i in range(2*n-2)]
    off=[h[i+1]/6 for i in range(2*n-3)]
    dual=tridiagonal(diagonal,off,curvature)
    if n==16:
        dense=arb_mat(2*n-2,2*n-2)
        for i,d in enumerate(diagonal):dense[i,i]=d
        for i,d in enumerate(off):dense[i,i+1]=d;dense[i+1,i]=d
        independent=dense.solve(arb_mat([[x] for x in curvature]),algorithm='precond')
        assert all(dual[i].overlaps(independent[i,0]) for i in range(2*n-2))
    bending=sum((a*b for a,b in zip(curvature,dual)),arb(0))
    simple=sum((x*x/(h[i]+h[i+1]) for i,x in enumerate(curvature)),arb(0))
    assert bending>2*simple and bending<6*simple
    curvature_direction=adjoint(n,h,dual)
    diagonal_direction=adjoint(n,h,[x/(h[i]+h[i+1]) for i,x in enumerate(curvature)])
    assert (sum((a*b for a,b in zip(g,curvature_direction)),arb(0))-bending).contains(0)
    model=arb_mat(2*n,2*n)
    for i in range(1,2*n+1):
        for j in range(1,2*n+1):
            t=abs(kernel.logs[j]-kernel.logs[i])
            model[i-1,j-1]=(2*kernel.k1+kernel.k1*t+t*t/4)/max(i,j)
    projected_model,_=project(model,n,difference)
    model_direction=projected_model.solve(target,algorithm='precond')
    model_numerator=(target.transpose()*model_direction)[0,0]
    aa=kernel.k1-arb(3)/2;bb=kernel.k1/4+arb(1)/8
    assert aa>0 and bb>0 and model_numerator>bending/(4*bb)
    assert model_numerator<84*bending/aa
    directions={};direction_accuracies=[]
    for name,vector in [('spline_curvature',arb_mat([[v] for v in curvature_direction])),
                        ('diagonal_curvature',arb_mat([[v] for v in diagonal_direction])),
                        ('repaired_model',model_direction)]:
        numerator=(target.transpose()*vector)[0,0]
        cost=(vector.transpose()*projected*vector)[0,0]
        raw_cost=(vector.transpose()*raw*vector)[0,0]
        assert numerator>0 and cost>0 and raw_cost>cost
        gain=numerator*numerator/cost
        assert gain>0 and gain<full_gain
        item={'fraction_of_full_gain':gain/full_gain,'relative_gain':gain/energy,
              'raw_lower_relative_gain':numerator*numerator/(raw_cost*energy),
              'numerator':numerator,'true_projected_cost':cost}
        directions[name]={key:value.str(65) for key,value in item.items()}
        direction_accuracies.extend(value.rel_accuracy_bits() for value in item.values())
    quantities={'energy':energy,'full_relative_gain':full_gain/energy,
                'model_numerator':model_numerator,'bending_energy':bending,
                'local_curvature_sum':simple,'bending_to_model_ratio':bending/model_numerator,
                'certified_numerator_lower_fraction':bending/(4*bb*model_numerator),
                'curvature_lower_over_residual':bending/(4*bb*energy),
                'local_lower_over_residual':simple/(2*bb*energy),
                'RKHS_upper_over_residual':84*bending/(aa*energy),
                'A':aa,'B':bb,'causal_rate':(bb/aa).sqrt()}
    return {'N':n,'seconds':round(time.monotonic()-started,3),
            'quantities':{key:value.str(65) for key,value in quantities.items()},
            'directions':directions,
            'minimum_accuracy_bits':min(direction_accuracies+[value.rel_accuracy_bits() for value in quantities.values()]),
            'gates':{'complete_actual_gram':True,'full_projection':True,
                     'normalized_interpolation_data':True,'positive_tridiagonal_pivots':True,
                     'tridiagonal_residuals_contain_zero':True,'adjoint_bending_identity':True,
                     'uniform_model_curvature_comparison':True,'selected_gains_below_optimum':True}}


def main() -> None:
    parser=argparse.ArgumentParser();parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    parser.add_argument('--cutoff',type=int,default=128);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();ctx.prec=args.bits
    kernel=Kernel(2*max(args.sizes),args.cutoff,24)
    rows=[]
    for n in args.sizes:
        row=run(n,kernel);rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'minorant_fraction':row['quantities']['certified_numerator_lower_fraction'],
                          'gain_fractions':{key:value['fraction_of_full_gain'] for key,value in row['directions'].items()}}),flush=True)
    report={'classification':'certified finite model-curvature and selected-direction comparisons; no cofinal arithmetic estimate',
            'precision_bits':args.bits,'finite_series_cutoff':args.cutoff,'bernoulli_order':24,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'kernel_source_sha256':hashlib.sha256((KERNEL/'certify_smoothed.py').read_bytes()).hexdigest(),
            'projection_source_sha256':hashlib.sha256((PRIOR/'certify_preconditioner.py').read_bytes()).hexdigest(),
            'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
