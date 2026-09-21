# Windowed Li coefficients (closed form, no quadrature).
#   Phi_n^{[b]}(s) = int_0^b L^{(1)}_{n-1}(t) e^{-st} dt
#                  = sum_{k=1}^n C(n,k)(-1)^{k-1} s^{-k} [1 - e^{-sb} e_{k-1}(sb)],  e_m(z)=sum_{j<=m} z^j/j!
#   (b -> inf recovers G_n(s) = 1-(1-1/s)^n).
#   lambda_n^{[b]} := sum over conjugate pairs |Phi(rho)|^2  (rho = 1/2 + i gamma on the line)
#                  = (1/2) sum_rho Phi(rho) Phi(1-rho).
import json, sys
from mpmath import mp, mpf, mpc, binomial, exp, log, fsum, nstr, quad, pi, inf, laguerre, factorial

mp.dps = 50
NZ = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
gam = [mpf(g) for g in json.load(open("zeros_%d.json" % NZ))]
lam = {int(k): mpf(v[0]) + mpf(v[1]) for k, v in json.load(open("lambda_zeros_%d.json" % NZ)).items()}

def Phi(n, s, b):
    E = exp(-s*b); z = s*b
    tot = mpf(0); em = mpf(0); zj = mpf(1)
    for k in range(1, n+1):
        em += zj / factorial(k-1); zj *= z          # e_{k-1}(z)
        tot += binomial(n, k) * (-1)**(k-1) * s**(-k) * (1 - E*em)
    return tot

def G(n, s): return 1 - (1 - 1/s)**n

# sanity: Phi -> G as b grows, at a sample zero
s0 = mpc(mpf(1)/2, gam[0])
for b in [1, 5, 20, 80, 200]:
    print("b=%4d  |Phi_5 - G_5| = %s" % (b, nstr(abs(Phi(5, s0, mpf(b)) - G(5, s0)), 3)))

def windowed(n, b):
    T = gam[-1]
    partial = fsum(abs(Phi(n, mpc(mpf(1)/2, g), b))**2 for g in gam)
    Lb = laguerre(n-1, 1, b)
    tail = quad(lambda t: (n**2 + Lb**2*exp(-b)) / t**2 * log(t/(2*pi))/(2*pi), [T, 10*T, inf])
    return partial, tail

b = 2*log(4)
print("\nWindow b = 2 log 4 = log 16 =", nstr(b, 8), " (f supported in [-a,a], a = log 4, after dilation)")
print(" n   lambda_n        lambda_n^{[log16]} (zeros)   +tail(approx)   ratio  lambda_n^{[log16]}/n^2")
rows = {}
for n in [1,2,3,4,5,6,8,10,15,20,30,40,60]:
    p, t = windowed(n, b)
    rows[n] = (p, t)
    print("%3d  %-14s  %-26s  %-14s  %-6s %s" % (n, nstr(lam[n], 10), nstr(p, 10), nstr(p+t, 10), nstr((p+t)/lam[n], 4), nstr((p+t)/n**2, 5)))
print("\nConvergence in the window for n = 5: lambda_5 =", nstr(lam[5], 12))
for bb in [log(16), 5, 10, 20, 40, 80]:
    p, t = windowed(5, mpf(bb))
    print("  b = %-8s  lambda_5^{[b]} = %s" % (nstr(bb, 5), nstr(p+t, 12)))
json.dump({n: [nstr(p, 25), nstr(t, 25)] for n, (p, t) in rows.items()}, open("lambda_windowed.json", "w"), indent=1)
