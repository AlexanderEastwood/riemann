#!/usr/bin/env python3
"""
Deterministic Two-Precision (256-bit and 384-bit) flint.arb / flint.acb
Verification & Diagnostic Suite for the Six Post-v18 Cofinal Candidate Mechanisms
(Candidates I, II/IIb, III in WEIL-FLOOR / KERNEL-API and Candidates A, B, C in NB-GAIN).

Verifies at both 256-bit and 384-bit precision (with zero numpy/scipy/mpmath imports
and full-precision string ball overlap checks):
1. Theorem 1 & Candidate I (WEIL-FLOOR Legendre Tail Shell & Pole-Cancellation Identity):
   - Exact boundary-free dual-pole Chebyshev-Legendre identity in both even and odd parities:
       (T_arith(a) - T_pole(a))_{m,n}
         == int_0^2 ((psi(e^{au}) - e^{au} - a*u + 1)/e^{au/2}) (a C_{m,n}(u) - 2 C'_{m,n}(u)) du
     certified via .contains(0) across 8 (m,n) pairs at lambda = 5.
   - Exact 8x8 Cholesky positivity of the unpreconditioned, unshifted Weil operator
     W_lambda = A_arch^full(a) + T_pole(a) - T_arith(a) on V_8^even(-a,a) and V_8^odd(-a,a)
     across all four benchmark windows lambda in {2, 3, 5, 8} (up to 26 prime-power shifts, k <= 61),
     plus shifted Block-Schur complements at C_* = 8 (prop:v138-three-floors) and quantitative
     comparison of the M17 triangle-inequality bound vs. the finite-shell signed Frobenius norm
     ||T_arith(a)|_{V_[4,8]^even}||_F (finite 4-mode Legendre shell only, not V_4(a)^perp).
2. Theorem 2 & Candidate II / IIb (WEIL-FLOOR Radical Critical-Zero Screening vs. Commutator Obstruction):
   - Exact automatic-differentiation verification at rho_1 = 1/2 + i*gamma_1 that
     Xi(gamma_1) contains 0 while |Xi'(gamma_1)| = 0.0013827190892... > 0.
   - Exact closed-form odd pole moment identity for the position-weighted Gaussian radical x*h(x):
       int_R x sinh(x/2) h(x) dx == (1 + (gamma_E - log(4*pi))/2) / sqrt(3) = +0.0133343137887... > 0,
     certified against numerical quadrature (with explicit lem:v150-weight tail bounds for n >= 12
     and x >= 3.5) via .contains(0), together with compressed 8-mode Legendre Rayleigh quotients and
     compressed residuals for h(x), h'(x), and x*h(x) across lambda in {2, 3, 5, 8}.
3. Candidate III (WEIL-FLOOR / KERNEL-API Multiprime Codimension & NS57 Perturbation Enclosure):
   - Exact flint.arb Cholesky Weyl enclosure across lambda in {2, 3, 5, 8} under the NS57 perturbation
     delta_2 = -log(2)/100 certifying (2|delta_2|) I_8 +- B_{delta_2} > 0, hence
     |lambda_k(W_lambda^{delta_2}) - lambda_k(W_lambda)| < 2|delta_2| = log(2)/50 (thm:ns57-bounded-floor-stability).
4. Candidates A, B, and C (NB-GAIN Finite-Block Residual Diagnostics across N in {4, 8, 16, 32}):
   - Candidate A: Dual Stieltjes-divisor identity M_schur == M_div holds with
     .contains(0) on both the true load (beta = 1/2) and the NS74 positive-floor control (beta = 1/2 + 10^-2).
   - Candidate B: Exact NS83 q=2 transformed target Mellin magnitude |T_2(rho_1)| = |rho_1 - 1|/|rho_1|^3
     = 1/|rho_1|^2 = 0.0049989894328..., first-pair weight 2/|rho_1|^4 = 4.997979e-5, 50-pair floor
     C_{2,50} = 7.4079419e-5, and finite-block values of (log N) E_N^{(2)} and (log N / log 2)(Delta_N / E_N^{(2)})
     across N in {4, 8, 16, 32} (finite-block observations only; does not establish convergence).
   - Candidate C: Finite-block quantification of inverse-Gram trace ratio tr(H_N)/tr(D_N) = 4.307e-3 and
     old-space load refit norm ratio ||h_N||_2^2 / ||b_new||_2^2 = 2.051e-9 at N = 32.

Wall check: Same open gap. Does NOT prove RH, G2, or any cofinal lower bound.
Both missing-original evidence groups in evidence/MISSING.md remain OPEN.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

import flint
from flint import acb, arb, arb_mat, ctx

ROOT = Path(__file__).resolve().parents[2]
NS61_DIR = ROOT / "evidence" / "v159" / "ns61"
for p in (ROOT, NS61_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from certify_smoothed import Kernel, ball, dot, sub  # noqa: E402


def arb_abs(x: arb) -> arb:
    return abs(x)


def arb_to_dict(x: arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


def spherical_bessel_j_acb(m: int, z: acb) -> acb:
    double_fact = 1
    for k in range(1, 2 * m + 2, 2):
        double_fact *= k
    b_param = acb(arb(2 * m + 3) / arb(2))
    w_arg = -(z * z) / acb(4)
    hyp = w_arg.hypgeom_0f1(b_param)
    return (z**m) * hyp / acb(double_fact)


def cholesky_lower_arb(mat: list[list[arb]]) -> list[list[arb]]:
    n = len(mat)
    l_mat = [[arb(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = mat[i][j]
            for k in range(j):
                s = s - l_mat[i][k] * l_mat[j][k]
            if i == j:
                assert s > arb(0), f"Cholesky pivot <= 0 at index {i}: {s}"
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


def legendre_poly_coeffs(m: int) -> list[arb]:
    return [arb(c.numerator) / arb(c.denominator) for c in legendre_poly_fraction(m)]


def c_mn_poly_u(m: int, n: int) -> list[arb]:
    pm = legendre_poly_coeffs(m)
    pn = legendre_poly_coeffs(n)
    u_coeffs = [arb(0) for _ in range(m + n + 2)]
    for i, ci in enumerate(pm):
        for k, ck in enumerate(pn):
            binom_kj = 1
            for j in range(k + 1):
                if j > 0:
                    binom_kj = (binom_kj * (k - j + 1)) // j
                p1 = i + j + 1
                scale = (ci * ck * arb(binom_kj)) / arb(p1)
                binom_pr = 1
                for r in range(p1 + 1):
                    if r > 0:
                        binom_pr = (binom_pr * (p1 - r + 1)) // r
                    sign = 1 if r % 2 == 0 else -1
                    c_u = arb(sign * binom_pr)
                    if r == 0:
                        c_u = c_u - arb(1 if p1 % 2 == 0 else -1)
                    u_coeffs[k - j + r] = u_coeffs[k - j + r] + scale * c_u
    norm = (arb(2 * m + 1) * arb(2 * n + 1)).sqrt() / arb(2)
    return [c * norm for c in u_coeffs]


def eval_poly_acb(coeffs: list[arb], z: acb) -> acb:
    res = acb(0)
    for c in reversed(coeffs):
        res = res * z + acb(c)
    return res


def eval_poly_arb(coeffs: list[arb], x: arb) -> arb:
    res = arb(0)
    for c in reversed(coeffs):
        res = res * x + c
    return res


def arch_tail_closed(t_end: arb) -> arb:
    w = (-t_end / arb(2)).exp()
    return ((arb(1) + w) / (arb(1) - w)).log() + arb(2) * w.atan()


def exact_spatial_j_mn_zero(
    m: int,
    n: int,
    b: arb,
    tol_exp: int,
    poly_cache: dict[tuple[int, int], list[arb]],
) -> arb:
    if (m, n) not in poly_cache:
        poly_cache[(m, n)] = c_mn_poly_u(m, n)
    if (n, m) not in poly_cache:
        poly_cache[(n, m)] = c_mn_poly_u(n, m)
    poly_mn = poly_cache[(m, n)]
    poly_nm = poly_cache[(n, m)]
    poly_u = [(a + b_c) / arb(2) for a, b_c in zip(poly_mn, poly_nm)]
    tol = 2.0 ** (-tol_exp)
    pi = arb.pi()
    psi_14 = acb(arb(1) / arb(4)).digamma().real
    b_acb = acb(b)
    two_b = arb(2) * b
    phi_0 = poly_u[0]
    q_coeffs = [-c / b for c in poly_u[1:]]

    def int_lam0(t: acb, _: Any) -> acb:
        return (t / acb(2)).exp() * eval_poly_acb(q_coeffs, t / b_acb) / (acb(0, 1) * t).sinc()

    i_main = acb.integral(int_lam0, acb(0), acb(two_b), rel_tol=tol, abs_tol=tol).real
    return (psi_14 - pi.log() + arch_tail_closed(two_b)) * phi_0 + i_main


def p_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    return out


def eval_p(p: list[Fraction], x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def int_u_poly_exp(poly_coeffs: list[arb], alpha: arb, u0: arb, u1: arb) -> arb:
    """Exact closed-form integral int_{u0}^{u1} P(u) e^{alpha u} du in flint.arb."""
    d = len(poly_coeffs) - 1
    q = [arb(0)] * (d + 1)
    for k in range(d, -1, -1):
        rem = poly_coeffs[k] - (arb(k + 1) * q[k + 1] if k < d else arb(0))
        q[k] = rem / alpha
    val1 = (alpha * u1).exp() * eval_poly_arb(q, u1)
    val0 = (alpha * u0).exp() * eval_poly_arb(q, u0)
    return val1 - val0


def von_mangoldt_up_to(limit: int) -> list[arb]:
    lam = [arb(0)] * (limit + 1)
    is_p = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_p[p]:
            for mult in range(p * p, limit + 1, p):
                is_p[mult] = False
            lp = arb(p).log()
            pk = p
            while pk <= limit:
                lam[pk] = lp
                pk *= p
    return lam


def h_and_dh_acb(z: acb, n0: int = 16) -> tuple[acb, acb]:
    """Evaluate the even Gaussian arithmetic radical h(z) and odd derivative h'(z)
    on complex balls z = x + i*y used by flint.acb.integral:
      - For strictly negative balls (Re(z) < 0), applies exact Poisson reflection
        h(z) = h(-z) and h'(z) = -h'(-z) (lem:v150-weight).
      - Requires Re(z) > -1/4 and alpha = Re(exp(2z)) > 1/2 on the complex ball z;
        otherwise returns NaN balls so acb.integral bisects wide quadrature boxes.
      - Encloses the omitted n >= n0 summands dynamically over the complex box z
        using r = |exp(z)| and alpha = Re(exp(2z)) > 1/2."""
    if z.real < arb(0):
        h_neg, dh_neg = h_and_dh_acb(-z, n0=n0)
        return h_neg, -dh_neg
    if not (z.real > arb("-0.25")):
        nan_b = acb(arb("nan"), arb("nan"))
        return nan_b, nan_b
    alpha = (acb(2) * z).exp().real
    if not (alpha > arb("0.5")):
        nan_b = acb(arb("nan"), arb("nan"))
        return nan_b, nan_b
    pi = arb.pi()
    pi_acb = acb(pi)
    pref_acb = acb(arb(4) * pi / arb(3).sqrt())
    ex = z.exp()
    ex_half = (z / acb(2)).exp()
    h_val = acb(0)
    dh_val = acb(0)
    for n in range(1, n0):
        u = acb(n) * ex
        u2 = u * u
        exp_fac = ex_half * (-pi_acb * u2).exp()
        poly_h = u2 * (acb(2) * pi_acb * u2 - acb(3))
        poly_dh = u2 * (
            acb(9) * pi_acb * u2
            - acb(arb(15) / arb(2))
            - acb(2) * pi_acb * u2 * (acb(2) * pi_acb * u2 - acb(3))
        )
        h_val += pref_acb * poly_h * exp_fac
        dh_val += pref_acb * poly_dh * exp_fac
    r = abs(ex)
    r2 = r * r
    n0_arb = arb(n0)
    n0_sq = n0_arb * n0_arb
    q_ratio = (-pi * alpha * n0_arb).exp()
    tail_common = (
        (arb(4) * pi / arb(3).sqrt())
        * (r ** (arb(5) / arb(2)))
        * n0_sq
        * (-pi * alpha * n0_sq).exp()
        / (arb(1) - q_ratio)
    )
    tail_h = tail_common * (arb(2) * pi * n0_sq * r2 + arb(3))
    tail_dh = tail_common * (
        arb(4) * pi * pi * (n0_sq * n0_sq) * (r2 * r2)
        + arb(15) * pi * n0_sq * r2
        + arb(15) / arb(2)
    )
    return (
        h_val + acb(arb(0, tail_h), arb(0, tail_h)),
        dh_val + acb(arb(0, tail_dh), arb(0, tail_dh)),
    )


def run_all_candidate_tests_at_precision(prec_bits: int) -> dict[str, Any]:
    ctx.prec = prec_bits
    tol_exp = 95 if prec_bits <= 256 else 135
    tol = 2.0 ** (-tol_exp)

    n_modes = 8
    poly_cache: dict[tuple[int, int], list[arb]] = {}
    leg_polys = [legendre_poly_coeffs(m) for m in range(2 * n_modes)]
    for i in range(n_modes):
        for j in range(n_modes):
            poly_cache[(2 * i, 2 * j)] = c_mn_poly_u(2 * i, 2 * j)
            poly_cache[(2 * i + 1, 2 * j + 1)] = c_mn_poly_u(2 * i + 1, 2 * j + 1)

    lam_arr = von_mangoldt_up_to(64)

    # -----------------------------------------------------------------------
    # 1. Theorem 1: Boundary-Free Dual-Pole Chebyshev-Legendre Identity
    # -----------------------------------------------------------------------
    a_five = arb(5).log()
    psi_vals = [arb(0)] * 26
    acc = arb(0)
    for k in range(1, 26):
        acc += lam_arr[k]
        psi_vals[k] = acc

    abel_legendre_checks: list[dict[str, Any]] = []
    for m, n in [(0, 0), (0, 2), (2, 4), (4, 4), (1, 1), (1, 3), (3, 3), (3, 5)]:
        p_mn = poly_cache[(m, n)]
        p_nm = poly_cache[(n, m)]
        poly_c = [(x + y) / arb(2) for x, y in zip(p_mn, p_nm)]
        c_at_0 = eval_poly_arb(poly_c, arb(0))
        c_at_2 = eval_poly_arb(poly_c, arb(2))
        assert (c_at_0 - (arb(1) if m == n else arb(0))).contains(0)
        assert c_at_2.contains(0)

        poly_dc = [arb(k) * poly_c[k] for k in range(1, len(poly_c))]
        poly_k = [arb(0)] * len(poly_c)
        for idx, c in enumerate(poly_c):
            poly_k[idx] += a_five * c
        for idx, dc in enumerate(poly_dc):
            poly_k[idx] -= arb(2) * dc
        poly_uk = [arb(0)] + poly_k

        t_arith = arb(0)
        for k in range(2, 25):
            if lam_arr[k] > arb(0):
                lk = arb(k).log()
                wk = lam_arr[k] / arb(k).sqrt()
                t_arith += wk * arb(2) * eval_poly_arb(poly_c, lk / a_five)
        z = acb(0, a_five / arb(2))
        im = (acb(0, -1) ** m * spherical_bessel_j_acb(m, z)).real
        in_ = (acb(0, -1) ** n * spherical_bessel_j_acb(n, z)).real
        cm = (arb(2) * a_five * arb(2 * m + 1)).sqrt() * im
        cn = (arb(2) * a_five * arb(2 * n + 1)).sqrt() * in_
        t_pole = (arb(2) if m % 2 == 0 else -arb(2)) * cm * cn
        lhs = t_arith - t_pole

        rhs = -int_u_poly_exp(poly_k, a_five / arb(2), arb(0), arb(2))
        rhs -= a_five * int_u_poly_exp(poly_uk, -a_five / arb(2), arb(0), arb(2))
        rhs += int_u_poly_exp(poly_k, -a_five / arb(2), arb(0), arb(2))
        for k in range(1, 25):
            u0 = arb(k).log() / a_five
            u1 = arb(k + 1).log() / a_five
            rhs += psi_vals[k] * int_u_poly_exp(poly_k, -a_five / arb(2), u0, u1)
        diff = lhs - rhs
        assert diff.contains(0), f"Abel-Legendre identity failed at ({m},{n}): {diff}"
        abel_legendre_checks.append({
            "pair": f"({m},{n})",
            "parity": "even" if m % 2 == 0 else "odd",
            "lhs_direct": arb_to_dict(lhs),
            "rhs_boundary_free_integral": arb_to_dict(rhs),
            "diff": arb_to_dict(diff),
            "contains_zero": True,
        })

    # -----------------------------------------------------------------------
    # 2. Candidate I & III & II/IIb across windows lambda in {2, 3, 5, 8}
    # -----------------------------------------------------------------------
    window_rows: list[dict[str, Any]] = []
    delta_ns57 = -arb(2).log() / arb(100)
    two_abs_delta_ns57 = arb(2) * arb_abs(delta_ns57)

    for lam_int in (2, 3, 5, 8):
        a = arb(lam_int).log()
        two_a = arb(2) * a
        a_acb = acb(a)

        a_arch_e = [[arb(0)] * n_modes for _ in range(n_modes)]
        t_pole_e = [[arb(0)] * n_modes for _ in range(n_modes)]
        t_arith_e = [[arb(0)] * n_modes for _ in range(n_modes)]
        a_arch_o = [[arb(0)] * n_modes for _ in range(n_modes)]
        t_pole_o = [[arb(0)] * n_modes for _ in range(n_modes)]
        t_arith_o = [[arb(0)] * n_modes for _ in range(n_modes)]
        s2_mat_e = [[arb(0)] * n_modes for _ in range(n_modes)]

        c_vec: list[arb] = []
        s_vec: list[arb] = []
        for i in range(n_modes):
            me = 2 * i
            mo = 2 * i + 1
            z = acb(0, a / arb(2))
            i_me = (acb(0, -1) ** me * spherical_bessel_j_acb(me, z)).real
            i_mo = (acb(0, -1) ** mo * spherical_bessel_j_acb(mo, z)).real
            c_vec.append((arb(2) * a * arb(2 * me + 1)).sqrt() * i_me)
            s_vec.append((arb(2) * a * arb(2 * mo + 1)).sqrt() * i_mo)

        for i in range(n_modes):
            for j in range(i, n_modes):
                ae = exact_spatial_j_mn_zero(2 * i, 2 * j, a, tol_exp, poly_cache)
                ao = exact_spatial_j_mn_zero(2 * i + 1, 2 * j + 1, a, tol_exp, poly_cache)
                a_arch_e[i][j] = a_arch_e[j][i] = ae
                a_arch_o[i][j] = a_arch_o[j][i] = ao
                t_pole_e[i][j] = t_pole_e[j][i] = arb(2) * c_vec[i] * c_vec[j]
                t_pole_o[i][j] = t_pole_o[j][i] = -arb(2) * s_vec[i] * s_vec[j]

        tri_sum = arb(0)
        n_shifts = 0
        for k in range(2, lam_int * lam_int):
            if lam_arr[k] > arb(0):
                lk = arb(k).log()
                if lk < two_a:
                    n_shifts += 1
                    wk = lam_arr[k] / arb(k).sqrt()
                    tri_sum += arb(2) * wk
                    u = lk / a
                    for i in range(n_modes):
                        for j in range(i, n_modes):
                            pe_ij = poly_cache[(2 * i, 2 * j)]
                            pe_ji = poly_cache[(2 * j, 2 * i)]
                            polye = [(x + y) / arb(2) for x, y in zip(pe_ij, pe_ji)]
                            se = arb(2) * eval_poly_arb(polye, u)
                            po_ij = poly_cache[(2 * i + 1, 2 * j + 1)]
                            po_ji = poly_cache[(2 * j + 1, 2 * i + 1)]
                            polyo = [(x + y) / arb(2) for x, y in zip(po_ij, po_ji)]
                            so = arb(2) * eval_poly_arb(polyo, u)
                            t_arith_e[i][j] += wk * se
                            t_arith_o[i][j] += wk * so
                            if k == 2:
                                s2_mat_e[i][j] = s2_mat_e[j][i] = se
                            if i != j:
                                t_arith_e[j][i] = t_arith_e[i][j]
                                t_arith_o[j][i] = t_arith_o[i][j]

        w_e = [
            [a_arch_e[i][j] + t_pole_e[i][j] - t_arith_e[i][j] for j in range(n_modes)]
            for i in range(n_modes)
        ]
        w_o = [
            [a_arch_o[i][j] + t_pole_o[i][j] - t_arith_o[i][j] for j in range(n_modes)]
            for i in range(n_modes)
        ]

        # Certify 8x8 Cholesky positivity of unshifted W_e and W_o:
        chol_e = cholesky_lower_arb(w_e)
        chol_o = cholesky_lower_arb(w_o)
        min_piv_e = chol_e[0][0]
        min_piv_o = chol_o[0][0]
        for i in range(1, n_modes):
            if chol_e[i][i] < min_piv_e:
                min_piv_e = chol_e[i][i]
            if chol_o[i][i] < min_piv_o:
                min_piv_o = chol_o[i][i]

        # Shifted Block-Schur complement S_4^even(a; C_* = 8) on head 0..3 vs tail 4..7:
        c_shift = arb(8)
        w00 = arb_mat(4, 4)
        w01 = arb_mat(4, 4)
        w11 = arb_mat(4, 4)
        for i in range(4):
            for j in range(4):
                w00[i, j] = w_e[i][j] + (c_shift if i == j else arb(0))
                w01[i, j] = w_e[i][j + 4]
                w11[i, j] = w_e[i + 4][j + 4] + (c_shift if i == j else arb(0))
        schur_4 = w00 - w01 * w11.solve(w01.transpose(), algorithm="precond")
        schur_4_list = [[schur_4[i, j] for j in range(4)] for i in range(4)]
        chol_schur_4 = cholesky_lower_arb(schur_4_list)

        # Frobenius norm of T_arith on finite 4-mode Legendre shell 4..7 vs triangle-inequality bound:
        frob_sq_tail_e = arb(0)
        for i in range(4, 8):
            for j in range(4, 8):
                frob_sq_tail_e += t_arith_e[i][j] * t_arith_e[i][j]
        frob_tail_e = frob_sq_tail_e.sqrt()
        cancellation_ratio = tri_sum / frob_tail_e

        # Candidate III: NS57 perturbation delta_2 = -log(2)/100
        # Certify in pure flint.arb via ball Cholesky that (2|delta_2|) I_8 +- B_{delta_2} > 0,
        # which by Weyl's inequality certifies |lambda_k(W_lambda^{delta_2}) - lambda_k(W_lambda)| < 2|delta_2|:
        weyl_plus = [
            [(two_abs_delta_ns57 if i == j else arb(0)) + delta_ns57 * s2_mat_e[i][j] for j in range(n_modes)]
            for i in range(n_modes)
        ]
        weyl_minus = [
            [(two_abs_delta_ns57 if i == j else arb(0)) - delta_ns57 * s2_mat_e[i][j] for j in range(n_modes)]
            for i in range(n_modes)
        ]
        chol_weyl_plus = cholesky_lower_arb(weyl_plus)
        chol_weyl_minus = cholesky_lower_arb(weyl_minus)
        min_piv_weyl_plus = chol_weyl_plus[0][0]
        min_piv_weyl_minus = chol_weyl_minus[0][0]
        for i in range(1, n_modes):
            if chol_weyl_plus[i][i] < min_piv_weyl_plus:
                min_piv_weyl_plus = chol_weyl_plus[i][i]
            if chol_weyl_minus[i][i] < min_piv_weyl_minus:
                min_piv_weyl_minus = chol_weyl_minus[i][i]

        # Candidate II / IIb: Compressed 8-mode Legendre projections of h(x), h'(x), and x*h(x)
        v_h: list[arb] = []
        v_dh: list[arb] = []
        v_xh: list[arb] = []
        for i in range(n_modes):
            me = 2 * i
            mo = 2 * i + 1
            ne = (arb(2 * me + 1) / (arb(2) * a)).sqrt()
            no = (arb(2 * mo + 1) / (arb(2) * a)).sqrt()
            ih = arb(2) * ne * acb.integral(
                lambda x, _, m_idx=me: eval_poly_acb(leg_polys[m_idx], x / a_acb) * h_and_dh_acb(x)[0],
                acb(0),
                a_acb,
                rel_tol=tol,
                abs_tol=tol,
            ).real
            idh = arb(2) * no * acb.integral(
                lambda x, _, m_idx=mo: eval_poly_acb(leg_polys[m_idx], x / a_acb) * h_and_dh_acb(x)[1],
                acb(0),
                a_acb,
                rel_tol=tol,
                abs_tol=tol,
            ).real
            ixh = arb(2) * no * acb.integral(
                lambda x, _, m_idx=mo: eval_poly_acb(leg_polys[m_idx], x / a_acb) * x * h_and_dh_acb(x)[0],
                acb(0),
                a_acb,
                rel_tol=tol,
                abs_tol=tol,
            ).real
            v_h.append(ih)
            v_dh.append(idh)
            v_xh.append(ixh)

        def rayleigh_and_res_arb(mat: list[list[arb]], vec: list[arb]) -> tuple[arb, arb]:
            n2 = sum((x * x for x in vec), arb(0))
            mv = [sum((mat[r][c] * vec[c] for c in range(len(vec))), arb(0)) for r in range(len(vec))]
            rq = sum((vec[r] * mv[r] for r in range(len(vec))), arb(0)) / n2
            res = (sum((x * x for x in mv), arb(0)) / n2).sqrt()
            return rq, res

        rq_h, res_h = rayleigh_and_res_arb(w_e, v_h)
        rq_dh, res_dh = rayleigh_and_res_arb(w_o, v_dh)
        rq_xh, res_xh = rayleigh_and_res_arb(w_o, v_xh)
        assert res_xh > res_dh

        # Full-space infinite-dimensional L^2(-a,a) Parseval orthogonal tail enclosures
        # ||(I - P_8)f||_{L^2(-a,a)}^2 = ||f||_{L^2(-a,a)}^2 - ||P_8 f||_2^2 on V_8(-a,a)^perp:
        l2_sq_h = (
            arb(2)
            * acb.integral(
                lambda x, _: h_and_dh_acb(x)[0] ** 2,
                acb(0),
                a_acb,
                rel_tol=tol,
                abs_tol=tol,
            ).real
        )
        l2_sq_xh = (
            arb(2)
            * acb.integral(
                lambda x, _: (x * h_and_dh_acb(x)[0]) ** 2,
                acb(0),
                a_acb,
                rel_tol=tol,
                abs_tol=tol,
            ).real
        )
        p8_sq_h = sum((c * c for c in v_h), arb(0))
        p8_sq_xh = sum((c * c for c in v_xh), arb(0))
        parseval_tail_sq_h = l2_sq_h - p8_sq_h
        parseval_tail_sq_xh = l2_sq_xh - p8_sq_xh
        assert parseval_tail_sq_h > arb(0)
        assert parseval_tail_sq_xh > arb(0)
        rel_parseval_tail_h = (parseval_tail_sq_h / l2_sq_h).sqrt()
        rel_parseval_tail_xh = (parseval_tail_sq_xh / l2_sq_xh).sqrt()

        # Full-space rank-2 polar eigenvalues on L^2_even(-a,a) and L^2_odd(-a,a)
        # and lem:v150-weight exterior pole-leakage bound 2 * int_a^inf cosh(x/2) h(x) dx:
        pole_op_norm_even = arb(2) * (a + a.sinh())
        pole_op_norm_odd = arb(2) * (a.sinh() - a)
        pi_val = arb.pi()
        lam_sq = arb(lam_int * lam_int)
        exterior_pole_tail_bound = (
            arb(32)
            * pi_val
            * pi_val
            * (arb(lam_int) ** 5)
            * (-pi_val * lam_sq).exp()
            / (arb(3).sqrt() * (arb(2) * pi_val * lam_sq - arb(5)))
        )
        assert exterior_pole_tail_bound > arb(0)

        # Full-space exact inner products <f, (T_pole(a) - T_arith(a)) f>_{L^2(-a,a)}
        # and exact omitted V_8(a)^perp couplings for f = h(x) and f = x*h(x):
        tol_ap = tol
        ih_pole_a = arb(2) * acb.integral(
            lambda x, _: (x / acb(2)).cosh() * h_and_dh_acb(x)[0],
            acb(0),
            a_acb,
            rel_tol=tol_ap,
            abs_tol=tol_ap,
        ).real
        ixh_pole_a = arb(2) * acb.integral(
            lambda x, _: x * (x / acb(2)).sinh() * h_and_dh_acb(x)[0],
            acb(0),
            a_acb,
            rel_tol=tol_ap,
            abs_tol=tol_ap,
        ).real
        full_pole_qf_h = arb(2) * ih_pole_a * ih_pole_a
        full_pole_qf_xh = -arb(2) * ixh_pole_a * ixh_pole_a

        full_arith_qf_h = arb(0)
        full_arith_qf_xh = arb(0)
        for k in range(2, lam_int * lam_int):
            if lam_arr[k] > arb(0):
                lk = arb(k).log()
                if lk < two_a:
                    wk = lam_arr[k] / arb(k).sqrt()
                    hlk_arb = lk / arb(2)
                    half_lk = acb(hlk_arb)
                    rem_arb = a - hlk_arb
                    # Split at u_split = min(a - lk/2, lk/2) (exact integer branch k >= lam_int)
                    # so all real contour inputs to h_and_dh_acb lie in [0, a]:
                    if k >= lam_int:
                        u_split = acb(rem_arb)
                        conv_h_k = arb(2) * acb.integral(
                            lambda u, _, hlk=half_lk: h_and_dh_acb(hlk + u)[0] * h_and_dh_acb(hlk - u)[0],
                            acb(0),
                            u_split,
                            rel_tol=tol_ap,
                            abs_tol=tol_ap,
                        ).real
                        conv_xh_k = arb(2) * acb.integral(
                            lambda u, _, hlk=half_lk: (u * u - hlk * hlk)
                            * h_and_dh_acb(hlk + u)[0]
                            * h_and_dh_acb(hlk - u)[0],
                            acb(0),
                            u_split,
                            rel_tol=tol_ap,
                            abs_tol=tol_ap,
                        ).real
                    else:
                        u_split = half_lk
                        v_max = acb(a - lk)
                        lk_acb = acb(lk)
                        conv_h_1 = acb.integral(
                            lambda u, _, hlk=half_lk: h_and_dh_acb(hlk + u)[0] * h_and_dh_acb(hlk - u)[0],
                            acb(0),
                            u_split,
                            rel_tol=tol_ap,
                            abs_tol=tol_ap,
                        ).real
                        conv_h_2 = acb.integral(
                            lambda v, _, lkc=lk_acb: h_and_dh_acb(lkc + v)[0] * h_and_dh_acb(v)[0],
                            acb(0),
                            v_max,
                            rel_tol=tol_ap,
                            abs_tol=tol_ap,
                        ).real
                        conv_h_k = arb(2) * (conv_h_1 + conv_h_2)
                        conv_xh_1 = acb.integral(
                            lambda u, _, hlk=half_lk: (u * u - hlk * hlk)
                            * h_and_dh_acb(hlk + u)[0]
                            * h_and_dh_acb(hlk - u)[0],
                            acb(0),
                            u_split,
                            rel_tol=tol_ap,
                            abs_tol=tol_ap,
                        ).real
                        conv_xh_2 = acb.integral(
                            lambda v, _, lkc=lk_acb: v
                            * (v + lkc)
                            * h_and_dh_acb(lkc + v)[0]
                            * h_and_dh_acb(v)[0],
                            acb(0),
                            v_max,
                            rel_tol=tol_ap,
                            abs_tol=tol_ap,
                        ).real
                        conv_xh_k = arb(2) * (conv_xh_1 + conv_xh_2)
                    full_arith_qf_h += arb(2) * wk * conv_h_k
                    full_arith_qf_xh += arb(2) * wk * conv_xh_k

        full_ap_qf_h = full_pole_qf_h - full_arith_qf_h
        full_ap_qf_xh = full_pole_qf_xh - full_arith_qf_xh
        comp_ap_qf_h = sum(
            (v_h[r] * (t_pole_e[r][c] - t_arith_e[r][c]) * v_h[c] for r in range(n_modes) for c in range(n_modes)),
            arb(0),
        )
        comp_ap_qf_xh = sum(
            (v_xh[r] * (t_pole_o[r][c] - t_arith_o[r][c]) * v_xh[c] for r in range(n_modes) for c in range(n_modes)),
            arb(0),
        )
        omitted_ap_coupling_h = full_ap_qf_h - comp_ap_qf_h
        omitted_ap_coupling_xh = full_ap_qf_xh - comp_ap_qf_xh

        window_rows.append({
            "lambda": lam_int,
            "a": arb_to_dict(a),
            "n_active_prime_power_shifts": n_shifts,
            "triangle_inequality_bound": arb_to_dict(tri_sum),
            "finite_shell_4_to_7_frob_norm_T_arith_even": arb_to_dict(frob_tail_e),
            "finite_shell_4_to_7_cancellation_factor": arb_to_dict(cancellation_ratio),
            "even_8x8_min_cholesky_pivot": arb_to_dict(min_piv_e),
            "odd_8x8_min_cholesky_pivot": arb_to_dict(min_piv_o),
            "shifted_schur_4x4_C8_min_cholesky_pivot": arb_to_dict(chol_schur_4[3][3]),
            "ns57_perturbation_bound_2abs_delta2": arb_to_dict(two_abs_delta_ns57),
            "ns57_weyl_plus_min_cholesky_pivot": arb_to_dict(min_piv_weyl_plus),
            "ns57_weyl_minus_min_cholesky_pivot": arb_to_dict(min_piv_weyl_minus),
            "compressed_8mode_h_even_rayleigh": arb_to_dict(rq_h),
            "compressed_8mode_h_even_residual": arb_to_dict(res_h),
            "compressed_8mode_dh_odd_rayleigh": arb_to_dict(rq_dh),
            "compressed_8mode_dh_odd_residual": arb_to_dict(res_dh),
            "compressed_8mode_xh_odd_rayleigh": arb_to_dict(rq_xh),
            "compressed_8mode_xh_odd_residual": arb_to_dict(res_xh),
            "full_space_h_even_l2_norm_sq": arb_to_dict(l2_sq_h),
            "full_space_h_even_rel_parseval_tail": arb_to_dict(rel_parseval_tail_h),
            "full_space_xh_odd_l2_norm_sq": arb_to_dict(l2_sq_xh),
            "full_space_xh_odd_rel_parseval_tail": arb_to_dict(rel_parseval_tail_xh),
            "full_space_pole_op_norm_even": arb_to_dict(pole_op_norm_even),
            "full_space_pole_op_norm_odd": arb_to_dict(pole_op_norm_odd),
            "full_space_exterior_pole_leakage_bound": arb_to_dict(exterior_pole_tail_bound),
            "full_space_ap_quadratic_form_h_even": arb_to_dict(full_ap_qf_h),
            "omitted_v8_perp_ap_coupling_h_even": arb_to_dict(omitted_ap_coupling_h),
            "full_space_ap_quadratic_form_xh_odd": arb_to_dict(full_ap_qf_xh),
            "omitted_v8_perp_ap_coupling_xh_odd": arb_to_dict(omitted_ap_coupling_xh),
        })

    # -----------------------------------------------------------------------
    # 3. Theorem 2: Exact Closed-Form Odd Pole Moment of x*h(x) & Xi'(gamma_1)
    # -----------------------------------------------------------------------
    rho1 = acb.zeta_zero(1)
    s_ser = flint.acb_series([rho1, acb(0, 1)], prec=2)
    z_ser = s_ser.zeta()
    assert z_ser[0].contains(0)
    half_s0 = rho1 / acb(2)
    pi = arb.pi()
    pi_acb = acb(pi)
    p0 = acb(arb(1) / arb(2)) * rho1 * (rho1 - acb(1)) * (pi_acb ** (-half_s0)) * half_s0.gamma()
    xi_at_gamma1 = (p0 * z_ser[0]).real
    dxi_at_gamma1 = (p0 * z_ser[1]).real
    assert xi_at_gamma1.contains(0)
    assert arb_abs(dxi_at_gamma1) > arb("0.00138")

    # Integral on [0, 3.5] plus certified two-sided lem:v150-weight tail enclosure on [3.5, infinity):
    # By lem:v150-weight (eq:v150-weight-bounds), A_- e^{9x/2 - pi e^{2x}} <= h(x) <= A_+ e^{9x/2 - pi e^{2x}}
    # with A_- = 4*pi*(2*pi - 3)/sqrt(3) and A_+ = 16*pi^2/sqrt(3).
    # Since -(d/dx)(x e^{3x - pi e^{2x}}) = (2*pi - (3 + 1/x) e^{-2x}) x e^{5x - pi e^{2x}},
    # integrating on [x0, infinity) at x0 = 3.5 (w0 = e^7) yields the exact two-sided enclosure:
    x0_tail = arb("3.5")
    w0_tail = (arb(2) * x0_tail).exp()
    a_minus_v150 = arb(4) * pi * (arb(2) * pi - arb(3)) / arb(3).sqrt()
    a_plus_v150 = arb(16) * pi * pi / arb(3).sqrt()
    tail_35_lower = (
        (arb(1) - (-x0_tail).exp())
        * a_minus_v150
        * x0_tail
        * (arb(3) * x0_tail - pi * w0_tail).exp()
        / (arb(2) * pi)
    )
    tail_35_upper = (
        a_plus_v150
        * x0_tail
        * (arb(3) * x0_tail - pi * w0_tail).exp()
        / (arb(2) * pi - (arb(3) + arb(1) / x0_tail) * (-arb(2) * x0_tail).exp())
    )
    assert tail_35_lower > arb("8.53e-1492")
    assert tail_35_upper > tail_35_lower

    # Kernel enclosure self-checks on negative inputs and complex quadrature boxes:
    h_neg_17, dh_neg_17 = h_and_dh_acb(acb(arb("-1.7")))
    h_pos_17, dh_pos_17 = h_and_dh_acb(acb(arb("1.7")))
    assert h_neg_17.real > arb(0)
    assert (h_neg_17 - h_pos_17).contains(0)
    assert (dh_neg_17 + dh_pos_17).contains(0)
    z_wide = acb(arb("1.0", "1.0"), arb("0.0", "1.0"))
    assert not h_and_dh_acb(z_wide)[0].is_finite()
    z_box = acb(arb("-0.05", "0.08"), arb("0.10", "0.08"))
    z_sample = acb(arb("-0.10"), arb("0.15"))
    assert z_box.contains(z_sample)
    hb_box, dhb_box = h_and_dh_acb(z_box, n0=16)
    hs_pt, dhs_pt = h_and_dh_acb(z_sample, n0=32)
    assert hb_box.contains(hs_pt)
    assert dhb_box.contains(dhs_pt)

    m1_num = (
        arb(2)
        * acb.integral(
            lambda x, _: x * (x / acb(2)).sinh() * h_and_dh_acb(x)[0],
            acb(0),
            acb(x0_tail),
            rel_tol=tol,
            abs_tol=tol,
        ).real
        + arb(0, tail_35_upper)
    )
    gamma_e = -acb(1).digamma().real
    m1_closed = (arb(1) + (gamma_e - (arb(4) * pi).log()) / arb(2)) / arb(3).sqrt()
    diff_m1 = m1_num - m1_closed
    assert diff_m1.contains(0), f"Odd pole moment identity failed: {diff_m1}"
    assert m1_closed > arb("0.0133")

    theorem_2_cert = {
        "gamma_1": arb_to_dict(rho1.imag),
        "Xi_at_gamma1": arb_to_dict(xi_at_gamma1),
        "Xi_at_gamma1_contains_zero": True,
        "dXi_at_gamma1": arb_to_dict(dxi_at_gamma1),
        "odd_pole_moment_xh_numerical": arb_to_dict(m1_num),
        "odd_pole_moment_xh_closed_form": arb_to_dict(m1_closed),
        "odd_pole_moment_diff": arb_to_dict(diff_m1),
        "odd_pole_moment_contains_zero": True,
        "odd_pole_moment_tail_35_lower_bound": arb_to_dict(tail_35_lower),
        "odd_pole_moment_tail_35_upper_bound": arb_to_dict(tail_35_upper),
        "h_at_minus_1_7": arb_to_dict(h_neg_17.real),
    }

    # -----------------------------------------------------------------------
    # 4. Candidates A, B, and C in NB-GAIN across N in {4, 8, 16, 32}
    # -----------------------------------------------------------------------
    # Exact NS83 q=2 transformed target Mellin value T_2(s) = (s - 1) / s^3 (eq:ns83-transforms):
    t2_rho1 = (rho1 - acb(1)) / (rho1**3)
    abs_t2_rho1 = abs(t2_rho1)
    inv_abs_rho1_sq = arb(1) / (arb(1) / arb(4) + rho1.imag * rho1.imag)
    assert (abs_t2_rho1 - inv_abs_rho1_sq).contains(0)
    pair_weight_q2_rho1 = arb(2) * inv_abs_rho1_sq * inv_abs_rho1_sq
    c2_50 = arb(0)
    for j in range(1, 51):
        gj = acb.zeta_zero(j).imag
        c2_50 += arb(2) / ((arb(1) / arb(4) + gj * gj) ** 2)

    u_minus_1 = [Fraction(-1), Fraction(1)]
    two_minus_u = [Fraction(2), Fraction(-1)]
    two_u_minus_3 = [Fraction(-3), Fraction(2)]
    psi_deg7 = p_mul(
        p_mul(u_minus_1, p_mul(u_minus_1, u_minus_1)),
        p_mul(p_mul(two_minus_u, p_mul(two_minus_u, two_minus_u)), two_u_minus_3),
    )

    max_idx = 64
    kernel = Kernel(max_idx, 128, 24)
    gram = arb_mat(max_idx, max_idx)
    loads_orig = arb_mat(max_idx, 1)
    beta_ctrl = arb(1) / arb(2) + arb(1) / arb(100)
    slope_ctrl = (arb(1) - beta_ctrl) / beta_ctrl
    const_ctrl = (arb(2) * beta_ctrl - arb(1)) / (beta_ctrl * beta_ctrl)
    loads_ns74 = arb_mat(max_idx, 1)

    for m in range(1, max_idx + 1):
        lk_val = kernel.load(m)
        loads_orig[m - 1, 0] = lk_val
        loads_ns74[m - 1, 0] = (
            slope_ctrl * lk_val
            - const_ctrl * (kernel.logs[m] + arb(2) - arb.const_euler() + arb(1) / beta_ctrl) / m
        )
        for n in range(m, max_idx + 1):
            gram[m - 1, n - 1] = gram[n - 1, m - 1] = kernel.gram(m, n)

    nb_rows: list[dict[str, Any]] = []
    for n_size in (4, 8, 16, 32):
        g_old = sub(gram, 0, n_size, 0, n_size)
        c_cross = sub(gram, 0, n_size, n_size, 2 * n_size)
        d_new = sub(gram, n_size, 2 * n_size, n_size, 2 * n_size)
        cg_inv_c = c_cross.transpose() * g_old.solve(c_cross, algorithm="precond")
        s_schur = d_new - cg_inv_c

        b_old = sub(loads_orig, 0, n_size, 0, 1)
        b_new = sub(loads_orig, n_size, 2 * n_size, 0, 1)
        c_old = g_old.solve(b_old, algorithm="precond")
        h_vec = b_new - c_cross.transpose() * c_old
        y_vec = s_schur.solve(h_vec, algorithm="precond")
        u_vec = -g_old.solve(c_cross * y_vec, algorithm="precond")

        b_old_74 = sub(loads_ns74, 0, n_size, 0, 1)
        b_new_74 = sub(loads_ns74, n_size, 2 * n_size, 0, 1)
        c_old_74 = g_old.solve(b_old_74, algorithm="precond")
        h_vec_74 = b_new_74 - c_cross.transpose() * c_old_74
        y_vec_74 = s_schur.solve(h_vec_74, algorithm="precond")
        u_vec_74 = -g_old.solve(c_cross * y_vec_74, algorithm="precond")

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

        # Candidate A check on both original and NS74:
        m_schur_orig = dot(lam_proj, y_vec)
        m_div_orig = arb(0)
        m_schur_74 = dot(lam_proj, y_vec_74)
        m_div_74 = arb(0)
        for idx, n in enumerate(range(n_size + 1, 2 * n_size)):
            div_sum = y_vec[idx, 0] + sum(
                (u_vec[m - 1, 0] for m in range(1, n_size + 1) if n % m == 0), arb(0)
            )
            m_div_orig += lam_new[idx, 0] * div_sum
            div_sum_74 = y_vec_74[idx, 0] + sum(
                (u_vec_74[m - 1, 0] for m in range(1, n_size + 1) if n % m == 0), arb(0)
            )
            m_div_74 += lam_new[idx, 0] * div_sum_74
        assert (m_schur_orig - m_div_orig).contains(0)
        assert (m_schur_74 - m_div_74).contains(0)

        # Candidate B & C metrics:
        e_n = arb(2) - dot(b_old, c_old)
        delta_n = dot(h_vec, y_vec)
        log_n = arb(n_size).log()
        log_n_e_n = log_n * e_n
        norm_step_rate = (log_n / arb(2).log()) * (delta_n / e_n)
        assert log_n_e_n > c2_50

        tr_d = sum((d_new[i, i] for i in range(n_size)), arb(0))
        tr_h = sum((s_schur[i, i] for i in range(n_size)), arb(0))
        tr_ratio = tr_h / tr_d
        norm2_bnew = dot(b_new, b_new)
        norm2_h = dot(h_vec, h_vec)
        load_refit_ratio = norm2_h / norm2_bnew

        nb_rows.append({
            "N": n_size,
            "E_N": arb_to_dict(e_n),
            "Delta_N": arb_to_dict(delta_n),
            "logN_times_E_N": arb_to_dict(log_n_e_n),
            "normalized_dyadic_step_rate": arb_to_dict(norm_step_rate),
            "tr_H_N_over_tr_D_N": arb_to_dict(tr_ratio),
            "norm2_h_N_over_norm2_b_new": arb_to_dict(load_refit_ratio),
            "cand_A_divisor_pairing_orig": arb_to_dict(m_schur_orig),
            "cand_A_divisor_pairing_ns74": arb_to_dict(m_schur_74),
            "cand_A_both_identities_contain_zero": True,
        })

    return {
        "prec_bits": prec_bits,
        "theorem_1_abel_legendre_pole_cancellation": abel_legendre_checks,
        "weil_floor_and_kernel_api_windows": window_rows,
        "theorem_2_critical_zero_and_odd_pole_moment": theorem_2_cert,
        "nb_gain_candidates_a_b_c": {
            "abs_T2_at_rho1": arb_to_dict(abs_t2_rho1),
            "pair_weight_q2_at_rho1": arb_to_dict(pair_weight_q2_rho1),
            "ns83_50_pair_floor_C2_50": arb_to_dict(c2_50),
            "dyadic_rows": nb_rows,
        },
    }


def collect_arb_dicts(obj: Any, path: str, out: dict[str, dict[str, Any]]) -> None:
    if isinstance(obj, dict):
        if "str" in obj and "mid" in obj and "rad" in obj:
            out[path] = obj
        else:
            for k, v in obj.items():
                collect_arb_dicts(v, f"{path}.{k}" if path else k, out)
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            collect_arb_dicts(item, f"{path}[{idx}]", out)


def main() -> None:
    res_256 = run_all_candidate_tests_at_precision(256)
    res_384 = run_all_candidate_tests_at_precision(384)

    balls_256: dict[str, dict[str, Any]] = {}
    balls_384: dict[str, dict[str, Any]] = {}
    collect_arb_dicts(res_256, "", balls_256)
    collect_arb_dicts(res_384, "", balls_384)
    assert set(balls_256.keys()) == set(balls_384.keys())

    ctx.prec = 384
    n_overlaps = 0
    for key in sorted(balls_256.keys()):
        b256 = arb(balls_256[key]["str"])
        b384 = arb(balls_384[key]["str"])
        assert b256.overlaps(b384), f"Ball overlap failed at {key}: {b256} vs {b384}"
        n_overlaps += 1

    # Non-overlapping self-test (1 + 2^-100 vs 1 + 2^-101):
    a_test = arb(1) + arb(2) ** (-100)
    b_test = arb(1) + arb(2) ** (-101)
    assert not a_test.overlaps(b_test)

    payload_core = {
        "audit": "cofinal-candidate-mechanisms-screen-2026-10-16-v1",
        "lanes": ["WEIL-FLOOR", "KERNEL-API", "NB-GAIN"],
        "dual_precision_ball_overlap_checks": {
            "total_checked": n_overlaps,
            "all_passed": True,
            "non_overlapping_self_test_passed": True,
        },
        "cert_256": res_256,
        "cert_384": res_384,
        "open_status_disclosure": {
            "RH": "OPEN",
            "G2": "OPEN",
            "WEIL_FLOOR_cofinal_bound": "OPEN",
            "KERNEL_API_full_window_injectivity": "OPEN",
            "NB_GAIN_cofinal_actual_residual_decrease": "OPEN",
            "historical_missing_original_evidence_groups": "OPEN",
        },
    }
    payload_sha256 = hashlib.sha256(
        json.dumps(payload_core, sort_keys=True).encode("utf-8")
    ).hexdigest()
    full_out = {
        "audit_integrity": {
            "sha256_of_payload": payload_sha256,
        },
        **payload_core,
    }
    out_path = Path(__file__).resolve().parent / "verification.json"
    out_bytes = (json.dumps(full_out, indent=2) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    file_sha256 = hashlib.sha256(out_bytes).hexdigest()
    print(
        f"PASS: {n_overlaps}/{n_overlaps} two-precision ball overlaps verified. "
        f"payload_sha256={payload_sha256} file_sha256={file_sha256}"
    )


if __name__ == "__main__":
    main()
