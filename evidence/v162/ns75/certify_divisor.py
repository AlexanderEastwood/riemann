"""Certified block gains from the actual optimized divisor defect."""
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
for location in [ROOT/'v159/ns61', ROOT/'v160/ns71', ROOT/'v160/ns67', ROOT/'v161/ns72']:
    sys.path.insert(0, str(location))
from certify_smoothed import Kernel
from certify_preconditioner import block, project
from certify_curvature import adjoint


def run(n: int, kernel: Kernel) -> dict[str, Any]:
    started = time.monotonic()
    full = arb_mat([[kernel.gram(i,j) for j in range(1,2*n+1)] for i in range(1,2*n+1)])
    loads = arb_mat([[kernel.load(i)] for i in range(1,2*n+1)])
    old_load = arb_mat([[loads[i,0]] for i in range(n)])
    coeff = block(full,0,n).solve(old_load,algorithm='precond')
    energy = 2-(old_load.transpose()*coeff)[0,0]
    full_gain = energy-2+(loads.transpose()*full.solve(loads,algorithm='precond'))[0,0]
    difference = arb_mat(n+1,n)
    for j,k in enumerate(range(n+1,2*n+1)):
        difference[j+1,j] = 1
        difference[j,j] = -arb(k-1)/k
    cross = arb_mat([[full[i,j] for j in range(n-1,2*n)] for i in range(n)])*difference
    g = difference.transpose()*arb_mat([[loads[i,0]] for i in range(n-1,2*n)])-cross.transpose()*coeff
    projected, _ = project(full,n,difference)
    defect = [arb(0) for _ in range(2*n+1)]
    for divisor in range(1,n+1):
        for multiple in range(divisor,2*n+1,divisor):
            defect[multiple] += coeff[divisor-1,0]
    defect[1] += 1
    directions = []
    physical_directions: list[list[arb]] = []
    for power in range(3):
        physical: list[arb] = []
        for k in range(n+1,2*n+1):
            taper = kernel.logs[2*n]-kernel.logs[k] if k < 2*n else arb(0)
            weight = arb(1) if power == 0 else taper if power == 1 else taper*taper
            physical.append(-defect[k]*weight)
        suffix = arb(0)
        vector = [arb(0) for _ in range(n)]
        for k in range(2*n,n,-1):
            suffix += physical[k-n-1]/k
            vector[k-n-1] = k*suffix
        for i,k in enumerate(range(n+1,2*n+1)):
            restored = vector[i]-(arb(k)/(k+1)*vector[i+1] if i+1<n else 0)
            assert (restored-physical[i]).contains(0)
        directions.append(arb_mat([[x] for x in vector]))
        physical_directions.append(physical)
        if power == 0:
            assert all((defect[k]+physical[k-n-1]).contains(0) for k in range(n+1,2*n+1))
    values = [arb(0) for _ in range(2*n)]
    total = arb(0)
    for k in range(n+1,2*n+1):
        total += k*g[k-n-1,0]
        values[k-1] = total/arb(k).sqrt()
    h = [kernel.logs[i+1]-kernel.logs[i] for i in range(1,2*n)]
    slopes = [(values[i+1]-values[i])/h[i] for i in range(2*n-1)]
    dual = [(slopes[i+1]-slopes[i])/(h[i]+h[i+1]) for i in range(2*n-2)]
    curvature = arb_mat([[v] for v in adjoint(n,h,dual)])
    results: dict[str, dict[str, arb]] = {}
    for name, vector in zip(['raw_divisor_cancellation','linear_log_defect','quadratic_log_defect','diagonal_curvature'],directions+[curvature]):
        numerator = (g.transpose()*vector)[0,0]
        cost = (vector.transpose()*projected*vector)[0,0]
        gain = numerator*numerator/cost
        assert cost > 0 and gain > 0 and gain < full_gain
        results[name] = {'numerator':numerator,'true_projected_cost':cost,
                         'fraction_of_full_gain':gain/full_gain,'relative_gain':gain/energy}
    physical_gram = block(full,n,2*n)
    for name,physical in zip(list(results)[:3],physical_directions):
        vector = arb_mat([[x] for x in physical])
        raw_cost = (vector.transpose()*physical_gram*vector)[0,0]
        numerator = results[name]['numerator']
        raw_new_energy = energy-2*numerator+raw_cost
        assert raw_cost > results[name]['true_projected_cost'] > 0 and raw_new_energy > 0
        results[name]['held_old_unit_step_error_ratio'] = raw_new_energy/energy
        results[name]['held_old_optimal_step_relative_gain'] = numerator*numerator/(raw_cost*energy)
    basis = arb_mat([[v[i,0] for v in directions] for i in range(n)])
    small_gram = basis.transpose()*projected*basis
    small_load = basis.transpose()*g
    # Positive principal Schur pivots establish independence with complete cross terms.
    for size in range(1,4):
        assert block(small_gram,0,size).det() > 0
    fit = small_gram.solve(small_load,algorithm='precond')
    span_gain = (small_load.transpose()*fit)[0,0]
    assert 0 < span_gain < full_gain
    assert all(span_gain/full_gain > results[name]['fraction_of_full_gain'] for name in list(results)[:3])
    curvature_cost = results['diagonal_curvature']['true_projected_cost']
    span_load = basis.transpose()*projected*curvature
    overlap = (span_load.transpose()*small_gram.solve(span_load,algorithm='precond'))[0,0]/curvature_cost
    assert 0 < overlap < 1
    quantities = {'energy':energy,'full_relative_gain':full_gain/energy,
                  'three_direction_span_fraction':span_gain/full_gain,'three_direction_span_relative_gain':span_gain/energy,
                  'curvature_energy_fraction_in_span':overlap}
    all_values = list(quantities.values())+[v for item in results.values() for v in item.values()]
    return {'N':n,'seconds':round(time.monotonic()-started,3),
            'quantities':{key:value.str(65) for key,value in quantities.items()},
            'directions':{name:{key:value.str(65) for key,value in item.items()} for name,item in results.items()},
            'span_fit_coefficients':[fit[i,0].str(65) for i in range(3)],
            'minimum_accuracy_bits':min(x.rel_accuracy_bits() for x in all_values),
            'gates':{'complete_actual_gram':True,'complete_old_projection':True,'physical_difference_conversion':True,'raw_new_jumps_cancel':True,
                     'positive_three_direction_gram':True,'complete_span_cross_terms':True,'gains_below_optimum':True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    parser.add_argument('--cutoff',type=int,default=128)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    kernel = Kernel(2*max(args.sizes),args.cutoff,24)
    rows = []
    for n in args.sizes:
        row = run(n,kernel)
        rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'fractions':{key:value['fraction_of_full_gain'] for key,value in row['directions'].items()},
                          'span_fraction':row['quantities']['three_direction_span_fraction']}),flush=True)
    dependencies = {'kernel':ROOT/'v159/ns61/certify_smoothed.py',
                    'projection':ROOT/'v160/ns71/certify_preconditioner.py',
                    'curvature':ROOT/'v161/ns72/certify_curvature.py'}
    report = {'classification':'certified finite comparison of actual divisor-defect directions and their span; no cofinal estimate',
              'precision_bits':args.bits,'finite_series_cutoff':args.cutoff,'bernoulli_order':24,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256':{key:hashlib.sha256(path.read_bytes()).hexdigest() for key,path in dependencies.items()},'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    main()
