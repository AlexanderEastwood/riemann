# Route C: lambda_n = sum_rho [1 - (1-1/rho)^n] over the first NZ zeros (mpmath.zetazero,
# rho = 1/2 + i gamma, conjugate pairs), plus a smoothed tail from the Riemann-von Mangoldt
# density  dN = (1/2pi) log(t/2pi) dt  applied to the paired weight 2 - 2 cos(n*theta(t)),
# theta(t) = arg(1 - 1/(1/2 + i t)).
import json, sys, time
from mpmath import mp, mpf, mpc, zetazero, nstr, quad, log, pi, cos, arg, inf

NZ = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
NMAX = 60
mp.dps = 30
t0 = time.time()
gam = []
for k in range(1, NZ+1):
    gam.append(zetazero(k).imag)
    if k % 250 == 0:
        print("zeros:", k, nstr(gam[-1], 12), "%.0fs" % (time.time()-t0), flush=True)
json.dump([nstr(g, 25) for g in gam], open("/tmp/licriterion/zeros_%d.json" % NZ, "w"))

def paired(n, g):
    w = 1 - 1/mpc(mpf(1)/2, g)
    return 2*(1 - w**n).real

T = gam[-1]
def theta(t):
    return arg(1 - 1/mpc(mpf(1)/2, t))
out = {}
for n in range(1, NMAX+1):
    partial = sum(paired(n, g) for g in gam)
    tail = quad(lambda t: (2 - 2*cos(n*theta(t))) * log(t/(2*pi))/(2*pi), [T, 10*T, 100*T, inf])
    out[n] = (partial, tail)
    print(n, nstr(partial, 15), nstr(tail, 8), nstr(partial+tail, 15), flush=True)
json.dump({n: [nstr(p, 25), nstr(t, 25)] for n, (p, t) in out.items()},
          open("/tmp/licriterion/lambda_zeros_%d.json" % NZ, "w"), indent=1)
