"""Complete q=2 error of a prescribed logarithmic Mobius taper.

Includes exterior energy, exact reciprocal cells and the full analytic tail.
This is a finite certificate, never an asymptotic convergence estimate.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Any
from flint import arb, ctx

KERNEL_PATH = Path(__file__).resolve().parents[1]/'v159/ns61/certify_smoothed.py'
sys.path.insert(0,str(KERNEL_PATH.parent))
from certify_smoothed import Kernel, mobius


def evaluate(size: int, stop: int, kernel: Kernel) -> dict[str, Any]:
    start = time.monotonic()
    logn = arb(size).log()
    coefficients = [-mobius(n)*(1-arb(n).log()/logn) for n in range(1,size+1)]
    eta = sum((c/n for n,c in enumerate(coefficients,1)),arb(0))
    total = sum(coefficients,arb(0))
    slope = 1-total/2
    constant = sum((c*arb(n).log() for n,c in enumerate(coefficients,1)),arb(0))/2-total*(2*arb.pi()).log()/2
    remainder = sum((n*abs(c) for n,c in enumerate(coefficients,1)),arb(0))/6
    defects = [arb(0) for _ in range(stop)]
    defects[1] = arb(1)
    for n,c in enumerate(coefficients,1):
        if not c.is_zero():
            for multiple in range(n,stop,n):
                defects[multiple] += c
    running, logarithmic, logm = arb(0),arb(0),arb(0)
    finite = eta*eta
    prefix_to_n = arb(0)
    for m in range(1,stop):
        running += defects[m]
        logarithmic += defects[m]*logm
        lognext = arb(m+1).log()
        weight = arb(1)/(m*(m+1))
        i1 = (logm+1)/m-(lognext+1)/(m+1)
        i2 = (logm*logm+2*logm+2)/m-(lognext*lognext+2*lognext+2)/(m+1)
        cell = eta*eta+running*running*i2+logarithmic*logarithmic*weight
        cell -= eta*running*(lognext*lognext-logm*logm)
        cell += 2*eta*logarithmic*(lognext-logm)-2*running*logarithmic*i1
        assert not cell < 0
        finite += cell
        if m < size:
            prefix_to_n += cell
        logm = lognext
    q = slope*logm+constant
    tail = (q*q+2*slope*q+2*slope*slope)/stop
    remainder_energy = remainder**2/(3*arb(stop)**3)
    radius = 2*(tail*remainder_energy).sqrt()+remainder_energy
    energy = finite+tail+arb(0,radius)
    assert energy > 0
    pairing = kernel.load(1)-sum((c*kernel.gram(1,n) for n,c in enumerate(coefficients,1)),arb(0))
    norm1 = kernel.gram(1,1)
    fitted_step = pairing/norm1
    fitted_energy = energy-pairing*pairing/norm1
    balanced_energy = energy+2*eta*pairing+eta*eta*norm1
    assert fitted_energy > 0 and fitted_energy < energy and balanced_energy > 0
    values = {'sigma1_pairing':pairing,'sigma1_squared_norm':norm1,'optimal_sigma1_step':fitted_step,
              'one_atom_fitted_energy':fitted_energy,'exterior_balanced_energy':balanced_energy,
              'eta':eta,'exterior_energy':eta*eta,'prefix_energy_1_to_N':prefix_to_n,
              'finite_energy_with_exterior':finite,'main_tail':tail,'tail_radius':radius,
              'complete_energy':energy,'exterior_fraction':eta*eta/energy,
              'logN_times_energy':logn*energy,'logN_squared_times_energy':logn*logn*energy,
              'tail_relative_radius':radius/energy}
    return {'N':size,'cell_stop':stop,'values':{k:v.str(65) for k,v in values.items()},
            'seconds':round(time.monotonic()-start,3)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits',type=int,required=True)
    parser.add_argument('--sizes',type=int,nargs='+',required=True)
    parser.add_argument('--cell-stop',type=int,default=65536)
    parser.add_argument('--kernel-cutoff',type=int,default=128)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    assert min(args.sizes)>=2 and args.cell_stop>max(args.sizes)
    ctx.prec = args.bits
    kernel = Kernel(max(args.sizes),args.kernel_cutoff,24)
    rows=[]
    for n in args.sizes:
        row=evaluate(n,args.cell_stop,kernel);rows.append(row)
        print(json.dumps({'N':n,'bits':args.bits,**row['values'],'seconds':row['seconds']}),flush=True)
    report={'classification':'certified finite full error for fixed logarithmic taper; no rate theorem',
            'precision_bits':args.bits,'kernel_cutoff':args.kernel_cutoff,'kernel_order':24,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'mobius_source_sha256':hashlib.sha256(KERNEL_PATH.read_bytes()).hexdigest(),'rows':rows}
    args.output.write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':
    main()
