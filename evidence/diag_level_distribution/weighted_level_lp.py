"""Diagnostic, not a certificate.  NS-28 part 3: the level-set-measure-WEIGHTED hypothesis.
Let m(B) = |{xi in [0,X] : beta_a(xi) in B}| (level pushforward of Lebesgue measure on [0,X]), m~ = m/X, and
phi_- = m~([-D,0)) the negative fraction of [0,X].  Weighted hypothesis:  mu_g(B) >= c' m~(B) for all Borel B in [-D,0]
(a state with |F g|^2 >= b/X pointwise on [0,X] has it with c' = 2b).  For a K-level step minorant the loss is then
    int (beta - m)|Fg|^2  >=  c' * QC_K(m~),   QC_K(m~) = min over K levels l_1=-D<...<l_K<=0 of sum_j int_{l_j}^{l_{j+1}} (t - l_j) dm~(t),
the one-sided K-quantization cost of m~ (computed exactly by dynamic programming on a 200-level grid), and the crude bound
QC_K >= phi_-^2/(2K rho~_max) with rho~_max the sup of the normalized level density.  Then eta >= c' QC_K(m~) - Q, and we
compute Q_min^w(c') (SDP dual = pure primal, N=256 even head) and the resulting K_max.  Run from the repo root."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np
from scipy.optimize import minimize
from flint import ctx
from assembly_general import sequences, block
from pencil import beta_grid, Fe_grid
N=256; XI=800.0; nb=20; NL=200
def quant_cost(levels_mass, edges, K):
    """exact one-sided K-level quantization cost of a discrete measure (mass at bin midpoints) by DP; l_1 = -D fixed."""
    mid=(edges[:-1]+edges[1:])/2; n=len(mid)
    # cost of a gap starting at bin i (level at edges[i]) covering bins i..j-1
    C=np.zeros((n+1,n+1))
    for i in range(n):
        acc=0.0
        for j in range(i,n):
            acc+=(mid[j]-edges[i])*levels_mass[j]; C[i,j+1]=acc
    INF=1e18; dp=np.full((K+1,n+1),INF); dp[0,0]=0.0
    for k in range(1,K+1):
        for j in range(1,n+1):
            dp[k,j]=min(dp[k-1,i]+C[i,j] for i in range(j))
    return dp[K,n] if K<=n else 0.0
for lam in (3,4,6,8):
    t0=time.time(); bits=2048 if lam>=6 else 1024
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.005)]); hs=np.where(xs<40,0.002,0.005)
    beta,L=beta_grid(lam,xs); D=float(-beta.min())
    # level-set measure on a fine level grid and on the 20 bins
    fe=np.linspace(-D,0,NL+1); fm=np.array([np.sum(hs[(beta>=lo)&(beta<hi)]) for lo,hi in zip(fe[:-1],fe[1:])])/XI   # m~ per fine bin
    phi=fm.sum(); rho_max=(fm/(D/NL)).max()
    edges=np.linspace(-D,0,nb+1); sels=[(beta>=lo)&(beta<hi) for lo,hi in zip(edges[:-1],edges[1:])]
    mb=np.array([np.sum(hs[s]) for s in sels])/XI                     # m~(b)
    QC={K:quant_cost(fm,fe,K) for K in (1,2,4,8,16,32)}
    print(f"\n===== lambda={lam}  D={D:.3f}  phi_-={phi:.4f}  rho~_max={rho_max:.4f}  (uniform would be phi/D={phi/D:.4f})  [{time.time()-t0:.0f}s]")
    print("   m~ per bin (deepest->shallowest) x1e3: "+" ".join(f"{v*1e3:.2f}" for v in mb))
    print("   one-sided K-quantization cost QC_K(m~), and crude phi^2/(2K rho_max):  "+"  ".join(f"K={K}: {QC[K]:.4f}/{phi*phi/(2*K*rho_max):.4f}" for K in QC))
    ctx.prec=bits; Lq,b,d,aa=sequences(lam,N+8,bits); rows=list(range(N+1))
    Wb=block(rows,rows,'even',b,d); W=np.array([[float(Wb[i,j].mid()) for j in rows] for i in rows]); W=(W+W.T)/2
    sgn=np.array([(-1)**n for n in range(N+1)],float); Fs=sgn[:,None]*np.array([Fe_grid(n,L,xs) for n in range(N+1)])
    Mb=[2*(Fs[:,s]*hs[s])@Fs[:,s].T for s in sels]                    # MASS matrices per bin (not densities)
    print("   c'      c'phi_-   Q_min^w (dual)   Q_pure   min_b mu(b)/m~(b) of v*   K_max via QC_K (largest K with c'QC_K > Q)")
    for cp in (0.1,0.2,0.5,1.0,2.0,min(4.0,0.999/phi)):
        r=cp*mb
        def negphi(y):
            A=W-sum(yb*M for yb,M in zip(y,Mb)); w,V=np.linalg.eigh(A); v=V[:,0]
            return -(w[0]+y@r), -(r-np.array([v@M@v for M in Mb]))
        best=None
        for y0 in (np.zeros(nb), np.full(nb,0.01), np.full(nb,0.1), np.full(nb,1.0)):
            res=minimize(negphi,y0,jac=True,method='L-BFGS-B',bounds=[(0,None)]*nb,options={'maxiter':3000,'ftol':1e-15,'gtol':1e-12})
            if best is None or res.fun<best.fun: best=res
        Ql=-best.fun; A=W-sum(yb*M for yb,M in zip(best.x,Mb)); w,V=np.linalg.eigh(A); v=V[:,0]
        Qv=v@W@v; ratio=min((v@M@v)/mm for M,mm in zip(Mb,mb) if mm>0)
        if Ql>1e3:
            print(f"   {cp:4.2f}   {cp*phi:6.3f}   infeasible on the head (dual unbounded; c' phi_- exceeds the achievable level mass)"); continue
        Kmax=max([K for K in QC if cp*QC[K]>max(Ql,0)],default=0)
        print(f"   {cp:4.2f}   {cp*phi:6.3f}   {Ql:12.3e}   {Qv:9.3e}   {ratio:8.3f}        {Kmax if Kmax<32 else '>=32'}")
