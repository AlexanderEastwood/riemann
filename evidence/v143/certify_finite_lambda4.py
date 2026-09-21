#!/usr/bin/env python3
"""Finite N=120 lambda=4 discrepancy certificate; NOT complete-ground transfer."""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import tempfile
from typing import Any
from flint import acb, acb_mat, arb, ctx
import mpmath as mp
from archive import coarse as provenance


def load_benchmark() -> Any:
    path=provenance.ROOT/'evidence/v141/certify_ccm_semantic_lock.py'
    spec=importlib.util.spec_from_file_location('v141_benchmark',path)
    assert spec is not None and spec.loader is not None
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(bits: int) -> dict[str, Any]:
    ctx.prec=bits
    mp.mp.dps=190
    benchmark=load_benchmark()
    n=120
    with tempfile.TemporaryDirectory(prefix='ns18-lambda4-') as folder:
        asm=benchmark.load_assembly(Path(folder))
        length,b,d,_=asm.sequences(4,n,bits,128)
        even=asm.block(list(range(n+1)),list(range(n+1)),'even',b,d)
        odd=asm.block(list(range(1,n+1)),list(range(1,n+1)),'odd',b,d)
    values,vectors=acb_mat(even).eig(right=True,algorithm='rump')
    index=min(range(len(values)),key=lambda k:float(values[k].real.mid()))
    ground=values[index].real
    assert ground>0
    assert all(ground<value.real for k,value in enumerate(values) if k!=index)
    odd_values=acb_mat(odd).eig(algorithm='rump')
    assert all(ground<value.real for value in odd_values)
    coefficients=[(vectors[k,index]/vectors[0,index]).real for k in range(n+1)]
    assert coefficients[0].contains(1)
    coefficients[0]=arb(1)
    gamma=acb.zeta_zero(1).imag
    center=benchmark.mp_proposal(gamma,length,coefficients)
    radius='1e-110'
    interval=arb(center,radius)
    left,right=arb(center)-arb(radius),arb(center)+arb(radius)
    omega=[2*arb.pi()*k/length for k in range(n+1)]
    fl=benchmark.rational(left,coefficients,omega)
    fr=benchmark.rational(right,coefficients,omega)
    derivative=benchmark.derivative(interval,coefficients,omega)
    assert fl*fr<0 and not derivative.contains(0)
    assert not (interval*length/2).sin().contains(0)
    discrepancy=interval-gamma
    assert arb('2.9250e-71')<discrepancy<arb('2.9251e-71')
    direct=benchmark.centered_transform(gamma,length,coefficients)
    partial=2/length.sqrt()*(gamma*length/2).sin()*benchmark.rational(gamma,coefficients,omega)
    assert direct.overlaps(partial)
    return {'status':'PASS_FINITE_COMPRESSION_ONLY','lambda':4,'N':n,'K':128,'bits':bits,
            'ground':ground.str(110),'simple_even_global_finite_ground':True,
            'center_decimal':center,'radius_decimal':radius,
            'root_interval':interval.str(145,more=True),'gamma_1':gamma.str(145),
            'signed_finite_discrepancy':discrepancy.str(100),
            'left_rational':fl.str(100),'right_rational':fr.str(100),
            'rational_derivative':derivative.str(100),
            'direct_transform_identity_checked':True,
            'normalized_unshifted_even_coefficients':[v.str(145) for v in coefficients],
            'scope':'Finite compression only. The complete-root sign and factor-ten magnitude '
                    'remain unresolved; this value is not substituted for that requested result.',
            'assembly_sha256':provenance.sha256(benchmark.ASSEMBLY),
            'benchmark_helper_sha256':provenance.sha256(Path(benchmark.__file__)),
            'verifier_sha256':provenance.sha256(Path(__file__))}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits',type=int,choices=(1024,1280),required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    assert not args.output.exists(), 'Use a fresh output path.'
    result=run(args.bits)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],args.bits,result['signed_finite_discrepancy'],flush=True)


if __name__=='__main__':
    main()
