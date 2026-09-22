"""Diagnostic, not a certificate.  Step minorants for the weighted concentration criterion of
prop:v131-concentration (eq:v131-step-minorant, eq:v131-weighted-concentration) on the even head:

   eta(m) := max(0, -lambda_min( P_N Op(m) P_N )),   Op(m) = F* m F,   m <= beta_a pointwise, m a step function,

so that -D_a P + sum_j w_j C(G_j) = P Op(m) P >= -eta P is the criterion with m = -D_a + sum_j w_j 1_{G_j}.
Families:  (A) J deepest troughs (nested lobe complements),  (B) one level set {beta >= -t}, best t,
           (C) layer-cake reference (80 levels) and its J->infinity operator ||Op(beta^-)||,
           (D1) J-level quantization of beta_a (level sets = unions of crest cores; greedy + coordinate refinement),
           (D2) lattice-periodic comb: nested neighbourhoods of the lattice points 2 pi n/L, uniform across cells,
           (D3) binary-coded quantization: J sets with weights 2^j h encode 2^J uniform levels (set count vs level count).
Float quadrature on xi in [0,800] (step 0.002 below 40, 0.005 above), N=256 even modes, as in layercake.py.
The region |xi|>800 enters only through the tail matrix T = I - C([0,800]) (Plancherel), charged at the worst
tail value -D_tail found on [800, 40000]; ||T|| is not small (head directions near the cut), so every eta is
reported with the tail charge (valid minorant) and without it (grid-only, as layercake.py; not a valid minorant).
Run from the repo root:  /Users/alex/riemann/.venv/bin/python evidence/diag_comb_minorant/comb_minorant.py [lambdas]"""
import sys, math, time, json
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np
from pencil import beta_grid, Fe_grid

N=256; XI=800.0; XT=40000.0; NLEV=80; KNEG=2*NLEV; KPOS=80; NRING=40
JLIST=[1,2,3,4,6,8,12,16,24,32,48,64]; JREF=[1,2,3,4,6,8,12,16]; JMAX=64
OUT='evidence/diag_comb_minorant/'

def lmin(M): return float(np.linalg.eigvalsh(M)[0])
def eta_of(M): return max(0.0,-lmin(M))
def eta2(M,tail): return eta_of(M+tail), eta_of(M)   # (with tail charge, grid-only)

