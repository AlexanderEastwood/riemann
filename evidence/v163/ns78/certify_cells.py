"""Complete reciprocal-cell norm and sampling enclosures for actual NB residuals."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import arb, arb_mat, ctx

KERNEL_PATH = Path(__file__).resolve().parents[2]/'v159/ns61/certify_smoothed.py'
sys.path.insert(0,str(KERNEL_PATH.parent))
from certify_smoothed import Kernel


def run(n: int, stop: int, kernel: Kernel) -> dict[str, Any]:
    started = time.monotonic()
    gram = arb_mat([[kernel.gram(i,j) for j in range(1,n+1)] for i in range(1,n+1)])
    loads = arb_mat([[kernel.load(i)] for i in range(1,n+1)])
    fit = gram.solve(loads,algorithm='precond')
    coefficients = [fit[i,0] for i in range(n)]
    energy = 2-(loads.transpose()*fit)[0,0]
    eta = sum((c/(i+1) for i,c in enumerate(coefficients)),arb(0))
    total = sum(coefficients,arb(0))
    slope = 1-total/2
    constant = sum((c*arb(i+1).log() for i,c in enumerate(coefficients)),arb(0))/2-total*(2*arb.pi()).log()/2
    remainder_constant = sum(((i+1)*abs(c) for i,c in enumerate(coefficients)),arb(0))/6
    defects = [arb(0) for _ in range(stop)]
    defects[1] = arb(1)
    for k,c in enumerate(coefficients,1):
        for multiple in range(k,stop,k):
            defects[multiple] += c
    running = arb(0)
    logarithmic = arb(0)
    finite_energy = eta*eta
    sample_prefix = arb(0)
    logm = arb(0)
    left = -eta
    for m in range(1,stop):
        running += defects[m]
        logarithmic += defects[m]*logm
        lognext = arb(m+1).log()
        right = -eta*(m+1)+running*lognext-logarithmic
        weight = arb(1)/(m*(m+1))
        i1 = (logm+1)/m-(lognext+1)/(m+1)
        i2 = (logm*logm+2*logm+2)/m-(lognext*lognext+2*lognext+2)/(m+1)
        cell = eta*eta+running*running*i2+logarithmic*logarithmic*weight
        cell -= eta*running*(lognext*lognext-logm*logm)
        cell += 2*eta*logarithmic*(lognext-logm)-2*running*logarithmic*i1
        assert not cell < 0
        finite_energy += cell
        sample_prefix += weight*(left*left+right*right)
        left,logm = right,lognext
    centered = slope*logm+constant
    main_tail = (centered*centered+2*slope*centered+2*slope*slope)/stop
    remainder_tail = remainder_constant**2/(3*arb(stop)**3)
    cross_tail = 2*(main_tail*remainder_tail).sqrt()
    # This symmetric enclosure contains both the cross term and the nonnegative remainder norm.
    tail_radius = cross_tail+remainder_tail
    direct_energy = finite_energy+main_tail+arb(0,tail_radius)
    q = abs(centered)+(remainder_constant+abs(slope))/stop
    sample_tail_upper = 2*(q*q+2*abs(slope)*q+2*slope*slope)/stop
    sample_total = sample_prefix+arb(sample_tail_upper/2,sample_tail_upper/2)
    comparison_quantity = eta*eta+sample_total
    assert energy > 0 and direct_energy > 0 and direct_energy.overlaps(energy)
    assert sample_prefix > 0 and sample_tail_upper > 0
    # These stronger finite gates are checked directly, in addition to the all-size analytic theorem.
    assert (eta*eta+sample_prefix+sample_tail_upper)/16 < energy
    assert energy < arb(21)/16*(eta*eta+sample_prefix)
    values = {'gram_energy':energy,'eta':eta,'tail_slope':slope,'tail_constant':constant,
              'stirling_remainder_constant':remainder_constant,'finite_cell_energy_with_exterior':finite_energy,
              'complete_main_tail':main_tail,'complete_tail_radius':tail_radius,
              'complete_physical_energy_enclosure':direct_energy,'tail_radius_over_gram_energy':tail_radius/energy,
              'sample_prefix':sample_prefix,'complete_sample_tail_upper':sample_tail_upper,
              'complete_sample_sum_enclosure':sample_total,'comparison_quantity_enclosure':comparison_quantity,
              'comparison_quantity_over_energy':comparison_quantity/energy}
    return {'N':n,'reciprocal_cell_stop':stop,'seconds':round(time.monotonic()-started,3),
            'values':{key:value.str(65) for key,value in values.items()},
            'gates':{'complete_physical_tail':True,'complete_sampling_tail':True,'physical_gram_overlap':True,
                     'uniform_lower_comparison':True,'uniform_upper_comparison':True,'all_solves_keep_balls':True}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    parser.add_argument('--cell-stop',type=int,default=65536)
    parser.add_argument('--kernel-cutoff',type=int,default=128)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    assert args.cell_stop > max(args.sizes)
    ctx.prec = args.bits
    kernel = Kernel(max(args.sizes),args.kernel_cutoff,24)
    rows = []
    for n in args.sizes:
        row = run(n,args.cell_stop,kernel)
        rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,'seconds':row['seconds'],
                          'tail_radius_over_energy':row['values']['tail_radius_over_gram_energy'],
                          'sample_quantity_over_energy':row['values']['comparison_quantity_over_energy']}),flush=True)
    report = {'classification':'certified complete physical-cell and reciprocal-sampling checks; no cofinal arithmetic estimate',
              'precision_bits':args.bits,'kernel_series_cutoff':args.kernel_cutoff,'kernel_bernoulli_order':24,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependency_sha256':{'kernel':hashlib.sha256(KERNEL_PATH.read_bytes()).hexdigest()},'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    main()
