#!/usr/bin/env python3
"""
Two-Precision (256-bit and 384-bit) ARB-Certified Verification of Milestone 13:
`three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1` (KERNEL-API)

1. Theorem 1 (KERNEL-API): Universal Schur Decomposition, Two-Sided Positive-Shift
   Step-Rank-1 Minorant, and Single Aggregated Sherman-Morrison Trace Reduction:
   - For every active shift tau_r in (0, 2b) with c_r > 0 (across BOTH the two-sided
     overlap regime 0 < tau_r < b and the single-reflection regime b <= tau_r < 2b),
     M_{tau_r}^+ := c_r psi_r(x) I + c_r P_b(T_{tau_r} + T_{-tau_r})P_b >= 0 satisfies
     (M_{tau_r}^+ 1_{[-b, b]})(x) = 2 c_r psi_r(x) on [0, b], where
     psi_r(x) = 1_{[0, b - tau_r]}(x) + 1_{[tau_r - b, b]}(x) in S_step.
   - Summing over all positive active shifts c_r > 0 and applying operator Cauchy-Schwarz
     to M_pos^+ := sum_{c_r > 0} M_{tau_r}^+ >= 0 at the constant test vector 1_{[0, b]}
     yields the exact rank-1 step minorant:
       M_pos^+ >= (2 / S_pos) |Psi_pos><Psi_pos| >= 0,
     where Psi_pos(x) = sum_{c_r > 0} c_r psi_r(x) in S_step and
     S_pos = sum_{c_r > 0} c_r (2b - tau_r) = int_0^b Psi_pos(x) dx > 0.
   - By the Sherman-Morrison identity on P_0^{even} = V_a(x) I + (2 / S_pos) |Psi_pos><Psi_pos|:
       Tr(K_{sherman, even}) = Tr(K_{pure, even}) - ((2 / S_pos) * I_pos) / (1 + (2 / S_pos) * J_pos),
     where J_pos = <Psi_pos, V_a^{-1} Psi_pos>_{L^2(0, b)} and
     I_pos = <V_a^{-1} Psi_pos, M_{Delta_alpha}^{even} V_a^{-1} Psi_pos>_{L^2(0, b)}.

2. Theorem 2 (KERNEL-API): Crossing the First Internal Primorial Shift Horizons for
   K = 3 (B_{{2,3},{5}}, P_3 = 30) and K = 4 (B_{{2,3,5},{7}}, P_4 = 210):
   - K = 3 at Delta_alpha = 0 (zero archimedean shift!) across N in {36, 37, 38, 39, 40, 41, 42}
     (a in [(1/2) log 36, (1/2) log 42] = [log 6, (1/2) log 42], up to 14 active shifts):
     At N = 40, 41, 42 where Pure-Diagonal Tr(K_{pure, even}) = 1.030545, 1.467972, 2.400252 > 1
     fails, the Sherman-Morrison positive-shift reduction certifies
     Tr(K_{sherman, even}) = 0.458404, 0.533593, 0.626834 < 1!
   - K = 3 at Delta_alpha = 3/5 = 0.60 across N in {42, 43, 44, 45} up to the second internal
     shift horizon a = (1/2) log 45 = log(3*sqrt(5)) (2b = log(3/2), 18 active shifts):
     Where Pure-Diagonal Tr(K_{pure, even}) = 1.131822, 1.465187, 2.002820, 2.768965 > 1 fails,
     the Sherman-Morrison reduction certifies Tr(K_{sherman, even}) = 0.643630, 0.715016,
     0.812353, 0.931891 < 1!
   - K = 4 at Delta_alpha = 0 (zero archimedean shift!) across N in {225, 240} up to the second
     internal shift horizon a = (1/2) log 240 = log(4*sqrt(15)) (2b = log(8/7), 43 active shifts):
     Certifies Tr(K_{sherman, even}) = 0.049964 < 1 at N = 225 and 0.098744 < 1 at N = 240
     (a 4.54x reduction from Tr(K_{pure, even}) = 0.448470)!
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
    """Exact algebraic interval enclosure of min(a, b) with zero float conversions."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a < lo_b else (lo_b if lo_b < lo_a else flint.arb("0.5") * (lo_a + lo_b - abs(lo_a - lo_b)))
    hi = hi_a if hi_a < hi_b else (hi_b if hi_b < hi_a else flint.arb("0.5") * (hi_a + hi_b - abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_max(a: flint.arb, b: flint.arb) -> flint.arb:
    """Exact algebraic interval enclosure of max(a, b) with zero float conversions."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a > lo_b else (lo_b if lo_b > lo_a else flint.arb("0.5") * (lo_a + lo_b + abs(lo_a - lo_b)))
    hi = hi_a if hi_a > hi_b else (hi_b if hi_b > hi_a else flint.arb("0.5") * (hi_a + hi_b + abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_hull(a: flint.arb, b: flint.arb) -> flint.arb:
    """Exact interval hull containing both balls a and b."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a < lo_b else (lo_b if lo_b < lo_a else flint.arb("0.5") * (lo_a + lo_b - abs(lo_a - lo_b)))
    hi = hi_a if hi_a > hi_b else (hi_b if hi_b > hi_a else flint.arb("0.5") * (hi_a + hi_b + abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_strict_lt(a: flint.arb, b: flint.arb) -> bool:
    """Certified strict inequality in ball arithmetic."""
    if a < b:
        return True
    if a > b:
        return False
    raise AssertionError(f"Undecided strict inequality between balls: {a} vs {b}")


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


def deduplicate_and_sort_sym(pts: list[SymReal]) -> list[SymReal]:
    """Deduplicate algebraically identical cut points by exact Q-linear-independence key and sort."""
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

    for k in range(len(ordered) - 1):
        assert ordered[k].ball() < ordered[k + 1].ball(), (
            f"Non-strict cut ordering at {k}: {ordered[k]} vs {ordered[k + 1]}"
        )
    return ordered


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


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
    """Rigorous ball integration over [0, xi0] including endpoint radius enclosure."""
    xi0_mid = flint.arb(xi0.mid())
    rad_xi0 = flint.arb(xi0.rad())
    main_val = flint.acb.integral(fn, flint.acb(0), flint.acb(xi0_mid), rel_tol=rel_tol, abs_tol=abs_tol)
    val_at_ball = fn(flint.acb(xi0), None)
    tail_re = arb_abs(val_at_ball.real) * rad_xi0
    tail_im = arb_abs(val_at_ball.imag) * rad_xi0
    res_re = main_val.real + flint.arb(0, tail_re.upper())
    res_im = main_val.imag + flint.arb(0, tail_im.upper())
    return res_re, res_im


def build_q_terms_arb(p_set: list[int]) -> tuple[flint.arb, flint.arb, dict[Fraction, flint.arb]]:
    """Build exact reduced-fraction dictionary of shift coefficients in L_{P_K}(-W_arith)."""
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
    """
    Certify a single checkpoint N_target (a = (1/2) log N_target) using Theorem 1
    (Universal Schur Decomposition + Single Aggregated Positive-Shift Sherman-Morrison
    Reduction + Pure-Diagonal Odd Sector) with exact SymReal cut points.
    """
    primorial = math.prod(p_set)
    pi = flint.arb.pi()
    s_zero = SymReal.zero()
    s_b = SymReal.log_ratio(Fraction(n_target, primorial), Fraction(1, 2))
    a_val = flint.arb("0.5") * flint.arb(n_target).log()
    b_val = s_b.ball()
    r_horizon = Fraction(n_target, primorial)
    zero_thresh = flint.arb(2) ** (-200)

    active_shifts: list[tuple[Fraction, SymReal, flint.arb, flint.arb]] = []
    n_two_sided = 0
    n_single_ref = 0
    n_pos_shifts = 0
    for r in sorted(q_terms.keys()):
        if Fraction(1, 1) < r < r_horizon:
            coeff_r = q_terms[r]
            if arb_abs(coeff_r) > zero_thresh:
                s_tau = SymReal.log_ratio(r)
                tau_r = s_tau.ball()
                active_shifts.append((r, s_tau, tau_r, coeff_r))
                if r * r >= r_horizon:
                    n_single_ref += 1
                else:
                    n_two_sided += 1
                if coeff_r > flint.arb(0):
                    n_pos_shifts += 1

    raw_cuts: list[SymReal] = [s_zero, s_b]
    for _, s_tau, _, _ in active_shifts:
        for pt in (s_tau - s_b, s_b - s_tau):
            if sym_strict_lt(s_zero, pt) and sym_strict_lt(pt, s_b):
                raw_cuts.append(pt)
    sym_cuts = deduplicate_and_sort_sym(raw_cuts)
    cuts = [c.ball() for c in sym_cuts]

    # Build step intervals (xL, xR, vk, psi_pos_k) on [0, b_val]:
    intervals_data: list[tuple[flint.arb, flint.arb, flint.arb, flint.arb]] = []
    min_v = c_diag + c_zero * da
    max_v = flint.arb(0)
    s_pos = flint.arb(0)
    for _, _, tau_r, coeff_r in active_shifts:
        if coeff_r > flint.arb(0):
            s_pos = s_pos + coeff_r * (flint.arb(2) * b_val - tau_r)
    assert s_pos > flint.arb(0)

    j_pos = flint.arb(0)
    s_pos_check = flint.arb(0)
    for k_i in range(len(sym_cuts) - 1):
        s_xL, s_xR = sym_cuts[k_i], sym_cuts[k_i + 1]
        xL, xR = cuts[k_i], cuts[k_i + 1]
        s_xm = (s_xL + s_xR).scale(Fraction(1, 2))
        pen = flint.arb(0)
        psi_k = flint.arb(0)
        for _, s_tau, _, coeff_r in active_shifts:
            c_abs = arb_abs(coeff_r)
            in_right = sym_strict_lt(s_tau - s_b, s_xm)
            in_left = sym_strict_lt(s_xm, s_b - s_tau)
            if in_right:
                pen = pen + c_abs
            if in_left:
                pen = pen + c_abs
            if coeff_r > flint.arb(0):
                mult = (flint.arb(1) if in_right else flint.arb(0)) + (flint.arb(1) if in_left else flint.arb(0))
                psi_k = psi_k + coeff_r * mult
        vk = c_diag + c_zero * da - pen
        assert vk > flint.arb(0), f"Non-positive V_a on interval {k_i} at N={n_target}: {vk}"
        min_v = arb_min(min_v, vk)
        max_v = arb_max(max_v, vk)
        dx = xR - xL
        s_pos_check = s_pos_check + psi_k * dx
        j_pos = j_pos + (psi_k * psi_k / vk) * dx
        intervals_data.append((xL, xR, vk, psi_k))

    # Verify exact constant-mode identity int_0^b Psi_pos(x) dx == sum_{c_r > 0} c_r (2b - tau_r):
    const_mode_residual = arb_abs(s_pos_check - s_pos)
    assert (s_pos_check - s_pos).contains(0)

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


def run_at_precision(prec_bits: int) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    t0 = time.time()
    rel_tol = 2**-75 if prec_bits <= 256 else 2**-110
    abs_tol = 2**-75 if prec_bits <= 256 else 2**-110

    da0 = flint.arb(0)
    xi0_da0 = find_alpha_root_arb(da0)
    da06 = flint.arb(3) / flint.arb(5)
    xi0_da06 = find_alpha_root_arb(da06)

    # K = 3: P_3 = {2, 3, 5}, P_3# = 30
    c0_k3, cdiag_k3, q_k3 = build_q_terms_arb([2, 3, 5])
    k3_da0_points: list[dict[str, Any]] = []
    for n_t in [36, 37, 38, 39, 40, 41, 42]:
        k3_da0_points.append(
            certify_checkpoint_arb([2, 3, 5], n_t, da0, xi0_da0, c0_k3, cdiag_k3, q_k3, rel_tol, abs_tol)
        )

    k3_da06_points: list[dict[str, Any]] = []
    for n_t in [42, 43, 44, 45]:
        k3_da06_points.append(
            certify_checkpoint_arb([2, 3, 5], n_t, da06, xi0_da06, c0_k3, cdiag_k3, q_k3, rel_tol, abs_tol)
        )

    # K = 4: P_4 = {2, 3, 5, 7}, P_4# = 210
    c0_k4, cdiag_k4, q_k4 = build_q_terms_arb([2, 3, 5, 7])
    k4_da0_points: list[dict[str, Any]] = []
    for n_t in [225, 240]:
        k4_da0_points.append(
            certify_checkpoint_arb([2, 3, 5, 7], n_t, da0, xi0_da0, c0_k4, cdiag_k4, q_k4, rel_tol, abs_tol)
        )

    return {
        "prec_bits": prec_bits,
        "elapsed_s": round(time.time() - t0, 3),
        "xi0_da0": arb_to_dict(xi0_da0),
        "xi0_da06": arb_to_dict(xi0_da06),
        "k3_c_zero": arb_to_dict(c0_k3),
        "k3_c_diag": arb_to_dict(cdiag_k3),
        "k4_c_zero": arb_to_dict(c0_k4),
        "k4_c_diag": arb_to_dict(cdiag_k4),
        "k3_da0_points": k3_da0_points,
        "k3_da06_points": k3_da06_points,
        "k4_da0_points": k4_da0_points,
    }


def strip_balls(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: strip_balls(v) for k, v in obj.items() if k != "_balls"}
    if isinstance(obj, list):
        return [strip_balls(x) for x in obj]
    return obj


def main() -> None:
    t_start = time.time()
    res_256 = run_at_precision(256)
    res_384 = run_at_precision(384)

    overlap_checks = 0
    for group_key in ("k3_da0_points", "k3_da06_points", "k4_da0_points"):
        pts_256 = res_256[group_key]
        pts_384 = res_384[group_key]
        assert len(pts_256) == len(pts_384)
        for p256, p384 in zip(pts_256, pts_384):
            b256 = p256["_balls"]
            b384 = p384["_balls"]
            for k in b256:
                v256: flint.arb = b256[k]
                v384: flint.arb = b384[k]
                assert v256.overlaps(v384), f"Ball mismatch on {group_key} N={p256['N_target']} key={k}: {v256} vs {v384}"
                overlap_checks += 1

    clean_256 = strip_balls(res_256)
    clean_384 = strip_balls(res_384)

    payload: dict[str, Any] = {
        "package": "three-prime-complete-shift-spectrum-and-horizon-2026-10-15-v1",
        "lane": "KERNEL-API",
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

    print(f"[PASS] Milestone 13 certified in 256-bit and 384-bit flint.arb ({overlap_checks} ball overlaps).")
    print(f"       payload.sha256 = {payload_sha256}")
    print(f"       file_sha256    = {file_sha256}")


if __name__ == "__main__":
    main()
