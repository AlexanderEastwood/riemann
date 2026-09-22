"""Diagnostic, not a certificate.  Odd sector: validate q = int beta_a |F f|^2 against block(...,'odd',...)
and run the level pencil W v = nu (W + W^-) v there (prop:v135-both-parities: same symbol, both parities).
Odd modes e_n = sqrt(2/L) sin(2 pi n x/L) on (-L/2, L/2), n >= 1; |F e_n|^2 is real.  Run from the repo root."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
from pencil import beta_grid

def Fo_grid(n, L, xs):     # |F e_n| for the odd mode (imaginary transform; magnitude suffices for products of two odd modes up to a common sign)
    w=2*math.pi*n/L
    return math.sqrt(2/L)*(np.sin((w-xs)*L/2)/(w-xs)-np.sin((w+xs)*L/2)/(w+xs))/math.sqrt(2*math.pi)

def run(lam,N,bits,dps=120,XI=4000.0):
    t=time.time()
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.01)]); hs=np.where(xs<40,0.002,0.01)
    beta,L=beta_grid(lam,xs); neg=np.maximum(-beta,0.0)
    F=np.array([Fo_grid(n,L,xs) for n in range(1,N+1)])
    Wq=2*(F*(beta*hs))@F.T; Wm=2*(F*(neg*hs))@F.T
    I=float(mp.quad(lambda x:(mp.log(x/2)-mp.log(mp.pi))*2/(x**2)/(2*mp.pi),[XI,mp.inf]))
    cn=np.full(N,math.sqrt(2/L))
    ctx.prec=bits; Lq,b,d,aa=sequences(lam,N+8,bits); rows=list(range(1,N+1))
    try:
        Wb=block(rows,rows,'odd',b,d)
    except Exception as e:
        rows=list(range(0,N)); Wb=block(rows,rows,'odd',b,d); print("  (odd block indexed from 0)")
    Wf=np.array([[float(Wb[i,j].mid()) for j in range(N)] for i in range(N)])
    # sign convention: test both (-1)^{n+m} and none, with the asymptotic tail (odd tail: Fe_n ~ (-1)^n c_n 2 cos(xi L/2)/xi ... cos^2 -> 1/2, same constant)
    # odd modes: for xi >> w, F e_n ~ (-1)^n c_n 2 w sin(xi L/2)/xi^2, so |F e_n|^2 ~ 1/xi^4 and the tail beyond XI is
    # O(log XI / XI^3): negligible, no analytic tail is added.  Basis sign: block()'s odd basis carries (-1)^n like the even one.
    best=None
    for name,sg in (('none',np.ones(N)),('(-1)^n',np.array([(-1)**n for n in range(1,N+1)],float))):
        Wt=sg[:,None]*Wq*sg[None,:]
        big=np.abs(Wf)>1e-2; err=np.max(np.abs(Wt-Wf)[big]/np.abs(Wf)[big])
        if best is None or err<best[0]: best=(err,name,sg)
    err,name,sg=best
    print(f"lambda={lam} odd N={N}: basis sign '{name}': max rel. err of full-symbol quadrature vs block() on |W|>1e-2 = {err:.1e}")
    Wm=sg[:,None]*Wm*sg[None,:]
    mp.mp.dps=dps; W=tomp(Wb,dps); Wp=W+mp.matrix(Wm.tolist())
    C=mp.cholesky(Wp); Ci=mp.inverse(C); M=Ci*W*Ci.T; M=(M+M.T)/2
    nu=sorted(mp.eigsy(M)[0]); E=sorted(mp.eigsy(W)[0])
    print("   k   nu_k (odd pencil)   e_k (eig W odd)    e_k/nu_k")
    for k in range(10): print(f"  {k:2d}   {mp.nstr(nu[k],4):>12}      {mp.nstr(E[k],4):>12}     {mp.nstr(E[k]/nu[k],4)}")
    for thr in (1e-8,1e-16,1e-30): print(f"   #directions with nu < {thr:.0e}: {sum(1 for x in nu if x<thr)}")
    print(f"   [{time.time()-t:.0f}s]")
if __name__=='__main__':
    for lam,N,bits in ((3,48,1024),(4,48,1024)): run(lam,N,bits)
