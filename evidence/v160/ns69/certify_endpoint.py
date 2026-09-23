"""Complete Arb comparison of optimized correlations and their signed remainder."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

PREVIOUS = Path(__file__).resolve().parents[2] / 'v159' / 'ns61'
sys.path.insert(0,str(PREVIOUS))
from certify_smoothed import Kernel


def dot(a: list[arb], b: list[arb]) -> arb:
    return sum((x*y for x,y in zip(a,b)),arb(0))


def inspect(n: int, kernel: Kernel) -> dict[str,Any]:
    started=time.monotonic()
    gram=arb_mat([[kernel.gram(i,j) for j in range(1,n+1)] for i in range(1,n+1)])
    loads=arb_mat([[kernel.load(i)] for i in range(1,n+1)])
    coeff=gram.solve(loads,algorithm='precond')
    solution=[coeff[i,0] for i in range(n)]
    residual=gram*coeff-loads
    assert all(residual[i,0].contains(0) for i in range(n))
    energy=2-(loads.transpose()*coeff)[0,0]
    a=1-sum(solution,arb(0))/2
    ell=sum((solution[m-1]*(arb(m).log()-kernel.log2pi)/2 for m in range(1,n+1)),arb(0))
    mass=sum((m*abs(solution[m-1]) for m in range(1,n+1)),arb(0))
    actual,leading,remainders,old_budgets,new_budgets=[],[],[],[],[]
    samples=[]
    sample_indices=sorted(set(range(n+1,2*n+1)) | {4*n,8*n,16*n})
    for k in sample_indices:
        raw=kernel.load(k)-arb(k-1)*kernel.load(k-1)/k
        cross=[kernel.gram(m,k)-arb(k-1)*kernel.gram(m,k-1)/k for m in range(1,n+1)]
        full=raw-dot(solution,cross)
        logk,logprev=arb(k).log(),arb(k-1).log()
        model=(a*((logk*logk-logprev*logprev)/2+(2-kernel.gamma)*(logk-logprev))
               +ell*(logk-logprev))/k
        rem=full-model
        direct_remainder=arb(0)
        for m in range(1,n+1):
            d0,d1=math.gcd(k,m),math.gcd(k-1,m)
            direct_remainder-=solution[m-1]/m*(kernel.s2(k//d0,m//d0)
                -arb(k-1)*kernel.s2((k-1)//d1,m//d1)/k)
        assert (rem-direct_remainder).contains(0)
        budget_old=arb.pi()**2*mass/(8*k*k*(k-1))
        budget_new=budget_old/18
        assert abs(rem)<budget_new
        if k<=2*n:
            actual.append(full);leading.append(model);remainders.append(rem)
            old_budgets.append(budget_old);new_budgets.append(budget_new)
        if k in [n+1,2*n,4*n,8*n,16*n]:
            samples.append({'index':k,'actual':full.str(65),'leading':model.str(65),
                            'remainder':rem.str(65),'improved_absolute_budget':budget_new.str(65),
                            'relative_remainder':(abs(rem)/abs(model)).str(65)})
    actual2,leading2,rem2=dot(actual,actual),dot(leading,leading),dot(remainders,remainders)
    mixed=dot(leading,remainders)
    assert (actual2-leading2-2*mixed-rem2).contains(0)
    assert actual2>0 and leading2>0 and rem2>0
    quantities={'E_N':energy,'endpoint_log_coefficient':a,'endpoint_constant':ell,
                'coefficient_mass':mass,'actual_norm':actual2.sqrt(),
                'leading_norm':leading2.sqrt(),'actual_remainder_norm':rem2.sqrt(),
                'remainder_over_leading':(rem2/leading2).sqrt(),
                'actual_over_leading':(actual2/leading2).sqrt(),
                'leading_remainder_cosine':mixed/(leading2*rem2).sqrt(),
                'leading_actual_cosine':dot(leading,actual)/(leading2*actual2).sqrt(),
                'old_budget_over_leading':(dot(old_budgets,old_budgets)/leading2).sqrt(),
                'improved_budget_over_leading':(dot(new_budgets,new_budgets)/leading2).sqrt(),
                'improved_budget_over_actual_remainder':(dot(new_budgets,new_budgets)/rem2).sqrt(),
                'leading_model_scaled_energy_over_E':8*n*n*leading2/(3*kernel.kappa*energy),
                'actual_trace_bound_over_E':8*n*n*actual2/(3*kernel.kappa*energy)}
    quantities.update(trial_gains(n,kernel,gram,energy,actual,leading))
    assert all(x.is_finite() for x in quantities.values())
    return {'N':n,'seconds':round(time.monotonic()-started,3),
            'quantities':{key:x.str(65) for key,x in quantities.items()},
            'minimum_accuracy_bits':min(x.rel_accuracy_bits() for x in quantities.values()),
            'samples':samples,'gates':{'certified_old_projection_solve':True,
                                      'complete_signed_remainder_identity':True,
                                      'independent_S2_remainder_identity':True,
                                      'full_projected_trial_gains':True,
                                      'improved_analytic_error_budget':True}}


def trial_gains(n: int, kernel: Kernel, old: arb_mat, energy: arb,
                actual: list[arb], leading: list[arb]) -> dict[str,arb]:
    full=arb_mat([[kernel.gram(i,j) for j in range(1,2*n+1)] for i in range(1,2*n+1)])
    loads=arb_mat([[kernel.load(i)] for i in range(1,2*n+1)])
    next_coeff=full.solve(loads,algorithm='precond')
    next_energy=2-(loads.transpose()*next_coeff)[0,0]
    gain=energy-next_energy
    assert next_energy>0 and gain>0
    rawmap=arb_mat(n+1,n)
    for j,k in enumerate(range(n+1,2*n+1)):
        rawmap[j+1,j]=1
        rawmap[j,j]=-arb(k-1)/k
    tail=arb_mat([[full[i,j] for j in range(n-1,2*n)] for i in range(n-1,2*n)])
    cross=arb_mat([[full[i,j] for j in range(n-1,2*n)] for i in range(n)])*rawmap
    raw=rawmap.transpose()*tail*rawmap
    weights=arb_mat(n,3)
    for j,k in enumerate(range(n+1,2*n+1)):
        right,left=arb(k).log(),arb(k-1).log()
        weights[j,0]=n*n*(right-left)/k
        weights[j,1]=n*n*((right*right-left*left)/2-arb(n).log()*(right-left))/k
        weights[j,2]=actual[j]
    trial_cross=cross*weights
    projected=weights.transpose()*raw*weights-trial_cross.transpose()*old.solve(trial_cross,algorithm='precond')
    target=weights.transpose()*arb_mat([[value] for value in actual])
    moment_gram=arb_mat([[projected[i,j] for j in range(2)] for i in range(2)])
    moment_target=arb_mat([[target[i,0]] for i in range(2)])
    moment_gain=(moment_target.transpose()*moment_gram.solve(moment_target,algorithm='precond'))[0,0]
    actual_direction_gain=target[2,0]*target[2,0]/projected[2,2]
    leading_column=arb_mat([[value] for value in leading])
    leading_cross=cross*leading_column
    leading_denominator=(leading_column.transpose()*raw*leading_column
                         -leading_cross.transpose()*old.solve(leading_cross,algorithm='precond'))[0,0]
    leading_numerator=dot(leading,actual)
    leading_gain=leading_numerator*leading_numerator/leading_denominator
    assert leading_gain>0 and moment_gain>leading_gain and gain>moment_gain
    assert actual_direction_gain>0 and gain>actual_direction_gain
    return {'full_relative_gain':gain/energy,'two_moment_relative_gain':moment_gain/energy,
            'two_moment_fraction_of_gain':moment_gain/gain,
            'leading_direction_relative_gain':leading_gain/energy,
            'leading_direction_fraction_of_gain':leading_gain/gain,
            'actual_direction_relative_gain':actual_direction_gain/energy,
            'actual_direction_fraction_of_gain':actual_direction_gain/gain}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    parser.add_argument('--cutoff',type=int,default=128)
    parser.add_argument('--order',type=int,default=24)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=args.bits
    kernel=Kernel(16*max(args.sizes),args.cutoff,args.order)
    rows=[]
    for n in args.sizes:
        row=inspect(n,kernel)
        rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'remainder_over_leading':row['quantities']['remainder_over_leading'],
                          'leading_actual_cosine':row['quantities']['leading_actual_cosine']}),flush=True)
    report={'classification':'certified finite optimized endpoint comparisons, no asymptotic lower bound',
            'precision_bits':args.bits,'finite_series_cutoff':args.cutoff,'bernoulli_order':args.order,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'kernel_source_sha256':hashlib.sha256((PREVIOUS/'certify_smoothed.py').read_bytes()).hexdigest(),
            'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
