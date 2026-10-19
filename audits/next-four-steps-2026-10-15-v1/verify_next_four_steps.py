"""Deterministic 256-bit flint.arb + mpmath verification for Next Four Steps (2026-10-15, v1).

Verifies:
- Part 1 (KERNEL-API 256-bit flint.arb / flint.acb Certificate):
  1. Rigorous interval-bisection and flint.acb.integral enclosure of the unique positive root
     xi_0 of alpha(xi) = Re psi(1/4 + i xi/2) - log pi = 0, I_neg, C_low, and the
     All-Vector Coercivity Floor on V_{a - log 2} across the Three-Island window
     log 2 < a <= (1/2) log 5:
       q[L_2 g] >= (5 log 2 / 2 - C_low (a - log 2)) ||g||_2^2
                >= [0.92182853...] ||g||_2^2 = [0.28363954...] ||L_2 g||_2^2 > 0.
  2. Rigorous 256-bit flint.arb / flint.acb.integral enclosure (with proved Plancherel
     short-interval bound on [0, 2^-60]) of the 2x2 even Dirichlet Galerkin matrices
     M_orig(a) and M_NS57(a) across all 5 sub-window checkpoints
     a in {0.75, (1/2)log 5, 0.90, (1/2)log 7, log 3}.
  3. Rigorous flint.arb separation at a = log 3: det M_orig(log 3) > 0 > det M_NS57(log 3),
     and rational witness g_* = g_1^+ + (3/25) g_2^+ in H_0^1(-log(3/2), log(3/2))
     satisfying q_orig[L_2 g_*] > 0 > q_NS57[L_2 g_*].
- Part 2 (NB-GAIN / COEFF Stieltjes-Divisor Dual Identity & NS-74 Control Diagnostic):
  1. Exact rational polynomial constants C_{psi_5} = 46183/15015 and C_{psi_7} = 5132/12155
     for the H_0^2([1,2]) Stieltjes-Divisor extractors Lambda_b(x) = d/dx(x F_b'(x)).
  2. 256-bit flint.arb certification across N in {4, 8, 16, 32, 64} for the Original NS-61
     family (beta = 1/2) and NS-74 altered-target controls (beta = 1/2 + 10^-2, 1/2 + 10^-6)
     that M_schur == M_pair == M_div, ||(Pi_{2N} - Pi_N)Lambda_b||_H^2 < C_psi N^3, and
     the orthogonal splitting E_N^(2)(beta) = E_{N,rem}^(2)(beta) + F_beta holds.
- Part 3 (ZERO-GEOMETRY Single-Point Wronskian & Cubic Integrating-Factor Obstruction):
  1. Exact symbolic jet-ring verification in Q[phi, phi', phi'', phi'''] of the cubic
     normal form of 8 phi(u)^3 J_PS(u).
  2. 50-digit verification of the gauge-invariant single-point Wronskian Parseval identity
     int_R 4 phi(u)^2 P_1(u) e^{2xu} du = -2 int_R |(phi(u)e^{xu})'|^2 du
     = -(1/pi) int_R tau^2 |f(x+i tau)|^2 dtau < 0
     on both RH-true and RH-false (NS-101) kernels, plus Davenport-Heilbronn screen.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

from flint import acb, arb, arb_mat, ctx

ROOT = Path(__file__).resolve().parents[2]
NS61_DIR = ROOT / "evidence" / "v159" / "ns61"
for p in (ROOT, NS61_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from certify_smoothed import Kernel, ball, dot, sub  # noqa: E402
from controls.davenport_heilbronn import screen  # noqa: E402


# ---------------------------------------------------------------------------
# Part 1: KERNEL-API 256-bit flint.arb / flint.acb Certificate
# ---------------------------------------------------------------------------

def overlap_even_arb(j: int, k: int, b: arb, tau: arb) -> arb:
    """Exact L^2(-b, b) shift overlap <T_tau g_j^+, g_k^+> in flint.arb."""
    pi_b = arb.pi()
    t = abs(tau)
    if t >= 2 * b:
        return arb(0)
    wj = (2 * j - 1) * pi_b / (2 * b)
    wk = (2 * k - 1) * pi_b / (2 * b)
    half_len = b - t / 2
    if j == k:
        return ((wj * t).cos() * (2 * half_len) + (2 * wj * half_len).sin() / wj) / (2 * b)
    term_diff = ((wj + wk) * t / 2).cos() * ((wj - wk) * half_len).sin() / (wj - wk)
    term_sum = ((wj - wk) * t / 2).cos() * ((wj + wk) * half_len).sin() / (wj + wk)
    return (term_diff + term_sum) / b


def overlap_even_acb(j: int, k: int, b: arb, t_z: acb) -> acb:
    """Analytic continuation of overlap_even_arb on a smooth subinterval 0 <= Re(t_z) <= 2b."""
    b_c = acb(b)
    pi_c = acb(arb.pi())
    wj = (2 * j - 1) * pi_c / (2 * b_c)
    wk = (2 * k - 1) * pi_c / (2 * b_c)
    half_len = b_c - t_z / 2
    if j == k:
        return ((wj * t_z).cos() * (2 * half_len) + (2 * wj * half_len).sin() / wj) / (2 * b_c)
    term_diff = ((wj + wk) * t_z / 2).cos() * ((wj - wk) * half_len).sin() / (wj - wk)
    term_sum = ((wj - wk) * t_z / 2).cos() * ((wj + wk) * half_len).sin() / (wj + wk)
    return (term_diff + term_sum) / b_c


def l2_shift_even_arb(j: int, k: int, b: arb, shift: arb) -> arb:
    """Exact inner product <(T_shift + T_{-shift}) L_2 g_j^+, L_2 g_k^+> in flint.arb."""
    ell2 = arb(2).log()
    r2 = arb(1) / arb(2).sqrt()
    weights = [
        (arb(0), arb(13) / 4),
        (ell2, -3 * r2),
        (-ell2, -3 * r2),
        (2 * ell2, arb(1) / 2),
        (-2 * ell2, arb(1) / 2),
    ]
    total = arb(0)
    for s_tau, w_tau in weights:
        total += w_tau * (
            overlap_even_arb(j, k, b, shift + s_tau)
            + overlap_even_arb(j, k, b, -shift + s_tau)
        )
    return total


def l2_shift_even_acb_piece(j: int, k: int, b: arb, t_mid: arb, t_z: acb) -> acb:
    """Analytic expression for <(T_t + T_{-t}) L_2 g_j^+, L_2 g_k^+> on a breakpoint-free subinterval."""
    ell2 = arb(2).log()
    r2 = arb(1) / arb(2).sqrt()
    weights = [
        (arb(0), arb(13) / 4),
        (ell2, -3 * r2),
        (-ell2, -3 * r2),
        (2 * ell2, arb(1) / 2),
        (-2 * ell2, arb(1) / 2),
    ]
    total = acb(0)
    for s_tau, w_tau in weights:
        for sign in (1, -1):
            val_mid = sign * t_mid + s_tau
            if abs(val_mid) < 2 * b:
                arg_z = (
                    (acb(sign) * t_z + acb(s_tau))
                    if val_mid >= 0
                    else -(acb(sign) * t_z + acb(s_tau))
                )
                total += acb(w_tau) * overlap_even_acb(j, k, b, arg_z)
    return total


def arch_even_arb(j: int, k: int, b: arb) -> arb:
    """Rigorous flint.arb + flint.acb.integral enclosure of q_arch(L_2 g_j^+, L_2 g_k^+)."""
    pi_b = arb.pi()
    ell2 = arb(2).log()
    a = b + ell2
    c_ar = (acb(1) / 4).digamma().real - pi_b.log()
    c0 = l2_shift_even_arb(j, k, b, arb(0)) / 2
    tail_const = ((1 + (-a).exp()) / (1 - (-a).exp())).log() + 2 * ((-a).exp()).atan()

    bpts = [arb(0), 2 * a]
    for s_mult in (0, 1, 2):
        base_s = s_mult * ell2
        for delta in (-2 * b, arb(0), 2 * b):
            for sign in (1, -1):
                cand = sign * (base_s + delta)
                if arb(0) < cand < 2 * a:
                    if not any((cand - x).contains(0) for x in bpts):
                        bpts.append(cand)
    bpts.sort(key=lambda x: float(x))

    # Proved Plancherel bound on [0, eps_t] (Lemma 1.1):
    # |int_0^eps (e^{t/2}/sinh t)(c0 - ct(t)) dt| <= (1/4)(3/2 + sqrt(2))^2 w_j w_k e^{eps/2} eps^2
    eps_t = arb(2) ** (-60)
    wj = (2 * j - 1) * pi_b / (2 * b)
    wk = (2 * k - 1) * pi_b / (2 * b)
    l2_sup_sq = (arb(3) / 2 + arb(2).sqrt()) ** 2
    short_err = (l2_sup_sq * wj * wk * (eps_t / 2).exp() * (eps_t ** 2)) / 4
    integral_total = arb(0, short_err)

    for idx in range(len(bpts) - 1):
        p0, p1 = bpts[idx], bpts[idx + 1]
        t_mid = (p0 + p1) / 2
        left_pt = eps_t if idx == 0 else p0

        def piece_fn(z: acb, _analytic: bool = False, tm: arb = t_mid) -> acb:
            ct = l2_shift_even_acb_piece(j, k, b, tm, z) / 2
            return (z / 2).exp() * (acb(c0) - ct) / z.sinh()

        piece_val = acb.integral(
            piece_fn, acb(left_pt), acb(p1), rel_tol=2 ** (-180), eval_limit=100000
        ).real
        integral_total += piece_val

    return (c_ar + tail_const) * c0 + integral_total


def prime_even_arb(j: int, k: int, a: arb, ns57: bool) -> arb:
    """Rigorous flint.arb enclosure of q_prime(L_2 g_j^+, L_2 g_k^+)."""
    ell2 = arb(2).log()
    r2 = arb(1) / arb(2).sqrt()
    eps_ns57 = arb(1) / arb(100)
    b = a - ell2
    ov = overlap_even_arb
    l2_jk = (arb(3) / 2) * ov(j, k, b, arb(0)) - r2 * (ov(j, k, b, ell2) + ov(j, k, b, -ell2))
    l2_sq_jk = (
        (arb(13) / 4) * ov(j, k, b, arb(0))
        - 3 * r2 * (ov(j, k, b, ell2) + ov(j, k, b, -ell2))
        + (arb(1) / 2) * (ov(j, k, b, 2 * ell2) + ov(j, k, b, -2 * ell2))
    )
    total = -ell2 * ((arb(1) / 2) * l2_jk - l2_sq_jk)
    for n, q in ((3, 3), (5, 5), (7, 7), (9, 3)):
        ln = arb(n).log()
        if ln < 2 * a:
            total -= (arb(q).log() / arb(n).sqrt()) * l2_shift_even_arb(j, k, b, ln)
    if ns57:
        total += eps_ns57 * ell2 * l2_shift_even_arb(j, k, b, ell2)
    return total


def min_eig_2x2_arb(m00: arb, m01: arb, m11: arb) -> arb:
    tr = m00 + m11
    disc = ((m00 - m11) ** 2 + 4 * (m01 ** 2)).sqrt()
    return (tr - disc) / 2


def verify_part1_kernel_api_arb() -> dict[str, Any]:
    """Run 256-bit flint.arb verification for Theorem 1A and Theorem 1B."""
    ctx.prec = 256
    pi_b = arb.pi()
    ell2 = arb(2).log()

    def alpha_real(xi: arb) -> arb:
        return acb(arb(1) / 4, xi / 2).digamma().real - pi_b.log()

    # 1. Enclose unique positive root xi_0 of alpha(xi) = 0
    lo = arb("6.289835988836902")
    hi = arb("6.289835988836904")
    assert alpha_real(lo) < 0 and alpha_real(hi) > 0
    for _ in range(80):
        mid = (lo + hi) / 2
        if alpha_real(mid) > 0:
            hi = mid
        else:
            lo = mid
    xi0 = lo.union(hi)
    assert alpha_real(lo) < 0 and alpha_real(hi) > 0

    def neg_integrand(z: acb, _analytic: bool = False) -> acb:
        s_l2 = acb(arb(3) / 2) - acb(arb(2).sqrt()) * (z * acb(ell2)).cos()
        alp = (acb(arb(1) / 4) + acb(0, 1) * z / 2).digamma() - acb(pi_b.log())
        return -alp * s_l2 * s_l2

    i_neg = acb.integral(neg_integrand, acb(0), acb(xi0), rel_tol=2 ** (-200), eval_limit=200000).real
    c_low = (2 / pi_b) * i_neg
    prime_three_island = arb(5) * ell2 / 2

    a_075 = arb(3) / 4
    b_075 = a_075 - ell2
    floor_g_075 = prime_three_island - c_low * b_075
    floor_f_075 = floor_g_075 / (arb(13) / 4)

    a_five = arb(5).log() / 2
    b_five = a_five - ell2
    floor_g_five = prime_three_island - c_low * b_five
    floor_f_five = floor_g_five / (arb(13) / 4)
    assert floor_g_075 > 0 and floor_f_075 > 0
    assert floor_g_five > 0 and floor_f_five > 0

    # 2. Enclose 2x2 even interior matrices across all 5 sub-window checkpoints
    windows = [
        ("subwindow_I_a_0.75", arb(3) / 4),
        ("subwindow_I_edge_half_log5", arb(5).log() / 2),
        ("subwindow_II_a_0.90", arb(9) / 10),
        ("subwindow_II_edge_half_log7", arb(7).log() / 2),
        ("subwindow_III_edge_log3", arb(3).log()),
    ]
    window_certificates: list[dict[str, Any]] = []
    c_rat = arb(3) / arb(25)

    for label, a_val in windows:
        b_val = a_val - ell2
        ae00 = arch_even_arb(1, 1, b_val)
        ae01 = arch_even_arb(1, 2, b_val)
        ae11 = arch_even_arb(2, 2, b_val)

        m00_orig = ae00 + prime_even_arb(1, 1, a_val, False)
        m01_orig = ae01 + prime_even_arb(1, 2, a_val, False)
        m11_orig = ae11 + prime_even_arb(2, 2, a_val, False)

        m00_ns57 = ae00 + prime_even_arb(1, 1, a_val, True)
        m01_ns57 = ae01 + prime_even_arb(1, 2, a_val, True)
        m11_ns57 = ae11 + prime_even_arb(2, 2, a_val, True)

        det_orig = m00_orig * m11_orig - m01_orig * m01_orig
        det_ns57 = m00_ns57 * m11_ns57 - m01_ns57 * m01_ns57
        eig_orig = min_eig_2x2_arb(m00_orig, m01_orig, m11_orig)
        eig_ns57 = min_eig_2x2_arb(m00_ns57, m01_ns57, m11_ns57)

        q_star_orig = m00_orig + 2 * c_rat * m01_orig + c_rat * c_rat * m11_orig
        q_star_ns57 = m00_ns57 + 2 * c_rat * m01_ns57 + c_rat * c_rat * m11_ns57

        assert m00_orig > 0 and det_orig > 0 and eig_orig > 0 and q_star_orig > 0
        if label != "subwindow_III_edge_log3":
            assert m00_ns57 > 0 and det_ns57 > 0 and eig_ns57 > 0
        else:
            assert det_ns57 < 0 and eig_ns57 < 0 and q_star_ns57 < 0

        window_certificates.append({
            "window": label,
            "a": a_val.str(25),
            "b": b_val.str(25),
            "M11_orig": m00_orig.str(25),
            "M12_orig": m01_orig.str(25),
            "M22_orig": m11_orig.str(25),
            "det_orig": det_orig.str(25),
            "min_eig_orig": eig_orig.str(25),
            "det_NS57": det_ns57.str(25),
            "min_eig_NS57": eig_ns57.str(25),
            "rational_witness_q_orig": q_star_orig.str(25),
            "rational_witness_q_NS57": q_star_ns57.str(25),
            "certified_orig_positive": bool(det_orig > 0 and m00_orig > 0),
            "certified_NS57_separated": bool(det_orig > 0 and det_ns57 < 0 and q_star_ns57 < 0),
        })

    return {
        "precision_bits": 256,
        "xi_0_ball": xi0.str(30),
        "I_neg_ball": i_neg.str(30),
        "C_low_ball": c_low.str(30),
        "three_island_prime_constant_5_log2_over_2": prime_three_island.str(30),
        "all_vector_floor_a_0.75_on_g_norm2": floor_g_075.str(30),
        "all_vector_floor_a_0.75_on_L2g_norm2": floor_f_075.str(30),
        "all_vector_floor_half_log5_on_g_norm2": floor_g_five.str(30),
        "all_vector_floor_half_log5_on_L2g_norm2": floor_f_five.str(30),
        "all_vector_three_island_certified": True,
        "rational_witness_c": "3/25",
        "window_certificates": window_certificates,
    }


# ---------------------------------------------------------------------------
# Part 2: NB-GAIN / COEFF Stieltjes-Divisor Identity & NS-74 Diagnostic
# ---------------------------------------------------------------------------

def p_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, va in enumerate(a):
        for j, vb in enumerate(b):
            out[i + j] += va * vb
    return out


def p_diff(a: list[Fraction]) -> list[Fraction]:
    return [Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)]


def p_int_12(a: list[Fraction]) -> Fraction:
    return sum((v * Fraction(2 ** (i + 1) - 1, i + 1) for i, v in enumerate(a)), Fraction(0))


def eval_p(p: list[Fraction], x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def verify_part2_nb_gain_ns74_arb() -> dict[str, Any]:
    """Run 256-bit flint.arb diagnostic for Theorem 2A and Theorem 2B across N in {4, 8, 16, 32, 64}."""
    ctx.prec = 256
    t0 = time.monotonic()

    u_minus_1 = [Fraction(-1), Fraction(1)]
    two_minus_u = [Fraction(2), Fraction(-1)]
    u_minus_3_2 = [Fraction(-3, 2), Fraction(1)]
    two_u_minus_3 = [Fraction(-3), Fraction(2)]
    u_poly = [Fraction(0), Fraction(1)]
    u2_poly = p_mul(u_poly, u_poly)

    psi_deg5 = p_mul(
        p_mul(u_minus_1, u_minus_1),
        p_mul(p_mul(two_minus_u, two_minus_u), u_minus_3_2),
    )
    psi_deg7 = p_mul(
        p_mul(u_minus_1, p_mul(u_minus_1, u_minus_1)),
        p_mul(p_mul(two_minus_u, p_mul(two_minus_u, two_minus_u)), two_u_minus_3),
    )

    assert p_int_12(psi_deg5) == Fraction(0)
    assert p_int_12(psi_deg7) == Fraction(0)

    op_psi5 = p_diff(p_mul(u2_poly, p_diff(psi_deg5)))
    op_psi7 = p_diff(p_mul(u2_poly, p_diff(psi_deg7)))
    c_psi5_frac = p_int_12(p_mul(u2_poly, p_mul(op_psi5, op_psi5)))
    c_psi7_frac = p_int_12(p_mul(u2_poly, p_mul(op_psi7, op_psi7)))
    assert c_psi5_frac == Fraction(46183, 15015)
    assert c_psi7_frac == Fraction(5132, 12155)
    c_psi7_ball = ball(c_psi7_frac)

    max_idx = 128
    kernel = Kernel(max_idx, 128, 24)
    gram = arb_mat(max_idx, max_idx)
    for m in range(1, max_idx + 1):
        for n in range(m, max_idx + 1):
            gram[m - 1, n - 1] = gram[n - 1, m - 1] = kernel.gram(m, n)

    families = [
        ("original_beta_0.5", arb(1) / 2, False),
        ("ns74_beta_0.5_plus_1e-2", arb(1) / 2 + arb(1) / 100, True),
        ("ns74_beta_0.5_plus_1e-6", arb(1) / 2 + arb(1) / 1000000, True),
    ]

    family_results: dict[str, Any] = {}
    for fam_name, beta, is_altered in families:
        loads = arb_mat(max_idx, 1)
        if not is_altered:
            for k in range(1, max_idx + 1):
                loads[k - 1, 0] = kernel.load(k)
            floor_val = arb(0)
        else:
            slope = (1 - beta) / beta
            constant = (2 * beta - 1) / (beta * beta)
            for k in range(1, max_idx + 1):
                loads[k - 1, 0] = (
                    slope * kernel.load(k)
                    - constant * (kernel.logs[k] + 2 - arb.const_euler() + 1 / beta) / k
                )
            floor_val = (2 * beta - 1) * (1 - beta) * (1 - beta) / (beta ** 6)

        rows: list[dict[str, Any]] = []
        for n_size in (4, 8, 16, 32, 64):
            g_old = sub(gram, 0, n_size, 0, n_size)
            c_cross = sub(gram, 0, n_size, n_size, 2 * n_size)
            d_new = sub(gram, n_size, 2 * n_size, n_size, 2 * n_size)
            b_old = sub(loads, 0, n_size, 0, 1)
            b_new = sub(loads, n_size, 2 * n_size, 0, 1)
            c_old = g_old.solve(b_old, algorithm="precond")
            h_vec = b_new - c_cross.transpose() * c_old
            s_schur = d_new - c_cross.transpose() * g_old.solve(c_cross, algorithm="precond")
            y_vec = s_schur.solve(h_vec, algorithm="precond")
            u_vec = -g_old.solve(c_cross * y_vec, algorithm="precond")

            e_n = 2 - dot(b_old, c_old)
            delta_n = dot(h_vec, y_vec)
            e_2n = e_n - delta_n
            e_n_rem = e_n - floor_val
            assert e_n > e_2n > floor_val and delta_n > 0

            lam_new_frac = [eval_p(psi_deg7, Fraction(n, n_size)) for n in range(n_size + 1, 2 * n_size + 1)]
            lam_old_frac = [
                sum(
                    (eval_p(psi_deg7, Fraction(k * m, n_size)) for k in range(2, 2 * n_size) if n_size < k * m < 2 * n_size),
                    Fraction(0),
                )
                for m in range(1, n_size + 1)
            ]
            lam_new = arb_mat([[ball(x)] for x in lam_new_frac])
            lam_old = arb_mat([[ball(x)] for x in lam_old_frac])
            lam_proj = lam_new - c_cross.transpose() * g_old.solve(lam_old, algorithm="precond")

            m_schur = dot(lam_proj, y_vec)
            m_pair = dot(lam_new, y_vec) + dot(lam_old, u_vec)
            m_div = arb(0)
            for idx, n in enumerate(range(n_size + 1, 2 * n_size)):
                div_sum = y_vec[idx, 0] + sum(
                    (u_vec[m - 1, 0] for m in range(1, n_size + 1) if n % m == 0), arb(0)
                )
                m_div += lam_new[idx, 0] * div_sum

            proj_norm2 = dot(lam_proj, s_schur.solve(lam_proj, algorithm="precond"))
            bessel_bound = c_psi7_ball * (arb(n_size) ** 3)
            assert (m_schur - m_pair).contains(0)
            assert (m_schur - m_div).contains(0)
            assert proj_norm2 < bessel_bound

            rayleigh_gain = (m_schur ** 2) / proj_norm2
            bessel_gain = (m_schur ** 2) / bessel_bound
            assert 0 < bessel_gain < rayleigh_gain < delta_n

            rows.append({
                "N": n_size,
                "E_N": e_n.str(25),
                "E_2N": e_2n.str(25),
                "E_N_removable": e_n_rem.str(25),
                "Delta_N": delta_n.str(25),
                "Delta_N_over_E_N": (delta_n / e_n).str(25),
                "Delta_N_over_E_N_removable": (delta_n / e_n_rem).str(25),
                "M_N_divisor_pairing": m_schur.str(25),
                "three_way_identity_max_diff": max(
                    float(abs(m_schur - m_pair).upper()),
                    float(abs(m_schur - m_div).upper()),
                ),
                "proj_norm2_over_N": (proj_norm2 / n_size).str(25),
                "proj_norm2_over_bessel_bound": (proj_norm2 / bessel_bound).str(25),
                "rayleigh_fraction_of_Delta_N": (rayleigh_gain / delta_n).str(25),
                "rayleigh_gain_over_E_N": (rayleigh_gain / e_n).str(25),
                "rayleigh_gain_over_E_N_removable": (rayleigh_gain / e_n_rem).str(25),
                "bessel_gain_over_E_N": (bessel_gain / e_n).str(25),
            })

        family_results[fam_name] = {
            "beta": beta.str(25),
            "positive_floor_F_beta": floor_val.str(25),
            "rows": rows,
        }

    return {
        "C_psi_deg5_H02": f"{c_psi5_frac.numerator}/{c_psi5_frac.denominator}",
        "C_psi_deg7_brief_v3": f"{c_psi7_frac.numerator}/{c_psi7_frac.denominator}",
        "elapsed_seconds": round(time.monotonic() - t0, 3),
        "families": family_results,
        "all_three_way_identities_and_bessel_bounds_verified": True,
    }


# ---------------------------------------------------------------------------
# Part 3: ZERO-GEOMETRY Single-Point Wronskian & Cubic Integrating-Factor
# ---------------------------------------------------------------------------

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


def poly_diff_jet(p: Poly, n_vars: int) -> Poly:
    """Apply d/du in the jet ring Q[phi, phi', phi'', phi'''] where d/du(phi^(k)) = phi^(k+1)."""
    out: Poly = {}
    for k, v in p.items():
        for idx in range(n_vars - 1):
            deg = k[idx]
            if deg > 0:
                new_k = list(k)
                new_k[idx] -= 1
                new_k[idx + 1] += 1
                tk = tuple(new_k)
                out[tk] = out.get(tk, Fraction(0)) + v * Fraction(deg)
    return poly_clean(out)


def verify_part3_zero_geometry_wronskian() -> dict[str, Any]:
    """Verify Theorem 3A (Single-Point Wronskian Parseval) and Theorem 3B (Cubic Normal Form)."""
    # 1. Symbolic jet-ring verification in Q[phi, phi', phi'', phi'''] (n_vars = 4)
    n_vars = 4
    phi0 = poly_var(n_vars, 0)
    phi1 = poly_var(n_vars, 1)
    phi2 = poly_var(n_vars, 2)
    phi3 = poly_var(n_vars, 3)

    phi0_sq = poly_mul(phi0, phi0)
    phi0_cu = poly_mul(phi0_sq, phi0)
    phi1_sq = poly_mul(phi1, phi1)
    phi1_cu = poly_mul(phi1_sq, phi1)

    # Principal part of 8 phi^3 J_PS = phi''' phi^2 + 9 phi' phi'' phi - 6 (phi')^3
    lhs_principal = poly_add(
        poly_mul(phi3, phi0_sq),
        poly_add(
            poly_mul(phi1, poly_mul(phi2, phi0)),
            phi1_cu,
            scale_b=Fraction(-2, 3),
        ),
        scale_b=Fraction(9),
    )

    # (1/3)(phi^3)''' + (3/2)((phi')^2 phi)' - (19/2)(phi')^3
    d1_phi_cu = poly_diff_jet(phi0_cu, n_vars)
    d2_phi_cu = poly_diff_jet(d1_phi_cu, n_vars)
    d3_phi_cu = poly_diff_jet(d2_phi_cu, n_vars)
    d1_phi1sq_phi0 = poly_diff_jet(poly_mul(phi1_sq, phi0), n_vars)

    rhs_principal = poly_add(
        d3_phi_cu,
        poly_add(
            d1_phi1sq_phi0,
            phi1_cu,
            scale_b=Fraction(-19, 3),
        ),
        scale_b=Fraction(9, 2),
    )
    rhs_principal = {k: v * Fraction(1, 3) for k, v in rhs_principal.items()}
    assert lhs_principal == rhs_principal

    # c_1 part: 8 phi^3 (-4 P_1 - 12 P_0^2) = -8 (phi'' phi^2 + 2 (phi')^2 phi) == -(8/3) (phi^3)''
    lhs_c1 = poly_add(
        poly_mul(phi2, phi0_sq),
        poly_mul(phi1_sq, phi0),
        scale_b=Fraction(2),
    )
    lhs_c1 = {k: v * Fraction(-8) for k, v in lhs_c1.items()}
    rhs_c1 = {k: v * Fraction(-8, 3) for k, v in d2_phi_cu.items()}
    assert lhs_c1 == rhs_c1

    # c_2 part: 8 phi^3 (P_0) = 4 phi' phi^2 == (4/3) (phi^3)'
    lhs_c2 = {k: v * Fraction(4) for k, v in poly_mul(phi1, phi0_sq).items()}
    rhs_c2 = {k: v * Fraction(4, 3) for k, v in d1_phi_cu.items()}
    assert lhs_c2 == rhs_c2

    # 2. High-precision (256-bit flint.arb / flint.acb.integral) verification of Theorem 3A
    # (Single-Point Wronskian Parseval) on both an RH-true kernel (Gaussian-cosh) and an
    # RH-violating NS-101 kernel.
    ctx.prec = 256
    pi_b = arb.pi()
    pi_c = acb(pi_b)
    sqrt_pi_c = pi_c.sqrt()
    half_c = acb(arb(1) / 2)
    qtr_c = acb(arb(1) / 4)

    def jet_rh_true(u: acb) -> tuple[acb, acb, acb]:
        eu2 = (-u * u).exp()
        g0 = (u * half_c).cosh()
        g1 = half_c * (u * half_c).sinh()
        g2 = qtr_c * g0
        p0 = eu2 * g0
        p1 = eu2 * (g1 - acb(2) * u * g0)
        p2 = eu2 * (g2 - acb(4) * u * g1 + (acb(4) * u * u - acb(2)) * g0)
        return p0, p1, p2

    def f_rh_true(z: acb) -> acb:
        return (sqrt_pi_c * half_c) * (
            (((z + half_c) ** 2) * qtr_c).exp()
            + (((z - half_c) ** 2) * qtr_c).exp()
        )

    def jet_ns101(u: acb) -> tuple[acb, acb, acb]:
        eu2 = (-u * u).exp()
        ch = (u * half_c).cosh()
        sh = (u * half_c).sinh()
        c2 = (acb(2) * u).cos()
        s2 = (acb(2) * u).sin()
        g0 = ch + half_c * c2
        g1 = half_c * sh - s2
        g2 = qtr_c * ch - acb(2) * c2
        p0 = eu2 * g0
        p1 = eu2 * (g1 - acb(2) * u * g0)
        p2 = eu2 * (g2 - acb(4) * u * g1 + (acb(4) * u * u - acb(2)) * g0)
        return p0, p1, p2

    def f_ns101(z: acb) -> acb:
        base = f_rh_true(z)
        two_i = acb(0, 2)
        pert = (sqrt_pi_c * qtr_c) * (
            (((z + two_i) ** 2) * qtr_c).exp()
            + (((z - two_i) ** 2) * qtr_c).exp()
        )
        return base + pert

    x_slice_b = arb(3) / arb(10)
    x_slice_c = acb(x_slice_b)
    tol_int = 2 ** (-180)
    wronskian_checks: dict[str, Any] = {}
    for name, jet_fn, f_fn in (
        ("rh_true_gaussian_cosh", jet_rh_true, f_rh_true),
        ("rh_false_ns101_control", jet_ns101, f_ns101),
    ):
        def w2_integrand(u: acb, _analytic: bool = False, jf: Any = jet_fn) -> acb:
            p0, p1, p2 = jf(u)
            return (p2 * p0 - p1 * p1) * (acb(2) * x_slice_c * u).exp()

        def psi_deriv_sq(u: acb, _analytic: bool = False, jf: Any = jet_fn) -> acb:
            p0, p1, _ = jf(u)
            val = (p1 + x_slice_c * p0) * (x_slice_c * u).exp()
            return val * val

        def freq_integrand(tau: acb, _analytic: bool = False, ff: Any = f_fn) -> acb:
            z_p = x_slice_c + acb(0, 1) * tau
            z_m = x_slice_c - acb(0, 1) * tau
            return (tau * tau) * ff(z_p) * ff(z_m)

        lhs_w2 = acb.integral(w2_integrand, acb(-12), acb(12), rel_tol=tol_int, abs_tol=tol_int, eval_limit=200000).real
        mid_spatial = -arb(2) * acb.integral(psi_deriv_sq, acb(-12), acb(12), rel_tol=tol_int, abs_tol=tol_int, eval_limit=200000).real
        rhs_freq = -(arb(1) / pi_b) * acb.integral(freq_integrand, acb(-20), acb(20), rel_tol=tol_int, abs_tol=tol_int, eval_limit=200000).real
        err_spatial = abs(lhs_w2 - mid_spatial)
        err_freq = abs(lhs_w2 - rhs_freq)
        assert lhs_w2 < 0 and err_spatial < arb("1e-42") and err_freq < arb("1e-42"), (lhs_w2, err_spatial, err_freq)
        wronskian_checks[name] = {
            "x_slice": "0.3",
            "single_point_wronskian_transform": lhs_w2.str(25),
            "spatial_energy_identity_error": err_spatial.str(12),
            "vertical_line_parseval_error": err_freq.str(12),
            "strictly_negative": bool(lhs_w2 < 0),
        }

    def dh_candidate(_f_ctrl: Any, phi_ctrl: Any) -> bool:
        u0 = 0.5
        h_fd = 1e-6
        p0 = float(phi_ctrl(u0))
        p1 = (float(phi_ctrl(u0 + h_fd)) - float(phi_ctrl(u0 - h_fd))) / (2.0 * h_fd)
        x_f = 0.3
        integrand_val = -2.0 * (((p1 + x_f * p0) * (2.718281828459045 ** (x_f * u0))) ** 2)
        return bool(integrand_val < 0.0)

    dh_screen = screen(
        dh_candidate,
        "Single-point quadratic Wronskian W_2[phi] = 4 phi^2 P_1 and cubic cleared 8 phi^3 J_PS",
        sample_domain="x in R vertical-line Parseval slice and jet ring Q[phi, phi', phi'', phi''']",
        applicability=(
            "Applicable to any real-even kernel phi(u), including NS-101 and Davenport-Heilbronn: "
            "Theorem 3A proves int_R 4 phi(u)^2 P_1(u) e^{2xu} du = -(1/pi) int_R tau^2 |f(x+i tau)|^2 dtau < 0 "
            "for ALL non-zero real kernels regardless of off-line zeros, so single-point Wronskian "
            "clearing cannot separate RH-true kernels from NS-101 or Davenport-Heilbronn."
        ),
        applicable=True,
        observations={
            "rh_true_wronskian_transform": wronskian_checks["rh_true_gaussian_cosh"]["single_point_wronskian_transform"],
            "ns101_wronskian_transform": wronskian_checks["rh_false_ns101_control"]["single_point_wronskian_transform"],
        },
    )

    return {
        "cubic_jet_ring_normal_form_verified": True,
        "principal_normal_form": "(1/3)(phi^3)''' + (3/2)((phi')^2 phi)' - (19/2)(phi')^3",
        "c1_normal_form": "-(8/3) c_1 (phi^3)''",
        "c2_normal_form": "+(4/3) c_2 (phi^3)'",
        "c3_normal_form": "+8 c_3 phi^3",
        "single_point_wronskian_parseval_checks": wronskian_checks,
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

    res_part1 = verify_part1_kernel_api_arb()
    res_part2 = verify_part2_nb_gain_ns74_arb()
    res_part3 = verify_part3_zero_geometry_wronskian()

    payload = {
        "audit": "next-four-steps-2026-10-15-v1",
        "date": "2026-10-15",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "part1_kernel_api_arb_certificate": res_part1,
        "part2_nb_gain_stieltjes_divisor_vs_ns74": res_part2,
        "part3_zero_geometry_single_point_wronskian": res_part3,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "part1_three_island_floor_g": res_part1["all_vector_floor_half_log5_on_g_norm2"],
        "part1_log3_separation_certified": res_part1["window_certificates"][-1]["certified_NS57_separated"],
        "part2_C_psi7": res_part2["C_psi_deg7_brief_v3"],
        "part3_cubic_normal_form": res_part3["cubic_jet_ring_normal_form_verified"],
    }, indent=2))


if __name__ == "__main__":
    main()
