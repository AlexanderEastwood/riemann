"""DIAGNOSTIC, NOT A CERTIFICATE (NS-21).  Lobe-mass test against the level surplus.

For the pencil vectors v_k (W v = nu (W + W^-) v on the even head, exactly as in
evidence/diag_true_symbol/pencil.py) with ||v_k||_2 = 1, compute for every negative
lobe I of beta_a in xi < 60

    mass_k(I)  = 2 int_I |F v_k|^2 dxi            (fraction of the unit Plancherel mass)
    E_k(I)     = 2 int_I beta_a |F v_k|^2 dxi     (negative-level energy in the lobe, <= 0)

and test the candidate inequalities
    (A)  mass_k(lobe nearest gamma_1) <= C nu_k
    (B)  mass_k(lobe nearest gamma_1) <= C sqrt(nu_k)
    (C)  max over lobes of mass_k(I)   <= C nu_k
with nu_k = q[v_k]/q+[v_k] from the pencil.  The vector-to-transform map carries the
(-1)^n of pencil.py (`sgn`).  Float quadrature throughout; nu_k from the mpmath pencil.
Run from the repo root with .venv/bin/python; cases as "lam,N,bits" arguments."""
import sys, math, time, json
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np, mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
from pencil import beta_grid, Fe_grid

GAMMA1 = 14.134725
KMAX = 6          # pencil vectors k = 0..5
XI_LOBE = 60.0    # lobe scan range
H_LOBE = 0.001

def pencil_vectors(lam, N, bits, dps, XI=4000.0):
    """Copy of pencil.run, returning (nu, V, L) with V[:,k] the k-th pencil vector in
    block() coordinates, ||V[:,k]||_2 = 1, and nu sorted ascending."""
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.01)])
    hs=np.where(xs<40,0.002,0.01)
    beta,L=beta_grid(lam,xs); neg=np.maximum(-beta,0.0)
    F=np.array([Fe_grid(n,L,xs) for n in range(N+1)]); sgn=np.array([(-1)**n for n in range(N+1)],float)
    Wm=2*(F*(neg*hs))@F.T
    Wm=sgn[:,None]*Wm*sgn[None,:]
    ctx.prec=bits; Lq,b,d,aa=sequences(lam,N+8,bits); rows=list(range(N+1))
    Wb=block(rows,rows,'even',b,d)
    mp.mp.dps=dps
    W=tomp(Wb,dps); Wp=W+mp.matrix(Wm.tolist())
    C=mp.cholesky(Wp); Ci=mp.inverse(C); M=Ci*W*Ci.T; M=(M+M.T)/2
    nu,U=mp.eigsy(M); order=sorted(range(N+1),key=lambda k:nu[k])
    V=Ci.T*U                          # pencil vectors: W v = nu W+ v
    nus=[]; vecs=[]
    for k in order[:KMAX]:
        v=V[:,k]
        # sanity: Rayleigh ratio reproduces nu
        num=(v.T*W*v)[0]; den=(v.T*Wp*v)[0]
        assert abs(num/den-nu[k]) <= 1e-6*abs(nu[k])+mp.mpf(10)**(-dps+10), (num/den, nu[k])
        vf=np.array([float(v[i]) for i in range(N+1)]); vf/=np.linalg.norm(vf)
        nus.append(nu[k]); vecs.append(vf)
    return nus, np.array(vecs).T, L, sgn

def transform(V, sgn, L, xs):
    """F v on the grid: sum_n sgn[n] v[n] Fe_n(xs)   (the (-1)^n of pencil.py / nearzero.py)."""
    N=V.shape[0]-1
    F=np.array([Fe_grid(n,L,xs) for n in range(N+1)])
    return (sgn[:,None]*V).T @ F          # shape (K, len(xs))

def lobes_of(beta, xs, h):
    """Maximal intervals where beta < 0, as (lo, hi) index pairs (inclusive)."""
    neg=beta<0; out=[]; i=0; n=len(xs)
    while i<n:
        if neg[i]:
            j=i
            while j+1<n and neg[j+1]: j+=1
            out.append((i,j)); i=j+1
        else: i+=1
    return out

def nearest_lobe(lobes, xs, g):
    """nearzero.py's rule: the negative interval containing the grid point nearest g,
    else the nearer of the two flanking intervals (by grid distance)."""
    j=int(np.argmin(np.abs(xs-g)))
    for (lo,hi) in lobes:
        if lo<=j<=hi: return (lo,hi)
    left=[l for l in lobes if l[1]<j]; right=[l for l in lobes if l[0]>j]
    dl=j-left[-1][1] if left else 10**9; dr=right[0][0]-j if right else 10**9
    return left[-1] if dl<=dr else right[0]

