import sys, math
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import mpmath as mp
from beta_true import make_beta_true
mp.mp.dps=15
print("TRUE symbol beta_a (eq:v130-beta), scanned on [0,400], step 0.005")
print("%-4s %-7s %-9s %-7s %-10s %-9s %-s"%("lam","L","min beta","at xi","|neg| 2s","(L/2pi)|neg|","negative intervals (first 6)"))
for lam in (3,4,6,8):
    beta,L=make_beta_true(lam); L=float(L); h=0.005; xs=[i*h+h/2 for i in range(int(400/h))]
    v=[float(beta(x)) for x in xs]; mn=min(v); am=xs[v.index(mn)]
    lobes=[];cur=None
    for x,y in zip(xs,v):
        if y<0 and cur is None: cur=x
        if y>=0 and cur is not None: lobes.append((cur,x)); cur=None
    if cur is not None: lobes.append((cur,400.0))
    meas=2*sum(b-a for a,b in lobes)
    desc="; ".join("[%.2f,%.2f]"%ab for ab in lobes[:6])+(" …(%d)"%len(lobes) if len(lobes)>6 else "")
    print("%-4d %-7.4f %-9.4f %-7.2f %-10.3f %-9.3f %s"%(lam,L,mn,am,meas,L/(2*math.pi)*meas,desc),flush=True)
