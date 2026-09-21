"""Diagnostic, not a certificate.  The layer-cake constant of prop:v131-concentration on the even head:
   eta_a^op = int_0^{D_a} ||C_a(E_a(t))|| dt,  E_a(t) = {beta_a < -t},  C_a(E) = P_a F* 1_E F P_a
(source term omitted: this is the norm on the FULL head, an upper bound for the complement).
Compares eta_a^op with D_a = ||beta_a^-||_inf and with the trace bound.  Run from the repo root."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np
from pencil import beta_grid, Fe_grid
N=int(sys.argv[1]) if len(sys.argv)>1 else 48; XI=float(sys.argv[2]) if len(sys.argv)>2 else 4000.0
for lam in (3,4,6,8):
    t0=time.time()
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.005 if N>64 else 0.01)]); hs=np.where(xs<40,0.002,(0.005 if N>64 else 0.01))
    beta,L=beta_grid(lam,xs); a=L/2; D=float(np.max(-beta))
    F=np.array([Fe_grid(n,L,xs) for n in range(N+1)])
    ts=np.linspace(0,D,81)[:-1]; norms=[]; traces=[]; meas=[]
    for t in ts:
        E=beta<-t; C=2*(F[:,E]*hs[E])@F[:,E].T           # two-sided integral over E of Fe_n Fe_m
        w=np.linalg.eigvalsh(C); norms.append(w[-1]); meas.append(2*np.sum(hs[E]))
        traces.append(np.sum(((a+np.sin(2*a*xs[E])/(2*xs[E]))/(2*np.pi))*hs[E])*2)   # source term omitted
    dt=ts[1]-ts[0]; eta=np.sum(norms)*dt; eta_tr=np.sum(np.minimum(1,traces))*dt
    k1=int(np.sum(np.array(norms)>0.99)); 
    print(f"lambda={lam} a={a:.3f}: head N={N} covers xi < 2 pi N/L = {2*math.pi*N/L:.0f}, grid to {XI:.0f}; D_a={D:.3f}  eta^op(head)={eta:.3f}  ({eta/D:.2%} of D_a)   trace-bound eta={eta_tr:.3f}   "
          f"||C||>0.99 for t < {ts[k1-1] if k1 else 0:.2f};  |E(0)|={meas[0]:.0f}  [{time.time()-t0:.0f}s]")
    print("    t/D_a:   "+" ".join(f"{t/D:5.2f}" for t in ts[::10]))
    print("    ||C||:   "+" ".join(f"{n:5.3f}" for n in np.array(norms)[::10]))
    print("    |E(t)|:  "+" ".join(f"{m:5.0f}" for m in np.array(meas)[::10]))
