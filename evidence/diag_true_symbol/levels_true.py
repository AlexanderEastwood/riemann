"""Level split of the lambda=3 ground-state Weil energy with the VALIDATED symbol beta_a
(eq:v130-beta), the accurate N=120 ground vector, and the (-1)^n basis convention.
q = int_R beta_a |F f|^2 dxi  (unitary F of the zero extension)."""
import sys, json, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import numpy as np, mpmath as mp
from beta_true import make_beta_true
g=json.load(open('ground_l3_N120.json')); lam=g['lambda']; L=2*math.log(g['lambda']); eps=float(mp.mpf(g['eps']))
v=np.array([float(mp.mpf(s)) for s in g['v']]); v=np.where(np.abs(v)>1e-16,v,0.0)
nmax=int(np.max(np.nonzero(np.abs(v)>1e-13)))+1; print(f"lambda={lam} L={L:.6f} eps_N={eps:.4e}; modes kept n<{nmax} (|v_n|>1e-13)")
def Ff(xi):   # unitary transform of the zero-extended even function, centered window, (-1)^n convention
    xi=np.asarray(xi,dtype=float); out=v[0]/np.sqrt(L)*2*np.sin(xi*L/2)/xi
    for n in range(1,nmax):
        w=2*np.pi*n/L
        out+=((-1)**n)*v[n]*np.sqrt(2/L)*(np.sin((w-xi)*L/2)/(w-xi)+np.sin((w+xi)*L/2)/(w+xi))
    return out/np.sqrt(2*np.pi)
beta,_=make_beta_true(lam); mp.mp.dps=15
XI=3000.0; h=0.005; xs=np.arange(h/2,XI,h); t0=time.time()
bv=np.array([float(beta(x)) for x in xs]); print(f"  beta on {len(xs)} points: {time.time()-t0:.0f}s")
f2=Ff(xs)**2
plan=2*np.sum(f2)*h
neg=bv<0
q_neg=2*np.sum(bv[neg]*f2[neg])*h; q_pos=2*np.sum(bv[~neg]*f2[~neg])*h
massneg=2*np.sum(f2[neg])*h
# tail beyond XI: |Ff|^2 ~ A * 4 sin^2(xi L/2)/xi^2/(2pi) -> fit A from the last 2000 points, then averaged tail with beta ~ log(xi/2)-log(pi)
sl=xs>XI-20; A=np.mean(f2[sl]*xs[sl]**2*2*np.pi/(4*np.sin(xs[sl]*L/2)**2+1e-30))
tail_mass=2*A*4*0.5/(2*np.pi)/XI
tail_q=2*A*4*0.5/(2*np.pi)*float(mp.quad(lambda x:(mp.log(x/2)-mp.log(mp.pi))/x**2,[XI,mp.inf]))
print(f"  Plancherel: {plan:.6f} + tail {tail_mass:.2e} = {plan+tail_mass:.6f}   (should be 1)")
print(f"  fraction of |Ff|^2 mass on {{beta_a<0}}: {massneg:.4f}")
print(f"  q_neg = int_{{beta<0}} beta|Ff|^2 = {q_neg:+.6f}")
print(f"  q_pos = int_{{beta>0}} beta|Ff|^2 = {q_pos:+.6f}  (+ tail {tail_q:+.2e})")
print(f"  q_neg + q_pos + tail = {q_neg+q_pos+tail_q:+.3e}    vs true eps_N = {eps:.2e}   (quadrature-limited; O(1) parts cancel)")
# where the negative energy sits
edges=[0,5,10,20,40,80,160,400,3000]
print("  negative-level energy by frequency band:")
for a_,b_ in zip(edges,edges[1:]):
    m=neg&(xs>=a_)&(xs<b_); print(f"    xi in [{a_:4d},{b_:4d}):  {2*np.sum(bv[m]*f2[m])*h:+.5f}")
print("  positive-level energy by band:")
for a_,b_ in zip(edges,edges[1:]):
    m=(~neg)&(xs>=a_)&(xs<b_); print(f"    xi in [{a_:4d},{b_:4d}):  {2*np.sum(bv[m]*f2[m])*h:+.5f}")
