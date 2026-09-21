"""The manuscript's symbol beta_a (eq:v130-beta) and a validation:
   W_nm  ?=  int_R beta_a(xi) Fe_n(xi) conj(Fe_m(xi)) dxi   (unitary F of zero extension)
against assembly_general.block() at lambda=3."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import mpmath as mp
from flint import ctx
from assembly_general import sequences, block, pairs
mp.mp.dps=18
def make_beta_true(lam):
    a=mp.log(lam); L=2*a
    pw=[(mp.log(m), mp.log(p)/mp.sqrt(m)) for m,p in pairs(lam)]    # Lambda(m)/sqrt m = log p / sqrt m
    def r(xi):
        s=2*sum(w*mp.cos(xi*y) for y,w in pw)
        c=mp.mpf(1)/2+1j*xi                                            # int_0^L e^{t/2} cos(xi t) dt = Re[(e^{cL}-1)/c]
        return s-2*mp.re((mp.exp(c*L)-1)/c)
    def beta(xi):
        return mp.re(mp.digamma(mp.mpf(5)/4+1j*xi/2))-mp.log(mp.pi)-r(xi)
    return beta,L
def Fe(n,L,xi):        # unitary transform of the zero-extended even mode: e_0=1/sqrt L, e_n=sqrt(2/L)cos(2 pi n x/L) on (-L/2,L/2)
    if n==0: return (1/mp.sqrt(L))*2*mp.sin(xi*L/2)/xi/mp.sqrt(2*mp.pi) if xi!=0 else mp.sqrt(L)/mp.sqrt(2*mp.pi)
    w=2*mp.pi*n/L
    return mp.sqrt(2/L)*(mp.sin((w-xi)*L/2)/(w-xi)+mp.sin((w+xi)*L/2)/(w+xi))/mp.sqrt(2*mp.pi)
if __name__=='__main__':
    lam=3; beta,L=make_beta_true(lam)
    ctx.prec=256; Lq,b,d,aa=sequences(lam,16,256); W=block([0,1,2],[0,1,2],'even',b,d)
    print(f"lambda={lam} L={float(L):.6f}   beta_a(0)={float(beta(0)):+.6f}  beta_a(1)={float(beta(1)):+.6f}  beta_a(10)={float(beta(10)):+.6f}  beta_a(100)={float(beta(100)):+.6f}")
    # quadrature: even integrand => 2 * int_0^XI ; trapezoid with fine step + averaged tail
    XI=3000.0; h=0.01; t0=time.time()
    def entry(n,m):
        tot=mp.mpf(0); xi=h/2
        while xi<XI:
            tot+=beta(xi)*Fe(n,L,xi)*Fe(m,L,xi)*h; xi+=h
        # tail: sin^2 -> 1/2 average, beta ~ Re psi ~ log(xi/2); crude, reported separately
        tail=mp.quad(lambda x:(mp.log(x/2)-mp.log(mp.pi))*(2/L)*(mp.mpf(1)/2)*(4/x**2)/(2*mp.pi)*(1 if n==m and n>0 else (2 if n==m==0 else 0)), [XI,mp.inf]) if n==m else 0
        return 2*tot, 2*tail
    for (n,m) in ((0,0),(1,1),(2,2),(0,1),(1,2)):
        main,tail=entry(n,m); ref=float(W[n,m].mid())
        print(f"  W[{n},{m}]  block()={ref:+.8f}   quad[0,{XI:.0f}]={float(main):+.8f}   +tail~{float(tail):+.2e}   => {float(main+tail):+.8f}   rel.err={(float(main+tail)-ref)/abs(ref):+.2e}   [{time.time()-t0:.0f}s]", flush=True)
    