#!/usr/bin/env python3
"""Rigorous Arb evaluation of analytic high-Fourier tail constants, lambda=3."""
import json
from pathlib import Path
from flint import arb, ctx

ctx.prec = 256
BASE = Path(__file__).resolve().parent
L = 2*arb(3).log()
pi = arb.pi()
R = arb(27)/80
h = arb(1)/3
w = {m: arb(p).log()/arb(m).sqrt()
     for m,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]}
P = sum(w.values(), arb(0))
degrees = [P, P-w[8], P-w[8]-w[7], w[2]+w[3]+w[4],
           2*w[2]+w[3]+w[4], 2*w[2]+w[3]]
assert all(P > value for value in degrees[1:])
assert arb(1) > arb(1)/4+R
rows=[]
for N in [252,253,256,512]:
    t = 2*pi*(N+1)/L
    E = 1/(15*t)+arb(7)/(2*t*t)+pi/(2*L*t)+(2+2*R)/(L*t*t)
    pole = 4*h*L/(pi*pi*N)
    even = (arb(N+1)/L).log()-P-2/t-E
    full = even-pi/2-pole
    if N == 256:
        assert full > arb('0.0148')
        assert even > arb('1.5867')
    if N == 512:
        assert full > arb('0.7085')
    rows.append(dict(N=N,t_min=t.str(65),diagonal_error=E.str(65),
                     arch_offdiagonal_error=(2/t).str(65),
                     negative_pole_tail=pole.str(65),
                     full_tail_lower=full.str(65),even_tail_lower=even.str(65)))
result=dict(status='PASS',scope='Scalar interval evaluation of proved analytic tail constants; no head/Schur certification.',
            lambda_exact=3,precision_bits=ctx.prec,L=L.str(65),prime_degree=P.str(65),
            degree_interval_values=[v.str(65) for v in degrees],rows=rows)
(BASE/'sharp_tail_constants.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
