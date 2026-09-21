#!/usr/bin/env python3
"""Rigorous scale check for the analytic omitted-Fourier-tail theorem.

Requires python-flint 0.9.0. Does not assemble or certify a full window.
The archimedean zero-mode integral is regularized exactly at zero.
"""
from pathlib import Path
import json
from flint import arb, acb, ctx

ctx.prec = 256
base = Path(__file__).resolve().parent
lam = arb(3)
L = 2*lam.log()
pi = arb.pi()
ii = acb(0, 1)
def integrand(y, analytic):
    return (y/2).exp()/(ii*y).sinc()*((-y/4).exp()*(ii*y/4).sinc()/2-1/L)
val = acb.integral(integrand, 0, L, abs_tol=arb('1e-60'), rel_tol=arb('1e-60'))
assert val.is_finite() and val.imag.contains(0)
A0 = val.real + (4*pi).log() + arb.const_euler() + (L/2).tanh().log()
pairs = [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
P = sum((arb(p).log()/arb(m).sqrt() for m,p in pairs), arb(0))
Bm = (4*(L/4).sinh()**2+P+1+pi/4)/pi
a = arb(1)
C = abs(A0)+4+pi/2+a+2*a/L+2*P+2*(L/2).sinh()-L
threshold = L/(2*pi*a)*(C+1).exp()
# Choose a deliberately coarse decimal cutoff, then prove Gamma>1.
N = 50_000_000
Gamma = (2*pi*(N+1)*a/L).log()-C
assert Gamma > 1
out = dict(status='PASS', lambda_exact=3, precision_bits=ctx.prec,
    complete_arch_diagonal_zero=A0.str(50), prime_mass=P.str(50),
    bounded_b_constant=Bm.str(50), tail_constant=C.str(50),
    threshold_for_Gamma_one=threshold.str(50), chosen_N=N,
    gamma_at_chosen_N=Gamma.str(50),
    scope='Analytic tail constant only. No finite head sign, head-tail Schur sign, whole-window positivity or G2 is certified.')
(base/'tail_constant_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