def run(lam):
    t0=time.time(); R={'lambda':lam}
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.005)]); hs=np.where(xs<40,0.002,0.005)
    beta,L=beta_grid(lam,xs); a=L/2
    xt=np.arange(XI+0.005,XT,0.01); bt,_=beta_grid(lam,xt)
    Dg=float(np.max(-beta)); Dt=float(max(0.0,np.max(-bt))); Dtrue=max(Dg,Dt)
    F=np.array([Fe_grid(n,L,xs) for n in range(N+1)])
    def cmat(idx):
        G=F[:,idx]; return 2*(G*hs[idx])@G.T
    Cg=cmat(np.ones(len(xs),bool)); T=np.eye(N+1)-Cg
    Tn=float(np.linalg.eigvalsh(T)[-1]); tail=-Dtrue*T          # tail charge, worst valid value
    W=2*(F*(beta*hs))@F.T
    lW=lmin(W); lWt=lmin(W+tail)
    print(f"lambda={lam} a={a:.3f} L={L:.3f}: head N={N} reaches xi < 2 pi N/L = {2*math.pi*N/L:.0f}; grid to {XI:.0f}; "
          f"D_a(grid)={Dg:.3f} at xi={xs[np.argmin(beta)]:.2f}; D on [800,{XT:.0f}]={Dt:.3f} at xi={xt[np.argmin(bt)]:.1f} (neg. set ends {xt[bt<0].max() if np.any(bt<0) else xs[beta<0].max():.0f}+)")
    print(f"   tail matrix ||T|| = ||I - C([0,800])|| = {Tn:.2e}, min diag C = {np.min(np.diag(Cg)):.5f}; tail charge <= D_tail ||T|| = {Dtrue*Tn:.1e}")
    print(f"   head floor: lambda_min(Op(beta)) = {lW:.3e} (grid), {lWt:.3e} (grid + tail charge)  -- eta below |this| is not resolved")
    R.update(a=a,L=L,Dg=Dg,Dt=Dt,Tnorm=Tn,lW=lW,lWt=lWt,head_reach=2*math.pi*N/L)

    # ---- level bins (K = KNEG negative + KPOS positive), suffix sums S[b] = C({beta >= edge_b}) ----
    bmax=float(beta.max())
    edges=np.concatenate([np.linspace(-Dg,0,KNEG+1), np.linspace(0,bmax,KPOS+1)[1:]]); K=KNEG+KPOS
    binid=np.clip(np.searchsorted(edges,beta,side='right')-1,0,K-1); lo=edges[:-1]
    B=np.array([cmat(binid==b) for b in range(K)]); S=np.cumsum(B[::-1],axis=0)[::-1]
    print(f"   level bins: {KNEG} on [-D_a,0), {KPOS} on [0,{bmax:.2f}]; sum of bins vs C(grid): {np.abs(B.sum(0)-Cg).max():.1e}  [{time.time()-t0:.0f}s]")

    # ---- (C) layer-cake reference: eta^op = int_0^D ||C(E(t))|| dt, E(t) = {beta < -t}, 80 levels (as layercake.py) ----
    norms=[]; norms0=[]
    for k in range(NLEV):
        t=k*Dg/NLEV; C=Cg-S[KNEG-2*k] if k>0 else Cg-S[KNEG]
        # E(t) = bins b < KNEG-2k = C(grid) - S[KNEG-2k]; tail part bounded by T when the tail dips below -t
        norms0.append(float(np.linalg.eigvalsh(C)[-1]))
        if Dt>t: C=C+T
        norms.append(float(np.linalg.eigvalsh(C)[-1]))
    etaC=float(np.sum(norms)*Dg/NLEV)+max(0.0,Dt-Dg)*Tn
    neg=beta<0; Wm=cmat(neg) if False else 2*(F[:,neg]*((-beta[neg])*hs[neg]))@F[:,neg].T
    etaCx,etaCx0=eta2(-Wm,tail); etaC0=float(np.sum(norms0)*Dg/NLEV)
    print(f"(C) layer-cake eta^op = {etaC:.3f} ({etaC/Dg:.2%} of D_a) [grid-only {etaC0:.3f}];  J->inf level-set limit ||Op(beta^-)|| = {etaCx:.3f} ({etaCx/Dg:.2%}) [grid-only {etaCx0:.3f}];  ||C(E(0))||={norms0[0]:.3f}")
    R.update(etaC=etaC,etaC0=etaC0,etaCx=etaCx,etaCx0=etaCx0,normsC=norms0)

    # ---- helper: minorant from a sorted list of level bin-indices (floor -D_a implicit) ----
    def op_levels(bs):
        M=-Dg*Cg; prev=-Dg
        for b in sorted(bs):
            M=M+(lo[b]-prev)*S[b]; prev=lo[b]
        return M
    def m_levels(bs):
        m=np.full(len(xs),-Dg)
        for b in sorted(bs): m[binid>=b]=lo[b]
        return m

    # ---- (B) one level set G(t) = {beta >= -t}, weight D_a - t ----
    rowsB=[]
    for k in range(NLEV+1):
        b=KNEG-2*k if k<NLEV else 0   # level -t = edge KNEG-2k ; k=NLEV -> t=D_a (no set)
        e,e0=eta2(op_levels([b]) if b>0 else -Dg*Cg,tail); rowsB.append((k*Dg/NLEV,e,e0))
    kB=int(np.argmin([e for e in [r[1] for r in rowsB]])); tB,eB,eB0=rowsB[kB]
    viol=float(np.max(m_levels([KNEG-2*kB])-beta)) if kB<NLEV else float(np.max(-Dg-beta))
    print(f"(B) one level set: best t = {tB:.3f} = {tB/Dg:.2f} D_a, eta = {eB:.3f} ({eB/Dg:.2%} of D_a) [grid-only {eB0:.3f}]; max pointwise violation {viol:.1e}")
    print("    t/D_a: "+" ".join(f"{t/Dg:5.2f}" for t,_,_ in rowsB[::8]))
    print("    eta:   "+" ".join(f"{e:5.3f}" for _,e,_ in rowsB[::8]))
    R.update(B=rowsB,tB=tB,etaB=eB)

    # ---- (A) J deepest troughs: nested complements of the J deepest negative lobes ----
    d=np.diff(np.concatenate([[0],neg.astype(int),[0]])); st=np.where(d==1)[0]; en=np.where(d==-1)[0]
    lobes=[(float(-beta[s:e].min()),float(xs[s+np.argmin(beta[s:e])]),s,e) for s,e in zip(st,en)]
    lobes.sort(key=lambda z:-z[0]); nl=len(lobes); depths=[z[0] for z in lobes]+[0.0]
    A=np.zeros((N+1,N+1)); P=np.zeros((N+1,N+1)); rowsA=[]
    print(f"(A) {nl} negative lobes on the grid; deepest 8 (depth @ xi, in cells u=xi L/2pi): "
          +", ".join(f"{z[0]:.2f}@{z[1]:.1f}(u={z[1]*L/(2*math.pi):.1f})" for z in lobes[:8]))
    for j in range(1,nl+1):
        dj,_,s,e=lobes[j-1]; Bl=cmat(np.arange(s,e)); A+=dj*Bl; P+=Bl
        if j in JLIST or j==nl:
            dn=depths[j]; M=-A-dn*(Cg-P); e_,e0=eta2(M,tail)
            m=np.full(len(xs),-dn)
            for z in lobes[:j]: m[z[2]:z[3]]=-z[0]
            rowsA.append((j,e_,dn,float(np.max(m-beta)),e0))
    print("    J:        "+" ".join(f"{j:6d}" for j,*_ in rowsA))
    print("    eta(J):   "+" ".join(f"{e:6.3f}" for _,e,*_ in rowsA))
    print("    eta/D_a:  "+" ".join(f"{e/Dg:6.3f}" for _,e,*_ in rowsA))
    print("    grid-only:"+" ".join(f"{e0:6.3f}" for *_,e0 in rowsA))
    print("    floor d_{J+1}: "+" ".join(f"{dn:6.3f}" for _,_,dn,_,_ in rowsA)+f"   max violation {max(v for _,_,_,v,_ in rowsA):.1e}")
    R.update(A=rowsA,nlobes=nl,lobes=[(z[0],z[1]) for z in lobes[:16]])

    # ---- (D1) J-level quantization of beta_a: greedy insertion on bin edges, coordinate refinement at J in JREF ----
    levels=[]; rowsD=[]; cands=list(range(1,K))
    for J in range(1,JMAX+1):
        best=None
        for b in cands:
            if b in levels: continue
            e=eta_of(op_levels(levels+[b])+tail)
            if best is None or e<best[0]: best=(e,b)
        levels.append(best[1]); e=best[0]
        if J in JREF:
            for sweep in range(3):
                improved=False
                for i in range(J):
                    cur=eta_of(op_levels(levels)+tail); bi=levels[i]
                    for b in cands:
                        if b in levels: continue
                        trial=levels[:i]+[b]+levels[i+1:]; e2=eta_of(op_levels(trial)+tail)
                        if e2<cur-1e-12: cur=e2; bi=b
                    if bi!=levels[i]: levels[i]=bi; improved=True
                if not improved: break
            e=eta_of(op_levels(levels)+tail)
        if J in JLIST:
            M=op_levels(levels); e0=eta_of(M); w,V=np.linalg.eigh(M+tail); v=V[:,0]; fv=(v@F)**2*hs*2
            cen=float(np.sum(xs*fv)/np.sum(fv)); low=float(np.sum(fv[xs<20])/np.sum(fv))
            m=m_levels(levels); lv=sorted(lo[b] for b in levels)
            rowsD.append((J,e,lv,float(np.max(m-beta)),cen,low,sum(1 for x in lv if x<0),e0))
            print(f"(D1) J={J:2d}: eta={e:.4f} ({e/Dg:.3f} D_a) [grid-only {e0:.4f}]  J*eta/D_a={J*e/Dg:.2f}  levels<0: {rowsD[-1][6]:2d}  top level {lv[-1]:+.2f}  "
                  f"min-direction centroid xi={cen:.1f}, mass below xi=20: {low:.2f}  violation {rowsD[-1][3]:.1e}  [{time.time()-t0:.0f}s]")
    print("    levels at J=8: "+", ".join(f"{x:+.2f}" for x in rowsD[JLIST.index(8)][2]))
    R.update(D1=rowsD)

    # ---- (D2) lattice-periodic comb: G(rho) = {dist(xi L/2pi, Z) <= rho} within cells |n| <= U, uniform profile ----
    u=xs*L/(2*math.pi); cell=np.rint(u); rho=np.abs(u-cell); ring=np.minimum((rho*2*NRING).astype(int),NRING-1)
    rowsD2=[]
    for U in (None,):
        mask=np.ones(len(xs),bool) if U is None else (cell<=U)
        Br=[cmat(mask&(ring==k)) for k in range(NRING)]
        rmin=np.array([beta[mask&(ring==k)].min() if np.any(mask&(ring==k)) else np.inf for k in range(NRING)])
        g=np.minimum.accumulate(rmin[::-1])[::-1]; g=np.minimum(g,0.0) if False else g   # nonincreasing in rho
        M=sum(gk*Bk for gk,Bk in zip(g,Br))-Dg*(Cg-sum(Br)); e,e0=eta2(M,tail)
        m=np.full(len(xs),-Dg); m[mask]=g[ring[mask]]
        rowsD2.append((U,e,float(g[0]),float(g[-1]),int(len(set(np.round(g,9)))),float(np.max(m-beta)),e0))
        print(f"(D2) lattice-periodic comb, all cells, {NRING} rings, profile g(rho) = min of beta over the ring and beyond: eta={e:.3f} ({e/Dg:.3f} D_a) [grid-only {e0:.3f}]; "
              f"profile g(0)={g[0]:+.3f} .. g(1/2)={g[-1]:+.3f}, {rowsD2[-1][4]} distinct levels; violation {rowsD2[-1][5]:.1e}")
    R.update(D2=rowsD2)

    # ---- (D3) binary-coded uniform quantization: J sets G_j = {bit j of floor((beta+D_a)/h) is 1}, w_j = 2^j h, h=(D_a+cap)/2^J ----
    rowsD3=[]
    for J in range(1,9):
        best=None
        for cap in (1.0,2.0,3.0,4.0,5.0,6.0,8.0):
            h=(Dg+cap)/2**J; q=np.minimum(np.floor((lo+Dg)/h+1e-12),2**J-1)   # level index per bin (by lower edge: valid)
            mb=-Dg+q*h; M=np.tensordot(mb,B,axes=1); e,e0=eta2(M,tail)
            if best is None or e<best[0]:
                mg=-Dg+np.minimum(np.floor((beta+Dg)/h+1e-12),2**J-1)*h
                best=(e,cap,h,e0,float(np.max(mg-beta)))
        rowsD3.append((J,)+best)
        print(f"(D3) J={J} bit-sets = {2**J} levels, spacing h={best[2]:.3f} (cap {best[1]:.0f}): eta={best[0]:.4f} ({best[0]/Dg:.3f} D_a) [grid-only {best[3]:.4f}]  2^J*eta/D_a={2**J*best[0]/Dg:.2f}  violation {best[4]:.1e}")
    R.update(D3=rowsD3)
    print(f"   done lambda={lam} [{time.time()-t0:.0f}s]\n")
    return R

if __name__=='__main__':
    lams=[int(x) for x in sys.argv[1:]] or [3,4,6,8]
    res=[run(l) for l in lams]
    json.dump(res,open(OUT+f"comb_minorant_l{'_'.join(map(str,lams))}.json",'w'),indent=1)
