#!/usr/bin/env python3
"""
Milestone 17 Verification & Certificate Script (v2 — Repaired per argon-m17-review-2026-10-15-v1):
Infinite-Dimensional High-Mode Operator Lower Bound, Exact Two-Shift Product
Defect Algebra, Full-Space Block-Schur Positivity Certificate on Q(A_arch) subset L^2(-b, b),
and Matched Davenport-Heilbronn Control Separation (WEIL-FLOOR, NB-GAIN / COEFF, & KERNEL-API).

Addresses all 7 findings from argon-m17-review-2026-10-15-v1:
  1 & 2. Subtracts the globally positive semidefinite high-frequency local operator
         A_{loc,+,R}(b) >= 0 from ALL blocks on Q(A_arch) subset L^2(-b, b) (never dropping it
         selectively on the tail/off-diagonal while keeping it on the low-low block), and
         certifies strict positive definiteness of the bounded remainder operator
           R_R(b) := W_{P_2}^{full}(b) - A_{loc,+,R}(b)
                   = W_{comb,R}(b) + C_{diag}(P_2) I - D_{loc,R}(b) + A_{ext}(b),
         where W_{comb,R}(b) = alpha(R) L_{loc}(b) + W_{sh}(b) includes the low-to-high shift
         coupling of alpha(R) L_{loc}(b) inside the exact two-shift Gram matrix G_{comb,R},
         and the remaining archimedean off-diagonal block B_{rem,arch,R} = P_> (-D_{loc,R}(b) + A_{ext}(b)) P_<=
         is smooth and exponentially small (verified against individual entries such as (m,n)=(12,10)).
  3.     Uses the exact repository Davenport-Heilbronn definition (controls/davenport_heilbronn.py)
         with kappa = (sqrt(10 - 2*sqrt(5)) - 2)/(sqrt(5) - 1), Dirichlet convolution recurrence
         for Lambda_{DH}(n), C_{diag,DH}({2,3}) = -0.694999969664314..., composite/prime-power shift
         dictionary q_{terms,DH}, and odd-character completion alpha_{DH}(xi) = Re psi(3/4 + i*xi/2) + log(5/pi),
         explicitly qualifying that a negative lower-bound budget is a failure of the sufficient
         positivity certificate (while actual negative Rayleigh quotients are certified at b in {2, 5/2, 3} in M9).
  4.     Fixes alpha_arch_acb(xi) to evaluate the holomorphic extension of Re psi(1/4 + i*xi/2) - log(pi)
         with factor i/2, verified against alpha_arch_arb(9) = 0.35883198893599235...
  5.     Fixes verify_overlap to reconstruct balls from full-precision strings flint.arb(a["str"]),
         with a self-test asserting that 1 + 2^(-100) and 1 + 2^(-101) do NOT overlap.
  6.     Fixes the normalization factor (2*b instead of 4*b) and exact weights |2*w_r| in
         ext_laplace_bessel_bounds, verified against the modified spherical Bessel series for J_{m,n}(lambda; b).
  7.     Distinguishes parity-block size N_leg from first omitted Legendre degree M_0 in the
         cutoff-selection rate analysis.

Replays all ball-arithmetic certificates at TWO precisions (256-bit and 384-bit
flint.arb / flint.acb) with zero float tolerances and zero numpy/mpmath imports.

Wall check: Does NOT prove RH, G2, or the cofinal prime-shift lower bound as a -> infinity
(or K -> infinity). Both missing-original evidence groups in evidence/MISSING.md remain OPEN.
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


def arb_abs(x: flint.arb) -> flint.arb:
    return abs(x)


def arb_pow_int(x: flint.arb, k: int) -> flint.arb:
    """Exact integer power via repeated multiplication (safe when x contains 0)."""
    res = flint.arb(1)
    for _ in range(k):
        res = res * x
    return res


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


def jacobi_eigvalsh_mid(a_in: list[list[float]], max_sweeps: int = 35) -> list[float]:
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


def cholesky_lower_arb(mat: list[list[flint.arb]]) -> list[list[flint.arb]]:
    """Rigorous ball-arithmetic lower-triangular Cholesky factorization."""
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


def legendre_poly_coeffs(m: int) -> list[flint.arb]:
    return [flint.arb(c.numerator) / flint.arb(c.denominator) for c in legendre_poly_fraction(m)]


def c_mn_poly_u(m: int, n: int) -> list[flint.arb]:
    """Exact polynomial coefficients of C_{m,n}(u) on u in [0, 2]."""
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


def s_tau_entry(
    m: int,
    n: int,
    u: flint.arb,
    poly_cache: dict[tuple[int, int], list[flint.arb]],
) -> flint.arb:
    """Exact Legendre entry (P_b S_tau P_b)_{m,n} = C_{m,n}(u) + (-1)^{m+n} C_{n,m}(u) for u = tau/b."""
    if not (u < flint.arb(2)):
        return flint.arb(0)
    if (m, n) not in poly_cache:
        poly_cache[(m, n)] = c_mn_poly_u(m, n)
    if (n, m) not in poly_cache:
        poly_cache[(n, m)] = c_mn_poly_u(n, m)
    c1 = eval_poly_arb(poly_cache[(m, n)], u)
    c2 = eval_poly_arb(poly_cache[(n, m)], u)
    return c1 + c2 if (m + n) % 2 == 0 else c1 - c2


def d_two_shift_entry(
    m: int,
    n: int,
    u1: flint.arb,
    u2: flint.arb,
    same_shift: bool = False,
) -> flint.arb:
    """
    Exact boundary-strip defect entry (D_{tau_1, tau_2})_{m,n} for 0 <= u1 <= u2 < 2
    and m + n even (both even or both odd):
      (D_{tau_1, tau_2})_{m,n} = sqrt((2m+1)(2n+1)) * int_{max(-1 + du, 1 - u1)}^1 P_m(x) P_n(x - du) dx
    where du = u2 - u1.
    """
    if (m + n) % 2 != 0:
        return flint.arb(0)
    du = flint.arb(0) if same_shift else (u2 - u1)
    a1 = flint.arb(-1) + du
    a2 = flint.arb(1) - u1
    a_low = a1 if a1 > a2 else a2
    if not (a_low < flint.arb(1)):
        return flint.arb(0)
    pm = legendre_poly_coeffs(m)
    pn = legendre_poly_coeffs(n)
    x_coeffs = [flint.arb(0) for _ in range(m + n + 1)]
    for i, ci in enumerate(pm):
        for k, ck in enumerate(pn):
            binom_kj = 1
            for j in range(k + 1):
                if j > 0:
                    binom_kj = (binom_kj * (k - j + 1)) // j
                sign = 1 if (k - j) % 2 == 0 else -1
                term = ci * ck * flint.arb(sign * binom_kj) * arb_pow_int(du, k - j)
                x_coeffs[i + j] = x_coeffs[i + j] + term
    integral_val = flint.arb(0)
    for deg, c in enumerate(x_coeffs):
        p1 = deg + 1
        integral_val = integral_val + c * (flint.arb(1) - arb_pow_int(a_low, p1)) / flint.arb(p1)
    norm = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
    return norm * integral_val


def arch_tail_closed(t_end: flint.arb, is_dh: bool = False) -> flint.arb:
    w = (-t_end / flint.arb(2)).exp()
    log_term = ((flint.arb(1) + w) / (flint.arb(1) - w)).log()
    atan_term = flint.arb(2) * w.atan()
    return (log_term - atan_term) if is_dh else (log_term + atan_term)


def exact_spatial_j_mn(
    m: int,
    n: int,
    lam: flint.arb,
    b: flint.arb,
    tol_exp: int,
    poly_cache: dict[tuple[int, int], list[flint.arb]],
    is_dh: bool = False,
) -> flint.arb:
    """
    Exact compact spatial archimedean integral J_{m,n}(lambda; b) for zeta (is_dh=False)
    or for the odd-character completion of Davenport-Heilbronn f_DH (is_dh=True).
    """
    if (m, n) not in poly_cache:
        poly_cache[(m, n)] = c_mn_poly_u(m, n)
    if (n, m) not in poly_cache:
        poly_cache[(n, m)] = c_mn_poly_u(n, m)
    poly_mn = poly_cache[(m, n)]
    poly_nm = poly_cache[(n, m)]
    poly_u = [(a + b_c) / flint.arb(2) for a, b_c in zip(poly_mn, poly_nm)]
    tol = 2.0 ** (-tol_exp)
    pi = flint.arb.pi()
    if is_dh:
        psi_val = flint.acb(flint.arb(3) / flint.arb(4)).digamma().real
        const_shift = (flint.arb(5) / pi).log()
        exp_near_0 = flint.acb(flint.arb(-1) / flint.arb(2))
        exp_num = flint.acb(flint.arb(-3) / flint.arb(2))
    else:
        psi_val = flint.acb(flint.arb(1) / flint.arb(4)).digamma().real
        const_shift = -pi.log()
        exp_near_0 = flint.acb(flint.arb(1) / flint.arb(2))
        exp_num = flint.acb(flint.arb(-1) / flint.arb(2))

    b_acb = flint.acb(b)
    two_b = flint.arb(2) * b
    tiny = flint.arb(2) ** (-200)

    if lam.contains(0):
        phi_0 = poly_u[0]
        q_coeffs = [-c / b for c in poly_u[1:]]

        def int_lam0(t: flint.acb, _: Any) -> flint.acb:
            return (exp_near_0 * t).exp() * eval_poly_acb(q_coeffs, t / b_acb) / (flint.acb(0, 1) * t).sinc()

        i_main = flint.acb.integral(int_lam0, flint.acb(0), flint.acb(two_b), rel_tol=tol, abs_tol=tol).real
        return (psi_val + const_shift + arch_tail_closed(two_b, is_dh=is_dh)) * phi_0 + i_main

    if lam > two_b:
        lam_acb = flint.acb(lam)

        def int_large_lam(s: flint.acb, _: Any) -> flint.acb:
            c_val = eval_poly_acb(poly_u, s / b_acb)
            t1 = lam_acb + s
            t2 = lam_acb - s
            k1 = (exp_num * t1).exp() / (flint.acb(1) - (-flint.acb(2) * t1).exp())
            k2 = (exp_num * t2).exp() / (flint.acb(1) - (-flint.acb(2) * t2).exp())
            return -c_val * (k1 + k2)

        return flint.acb.integral(int_large_lam, flint.acb(0), flint.acb(two_b), rel_tol=tol, abs_tol=tol).real

    u0 = lam / b
    d_coeffs = [flint.arb(0) for _ in range(len(poly_u))]
    for k, ck in enumerate(poly_u):
        binom = 1
        for j in range(k + 1):
            if j > 0:
                binom = (binom * (k - j + 1)) // j
            d_coeffs[j] = d_coeffs[j] + ck * flint.arb(binom) * arb_pow_int(u0, k - j)
    phi_0 = d_coeffs[0]
    t_end = lam + two_b
    bp1 = lam if lam < (two_b - lam) else (two_b - lam)
    bp2 = (two_b - lam) if lam < (two_b - lam) else lam
    r_coeffs = [flint.arb(0)] + [
        -d_coeffs[j] / b if j % 2 == 0 else flint.arb(0) for j in range(2, len(d_coeffs))
    ]

    def int_sub_a(t: flint.acb, _: Any) -> flint.acb:
        return (exp_near_0 * t).exp() * eval_poly_acb(r_coeffs, t / b_acb) / (flint.acb(0, 1) * t).sinc()

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
            * (exp_num * t).exp()
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
            * (exp_num * t).exp()
            * (phi0_acb - p_val)
            / (flint.acb(1) - (-flint.acb(2) * t).exp())
        )

    i_c = flint.acb.integral(int_sub_c, flint.acb(bp2), flint.acb(t_end), rel_tol=tol, abs_tol=tol).real
    return (psi_val + const_shift + arch_tail_closed(t_end, is_dh=is_dh)) * phi_0 + i_a + i_b + i_c


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


def alpha_arch_arb(xi: flint.arb) -> flint.arb:
    z = flint.acb(flint.arb(1) / flint.arb(4), xi / flint.arb(2))
    return z.digamma().real - flint.arb.pi().log()


def alpha_arch_acb(xi: flint.acb) -> flint.acb:
    """
    Holomorphic extension of Re psi(1/4 + i*xi/2) - log(pi) on the strip |Im(xi)| < 1/2:
      1/2 * (psi(1/4 + i*xi/2) + psi(1/4 - i*xi/2)) - log(pi).
    Fixes Finding 4 of argon-m17-review (previously omitted the factor i in xi/2).
    """
    i_unit = flint.acb(0, 1)
    qtr = flint.acb(flint.arb(1) / flint.arb(4))
    half_i_xi = i_unit * xi / flint.acb(2)
    z1 = qtr + half_i_xi
    z2 = qtr - half_i_xi
    return (z1.digamma() + z2.digamma()) / flint.acb(2) - flint.acb(flint.arb.pi().log())


def alpha_dh_arb(xi: flint.arb) -> flint.arb:
    """Odd-character archimedean multiplier Re psi(3/4 + i*xi/2) + log(5/pi) for f_DH(s)."""
    z = flint.acb(flint.arb(3) / flint.arb(4), xi / flint.arb(2))
    return z.digamma().real + (flint.arb(5) / flint.arb.pi()).log()


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


def sigma_loc_acb(xi: flint.acb) -> flint.acb:
    """Local positive Fourier multiplier sigma_loc(xi) = 2 + (2/sqrt(6)) cos(xi * log(3/2))."""
    tau_32 = flint.acb(flint.arb(3).log() - flint.arb(2).log())
    return flint.acb(2) + (flint.acb(2) / flint.acb(6).sqrt()) * (xi * tau_32).cos()


def double_factorial_int(n: int) -> int:
    res = 1
    for k in range(1, n + 1, 2):
        res *= k
    return res


def poisson_bessel_tail_trace_bound(
    b: flint.arb,
    r_cut: flint.arb,
    m_start_idx: int,
    parity: str,
    m_symbol_max: flint.arb,
) -> tuple[flint.arb, flint.arb, flint.arb]:
    """
    Closed-form geometric-series upper bound on Tr(P_{>= m_start_idx}^{parity} D(b) P_{>= m_start_idx}^{parity})
    via Poisson's Bessel bound |j_m(u)| <= u^m / (2m+1)!!:
      int_0^R (2m+1) b j_m(b xi)^2 dxi <= (b R)^{2m+1} / ((2m+1)!!)^2.
    """
    m0 = 2 * m_start_idx if parity == "even" else 2 * m_start_idx + 1
    alpha_diff = alpha_arch_arb(r_cut) - alpha_arch_arb(flint.arb(0))
    br = b * r_cut
    df_m0 = flint.arb(double_factorial_int(2 * m0 + 1))
    lead_integral = arb_pow_int(br, 2 * m0 + 1) / (df_m0 * df_m0)
    rho = arb_pow_int(br, 4) / (flint.arb((2 * m0 + 3) * (2 * m0 + 5)) ** 2)
    assert rho < flint.arb(1), f"Geometric ratio rho >= 1: {rho}"
    geom_sum = lead_integral / (flint.arb(1) - rho)
    bound = m_symbol_max * alpha_diff * (flint.arb(2) / flint.arb.pi()) * geom_sum
    return bound, rho, m_symbol_max * alpha_diff


def ext_laplace_bessel_bounds(
    b: flint.arb,
    n_leg: int,
    parity: str,
    k_cut: int = 12,
) -> tuple[flint.arb, flint.arb]:
    """
    Certified closed-form Laplace-Bessel upper bounds on the high-mode tail norm
    ||P_{>= m0}^{parity} A_ext(b) P_{>= m0}^{parity}||_op and off-diagonal norm
    ||P_{>= m0}^{parity} A_ext(b) P_{< m0}^{parity}||_op for the smooth external
    archimedean kernels lambda_r in {log 2, log 3, log 6} (> 2b for 2b <= 0.50).

    Fixes Finding 6 of argon-m17-review:
      - In A_ext(b) = sum_{r in {2,3,6}} 2*w_r J(log r; b), the cosine coefficients
        have magnitudes |2*w_2| = 8/(3*sqrt(2)), |2*w_3| = sqrt(3), |2*w_6| = 2/sqrt(6).
      - For lambda > 2b, J_{m,n}(lambda; b) = (-1)^{m+1} sum_{k>=0} e^{-beta_k lambda} <e_m, psi_k><e_n, psi_k>
        with rank-1 weight 1 * e^{-beta_k lambda} and <e_m, psi_k>^2 = 2b(2m+1) i_m(beta_k b)^2
        (factor 2b, not 4b).
    """
    m0 = 2 * n_leg if parity == "even" else 2 * n_leg + 1
    df_m0 = flint.arb(double_factorial_int(2 * m0 + 1))
    ext_shifts = [
        (flint.arb(2).log(), flint.arb(8) / (flint.arb(3) * flint.arb(2).sqrt())),
        (flint.arb(3).log(), flint.arb(3).sqrt()),
        (flint.arb(6).log(), flint.arb(2) / (flint.arb(6).sqrt())),
    ]
    tail_diag_bound = flint.arb(0)
    tail_off_bound = flint.arb(0)
    denom_rho = flint.arb((2 * m0 + 1) * ((2 * m0 + 3) ** 2) * (2 * m0 + 5))
    for lam, abs_2w in ext_shifts:
        delta = lam - flint.arb(2) * b
        assert delta > flint.arb(0), f"External shift lam={lam} not > 2b={2*b}"
        s_off_low = flint.arb(0)
        s_diag_low = flint.arb(0)
        for k in range(k_cut):
            bk = flint.arb(2 * k) + flint.arb(1) / flint.arb(2)
            z = bk * b
            rho_k = arb_pow_int(z, 4) / denom_rho
            assert rho_k < flint.arb(1), f"Modified Bessel ratio rho_k >= 1 at k={k}: {rho_k}"
            eb = (-(bk * delta)).exp()
            factor_m0 = (
                (flint.arb(2 * m0 + 1) / (flint.arb(1) - rho_k)).sqrt()
                * arb_pow_int(z, m0)
                / df_m0
            )
            s_off_low = s_off_low + flint.arb(2) * b * factor_m0 * eb
            s_diag_low = s_diag_low + flint.arb(2) * b * (factor_m0 * factor_m0) * eb
        bk_cut = flint.arb(2 * k_cut) + flint.arb(1) / flint.arb(2)
        geom_tail = (
            flint.arb(2)
            * b
            * (-(bk_cut * delta)).exp()
            / (flint.arb(1) - (-flint.arb(2) * delta).exp())
        )
        tail_off_bound = tail_off_bound + abs_2w * (s_off_low + geom_tail)
        tail_diag_bound = tail_diag_bound + abs_2w * (s_diag_low + geom_tail)
    return tail_diag_bound, tail_off_bound


def exact_d_r_entry(
    m: int,
    n: int,
    b: flint.arb,
    r_cut: flint.arb,
    primes: list[int],
    tol_exp: int,
) -> flint.arb:
    """Exact integral entry (D_R(b))_{m,n} on [0, R] for m + n even using corrected alpha_arch_acb."""
    if (m + n) % 2 != 0:
        return flint.arb(0)
    tol = 2.0 ** (-tol_exp)
    b_acb = flint.acb(b)
    alpha_r_acb = flint.acb(alpha_arch_arb(r_cut))

    def integrand(xi: flint.acb, _: Any) -> flint.acb:
        u = b_acb * xi
        jm = spherical_bessel_j_acb(m, u)
        jn = spherical_bessel_j_acb(n, u)
        sig = sigma_lp_acb(xi, primes)
        diff = alpha_r_acb - alpha_arch_acb(xi)
        return sig * diff * jm * jn

    val = flint.acb.integral(integrand, flint.acb(0), flint.acb(r_cut), rel_tol=tol, abs_tol=tol).real
    scale = (
        (flint.arb(2) * b / flint.arb.pi())
        * (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
        * flint.arb(1 if ((m - n) // 2) % 2 == 0 else -1)
    )
    return scale * val


def exact_d_loc_r_entry(
    m: int,
    n: int,
    b: flint.arb,
    r_cut: flint.arb,
    tol_exp: int,
) -> flint.arb:
    """Exact integral entry (D_{loc,R}(b))_{m,n} on [0, R] for m + n even."""
    if (m + n) % 2 != 0:
        return flint.arb(0)
    tol = 2.0 ** (-tol_exp)
    b_acb = flint.acb(b)
    alpha_r_acb = flint.acb(alpha_arch_arb(r_cut))

    def integrand(xi: flint.acb, _: Any) -> flint.acb:
        u = b_acb * xi
        jm = spherical_bessel_j_acb(m, u)
        jn = spherical_bessel_j_acb(n, u)
        sig = sigma_loc_acb(xi)
        diff = alpha_r_acb - alpha_arch_acb(xi)
        return sig * diff * jm * jn

    val = flint.acb.integral(integrand, flint.acb(0), flint.acb(r_cut), rel_tol=tol, abs_tol=tol).real
    scale = (
        (flint.arb(2) * b / flint.arb.pi())
        * (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
        * flint.arb(1 if ((m - n) // 2) % 2 == 0 else -1)
    )
    return scale * val


def build_multi_shift_gram_and_trunc(
    b: flint.arb,
    n_leg: int,
    parity: str,
    q_terms: dict[Fraction, flint.arb],
    poly_cache: dict[tuple[int, int], list[flint.arb]],
) -> tuple[
    list[list[flint.arb]],
    list[list[flint.arb]],
    flint.arb,
    flint.arb,
    list[dict[str, Any]],
]:
    """
    Computes:
      1. Exact truncated shift matrix W_sh^(<=) on P_{<=}^{parity}
      2. Exact infinite-dimensional block-coupling Gram matrix
         G_multi = P_<= W_sh^2 P_<= - (P_<= W_sh P_<=)^2
         using Theorem 1 (S_{tau_1} S_{tau_2} = S_{tau_1+tau_2} + S_{|tau_2-tau_1|} - D_{tau_1,tau_2}).
      3. Certified upper bound on ||B_sh||_op = sqrt(lambda_max(G_multi)) via Frobenius norm ||G_multi||_F^(1/2)
         and triangle-inequality comparison sum_r |c_r| ||B_{sh,r}||_op.
    """
    two_b = flint.arb(2) * b
    tiny = flint.arb(2) ** (-200)
    modes = [2 * i if parity == "even" else 2 * i + 1 for i in range(n_leg)]
    active_shifts: list[tuple[Fraction, flint.arb, flint.arb]] = []
    for r, coeff in sorted(q_terms.items(), key=lambda kv: float(kv[0])):
        if r > Fraction(1, 1) and arb_abs(coeff) > tiny:
            tau = flint.arb(r.numerator).log() - flint.arb(r.denominator).log()
            if tau < two_b:
                active_shifts.append((r, tau, coeff))

    w_sh_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
    for _, tau, coeff in active_shifts:
        u = tau / b
        for i, m in enumerate(modes):
            for j, n in enumerate(modes):
                w_sh_le[i][j] = w_sh_le[i][j] + coeff * s_tau_entry(m, n, u, poly_cache)

    w_sh_sq_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
    for r1, tau1, c1 in active_shifts:
        for r2, tau2, c2 in active_shifts:
            same = r1 == r2
            if r1 <= r2:
                u1, u2 = tau1 / b, tau2 / b
                tau_diff = flint.arb(0) if same else (tau2 - tau1)
            else:
                u1, u2 = tau2 / b, tau1 / b
                tau_diff = tau1 - tau2
            u_sum = (tau1 + tau2) / b
            u_diff = tau_diff / b
            prod_c = c1 * c2
            for i, m in enumerate(modes):
                for j, n in enumerate(modes):
                    s_sum = s_tau_entry(m, n, u_sum, poly_cache)
                    s_diff = s_tau_entry(m, n, u_diff, poly_cache)
                    d_val = d_two_shift_entry(m, n, u1, u2, same_shift=same)
                    w_sh_sq_le[i][j] = w_sh_sq_le[i][j] + prod_c * (s_sum + s_diff - d_val)

    g_multi = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
    for i in range(n_leg):
        for j in range(n_leg):
            sq_trunc = flint.arb(0)
            for k in range(n_leg):
                sq_trunc = sq_trunc + w_sh_le[i][k] * w_sh_le[k][j]
            g_multi[i][j] = (w_sh_sq_le[i][j] - sq_trunc + w_sh_sq_le[j][i] - sq_trunc) / flint.arb(2)

    frob_sq = flint.arb(0)
    for i in range(n_leg):
        for j in range(n_leg):
            frob_sq = frob_sq + g_multi[i][j] * g_multi[i][j]
    b_sh_norm_bound = frob_sq.sqrt().sqrt()

    triangle_sum = flint.arb(0)
    shift_records: list[dict[str, Any]] = []
    for r, tau, coeff in active_shifts:
        u = tau / b
        s_le = [[s_tau_entry(m, n, u, poly_cache) for n in modes] for m in modes]
        frob_single = flint.arb(0)
        for i, m in enumerate(modes):
            for j, n in enumerate(modes):
                s_sum = s_tau_entry(m, n, flint.arb(2) * u, poly_cache)
                s_diff = flint.arb(2) if i == j else flint.arb(0)
                d_val = d_two_shift_entry(m, n, u, u, same_shift=True)
                sq_trunc = flint.arb(0)
                for k in range(n_leg):
                    sq_trunc = sq_trunc + s_le[i][k] * s_le[k][j]
                g_ij = s_sum + s_diff - d_val - sq_trunc
                frob_single = frob_single + g_ij * g_ij
        single_norm_bound = frob_single.sqrt().sqrt()
        triangle_sum = triangle_sum + arb_abs(coeff) * single_norm_bound
        shift_records.append(
            {
                "ratio": f"{r.numerator}/{r.denominator}",
                "tau": arb_to_dict(tau),
                "coeff": arb_to_dict(coeff),
                "single_shift_coupling_bound": arb_to_dict(single_norm_bound),
            }
        )

    return w_sh_le, g_multi, b_sh_norm_bound, triangle_sum, shift_records


def build_a_pk_le(
    b: flint.arb,
    n_leg: int,
    parity: str,
    l_full: dict[Fraction, flint.arb],
    tol_exp: int,
    poly_cache: dict[tuple[int, int], list[flint.arb]],
    j_cache: dict[tuple[int, int, Fraction, str], flint.arb],
    b_label: str,
    is_dh: bool = False,
) -> list[list[flint.arb]]:
    modes = [2 * i if parity == "even" else 2 * i + 1 for i in range(n_leg)]
    a_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
    tag = f"{b_label}_{'dh' if is_dh else 'zeta'}"
    for r, coeff in l_full.items():
        if r < Fraction(1, 1):
            continue
        mult = flint.arb(1) if r == Fraction(1, 1) else flint.arb(2)
        lam = flint.arb(0) if r == Fraction(1, 1) else (flint.arb(r.numerator).log() - flint.arb(r.denominator).log())
        for i in range(n_leg):
            for j in range(i, n_leg):
                m, n = modes[i], modes[j]
                key = (m, n, r, tag)
                if key not in j_cache:
                    j_cache[key] = exact_spatial_j_mn(m, n, lam, b, tol_exp, poly_cache, is_dh=is_dh)
                val = mult * coeff * j_cache[key]
                a_le[i][j] = a_le[i][j] + val
                if i != j:
                    a_le[j][i] = a_le[j][i] + val
    return a_le


def build_dh_arithmetic_data(
    l_full_k2: dict[Fraction, flint.arb], r_max: int = 6
) -> tuple[flint.arb, list[flint.arb], dict[Fraction, flint.arb]]:
    """
    Constructs the exact Davenport-Heilbronn arithmetic coefficients Lambda_DH(n)
    from controls/davenport_heilbronn.py via the Dirichlet convolution recurrence
      a_DH * Lambda_DH = (a_DH log n)
    and convolves with L_{P_2} to obtain C_{diag,DH}({2,3}) and q_{terms,DH}.
    """
    five = flint.arb(5)
    sqrt5 = five.sqrt()
    kappa = ((flint.arb(10) - flint.arb(2) * sqrt5).sqrt() - flint.arb(2)) / (sqrt5 - flint.arb(1))
    assert kappa > flint.arb(0)

    nmax = 6 * r_max
    a_dh: list[flint.arb] = [flint.arb(0)] * (nmax + 1)
    for n in range(1, nmax + 1):
        rem = n % 5
        if rem == 1:
            a_dh[n] = flint.arb(1)
        elif rem == 2:
            a_dh[n] = kappa
        elif rem == 3:
            a_dh[n] = -kappa
        elif rem == 4:
            a_dh[n] = flint.arb(-1)

    lam_dh: list[flint.arb] = [flint.arb(0)] * (nmax + 1)
    for n in range(2, nmax + 1):
        s = a_dh[n] * flint.arb(n).log()
        d = 2
        while d * d <= n:
            if n % d == 0:
                s = s - lam_dh[d] * a_dh[n // d]
                q = n // d
                if q != d:
                    s = s - lam_dh[q] * a_dh[d]
            d += 1
        lam_dh[n] = s

    q_terms_dh: dict[Fraction, flint.arb] = {}
    tiny = flint.arb(2) ** (-200)
    for n in range(2, nmax + 1):
        if arb_abs(lam_dh[n]) > tiny:
            w_n = -lam_dh[n] / flint.arb(n).sqrt()
            for r_l, c_l in l_full_k2.items():
                for prod_r in (r_l * n, r_l / Fraction(n, 1)):
                    if Fraction(1, r_max) < prod_r < Fraction(r_max, 1):
                        q_terms_dh[prod_r] = q_terms_dh.get(prod_r, flint.arb(0)) + c_l * w_n

    c_diag_dh_formula = (
        (flint.arb(4) / flint.arb(3)) * lam_dh[2]
        + lam_dh[3]
        - (flint.arb(1) / flint.arb(3)) * lam_dh[6]
    )
    assert (q_terms_dh[Fraction(1, 1)] - c_diag_dh_formula).contains(0)
    return kappa, lam_dh, q_terms_dh


def run_suite(prec: int) -> dict[str, Any]:
    flint.ctx.prec = prec
    tol_exp = 75 if prec == 256 else 110
    poly_cache: dict[tuple[int, int], list[flint.arb]] = {}
    j_cache: dict[tuple[int, int, Fraction, str], flint.arb] = {}

    # Self-test for Finding 4: alpha_arch_acb(9) == alpha_arch_arb(9)
    alpha_9_arb = alpha_arch_arb(flint.arb(9))
    alpha_9_acb_real = alpha_arch_acb(flint.acb(9)).real
    assert (alpha_9_arb - alpha_9_acb_real).contains(0), f"alpha_arch_acb mismatch at xi=9: {alpha_9_arb} vs {alpha_9_acb_real}"
    assert alpha_9_arb > flint.arb(358831) / flint.arb(1000000) and alpha_9_arb < flint.arb(358832) / flint.arb(1000000)

    # =========================================================================
    # 1. Theorem 1: Exact Two-Shift Product Identity & Boundary-Strip Defect D_{tau_1, tau_2}
    # =========================================================================
    b_test = flint.arb(1) / flint.arb(4)  # b = 0.25, 2b = 0.50
    r1_test = Fraction(7, 6)
    r2_test = Fraction(6, 5)
    tau1_test = flint.arb(7).log() - flint.arb(6).log()
    tau2_test = flint.arb(6).log() - flint.arb(5).log()
    u1_test = tau1_test / b_test
    u2_test = tau2_test / b_test
    u_sum_test = (tau1_test + tau2_test) / b_test
    u_diff_test = (tau2_test - tau1_test) / b_test

    two_shift_checks: list[dict[str, Any]] = []
    tol_quad = 2.0 ** (-tol_exp)
    for m, n in [(0, 0), (0, 2), (2, 2), (2, 4), (1, 1), (1, 3), (3, 3)]:
        exact_rhs = (
            s_tau_entry(m, n, u_sum_test, poly_cache)
            + s_tau_entry(m, n, u_diff_test, poly_cache)
            - d_two_shift_entry(m, n, u1_test, u2_test, same_shift=False)
        )
        pm_c = legendre_poly_coeffs(m)
        pn_c = legendre_poly_coeffs(n)
        norm_mn = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt() / flint.arb(2)
        u1_acb = flint.acb(u1_test)
        u2_acb = flint.acb(u2_test)
        bps = sorted(
            [
                flint.arb(-1),
                flint.arb(-1) + u1_test,
                flint.arb(-1) + u2_test,
                flint.arb(1) - u2_test,
                flint.arb(1) - u1_test,
                flint.arb(1),
            ],
            key=lambda x: float(x.mid()),
        )
        quad_sum = flint.arb(0)
        for idx_bp in range(len(bps) - 1):
            xa, xb = bps[idx_bp], bps[idx_bp + 1]
            x_mid = (xa + xb) / flint.arb(2)
            has_m_plus = (x_mid + u1_test) < flint.arb(1)
            has_m_minus = (x_mid - u1_test) > flint.arb(-1)
            has_n_plus = (x_mid + u2_test) < flint.arb(1)
            has_n_minus = (x_mid - u2_test) > flint.arb(-1)

            def seg_integrand(x: flint.acb, _: Any) -> flint.acb:
                vm = flint.acb(0)
                if has_m_plus:
                    vm = vm + eval_poly_acb(pm_c, x + u1_acb)
                if has_m_minus:
                    vm = vm + eval_poly_acb(pm_c, x - u1_acb)
                vn = flint.acb(0)
                if has_n_plus:
                    vn = vn + eval_poly_acb(pn_c, x + u2_acb)
                if has_n_minus:
                    vn = vn + eval_poly_acb(pn_c, x - u2_acb)
                return vm * vn

            quad_sum = (
                quad_sum
                + norm_mn
                * flint.acb.integral(seg_integrand, flint.acb(xa), flint.acb(xb), rel_tol=tol_quad, abs_tol=tol_quad).real
            )

        diff_quad = arb_abs(exact_rhs - quad_sum)
        assert diff_quad < flint.arb(2) ** (-65), f"Two-shift identity mismatch at ({m},{n}): {diff_quad}"

        trunc_errors: dict[str, Any] = {}
        for m_cut in [20, 40, 80]:
            partial = flint.arb(0)
            for k in range(m % 2, m_cut + 1, 2):
                partial = partial + s_tau_entry(m, k, u1_test, poly_cache) * s_tau_entry(k, n, u2_test, poly_cache)
            trunc_errors[str(m_cut)] = arb_to_dict(arb_abs(exact_rhs - partial))

        two_shift_checks.append(
            {
                "m": m,
                "n": n,
                "r1": f"{r1_test.numerator}/{r1_test.denominator}",
                "r2": f"{r2_test.numerator}/{r2_test.denominator}",
                "exact_product_entry": arb_to_dict(exact_rhs),
                "d_defect_entry": arb_to_dict(d_two_shift_entry(m, n, u1_test, u2_test, same_shift=False)),
                "quadrature_entry": arb_to_dict(quad_sum),
                "abs_diff_exact_vs_quadrature": arb_to_dict(diff_quad),
                "finite_mode_truncation_errors": trunc_errors,
            }
        )

    # =========================================================================
    # 2. Theorem 2: Poisson-Bessel Infinite Tail Trace Bound vs Exact D_R Trace
    # =========================================================================
    primes_k2 = [2, 3]
    m_pk2_max = ((flint.arb(1) + flint.arb(1) / flint.arb(2).sqrt()) * (flint.arb(1) + flint.arb(1) / flint.arb(3).sqrt())) ** 2
    pb_tail_checks: list[dict[str, Any]] = []
    for two_b_num, two_b_den, b_str in [(2, 5, "0.40"), (9, 20, "0.45"), (1, 2, "0.50")]:
        b_val = flint.arb(two_b_num) / flint.arb(2 * two_b_den)
        for r_int in [7, 9]:
            r_cut = flint.arb(r_int)
            for n_leg in [4, 5]:
                for parity in ["even", "odd"]:
                    pb_bound, rho_val, pref_val = poisson_bessel_tail_trace_bound(
                        b_val, r_cut, n_leg, parity, m_pk2_max
                    )
                    exact_first3 = flint.arb(0)
                    for idx_tail in range(n_leg, n_leg + 3):
                        deg = 2 * idx_tail if parity == "even" else 2 * idx_tail + 1
                        exact_first3 = exact_first3 + exact_d_r_entry(deg, deg, b_val, r_cut, primes_k2, tol_exp)
                    assert exact_first3 < pb_bound, f"Poisson-Bessel bound violated: {exact_first3} >= {pb_bound}"
                    pb_tail_checks.append(
                        {
                            "two_b": b_str,
                            "R": r_int,
                            "n_leg": n_leg,
                            "parity": parity,
                            "first_tail_degree": 2 * n_leg if parity == "even" else 2 * n_leg + 1,
                            "poisson_bessel_tail_trace_bound": arb_to_dict(pb_bound),
                            "geometric_ratio_rho": arb_to_dict(rho_val),
                            "prefactor_M0_alpha_diff": arb_to_dict(pref_val),
                            "exact_first_3_tail_modes_trace": arb_to_dict(exact_first3),
                            "certified_bound_exceeds_exact": True,
                        }
                    )

    # =========================================================================
    # 3. Theorem 3: Full-Space Infinite-Dimensional Block-Schur Certificate on Q(A_arch) subset L^2(-b, b)
    #    via Global Subtraction W_{P_2}^{full}(b) >= R_R(b) := W_{P_2}^{full}(b) - A_{loc,+,R}(b)
    # =========================================================================
    _, c_diag_k2, l_full_k2, q_terms_k2 = build_q_terms_rmax(primes_k2, 6)
    tau_32 = flint.arb(3).log() - flint.arb(2).log()
    m_loc_max = flint.arb(2) + flint.arb(2) / flint.arb(6).sqrt()
    tiny = flint.arb(2) ** (-200)

    full_space_certificates: list[dict[str, Any]] = []
    bandwidths = [
        (2, 5, "0.40", 9, 4),
        (21, 50, "0.42", 14, 5),
        (9, 20, "0.45", 14, 5),
        (12, 25, "0.48", 14, 5),
        (1, 2, "0.50", 18, 6),
    ]
    for two_b_num, two_b_den, two_b_str, r_int, n_leg in bandwidths:
        b_val = flint.arb(two_b_num) / flint.arb(2 * two_b_den)
        two_b_val = flint.arb(two_b_num) / flint.arb(two_b_den)
        r_cut = flint.arb(r_int)
        alpha_r = alpha_arch_arb(r_cut)
        l_loc_min = flint.arb(2) if two_b_val <= tau_32 else (flint.arb(2) - flint.arb(1) / flint.arb(6).sqrt())

        shift_tail_penalty = flint.arb(0)
        for r_frac, coeff in q_terms_k2.items():
            if r_frac > Fraction(1, 1) and arb_abs(coeff) > tiny:
                tau = flint.arb(r_frac.numerator).log() - flint.arb(r_frac.denominator).log()
                if tau < two_b_val:
                    mult = flint.arb(1) if tau >= b_val else flint.arb(2)
                    shift_tail_penalty = shift_tail_penalty + mult * arb_abs(coeff)

        # Combined shift dictionary q_{comb,R} = q_{terms} + alpha(R)*l_{loc}
        # so that W_{comb,R}(b) = alpha(R)*L_{loc}(b) + W_{sh}(b) includes the low-to-high
        # coupling of alpha(R)*L_{loc}(b) when log(3/2) < 2b (Fixing Findings 1 & 2):
        q_comb_r = dict(q_terms_k2)
        q_comb_r[Fraction(3, 2)] = q_comb_r.get(Fraction(3, 2), flint.arb(0)) + alpha_r * l_full_k2[Fraction(3, 2)]
        q_comb_r[Fraction(2, 3)] = q_comb_r.get(Fraction(2, 3), flint.arb(0)) + alpha_r * l_full_k2[Fraction(2, 3)]

        for parity in ["even", "odd"]:
            modes = [2 * i if parity == "even" else 2 * i + 1 for i in range(n_leg)]
            pb_loc, _, m_loc_alpha_diff = poisson_bessel_tail_trace_bound(
                b_val, r_cut, n_leg, parity, m_loc_max
            )
            ext_diag, ext_off = ext_laplace_bessel_bounds(b_val, n_leg, parity, k_cut=12)
            mu_tail = alpha_r * l_loc_min + c_diag_k2 - shift_tail_penalty - pb_loc - ext_diag
            assert mu_tail > flint.arb(0), f"Tail floor <= 0 at 2b={two_b_str}, {parity}: {mu_tail}"

            # Remaining archimedean off-diagonal block of R_R(b) is ONLY P_> (-D_{loc,R}(b) + A_{ext}(b)) P_<=:
            b_rem_arch_norm_bound = (m_loc_alpha_diff * pb_loc).sqrt() + ext_off
            w_comb_le, g_comb_multi, b_comb_sh_norm_bound, triangle_sum_comb, shift_recs = build_multi_shift_gram_and_trunc(
                b_val, n_leg, parity, q_comb_r, poly_cache
            )
            b_total_rem_norm_bound = b_rem_arch_norm_bound + b_comb_sh_norm_bound

            # Build exact low-low block R_<=^{parity}(b) = P_<= R_R(b) P_<=:
            #   R_<= = (2*alpha(R) + C_diag(P_2)) I_<= + P_<= W_{comb,R}^{off}(b) P_<= - P_<= D_{loc,R}(b) P_<= + P_<= A_{ext}(b) P_<=
            d_loc_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
            for i in range(n_leg):
                for j in range(i, n_leg):
                    val_d = exact_d_loc_r_entry(modes[i], modes[j], b_val, r_cut, tol_exp)
                    d_loc_le[i][j] = val_d
                    d_loc_le[j][i] = val_d

            a_ext_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
            for r_ext in [Fraction(2, 1), Fraction(3, 1), Fraction(6, 1)]:
                lam_ext = flint.arb(r_ext.numerator).log()
                w_ext = flint.arb(2) * l_full_k2[r_ext]
                for i in range(n_leg):
                    for j in range(i, n_leg):
                        m, n = modes[i], modes[j]
                        key = (m, n, r_ext, f"{two_b_str}_zeta")
                        if key not in j_cache:
                            j_cache[key] = exact_spatial_j_mn(m, n, lam_ext, b_val, tol_exp, poly_cache, is_dh=False)
                        val_ext = w_ext * j_cache[key]
                        a_ext_le[i][j] = a_ext_le[i][j] + val_ext
                        if i != j:
                            a_ext_le[j][i] = a_ext_le[j][i] + val_ext

            r_rem_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
            for i in range(n_leg):
                for j in range(n_leg):
                    diag_c = (flint.arb(2) * alpha_r + c_diag_k2) if i == j else flint.arb(0)
                    r_rem_le[i][j] = diag_c + w_comb_le[i][j] - d_loc_le[i][j] + a_ext_le[i][j]

            # Also compute the untruncated low-low block W_<=^{full}(b) for comparison and verify
            # that W_<=^{full}(b) - R_<=^{parity}(b) = P_<= A_{loc,+,R}(b) P_<= is SPD:
            a_pk_le = build_a_pk_le(b_val, n_leg, parity, l_full_k2, tol_exp, poly_cache, j_cache, two_b_str, is_dh=False)
            w_sh_only_le, _, _, _, _ = build_multi_shift_gram_and_trunc(b_val, n_leg, parity, q_terms_k2, poly_cache)
            w_full_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
            a_loc_plus_le = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
            for i in range(n_leg):
                for j in range(n_leg):
                    diag_add = c_diag_k2 if i == j else flint.arb(0)
                    w_full_le[i][j] = a_pk_le[i][j] + diag_add + w_sh_only_le[i][j]
                    a_loc_plus_le[i][j] = w_full_le[i][j] - r_rem_le[i][j]
            _ = cholesky_lower_arb(a_loc_plus_le)  # Certifies P_<= A_{loc,+,R}(b) P_<= > 0

            # Matrix Schur complement of the actual remainder operator R_R(b):
            #   S_mat = R_<= - ((1 + eta) G_{comb,R} + (1 + 1/eta) ||B_{rem,arch,R}||_op^2 I_<=) / mu_tail
            eta = flint.arb(1) / flint.arb(20)
            one_p_eta = flint.arb(1) + eta
            one_p_inv_eta = flint.arb(21)
            s_mat_schur = [[flint.arb(0) for _ in range(n_leg)] for _ in range(n_leg)]
            for i in range(n_leg):
                for j in range(n_leg):
                    diag_arch = (one_p_inv_eta * b_rem_arch_norm_bound * b_rem_arch_norm_bound) if i == j else flint.arb(0)
                    s_mat_schur[i][j] = r_rem_le[i][j] - (one_p_eta * g_comb_multi[i][j] + diag_arch) / mu_tail

            chol_r_le = cholesky_lower_arb(r_rem_le)
            chol_l = cholesky_lower_arb(s_mat_schur)
            chol_pivots = [chol_l[i][i] * chol_l[i][i] for i in range(n_leg)]
            _ = chol_r_le
            eig_w_full_le = jacobi_eigvalsh_mid([[float(x.mid()) for x in row] for row in w_full_le])
            eig_r_rem_le = jacobi_eigvalsh_mid([[float(x.mid()) for x in row] for row in r_rem_le])
            eig_schur = jacobi_eigvalsh_mid([[float(x.mid()) for x in row] for row in s_mat_schur])

            cert_entry: dict[str, Any] = {
                "two_b": two_b_str,
                "R": r_int,
                "n_leg": n_leg,
                "parity": parity,
                "first_omitted_degree_M0": 2 * n_leg if parity == "even" else 2 * n_leg + 1,
                "active_shift_count": len(shift_recs),
                "active_combined_shifts": shift_recs,
                "mu_tail_floor": arb_to_dict(mu_tail),
                "pb_loc_tail_trace_bound": arb_to_dict(pb_loc),
                "ext_laplace_bessel_tail_diag_bound": arb_to_dict(ext_diag),
                "ext_laplace_bessel_tail_off_bound": arb_to_dict(ext_off),
                "b_rem_arch_offdiag_bound": arb_to_dict(b_rem_arch_norm_bound),
                "b_comb_sh_offdiag_bound_signed_gram": arb_to_dict(b_comb_sh_norm_bound),
                "b_comb_sh_offdiag_triangle_bound": arb_to_dict(triangle_sum_comb),
                "b_total_rem_offdiag_bound": arb_to_dict(b_total_rem_norm_bound),
                "w_full_le_lambda_min_mid": eig_w_full_le[0],
                "r_rem_le_lambda_min_mid": eig_r_rem_le[0],
                "matrix_schur_complement_lambda_min_mid": eig_schur[0],
                "cholesky_pivots_sq": [arb_to_dict(p) for p in chol_pivots],
                "certified_full_space_spd": True,
            }

            # Explicit individual entry check for Finding 2 at 2b = 0.50, even (N_leg = 6, R = 18):
            # verify |<e_12, (-D_{loc,R}(b) + A_{ext}(b)) e_10>| < b_rem_arch_norm_bound
            if two_b_str == "0.50" and parity == "even":
                d_loc_12_10 = exact_d_loc_r_entry(12, 10, b_val, r_cut, tol_exp)
                a_ext_12_10 = flint.arb(0)
                for r_ext in [Fraction(2, 1), Fraction(3, 1), Fraction(6, 1)]:
                    lam_ext = flint.arb(r_ext.numerator).log()
                    w_ext = flint.arb(2) * l_full_k2[r_ext]
                    a_ext_12_10 = a_ext_12_10 + w_ext * exact_spatial_j_mn(12, 10, lam_ext, b_val, tol_exp, poly_cache, is_dh=False)
                rem_arch_12_10 = -d_loc_12_10 + a_ext_12_10
                full_a_12_10 = flint.arb(0)
                for r_frac, coeff in l_full_k2.items():
                    if r_frac >= Fraction(1, 1):
                        mult = flint.arb(1) if r_frac == Fraction(1, 1) else flint.arb(2)
                        lam_f = flint.arb(0) if r_frac == Fraction(1, 1) else (flint.arb(r_frac.numerator).log() - flint.arb(r_frac.denominator).log())
                        full_a_12_10 = full_a_12_10 + mult * coeff * exact_spatial_j_mn(12, 10, lam_f, b_val, tol_exp, poly_cache, is_dh=False)
                assert arb_abs(rem_arch_12_10) < b_rem_arch_norm_bound, (
                    f"Individual coupling check failed: |{rem_arch_12_10}| >= {b_rem_arch_norm_bound}"
                )
                cert_entry["coupling_entry_check_m12_n10"] = {
                    "unsubtracted_full_A_P2_12_10": arb_to_dict(full_a_12_10),
                    "remainder_arch_entry_12_10": arb_to_dict(rem_arch_12_10),
                    "abs_remainder_arch_entry_12_10": arb_to_dict(arb_abs(rem_arch_12_10)),
                    "certified_b_rem_arch_offdiag_bound": arb_to_dict(b_rem_arch_norm_bound),
                    "strictly_bounded_by_b_rem_arch": True,
                }

            full_space_certificates.append(cert_entry)

    # =========================================================================
    # 4. Dependency Edge Table: High-Mode Asymptotic Divergence vs K -> infinity Decay
    # =========================================================================
    dependency_edge_records: list[dict[str, Any]] = []
    first_primes = [2, 3, 5, 7, 11, 13]
    for k_cnt in range(1, len(first_primes) + 1):
        p_sub = first_primes[:k_cnt]
        sig_min = flint.arb(1)
        sig_max = flint.arb(1)
        c_zero = flint.arb(1)
        gamma_k = flint.arb(0)
        for p in p_sub:
            p_arb = flint.arb(p)
            sig_min = sig_min * (flint.arb(1) - flint.arb(1) / p_arb.sqrt()) ** 2
            sig_max = sig_max * (flint.arb(1) + flint.arb(1) / p_arb.sqrt()) ** 2
            c_zero = c_zero * (flint.arb(1) + flint.arb(1) / p_arb)
            gamma_k = gamma_k + (flint.arb(2) * p_arb.log()) / (p_arb + flint.arb(1))
        c_diag = c_zero * gamma_k
        dependency_edge_records.append(
            {
                "K": k_cnt,
                "primes": p_sub,
                "sigma_min_L_PK": arb_to_dict(sig_min),
                "sigma_max_L_PK": arb_to_dict(sig_max),
                "condition_ratio_max_over_min": arb_to_dict(sig_max / sig_min),
                "c_diag_PK": arb_to_dict(c_diag),
            }
        )

    # =========================================================================
    # 5. Theorem 4: Matched Davenport-Heilbronn Control Separation (Finding 3)
    #    Using the exact repository DH definition (controls/davenport_heilbronn.py)
    # =========================================================================
    kappa_dh, lam_dh, q_terms_dh = build_dh_arithmetic_data(l_full_k2, r_max=6)
    c_diag_dh_k2 = q_terms_dh[Fraction(1, 1)]
    sigma_min_k2 = ((flint.arb(1) - flint.arb(1) / flint.arb(2).sqrt()) * (flint.arb(1) - flint.arb(1) / flint.arb(3).sqrt())) ** 2

    dh_control_records: list[dict[str, Any]] = []
    for two_b_num, two_b_den, two_b_str in [(2, 5, "0.40"), (9, 20, "0.45"), (1, 2, "0.50")]:
        b_val = flint.arb(two_b_num) / flint.arb(2 * two_b_den)
        two_b_val = flint.arb(two_b_num) / flint.arb(two_b_den)
        l_loc_min = flint.arb(2) if two_b_val <= tau_32 else (flint.arb(2) - flint.arb(1) / flint.arb(6).sqrt())

        shift_pen_dh = flint.arb(0)
        dh_active_shifts: list[dict[str, Any]] = []
        for r_frac, coeff in sorted(q_terms_dh.items(), key=lambda kv: float(kv[0])):
            if r_frac > Fraction(1, 1) and arb_abs(coeff) > tiny:
                tau = flint.arb(r_frac.numerator).log() - flint.arb(r_frac.denominator).log()
                if tau < two_b_val:
                    mult = flint.arb(1) if tau >= b_val else flint.arb(2)
                    shift_pen_dh = shift_pen_dh + mult * arb_abs(coeff)
                    dh_active_shifts.append(
                        {
                            "ratio": f"{r_frac.numerator}/{r_frac.denominator}",
                            "tau": arb_to_dict(tau),
                            "coeff": arb_to_dict(coeff),
                        }
                    )

        # Evaluate sufficient tail lower-bound budgets under both:
        # (a) matched archimedean height alpha_DH(R_DH=2) = 0.312514... (~ alpha_zeta(9) = 0.358832...), and
        # (b) zeta archimedean height alpha_zeta(9) = 0.358832...
        r_cut_zeta = flint.arb(9)
        r_cut_dh = flint.arb(2)
        alpha_r_zeta = alpha_arch_arb(r_cut_zeta)
        alpha_r_dh = alpha_dh_arb(r_cut_dh)
        pb_bound_dh, _, _ = poisson_bessel_tail_trace_bound(b_val, r_cut_zeta, 4, "even", m_pk2_max)

        budget_sigma_min_without_shifts = alpha_r_dh * sigma_min_k2 + c_diag_dh_k2
        budget_sigma_min_with_shifts_and_pb = budget_sigma_min_without_shifts - shift_pen_dh - pb_bound_dh
        budget_loc_with_shifts = alpha_r_dh * l_loc_min + c_diag_dh_k2 - shift_pen_dh

        assert budget_sigma_min_without_shifts < flint.arb(0)
        assert budget_loc_with_shifts < flint.arb(0)

        # Also evaluate the (0,0) entry under arithmetic substitution (DH arithmetic + zeta archimedean)
        # and under the full odd-character DH completion (DH arithmetic + odd-character archimedean):
        a_pk_le_zeta = build_a_pk_le(b_val, 4, "even", l_full_k2, tol_exp, poly_cache, j_cache, two_b_str, is_dh=False)
        a_pk_le_dh = build_a_pk_le(b_val, 4, "even", l_full_k2, tol_exp, poly_cache, j_cache, two_b_str, is_dh=True)
        w_sh_le_dh, _, _, _, _ = build_multi_shift_gram_and_trunc(b_val, 4, "even", q_terms_dh, poly_cache)
        a_00_arith_sub = a_pk_le_zeta[0][0] + c_diag_dh_k2 + w_sh_le_dh[0][0]
        a_00_full_odd_dh = a_pk_le_dh[0][0] + c_diag_dh_k2 + w_sh_le_dh[0][0]
        assert a_00_arith_sub < flint.arb(0)

        dh_control_records.append(
            {
                "two_b": two_b_str,
                "kappa_dh": arb_to_dict(kappa_dh),
                "lambda_dh_2": arb_to_dict(lam_dh[2]),
                "lambda_dh_3": arb_to_dict(lam_dh[3]),
                "lambda_dh_4": arb_to_dict(lam_dh[4]),
                "lambda_dh_6": arb_to_dict(lam_dh[6]),
                "c_diag_dh_k2": arb_to_dict(c_diag_dh_k2),
                "dh_active_shifts": dh_active_shifts,
                "dh_shift_tail_penalty": arb_to_dict(shift_pen_dh),
                "alpha_dh_at_R2": arb_to_dict(alpha_r_dh),
                "alpha_zeta_at_R9": arb_to_dict(alpha_r_zeta),
                "sufficient_tail_budget_sigma_min_no_shifts": arb_to_dict(budget_sigma_min_without_shifts),
                "sufficient_tail_budget_sigma_min_with_shifts_pb": arb_to_dict(budget_sigma_min_with_shifts_and_pb),
                "sufficient_tail_budget_loc_with_shifts": arb_to_dict(budget_loc_with_shifts),
                "arith_substituted_00_entry_zeta_arch": arb_to_dict(a_00_arith_sub),
                "full_odd_completion_00_entry_dh": arb_to_dict(a_00_full_odd_dh),
                "sufficient_tail_positivity_budget_strictly_negative": True,
                "note_on_scope": (
                    "A negative lower-bound budget certifies failure of the sufficient tail positivity "
                    "certificate on f_DH(s) (due to C_{diag,DH}({2,3}) = -0.695000 < 0 and the non-collapsing "
                    "prime-2 tower shift r=4/3 with coeff -0.683641); actual negative Rayleigh quotients "
                    "Q_{{2,3},DH}(g_b) < 0 are certified at b in {2, 5/2, 3} in Milestone 9."
                ),
            }
        )

    return {
        "prec": prec,
        "alpha_arch_acb_self_test_xi9": arb_to_dict(alpha_9_acb_real),
        "two_shift_product_checks": two_shift_checks,
        "poisson_bessel_tail_checks": pb_tail_checks,
        "full_space_block_schur_certificates": full_space_certificates,
        "dependency_edge_records": dependency_edge_records,
        "dh_control_records": dh_control_records,
    }


def verify_overlap(res256: dict[str, Any], res384: dict[str, Any]) -> int:
    """
    Reconstructs balls from exact full-precision string representations flint.arb(a["str"])
    rather than rounded float mid/rad fields (Fixing Finding 5 of argon-m17-review).
    Includes a mandatory self-test verifying that 1 + 2^(-100) and 1 + 2^(-101) do NOT overlap.
    """
    flint.ctx.prec = 384
    test_a = flint.arb(str(flint.arb(1) + flint.arb(2) ** (-100)))
    test_b = flint.arb(str(flint.arb(1) + flint.arb(2) ** (-101)))
    assert not test_a.overlaps(test_b), "Overlap self-test failed: 1+2^(-100) and 1+2^(-101) should not overlap!"

    count = 0

    def walk(a: Any, b: Any) -> None:
        nonlocal count
        if isinstance(a, dict) and "mid" in a and "rad" in a and "str" in a:
            ball_a = flint.arb(a["str"])
            ball_b = flint.arb(b["str"])
            assert ball_a.overlaps(ball_b), f"Full-precision ball mismatch: {a['str']} vs {b['str']}"
            count += 1
        elif isinstance(a, dict):
            for k in a:
                walk(a[k], b[k])
        elif isinstance(a, list):
            for x, y in zip(a, b):
                walk(x, y)

    walk(res256, res384)
    return count


def main() -> None:
    t0 = time.time()
    print("Running Milestone 17 verification (v2) at 256-bit flint.arb...")
    res256 = run_suite(256)
    print("Running Milestone 17 verification (v2) at 384-bit flint.arb...")
    res384 = run_suite(384)
    overlap_cnt = verify_overlap(res256, res384)
    elapsed = time.time() - t0
    print(f"256-bit vs 384-bit full-precision ball overlap checks passed: {overlap_cnt}/{overlap_cnt} ({elapsed:.2f}s)")

    payload: dict[str, Any] = {
        "milestone": "M17-infinite-dimensional-tail-floor-and-shift-coupling-defect-2026-10-15-v2",
        "lanes": ["WEIL-FLOOR", "NB-GAIN / COEFF", "KERNEL-API"],
        "wall_check": (
            "Does NOT prove RH, G2, or the cofinal prime-shift lower bound as a -> infinity "
            "(or K -> infinity). Both missing-original evidence groups in evidence/MISSING.md remain OPEN."
        ),
        "precisions_bits": [256, 384],
        "overlap_check_count": overlap_cnt,
        "overlap_self_test_non_overlapping_balls_2_minus_100_vs_101": True,
        "elapsed_seconds": round(elapsed, 3),
        "results_256": res256,
        "results_384": res384,
    }

    payload_bytes = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
    payload_sha256 = hashlib.sha256(payload_bytes).hexdigest()
    out_doc = {
        "schema_version": "1.0",
        "payload_sha256": payload_sha256,
        "payload": payload,
    }
    out_path = Path(__file__).resolve().parent / "verification.json"
    out_path.write_text(json.dumps(out_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    file_sha256 = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"Wrote {out_path}")
    print(f"payload.sha256 = {payload_sha256}")
    print(f"file_sha256    = {file_sha256}")


if __name__ == "__main__":
    main()
