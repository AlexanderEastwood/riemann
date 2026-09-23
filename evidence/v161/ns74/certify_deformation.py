"""Complete finite gains for a unitary altered family with a known floor."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

ROOT = Path(__file__).resolve().parents[2]
for location in [ROOT/'v159/ns61', ROOT/'v160/ns71', ROOT/'v161/ns72']:
    sys.path.insert(0, str(location))
from certify_smoothed import Kernel
from certify_preconditioner import block, project
from certify_curvature import adjoint


def run(n: int, kernel: Kernel, denominators: list[int]) -> dict[str, Any]:
    started = time.monotonic()
    full = arb_mat([[kernel.gram(i,j) for j in range(1,2*n+1)] for i in range(1,2*n+1)])
    betas = [arb(1)/2]+[arb(1)/2+arb(1)/d for d in denominators]
    loads = arb_mat(2*n,len(betas))
    for column, beta in enumerate(betas):
        slope = (1-beta)/beta
        constant = (2*beta-1)/(beta*beta)
        for k in range(1,2*n+1):
            loads[k-1,column] = slope*kernel.load(k)-constant*(kernel.logs[k]+2-arb.const_euler()+1/beta)/k
    old_load = arb_mat([[loads[i,j] for j in range(len(betas))] for i in range(n)])
    old_coeff = block(full,0,n).solve(old_load,algorithm='precond')
    next_coeff = full.solve(loads,algorithm='precond')
    difference = arb_mat(n+1,n)
    for j,k in enumerate(range(n+1,2*n+1)):
        difference[j+1,j] = 1
        difference[j,j] = -arb(k-1)/k
    cross = arb_mat([[full[i,j] for j in range(n-1,2*n)] for i in range(n)])*difference
    all_g = difference.transpose()*arb_mat([[loads[i,j] for j in range(len(betas))] for i in range(n-1,2*n)])-cross.transpose()*old_coeff
    projected, _ = project(full,n,difference)
    h = [kernel.logs[i+1]-kernel.logs[i] for i in range(1,2*n)]
    results: dict[str, dict[str, arb]] = {}
    for column, beta in enumerate(betas):
        key = 'original' if column == 0 else f'beta_half_plus_1_over_{denominators[column-1]}'
        energy = 2-sum((old_load[i,column]*old_coeff[i,column] for i in range(n)),arb(0))
        next_energy = 2-sum((loads[i,column]*next_coeff[i,column] for i in range(2*n)),arb(0))
        full_gain = energy-next_energy
        floor = (2*beta-1)*(1-beta)*(1-beta)/(beta**6)
        assert energy > next_energy > floor
        g = arb_mat([[all_g[i,column]] for i in range(n)])
        values = [arb(0) for _ in range(2*n)]
        total = arb(0)
        for k in range(n+1,2*n+1):
            total += k*g[k-n-1,0]
            values[k-1] = total/arb(k).sqrt()
        slopes = [(values[i+1]-values[i])/h[i] for i in range(2*n-1)]
        dual = [(slopes[i+1]-slopes[i])/(h[i]+h[i+1]) for i in range(2*n-2)]
        vector = arb_mat([[v] for v in adjoint(n,h,dual)])
        numerator = (g.transpose()*vector)[0,0]
        cost = (vector.transpose()*projected*vector)[0,0]
        gain = numerator*numerator/cost
        assert numerator > 0 and cost > 0 and 0 < gain < full_gain
        results[key] = {'beta':beta,'energy':energy,'next_energy':next_energy,
                        'positive_floor':floor,'floor_fraction_of_energy':floor/energy,
                        'full_relative_gain':full_gain/energy,'curvature_relative_gain':gain/energy,
                        'curvature_fraction_of_full_gain':gain/full_gain,
                        'curvature_numerator':numerator,'curvature_true_cost':cost}
    nonzero = [v for name,item in results.items() for key,v in item.items()
               if not (name == 'original' and key in ['positive_floor','floor_fraction_of_energy'])]
    return {'N':n,'seconds':round(time.monotonic()-started,3),
            'families':{name:{key:value.str(65) for key,value in item.items()} for name,item in results.items()},
            'minimum_accuracy_bits':min(x.rel_accuracy_bits() for x in nonzero),
            'gates':{'identical_complete_gram':True,'exact_analytic_loads':True,
                     'complete_old_projection':True,'positive_floor_below_both_errors':True,
                     'curvature_gain_positive_below_full_gain':True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    parser.add_argument('--denominators',type=int,nargs='+',default=[1000000,10000000000])
    parser.add_argument('--cutoff',type=int,default=128)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    assert all(d > 2 for d in args.denominators)
    ctx.prec = args.bits
    kernel = Kernel(2*max(args.sizes),args.cutoff,24)
    rows = []
    for n in args.sizes:
        row = run(n,kernel,args.denominators)
        rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'fractions':{key:value['curvature_fraction_of_full_gain'] for key,value in row['families'].items()}}),flush=True)
    dependencies = {'kernel':ROOT/'v159/ns61/certify_smoothed.py',
                    'projection':ROOT/'v160/ns71/certify_preconditioner.py',
                    'curvature':ROOT/'v161/ns72/certify_curvature.py'}
    report = {'classification':'certified finite altered-family control; no error floor asserted for original arithmetic atoms',
              'precision_bits':args.bits,'finite_series_cutoff':args.cutoff,'bernoulli_order':24,
              'beta_offset_denominators':args.denominators,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256':{key:hashlib.sha256(path.read_bytes()).hexdigest() for key,path in dependencies.items()},'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    main()
