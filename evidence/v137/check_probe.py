"""Diagnostic quadrature and exact rational gates for the cutoff-side-lobe proof.

No Weil eigenvalue or RH sign is inferred from these computations.
The manuscript supplies analytic proofs of the inequalities.
"""
from fractions import Fraction
from pathlib import Path
import json
import math

delta=1/100
def quad(f,a,b,tol=1e-12):
    def sim(a,b,fa,fm,fb): return (b-a)*(fa+4*fm+fb)/6
    fa,fb=f(a),f(b);m=(a+b)/2;fm=f(m);whole=sim(a,b,fa,fm,fb)
    def rec(a,b,fa,fm,fb,s,tol,depth):
        m=(a+b)/2; l=(a+m)/2;r=(m+b)/2;fl,fr=f(l),f(r)
        left,right=sim(a,m,fa,fl,fm),sim(m,b,fm,fr,fb)
        error=left+right-s
        if depth==0 or abs(error)<15*tol:return left+right+error/15
        return rec(a,m,fa,fl,fm,left,tol/2,depth-1)+rec(m,b,fm,fr,fb,right,tol/2,depth-1)
    return rec(a,b,fa,fm,fb,whole,tol,25)

def bump(x):
    return math.exp(-1/(1-x*x)) if abs(x)<1 else 0.
z=quad(bump,-1,0)+quad(bump,0,1)
def average(fun):
    f=lambda x:bump(x)*fun(delta*x)
    return (quad(f,-1,0)+quad(f,0,1))/z
def kappa_hat(t):
    return average(lambda v:math.cos(t*v))
def H(t):
    s=2*math.pi if t==0 else 2*math.sin(math.pi*t)/t
    return complex(math.cos(2*math.pi*t),-math.sin(2*math.pi*t))*s*kappa_hat(t)

c0=quad(lambda s:math.sin(s)/s,math.pi,3*math.pi)
k0=2*average(lambda v:quad(lambda s:math.sin(s)/s,math.pi+v,3*math.pi+v))
# pi < 22/7 proves pi/100 < 1/(6*pi), without floating point.
assert Fraction(6)*Fraction(22,7)**2 < 100
assert k0 < -1/(3*math.pi)
assert abs(H(1))<1e-13
assert abs(H(-1))<1e-13

# Unsmeared single atom: integral 2T sinc(T xi) times 1_[pi,3pi](T xi).
# It is exactly 2*C0 at every T; quadrature independently checks the scaling.
atom_checks=[]
for T in [2,7,19,100]:
    value=quad(lambda xi:2*math.sin(T*xi)/xi,math.pi/T,3*math.pi/T)
    assert abs(value-2*c0)<1e-10
    atom_checks.append({'T':T,'pairing':value})

result={'status':'analytic sign/endpoint gates and numerical scaling checks passed',
 'scope':'probe and isolated spectral-atom diagnostics; not a numerical proof of the arithmetic theorem',
 'delta':'1/100','unsmeared_sinc_integral':c0,
 'smoothed_K0':k0,'proved_upper_bound_on_K0':'-1/(3*pi)',
 'proved_total_variation_of_w':2,'proved_mass_of_w':'2*pi',
 'exact_rational_gate':'6*(22/7)^2 < 100',
 'endpoint_residual_abs':abs(H(1)),'atom_scaling':atom_checks,
 'quadrature':'binary64 adaptive Simpson diagnostic; not interval-certified'}
out=Path(__file__).with_name('probe_results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
