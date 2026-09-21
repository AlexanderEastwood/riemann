"""Sensitivity of the NS-2 test to deliberate assembly perturbations (N=30, lambda=3).
Diagnostic; not a certificate.  Run from the repo root with .venv/bin/python."""
import sys, tempfile; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from pathlib import Path
import mpmath as mp
from flint import arb, ctx
import reproduce_ccm as R
mod=R.load_assembly(Path(tempfile.mkdtemp()))
N=30; bits=512; dps=80; M=9
def base():
    ctx.prec=bits; return R.sequences_M(M,N,bits,96)
def diffs(b,d,zero_mode_factor=None):
    ctx.prec=bits
    T=mod.block(range(0,N+1),range(0,N+1),'even',b,d)
    digits=int(bits*.30103)-2
    mp.mp.dps=dps
    A=mp.matrix(N+1,N+1)
    for i in range(N+1):
        for j in range(N+1):
            A[i,j]=R.arb_to_mpf(T[i,j],digits)
    if zero_mode_factor is not None:
        for j in range(1,N+1):
            A[0,j]*=zero_mode_factor; A[j,0]*=zero_mode_factor
    E,Q=mp.eigsy(A); i0=min(range(N+1),key=lambda i:E[i])
    v=[Q[i,i0] for i in range(N+1)]
    with mp.workdps(120): gam=[mp.im(mp.zetazero(k)) for k in range(1,6)]
    L=mp.mpf(arb(M).log().mid().str(digits,radius=False))
    roots,sc=R.zeros_of_xi_hat(v,L,gam,dps)
    return E[i0],[ (mp.nstr(abs(g-r),4) if r is not None else None) for g,r in zip(gam,roots)],len(sc)
L,b,d,a=base()
print('baseline           ', diffs(b,d))
print('zero-mode sqrt2->1 ', diffs(b,d,zero_mode_factor=1/mp.sqrt(2)))
# prime term scaled by (1+1e-8): recompute prime sums
ctx.prec=bits; pi=arb.pi(); Lb=arb(M).log()
pw=[(arb(m).log(),arb(p).log()/arb(m).sqrt()) for m,p in R.pairs_M(M)]
def prime_parts(n):
    t=2*pi*n/Lb
    return sum(((t*y).sin()*w for y,w in pw),arb(0))/pi, -2*sum(((t*y).cos()*(1-y/Lb)*w for y,w in pw),arb(0))
for eps_ in ['1e-8','1e-20','1e-40']:
    e=arb(eps_)
    b2=[bn+e*prime_parts(n)[0] for n,bn in enumerate(b)]
    d2=[dn+e*prime_parts(n)[1] for n,dn in enumerate(d)]
    print(f'prime term x(1+{eps_})', diffs(b2,d2))
# archimedean diagonal sign flipped
d3=[dn-2*an for dn,an in zip(d,a)]
print('arch diagonal sign ', diffs(b,d3))
# drop the pole term entirely
h=(Lb/4).sinh()**2
b4=[bn-32*Lb*h*n/(Lb*Lb+16*pi*pi*n*n) for n,bn in enumerate(b)]
d4=[dn-32*Lb*h*(Lb*Lb-16*pi*pi*n*n)/(Lb*Lb+16*pi*pi*n*n)**2 for n,dn in enumerate(d)]
print('pole term dropped  ', diffs(b4,d4))
