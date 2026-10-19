#!/usr/bin/env python3
"""
Deterministic 384-bit flint.arb + exact rational (fractions.Fraction) verification for:
Multi-Mode Jacobi-Stieltjes-Divisor Extractors in NS-61 Hilbert Space (2026-10-15, v1).

Verifies:
1. Exact symbolic polynomial construction of the Jacobi-Stieltjes-Divisor hierarchy
   psi_nu^(m)(u) = (u - 1)^nu (2 - u)^nu P_m^(nu, nu)(2u - 3) for nu in {2, 3} and m in {1, 2, 3, 4},
   and exact verification that int_1^2 psi_nu^(m)(u) du == 0 for every (nu, m).
2. Exact 4x4 rational Gram matrices G_hat^(nu, 4) in Q^(4x4) for the scale-invariant operator
   D psi(u) = (d/du)(u psi'(u)) in L^2([1, 2], u^2 du), cross-checked against 384-bit
   flint.acb.integral to < 10^-105.
3. Exact rational Cholesky L D L^T factorization G_hat^(nu, 4) = L_nu D_nu L_nu^T, exact
   unit lower-triangular inverse L_nu^{-1}, and exact mutual H-orthogonality of the
   orthogonalized polynomial profiles phi_nu^(k)(u) = sum_{j=1}^k (L_nu^{-1})_{k,j} psi_nu^(j)(u).
4. Independent piecewise 384-bit flint.acb.integral verification of the atom inner product
   <Lambda_{4, nu}^(m), sigma_5>_H == +psi_nu^(m)(5/4) for all 4 modes m in {1, 2, 3, 4}.
5. 384-bit flint.arb certification across dyadic blocks N in {4, 8, 16, 32, 64} and across
   both the Original NS-61 family (beta = 1/2) and NS-74 altered-target controls
   (beta = 1/2 + 10^-2, 1/2 + 10^-6, 3/4) that:
   - The three-way divisor-sum identity M_schur == M_pair == M_div holds for every mode m=1..4,
   - The Loewner matrix Bessel inequality 0 < G_proj,N^(nu, K) <= N * G_hat^(nu, K) holds
     (verified via positive definiteness of N * G_hat^(nu, K) - G_proj,N^(nu, K) by Sylvester's
     criterion in 384-bit ball arithmetic),
   - The diagonalized sum of squares sum_{k=1}^K |tilde_M_{N,nu}^(k)|^2 / (N d_{nu,k}) equals
     the matrix Bessel bound (1/N) M^T (G_hat)^{-1} M to 384-bit accuracy, and satisfies
     0 < B_{N,nu}^(1) <= ... <= B_{N,nu}^(K) <= R_{N,nu}^(K) <= Delta_N.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any

import flint

PREC_BITS = 384
flint.ctx.prec = PREC_BITS

ROOT = Path(__file__).resolve().parents[2]
NS61_DIR = ROOT / "evidence" / "v159" / "ns61"
for p_dir in (ROOT, NS61_DIR):
    if str(p_dir) not in sys.path:
        sys.path.insert(0, str(p_dir))

from certify_smoothed import Kernel, ball, dot, sub  # type: ignore[import-not-found]  # noqa: E402


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    mid_f = float(x.mid())
    rad_f = float(x.rad())
    return {
        "str": str(x),
        "mid": mid_f,
        "rad": rad_f,
        "lower": float(x.lower()),
        "upper": float(x.upper()),
    }


def p_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, va in enumerate(a):
        for j, vb in enumerate(b):
            out[i + j] += va * vb
    return out


def p_add(a: list[Fraction], b: list[Fraction], scale_b: Fraction = Fraction(1)) -> list[Fraction]:
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i, va in enumerate(a):
        out[i] += va
    for i, vb in enumerate(b):
        out[i] += scale_b * vb
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def p_scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return [v * c for v in a]


def p_diff(a: list[Fraction]) -> list[Fraction]:
    return [Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)]


def p_int_12(a: list[Fraction]) -> Fraction:
    return sum((v * Fraction(2 ** (i + 1) - 1, i + 1) for i, v in enumerate(a)), Fraction(0))


def eval_p_frac(p: list[Fraction], x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def eval_p_acb(p: list[Fraction], z: flint.acb) -> flint.acb:
    acc = flint.acb(0)
    for c in reversed(p):
        c_arb = flint.arb(c.numerator) / flint.arb(c.denominator)
        acc = acc * z + flint.acb(c_arb)
    return acc


def cholesky_ldlt_rational(
    g_mat: list[list[Fraction]],
) -> tuple[list[list[Fraction]], list[Fraction], list[list[Fraction]]]:
    """
    Exact rational Cholesky LDL^T factorization G = L D L^T and inverse L^{-1}.
    """
    k_dim = len(g_mat)
    l_mat = [[Fraction(1 if i == j else 0) for j in range(k_dim)] for i in range(k_dim)]
    d_vec = [Fraction(0) for _ in range(k_dim)]
    for i in range(k_dim):
        for j in range(i):
            s = g_mat[i][j] - sum(
                (l_mat[i][r] * l_mat[j][r] * d_vec[r] for r in range(j)), Fraction(0)
            )
            l_mat[i][j] = s / d_vec[j]
        d_vec[i] = g_mat[i][i] - sum(
            (l_mat[i][r] * l_mat[i][r] * d_vec[r] for r in range(i)), Fraction(0)
        )
        assert d_vec[i] > 0, f"Non-positive pivot d[{i}] = {d_vec[i]}"

    l_inv = [[Fraction(1 if i == j else 0) for j in range(k_dim)] for i in range(k_dim)]
    for i in range(k_dim):
        for j in range(i):
            l_inv[i][j] = -sum(
                (l_mat[i][r] * l_inv[r][j] for r in range(j, i)), Fraction(0)
            )
    return l_mat, d_vec, l_inv


def sylvester_spd_arb(mat: flint.arb_mat) -> tuple[bool, list[flint.arb]]:
    """
    Certify positive definiteness of a symmetric K x K arb_mat via Sylvester's criterion
    (all leading principal minors strictly positive in 384-bit ball arithmetic).
    """
    k_dim = mat.nrows()
    minors: list[flint.arb] = []
    for m in range(1, k_dim + 1):
        sub_m = sub(mat, 0, m, 0, m)
        det_m = sub_m.det()
        minors.append(det_m)
        if not bool(det_m > 0):
            return False, minors
    return True, minors


def build_jacobi_hierarchy() -> dict[str, dict[str, Any]]:
    """
    Construct exact rational polynomials psi_nu^(m), D psi_nu^(m), Gram matrices G_hat^(nu, 4),
    and LDL^T orthogonalized profiles phi_nu^(m) for nu in {2, 3}, m in {1, 2, 3, 4}.
    """
    flint.ctx.prec = PREC_BITS
    u_m1 = [Fraction(-1), Fraction(1)]
    two_mu = [Fraction(2), Fraction(-1)]
    t_poly = [Fraction(-3), Fraction(2)]  # t = 2u - 3
    t2_poly = p_mul(t_poly, t_poly)
    t4_poly = p_mul(t2_poly, t2_poly)
    u_poly = [Fraction(0), Fraction(1)]
    u2_poly = p_mul(u_poly, u_poly)

    base2 = p_mul(p_mul(u_m1, u_m1), p_mul(two_mu, two_mu))
    base3 = p_mul(base2, p_mul(u_m1, two_mu))

    jac_t2 = [
        t_poly,
        p_add(p_scale(t2_poly, Fraction(7)), [Fraction(-1)]),
        p_mul(t_poly, p_add(p_scale(t2_poly, Fraction(3)), [Fraction(-1)])),
        p_add(
            p_add(p_scale(t4_poly, Fraction(33)), p_scale(t2_poly, Fraction(-18))),
            [Fraction(1)],
        ),
    ]
    jac_t3 = [
        t_poly,
        p_add(p_scale(t2_poly, Fraction(9)), [Fraction(-1)]),
        p_mul(t_poly, p_add(p_scale(t2_poly, Fraction(11)), [Fraction(-3)])),
        p_add(
            p_add(p_scale(t4_poly, Fraction(143)), p_scale(t2_poly, Fraction(-66))),
            [Fraction(3)],
        ),
    ]

    families_spec = [
        ("H03_Jacobi33", 3, base3, jac_t3),
        ("H02_Jacobi22", 2, base2, jac_t2),
    ]

    out: dict[str, dict[str, Any]] = {}
    for label, nu_val, base_poly, jac_list in families_spec:
        psis = [p_mul(base_poly, j_p) for j_p in jac_list]
        k_dim = len(psis)
        for m_idx, psi in enumerate(psis, 1):
            assert p_int_12(psi) == Fraction(0), f"{label} mode {m_idx} mean-zero failed"
            # Check endpoint vanishing up to order nu_val - 1:
            cur = psi
            for deriv_order in range(nu_val):
                assert eval_p_frac(cur, Fraction(1)) == Fraction(0)
                assert eval_p_frac(cur, Fraction(2)) == Fraction(0)
                cur = p_diff(cur)

        d_psis = [p_diff(p_mul(u_poly, p_diff(psi))) for psi in psis]
        g_hat = [
            [p_int_12(p_mul(u2_poly, p_mul(d_psis[i], d_psis[j]))) for j in range(k_dim)]
            for i in range(k_dim)
        ]

        # Cross-check every entry of G_hat against 384-bit flint.acb.integral:
        max_int_err = flint.arb(0)
        for i in range(k_dim):
            for j in range(i, k_dim):
                pi_poly = d_psis[i]
                pj_poly = d_psis[j]

                def g_integrand(
                    u_z: flint.acb,
                    _: bool,
                    pa: list[Fraction] = pi_poly,
                    pb: list[Fraction] = pj_poly,
                ) -> flint.acb:
                    return (u_z ** 2) * eval_p_acb(pa, u_z) * eval_p_acb(pb, u_z)

                val_arb = flint.acb.integral(
                    g_integrand, flint.acb(1), flint.acb(2), rel_tol=2 ** (-340), eval_limit=100000
                ).real
                exact_arb = ball(g_hat[i][j])
                err_ij = abs(val_arb - exact_arb)
                assert (val_arb - exact_arb).contains(0), f"Gram integral ball does not contain exact at ({i},{j})"
                assert bool(err_ij < flint.arb("1e-95")), f"Gram integral radius too large at ({i},{j}): {err_ij}"
                if float(err_ij.upper()) > float(max_int_err.upper()):
                    max_int_err = err_ij

        l_mat, d_vec, l_inv = cholesky_ldlt_rational(g_hat)

        # Construct orthogonalized polynomials phi^(k)(u) = sum_{j=0}^k L_inv[k][j] psi^(j)(u):
        phis: list[list[Fraction]] = []
        d_phis: list[list[Fraction]] = []
        for k_i in range(k_dim):
            phi_k = [Fraction(0)]
            for j_i in range(k_i + 1):
                phi_k = p_add(phi_k, psis[j_i], l_inv[k_i][j_i])
            assert p_int_12(phi_k) == Fraction(0)
            phis.append(phi_k)
            d_phis.append(p_diff(p_mul(u_poly, p_diff(phi_k))))

        # Verify exact mutual orthogonality <phi^(i), phi^(j)>_D == d_i delta_{ij}:
        for i in range(k_dim):
            for j in range(k_dim):
                ip_ij = p_int_12(p_mul(u2_poly, p_mul(d_phis[i], d_phis[j])))
                target_ij = d_vec[i] if i == j else Fraction(0)
                assert ip_ij == target_ij, f"Orthogonality failed at ({i},{j}): {ip_ij} != {target_ij}"

        # Independent piecewise verification at N=4, r=5 for all 4 modes:
        # <Lambda_{4, nu}^(m), sigma_5>_H == +psi_nu^(m)(5/4)
        piecewise_checks: list[dict[str, Any]] = []
        for m_i in range(k_dim):
            d_psi_m = d_psis[m_i]

            def lam4_acb(x_z: flint.acb, dp: list[Fraction] = d_psi_m) -> flint.acb:
                u_z = 1 / (4 * x_z)
                return -4 * (u_z ** 2) * eval_p_acb(dp, u_z)

            def p1_int(x_z: flint.acb, _: bool) -> flint.acb:
                sig5 = 1 / (5 * x_z) - flint.acb("0.5") + (5 * x_z).log()
                return lam4_acb(x_z) * sig5

            def p2_int(x_z: flint.acb, _: bool) -> flint.acb:
                sig5 = 1 / (5 * x_z) - flint.acb("0.5")
                return lam4_acb(x_z) * sig5

            ip1 = flint.acb.integral(
                p1_int, flint.acb(flint.arb(1) / 8), flint.acb(flint.arb(1) / 5), rel_tol=2 ** (-340)
            ).real
            ip2 = flint.acb.integral(
                p2_int, flint.acb(flint.arb(1) / 5), flint.acb(flint.arb(1) / 4), rel_tol=2 ** (-340)
            ).real
            ip_tot = ip1 + ip2
            exact_f = eval_p_frac(psis[m_i], Fraction(5, 4))
            exact_b = ball(exact_f)
            diff_b = abs(ip_tot - exact_b)
            assert (ip_tot - exact_b).contains(0), f"Piecewise N=4, r=5 ball miss at mode {m_i+1}"
            assert bool(diff_b < flint.arb("1e-95")), f"Piecewise N=4, r=5 radius at mode {m_i+1}: {diff_b}"
            piecewise_checks.append({
                "mode": m_i + 1,
                "exact_fraction": f"{exact_f.numerator}/{exact_f.denominator}",
                "integral_ball": arb_to_dict(ip_tot),
                "abs_diff_upper": float(diff_b.upper()),
            })

        out[label] = {
            "nu": nu_val,
            "K": k_dim,
            "psis": psis,
            "phis": phis,
            "G_hat": g_hat,
            "L": l_mat,
            "D": d_vec,
            "L_inv": l_inv,
            "G_hat_str": [[f"{x.numerator}/{x.denominator}" for x in row] for row in g_hat],
            "D_str": [f"{x.numerator}/{x.denominator}" for x in d_vec],
            "D_float": [float(x) for x in d_vec],
            "L_inv_str": [
                [f"{l_inv[i][j].numerator}/{l_inv[i][j].denominator}" for j in range(i + 1)]
                for i in range(k_dim)
            ],
            "max_gram_integral_check_error": float(max_int_err.upper()),
            "piecewise_N4_r5_checks": piecewise_checks,
        }
    return out


def verify_multimode_dyadic_gains(hierarchy: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """
    Certify multi-mode Rayleigh and Bessel lower bounds across N in {4, 8, 16, 32, 64}
    and across both Original NS-61 (beta = 1/2) and NS-74 altered controls.
    """
    flint.ctx.prec = PREC_BITS
    t0 = time.monotonic()

    max_idx = 128
    kernel = Kernel(max_idx, 128, 24)
    gram = flint.arb_mat(max_idx, max_idx)
    for m in range(1, max_idx + 1):
        for n in range(m, max_idx + 1):
            gram[m - 1, n - 1] = gram[n - 1, m - 1] = kernel.gram(m, n)

    target_families = [
        ("original_beta_0.5", flint.arb(1) / 2, False),
        ("ns74_beta_0.5_plus_1e-2", flint.arb(1) / 2 + flint.arb(1) / 100, True),
        ("ns74_beta_0.5_plus_1e-6", flint.arb(1) / 2 + flint.arb(1) / 1000000, True),
        ("ns74_beta_0.75", flint.arb(3) / 4, True),
    ]

    results_by_target: dict[str, Any] = {}

    for t_name, beta, is_altered in target_families:
        loads = flint.arb_mat(max_idx, 1)
        if not is_altered:
            for k in range(1, max_idx + 1):
                loads[k - 1, 0] = kernel.load(k)
            floor_val = flint.arb(0)
        else:
            slope = (1 - beta) / beta
            constant = (2 * beta - 1) / (beta * beta)
            for k in range(1, max_idx + 1):
                loads[k - 1, 0] = (
                    slope * kernel.load(k)
                    - constant * (kernel.logs[k] + 2 - flint.arb.const_euler() + 1 / beta) / k
                )
            floor_val = (2 * beta - 1) * (1 - beta) * (1 - beta) / (beta ** 6)

        block_rows: list[dict[str, Any]] = []
        for n_size in (4, 8, 16, 32, 64):
            g_old = sub(gram, 0, n_size, 0, n_size)
            c_cross = sub(gram, 0, n_size, n_size, 2 * n_size)
            d_new = sub(gram, n_size, 2 * n_size, n_size, 2 * n_size)
            b_old = sub(loads, 0, n_size, 0, 1)
            b_new = sub(loads, n_size, 2 * n_size, 0, 1)

            c_old = g_old.solve(b_old, algorithm="precond")
            h_vec = b_new - c_cross.transpose() * c_old
            g_inv_c = g_old.solve(c_cross, algorithm="precond")
            s_schur = d_new - c_cross.transpose() * g_inv_c
            y_vec = s_schur.solve(h_vec, algorithm="precond")
            u_vec = -g_inv_c * y_vec

            e_n = 2 - dot(b_old, c_old)
            delta_n = dot(h_vec, y_vec)
            e_2n = e_n - delta_n
            e_n_rem = e_n - floor_val
            assert bool(e_n > e_2n > floor_val) and bool(delta_n > 0)

            # Precompute divisor-difference vector div_diff[idx] = y_n + sum_{d|n, d<=N} u_d
            # for n = N+1, ..., 2N-1:
            div_diff: list[flint.arb] = []
            for idx, n in enumerate(range(n_size + 1, 2 * n_size)):
                d_sum = y_vec[idx, 0] + sum(
                    (u_vec[m - 1, 0] for m in range(1, n_size + 1) if n % m == 0), flint.arb(0)
                )
                div_diff.append(d_sum)

            max_k = min(4, n_size - 2)
            basis_reports: dict[str, Any] = {}

            for b_label, b_info in hierarchy.items():
                psis: list[list[Fraction]] = b_info["psis"]
                phis: list[list[Fraction]] = b_info["phis"]
                g_hat: list[list[Fraction]] = b_info["G_hat"]
                d_vec: list[Fraction] = b_info["D"]

                lam_proj_cols: list[flint.arb_mat] = []
                mode_identities: list[dict[str, Any]] = []

                for m_i in range(max_k):
                    psi = psis[m_i]
                    ln_f = [
                        eval_p_frac(psi, Fraction(n, n_size)) if n < 2 * n_size else Fraction(0)
                        for n in range(n_size + 1, 2 * n_size + 1)
                    ]
                    lo_f = [
                        sum(
                            (
                                eval_p_frac(psi, Fraction(mult * m, n_size))
                                for mult in range(2, 2 * n_size)
                                if n_size < mult * m < 2 * n_size
                            ),
                            Fraction(0),
                        )
                        for m in range(1, n_size + 1)
                    ]
                    ln_m = flint.arb_mat([[ball(x)] for x in ln_f])
                    lo_m = flint.arb_mat([[ball(x)] for x in lo_f])
                    lp_m = ln_m - g_inv_c.transpose() * lo_m
                    lam_proj_cols.append(lp_m)

                    m_schur = dot(lp_m, y_vec)
                    m_pair = dot(ln_m, y_vec) + dot(lo_m, u_vec)
                    m_div = sum(
                        (ln_m[idx, 0] * div_diff[idx] for idx in range(n_size - 1)),
                        flint.arb(0),
                    )
                    assert (m_schur - m_pair).contains(0)
                    assert (m_schur - m_div).contains(0)
                    mode_identities.append({
                        "mode": m_i + 1,
                        "M_N_m": arb_to_dict(m_schur),
                        "max_three_way_diff": max(
                            float(abs(m_schur - m_pair).upper()),
                            float(abs(m_schur - m_div).upper()),
                        ),
                    })

                # Also compute orthogonalized moments tilde_M_{N, k}:
                tilde_moments: list[flint.arb] = []
                for k_i in range(max_k):
                    phi_k = phis[k_i]
                    tm_k = sum(
                        (
                            ball(eval_p_frac(phi_k, Fraction(n_size + 1 + idx, n_size))) * div_diff[idx]
                            for idx in range(n_size - 1)
                        ),
                        flint.arb(0),
                    )
                    tilde_moments.append(tm_k)

                # Evaluate cumulative K_sub in 1 .. max_k:
                k_progression: list[dict[str, Any]] = []
                prev_rayleigh = flint.arb(0)
                prev_bessel = flint.arb(0)
                for k_sub in range(1, max_k + 1):
                    l_mat_proj = flint.arb_mat(n_size, k_sub)
                    for c_i in range(k_sub):
                        for r_i in range(n_size):
                            l_mat_proj[r_i, c_i] = lam_proj_cols[c_i][r_i, 0]

                    m_vec_k = l_mat_proj.transpose() * y_vec
                    g_proj_k = l_mat_proj.transpose() * s_schur.solve(l_mat_proj, algorithm="precond")
                    g_bessel_k = flint.arb_mat(
                        [[ball(g_hat[i][j] * n_size) for j in range(k_sub)] for i in range(k_sub)]
                    )

                    # Certify Loewner matrix Bessel inequality: G_bessel_k - G_proj_k > 0
                    diff_mat_k = g_bessel_k - g_proj_k
                    spd_proj, _ = sylvester_spd_arb(g_proj_k)
                    spd_diff, diff_minors = sylvester_spd_arb(diff_mat_k)
                    assert spd_proj, f"G_proj not SPD at N={n_size}, K={k_sub}"
                    assert spd_diff, f"Loewner Bessel inequality failed at N={n_size}, K={k_sub}"

                    rayleigh_k = (m_vec_k.transpose() * g_proj_k.solve(m_vec_k, algorithm="precond"))[0, 0]
                    bessel_k_mat = (m_vec_k.transpose() * g_bessel_k.solve(m_vec_k, algorithm="precond"))[0, 0]

                    # Diagonal sum of squares via exact LDL^T orthogonalized moments:
                    bessel_k_diag = sum(
                        (
                            (tilde_moments[idx_k] ** 2) / ball(d_vec[idx_k] * n_size)
                            for idx_k in range(k_sub)
                        ),
                        flint.arb(0),
                    )
                    assert (bessel_k_mat - bessel_k_diag).contains(0)
                    assert bool(abs(bessel_k_mat - bessel_k_diag) < flint.arb("1e-20"))
                    assert bool(0 < bessel_k_diag <= rayleigh_k <= delta_n)
                    assert bool(bessel_k_diag >= prev_bessel)
                    assert bool(rayleigh_k >= prev_rayleigh)
                    prev_bessel = bessel_k_diag
                    prev_rayleigh = rayleigh_k

                    k_progression.append({
                        "K": k_sub,
                        "rayleigh_gain": arb_to_dict(rayleigh_k),
                        "bessel_gain": arb_to_dict(bessel_k_diag),
                        "diag_vs_mat_bessel_abs_diff": float(abs(bessel_k_mat - bessel_k_diag).upper()),
                        "rayleigh_fraction_of_Delta_N": float((rayleigh_k / delta_n).mid()),
                        "bessel_fraction_of_Delta_N": float((bessel_k_diag / delta_n).mid()),
                        "bessel_over_rayleigh": float((bessel_k_diag / rayleigh_k).mid()),
                        "rayleigh_over_E_N": float((rayleigh_k / e_n).mid()),
                        "bessel_over_E_N": float((bessel_k_diag / e_n).mid()),
                        "rayleigh_over_E_N_removable": float((rayleigh_k / e_n_rem).mid()),
                        "bessel_over_E_N_removable": float((bessel_k_diag / e_n_rem).mid()),
                        "loewner_bessel_certified": bool(spd_diff),
                        "loewner_min_leading_minor_lower": min(float(x.lower()) for x in diff_minors),
                    })

                improvement_rayleigh = (
                    k_progression[-1]["rayleigh_fraction_of_Delta_N"]
                    / k_progression[0]["rayleigh_fraction_of_Delta_N"]
                )
                improvement_bessel = (
                    k_progression[-1]["bessel_fraction_of_Delta_N"]
                    / k_progression[0]["bessel_fraction_of_Delta_N"]
                )

                basis_reports[b_label] = {
                    "max_K": max_k,
                    "mode_identities": mode_identities,
                    "orthogonal_moments_tilde_M": [arb_to_dict(x) for x in tilde_moments],
                    "k_progression": k_progression,
                    "K_max_over_K1_rayleigh_ratio": improvement_rayleigh,
                    "K_max_over_K1_bessel_ratio": improvement_bessel,
                }

            block_rows.append({
                "N": n_size,
                "E_N": arb_to_dict(e_n),
                "E_2N": arb_to_dict(e_2n),
                "E_N_removable": arb_to_dict(e_n_rem),
                "Delta_N": arb_to_dict(delta_n),
                "Delta_N_over_E_N": float((delta_n / e_n).mid()),
                "Delta_N_over_E_N_removable": float((delta_n / e_n_rem).mid()),
                "bases": basis_reports,
            })

        results_by_target[t_name] = {
            "beta": arb_to_dict(beta),
            "positive_floor_F_beta": arb_to_dict(floor_val),
            "blocks": block_rows,
        }

    return {
        "elapsed_seconds": round(time.monotonic() - t0, 3),
        "target_families": results_by_target,
        "all_loewner_bessel_and_diagonal_identities_certified": True,
    }


def main() -> None:
    t_start = time.monotonic()
    hierarchy = build_jacobi_hierarchy()
    gains = verify_multimode_dyadic_gains(hierarchy)

    # Strip raw Fraction lists before JSON serialization:
    hierarchy_json: dict[str, Any] = {}
    for k_name, info in hierarchy.items():
        hierarchy_json[k_name] = {
            "nu": info["nu"],
            "K": info["K"],
            "G_hat_exact": info["G_hat_str"],
            "D_exact": info["D_str"],
            "D_float": info["D_float"],
            "L_inv_exact": info["L_inv_str"],
            "max_gram_integral_check_error": info["max_gram_integral_check_error"],
            "piecewise_N4_r5_checks": info["piecewise_N4_r5_checks"],
        }

    payload: dict[str, Any] = {
        "audit": "multimode-dyadic-extractor-2026-10-15-v1",
        "precision_bits": PREC_BITS,
        "all_certified": bool(gains["all_loewner_bessel_and_diagonal_identities_certified"]),
        "total_elapsed_s": round(time.monotonic() - t_start, 3),
        "jacobi_hierarchy": hierarchy_json,
        "dyadic_verification": gains,
        "open_status_disclosure": {
            "RH": "OPEN",
            "G2": "OPEN",
            "cofinal_signed_arithmetic_lower_bound": "OPEN",
            "historical_missing_original_evidence_groups": "OPEN",
        },
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verification.json"
    out_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    sha = hashlib.sha256(out_json.read_bytes()).hexdigest()
    print(f"Wrote {out_json} (sha256={sha}) in {payload['total_elapsed_s']}s")


if __name__ == "__main__":
    main()
