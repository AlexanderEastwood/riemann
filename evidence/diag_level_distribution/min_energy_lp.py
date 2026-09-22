"""Diagnostic, not a certificate.  NS-28 part 2: the minimum packet energy compatible with a level-distribution
constant c.  prop:v146-level-complexity is linear in |F g|^2, so it holds verbatim for a density matrix X.  With
M_b the level-density matrices (20 bins on [-D,0]) and r_b = c/D the required density,
    Q_min(c) = min { tr(W X) : X >= 0, tr X = 1, tr(M_b X) >= r_b for all b }.
LOWER bound (SDP dual, valid for ALL states in the head): for any y >= 0,
    Q_min(c) >= phi(y) := lambda_min(W - sum_b y_b M_b) + sum_b y_b r_b,   maximised over y (L-BFGS-B).
UPPER bounds: (i) LP over mixtures of a dictionary of pure states (eigenvectors of W, exact head coefficients of
cosine packets at the 40 deepest troughs, and the dual eigenvectors); (ii) the pure state v(y*) from the dual.
W: N=256 even head, Arb midpoints in float64 (energies below 1e-16 read as 0).  eq:v146-level-lower is
eta >= cD/(2K) - Q, so it has content only when Q_min(c) < cD/(2K) for some K >= 1.  Run from the repo root."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np
from scipy.optimize import linprog, minimize
from flint import ctx
from assembly_general import sequences, block
from pencil import beta_grid, Fe_grid
N=256; XI=800.0; nb=20
def packet_coeffs(omega,L,N):
    """exact coefficients of cos(omega t) on (-L/2,L/2) in the block() basis (centered cosines with (-1)^n)"""
    a=L/2; w=2*math.pi*np.arange(N+1)/L
    c=np.where(np.arange(N+1)==0, (1/math.sqrt(L))*2*np.sin(omega*a)/omega,
               math.sqrt(2/L)*(np.sin((omega-w)*a)/np.where(w==omega,1,omega-w)+np.sin((omega+w)*a)/(omega+w)))
    c=c*np.array([(-1)**n for n in range(N+1)]); return c/np.linalg.norm(c)
for lam in (3,4,6,8):
    t0=time.time(); bits=2048 if lam>=6 else 1024
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.005)]); hs=np.where(xs<40,0.002,0.005)
    beta,L=beta_grid(lam,xs); D=float(-beta.min())
    ctx.prec=bits; Lq,b,d,aa=sequences(lam,N+8,bits); rows=list(range(N+1))
    Wb=block(rows,rows,'even',b,d); W=np.array([[float(Wb[i,j].mid()) for j in rows] for i in rows]); W=(W+W.T)/2
    sgn=np.array([(-1)**n for n in range(N+1)],float); Fs=sgn[:,None]*np.array([Fe_grid(n,L,xs) for n in range(N+1)])
    edges=np.linspace(-D,0,nb+1); sels=[(beta>=lo)&(beta<hi) for lo,hi in zip(edges[:-1],edges[1:])]
    Mb=[2*(Fs[:,s]*hs[s])@Fs[:,s].T/(D/nb) for s in sels]
    e,U=np.linalg.eigh(W); e=np.maximum(e,0.0)
    neg=beta<0; st=np.where(np.diff(neg.astype(int))==1)[0]+1; en=np.where(np.diff(neg.astype(int))==-1)[0]+1
    if neg[0]: st=np.r_[0,st]
    if neg[-1]: en=np.r_[en,len(xs)]
    lobes=sorted([(float(-beta[s:e_].min()),float(xs[s+np.argmin(beta[s:e_])])) for s,e_ in zip(st,en)],reverse=True)[:40]
    P=np.array([packet_coeffs(x,L,N) for _,x in lobes]).T
    # sanity: the head coefficients of the deepest packet reproduce its transform on the grid
    g_grid=P[:,0]@Fs; print(f"\n===== lambda={lam} N={N} (xi < {2*math.pi*N/L:.0f})  D={D:.3f}  deepest packet: grid mass {2*np.sum(g_grid**2*hs):.4f}, deepest-bin mass {2*np.sum(g_grid[sels[0]]**2*hs[sels[0]]):.4f}  [{time.time()-t0:.0f}s]")
    print("   c      Q_lower(dual)   Q_pure(v*)   c_v*   Q_upper(LP)    cD/2      K_max(lower)  K_max(pure)")
    duals=[]
    for c in (0.01,0.03,0.05,0.1,0.2,0.3):
        r=np.full(nb,c/D)
        def negphi(y):
            A=W-sum(yb*M for yb,M in zip(y,Mb)); w,V=np.linalg.eigh(A); v=V[:,0]
            return -(w[0]+y@r), -(r-np.array([v@M@v for M in Mb]))
        best=None
        for y0 in (np.zeros(nb), np.full(nb,0.01), np.full(nb,0.1)):
            res=minimize(negphi,y0,jac=True,method='L-BFGS-B',bounds=[(0,None)]*nb,options={'maxiter':3000,'ftol':1e-15,'gtol':1e-12})
            if best is None or res.fun<best.fun: best=res
        Ql=-best.fun; y=best.x
        A=W-sum(yb*M for yb,M in zip(y,Mb)); w,V=np.linalg.eigh(A); v=V[:,0]; duals.append(v)
        Qv=v@W@v; cv=D*min(v@M@v for M in Mb)
        dic=np.column_stack([U,P,np.array(duals).T]); nd=dic.shape[1]
        Ed=np.einsum('ij,ij->j',dic,W@dic); Md=np.array([np.einsum('ij,ij->j',dic,M@dic) for M in Mb])
        lp=linprog(Ed, A_ub=-Md, b_ub=-r, A_eq=np.ones((1,nd)), b_eq=[1.0], bounds=[(0,None)]*nd, method='highs')
        Qu=lp.fun if lp.status==0 else float('nan')
        kl=math.floor(c*D/(2*Ql)) if Ql>1e-15 else 'inf'; kp=math.floor(c*D/(2*Qv)) if (Qv>1e-15 and cv>=c*0.999) else ('n/a' if cv<c*0.999 else 'inf')
        print(f"   {c:.2f}   {Ql:12.3e}   {Qv:10.3e}   {cv:5.3f}   {Qu:11.3e}   {c*D/2:.3e}   {str(kl):>10}   {str(kp):>10}")
