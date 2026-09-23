"""Numerical illustration: explicit old-space NB corrections, not certificates."""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import cho_factor, cho_solve, eigvalsh

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'diag_ns59_nb_budget'))
from scan_blocks import build_float

Array = NDArray[np.float64]


def mu(n: int) -> int:
    result=1
    divisor=2
    while divisor*divisor<=n:
        if n%divisor==0:
            n//=divisor
            result=-result
            if n%divisor==0:
                return 0
        divisor+=1
    return -result if n>1 else result


def correction_map(size: int, weights: dict[int,float]) -> Array:
    result=np.zeros((size,size))
    for n in range(size+1,2*size+1):
        for d,weight in weights.items():
            if d==1 or weight==0:
                continue
            m=(n+d-1)//d
            result[m-1,n-size-1]+=weight*m/(d*n)
    return result


def inspect(gram: Array,loads: Array,size: int) -> dict[str,Any]:
    full=gram[:2*size,:2*size]
    basis=np.eye(2*size)
    for n in range(2,2*size+1):
        basis[n-2,n-1]=-(n-1)/n
    old_basis,new_basis=basis[:,:size],basis[:,size:]
    delta_gram=basis.T@full@basis
    old_delta=delta_gram[:size,:size]
    cross=delta_gram[:size,size:]
    raw=delta_gram[size:,size:]
    factor=cho_factor(gram[:size,:size],lower=True)
    residual_load=loads[size:2*size]-gram[size:2*size,:size]@cho_solve(factor,loads[:size])
    g=basis[size:,size:].T@residual_load
    energy=1-float(loads[:size]@cho_solve(factor,loads[:size]))
    schur=raw-cross.T@cho_solve(cho_factor(old_delta,lower=True),cross)
    schur=(schur+schur.T)/2
    gain=float(g@cho_solve(cho_factor(schur,lower=True),g))
    g2=float(g@g)
    families:dict[str,dict[int,float]]={'raw':{1:1.0}}
    for product in [2,6,30]:
        families[f'euler_{product}']={d:float(mu(d)) for d in range(1,product+1) if product%d==0}
    for length in [4,16,64]:
        families[f'selberg_{length}']={d:mu(d)*(1-math.log(d)/math.log(length)) for d in range(1,length+1)}
    results:dict[str,Any]={}
    for name,weights in families.items():
        correction=correction_map(size,weights)
        corrected=raw+cross.T@correction+correction.T@cross+correction.T@old_delta@correction
        corrected=(corrected+corrected.T)/2
        value=float(g@corrected@g)
        eigen=eigvalsh(corrected)
        results[name]={'operator_norm_scaled':float(eigen[-1])*size**2,
                       'minimum_eigenvalue_scaled':float(eigen[0])*size**2,
                       'selected_rayleigh_scaled':value/g2*size**2,
                       'selected_gain_relative':g2*g2/value/energy,
                       'trace':float(np.trace(corrected)),
                       'minimum_eigenvalue_above_optimal':float(eigvalsh(corrected-schur)[0])}
    return {'N':size,'E_N':energy,'gain_relative':gain/energy,
            'g_norm2_over_E_scaled':g2/energy*size**2,
            'projected_operator_norm_scaled':float(eigvalsh(schur)[-1])*size**2,
            'projected_selected_rayleigh_scaled':float(g@schur@g)/g2*size**2,
            'projected_direction_gain_relative':g2*g2/float(g@schur@g)/energy,
            'families':results}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-index',type=int,default=1024)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    start=time.monotonic()
    gram,loads=build_float(args.max_index)
    rows=[]
    size=32
    while 2*size<=args.max_index:
        row=inspect(gram,loads,size)
        rows.append(row)
        print(size,{k:round(v['selected_rayleigh_scaled'],6) for k,v in row['families'].items()},flush=True)
        size*=2
    args.output.write_text(json.dumps({'classification':'numerical illustration, not a certificate',
                                      'max_index':args.max_index,'elapsed_seconds':time.monotonic()-start,
                                      'rows':rows},indent=2)+'\n')


if __name__=='__main__':
    main()
