"""Fine-grid scan of the window symbol beta_lambda(t) (the 'd' of sequences() at real t),
its negative set, and the Kac-Murdock-Szego count  (L/2pi)*|{t: beta<0}|  (two-sided)."""
import math, time, sys
from flint import arb, acb, ctx
ctx.prec = 192
def pairs(lam):
    out=[]
    for m in range(2,lam*lam):
        for p in range(2,m+1):
            if m%p==0:
                k=m
                while k%p==0:k//=p
                if k==1:out.append((m,p))
                break
    return out
def make_beta(lam, K=96):
    L=2*arb(lam).log(); pi=arb.pi(); h=(L/4).sinh()**2
    pw=[(arb(m).log(),arb(p).log()/arb(m).sqrt()) for m,p in pairs(lam)]
    ks=[(2*k+arb(1)/2,arb(1)/arb(lam)**(4*k+1)) for k in range(K)]
    def beta(t):
        t=arb(t); n=t*L/(2*pi)                       # real 'n' so the same algebra applies off-grid
        z=acb(arb(1)/4,-t/2); ps=z.digamma(); tri=z.polygamma(1)
        a=ps.real-pi.log()+tri.real/(2*L)
        for c,e in ks:
            den=c*c+t*t; a-=2/L*e*(c*c-t*t)/(den*den)
        den=L*L+16*pi*pi*n*n
        d=a+32*L*h*(L*L-16*pi*pi*n*n)/(den*den)-2*sum(((t*y).cos()*(1-y/L)*w for y,w in pw),arb(0))
        return float(d.mid())
    return beta, float(L.mid())
zeros=[14.1347,21.0220,25.0109,30.4249,32.9351,37.5862,40.9187,43.3271,48.0052,49.7738,52.9703,56.4462,59.3470,60.8318,65.1125,67.0798,69.5464,72.0672,75.7047,77.1448]
print("%-4s %-7s %-9s %-9s %-10s %-9s %-9s %-s"%("lam","L","tmax","min beta","argmin","|neg|2s","KMS cnt","first negative lobes (t-range) vs nearest zero"))
for lam in (3,4,6,8):
    t0=time.time(); beta,L=make_beta(lam); dt=0.01; tmax=120.0
    ts=[i*dt for i in range(int(tmax/dt)+1)]; vals=[beta(t) for t in ts]
    mn=min(vals); am=ts[vals.index(mn)]
    neg=[t for t,v in zip(ts,vals) if v<0]; meas=2*len(neg)*dt        # two-sided measure
    # lobes
    lobes=[]; cur=None
    for t,v in zip(ts,vals):
        if v<0 and cur is None: cur=t
        if v>=0 and cur is not None: lobes.append((cur,t)); cur=None
    if cur is not None: lobes.append((cur,tmax))
    desc="; ".join("[%.2f,%.2f]~z%.2f"%(a,b,min(zeros,key=lambda z:abs(z-(a+b)/2))) for a,b in lobes[:4]) or "none"
    print("%-4d %-7.4f %-9.0f %-9.4f %-10.2f %-9.3f %-9.3f %s   (%.0fs, %d lobes)"%(lam,L,tmax,mn,am,meas,L/(2*math.pi)*meas,desc,time.time()-t0,len(lobes)),flush=True)
