# Route A: Li coefficients from the definition (Taylor coefficients of
#   d/dz log xi(1/(1-z)) = sum_{n>=1} lambda_n z^{n-1})
# via a Cauchy integral (trapezoid rule on a circle of radius r), using
# xi'/xi(s) = 1/s + 1/(s-1) - log(pi)/2 + psi(s/2)/2 + zeta'(s)/zeta(s).
# Route B: Bombieri-Lagarias / Coffey arithmetic formula
#   lambda_n = 1 - (n/2)(gamma + log pi + 2 log 2)
#             + sum_{j=2}^n (-1)^j C(n,j) (1-2^{-j}) zeta(j)
#             - sum_{j=1}^n C(n,j) eta_{j-1}
#   with zeta'/zeta(s) = -1/(s-1) - sum_{k>=0} eta_k (s-1)^k  (eta_0 = -gamma).
import sys, json
from mpmath import mp, mpf, mpc, zeta, digamma, log, pi, euler, binomial, exp, expj, nstr, fsum

NMAX = 60
mp.dps = 80

def xi_log_deriv(s):
    return 1/s + 1/(s-1) - log(pi)/2 + digamma(s/2)/2 + zeta(s, derivative=1)/zeta(s)

def taylor_by_cauchy(g, r, N, nmax):
    # coefficients c_k, k=0..nmax of g(z) = sum c_k z^k, |z|<=r analytic
    vals = [g(r*expj(2*pi*k/N)) for k in range(N)]
    coeffs = []
    for m in range(nmax+1):
        c = fsum(vals[k]*expj(-2*pi*k*m/N) for k in range(N)) / N / r**m
        coeffs.append(c)
    return coeffs

def route_A(r, N):
    g = lambda z: xi_log_deriv(1/(1-z)) / (1-z)**2
    c = taylor_by_cauchy(g, mpf(r), N, NMAX-1)
    return [x.real for x in c], max(abs(x.imag) for x in c)

def eta_coeffs(kmax, r=mpf(1), N=256):
    h = lambda w: zeta(1+w, derivative=1)/zeta(1+w) + 1/w   # analytic near w=0
    c = taylor_by_cauchy(h, r, N, kmax)
    return [-x.real for x in c]                               # eta_k = -c_k

def route_B():
    eta = eta_coeffs(NMAX-1)
    out = []
    for n in range(1, NMAX+1):
        S1 = fsum((-1)**j * binomial(n,j) * (1-mpf(2)**(-j)) * zeta(j) for j in range(2, n+1))
        S2 = -fsum(binomial(n,j) * eta[j-1] for j in range(1, n+1))
        out.append(1 - mpf(n)/2*(euler + log(pi) + 2*log(2)) + S1 + S2)
    return out, eta

if __name__ == "__main__":
    A1, imA1 = route_A(0.5, 256)
    A2, imA2 = route_A(0.7, 320)     # stability check: different radius / node count
    B, eta = route_B()
    print("eta_0 =", nstr(eta[0], 20), " (-gamma =", nstr(-euler, 20), ")")
    print("max |Im| route A (r=.5, r=.7):", nstr(imA1, 3), nstr(imA2, 3))
    print("max |A1-A2| :", nstr(max(abs(a-b) for a,b in zip(A1,A2)), 3))
    print("max |A1-B|  :", nstr(max(abs(a-b) for a,b in zip(A1,B)), 3))
    res = {"A": [nstr(x, 40) for x in A1], "B": [nstr(x, 40) for x in B],
           "A_alt": [nstr(x, 40) for x in A2]}
    json.dump(res, open("/tmp/licriterion/lambda_arith.json","w"), indent=1)
    for n in range(1, NMAX+1):
        print(n, nstr(A1[n-1], 30), nstr(A1[n-1]-B[n-1], 3))
