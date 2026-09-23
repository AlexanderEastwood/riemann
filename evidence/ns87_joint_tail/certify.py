"""Certified joint localization of fixed-q=2 optimized block observations.

Finite physical quadrature, full arithmetic Schur metric and complete tails.
No midpoint solve and no asymptotic conclusion.
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

HERE = Path(__file__).resolve().parent
KERNEL = HERE.parent / 'v159/ns61/certify_smoothed.py'
sys.path.insert(0, str(KERNEL.parent))
from certify_smoothed import Kernel, dot, sub, trace


def vector(values: list[arb]) -> arb_mat:
    return arb_mat([[x] for x in values])


def upper(value: arb) -> arb:
    return arb(value.upper())


def analyze(n: int, kernel: Kernel, factors: list[int]) -> dict[str, Any]:
    start = time.monotonic()
    m = 2*n
    stop = m*max(factors)
    logs = [arb(0)] + [arb(k).log() for k in range(1, stop+1)]
    logfact = [arb(0)]
    for k in range(1, stop+1):
        logfact.append(logfact[-1]+logs[k])
    gram = arb_mat([[kernel.gram(i,j) for j in range(1,m+1)] for i in range(1,m+1)])
    loads = vector([kernel.load(i) for i in range(1,m+1)])
    old = sub(gram,0,n,0,n)
    cross = sub(gram,0,n,n,m)
    oldloads = sub(loads,0,n,0,1)
    c = old.solve(oldloads,algorithm='precond')
    fit = old.solve(cross,algorithm='precond')
    # D columns are actual projected new atoms in the original atom coordinates.
    d = arb_mat([[-fit[i,j] if i<n else arb(int(i-n==j)) for j in range(n)] for i in range(m)])
    h = sub(loads,n,m,0,1)-cross.transpose()*c
    schur = sub(gram,n,m,n,m)-cross.transpose()*fit
    energy = 2-dot(oldloads,c)
    gain = dot(h,schur.solve(h,algorithm='precond'))
    assert 0 < gain < energy
    assert all((sub(gram,0,n,0,m)*d)[i,j].contains(0) for i in range(n) for j in range(n))
    # Transform physical atom cells into [R_N, phi_(N+1),...,phi_M] coordinates.
    transform = arb_mat(m+1,n+1)
    transform[0,0] = 1
    for i in range(m):
        transform[i+1,0] = -c[i,0] if i<n else 0
        for j in range(n): transform[i+1,j+1] = d[i,j]
    full = arb_mat(n+1,n+1)
    full[0,0] = energy
    for j in range(n):
        full[0,j+1] = full[j+1,0] = h[j,0]
        for k in range(n): full[j+1,k+1] = schur[j,k]
    trans = transform.transpose()
    avec = trans*vector([arb(0)]+[arb(1)/k for k in range(1,m+1)])
    aa = avec*avec.transpose()
    head = aa # complete 0<t<1 contribution; tau=0 and sigma_n=t/n.
    cumulative0, cumulative1 = [arb(0)], [arb(0)]
    r_over_t = avec[0,0]
    rows: list[dict[str,Any]] = []
    q_checks = 0
    for k in range(1,stop):
        a,b = logs[k],logs[k+1]
        bvec = trans*vector([arb(1)]+[-arb(k//j) for j in range(1,m+1)])
        cvec = trans*vector([arb(0)]+[logfact[k//j]+(k//j)*logs[j] for j in range(1,m+1)])
        i0 = arb(1)/(k*(k+1))
        i1 = (a+1)/k-(b+1)/(k+1)
        i2 = (a*a+2*a+2)/k-(b*b+2*b+2)/(k+1)
        ab = avec*bvec.transpose()
        ac = avec*cvec.transpose()
        bc = bvec*cvec.transpose()
        head += aa+(ab+ab.transpose())*((b*b-a*a)/2)
        head += (ac+ac.transpose())*(b-a)+bvec*bvec.transpose()*i2
        head += (bc+bc.transpose())*i1+cvec*cvec.transpose()*i0
        ra,rb,rc = avec[0,0],bvec[0,0],cvec[0,0]
        cumulative0.append(cumulative0[-1]+ra*(b-a)+rb*i1+rc*i0)
        cumulative1.append(cumulative1[-1]+ra*(b*b-a*a)/2+rb*i2+rc*i1)
        r_over_t += ra+rb*(b*b-a*a)/2+rc*(b-a)
        t = k+1
        if t not in [m*f for f in factors]: continue
        tail = full-head
        tail_energy = tail[0,0]
        kt = sub(tail,1,n+1,1,n+1)
        tr = trace(schur.solve(kt,algorithm='precond'))
        assert tail_energy > 0 and tr > 0
        # Both 1 and trace are proved spectral upper bounds. Use an outward endpoint.
        beta = upper(tr) if tr < 1 else arb(1)
        finite = sub(head,1,n+1,0,1)
        finite_gain = dot(finite,schur.solve(finite,algorithm='precond'))
        delta = h-finite
        actual_tail_metric = dot(delta,schur.solve(delta,algorithm='precond'))
        budget = upper(beta*upper(tail_energy))
        assert actual_tail_metric < budget
        root_difference = finite_gain.sqrt()-budget.sqrt()
        lower_gain = root_difference**2 if root_difference > 0 else arb(0)
        # Choose an exact dyadic scalar below the safe optimum; interval solves
        # enclose a uniquely defined direction, never an uncertified midpoint.
        theta = 1-upper((budget/arb(finite_gain.lower())).sqrt()) if root_difference > 0 else arb(0)
        local_direction = schur.solve(finite,algorithm='precond')
        actual_safe_gain = 2*theta*dot(h,local_direction)-theta**2*finite_gain
        safe_guarantee = theta**2*finite_gain
        if theta > 0:
            assert actual_safe_gain > safe_guarantee > 0
        upper_gain = (finite_gain.sqrt()+budget.sqrt())**2
        assert lower_gain < gain < upper_gain
        # Same h_T from finite arithmetic quadrature, all raw old/new observations.
        pt = [arb(0)] + [cumulative1[-1]-cumulative1[j-1]
               -logs[j]*(cumulative0[-1]-cumulative0[j-1]) for j in range(1,t+1)]
        raw = vector([r_over_t/j-sum((pt[s] for s in range(j,t+1,j)),arb(0))
                      for j in range(1,m+1)])
        from_potential = d.transpose()*raw
        assert all(from_potential[j,0].overlaps(finite[j,0]) for j in range(n))
        q_checks += n
        # Independent complete Stirling norm interval for R after T.
        coeffs = [c[j,0] for j in range(n)]
        slope = 1-sum(coeffs,arb(0))/2
        const = sum((cc*(logs[j]-kernel.log2pi) for j,cc in enumerate(coeffs,1)),arb(0))/2
        rem = sum((j*abs(cc) for j,cc in enumerate(coeffs,1)),arb(0))/6
        qt = slope*logs[t]+const
        main = (qt*qt+2*slope*qt+2*slope*slope)/t
        err = rem**2/(3*arb(t)**3)
        stirling_tail = main+arb(0,2*(main*err).sqrt()+err)
        assert stirling_tail.overlaps(tail_energy)
        harmonic = sum((arb(1)/j for j in range(1,n+1)),arb(0))
        coefficient_constant = 48*harmonic*n**3*(n+2)
        majorant = (logs[t]+kernel.log2pi)/2+arb(n)/(6*t)
        universal_tail = (2*(logs[t]**2+2*logs[t]+2)
                          +64*n*coefficient_constant*(majorant**2+majorant+arb(1)/2))/t
        assert tail_energy < universal_tail
        values = {'universal_tail_majorant':universal_tail,'E_N':energy,'full_gain':gain,'full_relative_gain':gain/energy,
                  'tail_energy':tail_energy,'tail_energy_fraction':tail_energy/energy,
                  'tail_trace':tr,'tail_operator_bound':beta,
                  'finite_observation_gain':finite_gain,
                  'actual_tail_metric':actual_tail_metric,'tail_metric_budget':budget,
                  'safe_step_scalar':theta,'safe_step_actual_gain':actual_safe_gain,
                  'safe_step_guaranteed_gain':safe_guarantee,
                  'safe_step_guaranteed_fraction':safe_guarantee/gain,
                  'safe_step_actual_fraction':actual_safe_gain/gain,
                  'certified_gain_lower':lower_gain,'certified_relative_gain_lower':lower_gain/energy,
                  'certified_fraction_of_full_gain':lower_gain/gain,
                  'finite_gain_over_actual_gain':finite_gain/gain,
                  'complete_Stirling_tail':stirling_tail}
        rows.append({'T':t,'values':{key:val.str(65) for key,val in values.items()},
                     'gates':{'complete_tail_metric':True,'finite_potential_matches_physical_pairings':True,
                              'Stirling_tail_overlap':True,'certifies_positive_gain':bool(lower_gain>0),
                              'lower_and_upper_contain_actual_gain':True}})
    assert len(rows)==len(factors)
    return {'N':n,'M':m,'seconds':round(time.monotonic()-start,3),
            'potential_pairing_checks':q_checks,'rows':rows}


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--bits',type=int,required=True)
    p.add_argument('--sizes',type=int,nargs='+',default=[8,16,32])
    p.add_argument('--factors',type=int,nargs='+',default=[1,4,16,64])
    p.add_argument('--kernel-cutoff',type=int,default=128)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    assert min(args.sizes)>=2 and min(args.factors)>=1 and len(set(args.factors))==len(args.factors)
    ctx.prec=args.bits
    kernel=Kernel(2*max(args.sizes),args.kernel_cutoff,24)
    result=[]
    for n in args.sizes:
        row=analyze(n,kernel,args.factors)
        result.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'bounds':[(x['T'],x['values']['certified_fraction_of_full_gain']) for x in row['rows']]}),flush=True)
    report={'classification':'Certified finite localized gain bounds; no cofinal lower bound',
            'precision_bits':args.bits,'kernel_cutoff':args.kernel_cutoff,'kernel_order':24,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'kernel_sha256':hashlib.sha256(KERNEL.read_bytes()).hexdigest(),'rows':result}
    args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__': main()
