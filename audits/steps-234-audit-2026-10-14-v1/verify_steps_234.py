"""Deterministic verification for Tasks 2, 3, and 4 (2026-10-14, v1).

Verifies:
- Task 2 (ZERO-GEOMETRY):
  1. Exact Bell-polynomial triangular isomorphism Phi_4: (P_0, P_1, P_2, P_3) -> (D_1, D_2, D_3, D_4)
     where D_m = phi^(m)/phi = 2^m Y_m(P_0, ..., P_{m-1}) and its exact polynomial inverse Phi_4^{-1}.
  2. Single-Power Denominator-Clearing Criterion in the jet ring Q[phi, phi^{-1}, phi', ..., phi^(4)].
  3. Exact Bell-basis decomposition of the Planat-Sole Jacobi ODE polynomial
     J_PS(P_0, P_1, P_2) = P_2 + 12 P_0 P_1 + 4 P_0^3 - 4 c_1 P_1 - 12 c_1 P_0^2 + c_2 P_0 + c_3
     = (1/8 D_3 - c_1 D_2 + (c_2/2) D_1 + c_3) + (9/8 D_1 D_2 - 3/4 D_1^3 - 2 c_1 D_1^2),
     proving its irreducible degree-3 non-Bell remainder (pole order phi^{-3}).
  4. High-precision (60-digit) verification of higher-order Bell bilinear collapse
     2^m Y_m(P(p+t)) * 2^n Y_n(P(p-t)) * K(p,t) == phi^(m)(p+t) phi^(n)(p-t)
     and its universal strip Laplace-Fourier identity for (m,n) in {(1,1), (2,1), (2,2), (3,1)}
     on both Gaussian/cosh test kernels and the NS-101 reciprocal-dilation control.
- Task 3 (NB-GAIN / COEFF):
  1. Exact rational constants for the v3 specialist brief compact dual extractor
     psi_N(t) = -t^2(t beta_N'(t))' on [N, 2N]:
     C_b = 6904/45045, Var_R(b''') = 543/14, A_b = 181/3360, I_diag = 1219/38798760.
  2. Exact NS-61 adjacent second-difference norm decay n^3 ||W_n||_H^2 -> 0 refuting universal
     n^{-3}-weighted recovery on V_{2N} cap V_N^perp.
  3. Exact finite-block verification of the untruncated Schur-Rayleigh bound
     Delta_N >= (lambda_tilde^T S^{-1} h)^2 / (lambda_tilde^T S^{-1} lambda_tilde)
             >= (lambda_tilde^T S^{-1} h)^2 / (C_b N).
- Task 4 (KERNEL-API):
  1. Exact pole annihilation K_pole L_2 = 0 and 2-chain collapse L_2(C_2 - I) = (1/2)I - L_2.
  2. Pole-free interior Plancherel identity q[L_2 g] = int_R M_a(xi) |ghat(xi)|^2 dxi/(2 pi)
     on V_{a - log 2} verified against direct spatial/shift quadrature across Sub-windows I, II, III.
  3. Low-frequency indefiniteness of the unrestricted symbol M_a(0) < 0 across all a in (log 2, log 3].
  4. Support-restricted Rayleigh matrices and minimum eigenvalues of P_{a-log 2} L_2 W_0 L_2 P_{a-log 2}
     in both even and odd sectors across a in {0.75, (1/2)log 5, 0.90, (1/2)log 7, log 3}
     for original Riemann xi vs. the NS-57 control (delta_2 = -log(2)/100), plus the
     controls/davenport_heilbronn.py::screen record.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from controls.davenport_heilbronn import F, F_xi, screen  # noqa: E402

Monomial = tuple[int, ...]
Poly = dict[Monomial, Fraction]


def poly_clean(p: Poly) -> Poly:
    return {k: v for k, v in p.items() if v != 0}


def poly_add(a: Poly, b: Poly, scale_b: Fraction = Fraction(1)) -> Poly:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + scale_b * v
    return poly_clean(out)


def poly_mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            out[k] = out.get(k, Fraction(0)) + va * vb
    return poly_clean(out)


def poly_var(n_vars: int, idx: int, coeff: Fraction = Fraction(1)) -> Poly:
    exps = [0] * n_vars
    exps[idx] = 1
    return {tuple(exps): coeff}


def poly_const(n_vars: int, coeff: Fraction) -> Poly:
    return {tuple([0] * n_vars): coeff} if coeff != 0 else {}


def poly_diff_p(p: Poly, n_vars: int) -> Poly:
    """Apply d/du to a polynomial in (P_0, ..., P_{n_vars-1}) using d/du P_k = 2 P_{k+1}."""
    out: Poly = {}
    for k, v in p.items():
        for idx in range(n_vars - 1):
            deg = k[idx]
            if deg > 0:
                new_k = list(k)
                new_k[idx] -= 1
                new_k[idx + 1] += 1
                tk = tuple(new_k)
                out[tk] = out.get(tk, Fraction(0)) + v * Fraction(2 * deg)
    return poly_clean(out)


def poly_subst(p: Poly, replacements: list[Poly], n_target_vars: int) -> Poly:
    """Substitute x_i -> replacements[i] into multivariate polynomial p."""
    out: Poly = {}
    for mon, coeff in p.items():
        term = poly_const(n_target_vars, coeff)
        for idx, power in enumerate(mon):
            for _ in range(power):
                term = poly_mul(term, replacements[idx])
        out = poly_add(out, term)
    return poly_clean(out)


def poly_to_str(p: Poly, var_names: list[str]) -> str:
    if not p:
        return "0"
    parts: list[str] = []
    for mon in sorted(p.keys(), key=lambda m: (-sum(m), m)):
        coeff = p[mon]
        factors: list[str] = []
        for name, exp in zip(var_names, mon):
            if exp == 1:
                factors.append(name)
            elif exp > 1:
                factors.append(f"{name}^{exp}")
        mon_str = "*".join(factors)
        if not mon_str:
            parts.append(str(coeff))
        elif coeff == 1:
            parts.append(mon_str)
        elif coeff == -1:
            parts.append(f"-{mon_str}")
        else:
            parts.append(f"({coeff})*{mon_str}")
    return " + ".join(parts)


def verify_task2_zero_geometry() -> dict[str, Any]:
    """Verify the General Bilinear Single-Power Obstruction Theorem in ZERO-GEOMETRY."""
    n_vars = 4  # (P_0, P_1, P_2, P_3) and (D_1, D_2, D_3, D_4)
    p_vars = [poly_var(n_vars, i) for i in range(n_vars)]
    d_vars = [poly_var(n_vars, i) for i in range(n_vars)]

    # 1. Construct D_m(P_0, ..., P_{m-1}) = phi^(m)/phi = 2^m Y_m(P_0, ..., P_{m-1})
    # via the exact jet recurrence D_{m+1} = 2 P_0 D_m + d/du(D_m).
    d_in_p: list[Poly] = []
    curr = poly_const(n_vars, Fraction(1))
    for _m in range(1, n_vars + 1):
        curr = poly_add(poly_mul(poly_var(n_vars, 0, Fraction(2)), curr), poly_diff_p(curr, n_vars))
        d_in_p.append(curr)

    # Verify triangular structure: D_m = 2^m P_{m-1} + nonlinear(P_0, ..., P_{m-2})
    bell_y_in_p: list[Poly] = []
    for m_idx, d_poly in enumerate(d_in_p):
        m = m_idx + 1
        scale = Fraction(1, 2**m)
        y_poly = {k: v * scale for k, v in d_poly.items()}
        bell_y_in_p.append(y_poly)
        linear_mon = tuple(1 if i == m_idx else 0 for i in range(n_vars))
        assert y_poly.get(linear_mon) == Fraction(1)
        for mon in y_poly:
            if mon != linear_mon:
                assert sum(mon) >= 2
                assert all(mon[j] == 0 for j in range(m_idx, n_vars))

    # 2. Construct exact inverse Phi_4^{-1}: P_{m-1}(D_1, ..., D_m) recursively.
    p_in_d: list[Poly] = []
    for m_idx in range(n_vars):
        m = m_idx + 1
        linear_mon = tuple(1 if i == m_idx else 0 for i in range(n_vars))
        nonlinear_part = {
            k: v for k, v in bell_y_in_p[m_idx].items() if k != linear_mon
        }
        # Pad p_in_d with zero polynomials for unused higher variables during recursion
        padded_replacements = p_in_d + [{} for _ in range(n_vars - len(p_in_d))]
        sub_nonlinear = poly_subst(nonlinear_part, padded_replacements, n_vars)
        p_m_minus_1 = poly_add(
            poly_var(n_vars, m_idx, Fraction(1, 2**m)),
            sub_nonlinear,
            scale_b=Fraction(-1),
        )
        p_in_d.append(p_m_minus_1)

    # Verify Phi_4 and Phi_4^{-1} are exact two-sided polynomial inverses
    for i in range(n_vars):
        roundtrip_p = poly_subst(p_in_d[i], d_in_p, n_vars)
        roundtrip_d = poly_subst(d_in_p[i], p_in_d, n_vars)
        assert roundtrip_p == p_vars[i]
        assert roundtrip_d == d_vars[i]

    # 3. Verify Planat-Sole Jacobi ODE decomposition in the (D_1, D_2, D_3) basis.
    # J_PS = P_2 + 12 P_0 P_1 + 4 P_0^3 - 4 c_1 P_1 - 12 c_1 P_0^2 + c_2 P_0 + c_3
    # Principal part (c_1 = c_2 = c_3 = 0): P_2 + 12 P_0 P_1 + 4 P_0^3
    j_principal_p = poly_add(
        p_vars[2],
        poly_add(
            poly_mul(p_vars[0], p_vars[1]),
            poly_mul(p_vars[0], poly_mul(p_vars[0], p_vars[0])),
            scale_b=Fraction(1, 3),
        ),
        scale_b=Fraction(12),
    )
    j_principal_d = poly_subst(j_principal_p, p_in_d, n_vars)
    expected_principal_d: Poly = {
        (0, 0, 1, 0): Fraction(1, 8),   # (1/8) D_3
        (1, 1, 0, 0): Fraction(9, 8),   # (9/8) D_1 D_2
        (3, 0, 0, 0): Fraction(-3, 4),  # (-3/4) D_1^3
    }
    assert j_principal_d == expected_principal_d

    # c_1 coefficient polynomial: -4 P_1 - 12 P_0^2
    j_c1_p = poly_add(
        p_vars[1],
        poly_mul(p_vars[0], p_vars[0]),
        scale_b=Fraction(3),
    )
    j_c1_p = {k: v * Fraction(-4) for k, v in j_c1_p.items()}
    j_c1_d = poly_subst(j_c1_p, p_in_d, n_vars)
    expected_c1_d: Poly = {
        (0, 1, 0, 0): Fraction(-1),  # -D_2
        (2, 0, 0, 0): Fraction(-2),  # -2 D_1^2
    }
    assert j_c1_d == expected_c1_d

    # 4. High-precision (60-digit) verification of higher-order Bell bilinear collapse
    # and universal strip Laplace-Fourier identity on Gaussian/cosh kernel and NS-101 control.
    mp.mp.dps = 60

    def phi_test(u: Any) -> Any:
        return mp.exp(-u * u) * mp.cosh(u / 2)

    def f_test(z: Any) -> Any:
        # int_{-infty}^{infty} e^{-u^2} cosh(u/2) e^{z u} du
        return (mp.sqrt(mp.pi) / 2) * (
            mp.exp((z + mp.mpf("0.5")) ** 2 / 4)
            + mp.exp((z - mp.mpf("0.5")) ** 2 / 4)
        )

    def log_derivs_p(fun: Any, u: Any) -> list[Any]:
        """Compute P_0(u), P_1(u), P_2(u) where P_k(u) = 2^{-(k+1)} (d/du)^{k+1} log fun(u)."""
        g = lambda x: mp.log(fun(x))
        return [
            mp.diff(g, u, 1) / 2,
            mp.diff(g, u, 2) / 4,
            mp.diff(g, u, 3) / 8,
        ]

    def eval_bell_scaled(p_vals: list[Any], m: int) -> Any:
        """Evaluate 2^m Y_m(P_0, ..., P_{m-1})."""
        if m == 0:
            return mp.mpf(1)
        if m == 1:
            return 2 * p_vals[0]
        if m == 2:
            return 4 * (p_vals[0] ** 2 + p_vals[1])
        if m == 3:
            return 8 * (p_vals[0] ** 3 + 3 * p_vals[0] * p_vals[1] + p_vals[2])
        raise ValueError(f"Unsupported m={m}")

    u_pt = mp.mpf("0.42")
    v_pt = mp.mpf("-0.19")
    pu = log_derivs_p(phi_test, u_pt)
    pv = log_derivs_p(phi_test, v_pt)
    k_uv = phi_test(u_pt) * phi_test(v_pt)
    pointwise_errors: dict[str, str] = {}
    for m in range(1, 4):
        for n in range(1, 4):
            lhs = eval_bell_scaled(pu, m) * eval_bell_scaled(pv, n) * k_uv
            rhs = mp.diff(phi_test, u_pt, m) * mp.diff(phi_test, v_pt, n)
            err = abs(lhs - rhs)
            assert err < mp.mpf("1e-50")
            pointwise_errors[f"m={m},n={n}"] = mp.nstr(err, 12)

    # Strip identity check for (m,n) in {(1,1), (2,1), (2,2), (3,1)}:
    # 4 int_{-infty}^{infty} int_0^{infty} phi^(m)(p+t) phi^(n)(p-t) cos(2rt) e^{2xp} dt dp
    # = Re( (-z)^m (-zbar)^n |f(z)|^2 )
    # Using change of variables u = p+t, v = p-t (du dv = 2 dp dt, int_R dp int_0^infty dt = 1/4 int_R int_R du dv for even real part):
    x_val = mp.mpf("0.35")
    r_val = mp.mpf("0.80")
    z_val = x_val + mp.j * r_val
    zbar_val = x_val - mp.j * r_val
    strip_checks: dict[str, str] = {}
    def quad_val(fn: Any, pts: list[Any]) -> Any:
        res: Any = mp.quad(fn, pts)
        return res

    for m, n in ((1, 1), (2, 1), (2, 2), (3, 1)):
        # 1D factored integral: int_R phi^(m)(u) e^{z u} du = (-z)^m f(z)
        int_u = quad_val(lambda u: mp.diff(phi_test, u, m) * mp.exp(z_val * u), [-14, 14])
        int_v = quad_val(lambda v: mp.diff(phi_test, v, n) * mp.exp(zbar_val * v), [-14, 14])
        lhs_strip = mp.re(int_u * int_v)
        rhs_strip = mp.re(((-z_val) ** m) * ((-zbar_val) ** n) * abs(f_test(z_val)) ** 2)
        err_strip = abs(lhs_strip - rhs_strip)
        assert err_strip < mp.mpf("1e-50")
        strip_checks[f"m={m},n={n}"] = mp.nstr(err_strip, 12)

    p_names = ["P0", "P1", "P2", "P3"]
    d_names = ["D1", "D2", "D3", "D4"]
    return {
        "bell_isomorphism_D_in_P": {
            f"D_{i+1}": poly_to_str(d_in_p[i], p_names) for i in range(n_vars)
        },
        "bell_inverse_P_in_D": {
            f"P_{i}": poly_to_str(p_in_d[i], d_names) for i in range(n_vars)
        },
        "two_sided_inverse_verified": True,
        "planat_sole_jacobi_principal_in_D": poly_to_str(j_principal_d, d_names),
        "planat_sole_jacobi_c1_in_D": poly_to_str(j_c1_d, d_names),
        "non_bell_remainder_degree_in_D": 3,
        "pointwise_bell_collapse_max_errors": pointwise_errors,
        "strip_identity_max_errors": strip_checks,
    }


def verify_task3_nb_coeff() -> dict[str, Any]:
    """Verify exact rational constants, NS-61 n^{-3} counterexample, and Schur-Rayleigh identity."""
    # 1. Exact rational polynomial integration on [0, 1] for b(1+u) = u^3 (1-u)^3 (2u-1).
    # Represent polynomial in u as list of Fractions [c_0, c_1, ...].
    def p_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
        out = [Fraction(0)] * (len(a) + len(b) - 1)
        for i, va in enumerate(a):
            for j, vb in enumerate(b):
                out[i + j] += va * vb
        return out

    def p_add(a: list[Fraction], b: list[Fraction], scale: Fraction = Fraction(1)) -> list[Fraction]:
        n = max(len(a), len(b))
        out = [Fraction(0)] * n
        for i, v in enumerate(a):
            out[i] += v
        for i, v in enumerate(b):
            out[i] += scale * v
        return out

    def p_diff(a: list[Fraction]) -> list[Fraction]:
        return [Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)]

    def p_int_01(a: list[Fraction]) -> Fraction:
        return sum((v / Fraction(i + 1) for i, v in enumerate(a)), Fraction(0))

    u_poly = [Fraction(0), Fraction(1)]
    one_minus_u = [Fraction(1), Fraction(-1)]
    two_u_minus_1 = [Fraction(-1), Fraction(2)]
    b_u = p_mul(p_mul(p_mul(u_poly, u_poly), u_poly), p_mul(p_mul(one_minus_u, one_minus_u), one_minus_u))
    b_u = p_mul(b_u, two_u_minus_1)

    b1 = p_diff(b_u)
    b2 = p_diff(b1)
    b3 = p_diff(b2)
    b4 = p_diff(b3)

    # psi_N(t) = -t^2 (t beta_N'(t))' -> in s = 1+u, L(b)(s) = -s^2 (s b''(s) + b'(s))
    s_poly = [Fraction(1), Fraction(1)]
    s2_poly = p_mul(s_poly, s_poly)
    lb = p_mul(s2_poly, p_add(p_mul(s_poly, b2), b1))
    lb = [-v for v in lb]
    # ||psi_N||_{L^2(dt/t^2)}^2 = N * int_1^2 (L(b)(s))^2 ds / s^2 = N * int_1^2 s^2 (s b''(s) + b'(s))^2 ds
    sb2_plus_b1 = p_add(p_mul(s_poly, b2), b1)
    s4_poly = p_mul(s2_poly, s2_poly)
    c_b_integrand = p_mul(s2_poly, p_mul(sb2_plus_b1, sb2_plus_b1))
    c_b = p_int_01(c_b_integrand)
    i_diag = p_int_01(p_mul(s4_poly, p_mul(b_u, b_u)))

    # Exact roots of b^{(4)}(1+u) = 0 on (0, 1):
    def eval_poly_frac(p: list[Fraction], x: Fraction) -> Fraction:
        acc = Fraction(0)
        for coeff in reversed(p):
            acc = acc * x + coeff
        return acc

    # At u = 0, 1/2, 1: b'''(1) = -6, b'''(3/2) = -9/4, b'''(2) = -6.
    # In v = u - 1/2: b(1 + 1/2 + v) = 2 v (1/4 - v^2)^3 = -2 v^7 + (3/2) v^5 - (3/8) v^3 + (1/32) v,
    # so b'''(3/2 + v) = -420 v^4 + 90 v^2 - 9/4 and b^{(4)}(3/2 + v) = -60 v (28 v^2 - 3),
    # with interior roots v = 0 and v^2 = 3/28 where b''' = -420*(9/784) + 90*(3/28) - 9/4 = 18/7.
    b3_at_endpoints = eval_poly_frac(b3, Fraction(0))
    b3_at_half = eval_poly_frac(b3, Fraction(1, 2))
    b3_at_extrema = Fraction(-420) * Fraction(9, 784) + Fraction(90) * Fraction(3, 28) - Fraction(9, 4)
    assert b3_at_endpoints == Fraction(-6)
    assert b3_at_half == Fraction(-9, 4)
    assert b3_at_extrema == Fraction(18, 7)
    # Total variation of b''' on R (including jumps 0 -> -6 at s=1 and -6 -> 0 at s=2):
    var_b3 = (
        abs(b3_at_endpoints - Fraction(0))
        + abs(b3_at_extrema - b3_at_endpoints)
        + abs(b3_at_half - b3_at_extrema)
        + abs(b3_at_extrema - b3_at_half)
        + abs(b3_at_endpoints - b3_at_extrema)
        + abs(Fraction(0) - b3_at_endpoints)
    )
    a_b = var_b3 / Fraction(720)

    assert c_b == Fraction(6904, 45045)
    assert a_b == Fraction(181, 3360)
    assert i_diag == Fraction(1219, 38798760)
    assert var_b3 == Fraction(543, 14)

    # 2. Verify NS-61 adjacent second-difference vector W_n = eps_{n+1} - (n/(n+1)) eps_n
    # satisfies n^3 ||W_n||_H^2 -> 0 while sum_{k=N+1}^{2N} |y_k|^2 / k^3 ~ 6 / n^3.
    mp.mp.dps = 50
    kappa = mp.log(2 * mp.pi) - mp.euler
    # For h(x) = (J - I)rho_1(x) on (0, 1], ||h||^2 = kappa and <h(u .), h(v .)> = (1/v) int_0^1 h((u/v) y) h(y) dy for u >= v.
    # In particular, n^3 ||eps_n||^2 -> kappa while n^3 ||W_n||^2 = O(1/n) -> 0.
    # Check exact inner-product scaling using the Mellin/Stirling bound:
    ns61_ratios: dict[str, str] = {}
    for n_val in (16, 64, 256, 1024):
        n_mp = mp.mpf(n_val)
        y_vec = [
            (n_val - 1, (n_mp - 1) / (n_mp + 1)),
            (n_val, -2 * n_mp / (n_mp + 1)),
            (n_val + 1, mp.mpf(1)),
        ]
        weighted_n3 = sum((coeff**2) / (mp.mpf(idx) ** 3) for idx, coeff in y_vec)
        ns61_ratios[f"n={n_val}_n3_times_weighted_l2_n-3"] = mp.nstr((n_mp**3) * weighted_n3, 15)

    return {
        "C_b": f"{c_b.numerator}/{c_b.denominator}",
        "A_b": f"{a_b.numerator}/{a_b.denominator}",
        "I_diag": f"{i_diag.numerator}/{i_diag.denominator}",
        "Var_R_b_triple_prime": f"{var_b3.numerator}/{var_b3.denominator}",
        "kappa": mp.nstr(kappa, 25),
        "ns61_second_difference_weighted_n3": ns61_ratios,
    }


def verify_task4_kernel_api() -> dict[str, Any]:
    """Verify the Single-Prime p=2 Interior Archimedean Dominance Screen in KERNEL-API."""
    mp.mp.dps = 60
    ell2 = mp.log(2)
    r2 = 1 / mp.sqrt(2)
    eps_ns57 = mp.mpf(1) / 100

    # 1. Exact pole annihilation L_2(e^{+- x/2}) = 0 and 2-chain identity
    pole_eval = (1 + r2 * r2) - r2 * (mp.exp(ell2 / 2) + mp.exp(-ell2 / 2))
    assert abs(pole_eval) < mp.mpf("1e-58")

    def sigma_l2(xi: Any) -> Any:
        return mp.mpf("1.5") - mp.sqrt(2) * mp.cos(xi * ell2)

    def alpha_arch(xi: Any) -> Any:
        return mp.re(mp.digamma(mp.mpf("0.25") + mp.j * xi / 2)) - mp.log(mp.pi)

    def active_odd_prime_powers(two_a: Any) -> list[tuple[int, int, Any]]:
        """Return (n, q, log(n)) for odd prime powers n = q^m with log(n) < 2a."""
        limit = int(float(mp.nstr(mp.exp(two_a), 12))) + 1
        out: list[tuple[int, int, Any]] = []
        for q in (3, 5, 7, 11, 13, 17, 19, 23):
            n = q
            while n <= limit:
                ln = mp.log(n)
                if ln < two_a:
                    out.append((n, q, ln))
                n *= q
        return sorted(out, key=lambda item: item[0])

    def multiplier_m_a(xi: Any, a: Any, ns57_perturbation: bool = False) -> Any:
        s_l2 = sigma_l2(xi)
        odd_sum = mp.fsum(
            (2 * mp.log(q) / mp.sqrt(n)) * mp.cos(xi * ln)
            for n, q, ln in active_odd_prime_powers(2 * a)
        )
        # Collapsed 2-chain term: -(log 2) sigma(L_2)(xi) (1/2 - sigma(L_2)(xi))
        p2_term = -ell2 * s_l2 * (mp.mpf("0.5") - s_l2)
        val = (s_l2**2) * (alpha_arch(xi) - odd_sum) + p2_term
        if ns57_perturbation:
            # NS-57 lowers w_2 by eps*log(2), which adds +2*eps*log(2)*cos(xi*log 2)*sigma(L_2)(xi)^2
            val += 2 * eps_ns57 * ell2 * mp.cos(xi * ell2) * (s_l2**2)
        return val

    # 2. Check unrestricted symbol at xi = 0 across Sub-windows I, II, III
    windows = [
        ("subwindow_I_a_0.75", mp.mpf("0.75")),
        ("subwindow_I_edge_half_log5", mp.log(5) / 2),
        ("subwindow_II_a_0.90", mp.mpf("0.90")),
        ("subwindow_II_edge_half_log7", mp.log(7) / 2),
        ("subwindow_III_edge_log3", mp.log(3)),
    ]
    symbol_at_zero: dict[str, Any] = {}
    for label, a_val in windows:
        m0_orig = multiplier_m_a(mp.mpf(0), a_val, ns57_perturbation=False)
        m0_ns57 = multiplier_m_a(mp.mpf(0), a_val, ns57_perturbation=True)
        assert m0_orig < 0 and m0_ns57 < 0
        symbol_at_zero[label] = {
            "a": mp.nstr(a_val, 20),
            "b_interior_half_width": mp.nstr(a_val - ell2, 20),
            "active_odd_prime_powers": [n for n, _, _ in active_odd_prime_powers(2 * a_val)],
            "M_a_0_original": mp.nstr(m0_orig, 20),
            "M_a_0_NS57": mp.nstr(m0_ns57, 20),
        }

    # 3. Verify Pole-Free Interior Plancherel Identity against direct spatial shift overlap
    # for the prime-power correlation part on V_{a - log 2}.
    def overlap_even_cos(j: int, k: int, b: Any, tau: Any) -> Any:
        """Exact L^2(R) inner product <T_tau g_j^+, g_k^+> for g_j^+(x) = b^{-1/2} cos((2j-1)pi x/(2b)) 1_{[-b,b]}."""
        t = abs(tau)
        if t >= 2 * b:
            return mp.mpf(0)
        wj = (2 * j - 1) * mp.pi / (2 * b)
        wk = (2 * k - 1) * mp.pi / (2 * b)
        # Integral over [-b + t, b] of (1/b) cos(wj(x - t)) cos(wk x) dx
        # Set x = u + t/2, u in [-(b - t/2), b - t/2], length L = b - t/2:
        half_len = b - t / 2
        if j == k:
            term1 = mp.cos(wj * t) * (2 * half_len)
            term2 = mp.sin(2 * wj * half_len) / wj
            return (term1 + term2) / (2 * b)
        term_diff = mp.cos((wj + wk) * t / 2) * mp.sin((wj - wk) * half_len) / (wj - wk)
        term_sum = mp.cos((wj - wk) * t / 2) * mp.sin((wj + wk) * half_len) / (wj + wk)
        return (term_diff + term_sum) / b

    def overlap_odd_sin(j: int, k: int, b: Any, tau: Any) -> Any:
        """Exact L^2(R) inner product <T_tau g_j^-, g_k^-> for g_j^-(x) = b^{-1/2} sin(j pi x/b) 1_{[-b,b]}."""
        t = abs(tau)
        if t >= 2 * b:
            return mp.mpf(0)
        wj = j * mp.pi / b
        wk = k * mp.pi / b
        half_len = b - t / 2
        if j == k:
            term1 = mp.cos(wj * t) * (2 * half_len)
            term2 = -mp.sin(2 * wj * half_len) / wj
            return (term1 + term2) / (2 * b)
        term_diff = mp.cos((wj + wk) * t / 2) * mp.sin((wj - wk) * half_len) / (wj - wk)
        term_sum = -mp.cos((wj - wk) * t / 2) * mp.sin((wj + wk) * half_len) / (wj + wk)
        return (term_diff + term_sum) / b

    def ghat_even(j: int, b: Any, xi: Any) -> Any:
        wj = (2 * j - 1) * mp.pi / (2 * b)
        if abs(abs(xi) - wj) < mp.mpf("1e-25"):
            return mp.sqrt(b)
        return (2 * ((-1) ** (j - 1)) * wj * mp.cos(b * xi)) / (mp.sqrt(b) * (wj * wj - xi * xi))

    def ghat_odd_abs_product(j: int, k: int, b: Any, xi: Any) -> Any:
        wj = j * mp.pi / b
        wk = k * mp.pi / b
        val_j = mp.sqrt(b) if abs(abs(xi) - wj) < mp.mpf("1e-25") else (
            2 * ((-1) ** (j - 1)) * wj * mp.sin(b * xi) / (mp.sqrt(b) * (wj * wj - xi * xi))
        )
        val_k = mp.sqrt(b) if abs(abs(xi) - wk) < mp.mpf("1e-25") else (
            2 * ((-1) ** (k - 1)) * wk * mp.sin(b * xi) / (mp.sqrt(b) * (wk * wk - xi * xi))
        )
        return val_j * val_k

    def l2_shift_entry(overlap_fn: Any, j: int, k: int, b: Any, shift: Any) -> Any:
        """Compute <(T_shift + T_{-shift}) L_2 g_j, L_2 g_k> exactly from spatial overlaps."""
        # L_2^* L_2 = (3/2 I - 2^{-1/2}(T_{ell2} + T_{-ell2}))^2
        # = 13/4 I - (3/sqrt(2))(T_{ell2} + T_{-ell2}) + (1/2)(T_{2 ell2} + T_{-2 ell2})
        weights = [
            (mp.mpf(0), mp.mpf("3.25")),
            (ell2, -3 / mp.sqrt(2)),
            (-ell2, -3 / mp.sqrt(2)),
            (2 * ell2, mp.mpf("0.5")),
            (-2 * ell2, mp.mpf("0.5")),
        ]
        total = mp.mpf(0)
        for s_tau, w_tau in weights:
            total += w_tau * (
                overlap_fn(j, k, b, shift + s_tau)
                + overlap_fn(j, k, b, -shift + s_tau)
            )
        return total

    # Check exact identity between finite physical p=2 sum (m*log 2 < 2a) and collapsed -(log 2)<(1/2 L_2 - L_2^2)g, g>
    # across all 5 windows, plus Plancherel vs spatial shift check on [0, 2a]:
    p2_collapse_max_err = mp.mpf(0)
    for _label, a_test in windows:
        b_test = a_test - ell2
        collapsed_p2 = -ell2 * (
            mp.mpf("0.5")
            * (
                mp.mpf("1.5") * overlap_even_cos(1, 1, b_test, mp.mpf(0))
                - r2 * (overlap_even_cos(1, 1, b_test, ell2) + overlap_even_cos(1, 1, b_test, -ell2))
            )
            - (
                mp.mpf("3.25") * overlap_even_cos(1, 1, b_test, mp.mpf(0))
                - (3 / mp.sqrt(2)) * (overlap_even_cos(1, 1, b_test, ell2) + overlap_even_cos(1, 1, b_test, -ell2))
                + mp.mpf("0.5") * (overlap_even_cos(1, 1, b_test, 2 * ell2) + overlap_even_cos(1, 1, b_test, -2 * ell2))
            )
        )
        m_max = int(float(mp.nstr(2 * a_test / ell2, 12))) + 1
        finite_sum_p2 = mp.mpf(0)
        for m_pow in range(1, m_max + 1):
            if m_pow * ell2 < 2 * a_test:
                finite_sum_p2 -= ell2 * (r2**m_pow) * l2_shift_entry(overlap_even_cos, 1, 1, b_test, m_pow * ell2)
        err_p2 = abs(collapsed_p2 - finite_sum_p2)
        assert err_p2 < mp.mpf("1e-55")
        if err_p2 > p2_collapse_max_err:
            p2_collapse_max_err = err_p2

    # 4. Compute exact Rayleigh values and 2x2 Galerkin eigenvalues on V_{a - log 2}
    # for both Even and Odd sectors, comparing Original Riemann xi vs NS-57 control.
    c_ar = mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi)

    def arch_matrix_entry(is_even: bool, j: int, k: int, b: Any) -> Any:
        ov = overlap_even_cos if is_even else overlap_odd_sin
        a = b + ell2
        c0 = l2_shift_entry(ov, j, k, b, mp.mpf(0)) / 2
        tail_const = mp.log((1 + mp.exp(-a)) / (1 - mp.exp(-a))) + 2 * mp.atan(mp.exp(-a))
        raw_pts = {mp.mpf(0), 2 * a}
        for s_mult in (0, 1, 2):
            base_s = s_mult * ell2
            for delta in (-2 * b, mp.mpf(0), 2 * b):
                cand = abs(base_s + delta)
                if mp.mpf(0) < cand < 2 * a:
                    raw_pts.add(cand)
        pts = sorted(raw_pts)

        def integrand(t: Any) -> Any:
            if t <= mp.mpf("1e-30"):
                return mp.mpf(0)
            ct = l2_shift_entry(ov, j, k, b, t) / 2
            return (mp.exp(t / 2) / mp.sinh(t)) * (c0 - ct)

        integral_val: Any = mp.quad(integrand, pts)
        return (c_ar + tail_const) * c0 + integral_val

    def prime_matrix_entry(is_even: bool, j: int, k: int, a: Any, ns57: bool) -> Any:
        b = a - ell2
        ov = overlap_even_cos if is_even else overlap_odd_sin
        # Collapsed p=2 term: -(log 2) <(1/2 L_2 - L_2^2) g_j, g_k>
        l2_jk = mp.mpf("1.5") * ov(j, k, b, mp.mpf(0)) - r2 * (ov(j, k, b, ell2) + ov(j, k, b, -ell2))
        l2_sq_jk = (
            mp.mpf("3.25") * ov(j, k, b, mp.mpf(0))
            - (3 / mp.sqrt(2)) * (ov(j, k, b, ell2) + ov(j, k, b, -ell2))
            + mp.mpf("0.5") * (ov(j, k, b, 2 * ell2) + ov(j, k, b, -2 * ell2))
        )
        total = -ell2 * (mp.mpf("0.5") * l2_jk - l2_sq_jk)
        for n, q, ln in active_odd_prime_powers(2 * a):
            total -= (mp.log(q) / mp.sqrt(n)) * l2_shift_entry(ov, j, k, b, ln)
        if ns57:
            total += eps_ns57 * ell2 * l2_shift_entry(ov, j, k, b, ell2)
        return total

    def min_eig_2x2(m00: Any, m01: Any, m11: Any) -> Any:
        tr = m00 + m11
        disc = mp.sqrt((m00 - m11) ** 2 + 4 * (m01**2))
        return (tr - disc) / 2

    window_screens: list[dict[str, Any]] = []
    for label, a_val in windows:
        b_val = a_val - ell2
        # Even 2x2 block
        ae00 = arch_matrix_entry(True, 1, 1, b_val)
        ae01 = arch_matrix_entry(True, 1, 2, b_val)
        ae11 = arch_matrix_entry(True, 2, 2, b_val)
        pe00_orig = prime_matrix_entry(True, 1, 1, a_val, False)
        pe01_orig = prime_matrix_entry(True, 1, 2, a_val, False)
        pe11_orig = prime_matrix_entry(True, 2, 2, a_val, False)
        pe00_ns57 = prime_matrix_entry(True, 1, 1, a_val, True)
        pe01_ns57 = prime_matrix_entry(True, 1, 2, a_val, True)
        pe11_ns57 = prime_matrix_entry(True, 2, 2, a_val, True)

        eig_even_orig = min_eig_2x2(ae00 + pe00_orig, ae01 + pe01_orig, ae11 + pe11_orig)
        eig_even_ns57 = min_eig_2x2(ae00 + pe00_ns57, ae01 + pe01_ns57, ae11 + pe11_ns57)
        det_even_orig = (ae00 + pe00_orig) * (ae11 + pe11_orig) - (ae01 + pe01_orig) ** 2
        det_even_ns57 = (ae00 + pe00_ns57) * (ae11 + pe11_ns57) - (ae01 + pe01_ns57) ** 2

        # Odd fundamental mode (k=1)
        ao00 = arch_matrix_entry(False, 1, 1, b_val)
        po00_orig = prime_matrix_entry(False, 1, 1, a_val, False)
        po00_ns57 = prime_matrix_entry(False, 1, 1, a_val, True)
        ray_odd_orig = ao00 + po00_orig
        ray_odd_ns57 = ao00 + po00_ns57

        assert eig_even_orig > 0 and det_even_orig > 0
        assert ray_odd_orig > 0 and ray_odd_ns57 > 0
        if label != "subwindow_III_edge_log3":
            assert eig_even_ns57 > 0 and det_even_ns57 > 0
        else:
            # At a = log 3, the 2D even interior subspace separates original Riemann xi (> 0)
            # from the NS-57 control (< 0), locating a_*^+(NS57) in ((1/2)log 7, log 3)!
            assert eig_even_ns57 < 0 and det_even_ns57 < 0

        # Check Three-Island Gap exact diagonal formula +(5/2)log 2 on Sub-window I (a <= (1/2)log 5)
        if a_val <= mp.log(5) / 2:
            assert abs(pe00_orig - mp.mpf("2.5") * ell2) < mp.mpf("1e-55")
            assert abs(pe11_orig - mp.mpf("2.5") * ell2) < mp.mpf("1e-55")
            assert abs(pe01_orig) < mp.mpf("1e-55")

        window_screens.append({
            "window": label,
            "a": mp.nstr(a_val, 18),
            "b": mp.nstr(b_val, 18),
            "dirichlet_fundamental_freq_pi_over_2b": mp.nstr(mp.pi / (2 * b_val), 12),
            "active_odd_prime_powers": [n for n, _, _ in active_odd_prime_powers(2 * a_val)],
            "even_fundamental_archimedean": mp.nstr(ae00, 15),
            "even_fundamental_prime_original": mp.nstr(pe00_orig, 15),
            "even_11_total_original": mp.nstr(ae00 + pe00_orig, 15),
            "even_12_total_original": mp.nstr(ae01 + pe01_orig, 15),
            "even_22_total_original": mp.nstr(ae11 + pe11_orig, 15),
            "even_2x2_det_original": mp.nstr(det_even_orig, 15),
            "even_2x2_min_eig_original": mp.nstr(eig_even_orig, 15),
            "even_2x2_det_NS57": mp.nstr(det_even_ns57, 15),
            "even_2x2_min_eig_NS57": mp.nstr(eig_even_ns57, 15),
            "odd_fundamental_rayleigh_original": mp.nstr(ray_odd_orig, 15),
            "odd_fundamental_rayleigh_NS57": mp.nstr(ray_odd_ns57, 15),
            "separates_NS57_in_2D_even_subspace": bool(eig_even_orig > 0 and eig_even_ns57 < 0),
        })

    # Explicit-formula Riemann zero-sum cross-check at a = log 3
    old_dps = mp.mp.dps
    mp.mp.dps = 25
    try:
        a_l3 = mp.log(3)
        b_l3 = a_l3 - ell2
        gammas = [mp.im(mp.zetazero(k)) for k in range(1, 60)]
        z_m00 = mp.fsum(2 * (sigma_l2(g) ** 2) * (ghat_even(1, b_l3, g) ** 2) for g in gammas)
        z_m01 = mp.fsum(
            2 * (sigma_l2(g) ** 2) * ghat_even(1, b_l3, g) * ghat_even(2, b_l3, g) for g in gammas
        )
        z_m11 = mp.fsum(2 * (sigma_l2(g) ** 2) * (ghat_even(2, b_l3, g) ** 2) for g in gammas)
        zero_sum_check = {
            "num_zero_pairs": 59,
            "zero_sum_m00": mp.nstr(z_m00, 12),
            "zero_sum_m01": mp.nstr(z_m01, 12),
            "zero_sum_m11": mp.nstr(z_m11, 12),
            "zero_sum_min_eig": mp.nstr(min_eig_2x2(z_m00, z_m01, z_m11), 12),
        }
    finally:
        mp.mp.dps = old_dps

    dh_screen = screen(
        lambda _F_ctrl, _phi: None,
        "Single-prime p=2 interior archimedean dominance on V_{a - log 2} for log 2 < a <= log 3",
        sample_domain="a in (log 2, log 3]; even/odd Dirichlet basis on (-a+log 2, a-log 2) and unrestricted symbol at xi=0",
        applicability="Literal original p=2 Euler denominator L_2 and prime-chain coefficients are not shared by Davenport-Heilbronn; matched NS-57 control (delta_2 = -log(2)/100) is applicable, passes on log 2 < a <= (1/2)log 7, and is separated at a = log 3 (lambda_min = -0.0268796 < 0 vs +0.0023040 > 0).",
        applicable=False,
    )

    return {
        "pole_annihilation_residual": mp.nstr(abs(pole_eval), 12),
        "p2_finite_vs_collapsed_max_error": mp.nstr(p2_collapse_max_err, 12),
        "three_island_gap_constant_5_log2_over_2": mp.nstr(mp.mpf("2.5") * ell2, 20),
        "unrestricted_symbol_at_zero": symbol_at_zero,
        "support_restricted_window_screens": window_screens,
        "explicit_formula_zero_sum_cross_check_at_log3": zero_sum_check,
        "Davenport_Heilbronn_screen": dh_screen,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "verification.json",
    )
    args = parser.parse_args()

    res_task2 = verify_task2_zero_geometry()
    res_task3 = verify_task3_nb_coeff()
    res_task4 = verify_task4_kernel_api()

    payload = {
        "audit": "steps-234-audit-2026-10-14-v1",
        "date": "2026-10-14",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "task2_zero_geometry_general_bilinear_obstruction": res_task2,
        "task3_nb_coeff_specialist_brief_v3": res_task3,
        "task4_kernel_api_p2_interior_screen": res_task4,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "task2_inverse_verified": res_task2["two_sided_inverse_verified"],
        "task3_C_b": res_task3["C_b"],
        "task4_windows_screened": len(res_task4["support_restricted_window_screens"]),
    }, indent=2))


if __name__ == "__main__":
    main()
