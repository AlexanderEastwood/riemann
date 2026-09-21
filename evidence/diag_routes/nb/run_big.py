"""Extended certified run: Gram build with per-k cotangent tables, selected N up to NMAX."""
import sys, time, json
from math import gcd
from flint import arb, arb_mat, ctx
NMAX = int(sys.argv[1]); PREC = int(sys.argv[2])
ctx.prec = PREC
pi = arb.pi(); gam = arb.const_euler(); L2 = (2*pi).log()
t0 = time.time()
cot_tab = {1: []}
for k in range(2, NMAX+1):
    cot_tab[k] = [None] + [(arb(m)*pi/k).cot() for m in range(1, k)]
def V(h, k):
    if k == 1: return arb(0)
    tab = cot_tab[k]; s = arb(0); kk = arb(k)
    for m in range(1, k):
        r = (m*h) % k
        if r: s += (arb(r)/kk)*tab[m]
    return s
def gram_cop(h, k):
    H, K = arb(h), arb(k)
    return (L2-gam)/2*(1/H+1/K) + (K-H)/(2*H*K)*(H/K).log() - pi/(2*H*K)*(V(h,k)+V(k,h))
cache = {}
G = arb_mat(NMAX, NMAX)
for m in range(1, NMAX+1):
    for n in range(m, NMAX+1):
        g = gcd(m, n); key = (m//g, n//g)
        if key not in cache: cache[key] = gram_cop(*key)
        v = cache[key]/g; G[m-1, n-1] = v; G[n-1, m-1] = v
b = arb_mat(NMAX, 1)
for n in range(1, NMAX+1): b[n-1, 0] = (arb(n).log()+1-gam)/n
t1 = time.time(); print(f"# Arb {PREC} bits; Gram build N={NMAX}: {t1-t0:.0f}s", flush=True)
C = 2 + gam - (4*pi).log()
Ns = [N for N in range(200, NMAX+1, 20)] + ([NMAX] if NMAX % 20 else [])
rows = []
for N in sorted(set(Ns)):
    ts = time.time()
    GN = arb_mat(N, N); bN = arb_mat(N, 1)
    for i in range(N):
        bN[i, 0] = b[i, 0]
        for j in range(N): GN[i, j] = G[i, j]
    x = GN.solve(bN)
    s = arb(0)
    for i in range(N): s += bN[i, 0]*x[i, 0]
    d2 = 1 - s; lg = d2*arb(N).log(); ratio = lg/C
    rows.append((N, d2.str(25, radius=False), lg.str(15, radius=False), ratio.str(10, radius=False), d2.rad().str(3)))
    print(f"  {N:>5} {rows[-1][1]:>28} {rows[-1][2]:>18} {rows[-1][3]:>13}  rad {rows[-1][4]}  ({time.time()-ts:.0f}s)", flush=True)
json.dump(rows, open(f"/tmp/nymanbeurling/dN_arb_{PREC}bits_big_N{NMAX}.json", "w"), indent=1)
print(f"# total {time.time()-t0:.0f}s")
