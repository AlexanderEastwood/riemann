"""Diagnostic, not a certificate.  NS-28: measure the two inputs of prop:v146-level-complexity on the even head.
For a unit packet g, mu_g(B) = int_{beta_a in B} |F g|^2 (Fourier mass by LEVEL of the symbol).  The hypothesis
eq:v146-level-density asks mu_g(B) >= (c/D)|B| for every Borel B in [-D, 0]; we report the best c on 20 level bins
(c = D * min_bins mu_g(bin)/|bin|), the fraction of empty bins, and Q = q_a[g] = int beta_a |F g|^2.
Packets: (P) window cosine packets at the deepest troughs (lem:v146-packet-concentration); (S) their equal-weight sum;
(V) deep pencil directions from the N=48 even pencil.  Also the level-set measure |{beta_a < -t}| on [0, X].
Run from the repo root with .venv/bin/python."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
from pencil import beta_grid, Fe_grid

def level_stats(f2, beta, hs, D, nb=20):
    edges=np.linspace(-D,0,nb+1); dens=[]
    for lo,hi in zip(edges[:-1],edges[1:]):
        sel=(beta>=lo)&(beta<hi); dens.append(2*np.sum(f2[sel]*hs[sel])/(hi-lo))
    dens=np.array(dens); c=D*dens.min(); empty=int(np.sum(dens<1e-12))
    Q=2*np.sum(beta*f2*hs); negmass=2*np.sum(f2[beta<0]*hs[beta<0]); tot=2*np.sum(f2*hs)
    return c, empty, Q, negmass, tot, dens

def packet(omega, a, xs):      # unit cosine packet cos(omega t) on (-a,a); transform (unitary), even
    n=math.sqrt(a*(1+np.sinc(2*a*omega/math.pi)))
    # sin(u a)/u = a*sinc(u a/pi) with numpy's normalized sinc: finite at u = 0
    return a*(np.sinc((omega-xs)*a/math.pi)+np.sinc((omega+xs)*a/math.pi))/n/math.sqrt(2*math.pi)

for lam in (3,4,6,8):
    t0=time.time(); XI=800.0
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.005)]); hs=np.where(xs<40,0.002,0.005)
    beta,L=beta_grid(lam,xs); a=L/2; D=float(-beta.min())
    print(f"\n===== lambda={lam}  a={a:.3f}  D_a(grid {XI:.0f})={D:.3f}  cell 2pi/L={2*math.pi/L:.3f}")
    # (a) level-set measure on [0, X]
    print("  level-set measure |{beta<-t}| on [0,800] / 800, and count of lobes below -t:")
    line1=[];line2=[]
    for frac in (0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9):
        sel=beta<-frac*D; meas=np.sum(hs[sel]); nl=int(np.sum(np.diff(sel.astype(int))==1))
        line1.append(f"{frac:.1f}:{meas/XI:.4f}"); line2.append(f"{frac:.1f}:{nl}")
    print("    measure/X  "+"  ".join(line1)); print("    lobes      "+"  ".join(line2))
    # deepest troughs
    neg=beta<0; st=np.where(np.diff(neg.astype(int))==1)[0]+1; en=np.where(np.diff(neg.astype(int))==-1)[0]+1
    if neg[0]: st=np.r_[0,st]
    if neg[-1]: en=np.r_[en,len(xs)]
    lobes=sorted([(float(-beta[s:e].min()),float(xs[s+np.argmin(beta[s:e])])) for s,e in zip(st,en)],reverse=True)
    print(f"  {len(lobes)} lobes; five deepest (depth, xi): "+", ".join(f"({d:.2f},{x:.1f})" for d,x in lobes[:5]))
    print("  packet                 c (20 bins)  empty bins  Q=q[g]   mass on beta<0   ||g||^2 on grid")
    fsum=np.zeros_like(xs)
    for d,x in lobes[:5]:
        f=packet(x,a,xs); f2=f*f; fsum+=f
        c,empty,Q,nm,tot,_=level_stats(f2,beta,hs,D)
        print(f"  (P) trough {x:7.1f}      {c:9.4f}    {empty:3d}/20   {Q:+8.4f}     {nm:.3f}           {tot:.4f}")
    fs=fsum/np.sqrt(2*np.sum(fsum*fsum*hs)); c,empty,Q,nm,tot,dens=level_stats(fs*fs,beta,hs,D)
    print(f"  (S) sum of 5 packets    {c:9.4f}    {empty:3d}/20   {Q:+8.4f}     {nm:.3f}           {tot:.4f}")
    fall=np.zeros_like(xs)
    for d,x in lobes[:min(40,len(lobes))]: fall+=packet(x,a,xs)
    fa=fall/np.sqrt(2*np.sum(fall*fall*hs)); c,empty,Q,nm,tot,dens=level_stats(fa*fa,beta,hs,D)
    print(f"  (S) sum of 40 packets   {c:9.4f}    {empty:3d}/20   {Q:+8.4f}     {nm:.3f}           {tot:.4f}")
    print("      level density (x D) per bin, deepest to shallowest: "+" ".join(f"{v*D:.2f}" for v in dens))
    # (V) deep pencil directions, N=48
    N=48; bits=2048 if lam>=6 else 1024; dps=120
    xs2=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,4000,0.01)]); hs2=np.where(xs2<40,0.002,0.01)
    b2,_=beta_grid(lam,xs2); neg2=np.maximum(-b2,0.0)
    F2=np.array([Fe_grid(n,L,xs2) for n in range(N+1)]); sgn=np.array([(-1)**n for n in range(N+1)],float)
    Wm=2*(F2*(neg2*hs2))@F2.T; Wm=sgn[:,None]*Wm*sgn[None,:]
    ctx.prec=bits; Lq,bb,dd,aa=sequences(lam,N+8,bits); rows=list(range(N+1)); Wb=block(rows,rows,'even',bb,dd)
    mp.mp.dps=dps; W=tomp(Wb,dps); Wp=W+mp.matrix(Wm.tolist())
    C=mp.cholesky(Wp); Ci=mp.inverse(C); M=Ci*W*Ci.T; M=(M+M.T)/2; nu,U=mp.eigsy(M); V=Ci.T*U
    order=sorted(range(N+1),key=lambda k:nu[k])
    F=np.array([Fe_grid(n,L,xs) for n in range(N+1)])
    for k in order[:4]+order[8:10]:
        v=np.array([float(V[j,k]) for j in range(N+1)]); v/=np.linalg.norm(v)
        g=(sgn*v)@F; f2=g*g
        c,empty,Q,nm,tot,_=level_stats(f2,beta,hs,D)
        print(f"  (V) pencil k={order.index(k):2d} nu={mp.nstr(nu[k],3):>9}  c={c:8.4f}  empty {empty:2d}/20   Q={Q:+.3e}   mass beta<0 {nm:.3f}   ||g||^2 {tot:.4f}")
    print(f"  [{time.time()-t0:.0f}s]")
