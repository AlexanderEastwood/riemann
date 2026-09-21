#!/usr/bin/env python3
"""Numerical input generator only. The separate interval verifier certifies it."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=110
M=70;c=18*mp.pi
A=mp.matrix(M)
a=lambda n:(n+1)/mp.sqrt((2*n+1)*(2*n+3)) if n>=0 else mp.mpf(0)
for k in range(M):
 l=2*k; A[k,k]=l*(l+1)+c*c*(a(l)**2+a(l-1)**2)
 if k<M-1:A[k,k+1]=A[k+1,k]=c*c*a(l)*a(l+1)
e,v=mp.eigsy(A)
rows=[]
for j in [0,2]:
 center=mp.fsum(v[k,j]*mp.sqrt(mp.mpf(4*k+1)/2)*(-1)**k*mp.binomial(2*k,k)/4**k for k in range(M))
 sign=mp.sign(center)
 rows.append(dict(mode=2*j,xi=mp.nstr(e[j],100),coefficients=[mp.nstr(sign*v[k,j],100) for k in range(M)]))
path=Path(__file__).with_name('pswf_rational_input.json')
path.write_text(json.dumps(dict(lambda_exact=3,even_dimension=M,definition='Exact decimal rational input vectors; normalize exactly before certifying. These strings do not assume numerical eigenvector accuracy.',rows=rows),indent=2)+'\n')
print('Frozen input',[(x['mode'],x['xi'][:30]) for x in rows],flush=True)
