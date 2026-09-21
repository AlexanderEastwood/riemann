"""Nyman-Beurling-Baez-Duarte distances d_N in L^2((0,inf),dx):

    d_N^2 = inf_{c in C^N} || chi - sum_{n<=N} c_n rho_n ||^2,   rho_n(x) = {1/(n x)},  chi = 1_(0,1].

Closed forms (verified against quadrature in verify_formulas.py):
    <rho_h, rho_k> (gcd(h,k)=1) = (log 2pi - gamma)/2 (1/h+1/k) + (k-h)/(2hk) log(h/k)
                                  - pi/(2hk) (V(h/k) + V(k/h)),   V(h/k) = sum_{m<k} {mh/k} cot(pi m/k)
    <rho_m, rho_n>              = <rho_{m/g}, rho_{n/g}> / g,  g = gcd(m,n)   (substitute x -> x/g)
    <chi, rho_n>                = (log n + 1 - gamma)/n,   <chi,chi> = 1.
Then d_N^2 = 1 - b^T G^{-1} b  (Schur complement).

Two independent evaluations:
  (A) Arb ball arithmetic (python-flint): every d_N^2 comes as a rigorous enclosure
      [mid +- rad]; the radius is the built-in stability diagnostic, and the run
      is repeated at two precisions.
  (B) mpmath at mp.dps = 50 (and 80 for the stability check) with Cholesky.
"""
import sys, time, json
from math import gcd
from flint import arb, arb_mat, ctx

def build_arb(N):
    pi = arb.pi(); gam = arb.const_euler(); L2 = (2*pi).log()
    cache = {}
    def V(h, k):
        if k == 1: return arb(0)
        s = arb(0)
        for m in range(1, k):
            s += arb((m*h) % k)/k * (arb(m)*pi/k).cot()
        return s
    def gram_cop(h, k):
        key = (h, k)
        if key in cache: return cache[key]
        H, K = arb(h), arb(k)
        val = (L2-gam)/2*(1/H+1/K) + (K-H)/(2*H*K)*(H/K).log() - pi/(2*H*K)*(V(h,k)+V(k,h))
        cache[key] = val
        return val
    G = arb_mat(N, N)
    for m in range(1, N+1):
        for n in range(m, N+1):
            g = gcd(m, n)
            v = gram_cop(m//g, n//g)/g
            G[m-1, n-1] = v; G[n-1, m-1] = v
    b = arb_mat(N, 1)
    for n in range(1, N+1):
        b[n-1, 0] = (arb(n).log() + 1 - gam)/n
    return G, b

def dN2_arb(G, b, N):
    GN = arb_mat(N, N); bN = arb_mat(N, 1)
    for i in range(N):
        bN[i, 0] = b[i, 0]
        for j in range(N):
            GN[i, j] = G[i, j]
    x = GN.solve(bN)
    s = arb(0)
    for i in range(N):
        s += bN[i, 0]*x[i, 0]
    return 1 - s

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    PREC = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    ctx.prec = PREC
    t0 = time.time()
    G, b = build_arb(NMAX)
    t1 = time.time()
    C = 2 + arb.const_euler() - (4*arb.pi()).log()
    print(f"# Arb precision {PREC} bits; Gram build {t1-t0:.1f}s; C = 2+gamma-log(4pi) = {C.str(30)}")
    print(f"# {'N':>4} {'d_N':>22} {'d_N^2':>22} {'d_N^2 log N':>22} {'ratio/C':>12} {'rad(d_N^2)':>10}")
    rows = []
    for N in range(1, NMAX+1):
        d2 = dN2_arb(G, b, N)
        d = d2.sqrt()
        lg = d2*arb(N).log() if N > 1 else arb(0)
        ratio = lg/C
        rows.append(dict(N=N, d=d.str(25), d2=d2.str(25), d2logN=lg.str(20), ratio=ratio.str(12), rad=f"{float(d2.rad()):.2e}"))
        print(f"  {N:>4} {d.str(20, radius=False):>22} {d2.str(20, radius=False):>22} {lg.str(18, radius=False):>22} {ratio.str(8, radius=False):>12} {float(d2.rad()):>10.1e}")
    print(f"# total {time.time()-t0:.1f}s")
    with open(f"/tmp/nymanbeurling/dN_arb_{PREC}bits_N{NMAX}.json", "w") as f:
        json.dump(rows, f, indent=1)
