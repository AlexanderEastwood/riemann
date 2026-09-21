import sys, json, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
from beta_true import make_beta_true
lam,N,bits,dps=4,120,1024,220
ctx.prec=bits; Lq,b,d,a=sequences(lam,N+8,bits); rows=list(range(N+1)); mp.mp.dps=dps
t=time.time(); E,Q=mp.eigsy(tomp(block(rows,rows,'even',b,d),dps)); i=min(range(len(E)),key=lambda k:E[k]); eps=float(E[i])
v=np.array([float(Q[k,i]) for k in range(N+1)]); L=2*math.log(lam)
print(f"lambda={lam} N={N}: eps_N={eps:.4e} second even={float(sorted(E)[1]):.3e}  [{time.time()-t:.0f}s]  |v0..v5|={np.round(np.abs(v[:6]),4).tolist()}")
nmax=int(np.max(np.nonzero(np.abs(v)>1e-13)))+1
def Ff(xi):
    out=v[0]/np.sqrt(L)*2*np.sin(xi*L/2)/xi
    for n in range(1,nmax):
        w=2*np.pi*n/L; out+=((-1)**n)*v[n]*np.sqrt(2/L)*(np.sin((w-xi)*L/2)/(w-xi)+np.sin((w+xi)*L/2)/(w+xi))
    return out/np.sqrt(2*np.pi)
beta,_=make_beta_true(lam); mp.mp.dps=15; XI=3000.0; h=0.005; xs=np.arange(h/2,XI,h)
bv=np.array([float(beta(x)) for x in xs]); f2=Ff(xs)**2; neg=bv<0
plan=2*np.sum(f2)*h; qn=2*np.sum(bv[neg]*f2[neg])*h; qp=2*np.sum(bv[~neg]*f2[~neg])*h; mn=2*np.sum(f2[neg])*h
print(f"  Plancherel={plan:.6f}  mass on {{beta<0}}={mn:.4f}  q_neg={qn:+.6f}  q_pos={qp:+.6f}  sum={qn+qp:+.2e} (true {eps:.1e})")
for a_,b_ in ((0,5),(5,10),(10,20),(20,3000)):
    m=(xs>=a_)&(xs<b_); print(f"    xi in [{a_:4d},{b_:4d}):  neg {2*np.sum(bv[m&neg]*f2[m&neg])*h:+.5f}   pos {2*np.sum(bv[m&~neg]*f2[m&~neg])*h:+.5f}")
