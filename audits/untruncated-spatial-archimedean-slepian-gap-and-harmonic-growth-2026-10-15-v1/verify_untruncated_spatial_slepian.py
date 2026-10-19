#!/usr/bin/env python3
"""
Milestone 16 Verification & Certificate Script (Repaired per argon-m16-review):
Untruncated Spatial Archimedean Formula, Rational Harmonic & Weber-Schafheitlin
Legendre Asymptotics, Arbitrary-Bandwidth Positivity up to 2b = 2.50 (260 Shifts),
Certified Slepian Exterior-Frequency Leakage, and Conditional 50-Zero Prefix
Diagnostic (WEIL-FLOOR, NB-GAIN / COEFF, & KERNEL-API).

Replays all ball-arithmetic certificates at TWO precisions (256-bit and 384-bit
flint.arb / flint.acb) with zero float tolerances and zero numpy/mpmath imports.

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


# Exact rational near-minimizer test vectors in Q^6 (scaled by 10^12) for
# W_full^(6,even)(b) at K=3 and for E_Slep^(6,even)(b; gamma_1) at 2b in {1.0, 1.5, 2.0}:
V_MIN_RATIONAL_K3: dict[str, list[Fraction]] = {
    "1.0": [
        Fraction(794405048361, 10**12),
        Fraction(-571389337358, 10**12),
        Fraction(202846435670, 10**12),
        Fraction(-35865897389, 10**12),
        Fraction(905327480, 10**12),
        Fraction(992781343, 10**12),
    ],
    "1.5": [
        Fraction(-750746405153, 10**12),
        Fraction(595131681325, 10**12),
        Fraction(-273367542673, 10**12),
        Fraction(84385022771, 10**12),
        Fraction(-18465039926, 10**12),
        Fraction(2552230077, 10**12),
    ],
    "2.0": [
        Fraction(-632550712462, 10**12),
        Fraction(616060249502, 10**12),
        Fraction(-420405682331, 10**12),
        Fraction(200098554275, 10**12),
        Fraction(-59136131244, 10**12),
        Fraction(8480210437, 10**12),
    ],
}

V_SLEP_RATIONAL: dict[str, list[Fraction]] = {
    "1.0": [
        Fraction(803984320851, 10**12),
        Fraction(-559608551226, 10**12),
        Fraction(196612519761, 10**12),
        Fraction(-41907181731, 10**12),
        Fraction(5869913170, 10**12),
        Fraction(-574919137, 10**12),
    ],
    "1.5": [
        Fraction(-754334097965, 10**12),
        Fraction(593667607551, 10**12),
        Fraction(-268224444903, 10**12),
        Fraction(79564740494, 10**12),
        Fraction(-16086668928, 10**12),
        Fraction(2271277430, 10**12),
    ],
    "2.0": [
        Fraction(-736435378814, 10**12),
        Fraction(602188152342, 10**12),
        Fraction(-293007260909, 10**12),
        Fraction(93814675294, 10**12),
        Fraction(-19312698650, 10**12),
        Fraction(2221133904, 10**12),
    ],
}


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


def jacobi_eigvalsh_mid(a_in: list[list[float]], max_sweeps: int = 30) -> list[float]:
    """Pure-Python Jacobi symmetric eigenvalue solver on midpoint matrices (diagnostic display only)."""
    n = len(a_in)
    a = [row[:] for row in a_in]
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
    return sorted(a[i][i] for i in range(n))


def spherical_bessel_j_acb(m: int, z: flint.acb) -> flint.acb:
    double_fact = 1
    for k in range(1, 2 * m + 2, 2):
        double_fact *= k
    b_param = flint.acb(flint.arb(2 * m + 3) / flint.arb(2))
    w_arg = -(z * z) / flint.acb(4)
    hyp = w_arg.hypgeom_0f1(b_param)
    return (z**m) * hyp / flint.acb(double_fact)


def sigma_lp_acb(xi: flint.acb, primes: list[int]) -> flint.acb:
    prod = flint.acb(1)
    for p in primes:
        p_arb = flint.arb(p)
        logp = p_arb.log()
        c_p = flint.acb((p_arb + flint.arb(1)) / p_arb)
        amp_p = flint.acb(flint.arb(2) / p_arb.sqrt())
        prod = prod * (c_p - amp_p * (xi * flint.acb(logp)).cos())
    return prod


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


def legendre_poly_fraction(m: int) -> list[Fraction]:
    if m == 0:
        return [Fraction(1)]
    if m == 1:
        return [Fraction(0), Fraction(1)]
    p_prev = [Fraction(1)]
    p_curr = [Fraction(0), Fraction(1)]
    for k in range(1, m):
        p_next = [Fraction(0) for _ in range(k + 2)]
        for deg, c in enumerate(p_curr):
            p_next[deg + 1] += Fraction(2 * k + 1, k + 1) * c
        for deg, c in enumerate(p_prev):
            p_next[deg] -= Fraction(k, k + 1) * c
        p_prev = p_curr
        p_curr = p_next
    return p_curr


def c_mm_rational_poly(m: int) -> list[Fraction]:
    pm = legendre_poly_fraction(m)
    u_coeffs = [Fraction(0) for _ in range(2 * m + 2)]
    for i, ci in enumerate(pm):
        for k, ck in enumerate(pm):
            binom_kj = Fraction(1)
            for j in range(k + 1):
                if j > 0:
                    binom_kj = binom_kj * Fraction(k - j + 1, j)
                p1 = i + j + 1
                scale = ci * ck * binom_kj / Fraction(p1)
                binom_pr = Fraction(1)
                for r in range(p1 + 1):
                    if r > 0:
                        binom_pr = binom_pr * Fraction(p1 - r + 1, r)
                    sign = 1 if r % 2 == 0 else -1
                    c_u = Fraction(sign) * binom_pr
                    if r == 0:
                        c_u = c_u - Fraction(1 if p1 % 2 == 0 else -1)
                    u_coeffs[k - j + r] = u_coeffs[k - j + r] + scale * c_u
    return [c * Fraction(2 * m + 1, 2) for c in u_coeffs]


def legendre_poly_coeffs(m: int) -> list[flint.arb]:
    return [flint.arb(c.numerator) / flint.arb(c.denominator) for c in legendre_poly_fraction(m)]


def c_mn_poly_u(m: int, n: int) -> list[flint.arb]:
    pm = legendre_poly_coeffs(m)
    pn = legendre_poly_coeffs(n)
    u_coeffs = [flint.arb(0) for _ in range(m + n + 2)]
    for i, ci in enumerate(pm):
        for k, ck in enumerate(pn):
            binom_kj = 1
            for j in range(k + 1):
                if j > 0:
                    binom_kj = (binom_kj * (k - j + 1)) // j
                p1 = i + j + 1
                scale = (ci * ck * flint.arb(binom_kj)) / flint.arb(p1)
                binom_pr = 1
                for r in range(p1 + 1):
                    if r > 0:
                        binom_pr = (binom_pr * (p1 - r + 1)) // r
                    sign = 1 if r % 2 == 0 else -1
                    c_u = flint.arb(sign * binom_pr)
                    if r == 0:
                        c_u = c_u - flint.arb(1 if p1 % 2 == 0 else -1)
                    u_coeffs[k - j + r] = u_coeffs[k - j + r] + scale * c_u
    norm = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt() / flint.arb(2)
    return [c * norm for c in u_coeffs]


def eval_poly_acb(coeffs: list[flint.arb], z: flint.acb) -> flint.acb:
    res = flint.acb(0)
    for c in reversed(coeffs):
        res = res * z + flint.acb(c)
    return res


def eval_poly_arb(coeffs: list[flint.arb], x: flint.arb) -> flint.arb:
    res = flint.arb(0)
    for c in reversed(coeffs):
        res = res * x + c
    return res


def arch_tail_closed(t_end: flint.arb) -> flint.arb:
    w = (-t_end / flint.arb(2)).exp()
    return ((flint.arb(1) + w) / (flint.arb(1) - w)).log() + flint.arb(2) * w.atan()


def exact_spatial_j_mn(
    m: int,
    n: int,
    lam: flint.arb,
    b: flint.arb,
    tol_exp: int,
    poly_cache: dict[tuple[int, int], list[flint.arb]],
) -> flint.arb:
    if (m, n) not in poly_cache:
        poly_cache[(m, n)] = c_mn_poly_u(m, n)
    if (n, m) not in poly_cache:
        poly_cache[(n, m)] = c_mn_poly_u(n, m)
    poly_mn = poly_cache[(m, n)]
    poly_nm = poly_cache[(n, m)]
    poly_u = [(a + b_c) / flint.arb(2) for a, b_c in zip(poly_mn, poly_nm)]
    tol = 2.0 ** (-tol_exp)
    pi = flint.arb.pi()
    psi_14 = flint.acb(flint.arb(1) / flint.arb(4)).digamma().real
    b_acb = flint.acb(b)
    two_b = flint.arb(2) * b
    tiny = flint.arb(2) ** (-200)

    if lam.contains(0):
        phi_0 = poly_u[0]
        q_coeffs = [-c / b for c in poly_u[1:]]

        def int_lam0(t: flint.acb, _: Any) -> flint.acb:
            return (t / flint.acb(2)).exp() * eval_poly_acb(q_coeffs, t / b_acb) / (flint.acb(0, 1) * t).sinc()

        i_main = flint.acb.integral(int_lam0, flint.acb(0), flint.acb(two_b), rel_tol=tol, abs_tol=tol).real
        return (psi_14 - pi.log() + arch_tail_closed(two_b)) * phi_0 + i_main

    if lam > two_b:
        lam_acb = flint.acb(lam)

        def int_large_lam(s: flint.acb, _: Any) -> flint.acb:
            c_val = eval_poly_acb(poly_u, s / b_acb)
            t1 = lam_acb + s
            t2 = lam_acb - s
            k1 = (-t1 / flint.acb(2)).exp() / (flint.acb(1) - (-flint.acb(2) * t1).exp())
            k2 = (-t2 / flint.acb(2)).exp() / (flint.acb(1) - (-flint.acb(2) * t2).exp())
            return -c_val * (k1 + k2)

        return flint.acb.integral(int_large_lam, flint.acb(0), flint.acb(two_b), rel_tol=tol, abs_tol=tol).real

    u0 = lam / b
    d_coeffs = [flint.arb(0) for _ in range(len(poly_u))]
    for k, ck in enumerate(poly_u):
        binom = 1
        for j in range(k + 1):
            if j > 0:
                binom = (binom * (k - j + 1)) // j
            d_coeffs[j] = d_coeffs[j] + ck * flint.arb(binom) * (u0 ** (k - j))
    phi_0 = d_coeffs[0]
    t_end = lam + two_b
    bp1 = lam if lam < (two_b - lam) else (two_b - lam)
    bp2 = (two_b - lam) if lam < (two_b - lam) else lam
    r_coeffs = [flint.arb(0)] + [
        -d_coeffs[j] / b if j % 2 == 0 else flint.arb(0) for j in range(2, len(d_coeffs))
    ]

    def int_sub_a(t: flint.acb, _: Any) -> flint.acb:
        return (t / flint.acb(2)).exp() * eval_poly_acb(r_coeffs, t / b_acb) / (flint.acb(0, 1) * t).sinc()

    i_a = (
        flint.acb.integral(int_sub_a, flint.acb(0), flint.acb(bp1), rel_tol=tol, abs_tol=tol).real
        if bp1 > tiny
        else flint.arb(0)
    )
    lam_acb = flint.acb(lam)
    phi0_acb = flint.acb(phi_0)
    half_acb = flint.acb(flint.arb(1) / flint.arb(2))

    def int_sub_b(t: flint.acb, _: Any) -> flint.acb:
        if lam < two_b - lam:
            p_val = half_acb * (
                eval_poly_acb(poly_u, (t - lam_acb) / b_acb) + eval_poly_acb(poly_u, (t + lam_acb) / b_acb)
            )
        else:
            p_val = half_acb * eval_poly_acb(poly_u, (lam_acb - t) / b_acb)
        return (
            flint.acb(2)
            * (-t / flint.acb(2)).exp()
            * (phi0_acb - p_val)
            / (flint.acb(1) - (-flint.acb(2) * t).exp())
        )

    i_b = (
        flint.acb.integral(int_sub_b, flint.acb(bp1), flint.acb(bp2), rel_tol=tol, abs_tol=tol).real
        if (bp2 - bp1) > tiny
        else flint.arb(0)
    )

    def int_sub_c(t: flint.acb, _: Any) -> flint.acb:
        p_val = half_acb * eval_poly_acb(poly_u, (t - lam_acb) / b_acb)
        return (
            flint.acb(2)
            * (-t / flint.acb(2)).exp()
            * (phi0_acb - p_val)
            / (flint.acb(1) - (-flint.acb(2) * t).exp())
        )

    i_c = flint.acb.integral(int_sub_c, flint.acb(bp2), flint.acb(t_end), rel_tol=tol, abs_tol=tol).real
    return (psi_14 - pi.log() + arch_tail_closed(t_end)) * phi_0 + i_a + i_b + i_c


def build_l_terms(p_set: list[int]) -> dict[Fraction, flint.arb]:
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
    return terms


def build_q_terms_rmax(
    p_set: list[int], r_max: int
) -> tuple[flint.arb, flint.arb, dict[Fraction, flint.arb], dict[Fraction, flint.arb]]:
    primorial = math.prod(p_set)
    c_zero = flint.arb(1)
    gamma_k = flint.arb(0)
    for p in p_set:
        p_arb = flint.arb(p)
        c_zero = c_zero * (flint.arb(1) + flint.arb(1) / p_arb)
        gamma_k = gamma_k + (flint.arb(2) * p_arb.log()) / (p_arb + flint.arb(1))
    c_diag = c_zero * gamma_k
    l_full = build_l_terms(p_set)
    q_terms: dict[Fraction, flint.arb] = {}
    log_prim = flint.arb(primorial).log()
    for r, val in l_full.items():
        q_terms[r] = q_terms.get(r, flint.arb(0)) + log_prim * val
    for idx, p in enumerate(p_set):
        sub_p = p_set[:idx] + p_set[idx + 1 :]
        l_sub = build_l_terms(sub_p)
        w_p = (flint.arb(p - 1) / flint.arb(p)) * flint.arb(p).log()
        for r, val in l_sub.items():
            q_terms[r] = q_terms.get(r, flint.arb(0)) - w_p * val
    limit = primorial * r_max
    is_p = [True] * (limit + 1)
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    for p in range(2, limit + 1):
        if is_p[p] and p not in p_set:
            logp = flint.arb(p).log()
            pk = p
            while pk <= limit:
                w_coeff = -logp / flint.arb(pk).sqrt()
                for r, val in l_full.items():
                    for prod_r in (r * pk, r / Fraction(pk, 1)):
                        if Fraction(1, r_max) < prod_r < Fraction(r_max, 1):
                            q_terms[prod_r] = q_terms.get(prod_r, flint.arb(0)) + val * w_coeff
                pk *= p
    return c_zero, c_diag, l_full, q_terms


def certify_theorem_1_harmonic_growth(
    prec_bits: int, poly_cache: dict[tuple[int, int], list[flint.arb]]
) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()
    tol_exp = 65 if prec_bits <= 256 else 85

    harmonic_rows: list[dict[str, Any]] = []
    h_prev = Fraction(1)
    b_quarter = flint.arb(1) / flint.arb(4)
    b_half = flint.arb(1) / flint.arb(2)
    b_one = flint.arb(1)
    gamma_e = -flint.acb(1).digamma().real
    pi = flint.arb.pi()

    for m in range(10):
        c_poly = c_mm_rational_poly(m)
        assert c_poly[0] == Fraction(1)
        h_m = -sum(c_poly[k] * (Fraction(2) ** k) / Fraction(k) for k in range(1, len(c_poly)))
        h_expected = Fraction(1) + sum(Fraction(4 * k, 4 * k * k - 1) for k in range(1, m + 1))
        assert h_m == h_expected, f"Harmonic identity mismatch at m={m}: {h_m} vs {h_expected}"
        inc = (h_m - h_prev) if m > 0 else Fraction(0)
        if m > 0:
            assert inc == Fraction(4 * m, 4 * m * m - 1)
        h_prev = h_m

        # Exact Weber-Schafheitlin inverse-square Bessel moment and zero-mean identity for m >= 1:
        zero_mean_int = sum(
            c_poly[k] * (Fraction(2) ** (k + 1)) / Fraction(k + 1) for k in range(len(c_poly))
        )
        inv_sq_moment = -sum(
            c_poly[k] * (Fraction(2) ** (k + 2)) / Fraction(k + 2) for k in range(len(c_poly))
        )
        if m >= 1:
            assert zero_mean_int == Fraction(0), f"Non-zero mean for m={m}: {zero_mean_int}"
            expected_ws = Fraction(2, (2 * m - 1) * (2 * m + 3))
            assert inv_sq_moment == expected_ws, f"Weber-Schafheitlin mismatch at m={m}: {inv_sq_moment}"

        j_2b05 = exact_spatial_j_mn(m, m, flint.arb(0), b_quarter, tol_exp, poly_cache)
        j_2b10 = exact_spatial_j_mn(m, m, flint.arb(0), b_half, tol_exp, poly_cache)
        j_2b20 = exact_spatial_j_mn(m, m, flint.arb(0), b_one, tol_exp, poly_cache)
        if m >= 1:
            assert j_2b05 > flint.arb(0)
        if m >= 2:
            assert j_2b10 > flint.arb(0)
        if m >= 3:
            assert j_2b20 > flint.arb(0)

        hm_arb = flint.arb(h_m.numerator) / flint.arb(h_m.denominator)
        asymp_0_2b10 = hm_arb - gamma_e - (flint.arb(4) * pi * b_half).log()
        asymp_1_2b10 = (
            asymp_0_2b10 - (b_half * b_half) / flint.arb(12 * (2 * m - 1) * (2 * m + 3))
            if m >= 1
            else asymp_0_2b10
        )
        err_asymp_0_2b10 = j_2b10 - asymp_0_2b10
        err_asymp_1_2b10 = j_2b10 - asymp_1_2b10
        if m == 9:
            assert arb_abs(err_asymp_0_2b10) < flint.arb("6e-5")
            assert arb_abs(err_asymp_1_2b10) < flint.arb("3e-8")

        harmonic_rows.append({
            "m": m,
            "H_m_rational": f"{h_m.numerator}/{h_m.denominator}",
            "H_m_float": float(h_m),
            "increment_rational": f"{inc.numerator}/{inc.denominator}" if m > 0 else "0",
            "weber_schafheitlin_inv_sq_rational": (
                f"{inv_sq_moment.numerator}/{inv_sq_moment.denominator}" if m >= 1 else "N/A"
            ),
            "J_mm_2b_0_50": arb_to_dict(j_2b05),
            "J_mm_2b_1_00": arb_to_dict(j_2b10),
            "J_mm_2b_2_00": arb_to_dict(j_2b20),
            "asymp_log4pib_2b_1_00": arb_to_dict(asymp_0_2b10),
            "asymp_ws_refined_2b_1_00": arb_to_dict(asymp_1_2b10),
            "err_asymp_log4pib_2b_1_00": arb_to_dict(err_asymp_0_2b10),
            "err_asymp_ws_refined_2b_1_00": arb_to_dict(err_asymp_1_2b10),
        })

    for m in range(1, 10):
        b10_curr = flint.arb(harmonic_rows[m]["J_mm_2b_1_00"]["str"])
        b10_prev = flint.arb(harmonic_rows[m - 1]["J_mm_2b_1_00"]["str"])
        assert b10_curr > b10_prev

    return {
        "prec_bits": prec_bits,
        "harmonic_legendre_identities": harmonic_rows,
        "all_ten_rational_identities_exact": True,
        "all_nine_weber_schafheitlin_identities_exact": True,
        "strict_monotonic_diagonal_growth_certified": True,
        "elapsed_s": round(time.time() - t0, 4),
    }


def certify_slepian_exterior_matrix(
    b_val: flint.arb,
    gamma1: flint.arb,
    tol_exp: int,
    poly_cache: dict[tuple[int, int], list[flint.arb]],
) -> list[list[flint.arb]]:
    """
    Compute the exact 6x6 Slepian exterior-frequency matrix E_Slep^(6,even)(b; gamma1)
    on V_6^even(-b, b) in flint.arb via the spatial sinc integral:
      (E_Slep)_{i,j} = delta_{i,j} - (2 b gamma1 / pi) int_0^2 C_{2i,2j}(u b) sinc(b gamma1 u) du.
    """
    n_leg = 6
    c_slep = b_val * gamma1
    c_acb = flint.acb(c_slep)
    pi = flint.arb.pi()
    tol = 2.0 ** (-tol_exp)
    e_mat = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
    for i in range(n_leg):
        for j in range(i, n_leg):
            p_ij = poly_cache[(2 * i, 2 * j)]
            p_ji = poly_cache[(2 * j, 2 * i)]
            poly_u = [(a + b_c) / flint.arb(2) for a, b_c in zip(p_ij, p_ji)]

            def integrand(u: flint.acb, _: Any) -> flint.acb:
                return eval_poly_acb(poly_u, u) * (c_acb * u).sinc()

            k_ij = (flint.arb(2) * c_slep / pi) * (
                flint.acb.integral(integrand, flint.acb(0), flint.acb(2), rel_tol=tol, abs_tol=tol).real
            )
            e_ij = (flint.arb(1) if i == j else flint.arb(0)) - k_ij
            e_mat[i][j] = e_ij
            e_mat[j][i] = e_ij
    return e_mat


def certify_theorem_2_and_3(
    prec_bits: int, poly_cache: dict[tuple[int, int], list[flint.arb]]
) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()
    tol_exp = 60 if prec_bits <= 256 else 80

    # 1. Verify Proposition 2.1: All-bandwidth internal prime-tower telescoping up to R_max = 6 for K = 3:
    p3 = [2, 3, 5]
    _, _, l_full_3, q_eul_6 = build_q_terms_rmax(p3, 6)
    lam_zeta = [flint.arb(0) for _ in range(181)]
    for p in range(2, 181):
        if all(p % d != 0 for d in range(2, int(p**0.5) + 1)):
            pk = p
            while pk <= 180:
                lam_zeta[pk] = flint.arb(p).log()
                pk *= p
    q_conv_6: dict[Fraction, flint.arb] = {}
    tiny = flint.arb(2) ** (-200)
    for r, l_val in l_full_3.items():
        for n in range(2, 181):
            if arb_abs(lam_zeta[n]) > tiny:
                w_n = -lam_zeta[n] / flint.arb(n).sqrt()
                for q in (r * n, r / Fraction(n, 1)):
                    if Fraction(1, 6) < q < Fraction(6, 1):
                        q_conv_6[q] = q_conv_6.get(q, flint.arb(0)) + l_val * w_n

    all_keys_6 = sorted(set(q_eul_6.keys()) | set(q_conv_6.keys()))
    n_checked_6 = 0
    for q in all_keys_6:
        if Fraction(1, 1) <= q < Fraction(6, 1):
            n_checked_6 += 1
            diff = q_eul_6.get(q, flint.arb(0)) - q_conv_6.get(q, flint.arb(0))
            assert diff.contains(0), f"Tower telescoping mismatch at q={q}: {diff}"

    # 2. Certified FLINT interval enclosures of the first 50 critical-line zeros of zeta(s):
    gammas = [flint.acb.zeta_zero(k).imag for k in range(1, 51)]
    gamma1 = gammas[0]
    assert gamma1 > flint.arb("14.134725") and gamma1 < flint.arb("14.134726")

    family_results: dict[str, list[dict[str, Any]]] = {}
    slepian_duality_rows: list[dict[str, Any]] = []

    for label, p_set in [("K2", [2, 3]), ("K3", [2, 3, 5])]:
        _, c_diag, l_full, q_terms = build_q_terms_rmax(p_set, 15)
        l_pos = [
            (
                r,
                flint.arb(r.numerator).log() - flint.arb(r.denominator).log(),
                val if r == Fraction(1, 1) else flint.arb(2) * val,
            )
            for r, val in sorted(l_full.items())
            if r >= Fraction(1, 1)
        ]

        rows: list[dict[str, Any]] = []
        for tb_str in ["0.5", "1.0", "1.5", "2.0", "2.5"]:
            two_b = flint.arb(tb_str)
            b_val = two_b / flint.arb(2)
            n_leg = 6
            w_e = [[(c_diag if i == j else flint.arb(0)) for j in range(n_leg)] for i in range(n_leg)]
            w_o = [[(c_diag if i == j else flint.arb(0)) for j in range(n_leg)] for i in range(n_leg)]

            for i in range(n_leg):
                for j in range(i, n_leg):
                    ae = flint.arb(0)
                    ao = flint.arb(0)
                    for _, lam_r, w_r in l_pos:
                        ae = ae + w_r * exact_spatial_j_mn(2 * i, 2 * j, lam_r, b_val, tol_exp, poly_cache)
                        ao = ao + w_r * exact_spatial_j_mn(2 * i + 1, 2 * j + 1, lam_r, b_val, tol_exp, poly_cache)
                    w_e[i][j] = w_e[i][j] + ae
                    w_o[i][j] = w_o[i][j] + ao
                    if i != j:
                        w_e[j][i] = w_e[i][j]
                        w_o[j][i] = w_o[i][j]

            n_sh = 0
            for r, c_r in sorted(q_terms.items()):
                if r > Fraction(1, 1):
                    tau_r = flint.arb(r.numerator).log() - flint.arb(r.denominator).log()
                    if (tau_r - two_b).contains(0) or arb_abs(tau_r - two_b) < tiny:
                        continue
                    if tau_r < two_b and arb_abs(c_r) > tiny:
                        n_sh += 1
                        u = tau_r / b_val
                        for i in range(n_leg):
                            for j in range(i, n_leg):
                                se = flint.arb(2) * eval_poly_arb(poly_cache[(2 * i, 2 * j)], u)
                                so = flint.arb(2) * eval_poly_arb(poly_cache[(2 * i + 1, 2 * j + 1)], u)
                                w_e[i][j] = w_e[i][j] + c_r * se
                                w_o[i][j] = w_o[i][j] + c_r * so
                                if i != j:
                                    w_e[j][i] = w_e[i][j]
                                    w_o[j][i] = w_o[i][j]

            # Exact flint.arb Cholesky certification on full 6x6 even and odd matrices:
            l_e6 = cholesky_lower_arb(w_e)
            l_o6 = cholesky_lower_arb(w_o)

            mid_e = [[float(w_e[i][j].mid()) for j in range(n_leg)] for i in range(n_leg)]
            mid_o = [[float(w_o[i][j].mid()) for j in range(n_leg)] for i in range(n_leg)]

            rows.append({
                "two_b": arb_to_dict(two_b),
                "n_active_shifts": n_sh,
                "even_6x6_cholesky_pivots": [arb_to_dict(l_e6[i][i]) for i in range(n_leg)],
                "odd_6x6_cholesky_pivots": [arb_to_dict(l_o6[i][i]) for i in range(n_leg)],
                "even_min_eig_N2_4_6": [
                    jacobi_eigvalsh_mid([row[:d] for row in mid_e[:d]])[0] for d in (2, 4, 6)
                ],
                "odd_min_eig_N2_4_6": [
                    jacobi_eigvalsh_mid([row[:d] for row in mid_o[:d]])[0] for d in (2, 4, 6)
                ],
            })

            if label == "K3" and tb_str in ("1.0", "1.5", "2.0"):
                v_min = [
                    flint.arb(frac.numerator) / flint.arb(frac.denominator)
                    for frac in V_MIN_RATIONAL_K3[tb_str]
                ]
                v_norm_sq = sum((v * v for v in v_min), flint.arb(0))
                num_rq = flint.arb(0)
                for i in range(n_leg):
                    for j in range(n_leg):
                        num_rq = num_rq + v_min[i] * w_e[i][j] * v_min[j]
                rq_prime_arch = num_rq / v_norm_sq
                assert rq_prime_arch > flint.arb(0)

                # Exact flint.arb Slepian exterior-frequency matrix E_Slep^(6,even)(b; gamma1):
                e_slep = certify_slepian_exterior_matrix(b_val, gamma1, tol_exp, poly_cache)
                l_slep = cholesky_lower_arb(e_slep)
                v_slep = [
                    flint.arb(frac.numerator) / flint.arb(frac.denominator)
                    for frac in V_SLEP_RATIONAL[tb_str]
                ]
                v_slep_norm_sq = sum((v * v for v in v_slep), flint.arb(0))
                slep_min_rq = (
                    sum((v_slep[i] * e_slep[i][j] * v_slep[j] for i in range(n_leg) for j in range(n_leg)), flint.arb(0))
                    / v_slep_norm_sq
                )
                slep_on_vmin = (
                    sum((v_min[i] * e_slep[i][j] * v_min[j] for i in range(n_leg) for j in range(n_leg)), flint.arb(0))
                    / v_norm_sq
                )
                assert slep_min_rq > flint.arb(0)
                assert slep_on_vmin > flint.arb(0)

                zero_sum_50 = flint.arb(0)
                for g_k in gammas:
                    sig_k = sigma_lp_acb(flint.acb(g_k), p_set).real
                    g_hat = flint.arb(0)
                    for r in range(n_leg):
                        sgn = flint.arb(1 if r % 2 == 0 else -1)
                        norm_fac = (flint.arb(2) * b_val * flint.arb(4 * r + 1)).sqrt()
                        jr = spherical_bessel_j_acb(2 * r, flint.acb(b_val * g_k)).real
                        g_hat = g_hat + v_min[r] * sgn * norm_fac * jr
                    zero_sum_50 = zero_sum_50 + flint.arb(2) * sig_k * (g_hat * g_hat) / v_norm_sq

                ratio_50 = zero_sum_50 / rq_prime_arch
                assert ratio_50 > flint.arb("0.85") and ratio_50 < flint.arb("1.0")

                slepian_duality_rows.append({
                    "two_b": arb_to_dict(two_b),
                    "space_bandwidth_c": arb_to_dict(b_val * gamma1),
                    "slepian_exterior_leakage_min_rq": arb_to_dict(slep_min_rq),
                    "slepian_exterior_leakage_on_vmin": arb_to_dict(slep_on_vmin),
                    "slepian_last_cholesky_pivot": arb_to_dict(l_slep[5][5]),
                    "prime_arch_rayleigh_quotient": arb_to_dict(rq_prime_arch),
                    "explicit_50_zero_sum": arb_to_dict(zero_sum_50),
                    "capture_ratio_50_zeros": arb_to_dict(ratio_50),
                })

        family_results[label] = rows

    return {
        "prec_bits": prec_bits,
        "tower_telescoping_checked_keys_in_1_to_6": n_checked_6,
        "tower_telescoping_zero_discrepancies": True,
        "zeta_zeros_source": "flint.acb.zeta_zero(k).imag (certified interval enclosure)",
        "gamma_1": arb_to_dict(gamma1),
        "gamma_50": arb_to_dict(gammas[49]),
        "untruncated_6x6_positivity_by_family": family_results,
        "slepian_zero_gap_duality": slepian_duality_rows,
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

    for r256, r384 in zip(
        res_256["theorem_1"]["harmonic_legendre_identities"],
        res_384["theorem_1"]["harmonic_legendre_identities"],
    ):
        m = r256["m"]
        check_pair(f"T1_m{m}_J_2b_0_5", r256["J_mm_2b_0_50"], r384["J_mm_2b_0_50"])
        check_pair(f"T1_m{m}_J_2b_1_0", r256["J_mm_2b_1_00"], r384["J_mm_2b_1_00"])
        check_pair(f"T1_m{m}_J_2b_2_0", r256["J_mm_2b_2_00"], r384["J_mm_2b_2_00"])
        check_pair(
            f"T1_m{m}_err_ws_2b_1_0",
            r256["err_asymp_ws_refined_2b_1_00"],
            r384["err_asymp_ws_refined_2b_1_00"],
        )

    check_pair("T23_gamma_1", res_256["theorem_2_and_3"]["gamma_1"], res_384["theorem_2_and_3"]["gamma_1"])
    check_pair("T23_gamma_50", res_256["theorem_2_and_3"]["gamma_50"], res_384["theorem_2_and_3"]["gamma_50"])

    for fam in ("K2", "K3"):
        for r256, r384 in zip(
            res_256["theorem_2_and_3"]["untruncated_6x6_positivity_by_family"][fam],
            res_384["theorem_2_and_3"]["untruncated_6x6_positivity_by_family"][fam],
        ):
            tb = r256["two_b"]["mid"]
            check_pair(
                f"T2_{fam}_2b_{tb}_even_p5",
                r256["even_6x6_cholesky_pivots"][5],
                r384["even_6x6_cholesky_pivots"][5],
            )
            check_pair(
                f"T2_{fam}_2b_{tb}_odd_p5",
                r256["odd_6x6_cholesky_pivots"][5],
                r384["odd_6x6_cholesky_pivots"][5],
            )

    for s256, s384 in zip(
        res_256["theorem_2_and_3"]["slepian_zero_gap_duality"],
        res_384["theorem_2_and_3"]["slepian_zero_gap_duality"],
    ):
        tb = s256["two_b"]["mid"]
        check_pair(f"T3_2b_{tb}_c", s256["space_bandwidth_c"], s384["space_bandwidth_c"])
        check_pair(
            f"T3_2b_{tb}_slep_min_rq",
            s256["slepian_exterior_leakage_min_rq"],
            r384_d := s384["slepian_exterior_leakage_min_rq"],
        )
        _ = r384_d
        check_pair(
            f"T3_2b_{tb}_slep_on_vmin",
            s256["slepian_exterior_leakage_on_vmin"],
            s384["slepian_exterior_leakage_on_vmin"],
        )
        check_pair(f"T3_2b_{tb}_rq", s256["prime_arch_rayleigh_quotient"], s384["prime_arch_rayleigh_quotient"])
        check_pair(f"T3_2b_{tb}_zsum", s256["explicit_50_zero_sum"], s384["explicit_50_zero_sum"])
        check_pair(f"T3_2b_{tb}_ratio", s256["capture_ratio_50_zeros"], s384["capture_ratio_50_zeros"])

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
        flint.ctx.prec = prec
        poly_cache: dict[tuple[int, int], list[flint.arb]] = {}
        t1 = certify_theorem_1_harmonic_growth(prec, poly_cache)
        t23 = certify_theorem_2_and_3(prec, poly_cache)
        res_by_prec[str(prec)] = {
            "theorem_1": t1,
            "theorem_2_and_3": t23,
        }

    overlaps = verify_two_precision_overlaps(res_by_prec["256"], res_by_prec["384"])

    payload: dict[str, Any] = {
        "milestone": "untruncated-spatial-archimedean-slepian-gap-and-harmonic-growth-2026-10-15-v1",
        "lanes": ["WEIL-FLOOR", "NB-GAIN", "COEFF", "KERNEL-API"],
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
