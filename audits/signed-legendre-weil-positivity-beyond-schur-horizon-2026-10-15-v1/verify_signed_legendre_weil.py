#!/usr/bin/env python3
"""
Milestone 15 Verification & Certificate Script:
Exact Signed Legendre Weil Positivity Beyond the Unsigned Schur Horizon &
Universal Reflection Kernel Strictness (WEIL-FLOOR & NB-GAIN / COEFF).

Replays all ball-arithmetic certificates at TWO precisions (256-bit and 384-bit
flint.arb) with zero float tolerances in ball checks.

Wall check: Does NOT prove RH, G2, or the cofinal prime-shift lower bound as a -> infinity.
Both missing-original evidence groups in evidence/MISSING.md remain OPEN.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

import flint


def jacobi_eigh_f(a_in: list[list[float]], max_sweeps: int = 35) -> tuple[list[float], list[list[float]]]:
    """Pure-Python Jacobi symmetric eigenvalue/eigenvector solver on midpoint matrices."""
    n = len(a_in)
    a = [row[:] for row in a_in]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = sum(a[i][j] * a[i][j] for i in range(n) for j in range(i + 1, n))
        if off < 1e-30:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < 1e-18:
                    continue
                tau = (a[q][q] - a[p][p]) / (2.0 * apq)
                t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau) if tau != 0.0 else 1.0
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                a[p][p] -= t * apq
                a[q][q] += t * apq
                a[p][q] = a[q][p] = 0.0
                for r in range(n):
                    if r != p and r != q:
                        arp = a[r][p]
                        arq = a[r][q]
                        a[r][p] = a[p][r] = c * arp - s * arq
                        a[r][q] = a[q][r] = s * arp + c * arq
                for r in range(n):
                    vrp = v[r][p]
                    vrq = v[r][q]
                    v[r][p] = c * vrp - s * vrq
                    v[r][q] = s * vrp + c * vrq
    order = sorted(range(n), key=lambda idx: a[idx][idx])
    vals = [a[idx][idx] for idx in order]
    vecs = [[v[row_i][idx] for idx in order] for row_i in range(n)]
    return vals, vecs


ALL_PRIMES: list[int] = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
]


def arb_abs(x: flint.arb) -> flint.arb:
    return abs(x)


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


def acb_sinc(z: flint.acb) -> flint.acb:
    return z.sinc()


def spherical_bessel_j_acb(m: int, z: flint.acb) -> flint.acb:
    """
    Exact evaluation of the spherical Bessel function j_m(z) in flint.acb via
    the entire hypergeometric representation:
        j_m(z) = (z^m / (2m + 1)!!) * 0F1(; m + 3/2; -z^2 / 4).
    """
    double_fact = 1
    for k in range(1, 2 * m + 2, 2):
        double_fact *= k
    b_param = flint.acb(flint.arb(2 * m + 3) / flint.arb(2))
    w_arg = -(z * z) / flint.acb(4)
    hyp = w_arg.hypgeom_0f1(b_param)
    return (z**m) * hyp / flint.acb(double_fact)


def alpha_acb(xi: flint.acb) -> flint.acb:
    pi_acb = flint.acb.pi()
    qtr = flint.acb(flint.arb(1) / flint.arb(4))
    ihalf = flint.acb(flint.arb(0), flint.arb(1) / flint.arb(2))
    z1 = qtr + ihalf * xi
    z2 = qtr - ihalf * xi
    return flint.acb(flint.arb(1) / flint.arb(2)) * (z1.digamma() + z2.digamma()) - pi_acb.log()


def sigma_lp_acb(xi: flint.acb, primes: list[int]) -> flint.acb:
    prod = flint.acb(1)
    for p in primes:
        p_arb = flint.arb(p)
        logp = p_arb.log()
        c_p = flint.acb((p_arb + flint.arb(1)) / p_arb)
        amp_p = flint.acb(flint.arb(2) / p_arb.sqrt())
        prod = prod * (c_p - amp_p * (xi * flint.acb(logp)).cos())
    return prod


def find_alpha_root_arb(target_da: flint.arb, n_iter: int = 300) -> flint.arb:
    lo = flint.arb(4)
    hi = flint.arb(50)
    half = flint.arb(1) / flint.arb(2)
    for _ in range(n_iter):
        mid = half * (lo + hi)
        val = alpha_acb(flint.acb(mid)).real - target_da
        if val < flint.arb(0):
            lo = mid
        elif val > flint.arb(0):
            hi = mid
        else:
            break
    assert alpha_acb(flint.acb(lo)).real < target_da
    assert alpha_acb(flint.acb(hi)).real > target_da
    center = half * (lo + hi)
    rad = half * (hi - lo) + arb_abs(center - lo)
    return flint.arb(center.mid(), rad.upper())


def integrate_on_0_to_xi0(fn: Any, xi0: flint.arb, tol_exp: int) -> tuple[flint.arb, flint.arb]:
    xi0_mid = flint.arb(xi0.mid())
    rad_xi0 = flint.arb(xi0.rad())
    tol = 2.0 ** (-tol_exp)
    main_val = flint.acb.integral(fn, flint.acb(0), flint.acb(xi0_mid), rel_tol=tol, abs_tol=tol)
    val_at_ball = fn(flint.acb(xi0), None)
    tail_re = arb_abs(val_at_ball.real) * rad_xi0
    tail_im = arb_abs(val_at_ball.imag) * rad_xi0
    res_re = main_val.real + flint.arb(0, tail_re.upper())
    res_im = main_val.imag + flint.arb(0, tail_im.upper())
    return res_re, res_im


def cholesky_lower_arb(mat: list[list[flint.arb]]) -> list[list[flint.arb]]:
    n = len(mat)
    l_mat = [[flint.arb(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = mat[i][j]
            for k in range(j):
                s = s - l_mat[i][k] * l_mat[j][k]
            if i == j:
                assert s > flint.arb(0), f"Cholesky pivot <= 0 at index {i}: {s}"
                l_mat[i][i] = s.sqrt()
            else:
                l_mat[i][j] = s / l_mat[j][j]
    return l_mat


def certify_min_eig_lower_bound_arb(mat: list[list[flint.arb]]) -> tuple[flint.arb, list[flint.arb]]:
    """
    Certify a sharp positive lower bound lambda_lb > 0 on lambda_min(mat) in flint.arb
    by choosing a rational candidate slightly below the midpoint minimum eigenvalue
    and certifying positive definiteness of (mat - lambda_lb * I_d) via exact Cholesky
    factorization in flint.arb.
    """
    d = len(mat)
    m_mid = [[float(mat[i][j].mid()) for j in range(d)] for i in range(d)]
    vals, _ = jacobi_eigh_f(m_mid)
    lam_min_f = vals[0]
    assert lam_min_f > 0.0, f"Matrix midpoint min eig not positive: {lam_min_f}"
    # Choose rational candidate 0.999 * lam_min_f rounded to 10^-6
    cand_int = max(1, int(math.floor(lam_min_f * 0.999 * 1_000_000)))
    lam_lb = flint.arb(cand_int) / flint.arb(1_000_000)
    shifted = [
        [(mat[i][j] - lam_lb) if i == j else mat[i][j] for j in range(d)]
        for i in range(d)
    ]
    l_mat = cholesky_lower_arb(shifted)
    pivots = [l_mat[i][i] for i in range(d)]
    return lam_lb, pivots


def certify_rayleigh_upper_bound_arb(mat: list[list[flint.arb]]) -> tuple[flint.arb, list[int]]:
    """
    For a matrix mat whose minimum eigenvalue is negative (or any symmetric matrix),
    construct an integer witness vector v in Z^d from the rounded midpoint minimum
    eigenvector and compute the exact Rayleigh quotient R(v) = (v^T mat v) / (v^T v)
    in flint.arb, certifying lambda_min(mat) <= R(v).
    """
    d = len(mat)
    m_mid = [[float(mat[i][j].mid()) for j in range(d)] for i in range(d)]
    _, vecs = jacobi_eigh_f(m_mid)
    v_f = [vecs[i][0] for i in range(d)]
    v_int = [int(round(float(x) * 1_000_000)) for x in v_f]
    if all(x == 0 for x in v_int):
        v_int[0] = 1
    v_arb = [flint.arb(x) for x in v_int]
    num = flint.arb(0)
    den = flint.arb(0)
    for i in range(d):
        den = den + v_arb[i] * v_arb[i]
        for j in range(d):
            num = num + v_arb[i] * mat[i][j] * v_arb[j]
    rayleigh = num / den
    return rayleigh, v_int


def legendre_poly_coeffs(m: int) -> list[flint.arb]:
    if m == 0:
        return [flint.arb(1)]
    if m == 1:
        return [flint.arb(0), flint.arb(1)]
    p_prev = [flint.arb(1)]
    p_curr = [flint.arb(0), flint.arb(1)]
    for k in range(1, m):
        k_arb = flint.arb(k)
        kp1 = flint.arb(k + 1)
        twokp1 = flint.arb(2 * k + 1)
        p_next = [flint.arb(0) for _ in range(k + 2)]
        for deg, c in enumerate(p_curr):
            p_next[deg + 1] = p_next[deg + 1] + (twokp1 * c) / kp1
        for deg, c in enumerate(p_prev):
            p_next[deg] = p_next[deg] - (k_arb * c) / kp1
        p_prev = p_curr
        p_curr = p_next
    return p_curr


def poly_shift_arb(coeffs: list[flint.arb], u: flint.arb) -> list[flint.arb]:
    deg = len(coeffs) - 1
    out = [flint.arb(0) for _ in range(deg + 1)]
    for k, c_k in enumerate(coeffs):
        binom = 1
        for j in range(k + 1):
            if j > 0:
                binom = (binom * (k - j + 1)) // j
            out[j] = out[j] + c_k * flint.arb(binom) * (u ** (k - j))
    return out


def poly_mul_arb(p1: list[flint.arb], p2: list[flint.arb]) -> list[flint.arb]:
    out = [flint.arb(0) for _ in range(len(p1) + len(p2) - 1)]
    for i, a in enumerate(p1):
        for j, b in enumerate(p2):
            out[i + j] = out[i + j] + a * b
    return out


def poly_integrate_arb(coeffs: list[flint.arb], a: flint.arb, b: flint.arb) -> flint.arb:
    s = flint.arb(0)
    for k, c_k in enumerate(coeffs):
        kp1 = flint.arb(k + 1)
        s = s + c_k * ((b ** (k + 1)) - (a ** (k + 1))) / kp1
    return s


def exact_shift_entry_arb(m: int, n: int, u: flint.arb) -> flint.arb:
    assert (m - n) % 2 == 0
    pm = legendre_poly_coeffs(m)
    pn_shifted = poly_shift_arb(legendre_poly_coeffs(n), u)
    prod_poly = poly_mul_arb(pm, pn_shifted)
    norm_fac = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
    return norm_fac * poly_integrate_arb(prod_poly, flint.arb(-1), flint.arb(1) - u)


def exact_support_entry_any_parity_arb(m: int, n: int, u: flint.arb) -> flint.arb:
    """
    Compute (D_tau)_{m, n} for any same-parity (m == n mod 2) and u = tau / b in [0, 2]:
        (D_tau)_{m, n} = sqrt((2m+1)(2n+1)) * int_{-1}^{1 - u} P_m(t) P_n(t) dt.
    """
    assert (m - n) % 2 == 0
    pm = legendre_poly_coeffs(m)
    pn = legendre_poly_coeffs(n)
    prod_poly = poly_mul_arb(pm, pn)
    norm_fac = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
    return norm_fac * poly_integrate_arb(prod_poly, flint.arb(-1), flint.arb(1) - u)


def eval_legendre_acb(m: int, z: flint.acb) -> flint.acb:
    coeffs = legendre_poly_coeffs(m)
    res = flint.acb(0)
    for c in reversed(coeffs):
        res = res * z + flint.acb(c)
    return res


def build_q_terms_arb(p_set: list[int]) -> tuple[flint.arb, flint.arb, dict[Fraction, flint.arb]]:
    primorial = math.prod(p_set)
    c_zero = flint.arb(1)
    gamma_k = flint.arb(0)
    for p in p_set:
        p_arb = flint.arb(p)
        c_zero = c_zero * (flint.arb(1) + flint.arb(1) / p_arb)
        gamma_k = gamma_k + (flint.arb(2) * p_arb.log()) / (p_arb + flint.arb(1))
    c_diag = c_zero * gamma_k

    factors: list[tuple[int, flint.arb, flint.arb]] = [
        (p, flint.arb(p + 1) / flint.arb(p), -flint.arb(1) / flint.arb(p).sqrt())
        for p in p_set
    ]

    def build_l_sub(sub_f: list[tuple[int, flint.arb, flint.arb]]) -> dict[Fraction, flint.arb]:
        terms: dict[Fraction, flint.arb] = {Fraction(1, 1): flint.arb(1)}
        for p, c0, c1 in sub_f:
            nt: dict[Fraction, flint.arb] = {}
            for r, val in terms.items():
                nt[r] = nt.get(r, flint.arb(0)) + val * c0
                nt[r * p] = nt.get(r * p, flint.arb(0)) + val * c1
                nt[r / p] = nt.get(r / p, flint.arb(0)) + val * c1
            terms = nt
        return terms

    l_full = build_l_sub(factors)
    q_terms: dict[Fraction, flint.arb] = {}
    log_prim = flint.arb(primorial).log()
    for r, val in l_full.items():
        q_terms[r] = q_terms.get(r, flint.arb(0)) + log_prim * val
    for idx, p in enumerate(p_set):
        sub_f = factors[:idx] + factors[idx + 1 :]
        l_sub = build_l_sub(sub_f)
        w_p = (flint.arb(p - 1) / flint.arb(p)) * flint.arb(p).log()
        for r, val in l_sub.items():
            q_terms[r] = q_terms.get(r, flint.arb(0)) - w_p * val

    ext_primes = [p for p in ALL_PRIMES if p not in p_set]
    for p in ext_primes:
        logp = flint.arb(p).log()
        pk = p
        while pk <= primorial * 2:
            w_coeff = -logp / flint.arb(pk).sqrt()
            for r, val in l_full.items():
                for prod_r in (r * pk, r / pk):
                    if Fraction(1, 2) < prod_r < Fraction(2, 1):
                        q_terms[prod_r] = q_terms.get(prod_r, flint.arb(0)) + val * w_coeff
            pk *= p

    return c_zero, c_diag, q_terms


def build_general_dirichlet_q_terms_arb(
    p_set: list[int], lam_vec: list[flint.arb]
) -> tuple[flint.arb, dict[Fraction, flint.arb]]:
    terms: dict[Fraction, flint.arb] = {Fraction(1, 1): flint.arb(1)}
    for p in p_set:
        c0 = flint.arb(p + 1) / flint.arb(p)
        c1 = -flint.arb(1) / flint.arb(p).sqrt()
        nt: dict[Fraction, flint.arb] = {}
        for r, val in terms.items():
            nt[r] = nt.get(r, flint.arb(0)) + val * c0
            nt[r * p] = nt.get(r * p, flint.arb(0)) + val * c1
            nt[r / p] = nt.get(r / p, flint.arb(0)) + val * c1
        terms = nt

    q_terms: dict[Fraction, flint.arb] = {}
    tiny = flint.arb(2) ** (-200)
    for r, l_val in terms.items():
        for n in range(2, len(lam_vec)):
            if arb_abs(lam_vec[n]) > tiny:
                w_n = -lam_vec[n] / flint.arb(n).sqrt()
                for q in (r * n, r / Fraction(n, 1)):
                    if Fraction(1, 2) < q < Fraction(2, 1):
                        q_terms[q] = q_terms.get(q, flint.arb(0)) + l_val * w_n
    return q_terms[Fraction(1, 1)], q_terms


def certify_theorem_1_reflection_strictness(prec_bits: int) -> dict[str, Any]:
    """
    Certify Theorem 1 in prec_bits flint.arb:
      1. Single-integral completion-of-the-square identity across u = 1:
         symbolic polynomial integration vs numerical flint.acb.integral of
         (f(x) + sigma f(x+u))^2 on [-1, 1-u] for both even and odd Legendre modes.
      2. All-degree polynomial reflection strictness across u in {1/4, 3/4, 1, 5/4, 7/4}:
         - Q_{tau,+1}^{(4,even)} > 0 on R^4 via Cholesky
         - Q_{tau,+1}^{(4,odd)} > 0 on R^4 via Cholesky
         - Qtilde_{tau,-1}^{(4,even)} > 0 on R^3 via Cholesky (with row/col 0 == 0)
         - Q_{tau,-1}^{(4,odd)} > 0 on R^4 via Cholesky
    """
    flint.ctx.prec = prec_bits
    t0 = time.time()
    tol = 2.0 ** (-55 if prec_bits <= 256 else -75)

    u_grid = [
        ("1/4", flint.arb(1) / flint.arb(4)),
        ("3/4", flint.arb(3) / flint.arb(4)),
        ("1", flint.arb(1)),
        ("5/4", flint.arb(5) / flint.arb(4)),
        ("7/4", flint.arb(7) / flint.arb(4)),
    ]

    grid_certs: list[dict[str, Any]] = []
    for u_label, u_val in u_grid:
        q_pos_e = [[flint.arb(0) for _ in range(4)] for _ in range(4)]
        q_neg_e = [[flint.arb(0) for _ in range(4)] for _ in range(4)]
        q_pos_o = [[flint.arb(0) for _ in range(4)] for _ in range(4)]
        q_neg_o = [[flint.arb(0) for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(i, 4):
                se = exact_shift_entry_arb(2 * i, 2 * j, u_val)
                de = exact_support_entry_any_parity_arb(2 * i, 2 * j, u_val)
                so = exact_shift_entry_arb(2 * i + 1, 2 * j + 1, u_val)
                do = exact_support_entry_any_parity_arb(2 * i + 1, 2 * j + 1, u_val)

                q_pos_e[i][j] = de + se
                q_pos_e[j][i] = de + se
                q_neg_e[i][j] = de - se
                q_neg_e[j][i] = de - se

                q_pos_o[i][j] = do + so
                q_pos_o[j][i] = do + so
                q_neg_o[i][j] = do - so
                q_neg_o[j][i] = do - so

        # Verify Row 0 / Col 0 of Q_{tau,-1}^{(4,even)} contains 0:
        for j in range(4):
            assert q_neg_e[0][j].contains(0), f"Q_neg_e[0][{j}] != 0 at u={u_label}"

        # Verify single-integral square identity on (m,n) = (2,2) and (3,3) via flint.acb.integral:
        u_acb = flint.acb(u_val)
        upper_acb = flint.acb(flint.arb(1) - u_val)

        def sq_even_22(z: flint.acb, _: Any, u_c: flint.acb = u_acb) -> flint.acb:
            v = eval_legendre_acb(2, z) + eval_legendre_acb(2, z + u_c)
            return (flint.acb(5) / flint.acb(2)) * v * v

        def sq_odd_33(z: flint.acb, _: Any, u_c: flint.acb = u_acb) -> flint.acb:
            v = eval_legendre_acb(3, z) - eval_legendre_acb(3, z + u_c)
            return (flint.acb(7) / flint.acb(2)) * v * v

        int_e22 = flint.acb.integral(sq_even_22, flint.acb(-1), upper_acb, rel_tol=tol, abs_tol=tol).real
        int_o33 = flint.acb.integral(sq_odd_33, flint.acb(-1), upper_acb, rel_tol=tol, abs_tol=tol).real
        assert (q_pos_e[1][1] - int_e22).contains(0), f"Square integral mismatch even (2,2) at u={u_label}"
        assert (q_neg_o[1][1] - int_o33).contains(0), f"Square integral mismatch odd (3,3) at u={u_label}"

        # Cholesky certifications of all 4 blocks:
        l_pos_e = cholesky_lower_arb(q_pos_e)
        l_pos_o = cholesky_lower_arb(q_pos_o)
        q_neg_e_sub = [[q_neg_e[i][j] for j in range(1, 4)] for i in range(1, 4)]
        l_neg_e_sub = cholesky_lower_arb(q_neg_e_sub)
        l_neg_o = cholesky_lower_arb(q_neg_o)

        grid_certs.append({
            "u_label": u_label,
            "u": arb_to_dict(u_val),
            "Q_pos_even_cholesky_pivots": [arb_to_dict(l_pos_e[i][i]) for i in range(4)],
            "Q_pos_odd_cholesky_pivots": [arb_to_dict(l_pos_o[i][i]) for i in range(4)],
            "Q_neg_even_3x3_cholesky_pivots": [arb_to_dict(l_neg_e_sub[i][i]) for i in range(3)],
            "Q_neg_odd_cholesky_pivots": [arb_to_dict(l_neg_o[i][i]) for i in range(4)],
            "square_integral_even_22_diff_contains_zero": True,
            "square_integral_odd_33_diff_contains_zero": True,
            "row0_neg_even_contains_zero": True,
        })

    return {
        "prec_bits": prec_bits,
        "u_grid_certificates": grid_certs,
        "elapsed_s": round(time.time() - t0, 4),
    }


def certify_checkpoint_signed_vs_unsigned(
    p_set: list[int],
    n_target: int,
    da: flint.arb,
    xi0: flint.arb,
    c_zero: flint.arb,
    c_diag: flint.arb,
    q_terms: dict[Fraction, flint.arb],
    tol_exp: int,
) -> dict[str, Any]:
    primorial = math.prod(p_set)
    pi = flint.arb.pi()
    half = flint.arb(1) / flint.arb(2)
    tiny = flint.arb(2) ** (-200)

    a_val = half * flint.arb(n_target).log()
    b_val = half * (flint.arb(n_target).log() - flint.arb(primorial).log())

    active_shifts: list[tuple[Fraction, flint.arb, flint.arb]] = []
    n_two_sided = 0
    n_single_ref = 0
    n_pos_shifts = 0
    r_horizon = Fraction(n_target, primorial)
    for r in sorted(q_terms.keys()):
        if Fraction(1, 1) < r < r_horizon:
            tau_r = flint.arb(r.numerator).log() - flint.arb(r.denominator).log()
            coeff_r = q_terms[r]
            if arb_abs(coeff_r) > tiny:
                active_shifts.append((r, tau_r, coeff_r))
                if r * r >= r_horizon:
                    n_single_ref += 1
                else:
                    n_two_sided += 1
                if coeff_r > flint.arb(0):
                    n_pos_shifts += 1

    b_acb = flint.acb(b_val)
    two_b_over_pi = (flint.arb(2) * b_val) / pi
    two_b_over_pi_acb = flint.acb(two_b_over_pi)

    # Full infinite-dimensional Parseval traces Tr(A_even), Tr(A_odd):
    def int_traces(xi: flint.acb, _: Any) -> flint.acb:
        w = two_b_over_pi_acb * sigma_lp_acb(xi, p_set) * (flint.acb(da) - alpha_acb(xi))
        z = b_acb * xi
        s2z = acb_sinc(flint.acb(2) * z)
        tr_e = flint.acb(half) * (flint.acb(1) + s2z)
        tr_o = flint.acb(half) * (flint.acb(1) - s2z)
        return w * (tr_e + flint.acb(0, 1) * tr_o)

    tr_e_full, tr_o_full = integrate_on_0_to_xi0(int_traces, xi0, tol_exp)

    # 4x4 Archimedean Legendre matrices A^{(4,even)} and A^{(4,odd)}:
    a_even = [[flint.arb(0) for _ in range(4)] for _ in range(4)]
    a_odd = [[flint.arb(0) for _ in range(4)] for _ in range(4)]
    for r_idx in range(4):
        for s_idx in range(r_idx, 4):
            sgn_rs = flint.acb(1 if (r_idx + s_idx) % 2 == 0 else -1)
            norm_e = flint.acb((flint.arb(4 * r_idx + 1) * flint.arb(4 * s_idx + 1)).sqrt())
            norm_o = flint.acb((flint.arb(4 * r_idx + 3) * flint.arb(4 * s_idx + 3)).sqrt())

            def int_pair(
                xi: flint.acb,
                _: Any,
                ri: int = r_idx,
                si: int = s_idx,
                sgn: flint.acb = sgn_rs,
                ne: flint.acb = norm_e,
                no: flint.acb = norm_o,
            ) -> flint.acb:
                w = two_b_over_pi_acb * sigma_lp_acb(xi, p_set) * (flint.acb(da) - alpha_acb(xi))
                z = b_acb * xi
                je = sgn * ne * spherical_bessel_j_acb(2 * ri, z) * spherical_bessel_j_acb(2 * si, z)
                jo = sgn * no * spherical_bessel_j_acb(2 * ri + 1, z) * spherical_bessel_j_acb(2 * si + 1, z)
                return w * (je + flint.acb(0, 1) * jo)

            ie, io = integrate_on_0_to_xi0(int_pair, xi0, tol_exp)
            a_even[r_idx][s_idx] = ie
            a_even[s_idx][r_idx] = ie
            a_odd[r_idx][s_idx] = io
            a_odd[s_idx][r_idx] = io

    tr_e_4 = a_even[0][0] + a_even[1][1] + a_even[2][2] + a_even[3][3]
    tr_o_4 = a_odd[0][0] + a_odd[1][1] + a_odd[2][2] + a_odd[3][3]
    eps_even = tr_e_full - tr_e_4
    eps_odd = tr_o_full - tr_o_4
    assert not (eps_even < flint.arb(0)) and eps_even < flint.arb(10) ** (-10)
    assert not (eps_odd < flint.arb(0)) and eps_odd < flint.arb(10) ** (-10)

    diag_base = c_diag + c_zero * da
    w_sig_e = [[(diag_base if i == j else flint.arb(0)) - a_even[i][j] for j in range(4)] for i in range(4)]
    w_uns_e = [[(diag_base if i == j else flint.arb(0)) - a_even[i][j] for j in range(4)] for i in range(4)]
    w_sig_o = [[(diag_base if i == j else flint.arb(0)) - a_odd[i][j] for j in range(4)] for i in range(4)]
    w_uns_o = [[(diag_base if i == j else flint.arb(0)) - a_odd[i][j] for j in range(4)] for i in range(4)]

    delta_schur_e = [[flint.arb(0) for _ in range(4)] for _ in range(4)]
    delta_schur_o = [[flint.arb(0) for _ in range(4)] for _ in range(4)]

    for _, tau_r, c_r in active_shifts:
        u = tau_r / b_val
        abs_c = arb_abs(c_r)
        sgn_c = flint.arb(1) if c_r > flint.arb(0) else flint.arb(-1)
        for i in range(4):
            for j in range(i, 4):
                se = exact_shift_entry_arb(2 * i, 2 * j, u)
                de = exact_support_entry_any_parity_arb(2 * i, 2 * j, u)
                so = exact_shift_entry_arb(2 * i + 1, 2 * j + 1, u)
                do = exact_support_entry_any_parity_arb(2 * i + 1, 2 * j + 1, u)

                w_sig_e[i][j] = w_sig_e[i][j] + c_r * se
                w_uns_e[i][j] = w_uns_e[i][j] - abs_c * de
                delta_schur_e[i][j] = delta_schur_e[i][j] + abs_c * (de + sgn_c * se)

                w_sig_o[i][j] = w_sig_o[i][j] + c_r * so
                w_uns_o[i][j] = w_uns_o[i][j] - abs_c * do
                delta_schur_o[i][j] = delta_schur_o[i][j] + abs_c * (do + sgn_c * so)

                if i != j:
                    w_sig_e[j][i] = w_sig_e[i][j]
                    w_uns_e[j][i] = w_uns_e[i][j]
                    delta_schur_e[j][i] = delta_schur_e[i][j]
                    w_sig_o[j][i] = w_sig_o[i][j]
                    w_uns_o[j][i] = w_uns_o[i][j]
                    delta_schur_o[j][i] = delta_schur_o[i][j]

    # Verify Corollary 1.4: W_signed - W_unsigned == Delta_Schur and Delta_Schur > 0 via Cholesky:
    for i in range(4):
        for j in range(4):
            assert (w_sig_e[i][j] - w_uns_e[i][j] - delta_schur_e[i][j]).contains(0)
            assert (w_sig_o[i][j] - w_uns_o[i][j] - delta_schur_o[i][j]).contains(0)
    _ = cholesky_lower_arb(delta_schur_e)
    _ = cholesky_lower_arb(delta_schur_o)

    # Subtract infinite-dimensional Parseval tail eps_even * I_4 and eps_odd * I_4:
    w_sig_tail_e = [
        [(w_sig_e[i][j] - eps_even) if i == j else w_sig_e[i][j] for j in range(4)]
        for i in range(4)
    ]
    w_sig_tail_o = [
        [(w_sig_o[i][j] - eps_odd) if i == j else w_sig_o[i][j] for j in range(4)]
        for i in range(4)
    ]

    lam_lb_e, pivots_e = certify_min_eig_lower_bound_arb(w_sig_tail_e)
    lam_lb_o, pivots_o = certify_min_eig_lower_bound_arb(w_sig_tail_o)

    rayleigh_uns_e, v_uns_e = certify_rayleigh_upper_bound_arb(w_uns_e)
    rayleigh_uns_o, v_uns_o = certify_rayleigh_upper_bound_arb(w_uns_o)

    return {
        "K": len(p_set),
        "N": n_target,
        "a": arb_to_dict(a_val),
        "two_b": arb_to_dict(flint.arb(2) * b_val),
        "n_active_shifts": len(active_shifts),
        "n_two_sided_shifts": n_two_sided,
        "n_single_reflection_shifts": n_single_ref,
        "n_positive_shifts": n_pos_shifts,
        "tail_trace_even": arb_to_dict(eps_even),
        "tail_trace_odd": arb_to_dict(eps_odd),
        "W_signed_tail_even_min_eig_lb": arb_to_dict(lam_lb_e),
        "W_signed_tail_even_cholesky_pivots": [arb_to_dict(p) for p in pivots_e],
        "W_signed_tail_odd_min_eig_lb": arb_to_dict(lam_lb_o),
        "W_signed_tail_odd_cholesky_pivots": [arb_to_dict(p) for p in pivots_o],
        "W_unsigned_even_rayleigh_ub": arb_to_dict(rayleigh_uns_e),
        "W_unsigned_even_witness_v": v_uns_e,
        "W_unsigned_even_is_indefinite": bool(rayleigh_uns_e < flint.arb(0)),
        "W_unsigned_odd_rayleigh_ub": arb_to_dict(rayleigh_uns_o),
        "W_unsigned_odd_witness_v": v_uns_o,
        "W_unsigned_odd_is_indefinite": bool(rayleigh_uns_o < flint.arb(0)),
        "delta_schur_identity_and_pd_certified": True,
    }


def certify_theorem_2_horizon_and_dh(prec_bits: int) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()
    tol_exp = 55 if prec_bits <= 256 else 75

    da_zero = flint.arb(0)
    xi0_zero = find_alpha_root_arb(da_zero)

    # 1. K = 3 ([2, 3, 5], P_3 = 30) across N in {36, 40, 42, 45, 50}:
    p3 = [2, 3, 5]
    c_zero_3, c_diag_3, q_terms_3 = build_q_terms_arb(p3)
    k3_rows: list[dict[str, Any]] = []
    for n_val in [36, 40, 42, 45, 50]:
        row = certify_checkpoint_signed_vs_unsigned(
            p3, n_val, da_zero, xi0_zero, c_zero_3, c_diag_3, q_terms_3, tol_exp
        )
        if n_val >= 40:
            assert row["W_unsigned_even_is_indefinite"], f"Expected unsigned even indefinite at K=3 N={n_val}"
        if n_val >= 45:
            assert row["W_unsigned_odd_is_indefinite"], f"Expected unsigned odd indefinite at K=3 N={n_val}"
        k3_rows.append(row)

    # 2. K = 4 ([2, 3, 5, 7], P_4 = 210) across N in {225, 240, 252, 260, 300, 350, 380}:
    p4 = [2, 3, 5, 7]
    c_zero_4, c_diag_4, q_terms_4 = build_q_terms_arb(p4)
    k4_rows: list[dict[str, Any]] = []
    for n_val in [225, 240, 252, 260, 300, 350, 380]:
        row = certify_checkpoint_signed_vs_unsigned(
            p4, n_val, da_zero, xi0_zero, c_zero_4, c_diag_4, q_terms_4, tol_exp
        )
        if n_val >= 252:
            assert row["W_unsigned_even_is_indefinite"], f"Expected unsigned even indefinite at K=4 N={n_val}"
            assert row["W_unsigned_odd_is_indefinite"], f"Expected unsigned odd indefinite at K=4 N={n_val}"
        k4_rows.append(row)

    # 3. Direct Dirichlet convolution equivalence on K = 3 & Davenport-Heilbronn indefiniteness:
    n_max = 60
    lam_zeta = [flint.arb(0)] * (n_max + 1)
    for p in ALL_PRIMES:
        if p > n_max:
            break
        pk = p
        while pk <= n_max:
            lam_zeta[pk] = flint.arb(p).log()
            pk *= p

    c_diag_zeta_conv, q_zeta_conv = build_general_dirichlet_q_terms_arb(p3, lam_zeta)
    assert (c_diag_zeta_conv - c_diag_3).contains(0)
    for q_frac, val_3 in q_terms_3.items():
        if Fraction(1, 1) <= q_frac < Fraction(2, 1):
            assert (q_zeta_conv.get(q_frac, flint.arb(0)) - val_3).contains(0)

    five = flint.arb(5)
    sqrt5 = five.sqrt()
    kappa = ((flint.arb(10) - flint.arb(2) * sqrt5).sqrt() - flint.arb(2)) / (sqrt5 - flint.arb(1))
    a_dh = [flint.arb(0)] * (n_max + 1)
    for n in range(1, n_max + 1):
        r_mod = n % 5
        a_dh[n] = [flint.arb(0), flint.arb(1), kappa, -kappa, flint.arb(-1)][r_mod]
    lam_dh = [flint.arb(0)] * (n_max + 1)
    for n in range(2, n_max + 1):
        s_val = a_dh[n] * flint.arb(n).log()
        for d in range(2, n):
            if n % d == 0:
                s_val = s_val - lam_dh[d] * a_dh[n // d]
        lam_dh[n] = s_val

    c_diag_dh_2, _ = build_general_dirichlet_q_terms_arb([2, 3], lam_dh)
    c_diag_dh_3, q_dh_3 = build_general_dirichlet_q_terms_arb(p3, lam_dh)
    assert (c_diag_dh_3 - (flint.arb(6) / flint.arb(5)) * c_diag_dh_2).contains(0)
    assert c_diag_dh_3 < flint.arb(0)

    dh_rows: list[dict[str, Any]] = []
    half = flint.arb(1) / flint.arb(2)
    tiny = flint.arb(2) ** (-200)
    for n_val in [36, 40, 42, 45, 50]:
        b_val = half * (flint.arb(n_val).log() - flint.arb(30).log())
        w_dh_e = [[(c_diag_dh_3 if i == j else flint.arb(0)) for j in range(4)] for i in range(4)]
        w_dh_o = [[(c_diag_dh_3 if i == j else flint.arb(0)) for j in range(4)] for i in range(4)]
        n_sh_dh = 0
        r_dh_horizon = Fraction(n_val, 30)
        for q_frac, c_r in sorted(q_dh_3.items()):
            if Fraction(1, 1) < q_frac < r_dh_horizon and arb_abs(c_r) > tiny:
                tau_r = flint.arb(q_frac.numerator).log() - flint.arb(q_frac.denominator).log()
                n_sh_dh += 1
                u = tau_r / b_val
                for i in range(4):
                    for j in range(i, 4):
                        se = exact_shift_entry_arb(2 * i, 2 * j, u)
                        so = exact_shift_entry_arb(2 * i + 1, 2 * j + 1, u)
                        w_dh_e[i][j] = w_dh_e[i][j] + c_r * se
                        w_dh_o[i][j] = w_dh_o[i][j] + c_r * so
                        if i != j:
                            w_dh_e[j][i] = w_dh_e[i][j]
                            w_dh_o[j][i] = w_dh_o[i][j]

        assert w_dh_e[0][0] < flint.arb(0)
        assert w_dh_o[0][0] < flint.arb(0)
        ray_dh_e, v_dh_e = certify_rayleigh_upper_bound_arb(w_dh_e)
        ray_dh_o, v_dh_o = certify_rayleigh_upper_bound_arb(w_dh_o)
        assert ray_dh_e < flint.arb(0)
        assert ray_dh_o < flint.arb(0)

        dh_rows.append({
            "N": n_val,
            "n_active_shifts_dh": n_sh_dh,
            "W_arith_DH_even_00": arb_to_dict(w_dh_e[0][0]),
            "W_arith_DH_odd_00": arb_to_dict(w_dh_o[0][0]),
            "W_arith_DH_even_rayleigh_ub": arb_to_dict(ray_dh_e),
            "W_arith_DH_even_witness_v": v_dh_e,
            "W_arith_DH_odd_rayleigh_ub": arb_to_dict(ray_dh_o),
            "W_arith_DH_odd_witness_v": v_dh_o,
        })

    return {
        "prec_bits": prec_bits,
        "xi0_da_zero": arb_to_dict(xi0_zero),
        "c_diag_zeta_K3": arb_to_dict(c_diag_3),
        "c_diag_zeta_K4": arb_to_dict(c_diag_4),
        "c_diag_DH_K2": arb_to_dict(c_diag_dh_2),
        "c_diag_DH_K3": arb_to_dict(c_diag_dh_3),
        "dirichlet_convolution_matches_euler_tower_K3": True,
        "K3_signed_vs_unsigned_checkpoints": k3_rows,
        "K4_signed_vs_unsigned_checkpoints": k4_rows,
        "K3_davenport_heilbronn_checkpoints": dh_rows,
        "elapsed_s": round(time.time() - t0, 4),
    }


def verify_two_precision_overlaps(res_256: dict[str, Any], res_384: dict[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check_pair(label: str, d256: dict[str, Any], d384: dict[str, Any]) -> None:
        b256 = flint.arb(d256["str"])
        b384 = flint.arb(d384["str"])
        ov = bool(b256.overlaps(b384))
        assert ov, f"Two-precision overlap failed for {label}: {b256} vs {b384}"
        checks.append({
            "label": label,
            "overlaps": ov,
            "rad_256": d256["rad"],
            "rad_384": d384["rad"],
        })

    for c256, c384 in zip(
        res_256["theorem_1"]["u_grid_certificates"],
        res_384["theorem_1"]["u_grid_certificates"],
    ):
        u_lbl = c256["u_label"]
        check_pair(f"T1_u_{u_lbl}_Qpos_even_p3", c256["Q_pos_even_cholesky_pivots"][3], c384["Q_pos_even_cholesky_pivots"][3])
        check_pair(f"T1_u_{u_lbl}_Qpos_odd_p3", c256["Q_pos_odd_cholesky_pivots"][3], c384["Q_pos_odd_cholesky_pivots"][3])
        check_pair(f"T1_u_{u_lbl}_Qneg_even_p2", c256["Q_neg_even_3x3_cholesky_pivots"][2], c384["Q_neg_even_3x3_cholesky_pivots"][2])
        check_pair(f"T1_u_{u_lbl}_Qneg_odd_p3", c256["Q_neg_odd_cholesky_pivots"][3], c384["Q_neg_odd_cholesky_pivots"][3])

    check_pair("T2_xi0_da_zero", res_256["theorem_2"]["xi0_da_zero"], res_384["theorem_2"]["xi0_da_zero"])
    check_pair("T2_c_diag_DH_K3", res_256["theorem_2"]["c_diag_DH_K3"], res_384["theorem_2"]["c_diag_DH_K3"])

    for r256, r384 in zip(
        res_256["theorem_2"]["K3_signed_vs_unsigned_checkpoints"],
        res_384["theorem_2"]["K3_signed_vs_unsigned_checkpoints"],
    ):
        n_val = r256["N"]
        check_pair(f"T2_K3_N{n_val}_tail_even", r256["tail_trace_even"], r384["tail_trace_even"])
        check_pair(f"T2_K3_N{n_val}_tail_odd", r256["tail_trace_odd"], r384["tail_trace_odd"])
        check_pair(f"T2_K3_N{n_val}_sig_even_p3", r256["W_signed_tail_even_cholesky_pivots"][3], r384["W_signed_tail_even_cholesky_pivots"][3])
        check_pair(f"T2_K3_N{n_val}_sig_odd_p3", r256["W_signed_tail_odd_cholesky_pivots"][3], r384["W_signed_tail_odd_cholesky_pivots"][3])
        check_pair(f"T2_K3_N{n_val}_uns_even_ray", r256["W_unsigned_even_rayleigh_ub"], r384["W_unsigned_even_rayleigh_ub"])

    for r256, r384 in zip(
        res_256["theorem_2"]["K4_signed_vs_unsigned_checkpoints"],
        res_384["theorem_2"]["K4_signed_vs_unsigned_checkpoints"],
    ):
        n_val = r256["N"]
        check_pair(f"T2_K4_N{n_val}_tail_even", r256["tail_trace_even"], r384["tail_trace_even"])
        check_pair(f"T2_K4_N{n_val}_tail_odd", r256["tail_trace_odd"], r384["tail_trace_odd"])
        check_pair(f"T2_K4_N{n_val}_sig_even_p3", r256["W_signed_tail_even_cholesky_pivots"][3], r384["W_signed_tail_even_cholesky_pivots"][3])
        check_pair(f"T2_K4_N{n_val}_sig_odd_p3", r256["W_signed_tail_odd_cholesky_pivots"][3], r384["W_signed_tail_odd_cholesky_pivots"][3])
        check_pair(f"T2_K4_N{n_val}_uns_even_ray", r256["W_unsigned_even_rayleigh_ub"], r384["W_unsigned_even_rayleigh_ub"])

    for r256, r384 in zip(
        res_256["theorem_2"]["K3_davenport_heilbronn_checkpoints"],
        res_384["theorem_2"]["K3_davenport_heilbronn_checkpoints"],
    ):
        n_val = r256["N"]
        check_pair(f"T2_DH_N{n_val}_even_ray", r256["W_arith_DH_even_rayleigh_ub"], r384["W_arith_DH_even_rayleigh_ub"])
        check_pair(f"T2_DH_N{n_val}_odd_ray", r256["W_arith_DH_odd_rayleigh_ub"], r384["W_arith_DH_odd_rayleigh_ub"])

    return {
        "total_overlap_checks": len(checks),
        "all_passed": True,
        "checks": checks,
    }


def main() -> None:
    t_start = time.time()
    out_dir = Path(__file__).resolve().parent
    out_path = out_dir / "verification.json"

    res_by_prec: dict[str, Any] = {}
    for prec in (256, 384):
        t1 = certify_theorem_1_reflection_strictness(prec)
        t2 = certify_theorem_2_horizon_and_dh(prec)
        res_by_prec[str(prec)] = {
            "theorem_1": t1,
            "theorem_2": t2,
        }

    overlaps = verify_two_precision_overlaps(res_by_prec["256"], res_by_prec["384"])

    payload: dict[str, Any] = {
        "milestone": "signed-legendre-weil-positivity-beyond-schur-horizon-2026-10-15-v1",
        "lanes": ["WEIL-FLOOR", "NB-GAIN", "COEFF"],
        "wall_check": {
            "proves_RH": False,
            "proves_G2": False,
            "proves_cofinal_lower_bound": False,
            "missing_original_evidence_groups_open": [
                "src/verify_phase2.py",
                "final_weil_check.py",
            ],
        },
        "precisions_bits": [256, 384],
        "results_by_precision": res_by_prec,
        "two_precision_overlap_verification": overlaps,
        "total_elapsed_s": round(time.time() - t_start, 4),
    }

    canonical_bytes = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["sha256"] = hashlib.sha256(canonical_bytes).hexdigest()

    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    file_sha256 = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"Wrote {out_path}")
    print(f"payload.sha256 = {payload['sha256']}")
    print(f"file_sha256    = {file_sha256}")
    print(f"overlap checks = {overlaps['total_overlap_checks']} (all_passed={overlaps['all_passed']})")


if __name__ == "__main__":
    main()
