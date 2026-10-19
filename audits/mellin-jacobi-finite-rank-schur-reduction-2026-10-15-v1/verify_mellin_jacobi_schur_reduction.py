#!/usr/bin/env python3
"""
Milestone 11 Verification & Certificate Script:
Mellin-Jacobi-Legendre Finite-Rank Gram-Schur Reduction & Exact Polynomial
Shift Matrices (NB-GAIN / COEFF & NS-61).

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
from pathlib import Path
from typing import Any

import flint


def arb_abs(x: flint.arb) -> flint.arb:
    return abs(x)


def arb_min(a: flint.arb, b: flint.arb) -> flint.arb:
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a < lo_b else (lo_b if lo_b < lo_a else flint.arb("0.5") * (lo_a + lo_b - abs(lo_a - lo_b)))
    hi = hi_a if hi_a < hi_b else (hi_b if hi_b < hi_a else flint.arb("0.5") * (hi_a + hi_b - abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_max(a: flint.arb, b: flint.arb) -> flint.arb:
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a > lo_b else (lo_b if lo_b > lo_a else flint.arb("0.5") * (lo_a + lo_b + abs(lo_a - lo_b)))
    hi = hi_a if hi_a > hi_b else (hi_b if hi_b > hi_a else flint.arb("0.5") * (hi_a + hi_b + abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


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
    the hypergeometric representation:
        j_m(z) = (z^m / (2m + 1)!!) * 0F1(; m + 3/2; -z^2 / 4),
    which is entire on all of C and free of removable singularity division by z at z = 0.
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


def jacobi_max_eig_f(mat: list[list[float]]) -> float:
    n = len(mat)
    a = [[0.5 * (mat[i][j] + mat[j][i]) for j in range(n)] for i in range(n)]
    for _ in range(60):
        max_val = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > max_val:
                    max_val = abs(a[i][j])
                    p, q = i, j
        if max_val < 1e-15:
            break
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        tau = (aqq - app) / (2.0 * apq)
        t = (1.0 / (tau + math.hypot(1.0, tau))) if tau >= 0.0 else (-1.0 / (-tau + math.hypot(1.0, tau)))
        c = 1.0 / math.hypot(1.0, t)
        s = t * c
        a[p][p] = app - t * apq
        a[q][q] = aqq + t * apq
        a[p][q] = 0.0
        a[q][p] = 0.0
        for r in range(n):
            if r != p and r != q:
                arp, arq = a[r][p], a[r][q]
                a[r][p] = c * arp - s * arq
                a[p][r] = a[r][p]
                a[r][q] = s * arp + c * arq
                a[q][r] = a[r][q]
    return max(a[i][i] for i in range(n))


def certify_max_eig_upper_bound_arb(g_mat: list[list[flint.arb]]) -> flint.arb:
    """
    Certify a sharp, rigorous ball upper bound Lambda_1 > lambda_max(g_mat) in
    flint.arb by selecting a candidate scalar Lambda_1 slightly above the midpoint
    spectral radius and certifying positive definiteness of (Lambda_1 * I_d - g_mat)
    purely in flint.arb via exact Cholesky factorization:
        Lambda_1 * I_d - g_mat = L L^T  with  L_{ii} > 0.
    """
    d = len(g_mat)
    g_mid = [[float(g_mat[i][j].mid()) for j in range(d)] for i in range(d)]
    lam_max_f = jacobi_max_eig_f(g_mid)
    rad_bound = max(
        sum(float(g_mat[i][j].rad()) for j in range(d))
        for i in range(d)
    )
    cushion = max(1e-12, 10.0 * rad_bound)
    lam1_ub = flint.arb(str(lam_max_f + cushion))
    shifted = [
        [(lam1_ub - g_mat[i][j]) if i == j else (-g_mat[i][j]) for j in range(d)]
        for i in range(d)
    ]
    _ = cholesky_lower_arb(shifted)
    return lam1_ub


def legendre_poly_coeffs(m: int) -> list[flint.arb]:
    """
    Return exact rational coefficients [c_0, c_1, ..., c_m] in flint.arb of P_m(t) = sum_{k=0}^m c_k t^k
    via Bonnet's three-term recurrence:
        (k + 1) P_{k+1}(t) = (2k + 1) t P_k(t) - k P_{k-1}(t).
    """
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


def poly_eval_arb(coeffs: list[flint.arb], x: flint.arb) -> flint.arb:
    res = flint.arb(0)
    for c in reversed(coeffs):
        res = res * x + c
    return res


def poly_shift_arb(coeffs: list[flint.arb], u: flint.arb) -> list[flint.arb]:
    """
    Given polynomial P(t) = sum_k c_k t^k, return coefficients of P(t + u) in powers of t.
    """
    deg = len(coeffs) - 1
    out = [flint.arb(0) for _ in range(deg + 1)]
    # Expand (t + u)^k = sum_{j=0}^k binom(k, j) u^{k-j} t^j
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
    """
    Exact integral int_a^b (sum_{k=0}^d coeffs[k] t^k) dt in flint.arb.
    """
    s = flint.arb(0)
    for k, c_k in enumerate(coeffs):
        kp1 = flint.arb(k + 1)
        s = s + c_k * ((b ** (k + 1)) - (a ** (k + 1))) / kp1
    return s


def exact_shift_entry_arb(m: int, n: int, u: flint.arb) -> flint.arb:
    """
    Compute (S_tau)_{m, n} for same-parity (m == n mod 2) and u = tau / b in [0, 2]:
        (S_tau)_{m, n} = sqrt((2m+1)(2n+1)) * int_{-1}^{1 - u} P_m(t) P_n(t + u) dt.
    """
    assert (m - n) % 2 == 0
    pm = legendre_poly_coeffs(m)
    pn_shifted = poly_shift_arb(legendre_poly_coeffs(n), u)
    prod_poly = poly_mul_arb(pm, pn_shifted)
    norm_fac = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
    return norm_fac * poly_integrate_arb(prod_poly, flint.arb(-1), flint.arb(1) - u)


def exact_support_entry_arb(m: int, n: int, u: flint.arb) -> flint.arb:
    """
    Compute (D_tau)_{m, n} = <phi_m, 1_{[tau-b, b]}(|x|) phi_n> for even m, n and u = tau / b in [1, 2]:
        (D_tau)_{m, n} = sqrt((2m+1)(2n+1)) * int_{u - 1}^1 P_m(t) P_n(t) dt.
    """
    assert m % 2 == 0 and n % 2 == 0
    pm = legendre_poly_coeffs(m)
    pn = legendre_poly_coeffs(n)
    prod_poly = poly_mul_arb(pm, pn)
    norm_fac = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
    return norm_fac * poly_integrate_arb(prod_poly, u - flint.arb(1), flint.arb(1))


def certify_mellin_jacobi_schur_reduction(prec_bits: int) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()
    tol_exp = 65 if prec_bits <= 256 else 85

    half = flint.arb(1) / flint.arb(2)
    pi = flint.arb.pi()

    # 1. Certify Theorem 2.1: Closed-form polynomial identities for (S_tau)_{m, n} vs symbolic Legendre integration
    u_test_grid = [
        flint.arb(1) / flint.arb(5),
        flint.arb(1) / flint.arb(2),
        flint.arb(1),
        flint.arb(7) / flint.arb(5),
        flint.arb(9) / flint.arb(5),
    ]
    poly_identity_checks: list[dict[str, Any]] = []
    for u in u_test_grid:
        s00_closed = flint.arb(2) - u
        s02_closed = -(flint.arb(5).sqrt() / flint.arb(2)) * u * (u - flint.arb(1)) * (u - flint.arb(2))
        s22_closed = (
            flint.arb(2)
            - flint.arb(5) * u
            + (flint.arb(5) / flint.arb(2)) * (u**3)
            - (flint.arb(3) / flint.arb(8)) * (u**5)
        )
        s11_closed = flint.arb(2) - flint.arb(3) * u + half * (u**3)
        s13_closed = flint.arb(21).sqrt() * (
            -u
            + (flint.arb(5) / flint.arb(2)) * (u**2)
            - (flint.arb(3) / flint.arb(2)) * (u**3)
            + (flint.arb(1) / flint.arb(8)) * (u**5)
        )
        s33_closed = (
            flint.arb(2)
            - flint.arb(7) * u
            + flint.arb(7) * (u**3)
            - (flint.arb(21) / flint.arb(8)) * (u**5)
            + (flint.arb(5) / flint.arb(16)) * (u**7)
        )

        s00_sym = exact_shift_entry_arb(0, 0, u)
        s02_sym = exact_shift_entry_arb(0, 2, u)
        s22_sym = exact_shift_entry_arb(2, 2, u)
        s11_sym = exact_shift_entry_arb(1, 1, u)
        s13_sym = exact_shift_entry_arb(1, 3, u)
        s33_sym = exact_shift_entry_arb(3, 3, u)

        for closed_val, sym_val, name in (
            (s00_closed, s00_sym, "S_{0,0}"),
            (s02_closed, s02_sym, "S_{0,2}"),
            (s22_closed, s22_sym, "S_{2,2}"),
            (s11_closed, s11_sym, "S_{1,1}"),
            (s13_closed, s13_sym, "S_{1,3}"),
            (s33_closed, s33_sym, "S_{3,3}"),
        ):
            assert (closed_val - sym_val).contains(0), f"Polynomial identity mismatch for {name} at u={u}"

        poly_identity_checks.append(
            {
                "u": arb_to_dict(u),
                "S_00": arb_to_dict(s00_closed),
                "S_02": arb_to_dict(s02_closed),
                "S_22": arb_to_dict(s22_closed),
                "S_11": arb_to_dict(s11_closed),
                "S_13": arb_to_dict(s13_closed),
                "S_33": arb_to_dict(s33_closed),
                "all_six_identities_contain_zero": True,
            }
        )

    # 2. Certify Theorem 1 & Theorem 2.1: 4x4 Legendre-Gegenbauer Gram matrices & tail traces at K = 2, 3, 4
    # and at a = (1/2) log 12 (Delta_alpha = 3/5):
    def eval_legendre_archimedean(
        label: str,
        primes: list[int],
        b: flint.arb,
        da: flint.arb,
        c_diag: flint.arb,
        n_modes: int = 4,
    ) -> dict[str, Any]:
        xi0 = find_alpha_root_arb(da)
        b_acb = flint.acb(b)
        two_b_over_pi = (flint.arb(2) * b) / pi
        two_b_over_pi_acb = flint.acb(two_b_over_pi)

        # Compute full traces Tr(A_even), Tr(A_odd) and N=1..4 tail traces:
        def int_traces_and_diag(xi: flint.acb, _: Any) -> flint.acb:
            w = two_b_over_pi_acb * sigma_lp_acb(xi, primes) * (flint.acb(da) - alpha_acb(xi))
            z = b_acb * xi
            s2z = acb_sinc(flint.acb(2) * z)
            tr_e = flint.acb(half) * (flint.acb(1) + s2z)
            tr_o = flint.acb(half) * (flint.acb(1) - s2z)
            return w * (tr_e + flint.acb(0, 1) * tr_o)

        tr_e_full, tr_o_full = integrate_on_0_to_xi0(int_traces_and_diag, xi0, tol_exp)

        # Compute 4x4 even and odd Gram matrices A^{(4)}_even, A^{(4)}_odd:
        a_even = [[flint.arb(0) for _ in range(n_modes)] for _ in range(n_modes)]
        a_odd = [[flint.arb(0) for _ in range(n_modes)] for _ in range(n_modes)]

        for r in range(n_modes):
            for s in range(r, n_modes):
                sgn_rs = flint.acb(1 if (r + s) % 2 == 0 else -1)
                norm_e = flint.acb((flint.arb(4 * r + 1) * flint.arb(4 * s + 1)).sqrt())
                norm_o = flint.acb((flint.arb(4 * r + 3) * flint.arb(4 * s + 3)).sqrt())

                def int_entry(xi: flint.acb, _: Any, r_idx: int = r, s_idx: int = s) -> flint.acb:
                    w = two_b_over_pi_acb * sigma_lp_acb(xi, primes) * (flint.acb(da) - alpha_acb(xi))
                    z = b_acb * xi
                    je_r = spherical_bessel_j_acb(2 * r_idx, z)
                    je_s = je_r if r_idx == s_idx else spherical_bessel_j_acb(2 * s_idx, z)
                    jo_r = spherical_bessel_j_acb(2 * r_idx + 1, z)
                    jo_s = jo_r if r_idx == s_idx else spherical_bessel_j_acb(2 * s_idx + 1, z)
                    val_e = sgn_rs * norm_e * je_r * je_s
                    val_o = sgn_rs * norm_o * jo_r * jo_s
                    return w * (val_e + flint.acb(0, 1) * val_o)

                re_val, im_val = integrate_on_0_to_xi0(int_entry, xi0, tol_exp)
                a_even[r][s] = a_even[s][r] = re_val
                a_odd[r][s] = a_odd[s][r] = im_val

        # Exact finite-sum complement tail traces for N = 1, 2, 3, 4:
        tail_even_by_n: dict[str, Any] = {}
        tail_odd_by_n: dict[str, Any] = {}
        partial_e = flint.arb(0)
        partial_o = flint.arb(0)
        for n_trunc in range(1, n_modes + 1):
            partial_e = partial_e + a_even[n_trunc - 1][n_trunc - 1]
            partial_o = partial_o + a_odd[n_trunc - 1][n_trunc - 1]
            eps_e = tr_e_full - partial_e
            eps_o = tr_o_full - partial_o
            if n_trunc <= 2:
                assert eps_e > flint.arb(0)
                assert eps_o > flint.arb(0)
            else:
                assert not (eps_e < flint.arb(0))
                assert not (eps_o < flint.arb(0))
            tail_even_by_n[f"N={n_trunc}"] = {
                "tail_trace": arb_to_dict(arb_max(flint.arb(0), eps_e)),
                "captured_fraction": arb_to_dict(partial_e / tr_e_full),
            }
            tail_odd_by_n[f"N={n_trunc}"] = {
                "tail_trace": arb_to_dict(arb_max(flint.arb(0), eps_o)),
                "captured_fraction": arb_to_dict(partial_o / tr_o_full),
            }

        # Certify N=3 and N=4 Legendre-Gegenbauer continuum operator norm bounds:
        a_even_3 = [[a_even[i][j] for j in range(3)] for i in range(3)]
        a_odd_3 = [[a_odd[i][j] for j in range(3)] for i in range(3)]
        lam1_e3 = certify_max_eig_upper_bound_arb(a_even_3)
        lam1_o3 = certify_max_eig_upper_bound_arb(a_odd_3)
        lam1_e4 = certify_max_eig_upper_bound_arb(a_even)
        lam1_o4 = certify_max_eig_upper_bound_arb(a_odd)

        eps_e3 = arb_max(flint.arb(0), tr_e_full - (a_even[0][0] + a_even[1][1] + a_even[2][2]))
        eps_o3 = arb_max(flint.arb(0), tr_o_full - (a_odd[0][0] + a_odd[1][1] + a_odd[2][2]))
        eps_e4 = arb_max(flint.arb(0), tr_e_full - sum((a_even[i][i] for i in range(4)), flint.arb(0)))
        eps_o4 = arb_max(flint.arb(0), tr_o_full - sum((a_odd[i][i] for i in range(4)), flint.arb(0)))

        op_e_trace = tr_e_full / c_diag
        op_o_trace = tr_o_full / c_diag
        op_e_n3 = (lam1_e3 + eps_e3) / c_diag
        op_o_n3 = (lam1_o3 + eps_o3) / c_diag
        op_e_n4 = (lam1_e4 + eps_e4) / c_diag
        op_o_n4 = (lam1_o4 + eps_o4) / c_diag

        assert op_e_n4 < op_e_trace
        assert op_o_n4 < op_o_trace

        return {
            "label": label,
            "primes": primes,
            "b": arb_to_dict(b),
            "Delta_alpha": arb_to_dict(da),
            "xi0": arb_to_dict(xi0),
            "C_diag": arb_to_dict(c_diag),
            "tr_even_full": arb_to_dict(tr_e_full),
            "tr_odd_full": arb_to_dict(tr_o_full),
            "tail_even_by_N": tail_even_by_n,
            "tail_odd_by_N": tail_odd_by_n,
            "op_norm_bound_even_trace": arb_to_dict(op_e_trace),
            "op_norm_bound_even_N3": arb_to_dict(op_e_n3),
            "op_norm_bound_even_N4": arb_to_dict(op_e_n4),
            "op_norm_bound_odd_trace": arb_to_dict(op_o_trace),
            "op_norm_bound_odd_N3": arb_to_dict(op_o_n3),
            "op_norm_bound_odd_N4": arb_to_dict(op_o_n4),
        }

    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()
    log7 = flint.arb(7).log()

    c_diag_23 = (flint.arb(4) / flint.arb(3)) * log2 + log3
    c_diag_235 = (flint.arb(8) / flint.arb(5)) * log2 + (flint.arb(6) / flint.arb(5)) * log3 + (flint.arb(16) / flint.arb(15)) * log5
    c_diag_2357 = (
        (flint.arb(64) / flint.arb(35)) * log2
        + (flint.arb(48) / flint.arb(35)) * log3
        + (flint.arb(128) / flint.arb(105)) * log5
        + (flint.arb(32) / flint.arb(35)) * log7
    )

    arch_checkpoints = [
        eval_legendre_archimedean(
            "K=2 primorial isometric horizon b_iso(2) = 1/2 log(3/2)",
            [2, 3],
            half * (flint.arb(3) / flint.arb(2)).log(),
            flint.arb(0),
            c_diag_23,
        ),
        eval_legendre_archimedean(
            "K=3 primorial isometric horizon b_iso(3) = 1/2 log(6/5)",
            [2, 3, 5],
            half * (flint.arb(6) / flint.arb(5)).log(),
            flint.arb(0),
            c_diag_235,
        ),
        eval_legendre_archimedean(
            "K=4 primorial isometric horizon b_iso(4) = 1/2 log(15/14)",
            [2, 3, 5, 7],
            half * (flint.arb(15) / flint.arb(14)).log(),
            flint.arb(0),
            c_diag_2357,
        ),
        eval_legendre_archimedean(
            "K=2 internal log 2 entry a = 1/2 log 12 (b = 1/2 log 2, Delta_alpha = 3/5)",
            [2, 3],
            half * log2,
            flint.arb(3) / flint.arb(5),
            c_diag_23 + flint.arb(6) / flint.arb(5),
        ),
    ]

    # 3. Certify Theorem 2.2: Exact 3x3 and 4x4 Legendre-Schur reflection projection Gram matrix Q_{tau, +1}^{(N)} > 0
    # for tau = log(3/2) at b = 0.25 (u = tau / b ~ 1.62186):
    b_refl = flint.arb(1) / flint.arb(4)
    tau_32 = log3 - log2
    u_refl = tau_32 / b_refl
    q_refl_4x4 = [[flint.arb(0) for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for s in range(r, 4):
            d_rs = exact_support_entry_arb(2 * r, 2 * s, u_refl)
            s_rs = exact_shift_entry_arb(2 * r, 2 * s, u_refl)
            q_val = half * (d_rs + half * s_rs)
            q_refl_4x4[r][s] = q_refl_4x4[s][r] = q_val

    l_q4 = cholesky_lower_arb(q_refl_4x4)
    q_refl_3x3 = [[q_refl_4x4[i][j] for j in range(3)] for i in range(3)]
    l_q3 = cholesky_lower_arb(q_refl_3x3)

    return {
        "prec_bits": prec_bits,
        "polynomial_shift_identity_checks": poly_identity_checks,
        "legendre_archimedean_checkpoints": arch_checkpoints,
        "reflection_projection_gram_certificate": {
            "b": arb_to_dict(b_refl),
            "tau": arb_to_dict(tau_32),
            "u": arb_to_dict(u_refl),
            "cholesky_pivots_N3": [arb_to_dict(l_q3[i][i]) for i in range(3)],
            "cholesky_pivots_N4": [arb_to_dict(l_q4[i][i]) for i in range(4)],
            "positive_definite_certified": True,
        },
        "elapsed_s": round(time.time() - t0, 4),
    }


def verify_two_precision_consistency(res_256: dict[str, Any], res_384: dict[str, Any]) -> dict[str, Any]:
    flint.ctx.prec = 384
    checks = 0
    for c256, c384 in zip(
        res_256["legendre_archimedean_checkpoints"],
        res_384["legendre_archimedean_checkpoints"],
    ):
        for key in (
            "tr_even_full",
            "tr_odd_full",
            "op_norm_bound_even_N3",
            "op_norm_bound_even_N4",
            "op_norm_bound_odd_N3",
            "op_norm_bound_odd_N4",
        ):
            b256 = flint.arb(c256[key]["str"])
            b384 = flint.arb(c384[key]["str"])
            assert b256.overlaps(b384), f"Ball mismatch at {c384['label']} [{key}]"
            checks += 1
        for n_key in ("N=1", "N=2", "N=3", "N=4"):
            te256 = flint.arb(c256["tail_even_by_N"][n_key]["tail_trace"]["str"])
            te384 = flint.arb(c384["tail_even_by_N"][n_key]["tail_trace"]["str"])
            assert te256.overlaps(te384)
            checks += 1
    return {
        "precisions_compared": [256, 384],
        "num_ball_overlap_checks": checks,
        "all_overlaps_verified": True,
    }


def main() -> None:
    t_start = time.time()
    out_dir = Path(__file__).resolve().parent

    res_256 = certify_mellin_jacobi_schur_reduction(256)
    res_384 = certify_mellin_jacobi_schur_reduction(384)
    consistency = verify_two_precision_consistency(res_256, res_384)

    payload: dict[str, Any] = {
        "audit_id": "mellin-jacobi-finite-rank-schur-reduction-2026-10-15-v1",
        "date": "2026-10-15",
        "lanes": ["NB-GAIN", "COEFF", "NS-61"],
        "wall_check": {
            "rh_proved": False,
            "g2_completed": False,
            "cofinal_prime_shift_lower_bound_proved": False,
            "missing_historical_evidence_recovered": False,
            "open_obligations": [
                "Riemann Hypothesis (RH)",
                "Global archimedean completion (G2)",
                "Cofinal signed-arithmetic lower bound as a -> infinity",
                "Historical missing-original evidence groups in evidence/MISSING.md (stage4_run_summary.json / stage4_Ticks.json and certificate.json / verify_log.txt)",
            ],
        },
        "two_precision_consistency": consistency,
        "primary_384bit": res_384,
        "secondary_256bit": res_256,
        "total_elapsed_s": round(time.time() - t_start, 4),
    }

    ver_path = out_dir / "verification.json"
    raw_bytes = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
    payload_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    payload["sha256"] = payload_sha256
    ver_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    file_sha256 = hashlib.sha256(ver_path.read_bytes()).hexdigest()

    print("=== Milestone 11 Verification Complete ===")
    print(f"Two-precision consistency (256 vs 384 bits): {consistency['num_ball_overlap_checks']} checks PASS")
    for cp in res_384["legendre_archimedean_checkpoints"]:
        print(
            f"  {cp['label'][:46]:46s}: "
            f"op_N4={cp['op_norm_bound_even_N4']['upper']:.6f} < tr={cp['op_norm_bound_even_trace']['upper']:.6f}, "
            f"eps_N4={cp['tail_even_by_N']['N=4']['tail_trace']['upper']:.3e}"
        )
    print(f"verification.json payload.sha256 = {payload_sha256}")
    print(f"verification.json file_sha256    = {file_sha256}")


if __name__ == "__main__":
    main()
