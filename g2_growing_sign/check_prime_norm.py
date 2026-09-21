"""Non-certified consistency checks for the analytic prime-norm theorems."""
from pathlib import Path
from fractions import Fraction
import json
import math
import numpy as np
import mpmath as mp

b = Path(__file__).resolve().parent
mp.mp.dps = 60

def weights(bound):
    sieve = np.ones(bound + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(bound) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    vals = np.zeros(bound + 1)
    for p in np.flatnonzero(sieve):
        k = int(p)
        while k <= bound:
            vals[k] = math.log(int(p))
            k *= int(p)
    ms = np.flatnonzero(vals)
    return ms, vals[ms]

rows = []
for lam in [2, 3, 5, 10, 30, 100, 300]:
    L = 2 * math.log(lam)
    ms, lm = weights(lam * lam - 1)
    s = np.log(ms)
    # Exact analytic autocorrelation of phi=e^(-x/2)+e^(-(L-x)/2).
    corr = 2*np.exp(-s/2)*(1-np.exp(-(L-s))) + 2*(L-s)/lam*np.cosh(s/2)
    norm2 = 2*(1-lam**-2)+2*L/lam
    trial = 2*float(np.sum(lm/np.sqrt(ms)*corr))/norm2
    # A second evaluation integrates the exact pointwise ratio against phi^2.
    # At lambda=2,3 use high precision piecewise quadrature at every shift cut.
    diff = None
    if lam <= 3:
        l = 2*mp.log(lam)
        # Recover each exact von Mangoldt weight from the integer prime power.
        active = []
        for m in ms:
            for p in range(2, int(m)+1):
                if int(m)%p == 0:
                    active.append((int(m),mp.log(p)))
                    break
        cuts=sorted(set([mp.mpf(0),l]+[mp.log(m) for m,_ in active]+[l-mp.log(m) for m,_ in active]))
        phi=lambda x: mp.exp(-x/2)+mp.exp(-(l-x)/2)
        total=mp.mpf(0)
        for left,right in zip(cuts,cuts[1:]):
            mid=(left+right)/2
            forward=[(mp.log(m),v/mp.sqrt(m)) for m,v in active if mid+mp.log(m)<l]
            backward=[(mp.log(m),v/mp.sqrt(m)) for m,v in active if mid>mp.log(m)]
            total += mp.quad(lambda x: phi(x)*(sum(w*phi(x+a) for a,w in forward)+sum(w*phi(x-a) for a,w in backward)),[left,right])
        exact_corr=lambda a: 2*mp.exp(-a/2)*(1-mp.exp(-(l-a)))+2*(l-a)/lam*mp.cosh(a/2)
        second=2*sum(v/mp.sqrt(m)*exact_corr(mp.log(m)) for m,v in active)
        diff=mp.nstr(abs(total-second),8)
        assert abs(total-second)<mp.mpf('1e-50')
    rows.append(dict(lambda_=lam,trial_rayleigh=trial,trial_over_lambda=trial/lam,independent_quadrature_difference=diff))

lam=mp.mpf(2)
L=2*mp.log(lam)
norm2=2*(1-lam**-2)+2*L/lam
corr=lambda a: 2*mp.exp(-a/2)*(1-mp.exp(-(L-a)))+2*(L-a)/lam*mp.cosh(a/2)
alpha=mp.log(3)/mp.log(2)
base=2*sum(mp.log(m)/mp.sqrt(m)*corr(mp.log(m)) for m in [2,3])/norm2
recurrences=[]
for cap in [100,1000,10000,100000,1000000]:
    frac=Fraction(str(alpha)).limit_denominator(cap)
    q=frac.denominator
    k=2*q
    phase=2*mp.pi*(q*alpha-frac.numerator)
    ray=2*sum(mp.log(m)/mp.sqrt(m)*corr(mp.log(m))*mp.cos(2*mp.pi*k*mp.log(m)/L) for m in [2,3])/norm2
    phihat=lambda n: (1-1/lam)/(mp.sqrt(L)*((2*mp.pi*n/L)**2+mp.mpf('0.25')))
    head=mp.sqrt(sum(phihat(n-k)**2 for n in range(-64,65))/norm2)
    recurrences.append(dict(modulation_index=k,prime3_phase_error=mp.nstr(abs(phase),12),rayleigh=mp.nstr(ray,16),unmodulated_rayleigh=mp.nstr(base,16),P64_norm=mp.nstr(head,12)))

out=dict(status='PASS: non-certified numerical diagnostics only',scope='Analytic autocorrelation normalization and illustrative simultaneous prime-phase recurrence; no Weil sign or asymptotic theorem is inferred from these numbers.',growth_trials=rows,lambda2_recurrence=recurrences)
(b/'prime_norm_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
