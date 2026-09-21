"""Diagnostic, not a certificate.  Level pencil of the validated symbol on the even head:
   W v = nu (W + W^-) v,   W^- = int beta_a^- |F e|^2 (negative level, float quadrature), W = block() (Arb).
   nu_k = q[v]/q+[v] is the relative positive-level surplus in direction k (nu >= 0 everywhere is positivity);
   compared with W's own eigenvalues e_k.  W^- is accurate to ~1e-7 relative, so nu_k carries ~7 digits of
   RELATIVE accuracy however small it is (the numerator is exact).  Run from the repo root with .venv/bin/python."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block, pairs
from cert import tomp

def beta_grid(lam, xs):
    a=math.log(lam); L=2*a
    pw=[(math.log(m), math.log(p)/math.sqrt(m)) for m,p in pairs(lam)]
    r=np.zeros_like(xs)
    for y,w in pw: r+=2*w*np.cos(xs*y)
    c=0.5+1j*xs; r-=2*np.real((np.exp(c*L)-1)/c)
    z=1.25+0.5j*xs; psi=np.empty_like(xs); lo=xs<40
    psi[lo]=[float(mp.re(mp.digamma(mp.mpc(1.25,0.5*x)))) for x in xs[lo]]
    zz=z[~lo]; B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6]
    s=np.log(zz)-1/(2*zz)
    for k,b in enumerate(B,1): s-=b/(2*k*zz**(2*k))
    psi[~lo]=np.real(s)
    return psi-math.log(math.pi)-r, L

def Fe_grid(n, L, xs):
    if n==0: return (1/math.sqrt(L))*2*np.sin(xs*L/2)/xs/math.sqrt(2*math.pi)
    w=2*math.pi*n/L
    return math.sqrt(2/L)*(np.sin((w-xs)*L/2)/(w-xs)+np.sin((w+xs)*L/2)/(w+xs))/math.sqrt(2*math.pi)

def run(lam, N, bits, XI=4000.0, dps=120):
    t=time.time()
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.01)])
    hs=np.where(xs<40,0.002,0.01)
    beta,L=beta_grid(lam,xs); neg=np.maximum(-beta,0.0)
    F=np.array([Fe_grid(n,L,xs) for n in range(N+1)]); sgn=np.array([(-1)**n for n in range(N+1)],float)
    Wq=2*(F*(beta*hs))@F.T; Wm=2*(F*(neg*hs))@F.T
    # analytic tail of the full-symbol quadrature for EVERY entry: for xi >> 2 pi n/L,
    # Fe_n ~ (-1)^n c_n 2 sin(xi L/2)/xi/sqrt(2 pi), c_0=1/sqrt L, c_n=sqrt(2/L); sin^2 -> 1/2; beta ~ log(xi/2)-log pi
    I=float(mp.quad(lambda x:(mp.log(x/2)-mp.log(mp.pi))*2/(x**2)/(2*mp.pi),[XI,mp.inf]))
    cn=np.array([1/math.sqrt(L)]+[math.sqrt(2/L)]*N)
    Wq+=2*(sgn*cn)[:,None]*(sgn*cn)[None,:]*I          # factor 2: two-sided integral, as in beta_check2.py
    Wq=sgn[:,None]*Wq*sgn[None,:]; Wm=sgn[:,None]*Wm*sgn[None,:]
    ctx.prec=bits; Lq,b,d,aa=sequences(lam,N+8,bits); rows=list(range(N+1))
    Wb=block(rows,rows,'even',b,d); Wf=np.array([[float(Wb[i,j].mid()) for j in rows] for i in rows])
    big=np.abs(Wf)>1e-2; relerr=np.max(np.abs(Wq-Wf)[big]/np.abs(Wf)[big])
    # high-precision pencil  W v = nu W+ v,  W+ = W + W^-  (W exact from Arb, W^- float)
    mp.mp.dps=dps
    W=tomp(Wb,dps); Wp=W+mp.matrix(Wm.tolist())
    C=mp.cholesky(Wp); Ci=mp.inverse(C); M=Ci*W*Ci.T; M=(M+M.T)/2
    nu,U=mp.eigsy(M); order=sorted(range(N+1),key=lambda k:nu[k]); nu=[nu[k] for k in order]
    E=mp.eigsy(W)[0]; E=sorted(E)
    Wpe=sorted(mp.eigsy(Wp)[0])
    print(f"lambda={lam} N={N} bits={bits}: neg.set ends {xs[beta<0].max():.0f} (grid {XI:.0f}); quadrature vs block() on |W|>1e-2: {relerr:.1e}; "
          f"spec(W+) in [{float(Wpe[0]):.3f},{float(Wpe[-1]):.3f}]  [{time.time()-t:.0f}s]")
    print("   k   nu_k = q/q+ (pencil)     e_k (eig W)      e_k/nu_k")
    for k in range(min(N+1,14)):
        print(f"  {k:2d}   {mp.nstr(nu[k],4):>12}          {mp.nstr(E[k],4):>12}      {mp.nstr(E[k]/nu[k],4)}")
    for thr in (1e-8,1e-16,1e-30):
        print(f"   #directions with nu < {thr:.0e}: {sum(1 for x in nu if x<thr)}")
    return nu,E

if __name__=='__main__':
    cases=[tuple(int(x) for x in c.split(',')) for c in sys.argv[1:]] or [(3,24,1024),(3,48,1024),(4,24,1024),(4,48,1024),(6,48,2048),(8,48,2048)]
    for lam,N,bits in cases:
        run(lam,N,bits)
