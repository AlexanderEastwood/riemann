#!/usr/bin/env python3
"""
Milestone 10 Verification & Certificate Script:
Block-Invariant Cauchy-Poincare Step-Subspace Interlacing & Crossing the
Internal log 2 Shift Barrier (KERNEL-API).

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


def arb_abs(x: flint.arb) -> flint.arb:
    return abs(x)


def arb_min(a: flint.arb, b: flint.arb) -> flint.arb:
    """Exact interval enclosure of min(a, b) without dependency-radius inflation."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a < lo_b else (lo_b if lo_b < lo_a else flint.arb("0.5") * (lo_a + lo_b - abs(lo_a - lo_b)))
    hi = hi_a if hi_a < hi_b else (hi_b if hi_b < hi_a else flint.arb("0.5") * (hi_a + hi_b - abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_max(a: flint.arb, b: flint.arb) -> flint.arb:
    """Exact interval enclosure of max(a, b) without dependency-radius inflation."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a > lo_b else (lo_b if lo_b > lo_a else flint.arb("0.5") * (lo_a + lo_b + abs(lo_a - lo_b)))
    hi = hi_a if hi_a > hi_b else (hi_b if hi_b > hi_a else flint.arb("0.5") * (hi_a + hi_b + abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_strict_lt(a: flint.arb, b: flint.arb) -> bool:
    if a < b:
        return True
    if a > b:
        return False
    raise AssertionError(f"Ambiguous ball comparison between {a} and {b}")


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


def frac_to_arb(q: Fraction) -> flint.arb:
    return flint.arb(q.numerator) / flint.arb(q.denominator)


def _factor_positive_int(n: int) -> dict[int, int]:
    assert n >= 1
    out: dict[int, int] = {}
    d = 2
    m = n
    while d * d <= m:
        while m % d == 0:
            out[d] = out.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        out[m] = out.get(m, 0) + 1
    return out


class SymReal:
    """Exact element of Q + sum_{p prime} Q * log(p) with zero decimal tolerances."""

    def __init__(self, terms: dict[int, Fraction] | None = None) -> None:
        cleaned: dict[int, Fraction] = {}
        if terms:
            for k, v in terms.items():
                if v != 0:
                    cleaned[k] = Fraction(v)
        self._terms = cleaned
        self._key = tuple(sorted(cleaned.items()))

    @staticmethod
    def zero() -> SymReal:
        return SymReal()

    @staticmethod
    def const(q: int | str | Fraction) -> SymReal:
        f = Fraction(q)
        return SymReal({1: f}) if f != 0 else SymReal()

    @staticmethod
    def log_ratio(r: int | Fraction, coeff: int | str | Fraction = 1) -> SymReal:
        fr = Fraction(r)
        assert fr > 0
        fc = Fraction(coeff)
        if fc == 0 or fr == 1:
            return SymReal()
        terms: dict[int, Fraction] = {}
        for p, e in _factor_positive_int(fr.numerator).items():
            terms[p] = terms.get(p, Fraction(0)) + fc * e
        for p, e in _factor_positive_int(fr.denominator).items():
            terms[p] = terms.get(p, Fraction(0)) - fc * e
        return SymReal(terms)

    @property
    def key(self) -> tuple[tuple[int, Fraction], ...]:
        return self._key

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SymReal):
            return False
        return self._key == other._key

    def __hash__(self) -> int:
        return hash(self._key)

    def __add__(self, other: SymReal) -> SymReal:
        out = dict(self._terms)
        for k, v in other._terms.items():
            out[k] = out.get(k, Fraction(0)) + v
        return SymReal(out)

    def __sub__(self, other: SymReal) -> SymReal:
        out = dict(self._terms)
        for k, v in other._terms.items():
            out[k] = out.get(k, Fraction(0)) - v
        return SymReal(out)

    def scale(self, c: int | str | Fraction) -> SymReal:
        fc = Fraction(c)
        if fc == 0:
            return SymReal()
        return SymReal({k: v * fc for k, v in self._terms.items()})

    def ball(self) -> flint.arb:
        s = flint.arb(0)
        for k, v in self._key:
            c_arb = frac_to_arb(v)
            if k == 1:
                s = s + c_arb
            else:
                s = s + c_arb * flint.arb(k).log()
        return s


def sym_strict_lt(a: SymReal, b: SymReal) -> bool:
    if a == b:
        return False
    return arb_strict_lt(a.ball(), b.ball())


def sym_min(a: SymReal, b: SymReal) -> SymReal:
    if a == b:
        return a
    return a if arb_strict_lt(a.ball(), b.ball()) else b


def deduplicate_and_sort_sym(pts: list[SymReal]) -> list[SymReal]:
    unique: list[SymReal] = []
    seen: set[tuple[tuple[int, Fraction], ...]] = set()
    for p in pts:
        if p.key not in seen:
            seen.add(p.key)
            unique.append(p)
    ordered: list[SymReal] = []
    for p in unique:
        pos = len(ordered)
        for idx, q in enumerate(ordered):
            if sym_strict_lt(p, q):
                pos = idx
                break
        ordered.insert(pos, p)
    for i in range(len(ordered) - 1):
        assert ordered[i].ball() < ordered[i + 1].ball()
    return ordered


def seed_generalized_top_vecs(
    m_mat: list[list[float]], g_mat: list[list[float]], k_top: int
) -> list[list[float]]:
    """Pure-Python Cholesky + Jacobi generalized eigensolver returning top k_top eigenvectors."""
    n = len(m_mat)
    l_chol = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s_c = m_mat[i][j] - sum(l_chol[i][k] * l_chol[j][k] for k in range(j))
            if i == j:
                l_chol[i][i] = math.sqrt(max(s_c, 1e-30))
            else:
                l_chol[i][j] = s_c / l_chol[j][j]
    l_inv = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        l_inv[i][i] = 1.0 / l_chol[i][i]
        for j in range(i):
            l_inv[i][j] = -sum(l_chol[i][k] * l_inv[k][j] for k in range(j, i)) / l_chol[i][i]
    tmp = [[sum(l_inv[i][k] * g_mat[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    a_sym = [[sum(tmp[i][k] * l_inv[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    evecs = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(35):
        off_sq = sum(a_sym[i][j] ** 2 for i in range(n) for j in range(i + 1, n))
        if off_sq < 1e-28:
            break
        for p_i in range(n):
            for q_i in range(p_i + 1, n):
                apq = a_sym[p_i][q_i]
                if abs(apq) < 1e-16:
                    continue
                tau_j = (a_sym[q_i][q_i] - a_sym[p_i][p_i]) / (2.0 * apq)
                t_j = math.copysign(1.0 / (abs(tau_j) + math.sqrt(1.0 + tau_j * tau_j)), tau_j) if tau_j != 0.0 else 1.0
                c_j = 1.0 / math.sqrt(1.0 + t_j * t_j)
                s_j = t_j * c_j
                a_sym[p_i][p_i] -= t_j * apq
                a_sym[q_i][q_i] += t_j * apq
                a_sym[p_i][q_i] = a_sym[q_i][p_i] = 0.0
                for r_i in range(n):
                    if r_i != p_i and r_i != q_i:
                        arp = a_sym[r_i][p_i]
                        arq = a_sym[r_i][q_i]
                        a_sym[r_i][p_i] = a_sym[p_i][r_i] = c_j * arp - s_j * arq
                        a_sym[r_i][q_i] = a_sym[q_i][r_i] = s_j * arp + c_j * arq
                for r_i in range(n):
                    vrp = evecs[r_i][p_i]
                    vrq = evecs[r_i][q_i]
                    evecs[r_i][p_i] = c_j * vrp - s_j * vrq
                    evecs[r_i][q_i] = s_j * vrp + c_j * vrq
    order = sorted(range(n), key=lambda idx: a_sym[idx][idx], reverse=True)
    v_seed = [[0.0 for _ in range(k_top)] for _ in range(n)]
    for col_j in range(k_top):
        eig_col = order[col_j]
        for i in range(n - 1, -1, -1):
            s_back = evecs[i][eig_col] - sum(l_chol[k][i] * v_seed[k][col_j] for k in range(i + 1, n))
            v_seed[i][col_j] = s_back / l_chol[i][i]
    return v_seed


def acb_sinc(z: flint.acb) -> flint.acb:
    return z.sinc()


def alpha_acb(xi: flint.acb) -> flint.acb:
    pi_acb = flint.acb.pi()
    qtr = flint.acb(flint.arb(1) / flint.arb(4))
    ihalf = flint.acb(flint.arb(0), flint.arb(1) / flint.arb(2))
    z1 = qtr + ihalf * xi
    z2 = qtr - ihalf * xi
    return flint.acb(flint.arb(1) / flint.arb(2)) * (z1.digamma() + z2.digamma()) - pi_acb.log()


def sigma_l2_l3_acb(xi: flint.acb, log2: flint.arb, log3: flint.arb) -> flint.acb:
    sqrt2 = flint.acb(flint.arb(2).sqrt())
    sqrt3 = flint.acb(flint.arb(3).sqrt())
    s2 = flint.acb(flint.arb(3) / flint.arb(2)) - sqrt2 * (xi * flint.acb(log2)).cos()
    s3 = flint.acb(flint.arb(4) / flint.arb(3)) - (flint.acb(2) / sqrt3) * (xi * flint.acb(log3)).cos()
    return s2 * s3


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


def integrate_on_0_to_xi0(
    fn: Any, xi0: flint.arb, tol_exp: int
) -> tuple[flint.arb, flint.arb]:
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


def solve_linear_arb(a_mat: list[list[flint.arb]], b_mat: list[list[flint.arb]]) -> list[list[flint.arb]]:
    n = len(a_mat)
    m = len(b_mat[0])
    aug = [[a_mat[i][j] for j in range(n)] + [b_mat[i][k] for k in range(m)] for i in range(n)]
    for col in range(n):
        piv = col
        for r in range(col + 1, n):
            if arb_abs(aug[r][col]) > arb_abs(aug[piv][col]):
                piv = r
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        assert not pv.contains(0)
        for j in range(col, n + m):
            aug[col][j] = aug[col][j] / pv
        for r in range(n):
            if r != col:
                fac = aug[r][col]
                for j in range(col, n + m):
                    aug[r][j] = aug[r][j] - fac * aug[col][j]
    return [[aug[i][n + k] for k in range(m)] for i in range(n)]


def cholesky_lower_arb(mat: list[list[flint.arb]]) -> list[list[flint.arb]]:
    """
    Certify positive definiteness of a symmetric matrix mat in flint.arb by
    computing its lower-triangular Cholesky factor L such that L L^T = mat,
    asserting every diagonal pivot s > 0 in pure ball arithmetic.
    """
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


def certify_max_eig_upper_bound_arb(g_mat: list[list[flint.arb]]) -> flint.arb:
    """
    Construct a rigorous ball upper bound Lambda_1 > mu_1(g_mat) for a symmetric
    d x d matrix g_mat in flint.arb using Gershgorin's circle theorem, and also
    certify positive definiteness of (Lambda_1 * I_d - g_mat) by exact Cholesky
    factorization in flint.arb.
    """
    d = len(g_mat)
    max_gersh = g_mat[0][0] + sum((arb_abs(g_mat[0][j]) for j in range(1, d)), flint.arb(0))
    for i in range(1, d):
        row_rad = sum((arb_abs(g_mat[i][j]) for j in range(d) if j != i), flint.arb(0))
        max_gersh = arb_max(max_gersh, g_mat[i][i] + row_rad)
    # Add a small positive rational cushion 10^-7 so the lower bound of lam1_ball is strictly PD for Cholesky:
    cushion = flint.arb(1) / flint.arb(10**7)
    lam1_ball = max_gersh + cushion
    lam1_lb = flint.arb(lam1_ball.lower())
    shifted = [
        [(lam1_lb - g_mat[i][j]) if i == j else (-g_mat[i][j]) for j in range(d)]
        for i in range(d)
    ]
    _ = cholesky_lower_arb(shifted)
    return lam1_ball


def certify_internal_shift_and_block_interlacing(prec_bits: int) -> dict[str, Any]:
    """
    Certify Theorem 1 (Block-Invariant Step-Subspace & 4-Mode Cauchy-Poincare Interlacing)
    and Theorem 2 (Step-Subspace Gauge-Invariant Asymmetric Schur Weights & Crossing the
    Internal log 2 Shift Barrier across ((1/2) log 12, (1/2) log 13]) in prec_bits flint.arb.
    """
    flint.ctx.prec = prec_bits
    t0 = time.time()
    tol_exp = 40 if prec_bits <= 256 else 46

    half = flint.arb(1) / flint.arb(2)
    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()
    log6 = log2 + log3
    log7 = flint.arb(7).log()
    log11 = flint.arb(11).log()
    log12 = flint.arb(12).log()
    log13 = flint.arb(13).log()
    pi = flint.arb.pi()

    c0_23 = (flint.arb(4) / flint.arb(3)) * log2 + log3
    c76 = log7 / flint.arb(42).sqrt()
    c65 = log5 / flint.arb(30).sqrt()
    c53 = flint.arb(3) * log5 / (flint.arb(2) * flint.arb(15).sqrt())
    c11_6 = log11 / flint.arb(66).sqrt()

    s_tau76 = SymReal.log_ratio(Fraction(7, 6))
    s_tau65 = SymReal.log_ratio(Fraction(6, 5))
    s_tau32 = SymReal.log_ratio(Fraction(3, 2))
    s_tau53 = SymReal.log_ratio(Fraction(5, 3))
    s_tau11_6 = SymReal.log_ratio(Fraction(11, 6))
    s_tau2 = SymReal.log_ratio(Fraction(2, 1))
    s_zero = SymReal.zero()

    # Exact rational gauge weights for crossing a > (1/2) log 12:
    # gamma = (1, 1, 18/25, 39/50, 17/20, 1), eta = (41/50, 41/50, 1, 1, 1, 1)
    gam_asym = [
        flint.arb(1),
        flint.arb(1),
        flint.arb(18) / flint.arb(25),
        flint.arb(39) / flint.arb(50),
        flint.arb(17) / flint.arb(20),
        flint.arb(1),
    ]
    eta_asym = [
        flint.arb(41) / flint.arb(50),
        flint.arb(41) / flint.arb(50),
        flint.arb(1),
        flint.arb(1),
        flint.arb(1),
        flint.arb(1),
    ]
    gam_sym = [flint.arb(1)] * 5
    eta_sym = [flint.arb(1)] * 5

    def eval_checkpoint(
        label: str,
        s_a: SymReal,
        da: flint.arb,
        n_sub: int,
        include_log2: bool,
        gam_list: list[flint.arb],
        eta_list: list[flint.arb],
    ) -> dict[str, Any]:
        tc = time.time()
        s_b = s_a - SymReal.log_ratio(6, Fraction(1, 2))
        a = s_a.ball()
        b = s_b.ball()
        v0 = c0_23 + flint.arb(2) * da
        c32_da = (log6 + da) / flint.arb(6).sqrt()
        c2_da = (flint.arb(4) * log2 + log3 + flint.arb(4) * da) / (flint.arb(3) * flint.arb(2).sqrt())

        xi0 = find_alpha_root_arb(da)
        xi0_mid = flint.arb(xi0.mid())

        active_shifts: list[tuple[str, SymReal, int, flint.arb]] = [
            ("7/6", s_tau76, -1, c76),
            ("6/5", s_tau65, -1, c65),
            ("3/2", s_tau32, +1, c32_da),
            ("5/3", s_tau53, +1, c53),
            ("11/6", s_tau11_6, -1, c11_6),
        ]
        if include_log2:
            assert sym_strict_lt(s_tau2, s_b.scale(2))
            active_shifts.append(("2", s_tau2, -1, c2_da))

        raw_pts: list[SymReal] = [s_zero, s_b]
        vecs_e: list[list[tuple[SymReal, SymReal, flint.arb]]] = []
        vecs_o: list[list[tuple[SymReal, SymReal, flint.arb]]] = []
        b_diag: list[flint.arb] = []

        for idx, (_, s_tau, sgn_int, c) in enumerate(active_shifts):
            gam = gam_list[idx]
            eta = eta_list[idx]
            sgn = flint.arb(sgn_int)
            inv_sqrt_eta = flint.arb(1) / eta.sqrt()
            sqrt_eta = eta.sqrt()
            inv_sqrt_gam = flint.arb(1) / gam.sqrt()
            sqrt_gam = gam.sqrt()

            s_ht = s_tau.scale(Fraction(1, 2))
            for p_cut in (s_tau - s_b, s_b - s_tau, s_ht, s_tau):
                if sym_strict_lt(s_zero, p_cut) and sym_strict_lt(p_cut, s_b):
                    raw_pts.append(p_cut)

            s_dt = s_b - s_tau
            if sym_strict_lt(s_zero, s_dt):
                for r in range(n_sub):
                    p = s_dt.scale(Fraction(r, n_sub))
                    q = s_dt.scale(Fraction(r + 1, n_sub))
                    raw_pts.extend([p, q, p + s_tau, q + s_tau])
                    vecs_e.append([(p, q, inv_sqrt_eta), (p + s_tau, q + s_tau, sgn * sqrt_eta)])
                    vecs_o.append([(p, q, inv_sqrt_eta), (p + s_tau, q + s_tau, sgn * sqrt_eta)])
                    b_diag.append((q.ball() - p.ball()) / c)

            s_lrefl = sym_min(s_ht, s_b - s_ht)
            if sym_strict_lt(s_zero, s_lrefl):
                s_x0 = s_ht - s_lrefl
                for r in range(n_sub):
                    p = s_x0 + s_lrefl.scale(Fraction(r, n_sub))
                    q = s_x0 + s_lrefl.scale(Fraction(r + 1, n_sub))
                    raw_pts.extend([p, q, s_tau - q, s_tau - p])
                    vecs_e.append([(p, q, inv_sqrt_gam), (s_tau - q, s_tau - p, sgn * sqrt_gam)])
                    vecs_o.append([(p, q, inv_sqrt_gam), (s_tau - q, s_tau - p, (-sgn) * sqrt_gam)])
                    b_diag.append((q.ball() - p.ball()) / c)

        sym_pts = deduplicate_and_sort_sym(raw_pts)
        elem_pts = [p.ball() for p in sym_pts]
        sym_intervals = [(sym_pts[k], sym_pts[k + 1]) for k in range(len(sym_pts) - 1)]
        elem_intervals = [(elem_pts[k], elem_pts[k + 1]) for k in range(len(elem_pts) - 1)]
        n_elem = len(elem_intervals)
        elem_len = [xR - xL for xL, xR in elem_intervals]

        elem_v: list[flint.arb] = []
        min_v = v0
        for s_xL, s_xR in sym_intervals:
            s_xm = (s_xL + s_xR).scale(Fraction(1, 2))
            pen = flint.arb(0)
            for idx, (_, s_tau, _, c) in enumerate(active_shifts):
                gam = gam_list[idx]
                eta = eta_list[idx]
                s_dt = s_b - s_tau
                if sym_strict_lt(s_zero, s_dt):
                    if sym_strict_lt(s_xm, s_dt):
                        pen = pen + (c / eta)
                    if sym_strict_lt(s_tau, s_xm):
                        pen = pen + (c * eta)
                s_ht = s_tau.scale(Fraction(1, 2))
                s_lrefl = sym_min(s_ht, s_b - s_ht)
                if sym_strict_lt(s_zero, s_lrefl):
                    s_x0 = s_ht - s_lrefl
                    s_y1 = s_ht + s_lrefl
                    if sym_strict_lt(s_x0, s_xm) and sym_strict_lt(s_xm, s_ht):
                        pen = pen + (c / gam)
                    if sym_strict_lt(s_ht, s_xm) and sym_strict_lt(s_xm, s_y1):
                        pen = pen + (c * gam)
            vk = v0 - pen
            min_v = arb_min(min_v, vk)
            elem_v.append(vk)

        assert min_v > flint.arb(0), f"min_v <= 0 at {label}: {min_v}"

        m_tot = len(vecs_e)
        w_mat_e = [[flint.arb(0) for _ in range(m_tot)] for _ in range(n_elem)]
        w_mat_o = [[flint.arb(0) for _ in range(m_tot)] for _ in range(n_elem)]
        for m_idx, w in enumerate(vecs_e):
            for s_aL, s_aR, cf in w:
                for k, (s_xL, s_xR) in enumerate(sym_intervals):
                    s_xm = (s_xL + s_xR).scale(Fraction(1, 2))
                    if sym_strict_lt(s_aL, s_xm) and sym_strict_lt(s_xm, s_aR):
                        w_mat_e[k][m_idx] = w_mat_e[k][m_idx] + cf
        for m_idx, w in enumerate(vecs_o):
            for s_aL, s_aR, cf in w:
                for k, (s_xL, s_xR) in enumerate(sym_intervals):
                    s_xm = (s_xL + s_xR).scale(Fraction(1, 2))
                    if sym_strict_lt(s_aL, s_xm) and sym_strict_lt(s_xm, s_aR):
                        w_mat_o[k][m_idx] = w_mat_o[k][m_idx] + cf

        u_mat_e = [[w_mat_e[k][m_idx] / elem_v[k] for m_idx in range(m_tot)] for k in range(n_elem)]
        u_mat_o = [[w_mat_o[k][m_idx] / elem_v[k] for m_idx in range(m_tot)] for k in range(n_elem)]
        m_wood_e = [[flint.arb(0) for _ in range(m_tot)] for _ in range(m_tot)]
        m_wood_o = [[flint.arb(0) for _ in range(m_tot)] for _ in range(m_tot)]
        for i in range(m_tot):
            for j in range(m_tot):
                s_e = b_diag[i] if i == j else flint.arb(0)
                s_o = b_diag[i] if i == j else flint.arb(0)
                for k in range(n_elem):
                    s_e = s_e + elem_len[k] * w_mat_e[k][i] * u_mat_e[k][j]
                    s_o = s_o + elem_len[k] * w_mat_o[k][i] * u_mat_o[k][j]
                m_wood_e[i][j] = s_e
                m_wood_o[i][j] = s_o

        id_m = [[flint.arb(1 if i == j else 0) for j in range(m_tot)] for i in range(m_tot)]
        m_wood_inv_e = solve_linear_arb(m_wood_e, id_m)
        m_wood_inv_o = solve_linear_arb(m_wood_o, id_m)
        m_wood_inv_sym_e = [
            [half * (m_wood_inv_e[i][j] + m_wood_inv_e[j][i]) for j in range(m_tot)]
            for i in range(m_tot)
        ]
        m_wood_inv_sym_o = [
            [half * (m_wood_inv_o[i][j] + m_wood_inv_o[j][i]) for j in range(m_tot)]
            for i in range(m_tot)
        ]

        l_winv_e = cholesky_lower_arb(m_wood_inv_sym_e)
        l_winv_o = cholesky_lower_arb(m_wood_inv_sym_o)

        # Seed top 4 even eigenvectors and top 3 odd eigenvectors in pure Python + flint.acb, then orthonormalize in flint.arb:
        elem_len_f = [float(x.mid()) for x in elem_len]
        elem_v_f = [float(x.mid()) for x in elem_v]
        w_mat_e_f = [[float(w_mat_e[k][m].mid()) for m in range(m_tot)] for k in range(n_elem)]
        w_mat_o_f = [[float(w_mat_o[k][m].mid()) for m in range(m_tot)] for k in range(n_elem)]
        b_diag_f = [float(x.mid()) for x in b_diag]

        lw_e_f = [[elem_len_f[k] * w_mat_e_f[k][m] for m in range(m_tot)] for k in range(n_elem)]
        lw_o_f = [[elem_len_f[k] * w_mat_o_f[k][m] for m in range(m_tot)] for k in range(n_elem)]
        m_elem_e_f = [[0.0 for _ in range(n_elem)] for _ in range(n_elem)]
        m_elem_o_f = [[0.0 for _ in range(n_elem)] for _ in range(n_elem)]
        for i in range(n_elem):
            for j in range(n_elem):
                se_ij = (elem_len_f[i] * elem_v_f[i]) if i == j else 0.0
                so_ij = se_ij
                for m in range(m_tot):
                    se_ij += (lw_e_f[i][m] / b_diag_f[m]) * lw_e_f[j][m]
                    so_ij += (lw_o_f[i][m] / b_diag_f[m]) * lw_o_f[j][m]
                m_elem_e_f[i][j] = se_ij
                m_elem_o_f[i][j] = so_ij

        xi0_f = float(xi0_mid.mid())
        n_sub_q = 32
        inv_sqrt3 = 1.0 / math.sqrt(3.0)
        xi_pts: list[float] = []
        xi_w: list[float] = []
        h_q = xi0_f / n_sub_q
        for idx_q in range(n_sub_q):
            xm_q = (idx_q + 0.5) * h_q
            dx_q = 0.5 * h_q * inv_sqrt3
            xi_pts.append(xm_q - dx_q)
            xi_pts.append(xm_q + dx_q)
            xi_w.append(0.5 * h_q)
            xi_w.append(0.5 * h_q)

        g_elem_e_f = [[0.0 for _ in range(n_elem)] for _ in range(n_elem)]
        g_elem_o_f = [[0.0 for _ in range(n_elem)] for _ in range(n_elem)]
        pts_f = [float(p.mid()) for p in elem_pts]
        log2_f = float(log2.mid())
        log3_f = float(log3.mid())
        da_f = float(da.mid())

        for x_val, w_val in zip(xi_pts, xi_w):
            s2_f = 1.5 - math.sqrt(2.0) * math.cos(x_val * log2_f)
            s3_f = (4.0 / 3.0) - (2.0 / math.sqrt(3.0)) * math.cos(x_val * log3_f)
            alf_f = float(flint.acb(flint.arb(1) / flint.arb(4), flint.arb(str(0.5 * x_val))).digamma().real.mid()) - math.log(math.pi)
            wm_f = (2.0 / math.pi) * s2_f * s3_f * (da_f - alf_f) * w_val
            sin_pts = [math.sin(x_val * p_f) / x_val for p_f in pts_f]
            cos_pts = [(1.0 - math.cos(x_val * p_f)) / x_val for p_f in pts_f]
            hats_e_f = [sin_pts[k + 1] - sin_pts[k] for k in range(n_elem)]
            hats_o_f = [cos_pts[k + 1] - cos_pts[k] for k in range(n_elem)]
            for i in range(n_elem):
                he_i = wm_f * hats_e_f[i]
                ho_i = wm_f * hats_o_f[i]
                for j in range(n_elem):
                    g_elem_e_f[i][j] += he_i * hats_e_f[j]
                    g_elem_o_f[i][j] += ho_i * hats_o_f[j]

        d_even = 4
        v_seed_e_f = seed_generalized_top_vecs(m_elem_e_f, g_elem_e_f, d_even)
        d_odd = 3
        v_seed_o_f = seed_generalized_top_vecs(m_elem_o_f, g_elem_o_f, d_odd)

        def m_elem_inner(x_vec: list[flint.arb], y_vec: list[flint.arb], w_m_mat: list[list[flint.arb]]) -> flint.arb:
            s = flint.arb(0)
            for k in range(n_elem):
                s = s + elem_len[k] * elem_v[k] * x_vec[k] * y_vec[k]
            for m_idx in range(m_tot):
                wx = flint.arb(0)
                wy = flint.arb(0)
                for k in range(n_elem):
                    lw_k = elem_len[k] * w_m_mat[k][m_idx]
                    wx = wx + lw_k * x_vec[k]
                    wy = wy + lw_k * y_vec[k]
                s = s + (wx * wy) / b_diag[m_idx]
            return s

        q_vecs_e: list[list[flint.arb]] = []
        for j in range(d_even):
            v_j = [flint.arb(str(float(v_seed_e_f[k][j]))) for k in range(n_elem)]
            for i in range(j):
                proj = m_elem_inner(q_vecs_e[i], v_j, w_mat_e)
                v_j = [v_j[k] - proj * q_vecs_e[i][k] for k in range(n_elem)]
            norm_sq = m_elem_inner(v_j, v_j, w_mat_e)
            assert norm_sq > flint.arb(0)
            inv_norm = flint.arb(1) / norm_sq.sqrt()
            q_vecs_e.append([v_j[k] * inv_norm for k in range(n_elem)])

        q_vecs_o: list[list[flint.arb]] = []
        for j in range(d_odd):
            v_j = [flint.arb(str(float(v_seed_o_f[k][j]))) for k in range(n_elem)]
            for i in range(j):
                proj = m_elem_inner(q_vecs_o[i], v_j, w_mat_o)
                v_j = [v_j[k] - proj * q_vecs_o[i][k] for k in range(n_elem)]
            norm_sq = m_elem_inner(v_j, v_j, w_mat_o)
            assert norm_sq > flint.arb(0)
            inv_norm = flint.arb(1) / norm_sq.sqrt()
            q_vecs_o.append([v_j[k] * inv_norm for k in range(n_elem)])

        u_pref_e = [[flint.arb(0) for _ in range(m_tot)] for _ in range(n_elem)]
        u_pref_o = [[flint.arb(0) for _ in range(m_tot)] for _ in range(n_elem)]
        for m_idx in range(m_tot):
            for k in range(1, n_elem + 1):
                c_left = u_mat_e[k - 1][m_idx]
                c_right = u_mat_e[k][m_idx] if k < n_elem else flint.arb(0)
                u_pref_e[k - 1][m_idx] = elem_pts[k] * (c_left - c_right)

                co_left = u_mat_o[k - 1][m_idx]
                co_right = u_mat_o[k][m_idx] if k < n_elem else flint.arb(0)
                u_pref_o[k - 1][m_idx] = half * elem_pts[k] * elem_pts[k] * (co_left - co_right)

        f_mat_e_mat = flint.acb_mat([
            [
                flint.acb(sum((u_pref_e[k][r] * l_winv_e[r][m_idx] for r in range(m_idx, m_tot)), flint.arb(0)))
                for k in range(n_elem)
            ]
            for m_idx in range(m_tot)
        ])
        f_mat_o_mat = flint.acb_mat([
            [
                flint.acb(sum((u_pref_o[k][r] * l_winv_o[r][m_idx] for r in range(m_idx, m_tot)), flint.arb(0)))
                for k in range(n_elem)
            ]
            for m_idx in range(m_tot)
        ])

        q_pref_e_acb = [[flint.acb(0) for _ in range(n_elem)] for _ in range(d_even)]
        for j in range(d_even):
            for k in range(1, n_elem + 1):
                c_left = q_vecs_e[j][k - 1]
                c_right = q_vecs_e[j][k] if k < n_elem else flint.arb(0)
                q_pref_e_acb[j][k - 1] = flint.acb(elem_pts[k] * (c_left - c_right))
        q_pref_e_mat = flint.acb_mat(q_pref_e_acb)

        q_pref_o_acb = [[flint.acb(0) for _ in range(n_elem)] for _ in range(d_odd)]
        for j in range(d_odd):
            for k in range(1, n_elem + 1):
                co_left = q_vecs_o[j][k - 1]
                co_right = q_vecs_o[j][k] if k < n_elem else flint.arb(0)
                q_pref_o_acb[j][k - 1] = flint.acb(half * elem_pts[k] * elem_pts[k] * (co_left - co_right))
        q_pref_o_mat = flint.acb_mat(q_pref_o_acb)

        pos_pts_acb = [flint.acb(elem_pts[k]) for k in range(1, n_elem + 1)]
        half_pos_pts_acb = [flint.acb(half * elem_pts[k]) for k in range(1, n_elem + 1)]
        inv_elem_v_acb = [flint.acb(flint.arb(1) / vk) for vk in elem_v]

        def int_tr_and_red(xi: flint.acb, _: Any) -> flint.acb:
            w_m = (flint.acb(2) / flint.acb(pi)) * sigma_l2_l3_acb(xi, log2, log3) * (flint.acb(da) - alpha_acb(xi))
            two_xi = flint.acb(2) * xi
            acc_e = flint.acb(0)
            acc_o = flint.acb(0)
            s_prev = flint.acb(1)
            h_prev = flint.acb(0)
            for k in range(n_elem):
                s_curr = acb_sinc(two_xi * pos_pts_acb[k])
                h_curr = half_pos_pts_acb[k]
                inv_vk = inv_elem_v_acb[k]
                acc_e = acc_e + (h_curr * (flint.acb(1) + s_curr) - h_prev * (flint.acb(1) + s_prev)) * inv_vk
                acc_o = acc_o + (h_curr * (flint.acb(1) - s_curr) - h_prev * (flint.acb(1) - s_prev)) * inv_vk
                s_prev = s_curr
                h_prev = h_curr

            sincs_col = flint.acb_mat([[acb_sinc(xi * p_acb)] for p_acb in pos_pts_acb])
            s_half_col = flint.acb_mat([[xi * (acb_sinc(xi * hp_acb) ** 2)] for hp_acb in half_pos_pts_acb])

            fe_col = f_mat_e_mat * sincs_col
            fo_col = f_mat_o_mat * s_half_col
            red_e = (fe_col.transpose() * fe_col)[0, 0]
            red_o = (fo_col.transpose() * fo_col)[0, 0]

            return w_m * ((acc_e - red_e) + flint.acb(0, 1) * (acc_o - red_o))

        tr_even_after, tr_odd_after = integrate_on_0_to_xi0(int_tr_and_red, xi0, tol_exp)

        # Integrate the 4x4 even Gram matrix G^{(4)}_even and 3x3 odd Gram matrix G^{(3)}_odd:
        even_pairs = [(i, j) for i in range(d_even) for j in range(i, d_even)]
        g_even = [[flint.arb(0) for _ in range(d_even)] for _ in range(d_even)]
        for p_idx in range(0, len(even_pairs), 2):
            i1, j1 = even_pairs[p_idx]
            i2, j2 = even_pairs[p_idx + 1]

            def int_pair_e(xi: flint.acb, _: Any, a1: int = i1, b1: int = j1, a2: int = i2, b2: int = j2) -> flint.acb:
                w_m = (flint.acb(2) / flint.acb(pi)) * sigma_l2_l3_acb(xi, log2, log3) * (flint.acb(da) - alpha_acb(xi))
                sincs_col = flint.acb_mat([[acb_sinc(xi * p_acb)] for p_acb in pos_pts_acb])
                qe_col = q_pref_e_mat * sincs_col
                return w_m * (qe_col[a1, 0] * qe_col[b1, 0] + flint.acb(0, 1) * (qe_col[a2, 0] * qe_col[b2, 0]))

            val1, val2 = integrate_on_0_to_xi0(int_pair_e, xi0, tol_exp)
            g_even[i1][j1] = g_even[j1][i1] = val1
            g_even[i2][j2] = g_even[j2][i2] = val2

        odd_pairs = [(i, j) for i in range(d_odd) for j in range(i, d_odd)]
        g_odd = [[flint.arb(0) for _ in range(d_odd)] for _ in range(d_odd)]
        for p_idx in range(0, len(odd_pairs), 2):
            i1, j1 = odd_pairs[p_idx]
            i2, j2 = odd_pairs[p_idx + 1]

            def int_pair_o(xi: flint.acb, _: Any, a1: int = i1, b1: int = j1, a2: int = i2, b2: int = j2) -> flint.acb:
                w_m = (flint.acb(2) / flint.acb(pi)) * sigma_l2_l3_acb(xi, log2, log3) * (flint.acb(da) - alpha_acb(xi))
                s_half_col = flint.acb_mat([[xi * (acb_sinc(xi * hp_acb) ** 2)] for hp_acb in half_pos_pts_acb])
                qo_col = q_pref_o_mat * s_half_col
                return w_m * (qo_col[a1, 0] * qo_col[b1, 0] + flint.acb(0, 1) * (qo_col[a2, 0] * qo_col[b2, 0]))

            val1, val2 = integrate_on_0_to_xi0(int_pair_o, xi0, tol_exp)
            g_odd[i1][j1] = g_odd[j1][i1] = val1
            g_odd[i2][j2] = g_odd[j2][i2] = val2

        # Certify 2-mode, 3-mode, and 4-mode even bounds and 2-mode, 3-mode odd bounds in pure flint.arb:
        g_even_2x2 = [[g_even[i][j] for j in range(2)] for i in range(2)]
        g_even_3x3 = [[g_even[i][j] for j in range(3)] for i in range(3)]
        g_odd_2x2 = [[g_odd[i][j] for j in range(2)] for i in range(2)]

        lam1_e2 = certify_max_eig_upper_bound_arb(g_even_2x2)
        lam1_e3 = certify_max_eig_upper_bound_arb(g_even_3x3)
        lam1_e4 = certify_max_eig_upper_bound_arb(g_even)
        lam1_o2 = certify_max_eig_upper_bound_arb(g_odd_2x2)
        lam1_o3 = certify_max_eig_upper_bound_arb(g_odd)

        tr_g_e2 = g_even[0][0] + g_even[1][1]
        tr_g_e3 = tr_g_e2 + g_even[2][2]
        tr_g_e4 = tr_g_e3 + g_even[3][3]
        tr_g_o2 = g_odd[0][0] + g_odd[1][1]
        tr_g_o3 = tr_g_o2 + g_odd[2][2]

        op_bound_e2 = tr_even_after - tr_g_e2 + lam1_e2
        op_bound_e3 = tr_even_after - tr_g_e3 + lam1_e3
        op_bound_e4 = tr_even_after - tr_g_e4 + lam1_e4
        op_bound_o2 = tr_odd_after - tr_g_o2 + lam1_o2
        op_bound_o3 = tr_odd_after - tr_g_o3 + lam1_o3

        assert op_bound_e4 < flint.arb(1), f"Even 4-mode op bound >= 1 at {label}: {op_bound_e4}"
        assert op_bound_o3 < flint.arb(1), f"Odd 3-mode op bound >= 1 at {label}: {op_bound_o3}"

        coercivity_h = min_v * arb_min(flint.arb(1) - op_bound_e4, flint.arb(1) - op_bound_o3)
        assert coercivity_h > flint.arb(0)

        return {
            "label": label,
            "a": arb_to_dict(a),
            "b": arb_to_dict(b),
            "Delta_alpha": arb_to_dict(da),
            "xi0": arb_to_dict(xi0),
            "n_sub": n_sub,
            "include_log2_shift": include_log2,
            "num_step_vectors": m_tot,
            "num_elementary_intervals": n_elem,
            "lambda_min_P0": arb_to_dict(min_v),
            "tr_even_after": arb_to_dict(tr_even_after),
            "tr_odd_after": arb_to_dict(tr_odd_after),
            "op_norm_bound_even_2mode": arb_to_dict(op_bound_e2),
            "op_norm_bound_even_3mode": arb_to_dict(op_bound_e3),
            "op_norm_bound_even_4mode": arb_to_dict(op_bound_e4),
            "op_norm_bound_odd_2mode": arb_to_dict(op_bound_o2),
            "op_norm_bound_odd_3mode": arb_to_dict(op_bound_o3),
            "margin_even_4mode": arb_to_dict(flint.arb(1) - op_bound_e4),
            "margin_odd_3mode": arb_to_dict(flint.arb(1) - op_bound_o3),
            "coercivity_h_L2": arb_to_dict(coercivity_h),
            "certified": True,
            "elapsed_s": round(time.time() - tc, 4),
        }

    da_060 = flint.arb(3) / flint.arb(5)
    da_100 = flint.arb(1)

    checkpoints = [
        eval_checkpoint(
            "a = 1/2 log 12.00 = log(2*sqrt(3)) (log 2 entry, Theorem 1 4-mode vs 2-mode comparison)",
            SymReal.log_ratio(12, Fraction(1, 2)),
            da_060,
            5,
            False,
            gam_sym,
            eta_sym,
        ),
        eval_checkpoint(
            "a = 1/2 log(49/4) = log(7/2) = 1/2 log 12.25 (past internal log 2 shift)",
            SymReal.log_ratio(Fraction(49, 4), Fraction(1, 2)),
            da_100,
            7,
            True,
            gam_asym,
            eta_asym,
        ),
        eval_checkpoint(
            "a = 1/2 log(25/2) = 1/2 log 12.50",
            SymReal.log_ratio(Fraction(25, 2), Fraction(1, 2)),
            da_100,
            9,
            True,
            gam_asym,
            eta_asym,
        ),
        eval_checkpoint(
            "a = 1/2 log(51/4) = 1/2 log 12.75",
            SymReal.log_ratio(Fraction(51, 4), Fraction(1, 2)),
            da_100,
            11,
            True,
            gam_asym,
            eta_asym,
        ),
        eval_checkpoint(
            "a = 1/2 log 13.00 (tau_{13/6} = log(13/6) entry horizon)",
            SymReal.log_ratio(13, Fraction(1, 2)),
            da_100,
            13,
            True,
            gam_asym,
            eta_asym,
        ),
    ]

    # Verify at a = 1/2 log 12 that the 4-mode bound strictly improves upon the 2-mode bound:
    b2_12 = flint.arb(checkpoints[0]["op_norm_bound_even_2mode"]["str"])
    b4_12 = flint.arb(checkpoints[0]["op_norm_bound_even_4mode"]["str"])
    assert b4_12 < b2_12

    return {
        "prec_bits": prec_bits,
        "regime": "[(1/2) log 12, (1/2) log 13] ~ [1.242453, 1.282475]",
        "subspace": "Ran(B_{2, 3}) subset L^2_{pole-free}(-a, a)",
        "rational_gauge_weights_gamma": ["1", "1", "18/25", "39/50", "17/20", "1"],
        "rational_gauge_weights_eta": ["41/50", "41/50", "1", "1", "1", "1"],
        "checkpoints": checkpoints,
        "elapsed_s": round(time.time() - t0, 4),
    }


def verify_two_precision_consistency(res_256: dict[str, Any], res_384: dict[str, Any]) -> dict[str, Any]:
    flint.ctx.prec = 384
    checks = 0
    for c256, c384 in zip(res_256["checkpoints"], res_384["checkpoints"]):
        for key in (
            "lambda_min_P0",
            "tr_even_after",
            "tr_odd_after",
            "op_norm_bound_even_4mode",
            "op_norm_bound_odd_3mode",
            "coercivity_h_L2",
        ):
            b256 = flint.arb(c256[key]["str"])
            b384 = flint.arb(c384[key]["str"])
            assert b256.overlaps(b384), f"Ball mismatch at {c384['label']} [{key}]"
            checks += 1
    return {
        "precisions_compared": [256, 384],
        "num_ball_overlap_checks": checks,
        "all_overlaps_verified": True,
    }


def main() -> None:
    t_start = time.time()
    out_dir = Path(__file__).resolve().parent

    res_256 = certify_internal_shift_and_block_interlacing(256)
    res_384 = certify_internal_shift_and_block_interlacing(384)
    consistency = verify_two_precision_consistency(res_256, res_384)

    payload: dict[str, Any] = {
        "audit_id": "multiprime-internal-shift-and-block-interlacing-2026-10-15-v1",
        "date": "2026-10-15",
        "lanes": ["KERNEL-API"],
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

    print("=== Milestone 10 Verification Complete ===")
    print(f"Two-precision consistency (256 vs 384 bits): {consistency['num_ball_overlap_checks']} checks PASS")
    for cp in res_384["checkpoints"]:
        print(
            f"  {cp['label'][:42]:42s}: "
            f"even_4mode={cp['op_norm_bound_even_4mode']['upper']:.6f} < 1, "
            f"odd_3mode={cp['op_norm_bound_odd_3mode']['upper']:.6f} < 1, "
            f"min_v={cp['lambda_min_P0']['lower']:.4f} > 0"
        )
    print(f"verification.json payload.sha256 = {payload_sha256}")
    print(f"verification.json file_sha256    = {file_sha256}")


if __name__ == "__main__":
    main()
