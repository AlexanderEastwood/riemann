"""Verification script for the October 14, 2026 four-lane audit (NB-GAIN/COEFF, KERNEL-API, ZERO-GEOMETRY, and local audit reconciliation).

All checks are deterministic paper/algebra and control-screen validations using
exact rational polynomial calculus (fractions.Fraction) and high-precision mpmath.
No blind scans, no new research rows, and no manuscript version bump.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from controls import davenport_heilbronn as dh


Poly = list[Fraction]


def poly_add(p: Poly, q: Poly) -> Poly:
    n = max(len(p), len(q))
    out = [Fraction(0)] * n
    for i, c in enumerate(p):
        out[i] += c
    for i, c in enumerate(q):
        out[i] += c
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_sub(p: Poly, q: Poly) -> Poly:
    return poly_add(p, [-c for c in q])


def poly_mul(p: Poly, q: Poly) -> Poly:
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_pow(p: Poly, exp: int) -> Poly:
    res: Poly = [Fraction(1)]
    for _ in range(exp):
        res = poly_mul(res, p)
    return res


def poly_diff(p: Poly) -> Poly:
    if len(p) <= 1:
        return [Fraction(0)]
    return [Fraction(i) * p[i] for i in range(1, len(p))]


def poly_eval(p: Poly, x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def poly_integrate_def(p: Poly, a: Fraction, b: Fraction) -> Fraction:
    anti: Poly = [Fraction(0)] + [p[i] / Fraction(i + 1) for i in range(len(p))]
    return poly_eval(anti, b) - poly_eval(anti, a)


def verify_lane1_nb_coeff() -> dict[str, Any]:
    """Verify exact rational constants and the untruncated Schur-Rayleigh identity for Proposal 04."""
    # b(s) = (s - 1)^3 * (2 - s)^3 * (2*s - 3)
    s_minus_1: Poly = [Fraction(-1), Fraction(1)]
    two_minus_s: Poly = [Fraction(2), Fraction(-1)]
    two_s_minus_3: Poly = [Fraction(-3), Fraction(2)]
    s_poly: Poly = [Fraction(0), Fraction(1)]

    b = poly_mul(poly_mul(poly_pow(s_minus_1, 3), poly_pow(two_minus_s, 3)), two_s_minus_3)

    # 1. Endpoint vanishing up to order 2 and zero mean on [1, 2]
    mean_b = poly_integrate_def(b, Fraction(1), Fraction(2))
    assert mean_b == Fraction(0), f"Expected zero mean, got {mean_b}"

    b1 = poly_diff(b)
    b2 = poly_diff(b1)
    b3 = poly_diff(b2)
    b4 = poly_diff(b3)

    for deriv in (b, b1, b2):
        assert poly_eval(deriv, Fraction(1)) == Fraction(0)
        assert poly_eval(deriv, Fraction(2)) == Fraction(0)

    # 2. Exact rational C_b = int_1^2 s^2 [b'(s) + s b''(s)]^2 ds
    psi_profile = poly_mul(s_poly, poly_add(b1, poly_mul(s_poly, b2)))
    c_b_frac = poly_integrate_def(poly_mul(psi_profile, psi_profile), Fraction(1), Fraction(2))

    # 3. Exact total variation of b''' on R (including endpoint jumps at s=1 and s=2)
    jump_1 = abs(poly_eval(b3, Fraction(1)))
    jump_2 = abs(poly_eval(b3, Fraction(2)))
    assert jump_1 == Fraction(6) and jump_2 == Fraction(6)

    # In centered coordinate u = s - 3/2 in [-1/2, 1/2],
    # b(3/2 + u) = 2 * u * (1/4 - u^2)^3 = -2*u^7 + (3/2)*u^5 - (3/8)*u^3 + (1/32)*u
    # So b^{(4)}(3/2 + u) = -1680*u^3 + 180*u = -60*u*(28*u^2 - 3).
    # Its roots in (-1/2, 1/2) are u = 0 and u = +/- sqrt(3/28)!
    # At u = +/- sqrt(3/28), u^2 = 3/28, and b'''(3/2 + u) = -420*u^4 + 90*u^2 - 9/4:
    # At u = 0: b'''(3/2) = -9/4.
    # At u^2 = 3/28: b'''(3/2 +/- sqrt(3/28)) = -420*(9/784) + 90*(3/28) - 9/4
    #              = -135/28 + 270/28 - 63/28 = 72/28 = 18/7!
    # At u = +/- 1/2: b'''(1) = b'''(2) = -420*(1/16) + 90*(1/4) - 9/4 = -6!
    b3_at_center = poly_eval(b3, Fraction(3, 2))
    assert b3_at_center == Fraction(-9, 4)
    b3_at_local_max = Fraction(-420) * Fraction(9, 784) + Fraction(90) * Fraction(3, 28) - Fraction(9, 4)
    assert b3_at_local_max == Fraction(18, 7)

    # Monotone segments of b''' on [1, 2]:
    # s=1 (val -6) -> s=3/2-sqrt(3/28) (val 18/7) -> s=3/2 (val -9/4) -> s=3/2+sqrt(3/28) (val 18/7) -> s=2 (val -6)
    interior_var = (
        (Fraction(18, 7) - Fraction(-6))
        + (Fraction(18, 7) - Fraction(-9, 4))
        + (Fraction(18, 7) - Fraction(-9, 4))
        + (Fraction(18, 7) - Fraction(-6))
    )
    total_var_b3 = jump_1 + jump_2 + interior_var
    # 2 * zeta(4) / (2*pi)^4 = 1 / 720, so A_b is an EXACT RATIONAL NUMBER!
    a_b_frac = total_var_b3 / Fraction(720)

    # 4. Exact diagonal integral int_1^2 s^4 b(s)^2 ds
    s4_b2 = poly_mul(poly_pow(s_poly, 4), poly_mul(b, b))
    i_diag_frac = poly_integrate_def(s4_b2, Fraction(1), Fraction(2))

    # 5. Direct numerical verification of the alias bound and untruncated vs truncated cost at N=16
    mp.mp.dps = 50
    n_val = 16
    lam_old: list[mp.mpf] = []
    for m in range(1, n_val + 1):
        val = mp.mpf(0)
        k = 1
        while k * m <= 2 * n_val:
            x = Fraction(k * m, n_val)
            if Fraction(1) < x < Fraction(2):
                bx = poly_eval(b, x)
                val += mp.mpf(bx.numerator) / mp.mpf(bx.denominator)
            k += 1
        lam_old.append(val)

    a_b_mp = mp.mpf(a_b_frac.numerator) / mp.mpf(a_b_frac.denominator)
    max_alias_ratio = mp.mpf(0)
    for m in range(1, n_val + 1):
        bound = a_b_mp * (mp.mpf(m) / mp.mpf(n_val)) ** 3
        ratio = abs(lam_old[m - 1]) / bound
        if ratio > max_alias_ratio:
            max_alias_ratio = ratio
    assert max_alias_ratio <= 1, f"Alias bound violated: {max_alias_ratio}"

    c_b_mp = mp.mpf(c_b_frac.numerator) / mp.mpf(c_b_frac.denominator)
    b_const = mp.mpf(1536) * (mp.pi**2 / 6) ** 2
    d_n_mp = (
        mp.sqrt(c_b_mp * n_val) + mp.sqrt(b_const) * a_b_mp * (mp.mpf(n_val) ** (-0.25))
    ) ** 2
    untruncated_cost_bound = c_b_mp * n_val
    assert untruncated_cost_bound < d_n_mp

    return {
        "C_b_rational": f"{c_b_frac.numerator}/{c_b_frac.denominator}",
        "C_b_float": float(c_b_mp),
        "b3_jump_at_endpoints": int(jump_1),
        "b4_interior_roots": ["3/2 - sqrt(3/28)", "3/2", "3/2 + sqrt(3/28)"],
        "b3_local_extrema_rational": ["-6", "18/7", "-9/4", "18/7", "-6"],
        "Var_b3_rational": f"{total_var_b3.numerator}/{total_var_b3.denominator}",
        "Var_b3_float": float(total_var_b3),
        "A_b_rational": f"{a_b_frac.numerator}/{a_b_frac.denominator}",
        "A_b_float": float(a_b_mp),
        "I_diag_rational": f"{i_diag_frac.numerator}/{i_diag_frac.denominator}",
        "I_diag_float": float(i_diag_frac),
        "N16_max_alias_over_bound": float(max_alias_ratio),
        "N16_untruncated_cost_CbN": float(untruncated_cost_bound),
        "N16_truncated_cost_DN": float(d_n_mp),
        "untruncated_strictly_smaller_than_DN": bool(untruncated_cost_bound < d_n_mp),
    }


def verify_lane2_kernel_api() -> dict[str, Any]:
    """Verify the interior adjoint embedding L_p : V_{a-ell} -> V_a, pole annihilation, NS57 defect, and the multi-prime interior support barrier."""
    mp.mp.dps = 50

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    max_pole_residual = mp.mpf(0)
    for p in primes:
        r = 1 / mp.sqrt(p)
        ell = mp.log(p)
        res = abs((1 + r**2) - 2 * r * mp.cosh(ell / 2))
        if res > max_pole_residual:
            max_pole_residual = res
    assert max_pole_residual < mp.mpf("1e-45")

    eps = mp.mpf(1) / mp.mpf(100)
    r2 = 1 / mp.sqrt(2)
    max_symbol_diff = mp.mpf(0)
    for j in range(1, 33):
        theta = mp.pi * j / 33
        l2_sym = (1 + r2**2) - 2 * r2 * mp.cos(theta)
        p2_sym = (1 - r2**2) / (1 - 2 * r2 * mp.cos(theta) + r2**2)
        p2_tilde = p2_sym - 2 * eps * mp.cos(theta)
        lhs = l2_sym * p2_tilde - (1 - r2**2)
        rhs = -eps * (
            (1 + r2**2) * (2 * mp.cos(theta)) - r2 * (2 * mp.cos(2 * theta) + 2)
        )
        diff = abs(lhs - rhs)
        if diff > max_symbol_diff:
            max_symbol_diff = diff
    assert max_symbol_diff < mp.mpf("1e-45")

    barrier_table = []
    prefix_sum = 0.0
    for idx in range(len(primes) - 1):
        p_curr = primes[idx]
        p_next = primes[idx + 1]
        prefix_sum += math.log(p_curr)
        log_next = math.log(p_next)
        assert log_next < 2 * prefix_sum, f"Failed window reach at p={p_curr}"
        barrier_table.append(
            {
                "primes_annihilated": primes[: idx + 1],
                "min_half_width_a_gt": round(prefix_sum, 6),
                "min_window_width_2a_gt": round(2 * prefix_sum, 6),
                "next_uncancelled_prime": p_next,
                "log_next_prime": round(log_next, 6),
                "strictly_active_in_window": bool(log_next < 2 * prefix_sum),
            }
        )

    return {
        "max_pole_annihilation_residual": float(max_pole_residual),
        "max_ns57_symbol_defect_error": float(max_symbol_diff),
        "multi_prime_support_barrier": barrier_table[:6],
    }


def verify_lane3_zero_geometry() -> dict[str, Any]:
    """Verify the Tautological Collapse Theorem for B_p(r) across the original theta kernel, Davenport-Heilbronn, and NS101."""
    mp.mp.dps = 40

    # 1. High-precision check of the pointwise identity for the integrand of B_p(r) and dB_p/dp
    # on the true theta kernel phi(u) = (h''(u) - h(u)/4)/4:
    def theta_h(u: mp.mpf) -> mp.mpf:
        x = mp.exp(2 * u)
        # Theta(x) = 1 + 2 * sum_{n>=1} exp(-pi * n^2 * x)
        s_val = mp.mpf(1)
        n = 1
        while True:
            term = 2 * mp.exp(-mp.pi * (n**2) * x)
            if term < mp.mpf("1e-45"):
                break
            s_val += term
            n += 1
        return mp.exp(u / 2) * s_val

    def phi_orig(u: mp.mpf) -> mp.mpf:
        du = mp.mpf("1e-8")
        h0 = theta_h(u)
        hp = theta_h(u + du)
        hm = theta_h(u - du)
        h2 = (hp - 2 * h0 + hm) / (du**2)
        return (h2 - h0 / 4) / 4

    p_pt = mp.mpf("0.7")
    t_pt = mp.mpf("0.3")
    du = mp.mpf("1e-7")
    u_pt = p_pt + t_pt
    v_pt = p_pt - t_pt

    phi_u = phi_orig(u_pt)
    phi_v = phi_orig(v_pt)
    phi_u_1 = (phi_orig(u_pt + du) - phi_orig(u_pt - du)) / (2 * du)
    phi_v_1 = (phi_orig(v_pt + du) - phi_orig(v_pt - du)) / (2 * du)
    phi_u_2 = (phi_orig(u_pt + du) - 2 * phi_u + phi_orig(u_pt - du)) / (du**2)
    phi_v_2 = (phi_orig(v_pt + du) - 2 * phi_v + phi_orig(v_pt - du)) / (du**2)

    p_plus = phi_u_1 / (2 * phi_u)
    p_minus = phi_v_1 / (2 * phi_v)
    p1_plus = (phi_u_2 * phi_u - phi_u_1**2) / (4 * phi_u**2)
    p1_minus = (phi_v_2 * phi_v - phi_v_1**2) / (4 * phi_v**2)
    k_val = phi_u * phi_v

    collapse_b_err = abs(p_plus * p_minus * k_val - (phi_u_1 * phi_v_1) / 4)
    collapse_db_err = abs(
        2 * k_val * ((p_plus + p_minus) * p_plus * p_minus + p1_plus * p_minus + p_plus * p1_minus)
        - (phi_u_2 * phi_v_1 + phi_u_1 * phi_v_2) / 4
    )
    assert collapse_b_err < mp.mpf("1e-35")
    assert collapse_db_err < mp.mpf("1e-35")

    # 2. Numerical check on Davenport-Heilbronn control at an off-line point near the Spira zero
    z_dh = mp.mpf("0.3085") + mp.j * mp.mpf("85.699")
    h_step = mp.mpf("1e-10")
    f_dh = dh.F(z_dh)
    fp_dh = (dh.F(z_dh + h_step) - dh.F(z_dh - h_step)) / (2 * h_step)
    j_dh = mp.re(fp_dh * mp.conj(f_dh))
    g_dh = -z_dh * f_dh / 2
    gp_dh = -(f_dh + z_dh * fp_dh) / 2
    b_integral_equiv = 4 * mp.re(gp_dh * mp.conj(g_dh))
    x_dh = mp.re(z_dh)
    r_dh = mp.im(z_dh)
    identity_residual_dh = abs(
        (b_integral_equiv - x_dh * abs(f_dh) ** 2) - (x_dh**2 + r_dh**2) * j_dh
    )
    assert identity_residual_dh < mp.mpf("1e-25")

    # 3. Numerical check of the critical-line x -> 0+ limit on NS101 control:
    # 64 * int_0^inf p^2 B_{beta,p}(r) dp - X_beta(r)^2 == r^2 * L_1[X_beta](r) < 0
    # at beta = 4, r_beta = pi / 4.
    beta = mp.mpf(4)
    r_beta = mp.pi / beta
    b_beta = 3 + 2 * mp.cosh(beta / 2)

    def x_orig(r_val: mp.mpf) -> mp.mpf:
        s_val = mp.mpf("0.5") + mp.j * r_val
        return mp.re(
            s_val
            * (s_val - 1)
            * mp.power(mp.pi, -s_val / 2)
            * mp.gamma(s_val / 2)
            * mp.zeta(s_val)
            / 4
        )

    def x_beta_fn(r_val: mp.mpf) -> mp.mpf:
        q_val = 3 + 2 * mp.cos(beta * r_val)
        return q_val * x_orig(r_val) / b_beta

    eps_r = mp.mpf("1e-8")
    xb0 = x_beta_fn(r_beta)
    xb_p = x_beta_fn(r_beta + eps_r)
    xb_m = x_beta_fn(r_beta - eps_r)
    xb1 = (xb_p - xb_m) / (2 * eps_r)
    xb2 = (xb_p - 2 * xb0 + xb_m) / (eps_r**2)
    l1_x_beta = xb1**2 - xb0 * xb2

    hb0 = (r_beta / 2) * xb0
    hb1 = xb0 / 2 + (r_beta / 2) * xb1
    hb2 = xb1 + (r_beta / 2) * xb2
    b_moment_critical = 4 * (hb1**2 - hb0 * hb2)
    crit_limit_diff = abs((b_moment_critical - xb0**2) - (r_beta**2) * l1_x_beta)
    assert crit_limit_diff < mp.mpf("1e-30")
    assert l1_x_beta < 0, f"Expected negative L1 on NS101 control, got {l1_x_beta}"

    return {
        "pointwise_Bp_integrand_collapse_error": float(collapse_b_err),
        "pointwise_dBp_dp_collapse_error": float(collapse_db_err),
        "dh_sample_point": "0.3085+85.699i",
        "dh_strip_identity_residual": float(identity_residual_dh),
        "ns101_beta": float(beta),
        "ns101_r_beta": float(r_beta),
        "ns101_L1_X_beta": float(l1_x_beta),
        "ns101_64_int_p2_Bp_minus_X2": float(b_moment_critical - xb0**2),
        "ns101_critical_limit_identity_residual": float(crit_limit_diff),
        "ns101_violates_Bp_positivity": bool((b_moment_critical - xb0**2) < 0),
    }


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    results = {
        "date": "2026-10-14",
        "baseline_commit": "2d5638ed3b56ab2375162bb072f4866ad5bdfe6d",
        "wall_check": {
            "classification": "Same open gap",
            "narrow_closures": [
                "Known wall for linearized two-shift moment B_p(r) in 01-jacobi-transfer.md (collapses identically to (1/4) int phi'(p+t)phi'(p-t)cos(2rt)dt without using the Jacobi ODE)",
                "Known wall for pure interior finite-prime-product annihilation L_P : V_{a-ell_P} -> V_a removing all active window primes (blocked by the Chebyshev/Bertrand support barrier ell_P < a < 2a - ell_P)",
            ],
            "closest_results": [
                "NS51",
                "NS55",
                "NS57",
                "NS58",
                "NS61",
                "NS74",
                "NS78",
                "NS80",
                "NS83",
                "NS87",
                "NS100",
                "NS101",
                "PR76",
                "PR78",
                "PR80",
                "PR81",
            ],
        },
        "lane1_nb_coeff": verify_lane1_nb_coeff(),
        "lane2_kernel_api": verify_lane2_kernel_api(),
        "lane3_zero_geometry": verify_lane3_zero_geometry(),
    }
    out_path = out_dir / "verification.json"
    out_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
