"""NS-36 diagnostic PSWF source construction and lambda=4 pure-witness projection.

Generalizes the finite-polynomial formula in the archived lambda=3 source
certificate. This script does NOT certify the PSWF truncation, repair, or source
projection. It explicitly records the raw center defect and the possible bump
repair scale, and compares two truncations/precisions. Historical certificate
files are read only. Run after feasibility_repair.py --raw-search.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
from flint import ctx

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "evidence/v124/g2_schur_cancellation"), str(Path(__file__).resolve().parent)]
from assembly_general import block, sequences
from feasibility_repair import matrices

OUT = Path(__file__).resolve().parent


def source(lam: int, size: int, digits: int, cutoff: int) -> tuple[Any, dict[str, Any]]:
    """Return normalized cosine coefficients of the raw finite-polynomial source."""
    mp.mp.dps = digits
    length = 2 * mp.log(lam)
    c = 2 * mp.pi * lam**2
    def link(n: int) -> Any:
        return mp.mpf(n+1) / mp.sqrt((2*n+1)*(2*n+3)) if n >= 0 else mp.mpf(0)
    operator = mp.matrix(size)
    for k in range(size):
        ell = 2*k
        operator[k,k] = ell*(ell+1) + c*c*(link(ell)**2 + link(ell-1)**2)
        if k < size-1:
            operator[k,k+1] = operator[k+1,k] = c*c*link(ell)*link(ell+1)
    eigenvalues, vectors = mp.eigsy(operator)
    polynomials = []
    for index in (0,2):
        poly = [vectors[k,index] * mp.sqrt(mp.mpf(4*k+1)/2) / mp.sqrt(lam) for k in range(size)]
        center = mp.fsum(poly[k] * (-1)**k * mp.binomial(2*k,k) / 4**k for k in range(size))
        poly = [mp.sign(center) * value for value in poly]
        polynomials.append(poly)
    p0, p4 = polynomials
    a0, a4 = -2*lam*p4[0], 2*lam*p0[0]
    hc = [a0*p0[k] + a4*p4[k] for k in range(size)]
    center = mp.fsum(hc[k] * (-1)**k * mp.binomial(2*k,k) / 4**k for k in range(size))
    monomials = [mp.fsum(hc[k] * (-1)**(k-r) * mp.factorial(2*k+2*r) /
        (2**(2*k)*mp.factorial(k-r)*mp.factorial(k+r)*mp.factorial(2*r))
        for k in range(r,size)) for r in range(size)]
    moments = [mp.fsum(mp.mpf(m)**(2*r) for m in range(1,lam**2+1)) /
               mp.mpf(lam)**(4*r) / mp.sqrt(lam) for r in range(size)]
    co = []
    for n in range(cutoff+1):
        tau = 2*mp.pi*n/length
        pole = mp.mpf('.5') + 1j*tau
        aa = mp.sqrt(lam) * mp.fsum(mp.exp(-pole*mp.log(m)) for m in range(1,lam**2+1))
        co.append(mp.re(mp.fsum(monomials[r]*(aa-moments[r])/(2*r+pole)
                                for r in range(size))) / mp.sqrt(length))
    normalized = mp.matrix([value*(mp.sqrt(2) if n else 1) for n,value in enumerate(co)])
    norm = mp.norm(normalized)
    normalized /= norm
    # The certificate's elementary map estimate for a bump of sup norm <=129.
    # Here center is only a numerical approximation, not an enclosed defect.
    repair_scale = mp.sqrt(lam**3 * length) * 129 * abs(center)
    meta = {'lambda':lam, 'size':size, 'digits':digits, 'cutoff':cutoff,
            'eigenvalues_0_4':[mp.nstr(eigenvalues[i],40) for i in (0,2)],
            'raw_source_center_defect':mp.nstr(center,40),
            'projected_raw_source_norm':mp.nstr(norm,40),
            'bump_repair_norm_scale_unenclosed':mp.nstr(repair_scale,40),
            'relative_bump_repair_scale_unenclosed':mp.nstr(repair_scale/norm,40),
            'positive_complex_coefficients':[mp.nstr(value,80) for value in co],
            'normalized_cosine_coefficients':[mp.nstr(value,80) for value in normalized]}
    return normalized, meta


def run(size: int, digits: int, refinement: int) -> None:
    raw = json.loads((OUT / 'feasibility_grid1.json').read_text())['raw_pure_search']['best']
    u, meta = source(4,size,digits,256)
    v = mp.matrix([mp.mpf(value) for value in raw['vector_decimal']])
    v /= mp.norm(v)
    overlap = (u.T*v)[0]
    projected = v - overlap*u
    projected /= mp.norm(projected)
    ctx.prec = 1024
    _,b,d,_ = sequences(4,264,1024)
    wb = block(list(range(257)),list(range(257)),'even',b,d)
    w = mp.matrix([[mp.mpf(wb[i,j].str(digits, radius=False)) for j in range(257)] for i in range(257)])
    masses,reference,_,_,_ = matrices(refinement)
    f = np.array([float(value) for value in projected])
    measured = np.array([f@m@f for m in masses])
    payload = {'status':'DIAGNOSTIC, NOT A CERTIFICATE', 'source':meta,
        'refinement':refinement, 'raw_witness_source_overlap':mp.nstr(overlap,40),
        'projected_witness_internal_source_overlap':mp.nstr((u.T*projected)[0],20),
        'projected_witness_exported_source_overlap':mp.nstr((
            mp.matrix(meta['normalized_cosine_coefficients']).T *
            mp.matrix([mp.nstr(value,80) for value in projected]))[0],25),
        'raw_energy':mp.nstr((v.T*w*v)[0],40),
        'projected_energy':mp.nstr((projected.T*w*projected)[0],40),
        'min_ratio':float(np.min(measured/reference)), 'reference_masses':reference.tolist(),
        'bin_masses':measured.tolist(), 'all_slacks':(measured-reference).tolist(),
        'projected_vector_decimal':[mp.nstr(value,80) for value in projected]}
    path = OUT/f'source_projection_M{size}_d{digits}_grid{refinement}.json'
    path.write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({key:value for key,value in payload.items() if key not in
                     ('source','projected_vector_decimal','reference_masses','bin_masses','all_slacks')},indent=2),flush=True)
    print('source center',meta['raw_source_center_defect'],'relative repair scale',
          meta['relative_bump_repair_scale_unenclosed'],flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--size',type=int,default=90)
    parser.add_argument('--digits',type=int,default=130)
    parser.add_argument('--refinement',type=int,default=1)
    parser.add_argument('--validate-lambda3',action='store_true')
    args = parser.parse_args()
    if args.validate_lambda3:
        _,meta = source(3,70,110,64)
        old = json.loads((ROOT/'evidence/v124/g2_source_certificate/source_polynomial_intervals.json').read_text())
        exact = [mp.mpf(value.strip('[]').split('+/-')[0]) for value in old['projected_positive_coefficients']]
        err = max(abs(mp.mpf(v)-e) for v,e in zip(meta['positive_complex_coefficients'],exact))
        result = {'status':'diagnostic normalization check against archived lambda=3 intervals',
                  'maximum_midpoint_difference':mp.nstr(err,40)}
        (OUT/'source_loader_lambda3_check.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result),flush=True)
    else:
        run(args.size,args.digits,args.refinement)


if __name__ == '__main__':
    main()
