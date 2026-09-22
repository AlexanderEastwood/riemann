"""Diagnostic, not a certificate.  NS-20: arithmetic content of the pencil surplus.

For lambda = 3, 4, 6 on the even head N = 48, the first three pencil vectors v_k of
    W v = nu (W + W^-) v          (evidence/diag_true_symbol/pencil.py)
have their energy  q[v_k] = int beta_a |F v_k|^2  split into the explicit terms of the symbol
(eq:v130-beta):
    (i)   digamma    int (Re psi(5/4 + i xi/2) - log pi) |F v|^2
    (ii)  prime m    -2 Lambda(m)/sqrt(m) int cos(xi log m) |F v|^2 = -2 Lambda(m)/sqrt(m) A_v(log m)
    (iii) continuum  +2 int int_0^L e^{t/2} cos(xi t) dt |F v|^2   = +2 int_0^L e^{t/2} A_v(t) dt
where A_v(t) = int f(x) f(x+t) dx is the autocorrelation of the time-domain head function.
Each term's head matrix is assembled EXACTLY from the split Arb sequences (block() is linear in
(b, d); the split is checked against sequences()), so the term values are exact to the working
precision and sum to v^T W v identically.  The same terms are recomputed by grid quadrature of the
symbol (accuracy ~1e-5 relative, as in pencil.py), which also gives their positive-level
({beta_a > 0}) and negative-level ({beta_a < 0}) parts -- those have no closed form.
NOTE on the split: assembly_general.sequences() uses psi(1/4 - i xi/2) and folds the pole term
1/(1/4 + xi^2) = Re[1/(1/4 + i xi/2)]  (psi(5/4+z) = psi(1/4+z) + 1/(1/4+z))  into its continuum piece,
whose time-domain kernel is 2 cosh(t/2) = e^{t/2} + e^{-t/2} on |t| <= L.  The symbol's own split (i)/(iii)
is recovered exactly by moving the Lorentzian  int |F v|^2/(1/4+xi^2) = 2 int_0^L e^{-t/2} A_v(t) dt
(closed form below, and independently the e^{t/2} kernel gives (iii) directly).
The pencil vectors come from the float W^- (~1e-7 relative, plus <= 3e-4 beyond the grid at
lambda >= 4); that error enters the pencil vector as nu * (dW^-) v, i.e. scaled by nu itself, so
v^T W v = nu_k q+[v_k] to the RELATIVE accuracy of W^- however small nu_k is (pencil.py, and checked
here: the exact term sum reaches nu_k q+).  The exact eigenvectors of W (e_k) are decomposed too.
Run from the repo root with .venv/bin/python; cases as "lam,N,bits" arguments."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')
import numpy as np, mpmath as mp
from flint import arb, acb, ctx
from assembly_general import sequences, block, pairs
from cert import tomp
from pencil import beta_grid, Fe_grid

def label(m, p):
    k=round(math.log(m)/math.log(p))
    return f"{p}" if k==1 else f"{p}^{k}"

def sequences_split(lam, J, bits, K=96):
    """Same arithmetic as assembly_general.sequences, but the (b, d) pair returned per symbol term."""
    ctx.prec=bits
    L=2*arb(lam).log(); pi=arb.pi(); h=(L/4).sinh()**2
    pw=[(m,p,arb(m).log(),arb(p).log()/arb(m).sqrt()) for m,p in pairs(lam)]
    ks=[(2*k+arb(1)/2,arb(1)/arb(lam)**(4*k+1)) for k in range(K)]
    aK=2*K+arb(1)/2; eK=arb(1)/arb(lam)**(4*K+1)
    es=eK/(2*aK*(1-arb(1)/lam**4)); ed=2*eK/(L*aK*aK*(1-arb(1)/lam**4))
    parts={'psi':([],[]),'cont':([],[])}
    for m,p,y,w in pw: parts[m]=([],[])
    for n in range(J+1):
        t=2*pi*n/L; z=acb(arb(1)/4,-t/2); ps=z.digamma(); tri=z.polygamma(1)
        s=-ps.imag/2; a=ps.real-pi.log()+tri.real/(2*L)
        for c,e in ks:
            den=c*c+t*t; s-=e*t/den; a-=2/L*e*(c*c-t*t)/(den*den)
        s+=arb(0,es.upper()); a+=arb(0,ed.upper())
        den=L*L+16*pi*pi*n*n
        parts['psi'][0].append(s/pi); parts['psi'][1].append(a)
        parts['cont'][0].append(32*L*h*n/den); parts['cont'][1].append(32*L*h*(L*L-16*pi*pi*n*n)/(den*den))
        for m,p,y,w in pw:
            parts[m][0].append((t*y).sin()*w/pi); parts[m][1].append(-2*(t*y).cos()*(1-y/L)*w)
    return parts, pw

def symbol_terms(lam, xs):
    """The same terms on the xi grid (float): psi - log pi, per prime power, continuum."""
    a=math.log(lam); L=2*a
    z=1.25+0.5j*xs; psi=np.empty_like(xs); lo=xs<40
    psi[lo]=[float(mp.re(mp.digamma(mp.mpc(1.25,0.5*x)))) for x in xs[lo]]
    zz=z[~lo]; B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6]
    s=np.log(zz)-1/(2*zz)
    for k,b in enumerate(B,1): s-=b/(2*k*zz**(2*k))
    psi[~lo]=np.real(s)
    terms={'psi':psi-math.log(math.pi)}
    for m,p in pairs(lam):
        terms[m]=-2*(math.log(p)/math.sqrt(m))*np.cos(xs*math.log(m))
    c=0.5+1j*xs; terms['cont']=2*np.real((np.exp(c*L)-1)/c)
    return terms

def corr_matrix(L, N, y):
    """S_nm(y) = A_nm(y) + A_mn(y) = 2 A_nm(y),  A_nm(y) = int_0^{L-y} e_n(x) e_m(x+y) dx  (mpmath, exact closed form)."""
    L=mp.mpf(L); th=[2*mp.pi*n/L for n in range(N+1)]; c=[1/mp.sqrt(L)]+[mp.sqrt(2/L)]*N; y=mp.mpf(y)
    S=mp.zeros(N+1,N+1)
    for n in range(N+1):
        for m in range(n+1):
            if n==m:
                S[n,n]=2*(L-y)/L if n==0 else (2/L)*((L-y)*mp.cos(th[n]*y)-mp.sin(th[n]*y)/th[n])
            else:
                S[n,m]=S[m,n]=c[n]*c[m]*((mp.sin(th[m]*y)-mp.sin(th[n]*y))/(th[n]-th[m])-(mp.sin(th[n]*y)+mp.sin(th[m]*y))/(th[n]+th[m]))
    return S

def expcorr_matrix(L, N, s, T):
    """M_nm = int_0^T e^{s t} S_nm(t) dt, so v^T M v = 2 int_0^T e^{s t} A_v(t) dt  (mpmath, exact closed form).
    s=+1/2, T=L: the continuum term (iii);  s=-1/2, T=L: the Lorentzian int |Fv|^2/(1/4+xi^2);  T=log m: running (iii)."""
    L=mp.mpf(L); s=mp.mpf(s); T=mp.mpf(T); th=[2*mp.pi*n/L for n in range(N+1)]; c=[1/mp.sqrt(L)]+[mp.sqrt(2/L)]*N
    def Isin(t):  # int_0^T e^{st} sin(t x) dx
        k=mp.mpc(s,t); return mp.im((mp.exp(k*T)-1)/k)
    def ILcos(t): # int_0^T e^{st} (L-x) cos(t x) dx
        k=mp.mpc(s,t); return mp.re(((L-T)*mp.exp(k*T)-L)/k+(mp.exp(k*T)-1)/k**2)
    J=[Isin(t) for t in th]; M=mp.zeros(N+1,N+1)
    for n in range(N+1):
        for m in range(n+1):
            if n==m:
                M[n,n]=(2/L)*ILcos(0) if n==0 else (2/L)*(ILcos(th[n])-J[n]/th[n])
            else:
                M[n,m]=M[m,n]=c[n]*c[m]*((J[m]-J[n])/(th[n]-th[m])-(J[n]+J[m])/(th[n]+th[m]))
    return M

def fmt(x, w=13):
    return f"{mp.nstr(x,6):>{w}}" if isinstance(x,(mp.mpf,)) else f"{x:>{w}.6e}"

def run(lam, N, bits, XI=4000.0, dps=120):
    t0=time.time(); a=math.log(lam); L=2*a
    print(f"\n{'='*104}\nlambda={lam}  a=log {lam}={a:.6f}  L=2a={L:.6f}  even head N={N}  bits={bits}  dps={dps}")
    # ---- grid, symbol, negative level, W^- (as pencil.py) ----
    xs=np.concatenate([np.arange(0.001,40,0.002), np.arange(40.005,XI,0.01)])
    hs=np.where(xs<40,0.002,0.01)
    beta,_=beta_grid(lam,xs); neg=np.maximum(-beta,0.0); posmask=(beta>0).astype(float); negmask=1.0-posmask
    terms=symbol_terms(lam,xs); lor=1/(0.25+xs*xs)
    tsum=sum(terms.values()); print(f"grid: {len(xs)} points to xi={XI:.0f}; split symbol vs beta_grid: max|diff| = {np.max(np.abs(tsum-beta)):.1e}")
    F=np.array([Fe_grid(n,L,xs) for n in range(N+1)]); sgn=np.array([(-1)**n for n in range(N+1)],float)
    Wm=2*(F*(neg*hs))@F.T; Wm=sgn[:,None]*Wm*sgn[None,:]
    cn=np.array([1/math.sqrt(L)]+[math.sqrt(2/L)]*N)
    Ipsi=float(mp.quad(lambda x:(mp.log(x/2)-mp.log(mp.pi))*2/(x**2)/(2*mp.pi),[XI,mp.inf]))
    # ---- exact split assembly ----
    ctx.prec=bits; Lq,b,d,aa=sequences(lam,N+8,bits); rows=list(range(N+1))
    parts,pw=sequences_split(lam,N+8,bits)
    bsum=[sum(parts[k][0][n] for k in parts) for n in range(N+9)]; dsum=[sum(parts[k][1][n] for k in parts) for n in range(N+9)]
    ctx.prec=bits
    dev=max(max(abs(float((bsum[n]-b[n]).mid())) for n in range(N+9)), max(abs(float((dsum[n]-d[n]).mid())) for n in range(N+9)))
    Wb=block(rows,rows,'even',b,d)
    Wparts={k:block(rows,rows,'even',parts[k][0],parts[k][1]) for k in parts}
    mp.mp.dps=dps
    W=tomp(Wb,dps); Wseq={k:tomp(Wparts[k],dps) for k in parts}
    Wsum=sum(Wseq.values(),mp.zeros(N+1,N+1)); dW=max(abs(Wsum[i,j]-W[i,j]) for i in range(N+1) for j in range(N+1))
    print(f"split sequences vs sequences(): max|diff| = {dev:.1e};  sum of split blocks vs block(): max|diff| = {mp.nstr(dW,3)}")
    Lor=expcorr_matrix(L,N,-0.5,L); Ccf=expcorr_matrix(L,N,0.5,L)
    dC=max(abs(Wseq['cont'][i,j]-Ccf[i,j]-Lor[i,j]) for i in range(N+1) for j in range(N+1))
    wts={m:float(w) for m,p,y,w in pw}; ms=[m for m,p,y,w in pw]; ys={m:float(y) for m,p,y,w in pw}
    Sm={m:corr_matrix(L,N,ys[m]) for m in ms}
    dP=max(max(abs(Wseq[m][i,j]+mp.mpf(wts[m])*Sm[m][i,j]) for i in range(N+1) for j in range(N+1)) for m in ms)
    print(f"sequences' continuum block vs closed-form [e^(t/2) + e^(-t/2)] kernel: max|diff| = {mp.nstr(dC,3)};  "
          f"prime blocks vs -Lambda(m)/sqrt(m) * S(log m): max|diff| = {mp.nstr(dP,3)}")
    # task split: digamma(5/4) = sequences' psi + Lorentzian; continuum e^{t/2} = sequences' cont - Lorentzian
    Wt=dict(Wseq); Wt['psi']=Wseq['psi']+Lor; Wt['cont']=Wseq['cont']-Lor
    # ---- pencil (as pencil.py) and eigenvectors of W ----
    Wp=W+mp.matrix(Wm.tolist())
    C=mp.cholesky(Wp); Ci=mp.inverse(C); M=Ci*W*Ci.T; M=(M+M.T)/2
    nu,U=mp.eigsy(M); order=sorted(range(N+1),key=lambda k:nu[k])
    E,V=mp.eigsy(W); eorder=sorted(range(N+1),key=lambda k:E[k])
    print(f"[{time.time()-t0:.0f}s] pencil nu_0..2 = {', '.join(mp.nstr(nu[order[k]],4) for k in range(3))};  eig(W) e_0..2 = {', '.join(mp.nstr(E[eorder[k]],4) for k in range(3))}")
    keys=['psi']+ms+['cont']
    names={'psi':'digamma','cont':'continuum'}; names.update({m:f"m={m} ({label(m,p)})" for m,p,y,w in pw})
    Mrun={m:expcorr_matrix(L,N,0.5,ys[m]) for m in ms}
    def decompose(vec, tag, qplus=None):
        vv=mp.matrix(vec); vv=vv/mp.sqrt((vv.T*vv)[0])                     # ||v||_2 = 1 = Plancherel mass
        vf=np.array([float(x) for x in vv]); qexact=(vv.T*W*vv)[0]
        Fv=(sgn*vf)@F; P=Fv*Fv*hs*2                                       # two-sided |F v|^2 dxi
        tail=2*float(np.dot(vf,cn))**2*Ipsi
        exact={k:(vv.T*Wt[k]*vv)[0] for k in keys}; lor_ex=(vv.T*Lor*vv)[0]
        quad={k:float(np.sum(terms[k]*P))+(tail if k=='psi' else 0.0) for k in keys}
        qpos={k:float(np.sum(terms[k]*P*posmask))+(tail if k=='psi' else 0.0) for k in keys}
        qneg={k:float(np.sum(terms[k]*P*negmask)) for k in keys}
        qp=float(np.sum(np.maximum(beta,0)*P))+tail; qm=float(np.sum(np.minimum(beta,0)*P))
        print(f"\n--- {tag} ---")
        print(f"  ||v||=1;  Plancherel {float(np.sum(P)):.6f};  mass on {{beta<0}}: {float(np.sum(P*negmask)):.4f};  q+[v] = {qp:.6f}, q-[v] = {qm:.6f} (quadrature);  "
              f"Lorentzian int|Fv|^2/(1/4+xi^2): exact {mp.nstr(lor_ex,8)}, quadrature {float(np.sum(lor*P)):.8f}")
        print(f"  {'term':<16}{'exact (closed form)':>20}{'quadrature':>15}{'rel.diff':>10}{'pos-level part':>17}{'neg-level part':>17}{'A_v(log m)':>13}")
        for k in keys:
            Astr=mp.nstr(exact[k]/(-2*wts[k]),6) if k in wts else ''
            rel=abs(quad[k]-float(exact[k]))/max(abs(float(exact[k])),1e-300)
            print(f"  {names[k]:<16}{mp.nstr(exact[k],10):>20}{quad[k]:>15.6f}{rel:>10.1e}{qpos[k]:>17.6f}{qneg[k]:>17.6f}{Astr:>13}")
        sP=sum(exact[m] for m in ms)
        print(f"  {'sum of primes':<16}{mp.nstr(sP,10):>20}{sum(quad[m] for m in ms):>15.6f}{'':>10}{sum(qpos[m] for m in ms):>17.6f}{sum(qneg[m] for m in ms):>17.6f}")
        print(f"  {'primes+continuum':<16}{mp.nstr(sP+exact['cont'],10):>20}{sum(quad[m] for m in ms)+quad['cont']:>15.6f}{'':>10}"
              f"{sum(qpos[m] for m in ms)+qpos['cont']:>17.6f}{sum(qneg[m] for m in ms)+qneg['cont']:>17.6f}")
        tot=sum(exact.values())
        print(f"  {'TOTAL':<16}{mp.nstr(tot,6):>20}{sum(quad.values()):>15.6e}{'':>10}{sum(qpos.values()):>17.6f}{sum(qneg.values()):>17.6f}")
        print(f"  v^T W v (exact) = {mp.nstr(qexact,6)};  sum of exact terms - v^T W v = {mp.nstr(tot-qexact,3)}"+(f";  nu_k * q+ = {mp.nstr(qplus,4)}" if qplus is not None else ''))
        print(f"  running remainder: partial prime sums against the continuum integral up to log m  (C(<=T) = 2 int_0^T e^(t/2) A_v(t) dt):")
        print(f"    {'m':>6}{'log m':>9}{'A_v(log m)':>13}{'P_m':>13}{'sum P_<=m':>13}{'C(<=log m)':>13}{'psi+sumP+C':>13}")
        cum=mp.mpf(0)
        for m in ms:
            cum+=exact[m]; cr=(vv.T*Mrun[m]*vv)[0]
            print(f"    {m:>6}{ys[m]:>9.4f}{float(exact[m]/(-2*wts[m])):>13.6f}{float(exact[m]):>13.6f}{float(cum):>13.6f}{float(cr):>13.6f}{float(exact['psi']+cum+cr):>13.6f}")
        print(f"    {'L=2a':>6}{L:>9.4f}{'':>13}{'':>13}{float(cum):>13.6f}{float(exact['cont']):>13.6f}{float(exact['psi']+cum+exact['cont']):>13.6e}")
        return exact
    for k in range(3):
        u=U[:,order[k]]; v=Ci.T*u; v=v/mp.sqrt((v.T*v)[0]); qp=(v.T*Wp*v)[0]
        decompose([v[i] for i in range(N+1)], f"pencil vector v_{k}: nu_{k} = {mp.nstr(nu[order[k]],4)}", nu[order[k]]*qp)
    for k in range(3):
        decompose([V[i,eorder[k]] for i in range(N+1)], f"eigenvector of W, e_{k} = {mp.nstr(E[eorder[k]],4)} (exact cross-check: the sum reaches e_k)")
    print(f"[{time.time()-t0:.0f}s]")

if __name__=='__main__':
    cases=[tuple(int(x) for x in c.split(',')) for c in sys.argv[1:]] or [(3,48,1024),(4,48,1024),(6,48,2048)]
    for lam,N,bits in cases: run(lam,N,bits)
