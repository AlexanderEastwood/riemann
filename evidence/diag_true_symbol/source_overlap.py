"""Diagnostic, not a certificate.  Are the pencil directions source-admissible?
lambda=3, even head N=64: the certified projected source u (evidence/v124/g2_source_certificate/
source_polynomial_intervals.json, 'projected_positive_coefficients', block() basis) is normalized;
we check its angle to the finite Weil ground (certificate: sin < 2.16e-4), the overlaps b_k = <v_k,u>
with the pencil vectors of section 7, and the pencil restricted to the source complement u^perp.
Run from the repo root with .venv/bin/python."""
import sys, json, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
from pencil import beta_grid, Fe_grid
lam,N,bits,dps=3,64,1024,120
src=json.load(open('evidence/v124/g2_source_certificate/source_polynomial_intervals.json'))['projected_positive_coefficients']
u=np.array([float(mp.mpf(s.strip('[]').split('+/-')[0])) for s in src]); assert len(u)==N+1
u[0]/=math.sqrt(2)   # the file stores the n=0 coefficient against the unnormalized constant mode; block() uses 1/sqrt(L): angle check below confirms
u/=np.linalg.norm(u)
# exact W and quadrature W^- as in pencil.py
XI=4000.0; xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.01)]); hs=np.where(xs<40,0.002,0.01)
beta,L=beta_grid(lam,xs); neg=np.maximum(-beta,0.0)
F=np.array([Fe_grid(n,L,xs) for n in range(N+1)]); sgn=np.array([(-1)**n for n in range(N+1)],float)
Wm=2*(F*(neg*hs))@F.T; Wm=sgn[:,None]*Wm*sgn[None,:]
ctx.prec=bits; Lq,b,d,aa=sequences(lam,N+8,bits); rows=list(range(N+1)); Wb=block(rows,rows,'even',b,d)
mp.mp.dps=dps; W=tomp(Wb,dps); Wp=W+mp.matrix(Wm.tolist())
E,Q=mp.eigsy(W); i0=min(range(N+1),key=lambda k:E[k]); g=np.array([float(Q[k,i0]) for k in range(N+1)])
sin_angle=math.sqrt(max(0.0,1-float(abs(g@u))**2))
print(f"lambda={lam} N={N}: ground eigenvalue {mp.nstr(E[i0],4)}; |<ground,u>| = {abs(g@u):.8f}, sin(angle) = {sin_angle:.3e}  (certificate: < 2.16e-4)")
def pencil(Wx,Wpx):
    C=mp.cholesky(Wpx); Ci=mp.inverse(C); M=Ci*Wx*Ci.T; M=(M+M.T)/2
    nu,U=mp.eigsy(M); V=Ci.T*U; order=sorted(range(Wx.rows),key=lambda k:nu[k])
    return [nu[k] for k in order],[np.array([float(V[j,k]) for j in range(Wx.rows)]) for k in order]
nu,V=pencil(W,Wp)
print("full head pencil: k, nu_k, |b_k| = |<v_k,u>| (v_k Euclidean-normalized)")
for k in range(10):
    v=V[k]/np.linalg.norm(V[k]); print(f"  k={k:2d}  nu={mp.nstr(nu[k],4):>10}   |b_k|={abs(v@u):.6f}")
# complement: orthonormal basis of u^perp via Householder
Hh=np.eye(N+1)-2*np.outer(u,u)/(u@u); B=np.delete(np.linalg.qr(np.column_stack([u,np.eye(N+1)]))[0],0,axis=1)  # (N+1) x N basis of u^perp
assert np.allclose(B.T@u,0,atol=1e-12) and np.allclose(B.T@B,np.eye(N),atol=1e-12)
Bm=mp.matrix(B.tolist()); Wc=Bm.T*W*Bm; Wpc=Bm.T*Wp*Bm
nuc,Vc=pencil(Wc,Wpc)
print("source-complement pencil (E = head ∩ u^perp): k, nu'_k   vs full-head nu_{k+1}")
for k in range(10):
    print(f"  k={k:2d}  nu'={mp.nstr(nuc[k],4):>10}    full nu_{k+1}={mp.nstr(nu[k+1],4):>10}")
Ec=sorted(mp.eigsy(Wc)[0]); print(f"complement Rayleigh floor (min eig of W on u^perp) = {mp.nstr(Ec[0],4)}  vs full ground {mp.nstr(E[i0],4)}, second {mp.nstr(sorted(E)[1],4)}")
