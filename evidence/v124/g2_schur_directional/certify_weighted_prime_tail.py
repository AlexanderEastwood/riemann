#!/usr/bin/env python3
"""Arb certificate of a positive-weight Schur bound for lambda=3 prime shifts.

Only scalar exact rational coefficient comparisons and analytic tail constants
are certified. No head matrix or signed Schur complement is certified here.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
from flint import arb, ctx

ctx.prec = 256
OUT = Path(__file__).resolve().parent
powers = {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2}
weights = {m: arb(p).log()/arb(m).sqrt() for m,p in powers.items()}

def ab(q):
    return arb(q.numerator)/q.denominator

def val(coeff):
    return sum((ab(q)*weights[m] for m,q in coeff.items()), arb(0))

# The maximum is approached from u>7, equivalently from u<9/7.
maximum_coeff = {m: Q(49+9*m*m,58*m) if m != 8 else Q(0)
                 for m in powers}
maximum = val(maximum_coeff)
cuts = sorted({Q(1),Q(9)} | {Q(m) for m in powers}
              | {Q(9,m) for m in powers})
checks=[]
for left,right in zip(cuts,cuts[1:]):
    mid=(left+right)/2
    forward=[m for m in powers if mid*m<9]
    backward=[m for m in powers if mid>m]
    for endpoint in (left,right):
        q2=endpoint*endpoint
        coeff={m:Q(0) for m in powers}
        for m in forward:
            coeff[m]+=(m*q2+Q(9,m))/(q2+9)
        for m in backward:
            coeff[m]+=(q2/m+9*m)/(q2+9)
        difference={m:maximum_coeff[m]-coeff[m] for m in powers}
        if any(difference.values()):
            assert val(difference)>0, (left,right,endpoint,val(difference))
        checks.append(dict(interval=[str(left),str(right)],endpoint=str(endpoint),
                           ratio=val(coeff).str(60),
                           exact_equality=not any(difference.values())))

L=2*arb(3).log(); pi=arb.pi(); h=arb(1)/3; R=arb(27)/80
rows=[]
for N in [155,156,160,256,512]:
    t=2*pi*(N+1)/L
    error=1/(15*t)+arb(7)/(2*t*t)+pi/(2*L*t)+(2+2*R)/(L*t*t)
    even=(arb(N+1)/L).log()-maximum-2/t-error
    full=even-pi/2-4*h*L/(pi*pi*N)
    if N==256:
        assert full>arb('0.4970')
        assert even>arb('2.0689')
    if N==160:
        assert full>0
    rows.append(dict(N=N,even_lower=even.str(60),full_lower=full.str(60)))

result=dict(status='PASS',precision_bits=ctx.prec,lambda_exact=3,
            weight='phi(x)=cosh(x-log(3))',
            weighted_prime_bound=maximum.str(60),
            maximum_coefficients={str(m):str(q) for m,q in maximum_coeff.items()},
            endpoint_checks=checks,tail_rows=rows,
            scope='Scalar weighted-prime and omitted-tail certificate only; no head/Schur sign.')
(OUT/'weighted_prime_tail_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='endpoint_checks'},indent=2))
