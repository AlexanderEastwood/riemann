#!/usr/bin/env python3
"""Reproduce refinement and direct-correlation checks after the pilot runs."""
import json
from pathlib import Path
import mpmath as mp


def main():
    base=Path(__file__).resolve().parent
    mp.mp.dps=90
    data=json.loads((base/'g2_spectral_mp_checks.json').read_text())
    differences=[]
    for i in range(3):
        a,b=data['rows'][i],data['rows'][i+3]
        wa,wb=mp.matrix(a['matrix_N32']),mp.matrix(b['matrix_N32'])
        ca,cb=mp.matrix(a['coefficient_vector_N32']),mp.matrix(b['coefficient_vector_N32'])
        differences.append(dict(lambda_=a['source']['lambda_'],
            observed_matrix_frobenius_difference=mp.nstr(mp.norm(wa-wb),25),
            observed_source_coefficient_difference=mp.nstr(mp.norm(ca-cb),25),
            relative_B_difference=mp.nstr(abs(mp.mpf(a['source']['B_physical'])/mp.mpf(b['source']['B_physical'])-1),25)))
    (base/'g2_spectral_refinement_differences.json').write_text(json.dumps(dict(
        status='Observed differences only. Matrix/vector strings stored to 70 significant digits, B to 30; zero means agreement at stored precision, not zero true error.',
        rows=differences),indent=2)+'\n')
    W=mp.matrix(data['rows'][-1]['matrix_N32']); L=2*mp.log(3)
    checks=[]
    for n,m in [(0,0),(1,1),(0,1),(1,-1),(3,8)]:
        tn,tm=2*mp.pi*n/L,2*mp.pi*m/L
        def q(y):
            return 2*(1-y/L)*mp.cos(tn*y) if n==m else (mp.sin(tm*y)-mp.sin(tn*y))/(mp.pi*(n-m))
        pole=mp.quad(lambda y: (mp.exp(y/2)+mp.exp(-y/2))*q(y),[0,L])
        pp=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
        prime=mp.fsum(mp.log(p)/mp.sqrt(k)*q(mp.log(k)) for k,p in pp)
        def arch(y):
            if y==0:
                return mp.mpf('.5')-1/L if n==m else (tm-tn)/(2*mp.pi*(n-m))
            return mp.exp(y/2)/(2*mp.sinh(y))*(q(y)-(2*mp.exp(-y/2) if n==m else 0))
        aval=mp.quad(arch,[0,L/4,L/2,L])
        if n==m: aval+=mp.log(4*mp.pi)+mp.euler+mp.log(mp.tanh(L/2))
        direct=pole-prime-aval
        checks.append(dict(n=n,m=m,direct=mp.nstr(direct,60),matrix=mp.nstr(W[32+n,32+m],60),
            absolute_difference=mp.nstr(abs(direct-W[32+n,32+m]),15)))
    (base/'g2_direct_form_checks.json').write_text(json.dumps(dict(
        status='Independent adaptive high-precision correlation integration, not interval certified.',rows=checks),indent=2)+'\n')
    print(json.dumps(dict(refinement=differences,max_direct_form_difference=
        max(float(x['absolute_difference']) for x in checks)),indent=2))


if __name__=='__main__':
    main()
