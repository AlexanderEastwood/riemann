"""Continuous level split of the ground-state Weil energy:
   q(f) = (1/2pi) int beta(t) |f^(t)|^2 dt   split over {beta<0} and {beta>0},
   plus Plancherel check and Slepian count of the negative set.  Diagnostic."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation')  # run from repo root
from zeros import ground, xhat          # reuses inverse-iteration ground + transform
from symbol_scan import make_beta
import mpmath as mp
for lam in (3,4):
    t0=time.time(); L,v,ray=ground(lam,256); beta,_=make_beta(lam)
    mp.mp.dps=30
    dt=0.005; tmax=400.0; ts=[i*dt+dt/2 for i in range(int(tmax/dt))]
    neg=pos=plan=0; negE=posE=0
    for t in ts:
        f2=abs(xhat(v,L,t,dps=30))**2; b=beta(t)
        plan+=f2*dt
        if b<0: neg+=b*f2*dt; negE+=f2*dt
        else:   pos+=b*f2*dt; posE+=f2*dt
    two=2/(2*math.pi)   # even function: integral over R = 2 * integral over t>0, divided by 2pi
    print(f"\nlambda={lam}  L={L:.4f}   Rayleigh (true q) = {mp.nstr(ray,4)}   [{time.time()-t0:.0f}s]")
    print(f"  Plancherel  (1/2pi) int |f^|^2 dt  = {float(plan*two):.6f}   (should be 1.000)")
    print(f"  fraction of |f^|^2 mass on the NEGATIVE set of beta:  {float(negE/plan):.4f}")
    print(f"  q_neg = (1/2pi) int_{{beta<0}} beta |f^|^2 = {float(neg*two):+.6f}")
    print(f"  q_pos = (1/2pi) int_{{beta>0}} beta |f^|^2 = {float(pos*two):+.6f}")
    print(f"  q_neg + q_pos = {float((neg+pos)*two):+.2e}   (quadrature residual vs true q ~ 1e-38..1e-75)")
    print(f"  tail check: mass beyond t=120: {float(sum(abs(xhat(v,L,t,dps=30))**2*dt for t in ts if t>120)*two):.2e}")
