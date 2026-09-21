"""Floating-point Fredholm sign/scale checks, not an RH experiment.

Usage: python3 check_fredholm_shell.py > fredholm_shell_checks.json
Interval data are arbitrary complex profiles, not Sonine evaluators.
The first-slot-linear product is ip(x,y)=vdot(y,x).
"""
import json
import numpy as np
from numpy.polynomial.legendre import leggauss


def ip(x, y):
    return np.vdot(y, x)


def run(a, order):
    nodes, weights = leggauss(order)
    t = (nodes + 1) / 2
    x, w = a * t, a * weights / 2
    e = np.sqrt(w)
    F = 2 * np.cos(2 * np.pi * x[:, None] * x[None, :]) * np.outer(e, e)
    T = 2 * np.outer(e, e)
    I = np.eye(order)
    # Normalized rescaled profiles: their L2 norms do not shrink with a.
    u = e / np.sqrt(a) * (1 + 0.7j * t + t**2)
    v = e / np.sqrt(a) * (0.6 - 0.8j + (0.2 + 0.4j) * t)
    up = e / np.sqrt(a) * ((1 - 0.3j) * t + 0.2j * t**3)
    A = np.linalg.inv(I - F @ F)
    K = np.block([[I, F], [F, I]])
    uv, up0 = np.concatenate([u, v]), np.concatenate([up, np.zeros(order)])
    delta = (ip(up0, np.linalg.solve(K, up0)) - ip(uv, np.linalg.solve(K, uv))).real
    signed = (ip(up, A @ up) - ip(u, A @ u) - ip(v, A @ v)).real
    signed += 2 * ip(u, F @ A @ v).real
    m, n, mp = ip(u, e), ip(v, e), ip(up, e)
    base = (ip(up, up) - ip(u, u) - ip(v, v)).real
    correction = (4 * (m * n.conjugate()).real
                  + 4 * a * (abs(mp)**2 - abs(m)**2 - abs(n)**2)) / (1 - 4*a*a)
    KT = np.block([[I, T], [T, I]])
    deltaT = (ip(up0, np.linalg.solve(KT, up0)) - ip(uv, np.linalg.solve(KT, uv))).real
    H = (ip(up, up) + ip(u, u) + ip(v, v)).real
    bound = 4 * np.pi**2 * a**5 * H / (5 * (1 - 2*a)**2)
    cross = 2 * ip(u, F @ A @ v).real
    cross_negative = 2 * ip(u, F @ A @ (-v)).real
    out = dict(a=a, order=order, block_signed_discrepancy=abs(delta-signed),
               constant_kernel_discrepancy=abs(deltaT-base-correction),
               delta=float(delta), moment_correction=float(correction),
               remainder=float(delta-base-correction), remainder_bound=float(bound),
               remainder_bound_ratio=float(abs(delta-base-correction)/bound),
               kernel_operator_error=float(np.linalg.norm(F-T, 2)),
               kernel_operator_bound=float(4*np.pi**2*a**5/5),
               mixed_term=float(cross), mixed_term_sign_reversal=float(cross_negative),
               sign_reversal_discrepancy=abs(cross+cross_negative))
    assert out['block_signed_discrepancy'] < 1e-11
    assert out['constant_kernel_discrepancy'] < 1e-11
    assert out['remainder_bound_ratio'] <= 1 + 1e-7
    assert out['kernel_operator_error'] <= out['kernel_operator_bound'] * (1+1e-7)
    return out


if __name__ == '__main__':
    rows = [run(a, n) for a in [0.2, 0.1, 0.05, 0.025] for n in [48, 80]]
    comparisons = [dict(a=rows[i]['a'], delta_difference=abs(rows[i]['delta']-rows[i+1]['delta']))
                   for i in range(0, len(rows), 2)]
    print(json.dumps(dict(scope='Nyström algebra checks, not certified Sonine/evaluator data or RH evidence',
                          first_slot_linear=True, rows=rows, quadrature_comparison=comparisons), indent=2))
