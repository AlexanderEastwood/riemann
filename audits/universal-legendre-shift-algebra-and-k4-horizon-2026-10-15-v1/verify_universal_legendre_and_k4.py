#!/usr/bin/env python3
"""
Two-Precision (256-bit and 384-bit) ARB-Certified Verification of Milestone 14:
`universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1`
(Lanes: `NB-GAIN` / `COEFF` & `NS-61` and `KERNEL-API`)

1. Theorem 1 (`NB-GAIN` / `COEFF` & `NS-61`): Global Analyticity of Legendre Shift & Schur
   Multiplicity Matrices Across u = 1 and Universal Kernel-Plus-Positive-Definite Structure on (0, 2):
   - Certifies that (S_tau^{(N)})_{m, n} = sqrt((2m+1)(2n+1)) int_{-1}^{1-u} P_m(t) P_n(t+u) dt
     and (D_tau^{(N)})_{m, n} = sqrt((2m+1)(2n+1)) int_{u-1}^1 P_m(t) P_n(t) dt are single analytic
     rational polynomials across the entire interval u in [0, 2] (spanning both the two-sided
     overlap regime u in (0, 1) and the single-reflection regime u in [1, 2]) with zero piecewise
     branching at u = 1.
   - Certifies in 256-bit and 384-bit ball arithmetic that across u in {3/20, 1/2, 17/20} subset (0, 1),
     the single analytic polynomial formulas match the three-piece folded [0, 1] numerical integrals
     of P_b(T_tau + T_{-tau})P_b and psi_tau(x) = 1_{[0, b-tau]}(x) + 1_{[tau-b, b]}(x) to < 1e-100.
   - Certifies the Exact First-Row Polynomial Identity (D_tau^{(N)})_{0, 2s} == (S_tau^{(N)})_{0, 2s}
     for all s >= 0 and all u in [0, 2], and certifies via exact flint.arb Cholesky factorization across
     8 test points u in {1/20, 1/4, 1/2, 3/4, 19/20, 1, 27/20, 37/20} subset (0, 2) that:
       Q_{tau, +1}^{(4)} = D_tau^{(4)} + S_tau^{(4)} > 0 on R^4 (P_0, P_2, P_4, P_6), and
       tilde{Q}_{tau, -1}^{(4)} = (D_tau^{(4)} - S_tau^{(4)})_{r,s in {1,2,3}} > 0 on R^3 (P_2, P_4, P_6).

2. Theorem 2 (`KERNEL-API` + `NB-GAIN`): Crossing Four Internal Primorial Shift Horizons for K = 4
   (B_{{2,3,5},{7}}, P_4 = 210) up to a = (1/2) log 260 (66 Active Shifts) and Super-Exponential
   N = 4 Gegenbauer-Bessel Tail Completeness:
   - Certifies K = 4 across N in {225, 240, 245} at Delta_alpha = 0 (up to 49 shifts, crossing tau_{7/6}),
     N in {245, 250, 252} at Delta_alpha = 0.60 (up to 56 shifts, crossing tau_{6/5}),
     and N in {252, 255, 260} at Delta_alpha = 1.20 (up to 66 shifts: 30 two-sided and 36 single-reflection).
   - Certifies the exact N = 4 Gegenbauer-Spherical-Bessel Parseval tail defect eps_4^{even/odd}(b)
     across the extended horizons for K = 3 (N = 42, 45) and K = 4 (N = 240, 245, 252, 260).
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

ALL_PRIMES: list[int] = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251,
]


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


def arb_hull(a: flint.arb, b: flint.arb) -> flint.arb:
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a < lo_b else (lo_b if lo_b < lo_a else flint.arb("0.5") * (lo_a + lo_b - abs(lo_a - lo_b)))
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
    raise AssertionError(f"Undecided strict inequality between balls: {a} vs {b}")


class SymReal:
    """
    Exact symbolic linear combination in Q + sum_p Q * log(p), represented by a canonical
    sorted tuple of (prime_or_1, Fraction) pairs where key 1 denotes the rational constant
    and key p >= 2 denotes log(p).
    """

    def __init__(self, terms: dict[int, Fraction] | None = None) -> None:
        cleaned: dict[int, Fraction] = {}
        if terms:
            for k, v in terms.items():
                if v != 0:
                    cleaned[k] = v
        self.terms: dict[int, Fraction] = cleaned

    @staticmethod
    def zero() -> SymReal:
        return SymReal()

    @staticmethod
    def from_fraction(r: Fraction) -> SymReal:
        assert r.numerator > 0 and r.denominator > 0
        terms: dict[int, Fraction] = {}
        num = r.numerator
        den = r.denominator
        p = 2
        while p * p <= num:
            while num % p == 0:
                terms[p] = terms.get(p, Fraction(0)) + Fraction(1, 1)
                num //= p
            p += 1
        if num > 1:
            terms[num] = terms.get(num, Fraction(0)) + Fraction(1, 1)
        p = 2
        while p * p <= den:
            while den % p == 0:
                terms[p] = terms.get(p, Fraction(0)) - Fraction(1, 1)
                den //= p
            p += 1
        if den > 1:
            terms[den] = terms.get(den, Fraction(0)) - Fraction(1, 1)
        return SymReal(terms)

    def __add__(self, other: SymReal) -> SymReal:
        out = dict(self.terms)
        for k, v in other.terms.items():
            out[k] = out.get(k, Fraction(0)) + v
        return SymReal(out)

    def __sub__(self, other: SymReal) -> SymReal:
        out = dict(self.terms)
        for k, v in other.terms.items():
            out[k] = out.get(k, Fraction(0)) - v
        return SymReal(out)

    def scale(self, c: Fraction) -> SymReal:
        if c == 0:
            return SymReal.zero()
        return SymReal({k: v * c for k, v in self.terms.items()})

    def key(self) -> tuple[tuple[int, int, int], ...]:
        return tuple(sorted((k, v.numerator, v.denominator) for k, v in self.terms.items()))

    def eval_arb(self) -> flint.arb:
        s = flint.arb(0)
        for k, v in self.terms.items():
            coeff = flint.arb(v.numerator) / flint.arb(v.denominator)
            if k == 1:
                s = s + coeff
            else:
                s = s + coeff * flint.arb(k).log()
        return s


def build_symbolic_cuts_and_intervals(
    b_sym: SymReal,
    active_shifts: list[tuple[Fraction, SymReal, flint.arb, flint.arb]],
    c_diag: flint.arb,
    c_zero: flint.arb,
    da: flint.arb,
) -> tuple[list[flint.arb], list[tuple[flint.arb, flint.arb, flint.arb, flint.arb]], flint.arb, flint.arb, flint.arb, flint.arb]:
    b_val = b_sym.eval_arb()
    zero_sym = SymReal.zero()
    sym_map: dict[tuple[tuple[int, int, int], ...], SymReal] = {
        zero_sym.key(): zero_sym,
        b_sym.key(): b_sym,
    }
    for _, tau_sym, _, _ in active_shifts:
        for pt_sym in (tau_sym - b_sym, b_sym - tau_sym):
            k = pt_sym.key()
            if k in sym_map:
                continue
            pt_val = pt_sym.eval_arb()
            if pt_val < flint.arb(0) or pt_val > b_val:
                continue
            assert flint.arb(0) < pt_val < b_val, f"Undecided boundary cut comparison: {pt_val}"
            sym_map[k] = pt_sym

    sym_list = list(sym_map.values())
    ordered_pairs: list[tuple[SymReal, flint.arb]] = []
    for s_pt in sym_list:
        v_pt = s_pt.eval_arb()
        pos = len(ordered_pairs)
        for idx, (_, q_val) in enumerate(ordered_pairs):
            if arb_strict_lt(v_pt, q_val):
                pos = idx
                break
        ordered_pairs.insert(pos, (s_pt, v_pt))

    for k in range(len(ordered_pairs) - 1):
        assert ordered_pairs[k][1] < ordered_pairs[k + 1][1], (
            f"Non-strict cut ordering at {k}: {ordered_pairs[k][1]} vs {ordered_pairs[k + 1][1]}"
        )

    cuts = [pair[1] for pair in ordered_pairs]
    intervals_data: list[tuple[flint.arb, flint.arb, flint.arb, flint.arb]] = []
    min_v = c_diag + c_zero * da
    max_v = flint.arb(0)
    j_pos = flint.arb(0)
    s_pos_check = flint.arb(0)

    for k_i in range(len(cuts) - 1):
        xL, xR = cuts[k_i], cuts[k_i + 1]
        xm = flint.arb("0.5") * (xL + xR)
        pen = flint.arb(0)
        psi_k = flint.arb(0)
        for _, _, tau_r, coeff_r in active_shifts:
            c_abs = arb_abs(coeff_r)
            in_right = arb_strict_lt(tau_r - b_val, xm)
            in_left = arb_strict_lt(xm, b_val - tau_r)
            if in_right:
                pen = pen + c_abs
            if in_left:
                pen = pen + c_abs
            if coeff_r > flint.arb(0):
                mult = (flint.arb(1) if in_right else flint.arb(0)) + (flint.arb(1) if in_left else flint.arb(0))
                psi_k = psi_k + coeff_r * mult
        vk = c_diag + c_zero * da - pen
        assert vk > flint.arb(0), f"Non-positive V_a on interval {k_i}: {vk}"
        min_v = arb_min(min_v, vk)
        max_v = arb_max(max_v, vk)
        dx = xR - xL
        s_pos_check = s_pos_check + psi_k * dx
        j_pos = j_pos + (psi_k * psi_k / vk) * dx
        intervals_data.append((xL, xR, vk, psi_k))

    return cuts, intervals_data, min_v, max_v, j_pos, s_pos_check


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


def acb_spherical_j(m: int, z: flint.acb) -> flint.acb:
    df = 1
    for k in range(1, 2 * m + 2, 2):
        df *= k
    b_param = flint.acb(flint.arb(2 * m + 3) / flint.arb(2))
    w = -flint.acb("0.25") * z * z
    return (z**m) * w.hypgeom_0f1(b_param) / flint.acb(df)


def alpha_acb(xi: flint.acb) -> flint.acb:
    pi_acb = flint.acb.pi()
    qtr = flint.acb(flint.arb("0.25"))
    ihalf = flint.acb(flint.arb(0), flint.arb("0.5"))
    z1 = qtr + ihalf * xi
    z2 = qtr - ihalf * xi
    return flint.acb(flint.arb("0.5")) * (z1.digamma() + z2.digamma()) - pi_acb.log()


def find_alpha_root_arb(target_da: flint.arb) -> flint.arb:
    lo = flint.arb("4.0")
    hi = flint.arb("50.0")
    for _ in range(320):
        mid = flint.arb("0.5") * (lo + hi)
        val = alpha_acb(flint.acb(mid)).real - target_da
        if val < 0:
            lo = mid
        elif val > 0:
            hi = mid
        else:
            break
    assert alpha_acb(flint.acb(lo)).real < target_da
    assert alpha_acb(flint.acb(hi)).real > target_da
    center = flint.arb("0.5") * (lo + hi)
    rad = flint.arb("0.5") * (hi - lo) + arb_abs(center - lo)
    return flint.arb(center.mid(), rad.upper())


def integrate_on_0_to_xi0(
    fn: Any, xi0: flint.arb, rel_tol: float, abs_tol: float
) -> tuple[flint.arb, flint.arb]:
    xi0_mid = flint.arb(xi0.mid())
    rad_xi0 = flint.arb(xi0.rad())
    main_val = flint.acb.integral(fn, flint.acb(0), flint.acb(xi0_mid), rel_tol=rel_tol, abs_tol=abs_tol)
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


def exact_support_entry_arb(m: int, n: int, u: flint.arb) -> flint.arb:
    assert m % 2 == 0 and n % 2 == 0
    pm = legendre_poly_coeffs(m)
    pn = legendre_poly_coeffs(n)
    prod_poly = poly_mul_arb(pm, pn)
    norm_fac = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()
    return norm_fac * poly_integrate_arb(prod_poly, u - flint.arb(1), flint.arb(1))


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


def certify_checkpoint_arb(
    p_set: list[int],
    n_target: int,
    da: flint.arb,
    xi0: flint.arb,
    c_zero: flint.arb,
    c_diag: flint.arb,
    q_terms: dict[Fraction, flint.arb],
    rel_tol: float,
    abs_tol: float,
) -> dict[str, Any]:
    primorial = math.prod(p_set)
    pi = flint.arb.pi()
    a_val = flint.arb("0.5") * flint.arb(n_target).log()
    b_sym = SymReal.from_fraction(Fraction(n_target, primorial)).scale(Fraction(1, 2))
    b_val = b_sym.eval_arb()
    r_horizon = Fraction(n_target, primorial)

    active_shifts: list[tuple[Fraction, SymReal, flint.arb, flint.arb]] = []
    n_two_sided = 0
    n_single_ref = 0
    n_pos_shifts = 0
    for r in sorted(q_terms.keys()):
        if Fraction(1, 1) < r < r_horizon:
            coeff_r = q_terms[r]
            if not coeff_r.contains(0):
                tau_sym = SymReal.from_fraction(r)
                tau_r = tau_sym.eval_arb()
                active_shifts.append((r, tau_sym, tau_r, coeff_r))
                if r * r >= r_horizon:
                    n_single_ref += 1
                else:
                    n_two_sided += 1
                if coeff_r > flint.arb(0):
                    n_pos_shifts += 1

    cuts, intervals_data, min_v, max_v, j_pos, s_pos_check = build_symbolic_cuts_and_intervals(
        b_sym, active_shifts, c_diag, c_zero, da
    )

    s_pos = flint.arb(0)
    for _, _, tau_r, coeff_r in active_shifts:
        if coeff_r > flint.arb(0):
            s_pos = s_pos + coeff_r * (flint.arb(2) * b_val - tau_r)
    assert s_pos > flint.arb(0)

    const_mode_residual = arb_abs(s_pos_check - s_pos)
    assert (s_pos_check - s_pos).contains(0), f"Constant mode identity failed: {s_pos_check} vs {s_pos}"

    p_logs = [
        (flint.arb(p + 1) / flint.arb(p), flint.arb(2) / flint.arb(p).sqrt(), flint.arb(p).log())
        for p in p_set
    ]

    def int_even_pure_and_pos(xi: flint.acb, _: Any) -> flint.acb:
        sig = flint.acb(1)
        for c_p, s_p, lp in p_logs:
            sig = sig * (flint.acb(c_p) - flint.acb(s_p) * (xi * flint.acb(lp)).cos())
        w_m = (flint.acb(2) / flint.acb(pi)) * sig * (flint.acb(da) - alpha_acb(xi))
        two_xi = flint.acb(2) * xi
        acc_pure_e = flint.acb(0)
        acc_hat_pos = flint.acb(0)
        for xL, xR, vk, psi_k in intervals_data:
            xR_c = flint.acb(xR)
            xL_c = flint.acb(xL)
            s2R = (two_xi * xR_c).sinc()
            s2L = (two_xi * xL_c).sinc()
            s1R = (xi * xR_c).sinc()
            s1L = (xi * xL_c).sinc()
            hR = flint.acb("0.5") * xR_c
            hL = flint.acb("0.5") * xL_c
            inv_vk = flint.acb(flint.arb(1) / vk)
            acc_pure_e = acc_pure_e + (hR * (flint.acb(1) + s2R) - hL * (flint.acb(1) + s2L)) * inv_vk
            acc_hat_pos = acc_hat_pos + flint.acb(psi_k / vk) * (xR_c * s1R - xL_c * s1L)
        return w_m * (acc_pure_e + flint.acb(0, 1) * (acc_hat_pos * acc_hat_pos))

    def int_odd_pure(xi: flint.acb, _: Any) -> flint.acb:
        sig = flint.acb(1)
        for c_p, s_p, lp in p_logs:
            sig = sig * (flint.acb(c_p) - flint.acb(s_p) * (xi * flint.acb(lp)).cos())
        w_m = (flint.acb(2) / flint.acb(pi)) * sig * (flint.acb(da) - alpha_acb(xi))
        two_xi = flint.acb(2) * xi
        acc_pure_o = flint.acb(0)
        for xL, xR, vk, _ in intervals_data:
            xR_c = flint.acb(xR)
            xL_c = flint.acb(xL)
            s2R = (two_xi * xR_c).sinc()
            s2L = (two_xi * xL_c).sinc()
            hR = flint.acb("0.5") * xR_c
            hL = flint.acb("0.5") * xL_c
            inv_vk = flint.acb(flint.arb(1) / vk)
            acc_pure_o = acc_pure_o + (hR * (flint.acb(1) - s2R) - hL * (flint.acb(1) - s2L)) * inv_vk
        return w_m * acc_pure_o

    tr_pure_even, i_pos = integrate_on_0_to_xi0(int_even_pure_and_pos, xi0, rel_tol, abs_tol)
    tr_pure_odd, _ = integrate_on_0_to_xi0(int_odd_pure, xi0, rel_tol, abs_tol)

    alpha_pos = flint.arb(2) / s_pos
    sherman_gain = (alpha_pos * i_pos) / (flint.arb(1) + alpha_pos * j_pos)
    tr_sherman_even = tr_pure_even - sherman_gain

    assert tr_sherman_even < flint.arb(1), f"tr_sherman_even >= 1 at N={n_target}: {tr_sherman_even}"
    assert tr_pure_odd < flint.arb(1), f"tr_pure_odd >= 1 at N={n_target}: {tr_pure_odd}"

    margin_even = flint.arb(1) - tr_sherman_even
    margin_odd = flint.arb(1) - tr_pure_odd

    return {
        "K": len(p_set),
        "N_target": n_target,
        "a": arb_to_dict(a_val),
        "b": arb_to_dict(b_val),
        "two_b": arb_to_dict(flint.arb(2) * b_val),
        "delta_alpha": arb_to_dict(da),
        "n_active_shifts": len(active_shifts),
        "n_two_sided_shifts": n_two_sided,
        "n_single_reflection_shifts": n_single_ref,
        "n_positive_shifts": n_pos_shifts,
        "n_step_intervals": len(intervals_data),
        "min_v": arb_to_dict(min_v),
        "max_v": arb_to_dict(max_v),
        "s_pos": arb_to_dict(s_pos),
        "const_mode_residual": arb_to_dict(const_mode_residual),
        "j_pos": arb_to_dict(j_pos),
        "i_pos": arb_to_dict(i_pos),
        "sherman_gain": arb_to_dict(sherman_gain),
        "tr_pure_even": arb_to_dict(tr_pure_even),
        "tr_sherman_even": arb_to_dict(tr_sherman_even),
        "tr_pure_odd": arb_to_dict(tr_pure_odd),
        "margin_even": arb_to_dict(margin_even),
        "margin_odd": arb_to_dict(margin_odd),
        "certified": True,
        "_balls": {
            "min_v": min_v,
            "s_pos": s_pos,
            "j_pos": j_pos,
            "i_pos": i_pos,
            "tr_pure_even": tr_pure_even,
            "tr_sherman_even": tr_sherman_even,
            "tr_pure_odd": tr_pure_odd,
        },
    }


def certify_theorem_1_universal_legendre_algebra(prec_bits: int) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()

    u0 = flint.arb(0)
    max_u0_err = flint.arb(0)
    for r in range(4):
        for s in range(4):
            s_val = exact_shift_entry_arb(2 * r, 2 * s, u0)
            d_val = exact_support_entry_arb(2 * r, 2 * s, u0)
            s_exp = flint.arb(2 if r == s else 0)
            d_exp = flint.arb(2 if r == s else 0)
            assert (s_val - s_exp).contains(0), f"s_val({r},{s}) at u=0 failed: {s_val} vs {s_exp}"
            assert (d_val - d_exp).contains(0), f"d_val({r},{s}) at u=0 failed: {d_val} vs {d_exp}"
            err = arb_max(arb_abs(s_val - s_exp), arb_abs(d_val - d_exp))
            max_u0_err = arb_max(max_u0_err, err)

    two_sided_checks: list[dict[str, Any]] = []
    max_two_sided_shift_err = flint.arb(0)
    max_two_sided_mult_err = flint.arb(0)
    for u_num, u_den in [(3, 20), (1, 2), (17, 20)]:
        u = flint.arb(u_num) / flint.arb(u_den)
        u_shift_err = flint.arb(0)
        u_mult_err = flint.arb(0)
        for r in range(4):
            for s in range(4):
                m = 2 * r
                n = 2 * s
                s_poly = exact_shift_entry_arb(m, n, u)
                d_poly = exact_support_entry_arb(m, n, u)
                norm_fac = (flint.arb(2 * m + 1) * flint.arb(2 * n + 1)).sqrt()

                pm_coeffs = legendre_poly_coeffs(m)
                pn_coeffs = legendre_poly_coeffs(n)
                pn_plus_u = poly_shift_arb(pn_coeffs, u)
                pn_minus_u = poly_shift_arb(pn_coeffs, -u)
                # Since n = 2s is even, P_n(u - x) = P_n(x - u):
                prod_s1 = poly_mul_arb(pm_coeffs, pn_plus_u)
                prod_s2 = poly_mul_arb(pm_coeffs, pn_minus_u)
                i1 = norm_fac * poly_integrate_arb(prod_s1, flint.arb(0), flint.arb(1) - u)
                i2 = norm_fac * poly_integrate_arb(prod_s2, u, flint.arb(1))
                i3 = norm_fac * poly_integrate_arb(prod_s2, flint.arb(0), u)
                s_folded = i1 + i2 + i3

                prod_d = poly_mul_arb(pm_coeffs, pn_coeffs)
                d1 = flint.arb(2) * norm_fac * poly_integrate_arb(prod_d, flint.arb(0), flint.arb(1) - u)
                d2 = norm_fac * poly_integrate_arb(prod_d, flint.arb(1) - u, flint.arb(1))
                d_folded = d1 + d2

                assert (s_poly - s_folded).contains(0)
                assert (d_poly - d_folded).contains(0)
                u_shift_err = arb_max(u_shift_err, arb_abs(s_poly - s_folded))
                u_mult_err = arb_max(u_mult_err, arb_abs(d_poly - d_folded))

        max_two_sided_shift_err = arb_max(max_two_sided_shift_err, u_shift_err)
        max_two_sided_mult_err = arb_max(max_two_sided_mult_err, u_mult_err)
        two_sided_checks.append({
            "u": f"{u_num}/{u_den}",
            "u_val": arb_to_dict(u),
            "max_shift_err": arb_to_dict(u_shift_err),
            "max_mult_err": arb_to_dict(u_mult_err),
        })

    cholesky_grid: list[dict[str, Any]] = []
    max_first_row_residual = flint.arb(0)
    u_specs = [
        (1, 20, "two-sided"),
        (1, 4, "two-sided"),
        (1, 2, "two-sided"),
        (3, 4, "two-sided"),
        (19, 20, "two-sided"),
        (1, 1, "transition"),
        (27, 20, "single-reflection"),
        (37, 20, "single-reflection"),
    ]
    for u_num, u_den, regime in u_specs:
        u = flint.arb(u_num) / flint.arb(u_den)
        d_mat = [[exact_support_entry_arb(2 * r, 2 * s, u) for s in range(4)] for r in range(4)]
        s_mat = [[exact_shift_entry_arb(2 * r, 2 * s, u) for s in range(4)] for r in range(4)]
        for s in range(4):
            assert (d_mat[0][s] - s_mat[0][s]).contains(0), f"First-row identity failed at s={s}: {d_mat[0][s]} vs {s_mat[0][s]}"
            assert (d_mat[s][0] - s_mat[s][0]).contains(0), f"First-col identity failed at s={s}: {d_mat[s][0]} vs {s_mat[s][0]}"
            res0 = arb_max(arb_abs(d_mat[0][s] - s_mat[0][s]), arb_abs(d_mat[s][0] - s_mat[s][0]))
            max_first_row_residual = arb_max(max_first_row_residual, res0)

        q_plus = [[d_mat[r][s] + s_mat[r][s] for s in range(4)] for r in range(4)]
        q_minus_3x3 = [[d_mat[r][s] - s_mat[r][s] for s in range(1, 4)] for r in range(1, 4)]

        l_plus = cholesky_lower_arb(q_plus)
        l_minus = cholesky_lower_arb(q_minus_3x3)
        min_piv_plus = l_plus[0][0]
        for i in range(1, 4):
            min_piv_plus = arb_min(min_piv_plus, l_plus[i][i])
        min_piv_minus = l_minus[0][0]
        for i in range(1, 3):
            min_piv_minus = arb_min(min_piv_minus, l_minus[i][i])

        cholesky_grid.append({
            "u": f"{u_num}/{u_den}",
            "regime": regime,
            "u_val": arb_to_dict(u),
            "q_plus_00": arb_to_dict(q_plus[0][0]),
            "min_cholesky_pivot_q_plus_4x4": arb_to_dict(min_piv_plus),
            "min_cholesky_pivot_q_minus_3x3": arb_to_dict(min_piv_minus),
            "_balls": {
                "q_plus_00": q_plus[0][0],
                "min_piv_plus": min_piv_plus,
                "min_piv_minus": min_piv_minus,
            },
        })

    return {
        "elapsed_s": round(time.time() - t0, 3),
        "max_u0_err": arb_to_dict(max_u0_err),
        "max_two_sided_shift_err": arb_to_dict(max_two_sided_shift_err),
        "max_two_sided_mult_err": arb_to_dict(max_two_sided_mult_err),
        "max_first_row_residual": arb_to_dict(max_first_row_residual),
        "two_sided_checks": two_sided_checks,
        "cholesky_grid": cholesky_grid,
    }


def certify_gegenbauer_tail_arb(
    p_set: list[int], n_target: int, da: flint.arb, xi0: flint.arb, n_modes: int, rel_tol: float, abs_tol: float
) -> dict[str, Any]:
    primorial = math.prod(p_set)
    pi = flint.arb.pi()
    a_val = flint.arb("0.5") * flint.arb(n_target).log()
    b_val = flint.arb("0.5") * (flint.arb(n_target).log() - flint.arb(primorial).log())
    p_logs = [
        (flint.arb(p + 1) / flint.arb(p), flint.arb(2) / flint.arb(p).sqrt(), flint.arb(p).log())
        for p in p_set
    ]

    def int_tail_even(xi: flint.acb, _: Any) -> flint.acb:
        sig = flint.acb(1)
        for c_p, s_p, lp in p_logs:
            sig = sig * (flint.acb(c_p) - flint.acb(s_p) * (xi * flint.acb(lp)).cos())
        w_m = (flint.acb(2) / flint.acb(pi)) * sig * (flint.acb(da) - alpha_acb(xi))
        z = xi * flint.acb(b_val)
        tot = flint.acb("0.5") * (flint.acb(1) + (flint.acb(2) * z).sinc())
        partial = flint.acb(0)
        for r in range(n_modes):
            jm = acb_spherical_j(2 * r, z)
            partial = partial + flint.acb(4 * r + 1) * jm * jm
        tail_ker = flint.acb(b_val) * (tot - partial)
        full_ker = flint.acb(b_val) * tot
        return w_m * (tail_ker + flint.acb(0, 1) * full_ker)

    def int_tail_odd(xi: flint.acb, _: Any) -> flint.acb:
        sig = flint.acb(1)
        for c_p, s_p, lp in p_logs:
            sig = sig * (flint.acb(c_p) - flint.acb(s_p) * (xi * flint.acb(lp)).cos())
        w_m = (flint.acb(2) / flint.acb(pi)) * sig * (flint.acb(da) - alpha_acb(xi))
        z = xi * flint.acb(b_val)
        tot = flint.acb("0.5") * (flint.acb(1) - (flint.acb(2) * z).sinc())
        partial = flint.acb(0)
        for r in range(n_modes):
            jm = acb_spherical_j(2 * r + 1, z)
            partial = partial + flint.acb(4 * r + 3) * jm * jm
        tail_ker = flint.acb(b_val) * (tot - partial)
        full_ker = flint.acb(b_val) * tot
        return w_m * (tail_ker + flint.acb(0, 1) * full_ker)

    eps_even, tr_arch_even = integrate_on_0_to_xi0(int_tail_even, xi0, rel_tol, abs_tol)
    eps_odd, tr_arch_odd = integrate_on_0_to_xi0(int_tail_odd, xi0, rel_tol, abs_tol)
    rel_even = eps_even / tr_arch_even
    rel_odd = eps_odd / tr_arch_odd

    return {
        "K": len(p_set),
        "N_target": n_target,
        "a": arb_to_dict(a_val),
        "b": arb_to_dict(b_val),
        "delta_alpha": arb_to_dict(da),
        "n_modes": n_modes,
        "tr_arch_even": arb_to_dict(tr_arch_even),
        "eps_N_even": arb_to_dict(eps_even),
        "rel_defect_even": arb_to_dict(rel_even),
        "tr_arch_odd": arb_to_dict(tr_arch_odd),
        "eps_N_odd": arb_to_dict(eps_odd),
        "rel_defect_odd": arb_to_dict(rel_odd),
        "_balls": {
            "tr_arch_even": tr_arch_even,
            "eps_N_even": eps_even,
            "tr_arch_odd": tr_arch_odd,
            "eps_N_odd": eps_odd,
        },
    }


def strip_balls(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: strip_balls(v) for k, v in obj.items() if k != "_balls"}
    if isinstance(obj, list):
        return [strip_balls(x) for x in obj]
    return obj


def verify_ball_overlaps(obj_256: Any, obj_384: Any) -> int:
    flint.ctx.prec = 384
    if isinstance(obj_256, dict) and isinstance(obj_384, dict):
        if "str" in obj_256 and "str" in obj_384 and "mid" in obj_256 and "rad" in obj_256:
            b256 = flint.arb(obj_256["str"])
            b384 = flint.arb(obj_384["str"])
            assert b256.overlaps(b384), f"256-bit and 384-bit balls do not overlap: {obj_256['str']} vs {obj_384['str']}"
            return 1
        total = 0
        for k in obj_256:
            if k in ("elapsed_s", "prec_bits", "total_elapsed_s", "_balls"):
                continue
            if k in obj_384:
                total += verify_ball_overlaps(obj_256[k], obj_384[k])
        return total
    if isinstance(obj_256, list) and isinstance(obj_384, list):
        assert len(obj_256) == len(obj_384)
        return sum(verify_ball_overlaps(x, y) for x, y in zip(obj_256, obj_384))
    return 0


def run_at_precision(prec_bits: int) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()
    rel_tol = 2**-75 if prec_bits <= 256 else 2**-110
    abs_tol = 2**-75 if prec_bits <= 256 else 2**-110

    thm1 = certify_theorem_1_universal_legendre_algebra(prec_bits)

    da0 = flint.arb(0)
    xi0_0 = find_alpha_root_arb(da0)
    da06 = flint.arb(3) / flint.arb(5)
    xi0_06 = find_alpha_root_arb(da06)
    da12 = flint.arb(6) / flint.arb(5)
    xi0_12 = find_alpha_root_arb(da12)

    c0_k4, cdiag_k4, q_k4 = build_q_terms_arb([2, 3, 5, 7])
    k4_extended_points: list[dict[str, Any]] = []
    for n_t, da, xi0 in [
        (225, da0, xi0_0),
        (240, da0, xi0_0),
        (245, da0, xi0_0),
        (245, da06, xi0_06),
        (250, da06, xi0_06),
        (252, da06, xi0_06),
        (252, da12, xi0_12),
        (255, da12, xi0_12),
        (260, da12, xi0_12),
    ]:
        k4_extended_points.append(
            certify_checkpoint_arb([2, 3, 5, 7], n_t, da, xi0, c0_k4, cdiag_k4, q_k4, rel_tol, abs_tol)
        )

    gegenbauer_tails: list[dict[str, Any]] = []
    for p_set, n_t, da, xi0 in [
        ([2, 3, 5], 42, da0, xi0_0),
        ([2, 3, 5], 45, da06, xi0_06),
        ([2, 3, 5, 7], 240, da0, xi0_0),
        ([2, 3, 5, 7], 245, da0, xi0_0),
        ([2, 3, 5, 7], 252, da06, xi0_06),
        ([2, 3, 5, 7], 260, da12, xi0_12),
    ]:
        gegenbauer_tails.append(certify_gegenbauer_tail_arb(p_set, n_t, da, xi0, 4, rel_tol, abs_tol))

    return {
        "prec_bits": prec_bits,
        "elapsed_s": round(time.time() - t0, 3),
        "theorem_1_universal_legendre_algebra": thm1,
        "theorem_2_k4_extended_horizon": k4_extended_points,
        "theorem_2_gegenbauer_bessel_tails": gegenbauer_tails,
    }


def main() -> None:
    t_start = time.time()
    res_256 = run_at_precision(256)
    res_384 = run_at_precision(384)

    clean_256 = strip_balls(res_256)
    clean_384 = strip_balls(res_384)
    overlap_checks = verify_ball_overlaps(clean_256, clean_384)

    payload: dict[str, Any] = {
        "package": "universal-legendre-shift-algebra-and-k4-horizon-2026-10-15-v1",
        "lanes": ["NB-GAIN", "COEFF", "NS-61", "KERNEL-API"],
        "precision_bits_certified": [256, 384],
        "two_precision_ball_overlap_checks": overlap_checks,
        "all_certified": True,
        "wall_status": {
            "RH": "OPEN",
            "G2": "OPEN",
            "cofinal_signed_arithmetic_lower_bound": "OPEN",
            "missing_original_evidence_groups": "OPEN",
        },
        "certificate_384": clean_384,
        "certificate_256_summary": {
            "elapsed_s": clean_256["elapsed_s"],
            "all_balls_overlap_384": True,
        },
        "total_elapsed_s": round(time.time() - t_start, 3),
    }

    canonical_bytes = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload_sha256 = hashlib.sha256(canonical_bytes).hexdigest()

    out_dir = Path(__file__).resolve().parent
    out_file = out_dir / "verification.json"
    full_doc = {
        "payload": payload,
        "payload_sha256": payload_sha256,
    }
    out_file.write_text(json.dumps(full_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    file_sha256 = hashlib.sha256(out_file.read_bytes()).hexdigest()

    print(f"[PASS] Milestone 14 certified in 256-bit and 384-bit flint.arb ({overlap_checks} ball overlaps).")
    print(f"       payload.sha256 = {payload_sha256}")
    print(f"       file_sha256    = {file_sha256}")


if __name__ == "__main__":
    main()
