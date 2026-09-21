import sys, time, json
from flint import arb, arb_mat, ctx
sys.path.insert(0, "/tmp/nymanbeurling")
from compute_dN import build_arb, dN2_arb
NMAX = int(sys.argv[1]); PREC = int(sys.argv[2])
ctx.prec = PREC
t0 = time.time(); G, b = build_arb(NMAX); t1 = time.time()
C = 2 + arb.const_euler() - (4*arb.pi()).log()
Ns = list(range(1, 101)) + list(range(110, NMAX+1, 10))
print(f"# Arb {PREC} bits, Gram build {t1-t0:.1f}s")
rows = []
for N in Ns:
    d2 = dN2_arb(G, b, N)
    lg = d2*arb(N).log() if N > 1 else arb(0)
    rows.append((N, d2.str(30, radius=False), lg.str(20, radius=False), (lg/C).str(10, radius=False), float(d2.rad())))
    print(f"  {N:>4} {rows[-1][1]:>34} {rows[-1][2]:>24} {rows[-1][3]:>14} {rows[-1][4]:>10.1e}", flush=True)
print(f"# total {time.time()-t0:.1f}s")
json.dump(rows, open(f"/tmp/nymanbeurling/dN_arb_{PREC}bits_N{NMAX}_ext.json", "w"), indent=1)
