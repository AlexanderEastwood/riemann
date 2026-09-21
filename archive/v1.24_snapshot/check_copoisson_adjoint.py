"""Regularized co-Poisson adjoint checks; no zero or RH experiment.

python3 check_copoisson_adjoint.py > copoisson_adjoint_checks.json
The toy source is D phi, phi=(t-1)^3(2-t)^3 on [1,2].
It has sufficient endpoint smoothness for all quadrature identities,
but is not claimed to be C-infinity or a Sonine evaluator.
"""
import json
import mpmath as mp
import numpy as np
from fractions import Fraction

mp.mp.dps = 45
hc = [0,72,-396,756,-660,270,-42]
hc_int = [0,0,36,-132,189,-132,45,-6]
dc = [j*hc[j] for j in range(1,len(hc))]
hfun = lambda t: mp.polyval(list(reversed(hc)),t)
Hfun = lambda t: mp.polyval(list(reversed(hc_int)),t)
dhfun = lambda t: mp.polyval(list(reversed(dc)),t)
assert sum(Fraction(c*(2**(j+1)-1),j+1) for j,c in enumerate(hc)) == 0
assert sum(Fraction(hc[j]*(2**j-1),j) for j in range(1,len(hc))) == 0
ac = [mp.mpf(0)] + [(-1)**k*mp.zeta(k+1)/mp.factorial(k) for k in range(1,100)]


def h(x):
    return hfun(x) if 1 < x < 2 else mp.mpf(0)


def H(x):
    return Hfun(x) if 1 < x < 2 else mp.mpf(0)


def em(x, m):
    lo = max(1, int(mp.floor(1/x))+1)
    hi = min(m, int(mp.ceil(2/x))-1)
    return mp.fsum(hfun(n*x) for n in range(lo, hi+1)) - H(m*x)/x


def adj(t, m, z=1):
    return mp.fsum(mp.exp(-z*t/n)/n for n in range(1,m+1)) - mp.e1(z*t/m)


def adj_limit(t):
    return 2*mp.euler + mp.log(t) + mp.polyval(list(reversed(ac)),t)


if __name__ == '__main__':
    roots = [mp.mpf(float(z.real)) for z in np.roots(list(reversed(dc)))
             if abs(z.imag) < 1e-10 and 1 < z.real < 2]
    variation = mp.quad(lambda x: abs(dhfun(x)), [mp.mpf(1),*sorted(roots),mp.mpf(2)])
    limit_pair = mp.quad(lambda x: hfun(x)*adj_limit(x), [1,2])
    ch = mp.sqrt(mp.quad(lambda x: (Hfun(x)/x)**2, [1,2]))
    rows=[]
    for m in [4,8,16,32]:
        cuts=sorted(set([mp.mpf(1)/n for n in range(1,m+1)]
                        +[mp.mpf(2)/n for n in range(1,m+1)]))
        primal=mp.fsum(mp.quad(lambda x: em(x,m)*mp.exp(-x), [a,b])
                       for a,b in zip(cuts[:-1],cuts[1:]))
        dual=mp.quad(lambda x: hfun(x)*adj(x,m), [1,2])
        pair_bound=variation/mp.sqrt(m)  # ||e^-x||_2 sqrt(2/m) Var(h).
        errors=[abs(adj(x,m)-adj_limit(x)) for x in [mp.mpf('1.1'),mp.mpf('1.5'),mp.mpf('1.9')]]
        row=dict(M=m, primal=float(primal), dual=float(dual),
                 adjoint_identity_error=float(abs(primal-dual)),
                 weak_limit_error=float(abs(dual-limit_pair)),
                 weak_limit_bound=float(pair_bound),
                 sampled_adjoint_error=float(max(errors)),
                 raw_norm_leading_term=float(mp.sqrt(m)*ch))
        assert abs(primal-dual) < mp.mpf('1e-35')
        assert abs(dual-limit_pair) <= pair_bound
        rows.append(row)
    # Independent finite-sum power-response check; w is not a zeta zero.
    w=mp.mpc('0.7','1.1'); B=mp.mpf(3); tt=mp.mpf('1.4')
    exact=mp.zeta(w)*tt**(w-1)+B**(w-1)/(1-w)
    power=[]
    for m in [16,64,256,1024]:
        finite=tt**(w-1)*(mp.fsum(mp.power(n,-w) for n in range(1,m+1))
                          -mp.power(m,1-w)/(1-w))+B**(w-1)/(1-w)
        power.append(dict(M=m,error=float(abs(finite-exact))))
    # First-slot-linear convention check with a genuinely complex y.
    z=mp.mpc(1,'0.4'); m=8
    cuts=sorted(set([mp.mpf(1)/n for n in range(1,m+1)]
                    +[mp.mpf(2)/n for n in range(1,m+1)]))
    cp=mp.fsum(mp.quad(lambda x: em(x,m)*mp.exp(-mp.conj(z)*x),[a,b])
               for a,b in zip(cuts[:-1],cuts[1:]))
    cd=mp.quad(lambda x: hfun(x)*mp.conj(adj(x,m,z)),[1,2])
    assert abs(cp-cd)<mp.mpf('1e-35')
    print(json.dumps(dict(scope='Finite identities and nonzero-parameter response, no arithmetic evaluator or RH evidence',
                          h_polynomial='72t-396t^2+756t^3-660t^4+270t^5-42t^6', source_moments=[0,0],
                          total_variation=float(variation), limit_pair=float(limit_pair),
                          raw_divergence_coefficient=float(ch),rows=rows,power_response=power,
                          complex_adjoint_identity_error=float(abs(cp-cd))),indent=2))
