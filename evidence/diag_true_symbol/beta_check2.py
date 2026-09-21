import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from beta_true import make_beta_true, Fe
mp.mp.dps=18; lam=3; beta,L=make_beta_true(lam)
ctx.prec=256; Lq,b,d,aa=sequences(lam,16,256); W=block([0,1,2,3],[0,1,2,3],'even',b,d)
XI=3000.0; h=0.01
def cn(n): return (1/mp.sqrt(L)) if n==0 else mp.sqrt(2/L)     # mode amplitude
def entry(n,m):
    tot=mp.mpf(0); xi=h/2
    while xi<XI: tot+=beta(xi)*Fe(n,L,xi)*Fe(m,L,xi)*h; xi+=h
    # averaged tail: Fe_n Fe_m ~ c_n c_m (-1)^{n+m} 4 sin^2(xi L/2)/(2 pi xi^2)  ->  sin^2 -> 1/2
    tail=(-1)**(n+m)*cn(n)*cn(m)*2/(2*mp.pi)*mp.quad(lambda x:(mp.log(x/2)-mp.log(mp.pi))/x**2,[XI,mp.inf])
    return 2*(tot+tail)
print("sign convention test: block() vs  (-1)^{n+m} * quad   (centered-cosine transform)")
for (n,m) in ((0,0),(1,1),(0,1),(1,2),(0,2),(1,3)):
    q=entry(n,m); ref=float(W[n,m].mid()); flip=(-1)**(n+m)*float(q)
    print(f"  W[{n},{m}]  block={ref:+.8f}  quad={float(q):+.8f}  (-1)^(n+m)*quad={flip:+.8f}  rel.err={(flip-ref)/abs(ref):+.1e}", flush=True)
