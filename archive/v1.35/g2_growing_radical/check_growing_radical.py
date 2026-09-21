"""Independent diagnostics for v1.35; these are not interval certificates.

Analytic proofs, including all cofinal constants, are in new_section.tex.
No finite-window positivity or RH claim is inferred from these checks.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

C = 4 * math.pi / math.sqrt(3)

def source(u):
    z = np.asarray(u)
    return C*z*z*(2*math.pi*z*z-3)*np.exp(-math.pi*z*z)

def k(x):
    # Reflection uses the proved Poisson identity, not a fitted symmetry.
    u = math.exp(abs(x))
    if u > 20:
        return 0.0
    n = np.arange(1, 22)
    return math.sqrt(u)*float(np.sum(source(n*u)))

def direct_k(x):
    u = math.exp(x)
    n = np.arange(1, max(22, int(12/u)+1))
    return math.sqrt(u)*float(np.sum(source(n*u)))

kappa2 = 2*quad(lambda x:k(x)**2,0,4,epsabs=1e-12)[0]
M2 = math.sqrt(2*quad(lambda x:(1+x)**4*k(x)**2,0,4,
                     epsabs=1e-12)[0]/kappa2)
D = math.ceil(4*math.pi*math.sqrt(M2))
poisson_error = max(abs(direct_k(x)-direct_k(-x)) for x in [0,.2,.5,1.])
moment_zero = quad(lambda x:float(source(x)),0,8,epsabs=1e-12)[0]

# Polynomial complex vectors test both pole signs and the cancellation.
# The pointwise kernel check avoids treating cusp quadrature as exact.
checks = []
z, w = leggauss(120)
for lam in [3,4,5]:
    a = math.log(lam)
    x, weights = a*z, a*w
    plus = np.exp(np.abs(x[:,None]-x[None,:])/2)
    minus = np.exp(-np.abs(x[:,None]-x[None,:])/2)
    c, s = np.cosh(x/2), np.sinh(x/2)
    pole = 2*np.outer(c,c)-2*np.outer(s,s)
    kernel_error = float(np.max(np.abs(pole-plus-minus)))
    f = (1-z*z)**2*(1+.3*z*z+1j*(z+.2*z**3))
    v = weights*f
    full_error = abs(np.vdot(v,(pole-plus-minus)@v))
    # Omitting the negative odd pole must produce a nonzero wrong answer.
    missing_odd_pole = 2*abs(np.sum(weights*f*s))**2
    checks.append(dict(lam=lam,kernel_error=kernel_error,
                       complex_form_error=float(full_error),
                       missing_odd_pole=float(missing_odd_pole)))

# Riesz bound derived analytically: no numerical Gram cert is substituted.
row_bound = 8*math.pi**2*M2/(3*D*D)
result = dict(status="non-rigorous diagnostic, not a proof",
              kappa=math.sqrt(kappa2), M2=M2, diagnostic_D=D,
              analytic_row_majorant_evaluated=row_bound,
              poisson_symmetry_error=poisson_error,
              source_integral=moment_zero, parity_checks=checks)
assert row_bound < 1/6+1e-14
assert poisson_error < 2e-12
assert abs(moment_zero) < 2e-12
assert all(v["kernel_error"] < 1e-12 for v in checks)
assert all(v["missing_odd_pole"] > .01 for v in checks)
Path(__file__).with_name("diagnostic_results.json").write_text(
    json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
