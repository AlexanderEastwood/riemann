"""Complete optimized dilation defects and true projected correction costs.

Finite interval certificates, not an eventual lower bound.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any
from flint import arb, arb_mat, ctx

HERE=Path(__file__).resolve().parent
KERNEL=HERE.parent/'v159/ns61/certify_smoothed.py'
sys.path.insert(0,str(KERNEL.parent))
from certify_smoothed import Kernel, dot, sub


def vector(values: list[arb]) -> arb_mat:
    return arb_mat([[x] for x in values])


def analyze(n: int, kernel: Kernel) -> dict[str,Any]:
    start=time.monotonic()
    m=2*n; previous=n//2
    gram=arb_mat([[kernel.gram(i,j) for j in range(1,m+1)] for i in range(1,m+1)])
    loads=vector([kernel.load(j) for j in range(1,m+1)])
    old=sub(gram,0,n,0,n);oldloads=sub(loads,0,n,0,1)
    prev=sub(gram,0,previous,0,previous);prevloads=sub(loads,0,previous,0,1)
    c=old.solve(oldloads,algorithm='precond')
    cp=prev.solve(prevloads,algorithm='precond')
    cn=gram.solve(loads,algorithm='precond')
    energy=2-dot(oldloads,c);before=2-dot(prevloads,cp);after=2-dot(loads,cn)
    cpad=vector([c[j,0] if j<n else arb(0) for j in range(m)])
    prior=vector([cp[j,0] if j<previous else arb(0) for j in range(m)])
    increment=cpad-prior;next_increment=cn-cpad
    dilated=vector([c[j//2,0] if j%2==1 else arb(0) for j in range(m)])
    dilated_increment=vector([increment[j//2,0] if j%2==1 else arb(0) for j in range(m)])
    residual_loads=loads-gram*cpad
    numerator=dot(residual_loads,dilated)
    previous_gain=before-energy;next_gain=energy-after
    numerator_increment=dot(next_increment,gram*dilated_increment)
    assert (numerator-numerator_increment).contains(0)
    assert (dot(dilated_increment,gram*dilated_increment)-previous_gain/2).contains(0)
    assert all(residual_loads[j,0].contains(0) for j in range(n))
    overlap=sub(gram,0,n,0,m)*dilated
    removed=old.solve(overlap,algorithm='precond')
    projected=dilated-vector([removed[j,0] if j<n else arb(0) for j in range(m)])
    cost=dot(projected,gram*projected)
    gain=numerator**2/cost
    assert 0<gain<next_gain and 0<cost<previous_gain/2
    assert 2*numerator**2 < previous_gain*next_gain
    eta=sum((c[j-1,0]/j for j in range(1,n+1)),arb(0))
    j1=1-sum((c[j-1,0]*(kernel.logs[j]+2-kernel.gamma)/j for j in range(1,n+1)),arb(0))
    l=kernel.logs[2]
    potential=energy-l*j1-eta*l*l/2+(1+c[0,0])*(3*l/2-1)
    autocorrelation=potential-numerator
    values={'E_previous':before,'E_N':energy,'E_next':after,
            'previous_gain':previous_gain,'next_gain':next_gain,
            'dilation_defect':numerator,'potential_at_two':potential,
            'autocorrelation_at_two':autocorrelation,
            'defect_over_energy':numerator/energy,
            'dyadic_scaled_abs_defect':arb(n.bit_length()-1)*abs(numerator)/energy,
            'projected_cost':cost,'cost_over_previous_gain':2*cost/previous_gain,
            'increment_overlap':arb(2).sqrt()*numerator/(previous_gain*next_gain).sqrt(),
            'optimal_dilation_gain':gain,'fraction_of_available_gain':gain/next_gain,
            'relative_dilation_gain':gain/energy,'eta':eta,'J_at_one':j1,
            'simple_energy_budget':previous_gain/(2*energy),
            'product_budget':previous_gain*next_gain/2}
    return {'N':n,'j':n.bit_length()-1,'seconds':round(time.monotonic()-start,3),
            'values':{k:v.str(65) for k,v in values.items()},
            'coefficients':[c[j,0].str(65) for j in range(n)],
            'gates':{'complete_Gram':True,'normal_equations':True,'dilation_increment_identity':True,
                     'dilated_increment_energy':True,'complete_projected_cost':True,
                     'two_increment_Cauchy_bound':True,'strict_finite_gain':True}}


def main() -> None:
    p=argparse.ArgumentParser();p.add_argument('--bits',type=int,required=True)
    p.add_argument('--sizes',type=int,nargs='+',default=[8,16,32,64])
    p.add_argument('--cutoff',type=int,default=128)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    assert all(n>=4 and n&(n-1)==0 for n in args.sizes)
    ctx.prec=args.bits;kernel=Kernel(2*max(args.sizes),args.cutoff,24)
    rows=[]
    for n in args.sizes:
        row=analyze(n,kernel);rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'scaled_defect':row['values']['dyadic_scaled_abs_defect'],
                          'gain_capture':row['values']['fraction_of_available_gain']}),flush=True)
    args.output.write_text(json.dumps({'classification':'Certified finite dilation test; no eventual arithmetic lower estimate',
        'precision_bits':args.bits,'kernel_cutoff':args.cutoff,'kernel_order':24,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'kernel_sha256':hashlib.sha256(KERNEL.read_bytes()).hexdigest(),'rows':rows},indent=2)+'\n')


if __name__=='__main__':main()