def fit_power(lx, ly):
    """least squares ly = p*lx + c; returns p, c, rms residual."""
    A=np.vstack([lx,np.ones_like(lx)]).T
    (p,c),res,_,_=np.linalg.lstsq(A,ly,rcond=None)
    r=ly-(p*lx+c)
    return p,c,float(np.sqrt(np.mean(r**2)))

def run(lam, N, bits, dps):
    t=time.time()
    nus,V,L,sgn=pencil_vectors(lam,N,bits,dps)
    cell=2*math.pi/L
    xs=np.arange(H_LOBE/2, XI_LOBE, H_LOBE); h=H_LOBE
    beta,_=beta_grid(lam,xs)
    FV=transform(V,sgn,L,xs); f2=FV**2                 # (K, nx)
    lobes=lobes_of(beta,xs,h)
    g_lobe=nearest_lobe(lobes,xs,GAMMA1)
    rows=[]
    for (lo,hi) in lobes:
        seg=slice(lo,hi+1)
        width=(hi-lo+1)*h; depth=float(beta[seg].min()); centre=float(xs[seg][np.argmin(beta[seg])])
        mass=[float(2*np.sum(f2[k,seg])*h) for k in range(KMAX)]
        en=[float(2*np.sum(beta[seg]*f2[k,seg])*h) for k in range(KMAX)]
        rows.append(dict(lo=float(xs[lo]-h/2),hi=float(xs[hi]+h/2),centre=centre,depth=depth,width=width,
                         width_cells=width/cell,u_centre=centre/cell,mass=mass,energy=en,is_gamma1=(lo,hi)==g_lobe))
    mass60=[float(2*np.sum(f2[k])*h) for k in range(KMAX)]
    massneg60=[float(2*np.sum(f2[k][beta<0])*h) for k in range(KMAX)]
    eneg60=[float(2*np.sum((beta*f2[k])[beta<0])*h) for k in range(KMAX)]
    epos60=[float(2*np.sum((beta*f2[k])[beta>0])*h) for k in range(KMAX)]
    out=dict(lam=lam,N=N,bits=bits,dps=dps,L=L,cell=cell,u_gamma1=GAMMA1/cell,
             nu=[mp.nstr(x,12) for x in nus],log10nu=[float(mp.log10(x)) if x>0 else None for x in nus],
             mass_0_60=mass60,mass_neg_0_60=massneg60,E_neg_0_60=eneg60,E_pos_0_60=epos60,
             lobes=rows,seconds=time.time()-t)
    return out

