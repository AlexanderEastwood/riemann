"""Verify the closed forms for the Nyman-Beurling-Baez-Duarte Gram matrix
against direct high-precision quadrature.

Hilbert space H = L^2((0,inf), dx).  rho_n(x) = {1/(n x)},  chi = 1_(0,1].
Substituting t = 1/x:  <rho_m, rho_n> = int_0^inf {t/m}{t/n} dt/t^2.
"""
from mpmath import mp, mpf, quad, log, pi, euler, zeta, cot, floor, nstr
from math import gcd, lcm

mp.dps = 40

def frac(x):
    return x - floor(x)

def gram_quad(m, n):
    """<rho_m, rho_n> by folding: the integrand {t/m}{t/n} is periodic with
    period L = lcm(m,n) in the fractional parts, so
      int_0^inf f(t) dt/t^2 = int_0^L f(u) * sum_{k>=0} (u+kL)^{-2} du
                            = int_0^L f(u) * zeta(2, u/L) / L^2 du,
    and f is polynomial between consecutive multiples of m and n."""
    L = int(lcm(m, n))
    bps = sorted(set([0] + [k*m for k in range(1, L//m+1)] + [k*n for k in range(1, L//n+1)]))
    total = mpf(0)
    for a, b in zip(bps[:-1], bps[1:]):
        f = lambda u: frac(u/mpf(m))*frac(u/mpf(n))*zeta(2, u/mpf(L))/mpf(L)**2
        total += quad(f, [a, b])
    return total

def V(h, k):
    """Vasyunin sum V(h/k) = sum_{m=1}^{k-1} {m h/k} cot(pi m/k)."""
    h, k = int(h), int(k)
    return sum(mpf((m*h) % k)/k * cot(pi*m/k) for m in range(1, k))

def gram_closed_coprime(h, k):
    """Vasyunin / Bettin-Conrey closed form, coprime h,k (eq. (1.3) of arXiv:1705.09921):
    (1/(2 pi sqrt(hk))) int |zeta(1/2+it)|^2 (h/k)^{it} dt/(1/4+t^2)
      = (log 2pi - gamma)/2 (1/h + 1/k) + (k-h)/(2hk) log(h/k) - pi/(2hk) (V(h/k)+V(k/h))."""
    h, k = mpf(h), mpf(k)
    return ((log(2*pi) - euler)/2*(1/h + 1/k) + (k-h)/(2*h*k)*log(h/k)
            - pi/(2*h*k)*(V(h, k) + V(k, h)))

def gram_closed(m, n):
    g = int(gcd(m, n))
    return gram_closed_coprime(m//g, n//g)/g

def b_quad(n):
    """<chi, rho_n> = int_0^1 {1/(n x)} dx = int_1^inf {t/n} dt/t^2."""
    # fold on [1, inf): breakpoints at multiples of n; tail beyond K*n handled by zeta(2,.)
    n = int(n)
    # exact: (1/n) int_{1/n}^inf {u} du/u^2 ; split [1/n,1] (where {u}=u) and [1,inf)
    part1 = quad(lambda u: 1/u, [mpf(1)/n, 1])/n
    part2 = quad(lambda u: frac(u)*zeta(2, u+1), [0, 1])/n   # int_1^inf {u}/u^2 du folded (k>=1 terms)
    return part1 + part2

def b_closed(n):
    return (log(n) + 1 - euler)/mpf(n)

if __name__ == "__main__":
    print("mp.dps =", mp.dps)
    print("<rho_1,rho_1>: quad", nstr(gram_quad(1,1), 30), " closed log2pi-gamma", nstr(log(2*pi)-euler, 30))
    for (m, n) in [(1,2), (2,3), (3,5), (2,4), (4,6), (5,7), (3,8)]:
        q = gram_quad(m, n); c = gram_closed(m, n)
        print(f"<rho_{m},rho_{n}>: quad {nstr(q,30)}  closed {nstr(c,30)}  diff {nstr(q-c,3)}")
    for n in [1, 2, 3, 7]:
        q = b_quad(n); c = b_closed(n)
        print(f"<chi,rho_{n}>: quad {nstr(q,30)}  closed {nstr(c,30)}  diff {nstr(q-c,3)}")
    C = 2 + euler - log(4*pi)
    print("C = 2+gamma-log(4pi) =", nstr(C, 40))
