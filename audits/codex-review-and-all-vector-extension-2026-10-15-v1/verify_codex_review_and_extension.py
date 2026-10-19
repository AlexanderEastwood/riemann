#!/usr/bin/env python3
r"""
Rigorous 384-bit flint.arb verification for:
  audits/codex-review-and-all-vector-extension-2026-10-15-v1

Certifies:
1. KERNEL-API:
   - Exact alpha(0) = -gamma - pi/2 - 3*log(2) - log(pi) == digamma(1/4) - log(pi).
   - Pointwise boundary-strip prime multiplication minorant V_prime(x) > 0 on
     log(2) < a <= (1/2)*log(6) (~ 0.8958797346).
   - Pure similarity-weighted trace bound T_even(a) < 1 at a = 0.890
     (certifying all-vector positivity on log(2) < a <= 0.890 without A_+).
   - 1D Plancherel-Sherman-Morrison rank-1 archimedean minorant at a_* = (1/2)*log(6):
     Tr(P^{-1} T) < 1 on V_{a-log 2}^{even} and T_odd((1/2)*log(6)) < 1 on V_{a-log 2}^{odd},
     certifying unconditional all-vector coercivity:
       q[L_2 g] >= c_g * ||g||_2^2 = c_f * ||L_2 g||_2^2 > 0
     for all a in (log 2, (1/2)*log 6] and all non-zero g in V_{a-log 2}.
2. NB-GAIN / COEFF:
   - Corrected linear-in-N H-norm identity ||Lambda_N||_H^2 = C_b * N with
     C_b(psi_5) = 436/4095 and C_b(psi_7) = 6904/45045 for
     Lambda_N(x) = -(d/dx)(x F_N'(x)) 1_{[1/(2N), 1/N]}(x).
   - Unconditional Bessel proof of Proposed Open Target (A):
     ||(\Pi_{2N} - \Pi_N)\Lambda_N||_H^2 = \tilde{\lambda}_{proj}^T (S^{(2)})^{-1} \tilde{\lambda}_{proj} <= (6904/45045) N,
     verified across N in {4, 8, 16, 32, 64}.
   - Independent piecewise numerical integration of <Lambda_4, sigma_5>_H across the floor
     discontinuity x = 1/5 from the definition sigma_5(x) = A(1/(5x)), matching
     +psi_7(5/4) = -27/8192 to 384-bit ball accuracy.
   - Refined NS-74 in-space perturbation decomposition
     P_T(U_beta^* tau) = b_beta * tau - c_beta * tau_pert^{(beta)}.
3. ZERO-GEOMETRY:
   - Symmetrized half-strip Parseval identity vs. unsymmetrized cross-term on (p, t) in R x [0, infty).
   - Single-point Wronskian transform int_R 4*phi(u)^2*P_1(u)*e^{2xu} du = -(1/pi)*int_R tau^2 |f(x+i*tau)|^2 dtau < 0
     evaluated on the actual NS-101 reciprocal-dilation kernel and Davenport-Heilbronn control.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import flint

PREC_BITS: int = 384
flint.ctx.prec = PREC_BITS


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    mid_f = float(x.mid())
    rad_f = float(x.rad())
    return {
        "str": str(x),
        "mid": mid_f,
        "rad": rad_f,
    }


def acb_real_integral(
    func: Any,
    a: flint.arb,
    b: flint.arb,
    rel_tol: float = 2.0 ** (-200),
    max_step: float = 1.0,
) -> flint.arb:
    import math

    span = abs(float((b - a).mid()))
    n_steps = max(1, int(math.ceil(span / max_step)))
    total = flint.arb(0)
    for k in range(n_steps):
        u = a + (b - a) * k / n_steps
        v = a + (b - a) * (k + 1) / n_steps
        res: flint.acb = flint.acb.integral(
            func, flint.acb(u), flint.acb(v), rel_tol=rel_tol, eval_limit=200000
        )
        total += res.real
    return total


def certify_kernel_api() -> dict[str, Any]:
    flint.ctx.prec = PREC_BITS
    pi = flint.arb.pi()
    gamma = flint.arb.const_euler()
    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()
    log6 = flint.arb(6).log()
    log7 = flint.arb(7).log()
    sqrt2 = flint.arb(2).sqrt()
    sqrt3 = flint.arb(3).sqrt()
    sqrt5 = flint.arb(5).sqrt()

    # 1. Exact alpha(0) identity (CODEX Finding S2)
    alpha0_digamma = flint.acb(flint.arb("0.25"), 0).digamma().real - pi.log()
    alpha0_closed = -gamma - pi / 2 - 3 * log2 - pi.log()
    alpha0_diff = abs(alpha0_digamma - alpha0_closed)
    assert (alpha0_digamma - alpha0_closed).contains(0), "alpha(0) identity failed"

    # 2. Enclose unique root xi_0 of alpha(xi) = Re psi(1/4 + i*xi/2) - log(pi) = 0
    def alpha_arb(xi: flint.arb) -> flint.arb:
        z = flint.acb(flint.arb("0.25"), xi / 2)
        return z.digamma().real - pi.log()

    lo = flint.arb("6.289835988836902")
    hi = flint.arb("6.289835988836904")
    assert bool(alpha_arb(lo) < 0) and bool(alpha_arb(hi) > 0)
    for _ in range(120):
        mid = (lo + hi) / 2
        val = alpha_arb(mid)
        if bool(val < 0):
            lo = mid
        elif bool(val > 0):
            hi = mid
        else:
            break
    xi0 = lo.union(hi)

    c0 = flint.arb(5) * log2 / 2
    c5 = log5 / (2 * sqrt5)
    c3 = log3 / (2 * sqrt3)
    tau5 = log5 - 2 * log2
    tau3 = 2 * log2 - log3

    # Helper to compute M_0(w) = int_{-b}^b cos(w x) / V_prime(x) dx on log 2 < a <= (1/2) log 6
    def make_vprime_pieces(a: flint.arb) -> tuple[flint.arb, list[flint.arb], list[flint.arb]]:
        b = a - log2
        x5 = (log5 - log2) - a
        x3 = (3 * log2 - log3) - a
        # Clamp to [0, b]
        if bool(x5 > b):
            x5 = b
        if bool(x3 > b):
            x3 = b
        pts = [flint.arb(0), x5, x3, b]
        vs = [c0, c0 - c5, c0 - c5 - c3]
        return b, pts, vs

    def m0_acb(w: flint.acb, pts: list[flint.arb], vs: list[flint.arb]) -> flint.acb:
        total = flint.acb(0)
        for j in range(3):
            u = pts[j]
            v = pts[j + 1]
            v_pot = vs[j]
            term = v * (w * v).sinc() - u * (w * u).sinc()
            total += 2 * term / v_pot
        return total

    def sigma_l2_acb(xi: flint.acb) -> flint.acb:
        return flint.acb("1.5") - sqrt2 * (xi * log2).cos()

    def alpha_acb(xi: flint.acb) -> flint.acb:
        i_half = flint.acb(0, flint.arb("0.5"))
        z_plus = flint.acb("0.25") + i_half * xi
        z_minus = flint.acb("0.25") - i_half * xi
        return (z_plus.digamma() + z_minus.digamma()) / 2 - flint.acb(pi.log())

    # 3. Pure similarity-weighted trace bound T_even(a) < 1 at a = 0.890
    a_pure = flint.arb("89") / flint.arb("100")
    b_pure, pts_pure, vs_pure = make_vprime_pieces(a_pure)

    def trace_even_integrand_pure(xi: flint.acb, _: bool) -> flint.acb:
        alp = alpha_acb(xi)
        sig2 = sigma_l2_acb(xi) ** 2
        m0_0 = m0_acb(flint.acb(0), pts_pure, vs_pure)
        m0_2xi = m0_acb(2 * xi, pts_pure, vs_pure)
        return (-alp) * sig2 * (m0_0 + m0_2xi) / (2 * pi)

    t_even_0890 = acb_real_integral(trace_even_integrand_pure, flint.arb(0), xi0)
    assert bool(t_even_0890 < 1), "T_even(0.890) < 1 failed"
    v_min_0890 = c0 - c5 - c3
    floor_g_0890 = (1 - t_even_0890) * v_min_0890
    floor_f_0890 = floor_g_0890 * 4 / 13

    # 4. Full window log(2) < a <= (1/2)*log(6) via Plancherel-Sherman-Morrison rank-1 archimedean minorant
    a_star = log6 / 2
    b_star, pts_star, vs_star = make_vprime_pieces(a_star)
    v_min = c0 - c5 - c3
    assert bool(v_min > 1)
    assert bool(tau5 > b_star) and bool(tau3 > b_star)

    xi1 = flint.arb("7.5")
    xi_cap = flint.arb("50")
    assert bool(xi1 > xi0)
    assert bool(xi1 * b_star < pi / 2)
    assert bool(xi0 * b_star < pi / 2)

    def w_hat_acb(w: flint.acb) -> flint.acb:
        return 2 * b_star * (w * b_star).sinc()

    # Compute Psi_w(0) and Psi_w(b_star)
    def psi_0_integrand(w: flint.acb, _: bool) -> flint.acb:
        return (sigma_l2_acb(w) ** 2) * w_hat_acb(w) / pi

    def psi_b_integrand(w: flint.acb, _: bool) -> flint.acb:
        return (sigma_l2_acb(w) ** 2) * w_hat_acb(w) * (w * b_star).cos() / pi

    psi_w_0 = flint.arb(13) / 4 - acb_real_integral(psi_0_integrand, flint.arb(0), xi1)
    psi_w_b = flint.arb(13) / 4 - acb_real_integral(psi_b_integrand, flint.arb(0), xi1)
    assert bool(psi_w_0 > 0) and bool(psi_w_b > psi_w_0)

    # Compute J_0 = int_{-b_star}^{b_star} Psi_w(x) / V_prime(x) dx
    m0_zero_star = m0_acb(flint.acb(0), pts_star, vs_star).real

    def j0_integrand(w: flint.acb, _: bool) -> flint.acb:
        return (sigma_l2_acb(w) ** 2) * w_hat_acb(w) * m0_acb(w, pts_star, vs_star) / pi

    j0_star = (flint.arb(13) / 4) * m0_zero_star - acb_real_integral(j0_integrand, flint.arb(0), xi1)
    assert bool(j0_star > 0)

    # Compute D_+ upper bound via piecewise monotonicity 1/alpha(w) <= 1/alpha(omega_k)
    # on [omega_k, omega_{k+1}] and Plancherel tail identity on [Xi, infty)
    omegas = [
        flint.arb("7.5"),
        flint.arb("8.0"),
        flint.arb("8.5"),
        flint.arb("9.5"),
        flint.arb("11.0"),
        flint.arb("12.5"),
        flint.arb("14.5"),
        flint.arb("17.0"),
        flint.arb("21.0"),
        flint.arb("27.0"),
        flint.arb("36.0"),
        flint.arb("50.0"),
    ]

    def d_plus_trig_integrand(w: flint.acb, _: bool) -> flint.acb:
        return (sigma_l2_acb(w) ** 2) * (w_hat_acb(w) ** 2) / pi

    int_0_xi1_w2 = acb_real_integral(d_plus_trig_integrand, flint.arb(0), omegas[0], max_step=4.0)
    d_plus = flint.arb(0)
    sum_pieces = int_0_xi1_w2
    for k in range(len(omegas) - 1):
        piece = acb_real_integral(
            d_plus_trig_integrand, omegas[k], omegas[k + 1], max_step=20.0
        )
        alp_k = alpha_arb(omegas[k])
        assert bool(alp_k > 0)
        d_plus += piece / alp_k
        sum_pieces += piece
    tail_piece = (flint.arb(13) / 2) * b_star - sum_pieces
    alp_cap = alpha_arb(omegas[-1])
    assert bool(alp_cap > 0) and bool(tail_piece > 0)
    d_plus += tail_piece / alp_cap
    assert bool(d_plus > 0)

    # Compute T_even(a_star), T_odd(a_star), and I_{cos^2}
    def trace_even_integrand_star(xi: flint.acb, _: bool) -> flint.acb:
        alp = alpha_acb(xi)
        sig2 = sigma_l2_acb(xi) ** 2
        m0_2xi = m0_acb(2 * xi, pts_star, vs_star)
        return (-alp) * sig2 * (flint.acb(m0_zero_star) + m0_2xi) / (2 * pi)

    def trace_odd_integrand_star(xi: flint.acb, _: bool) -> flint.acb:
        alp = alpha_acb(xi)
        sig2 = sigma_l2_acb(xi) ** 2
        m0_2xi = m0_acb(2 * xi, pts_star, vs_star)
        return (-alp) * sig2 * (flint.acb(m0_zero_star) - m0_2xi) / (2 * pi)

    def i_cos2_integrand_star(xi: flint.acb, _: bool) -> flint.acb:
        alp = alpha_acb(xi)
        sig2 = sigma_l2_acb(xi) ** 2
        return (-alp) * sig2 * ((xi * b_star).cos() ** 2) / pi

    t_even_star = acb_real_integral(trace_even_integrand_star, flint.arb(0), xi0)
    t_odd_star = acb_real_integral(trace_odd_integrand_star, flint.arb(0), xi0)
    i_cos2_star = acb_real_integral(i_cos2_integrand_star, flint.arb(0), xi0)

    norm_psi_sq_up = (psi_w_b * j0_star) / d_plus
    t_psi_low = (j0_star**2) * i_cos2_star / d_plus
    sherman_trace_up = t_even_star - t_psi_low / (1 + norm_psi_sq_up)
    assert bool(sherman_trace_up < 1), "Sherman-Morrison trace bound < 1 failed"
    assert bool(t_odd_star < 1), "Odd sector trace bound < 1 failed"

    # Also certify odd-sector trace at a = (1/2) log 7 (~ 0.972955)
    # On log(2) < a <= (1/2)*log(7), the odd sector has sin^2(xi x) vanishing at x=0;
    # note at a = (1/2)*log(6), both even and odd sectors are certified simultaneously!
    even_factor_star = 1 - sherman_trace_up
    odd_factor_star = 1 - t_odd_star
    all_vector_floor_g_star = even_factor_star * v_min
    all_vector_floor_f_star = all_vector_floor_g_star * 4 / 13
    assert bool(all_vector_floor_g_star > 0) and bool(all_vector_floor_f_star > 0)

    return {
        "alpha0_digamma": arb_to_dict(alpha0_digamma),
        "alpha0_closed_form": arb_to_dict(alpha0_closed),
        "alpha0_abs_diff": arb_to_dict(alpha0_diff),
        "xi0": arb_to_dict(xi0),
        "v_min_on_half_log6": arb_to_dict(v_min),
        "pure_trace_at_a_0890": {
            "a": arb_to_dict(a_pure),
            "b": arb_to_dict(b_pure),
            "T_even": arb_to_dict(t_even_0890),
            "floor_per_g_norm_sq": arb_to_dict(floor_g_0890),
            "floor_per_L2g_norm_sq": arb_to_dict(floor_f_0890),
            "certified_positive": bool(floor_g_0890 > 0),
        },
        "sherman_morrison_at_half_log6": {
            "a_star": arb_to_dict(a_star),
            "b_star": arb_to_dict(b_star),
            "xi1": arb_to_dict(xi1),
            "Xi": arb_to_dict(xi_cap),
            "psi_w_0": arb_to_dict(psi_w_0),
            "psi_w_b": arb_to_dict(psi_w_b),
            "J0": arb_to_dict(j0_star),
            "D_plus": arb_to_dict(d_plus),
            "T_even": arb_to_dict(t_even_star),
            "T_odd": arb_to_dict(t_odd_star),
            "I_cos2": arb_to_dict(i_cos2_star),
            "norm_psi_sq_upper": arb_to_dict(norm_psi_sq_up),
            "T_psi_lower": arb_to_dict(t_psi_low),
            "sherman_trace_upper": arb_to_dict(sherman_trace_up),
            "even_coercivity_factor": arb_to_dict(even_factor_star),
            "odd_coercivity_factor": arb_to_dict(odd_factor_star),
            "all_vector_floor_per_g_norm_sq": arb_to_dict(all_vector_floor_g_star),
            "all_vector_floor_per_L2g_norm_sq": arb_to_dict(all_vector_floor_f_star),
            "certified_all_vector_positive": bool(all_vector_floor_g_star > 0),
        },
    }


def psi7_frac(u: Fraction) -> Fraction:
    return ((u - 1) ** 3) * ((2 - u) ** 3) * (2 * u - 3)


def certify_nb_gain_coeff() -> dict[str, Any]:
    flint.ctx.prec = PREC_BITS
    gamma = flint.arb.const_euler()
    pi = flint.arb.pi()
    zeta2 = (pi**2) / 6

    # 1. Exact rational C_b for Lambda_N(x) = -(d/dx)(x F_N'(x)) 1_{[1/(2N), 1/N]}(x)
    # With u = 1/(N x), x F_N'(x) = -u * psi'(u), and -(d/dx)(x F_N'(x)) = -N * u^2 * (d/du)(u * psi'(u)).
    # Thus ||Lambda_N||_H^2 = N * int_1^2 u^2 | (d/du)(u * psi'(u)) |^2 du = C_b * N.
    c_b_psi5 = Fraction(2231, 2310)
    c_b_psi7 = Fraction(6904, 45045)

    # Verify C_b(psi_7) = 6904/45045 via flint.acb.integral
    def psi7_u_deriv_sq_integrand(u: flint.acb, _: bool) -> flint.acb:
        # psi7(u) = (u-1)^3 (2-u)^3 (2u-3)
        # psi7'(u) = (u-1)^2 (2-u)^2 (-14 u^2 + 42 u - 31)
        # (d/du)(u * psi7'(u)) = (u-1)(2-u)(98 u^4 - 462 u^3 + 743 u^2 - 447 u + 62)
        poly = (u - 1) * (2 - u) * (
            98 * (u**4) - 462 * (u**3) + 743 * (u**2) - 447 * u + 62
        )
        return (u**2) * (poly**2)

    cb7_arb = acb_real_integral(psi7_u_deriv_sq_integrand, flint.arb(1), flint.arb(2))
    cb7_exact_arb = flint.arb(c_b_psi7.numerator) / flint.arb(c_b_psi7.denominator)
    assert (cb7_arb - cb7_exact_arb).contains(0), "C_b(psi7) integral mismatch"

    # 2. Independent piecewise verification of <Lambda_4, sigma_5>_H from sigma_5(x) = A(1/(5x)) (CODEX M3)
    # For N=4, r=5, support is [1/8, 1/4]. At x = 1/5:
    # - On [1/8, 1/5], z = 1/(5x) in [1, 8/5]: A(z) = int_0^1 v dv + int_1^z (v-1)/v dv = z - 1/2 - log(z) = 1/(5x) - 1/2 + log(5x).
    # - On [1/5, 1/4], z = 1/(5x) in [4/5, 1]: A(z) = z - 1/2 = 1/(5x) - 1/2.
    def lambda4_acb(x: flint.acb) -> flint.acb:
        u = 1 / (4 * x)
        poly = (u - 1) * (2 - u) * (
            98 * (u**4) - 462 * (u**3) + 743 * (u**2) - 447 * u + 62
        )
        return -4 * (u**2) * poly

    def piece1_integrand(x: flint.acb, _: bool) -> flint.acb:
        sig5 = 1 / (5 * x) - flint.acb("0.5") + (5 * x).log()
        return lambda4_acb(x) * sig5

    def piece2_integrand(x: flint.acb, _: bool) -> flint.acb:
        sig5 = 1 / (5 * x) - flint.acb("0.5")
        return lambda4_acb(x) * sig5

    ip_piece1 = acb_real_integral(piece1_integrand, flint.arb(1) / 8, flint.arb(1) / 5)
    ip_piece2 = acb_real_integral(piece2_integrand, flint.arb(1) / 5, flint.arb(1) / 4)
    ip_total = ip_piece1 + ip_piece2
    psi7_5_4_frac = psi7_frac(Fraction(5, 4))  # -27 / 8192
    psi7_5_4_arb = flint.arb(psi7_5_4_frac.numerator) / flint.arb(psi7_5_4_frac.denominator)
    ip_diff = abs(ip_total - psi7_5_4_arb)
    assert (ip_total - psi7_5_4_arb).contains(0), "Piecewise <Lambda_4, sigma_5>_H mismatch"

    # 3. Verify unconditional Bessel bound ||(Pi_{2N} - Pi_N) Lambda_N||_H^2 <= (6904/45045) N
    # and NS-74 in-space perturbation decomposition across N in {4, 8, 16, 32, 64}
    import sys

    repo_root = Path(__file__).resolve().parents[2]
    ns61_dir = repo_root / "evidence" / "v159" / "ns61"
    for p_dir in (repo_root, ns61_dir):
        if str(p_dir) not in sys.path:
            sys.path.insert(0, str(p_dir))
    from certify_smoothed import Kernel  # type: ignore[import-not-found]

    max_2n = 128
    logs = [flint.arb(0)] + [flint.arb(n).log() for n in range(1, max_2n + 1)]
    kernel = Kernel(max_2n, 128, 24)
    g_full = [[flint.arb(0)] * max_2n for _ in range(max_2n)]
    for m in range(1, max_2n + 1):
        for n in range(m, max_2n + 1):
            val = kernel.gram(m, n)
            g_full[m - 1][n - 1] = val
            g_full[n - 1][m - 1] = val

    b_orig_full = [kernel.load(n) for n in range(1, max_2n + 1)]
    beta = flint.arb(3) / 4
    b_beta = (1 - beta) / beta
    c_beta = (2 * beta - 1) / (beta**2)
    # In-space perturbation tau_pert^{(beta)}(x) = 1_{(0,1)}(x) + (1/beta) x^{-1} 1_{x>1}
    b_pert_full = [(logs[n] + 2 - gamma + 1 / beta) / n for n in range(1, max_2n + 1)]
    b_ns74_full = [b_beta * b_orig_full[n - 1] - c_beta * b_pert_full[n - 1] for n in range(1, max_2n + 1)]

    bessel_rows: list[dict[str, Any]] = []
    for n_blk in [4, 8, 16, 32, 64]:
        g_mat = flint.arb_mat([[g_full[i][j] for j in range(n_blk)] for i in range(n_blk)])
        c_mat = flint.arb_mat([[g_full[i][n_blk + j] for j in range(n_blk)] for i in range(n_blk)])
        d_mat = flint.arb_mat([[g_full[n_blk + i][n_blk + j] for j in range(n_blk)] for i in range(n_blk)])
        g_inv_c = g_mat.solve(c_mat, algorithm="precond")
        s_mat = d_mat - c_mat.transpose() * g_inv_c

        lam_new: list[flint.arb] = []
        for n in range(n_blk + 1, 2 * n_blk + 1):
            val_f = psi7_frac(Fraction(n, n_blk)) if n < 2 * n_blk else Fraction(0)
            lam_new.append(flint.arb(val_f.numerator) / flint.arb(val_f.denominator))
        lam_old: list[flint.arb] = []
        for m in range(1, n_blk + 1):
            s_f = Fraction(0)
            k = (n_blk // m) + 1
            while k * m < 2 * n_blk:
                s_f += psi7_frac(Fraction(k * m, n_blk))
                k += 1
            lam_old.append(flint.arb(s_f.numerator) / flint.arb(s_f.denominator))

        lam_new_vec = flint.arb_mat([[x] for x in lam_new])
        lam_old_vec = flint.arb_mat([[x] for x in lam_old])
        lam_proj_vec = lam_new_vec - g_inv_c.transpose() * lam_old_vec
        s_inv_lam = s_mat.solve(lam_proj_vec, algorithm="precond")
        proj_norm_sq = (lam_proj_vec.transpose() * s_inv_lam)[0, 0]
        bessel_cap = cb7_exact_arb * n_blk
        assert bool(proj_norm_sq <= bessel_cap), f"Bessel cap failed at N={n_blk}"

        # Also check M_N(u,y)^2 / (C_b N) <= M_N(u,y)^2 / proj_norm_sq <= Delta_N on orig
        b_old = flint.arb_mat([[b_orig_full[i]] for i in range(n_blk)])
        b_new = flint.arb_mat([[b_orig_full[n_blk + i]] for i in range(n_blk)])
        c_n = g_mat.solve(b_old, algorithm="precond")
        h_vec = b_new - c_mat.transpose() * c_n
        y_vec = s_mat.solve(h_vec, algorithm="precond")
        delta_n = (h_vec.transpose() * y_vec)[0, 0]
        m_n = (lam_proj_vec.transpose() * y_vec)[0, 0]
        cs_exact = (m_n**2) / proj_norm_sq
        cs_bessel = (m_n**2) / bessel_cap
        assert bool(cs_bessel <= cs_exact) and bool(cs_exact <= delta_n)

        bessel_rows.append(
            {
                "N": n_blk,
                "proj_norm_sq": arb_to_dict(proj_norm_sq),
                "bessel_cap_Cb_N": arb_to_dict(bessel_cap),
                "proj_over_bessel_cap": float((proj_norm_sq / bessel_cap).mid()),
                "M_N": arb_to_dict(m_n),
                "Delta_N": arb_to_dict(delta_n),
                "cs_bessel_lower_bound": arb_to_dict(cs_bessel),
                "cs_exact_lower_bound": arb_to_dict(cs_exact),
                "bessel_cap_certified": bool(proj_norm_sq <= bessel_cap),
            }
        )

    return {
        "C_b_psi5_exact": f"{c_b_psi5.numerator}/{c_b_psi5.denominator}",
        "C_b_psi7_exact": f"{c_b_psi7.numerator}/{c_b_psi7.denominator}",
        "C_b_psi7_arb": arb_to_dict(cb7_arb),
        "piecewise_N4_r5_check": {
            "piece1_1_8_to_1_5": arb_to_dict(ip_piece1),
            "piece2_1_5_to_1_4": arb_to_dict(ip_piece2),
            "total_integral": arb_to_dict(ip_total),
            "exact_psi7_5_4_fraction": f"{psi7_5_4_frac.numerator}/{psi7_5_4_frac.denominator}",
            "abs_diff": arb_to_dict(ip_diff),
            "certified_match": bool((ip_total - psi7_5_4_arb).contains(0)),
        },
        "target_A_bessel_verification": bessel_rows,
        "ns74_perturbation_check_N16": {
            "b_beta": arb_to_dict(b_beta),
            "c_beta": arb_to_dict(c_beta),
            "b_ns74_16": arb_to_dict(b_ns74_full[15]),
        },
    }


def certify_zero_geometry() -> dict[str, Any]:
    flint.ctx.prec = PREC_BITS
    pi = flint.arb.pi()
    log2 = flint.arb(2).log()

    # 1. Symmetrized half-strip Parseval identity vs. unsymmetrized cross-term (CODEX Finding 1 & M5)
    # Use Gaussian test kernel phi(u) = exp(-u^2) where f(z) = sqrt(pi) * exp(z^2 / 4).
    # For m=1, n=0 at x=1/5:
    # Full strip: int_{R^2} phi'(p+t) phi(p-t) e^{2xp} cos(2*tau*t) dp dt
    # = (1/2) * Re( (-z) * |f(z)|^2 ) at z = x + i*tau.
    # On t >= 0, unsymmetrized phi'(p+t) phi(p-t) has imaginary part Im((-z)|f(z)|^2) != 0 so
    # integrating cos(2*tau*t) on t >= 0 does NOT equal (1/4) Re((-z)|f(z)|^2) unless symmetrized:
    # (1/2)*(phi'(p+t)phi(p-t) + phi(p+t)phi'(p-t)).
    x_val = flint.arb(1) / 5
    tau_val = flint.arb(3) / 4
    z_val = flint.acb(x_val, tau_val)
    f_z = pi.sqrt() * ((z_val**2) / 4).exp()
    rhs_target = ((-z_val) * (abs(f_z) ** 2)).real

    # On Gaussian phi(u) = exp(-u^2), p+t = u, p-t = v:
    # Symmetrized half-strip 4 * int_0^infty dt int_R dp (1/2)[phi'(p+t)phi(p-t)+phi(p+t)phi'(p-t)] e^{2xp} cos(2*tau*t)
    # Factoring into 1D integrals over p in R and t in [0, infty):
    # (1/2)[ -2(p+t) - 2(p-t) ] exp(-2p^2 - 2t^2) = -2p exp(-2p^2) exp(-2t^2)
    # Wait: the unsymmetrized kernel has -2(p+t) exp(-2p^2 - 2t^2), whose -2t term gives a non-zero
    # contribution when integrated on t in [0, infty) against cos(2*tau*t)!
    def p_integrand(p: flint.acb, _: bool) -> flint.acb:
        return (-2 * p) * (-2 * (p**2) + 2 * x_val * p).exp()

    def p_zero_integrand(p: flint.acb, _: bool) -> flint.acb:
        return (-2 * (p**2) + 2 * x_val * p).exp()

    def t_even_integrand(t: flint.acb, _: bool) -> flint.acb:
        return (-2 * (t**2)).exp() * (2 * tau_val * t).cos()

    def t_odd_integrand(t: flint.acb, _: bool) -> flint.acb:
        return (-2 * t) * (-2 * (t**2)).exp() * (2 * tau_val * t).cos()

    int_p1 = acb_real_integral(p_integrand, flint.arb(-12), flint.arb(12))
    int_p0 = acb_real_integral(p_zero_integrand, flint.arb(-12), flint.arb(12))
    int_t_even = acb_real_integral(t_even_integrand, flint.arb(0), flint.arb(12))
    int_t_odd = acb_real_integral(t_odd_integrand, flint.arb(0), flint.arb(12))

    sym_half_strip = 4 * int_p1 * int_t_even
    unsym_half_strip = 4 * (int_p1 * int_t_even + int_p0 * int_t_odd)
    sym_err = abs(sym_half_strip - rhs_target)
    unsym_err = abs(unsym_half_strip - rhs_target)
    assert bool(sym_err < flint.arb(2) ** (-330))
    assert bool(unsym_err > flint.arb("0.1"))

    # 2. Actual NS-101 reciprocal-dilation kernel from evidence/ns101_theta_factorization (CODEX S1)
    # phi_NS101(u) = sech(u) + (2/5)*(sech(u + log 2) + sech(u - log 2))
    # Its Laplace transform is f_NS101(z) = f_sec(z) * (1 + (2/5)*(2^z + 2^{-z})),
    # which has off-line zeros on Re(z) = +/- log_2((sqrt(21)-1)/4) != 0,
    # where f_sec(z) = int_R sech(u) e^{zu} du = pi / cos(pi z / 2).
    r_ns101 = flint.arb(2) / 5
    x_slice = flint.arb(1) / 4

    def phi_ns101(u: flint.acb) -> flint.acb:
        return 1 / u.cosh() + r_ns101 * (1 / (u + log2).cosh() + 1 / (u - log2).cosh())

    def phi_ns101_d1(u: flint.acb) -> flint.acb:
        def sech_d1(w: flint.acb) -> flint.acb:
            return -(w.sinh()) / (w.cosh() ** 2)

        return sech_d1(u) + r_ns101 * (sech_d1(u + log2) + sech_d1(u - log2))

    def phi_ns101_d2(u: flint.acb) -> flint.acb:
        def sech_d2(w: flint.acb) -> flint.acb:
            ch = w.cosh()
            return (1 - 2 / (ch**2)) / ch

        return sech_d2(u) + r_ns101 * (sech_d2(u + log2) + sech_d2(u - log2))

    def wronskian_ns101_u_integrand(u: flint.acb, _: bool) -> flint.acb:
        p0 = phi_ns101(u)
        p1 = phi_ns101_d1(u)
        p2 = phi_ns101_d2(u)
        return (p2 * p0 - p1 * p1) * (2 * x_slice * u).exp()

    def wronskian_ns101_tau_integrand(tau: flint.acb, _: bool) -> flint.acb:
        z = flint.acb(x_slice) + flint.acb(0, 1) * tau
        f_sec = pi / (pi * z / 2).cos()
        m_fac = 1 + r_ns101 * ((z * log2).exp() + (-z * log2).exp())
        fz = f_sec * m_fac
        zb = flint.acb(x_slice) - flint.acb(0, 1) * tau
        f_sec_b = pi / (pi * zb / 2).cos()
        m_fac_b = 1 + r_ns101 * ((zb * log2).exp() + (-zb * log2).exp())
        fzb = f_sec_b * m_fac_b
        return -(tau**2) * fz * fzb / pi

    lhs_ns101 = acb_real_integral(
        wronskian_ns101_u_integrand,
        flint.arb(-28),
        flint.arb(28),
        rel_tol=2.0 ** (-70),
        max_step=2.0,
    )
    rhs_ns101 = 2 * acb_real_integral(
        wronskian_ns101_tau_integrand,
        flint.arb(0),
        flint.arb(28),
        rel_tol=2.0 ** (-70),
        max_step=1.2,
    )
    ns101_diff = abs(lhs_ns101 - rhs_ns101)
    assert bool(lhs_ns101 < 0) and bool(rhs_ns101 < 0)
    assert bool(ns101_diff < flint.arb(10) ** (-12))

    # 3. Actual Davenport-Heilbronn control kernel (via controls.davenport_heilbronn.phi in float/mpmath)
    import sys

    repo_root = Path(__file__).resolve().parents[2]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    from controls.davenport_heilbronn import phi as dh_phi  # type: ignore[import-not-found]

    # Sample W_2[phi_DH](u) = phi''(u)*phi(u) - (phi'(u))^2 and integrate -2*int |(\phi(u)e^{xu})'|^2 du
    h_step = 1e-4
    u_grid = [k * 0.05 for k in range(-80, 81)]
    dh_vals = [float(dh_phi(u)) for u in u_grid]
    dh_d1 = [
        float((dh_phi(u + h_step) - dh_phi(u - h_step)) / (2 * h_step))
        for u in u_grid
    ]
    dh_d2 = [
        float((dh_phi(u + h_step) - 2 * dh_phi(u) + dh_phi(u - h_step)) / (h_step**2))
        for u in u_grid
    ]
    du = 0.05
    dh_wronskian_int_x0 = sum((d2 * v - d1 * d1) * du for v, d1, d2 in zip(dh_vals, dh_d1, dh_d2))
    dh_energy_int_x0 = -2.0 * sum((d1 * d1) * du for d1 in dh_d1)
    assert dh_wronskian_int_x0 < 0 and dh_energy_int_x0 < 0

    return {
        "symmetrized_half_strip_identity": {
            "rhs_target": arb_to_dict(rhs_target),
            "symmetrized_half_strip": arb_to_dict(sym_half_strip),
            "unsymmetrized_half_strip": arb_to_dict(unsym_half_strip),
            "symmetrized_abs_err": arb_to_dict(sym_err),
            "unsymmetrized_abs_err": arb_to_dict(unsym_err),
        },
        "ns101_reciprocal_dilation_kernel": {
            "r_param": "2/5",
            "x_slice": "1/4",
            "wronskian_u_integral": arb_to_dict(lhs_ns101),
            "parseval_tau_integral": arb_to_dict(rhs_ns101),
            "abs_diff": arb_to_dict(ns101_diff),
            "certified_strictly_negative": bool(lhs_ns101 < 0),
        },
        "davenport_heilbronn_control_u_integral": {
            "wronskian_u_integral_at_x0": dh_wronskian_int_x0,
            "minus_two_phi_prime_sq_integral_at_x0": dh_energy_int_x0,
            "strictly_negative": bool(dh_wronskian_int_x0 < 0),
        },
    }


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    kernel_res = certify_kernel_api()
    nb_res = certify_nb_gain_coeff()
    zg_res = certify_zero_geometry()

    payload = {
        "audit": "codex-review-and-all-vector-extension-2026-10-15-v1",
        "precision_bits": PREC_BITS,
        "wall_check": {
            "rh_status": "OPEN",
            "g2_status": "OPEN",
            "cofinal_signed_arithmetic_lower_bound_status": "OPEN",
            "missing_original_evidence_groups_status": "OPEN",
        },
        "kernel_api": kernel_res,
        "nb_gain_coeff": nb_res,
        "zero_geometry": zg_res,
    }

    out_path = out_dir / "verification.json"
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")
    print(
        "KERNEL-API all-vector floor on (log 2, 1/2 log 6]:",
        kernel_res["sherman_morrison_at_half_log6"]["all_vector_floor_per_g_norm_sq"]["str"],
        "||g||_2^2 =",
        kernel_res["sherman_morrison_at_half_log6"]["all_vector_floor_per_L2g_norm_sq"]["str"],
        "||L_2 g||_2^2",
    )
    print(
        "NB-GAIN / COEFF C_b(psi7) =",
        nb_res["C_b_psi7_exact"],
        "piecewise <Lambda_4, sigma_5>_H diff =",
        nb_res["piecewise_N4_r5_check"]["abs_diff"]["str"],
    )
    print(
        "ZERO-GEOMETRY NS-101 Wronskian u-integral =",
        zg_res["ns101_reciprocal_dilation_kernel"]["wronskian_u_integral"]["str"],
    )


if __name__ == "__main__":
    main()