def report(out):
    lam=out['lam']; K=KMAX
    print(f"\n=== lambda={lam} N={out['N']} bits={out['bits']} dps={out['dps']}  L={out['L']:.4f}  cell 2pi/L={out['cell']:.4f}  u(gamma_1)={out['u_gamma1']:.2f}  [{out['seconds']:.0f}s] ===")
    print("  k   nu_k          log10 nu   mass[0,60)  mass{beta<0}[0,60)  E-[0,60)   E+[0,60)")
    for k in range(K):
        print(f"  {k}   {out['nu'][k]:>12}  {out['log10nu'][k]:8.2f}   {out['mass_0_60'][k]:.6f}    {out['mass_neg_0_60'][k]:.6f}        {out['E_neg_0_60'][k]:+.5f}  {out['E_pos_0_60'][k]:+.5f}")
    g=[r for r in out['lobes'] if r['is_gamma1']][0]
    print(f"\n  lobe nearest gamma_1: [{g['lo']:.3f},{g['hi']:.3f}]  centre {g['centre']:.3f}  depth {g['depth']:+.3f}  width {g['width']:.3f} = {g['width_cells']:.3f} cells")
    print("  k   log10 nu_k   log10 mass_k   log10 E_k(neg)   log10(mass/nu)   log10(mass/sqrt nu)   mass/nu^(1/10)")
    lx=np.array(out['log10nu']); lm=np.log10(np.array(g['mass'])); le=np.log10(-np.array(g['energy']))
    for k in range(K):
        print(f"  {k}   {lx[k]:9.2f}     {lm[k]:9.3f}      {le[k]:9.3f}        {lm[k]-lx[k]:9.2f}          {lm[k]-lx[k]/2:9.2f}          {10**(lm[k]-lx[k]/10):.3e}")
    p,c,rms=fit_power(lx,lm)
    print(f"  fit (gamma_1 lobe): log10 mass = {p:.4f} * log10 nu + ({c:.3f}),  rms resid {rms:.3f} decades  -> mass ~ nu^{p:.4f}")
    # (C) max over lobes
    print("\n  variant (C): max over all negative lobes in xi<60 of mass_k")
    print("  k   log10 nu_k   max mass   at lobe centre (u)   width cells   log10(max mass/nu)")
    lmx=[]
    for k in range(K):
        r=max(out['lobes'],key=lambda r:r['mass'][k]); lmx.append(math.log10(r['mass'][k]))
        print(f"  {k}   {lx[k]:9.2f}     {r['mass'][k]:.4f}   {r['centre']:7.3f} ({r['u_centre']:.2f})    {r['width_cells']:.3f}         {lmx[-1]-lx[k]:9.2f}")
    p,c,rms=fit_power(lx,np.array(lmx))
    print(f"  fit (max lobe): log10 maxmass = {p:.4f} * log10 nu + ({c:.3f}), rms {rms:.3f}")
    print("\n  all negative lobes in xi<60 (u = centre in cells; mass_k and E_k for k=0..5):")
    print("  centre    u     depth   w/cell  " + "  ".join(f"  mass_{k}  " for k in range(K)) + " | " + "  ".join(f"   E_{k}   " for k in range(K)))
    for r in out['lobes']:
        tag='*' if r['is_gamma1'] else ' '
        print(f" {tag}{r['centre']:7.3f} {r['u_centre']:6.2f} {r['depth']:+7.3f} {r['width_cells']:6.3f}  "
              + "  ".join(f"{m:.3e}" for m in r['mass']) + " | " + "  ".join(f"{e:+.2e}" for e in r['energy']))

def pooled(results):
    print("\n=== pooled across lambda, gamma_1 lobe, k=0..5 ===")
    lx=[];lm=[];lab=[]
    for out in results:
        g=[r for r in out['lobes'] if r['is_gamma1']][0]
        for k in range(KMAX):
            lx.append(out['log10nu'][k]); lm.append(math.log10(g['mass'][k])); lab.append((out['lam'],k))
    lx=np.array(lx); lm=np.array(lm)
    p,c,rms=fit_power(lx,lm)
    print(f"  log10 mass = {p:.4f} * log10 nu + ({c:.3f}), rms {rms:.3f} decades over {len(lx)} points")
    print(f"  range of log10(mass/nu):      [{(lm-lx).min():.1f}, {(lm-lx).max():.1f}]")
    print(f"  range of log10(mass/sqrt nu): [{(lm-lx/2).min():.1f}, {(lm-lx/2).max():.1f}]")
    print(f"  range of log10 mass:          [{lm.min():.2f}, {lm.max():.2f}]   range of log10 nu: [{lx.min():.1f}, {lx.max():.1f}]")
    print("\n  ground direction k=0 across lambda (gamma_1 lobe):")
    print("  lam   log10 nu_0   log10 mass_0   log10 E_0   C needed for mass<=C nu   C for mass<=C sqrt(nu)   depth   u(gamma_1)")
    for out in results:
        g=[r for r in out['lobes'] if r['is_gamma1']][0]; lx0=out['log10nu'][0]; lm0=math.log10(g['mass'][0])
        print(f"  {out['lam']}   {lx0:9.2f}     {lm0:9.3f}     {math.log10(-g['energy'][0]):9.3f}     1e{lm0-lx0:.1f}                 1e{lm0-lx0/2:.1f}              {g['depth']:+.3f}   {out['u_gamma1']:.2f}")

if __name__=='__main__':
    if sys.argv[1:2]==['--pool']:
        results=[json.load(open(f'evidence/diag_lobe_mass/lobe_mass_l{lam}.json')) for lam in (3,4,6,8)]
        for out in results: report(out)
        pooled(results); sys.exit()
    default=[(3,48,1024,120),(4,48,1024,120),(6,48,2048,180),(8,48,2048,180)]
    cases=[tuple(int(x) for x in c.split(',')) for c in sys.argv[1:]] or default
    results=[]
    for lam,N,bits,dps in cases:
        out=run(lam,N,bits,dps); results.append(out); report(out); sys.stdout.flush()
        with open(f'evidence/diag_lobe_mass/lobe_mass_l{lam}.json','w') as f: json.dump(out,f,indent=1)
    if len(results)>1: pooled(results)
