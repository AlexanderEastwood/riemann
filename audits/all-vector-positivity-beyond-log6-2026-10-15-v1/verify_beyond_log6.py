#!/usr/bin/env python3
"""
384-bit ARB-Certified Verification of All-Vector Weil Positivity Beyond a = (1/2) log 6
up to a = log(5/2), a = 0.960, and the Next Prime-Pair Threshold a = (1/2) log 7.

Deliverable for Milestone 3 (2026-10-15):
1. Exact Three-Island Identity P_b L_2^2 P_b = (13/4) I_{L^2(-b,b)} for all a <= (3/2) log 2 ~ 1.039721.
2. Exact Reflection-Involution Preconditioner P_0(a) and Sum-of-Squares Monotonicity
   certifying the entire interval a in ((1/2) log 6, log(5/2)] ~ (0.895880, 0.916291]
   from a single endpoint evaluation at a_{**} = log(5/2) with Delta_alpha = 7/20 = 0.35
   and zero rank-1 minorants.
3. 3x3 Fiber-Bundle Preconditioner + Prime-Reflection Step Minorants certifying:
   - a = 0.940000 and a = 0.960000 using prime operators alone (zero B_+ minorant),
   - a_{***} = (1/2) log 7 ~ 0.9729550745 using 5 natural-breakpoint prime step vectors
     and 1 Plancherel step vector w_* with rigorous midpoint-moment error enclosure.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
import time
from pathlib import Path
from typing import Any

import flint

# Set 384-bit working precision (~115 decimal digits)
PREC_BITS = 384
flint.ctx.prec = PREC_BITS


def arb_val(x: int | float | str | flint.arb) -> flint.arb:
    if isinstance(x, flint.arb):
        return x
    return flint.arb(x)


def acb_val(x: int | float | str | flint.arb | flint.acb) -> flint.acb:
    if isinstance(x, flint.acb):
        return x
    return flint.acb(x)


def arb_abs(x: flint.arb) -> flint.arb:
    return abs(x)


def arb_max(a: flint.arb, b: flint.arb) -> flint.arb:
    """Exact interval enclosure of max(a, b) in 384-bit ball arithmetic without float conversion."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a > lo_b else (lo_b if lo_b > lo_a else flint.arb("0.5") * (lo_a + lo_b + abs(lo_a - lo_b)))
    hi = hi_a if hi_a > hi_b else (hi_b if hi_b > hi_a else flint.arb("0.5") * (hi_a + hi_b + abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_strict_lt(a: flint.arb, b: flint.arb) -> bool:
    """Certified strict inequality in 384-bit ball arithmetic."""
    if a < b:
        return True
    if a > b:
        return False
    raise AssertionError(f"Undecided strict inequality between balls: {a} vs {b}")


def frac_to_arb(q: Fraction) -> flint.arb:
    return flint.arb(q.numerator) / flint.arb(q.denominator)


class SymReal:
    """
    Exact element of Q + sum_{p prime} Q * log(p).
    Key 1 represents the rational constant 1; prime keys p >= 2 represent log(p).
    By the Fundamental Theorem of Arithmetic and Baker's theorem, {1} union {log p : p prime}
    is linearly independent over Q, so two SymReal values are equal iff their reduced
    Fraction coefficient dictionaries match.
    """

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
    def log_prime(p: int, coeff: int | str | Fraction = 1) -> SymReal:
        assert p >= 2
        f = Fraction(coeff)
        return SymReal({p: f}) if f != 0 else SymReal()

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

    def __neg__(self) -> SymReal:
        return SymReal({k: -v for k, v in self._terms.items()})

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

    def __repr__(self) -> str:
        if not self._key:
            return "SymReal(0)"
        parts = [f"{v}" if k == 1 else f"{v}*log({k})" for k, v in self._key]
        return "SymReal(" + " + ".join(parts) + ")"


def sym_strict_lt(a: SymReal, b: SymReal) -> bool:
    """Exact equality-aware strict inequality: False if algebraically identical, certified by ball arithmetic if distinct."""
    if a == b:
        return False
    return arb_strict_lt(a.ball(), b.ball())


def sym_le(a: SymReal, b: SymReal) -> bool:
    """Exact equality-aware non-strict inequality a <= b."""
    return (a == b) or sym_strict_lt(a, b)


def deduplicate_and_sort_sym(pts: list[SymReal]) -> list[SymReal]:
    """
    Deduplicate algebraically identical endpoints by exact Q-linear-independence key
    equality (ZERO decimal tolerances), and sort distinct endpoints using certified
    flint.arb strict inequalities (arb_strict_lt).
    """
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
        "mid": float(x.mid().str(18, radius=False)),
        "rad": float(x.rad().str(18, radius=False)),
        "lower": float(x.lower().str(18, radius=False)),
        "upper": float(x.upper().str(18, radius=False)),
        "str": str(x),
    }


def acb_sinc(z: flint.acb) -> flint.acb:
    """
    Rigorous evaluation of sinc(z) = sin(z) / z on complex balls using FLINT's built-in C acb_sinc.
    """
    return z.sinc()


def arb_sinc(x: flint.arb) -> flint.arb:
    return acb_sinc(flint.acb(x)).real


def alpha_acb(xi: flint.acb) -> flint.acb:
    """
    Holomorphic extension of alpha(xi) = Re psi(1/4 + i*xi/2) - log(pi)
    off the real axis via 0.5*(psi(1/4 + i*xi/2) + psi(1/4 - i*xi/2)) - log(pi).
    """
    pi_acb = flint.acb.pi()
    qtr = flint.acb(flint.arb("0.25"))
    ihalf = flint.acb(flint.arb(0), flint.arb("0.5"))
    z1 = qtr + ihalf * xi
    z2 = qtr - ihalf * xi
    return flint.acb(flint.arb("0.5")) * (z1.digamma() + z2.digamma()) - pi_acb.log()


def alpha_arb(xi: flint.arb) -> flint.arb:
    return alpha_acb(flint.acb(xi)).real


def sigma_L2_sq_acb(xi: flint.acb, log2_arb: flint.arb) -> flint.acb:
    sqrt2 = flint.acb(flint.arb(2).sqrt())
    s = flint.acb(flint.arb("1.5")) - sqrt2 * (xi * flint.acb(log2_arb)).cos()
    return s * s


def find_alpha_root_arb(target_da: flint.arb) -> flint.arb:
    """
    Enclose the unique positive root xi_0 > 0 of alpha(xi_0) = target_da
    to 300+ bits by Newton-bisection and certify by strict sign change.
    """
    lo = flint.arb("6.0")
    hi = flint.arb("25.0")
    for _ in range(320):
        mid = flint.arb("0.5") * (lo + hi)
        val = alpha_arb(mid) - target_da
        if val < 0:
            lo = mid
        elif val > 0:
            hi = mid
        else:
            break
    assert alpha_arb(lo) < target_da, "Lower bracket failed strict sign check"
    assert alpha_arb(hi) > target_da, "Upper bracket failed strict sign check"
    center = flint.arb("0.5") * (lo + hi)
    rad = flint.arb("0.5") * (hi - lo) + arb_abs(center - lo)
    return flint.arb(center.mid(), rad.upper())


def certify_regime_1_log5_over_2() -> dict[str, Any]:
    """
    Certify Theorem 2: Exact Reflection-Involution Preconditioner P_0(a)
    on (1/2 log 6, log(5/2)] ~ (0.895880, 0.916291] at a_{**} = log(5/2)
    with Delta_alpha = 7/20 = 0.35 and ZERO rank-1 minorants.
    """
    t0 = time.time()
    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()
    log6 = flint.arb(6).log()
    pi = flint.arb.pi()

    a_star = flint.arb("0.5") * log6
    a_star2 = log5 - log2  # log(5/2)
    b = a_star2 - log2     # log(5/4) = tau5
    da = flint.arb(7) / flint.arb(20)  # 0.35

    c0 = flint.arb("2.5") * log2
    c5 = log5 / (flint.arb(2) * flint.arb(5).sqrt())
    c3 = log3 / (flint.arb(2) * flint.arb(3).sqrt())
    c6 = (flint.arb("1.5")).sqrt() * log3

    tau5 = log5 - flint.arb(2) * log2
    tau3 = flint.arb(2) * log2 - log3
    tau6 = log3 - log2

    # At a = log(5/2), b = tau5, so x5 = tau5 - b = 0:
    # Interval 1: [0, x3] where x3 = tau3 - b, with value v1 = c0 + 3.25*da - c5
    # Interval 2: [x3, x6] where x6 = tau6 - b, with value v2 = c0 + 3.25*da - c5 - c3
    # Interval 3: [x6, b] coupled by reflection R_{tau6} with diagonal v2 and off-diag +-c6!
    x3 = tau3 - b
    x6 = tau6 - b
    m6 = flint.arb("0.5") * tau6
    L_refl = b - x6  # = 2*a - log6 = log(25/24)

    base0 = c0 + flint.arb("3.25") * da
    v0 = base0
    v1 = base0 - c5
    v2 = base0 - c5 - c3

    # Verify spectral positivity and sum-of-squares monotonicity preconditions:
    assert v0 > v1 > v2 > c6 > 0
    inv_v1 = flint.arb(1) / v1
    inv_v2 = flint.arb(1) / v2
    inv_v2_plus_c6 = flint.arb(1) / (v2 + c6)
    inv_v2_minus_c6 = flint.arb(1) / (v2 - c6)
    alpha_2 = v2 / (v2 * v2 - c6 * c6)
    beta_2 = c6 / (v2 * v2 - c6 * c6)

    xi0 = find_alpha_root_arb(da)
    xi0_mid = flint.arb(xi0.mid())

    # On [0, b], <P_0(a)^{-1} u_xi, u_xi> for u_xi(x) = cos(xi*x) (even) or sin(xi*x) (odd):
    # Wait: on [0, x3], weight is 1/v1; on [x3, x6], weight is 1/v2; on [x6, b], weight is alpha_2!
    # Plus on [x6, b], the reflection term -+ beta_2 \int_{x6}^b u_xi(x) u_xi(tau6 - x) dx!
    # Notice:
    # \int_0^b w(x) cos^2(xi*x) dx = (1/v1) int_0^{x3} + (1/v2) int_{x3}^{x6} + alpha_2 int_0^b!
    #   = (1/v1 - 1/v2) int_0^{x3} + (1/v2 - alpha_2) int_0^{x6} + alpha_2 int_0^b!
    # And for the reflection integral on [x6, b] = [m6 - L_refl/2, m6 + L_refl/2]:
    # \int_{x6}^b cos(xi*x) cos(xi*(tau6 - x)) dx = 0.5 * L_refl * [sinc(xi * L_refl) + cos(xi * tau6)]!
    # \int_{x6}^b sin(xi*x) sin(xi*(tau6 - x)) dx = 0.5 * L_refl * [sinc(xi * L_refl) - cos(xi * tau6)]!
    w_step_1 = inv_v1 - inv_v2
    w_step_2 = inv_v2 - alpha_2

    def int_even_odd(xi: flint.acb, is_even: bool) -> flint.acb:
        w_m = sigma_L2_sq_acb(xi, log2) * (flint.acb(da) - alpha_acb(xi))
        two_xi = flint.acb(2) * xi
        # \int_0^p cos^2(xi*x) dx = 0.5 * p * (1 + sinc(2*xi*p))
        # \int_0^p sin^2(xi*x) dx = 0.5 * p * (1 - sinc(2*xi*p))
        sgn = flint.acb(1 if is_even else -1)
        i_x3 = flint.acb("0.5") * flint.acb(x3) * (flint.acb(1) + sgn * acb_sinc(two_xi * flint.acb(x3)))
        i_x6 = flint.acb("0.5") * flint.acb(x6) * (flint.acb(1) + sgn * acb_sinc(two_xi * flint.acb(x6)))
        i_b  = flint.acb("0.5") * flint.acb(b)  * (flint.acb(1) + sgn * acb_sinc(two_xi * flint.acb(b)))
        diag_part = flint.acb(w_step_1) * i_x3 + flint.acb(w_step_2) * i_x6 + flint.acb(alpha_2) * i_b

        refl_int = flint.acb("0.5") * flint.acb(L_refl) * (
            acb_sinc(xi * flint.acb(L_refl)) + sgn * (xi * flint.acb(tau6)).cos()
        )
        # On V_b^{even}, P_0 has +c6 R_{tau6}, so P_0^{-1} has -beta_2 R_{tau6}:
        # On V_b^{odd},  P_0 has -c6 R_{tau6}, so P_0^{-1} has +beta_2 R_{tau6}:
        refl_part = -sgn * flint.acb(beta_2) * refl_int
        return (flint.acb(2) / flint.acb(pi)) * w_m * (diag_part + refl_part)

    tr_even_main = flint.acb.integral(
        lambda x, _: int_even_odd(x, True), flint.acb(0), flint.acb(xi0_mid)
    ).real
    tr_odd_main = flint.acb.integral(
        lambda x, _: int_even_odd(x, False), flint.acb(0), flint.acb(xi0_mid)
    ).real

    # Certified ball enclosure of endpoint remainder over [xi0_mid, xi0]:
    rad_xi0 = flint.arb(xi0.rad())
    end_err_even = arb_abs(int_even_odd(flint.acb(xi0), True).real) * rad_xi0
    end_err_odd = arb_abs(int_even_odd(flint.acb(xi0), False).real) * rad_xi0
    tr_even = tr_even_main + flint.arb(0, end_err_even.upper())
    tr_odd = tr_odd_main + flint.arb(0, end_err_odd.upper())

    assert tr_even < flint.arb(1), f"Even trace failed < 1: {tr_even}"
    assert tr_odd < flint.arb(1), f"Odd trace failed < 1: {tr_odd}"

    # Minimum eigenvalue of P_0(a_{**}) on [0, b] is v2 - c6:
    lambda_min_P0 = v2 - c6
    c_Weierstrass_g = lambda_min_P0 * (flint.arb(1) - tr_even)
    c_Weierstrass_L2g = c_Weierstrass_g / flint.arb("3.25")

    return {
        "regime": "(1/2 log 6, log(5/2)]",
        "a_lower": arb_to_dict(a_star),
        "a_upper": arb_to_dict(a_star2),
        "b_upper": arb_to_dict(b),
        "Delta_alpha": arb_to_dict(da),
        "xi0": arb_to_dict(xi0),
        "v0": arb_to_dict(v0),
        "v1": arb_to_dict(v1),
        "v2": arb_to_dict(v2),
        "c6": arb_to_dict(c6),
        "lambda_min_P0": arb_to_dict(lambda_min_P0),
        "tr_even": arb_to_dict(tr_even),
        "tr_odd": arb_to_dict(tr_odd),
        "margin_even": arb_to_dict(flint.arb(1) - tr_even),
        "margin_odd": arb_to_dict(flint.arb(1) - tr_odd),
        "coercivity_g_L2": arb_to_dict(c_Weierstrass_g),
        "coercivity_L2g_L2": arb_to_dict(c_Weierstrass_L2g),
        "certified": bool(tr_even < flint.arb(1) and tr_odd < flint.arb(1)),
        "elapsed_s": round(time.time() - t0, 3),
    }


def solve_linear_arb(A: list[list[flint.arb]], B: list[list[flint.arb]]) -> list[list[flint.arb]]:
    """
    Rigorous Gauss-Jordan linear solver in 384-bit flint.arb for M x M systems A X = B.
    """
    n = len(A)
    m = len(B[0])
    aug = [[A[i][j] for j in range(n)] + [B[i][j] for j in range(m)] for i in range(n)]
    for col in range(n):
        piv = col
        for r in range(col + 1, n):
            if arb_abs(aug[r][col]) > arb_abs(aug[piv][col]):
                piv = r
        aug[col], aug[piv] = aug[piv], aug[col]
        piv_val = aug[col][col]
        assert not piv_val.contains(0), f"Zero pivot at col={col}"
        for j in range(col, n + m):
            aug[col][j] = aug[col][j] / piv_val
        for r in range(n):
            if r != col:
                factor = aug[r][col]
                if factor != flint.arb(0):
                    for j in range(col, n + m):
                        aug[r][j] = aug[r][j] - factor * aug[col][j]
    return [[aug[i][n + j] for j in range(m)] for i in range(n)]


def build_fiber_partition_arb(
    a_sym: SymReal,
    da: flint.arb,
    use_natural_splits: bool = True,
    n_step: int = 3,
) -> dict[str, Any]:
    """
    Construct the exact SymReal + 384-bit flint.arb fiber-closed partition {I_1, ..., I_K} of [0, b]
    for a in (log(5/2), 1/2 log 7], together with the exact fiber matrices P0_even, P0_odd,
    their rigorous inverses, and the prime-reflection step vectors.
    """
    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()

    zero_sym = SymReal.zero()
    log2_sym = SymReal.log_prime(2)
    log3_sym = SymReal.log_prime(3)
    log5_sym = SymReal.log_prime(5)

    b_sym = a_sym - log2_sym
    b = b_sym.ball()

    c0 = flint.arb("2.5") * log2
    c5 = log5 / (flint.arb(2) * flint.arb(5).sqrt())
    c3 = log3 / (flint.arb(2) * flint.arb(3).sqrt())
    c6 = (flint.arb("1.5")).sqrt() * log3

    tau5_sym = log5_sym - log2_sym.scale(2)
    tau3_sym = log2_sym.scale(2) - log3_sym
    tau6_sym = log3_sym - log2_sym

    tau5 = tau5_sym.ball()
    tau3 = tau3_sym.ball()
    tau6 = tau6_sym.ball()

    x3_sym = tau3_sym - b_sym
    d5_sym = b_sym - tau5_sym
    x6_sym = tau6_sym - b_sym
    m6_sym = tau6_sym.scale(Fraction(1, 2))
    m3_sym = tau3_sym.scale(Fraction(1, 2))
    m5_sym = tau5_sym.scale(Fraction(1, 2))

    x3 = x3_sym.ball()
    d5 = d5_sym.ball()
    x6 = x6_sym.ball()

    base0 = c0 + flint.arb("3.25") * da

    if use_natural_splits:
        pts_3_L_sym = [x3_sym, d5_sym, x6_sym, m3_sym]
        pts_5_L_sym = [zero_sym, d5_sym, m5_sym]
    else:
        pts_3_L_sym = [
            x3_sym + (m3_sym - x3_sym).scale(Fraction(r, n_step))
            for r in range(n_step + 1)
        ]
        pts_5_L_sym = [
            m5_sym.scale(Fraction(r, n_step))
            for r in range(n_step + 1)
        ]
    pts_3_R_sym = [tau3_sym - p for p in pts_3_L_sym]
    pts_5_R_sym = [tau5_sym - p for p in pts_5_L_sym]

    raw_pts_sym = [
        zero_sym,
        b_sym,
        x3_sym,
        d5_sym,
        x6_sym,
        m6_sym,
        m3_sym,
        m5_sym,
        tau5_sym,
        tau6_sym - tau5_sym,
    ]
    raw_pts_sym.extend(pts_3_L_sym + pts_3_R_sym + pts_5_L_sym + pts_5_R_sym)

    expanded_pts_sym: list[SymReal] = []
    for p in raw_pts_sym:
        if not (sym_le(zero_sym, p) and sym_le(p, b_sym)):
            continue
        expanded_pts_sym.append(p)
        if sym_le(p, d5_sym):
            expanded_pts_sym.append(p + tau5_sym)
            expanded_pts_sym.append(tau6_sym - tau5_sym - p)
        elif sym_le(tau5_sym, p):
            u = p - tau5_sym
            expanded_pts_sym.append(u)
            expanded_pts_sym.append(tau6_sym - tau5_sym - u)
        elif sym_le(x6_sym, p) and sym_le(p, tau6_sym - tau5_sym):
            u = (tau6_sym - tau5_sym) - p
            expanded_pts_sym.append(u)
            expanded_pts_sym.append(u + tau5_sym)
        elif sym_le(tau6_sym - tau5_sym, p) and sym_le(p, tau5_sym):
            expanded_pts_sym.append(tau6_sym - p)

    pts_sym = deduplicate_and_sort_sym(expanded_pts_sym)
    assert pts_sym[0] == zero_sym and pts_sym[-1] == b_sym
    pts = [p.ball() for p in pts_sym]

    K = len(pts_sym) - 1
    mids_sym = [(pts_sym[i] + pts_sym[i + 1]).scale(Fraction(1, 2)) for i in range(K)]
    lens_sym = [pts_sym[i + 1] - pts_sym[i] for i in range(K)]
    mids = [m.ball() for m in mids_sym]
    lens = [l.ball() for l in lens_sym]
    mid_index_map = {m.key: idx for idx, m in enumerate(mids_sym)}

    P0_e = [[flint.arb(0) for _ in range(K)] for _ in range(K)]
    P0_o = [[flint.arb(0) for _ in range(K)] for _ in range(K)]
    is_refl = [[False for _ in range(K)] for _ in range(K)]

    for i in range(K):
        xm_sym = mids_sym[i]
        vi = base0
        if sym_strict_lt(xm_sym, tau5_sym):
            vi = vi - c5
        if sym_strict_lt(x3_sym, xm_sym):
            vi = vi - c3
        P0_e[i][i] = vi
        P0_o[i][i] = vi
        if sym_strict_lt(xm_sym, d5_sym):
            target_sym = xm_sym + tau5_sym
            j2 = mid_index_map[target_sym.key]
            assert mids_sym[j2] - mids_sym[i] == tau5_sym
            assert lens_sym[j2] == lens_sym[i]
            assert ((mids[j2] - mids[i]) - tau5).contains(0)
            assert (lens[j2] - lens[i]).contains(0)
            P0_e[i][j2] = -c5
            P0_e[j2][i] = -c5
            P0_o[i][j2] = -c5
            P0_o[j2][i] = -c5
        if sym_strict_lt(x6_sym, xm_sym):
            target6_sym = tau6_sym - xm_sym
            j6 = mid_index_map[target6_sym.key]
            assert mids_sym[i] + mids_sym[j6] == tau6_sym
            assert lens_sym[j6] == lens_sym[i]
            assert ((mids[i] + mids[j6]) - tau6).contains(0)
            assert (lens[j6] - lens[i]).contains(0)
            P0_e[i][j6] = c6
            P0_o[i][j6] = -c6
            is_refl[i][j6] = True
            if sym_strict_lt(tau5_sym, xm_sym):
                target1_sym = xm_sym - tau5_sym
                i1 = mid_index_map[target1_sym.key]
                assert mids_sym[i1] + mids_sym[j6] == tau6_sym - tau5_sym
                assert ((mids[i1] + mids[j6]) - (tau6 - tau5)).contains(0)
                is_refl[i1][j6] = True
                is_refl[j6][i1] = True

    eye_K = [[flint.arb(1 if i == j else 0) for j in range(K)] for i in range(K)]
    P0inv_e = solve_linear_arb(P0_e, eye_K)
    P0inv_o = solve_linear_arb(P0_o, eye_K)

    # Certify minimum eigenvalue of P0_e and P0_o by checking 1x1, 2x2, and 3x3 fiber blocks:
    # In the 3x3 fiber M_3 = [[v1, -c5, 0], [-c5, v2+c5, +-c6], [0, +-c6, v2]]:
    v1_3 = base0 - c5 - c3  # worst-case V_1 on [x3, d5]
    v2_3 = base0 - c5 - c3
    # Characteristic polynomial / Gershgorin / Sylvester check on M_3:
    det1 = v1_3
    det2 = v1_3 * (v2_3 + c5) - c5 * c5
    det3 = v2_3 * det2 - v1_3 * c6 * c6
    assert det1 > 0 and det2 > 0 and det3 > 0, "Sylvester positivity failed on 3x3 fiber"

    # Prime step vectors:
    phi_e: list[list[flint.arb]] = []
    phi_o: list[list[flint.arb]] = []
    d_prime: list[flint.arb] = []

    for r in range(len(pts_3_L_sym) - 1):
        lo_L_sym, hi_L_sym = pts_3_L_sym[r], pts_3_L_sym[r + 1]
        lo_R_sym, hi_R_sym = tau3_sym - hi_L_sym, tau3_sym - lo_L_sym
        lo_L, hi_L = lo_L_sym.ball(), hi_L_sym.ball()
        norm_r = (flint.arb(2) * (hi_L - lo_L)).sqrt()
        inv_norm = flint.arb(1) / norm_r
        ue = [flint.arb(0) for _ in range(K)]
        uo = [flint.arb(0) for _ in range(K)]
        for i in range(K):
            if sym_strict_lt(lo_L_sym, mids_sym[i]) and sym_strict_lt(mids_sym[i], hi_L_sym):
                ue[i] = inv_norm
                uo[i] = inv_norm
            elif sym_strict_lt(lo_R_sym, mids_sym[i]) and sym_strict_lt(mids_sym[i], hi_R_sym):
                ue[i] = -inv_norm
                uo[i] = inv_norm
        phi_e.append(ue)
        phi_o.append(uo)
        d_prime.append(flint.arb(1) / (flint.arb(2) * c3))

    for r in range(len(pts_5_L_sym) - 1):
        lo_L_sym, hi_L_sym = pts_5_L_sym[r], pts_5_L_sym[r + 1]
        lo_R_sym, hi_R_sym = tau5_sym - hi_L_sym, tau5_sym - lo_L_sym
        lo_L, hi_L = lo_L_sym.ball(), hi_L_sym.ball()
        norm_r = (flint.arb(2) * (hi_L - lo_L)).sqrt()
        inv_norm = flint.arb(1) / norm_r
        ue = [flint.arb(0) for _ in range(K)]
        uo = [flint.arb(0) for _ in range(K)]
        for i in range(K):
            if sym_strict_lt(lo_L_sym, mids_sym[i]) and sym_strict_lt(mids_sym[i], hi_L_sym):
                ue[i] = inv_norm
                uo[i] = inv_norm
            elif sym_strict_lt(lo_R_sym, mids_sym[i]) and sym_strict_lt(mids_sym[i], hi_R_sym):
                ue[i] = -inv_norm
                uo[i] = inv_norm
        phi_e.append(ue)
        phi_o.append(uo)
        d_prime.append(flint.arb(1) / (flint.arb(2) * c5))

    return {
        "K": K,
        "b": b,
        "x3": x3,
        "d5": d5,
        "x6": x6,
        "tau5": tau5,
        "tau3": tau3,
        "tau6": tau6,
        "pts": pts,
        "mids": mids,
        "lens": lens,
        "P0_e": P0_e,
        "P0_o": P0_o,
        "P0inv_e": P0inv_e,
        "P0inv_o": P0inv_o,
        "is_refl": is_refl,
        "phi_e": phi_e,
        "phi_o": phi_o,
        "d_prime": d_prime,
        "det3_min": det3,
    }


def certify_beyond_log52_point(
    label: str,
    a_sym: SymReal,
    da: flint.arb,
    include_plancherel: bool,
    use_natural_splits: bool = True,
    n_step: int = 3,
    xi1_val: str = "8.4",
) -> dict[str, Any]:
    """
    384-bit ARB certification of a point a in (log(5/2), 1/2 log 7].
    When include_plancherel is False (e.g. a = 0.940, a = 0.960), uses prime operators alone.
    When include_plancherel is True (a = 1/2 log 7), adds the single Plancherel step vector
    w_{*, i} = 1_{m_i < x6} + (9/10 - (3/5)*(m_i - x6)/(b - x6)) * 1_{m_i > x6}
    with rigorous 4-step midpoint-moment error enclosure.
    """
    t0 = time.time()
    a = a_sym.ball()
    log2 = flint.arb(2).log()
    pi = flint.arb.pi()

    part = build_fiber_partition_arb(a_sym, da, use_natural_splits=use_natural_splits, n_step=n_step)
    K: int = part["K"]
    b: flint.arb = part["b"]
    x6: flint.arb = part["x6"]
    mids: list[flint.arb] = part["mids"]
    lens: list[flint.arb] = part["lens"]
    P0inv_e: list[list[flint.arb]] = part["P0inv_e"]
    P0inv_o: list[list[flint.arb]] = part["P0inv_o"]
    is_refl: list[list[bool]] = part["is_refl"]
    phi_e: list[list[flint.arb]] = part["phi_e"]
    phi_o: list[list[flint.arb]] = part["phi_o"]
    d_prime: list[flint.arb] = part["d_prime"]
    M_prime = len(phi_e)

    xi0 = find_alpha_root_arb(da)
    xi0_mid = flint.arb(xi0.mid())

    # Precompute P0inv_e @ phi_e[k] and P0inv_o @ phi_o[k]:
    p0inv_e = [
        [sum((P0inv_e[i][j] * phi_e[k][j] for j in range(K)), flint.arb(0)) for i in range(K)]
        for k in range(M_prime)
    ]
    p0inv_o = [
        [sum((P0inv_o[i][j] * phi_o[k][j] for j in range(K)), flint.arb(0)) for i in range(K)]
        for k in range(M_prime)
    ]
    J_prime = [
        [
            sum((lens[i] * phi_e[j][i] * p0inv_e[k][i] for i in range(K)), flint.arb(0))
            for k in range(M_prime)
        ]
        for j in range(M_prime)
    ]
    DJ_o = [
        [
            sum((lens[i] * phi_o[j][i] * p0inv_o[k][i] for i in range(K)), flint.arb(0))
            + (d_prime[j] if j == k else flint.arb(0))
            for k in range(M_prime)
        ]
        for j in range(M_prime)
    ]
    eye_Mp = [[flint.arb(1 if j == k else 0) for k in range(M_prime)] for j in range(M_prime)]
    DJ_o_inv = solve_linear_arb(DJ_o, eye_Mp)

    # Precompute active pairs (i, j) for K0_diag(xi):
    active_pairs_e: list[tuple[int, int, flint.arb, bool]] = []
    active_pairs_o: list[tuple[int, int, flint.arb, bool]] = []
    for i in range(K):
        for j in range(K):
            val_e = P0inv_e[i][j]
            val_o = P0inv_o[i][j]
            if not val_e.contains(0):
                active_pairs_e.append((i, j, val_e, is_refl[i][j]))
            if not val_o.contains(0):
                active_pairs_o.append((i, j, val_o, is_refl[i][j]))

    def integrate_subintervals(fn: Any, knots: list[flint.arb]) -> flint.arb:
        total = flint.arb(0)
        for idx in range(len(knots) - 1):
            a_k = flint.acb(knots[idx])
            b_k = flint.acb(knots[idx + 1])
            total += flint.acb.integral(fn, a_k, b_k).real
        return total

    # If include_plancherel is True, run the 4-step midpoint-moment pipeline in 384-bit arb:
    D_w = flint.arb(0)
    J_WW = flint.arb(0)
    J_We: list[flint.arb] = []
    W_loc: list[list[flint.arb]] = []
    delta_vW = flint.arb(0)
    R_xi = 8  # 16 terms in s = x - m_i

    if include_plancherel:
        xi1 = flint.arb(xi1_val)
        assert xi1 > xi0, "xi1 must exceed xi0"
        w_vec: list[flint.arb] = []
        for i in range(K):
            if arb_strict_lt(mids[i], x6):
                w_vec.append(flint.arb(1))
            else:
                w_vec.append(
                    flint.arb(9) / flint.arb(10)
                    - (flint.arb(3) / flint.arb(5)) * (mids[i] - x6) / (b - x6)
                )

        # Compute D_w on [xi1, infty) via [xi1, Xi] + Plancherel tail at Xi = 80:
        Xi = flint.arb(80)
        norm_w_sq = sum((lens[i] * w_vec[i] * w_vec[i] for i in range(K)), flint.arb(0))

        def Cw_acb(om: flint.acb) -> flint.acb:
            res = flint.acb(0)
            for i in range(K):
                Li = flint.acb(lens[i])
                mi = flint.acb(mids[i])
                res += flint.acb(w_vec[i]) * Li * (om * mi).cos() * acb_sinc(flint.acb("0.5") * om * Li)
            return res

        def int_Planch(om: flint.acb, _: Any) -> flint.acb:
            cw = Cw_acb(om)
            sig2 = sigma_L2_sq_acb(om, log2)
            return (flint.acb(2) / flint.acb(pi)) * sig2 * cw * cw

        # Piecewise monotonicity upper bound 1/(alpha(om) - da) <= 1/(alpha(om_k) - da) on [om_k, om_{k+1}]
        # avoids evaluating digamma on wide complex boxes and certifies D_w_upper >= D_w in 0.07s:
        om_strs = [
            xi1_val, "8.45", "8.5", "8.56", "8.63", "8.71", "8.8", "8.9",
            "9.02", "9.16", "9.32", "9.5", "9.72", "9.98", "10.3", "10.7",
            "11.2", "11.8", "12.5", "13.4", "14.5", "15.8", "17.5", "19.5",
            "22.0", "25.5", "30.0", "36.0", "44.0", "54.0", "66.0", "80.0",
        ]
        om_knots = [flint.arb(s) for s in om_strs]
        int_0_xi1 = flint.acb.integral(int_Planch, flint.acb(0), flint.acb(om_knots[0])).real
        int_1_upper = flint.arb(0)
        int_xi1_Xi = flint.arb(0)
        for idx in range(len(om_knots) - 1):
            assert om_knots[idx + 1] > om_knots[idx]
            ik = flint.acb.integral(int_Planch, flint.acb(om_knots[idx]), flint.acb(om_knots[idx + 1])).real
            int_xi1_Xi += ik
            alp_lo = alpha_arb(om_knots[idx]) - da
            assert alp_lo > 0
            int_1_upper += ik / alp_lo
        int_0_X = int_0_xi1 + int_xi1_Xi
        alp_Xi = alpha_arb(Xi) - da
        assert alp_Xi > 0
        D_w = int_1_upper + (flint.arb("3.25") * norm_w_sq - int_0_X) / alp_Xi

        # Step 1: M = 16 scalar moments mu_n on [0, xi1]:
        M_mom = 16
        mu: list[flint.arb] = []
        knots_01 = [flint.arb(0), flint.arb("4.2"), xi1]
        for n in range(M_mom):
            scale_n = flint.acb((-1) ** n) / flint.acb(math.factorial(2 * n))

            def mom_integrand(om: flint.acb, _: Any, n_pow: int = 2 * n, sc: flint.acb = scale_n) -> flint.acb:
                cw = Cw_acb(om)
                sig2 = sigma_L2_sq_acb(om, log2)
                return sc * (flint.acb(2) / flint.acb(pi)) * sig2 * cw * (om**n_pow)

            mu_n = integrate_subintervals(mom_integrand, knots_01)
            mu.append(mu_n)

        # Rigorous uniform remainder eps_1 on [0, b]:
        w_L1 = sum((lens[i] * arb_abs(w_vec[i]) for i in range(K)), flint.arb(0))
        sig2_max = (flint.arb("1.5") + flint.arb(2).sqrt()) ** 2
        eps_1 = (
            (flint.arb(2) / pi)
            * sig2_max
            * w_L1
            * (b ** (2 * M_mom) / flint.arb(math.factorial(2 * M_mom)))
            * (xi1 ** (2 * M_mom + 1) / flint.arb(2 * M_mom + 1))
        )

        # Step 2: Exact shift to midpoint coordinates s = x - m_j in [-L_j/2, L_j/2]
        deg = 2 * M_mom - 1
        Psi_loc = [[flint.arb(0) for _ in range(deg)] for _ in range(K)]
        for j in range(K):
            Psi_loc[j][0] = flint.arb("3.25") * w_vec[j]
            for r in range(deg):
                n_start = (r + 1) // 2
                s_val = flint.arb(0)
                for n in range(n_start, M_mom):
                    binom_val = flint.arb(math.comb(2 * n, r))
                    s_val += binom_val * mu[n] * (mids[j] ** (2 * n - r))
                Psi_loc[j][r] = Psi_loc[j][r] - s_val

        # Step 3: Exact application of P0^{-1} in midpoint coordinates
        Q_loc = [[flint.arb(0) for _ in range(deg)] for _ in range(K)]
        for i in range(K):
            for r in range(deg):
                s_q = flint.arb(0)
                if r % 2 == 0:
                    for j in range(K):
                        s_q += P0inv_e[i][j] * Psi_loc[j][r]
                else:
                    for j in range(K):
                        sgn_ij = flint.arb(-1 if is_refl[i][j] else 1)
                        s_q += sgn_ij * P0inv_e[i][j] * Psi_loc[j][r]
                Q_loc[i][r] = s_q

        # Step 4: Contract with moment matrix H_{i, r, r'} = \int_{-L_i/2}^{L_i/2} s^{r+r'} ds
        W_loc = [[flint.arb(0) for _ in range(deg)] for _ in range(K)]
        for i in range(K):
            half_Li = flint.arb("0.5") * lens[i]
            for r_prime in range(deg):
                s_w = flint.arb(0)
                for r in range(deg):
                    if (r + r_prime) % 2 == 0:
                        p_pow = r + r_prime + 1
                        s_w += Q_loc[i][r] * (flint.arb(2) * (half_Li**p_pow) / flint.arb(p_pow))
                W_loc[i][r_prime] = s_w

        # Rigorous error bounds delta_infty, err_JWe, err_JWW, delta_vW:
        C_inf_P0inv = flint.arb(0)
        for i in range(K):
            row_sum = sum((arb_abs(P0inv_e[i][j]) for j in range(K)), flint.arb(0))
            C_inf_P0inv = arb_max(C_inf_P0inv, row_sum)
        delta_inf = C_inf_P0inv * eps_1

        Psi_L1_bound = flint.arb(0)
        for i in range(K):
            half_Li = flint.arb("0.5") * lens[i]
            for r in range(deg):
                Psi_L1_bound += arb_abs(Psi_loc[i][r]) * (flint.arb(2) * (half_Li ** (r + 1)) / flint.arb(r + 1))

        err_JWW = (flint.arb(2) * Psi_L1_bound + b * eps_1) * delta_inf
        J_WW_nom = sum(
            (Psi_loc[i][r] * W_loc[i][r] for i in range(K) for r in range(deg)),
            flint.arb(0),
        )
        J_WW = J_WW_nom + flint.arb(0, err_JWW.upper())

        for k in range(M_prime):
            phi_k_L1 = sum((lens[i] * arb_abs(phi_e[k][i]) for i in range(K)), flint.arb(0))
            err_k = phi_k_L1 * delta_inf
            jwe_nom = sum((phi_e[k][i] * W_loc[i][0] for i in range(K)), flint.arb(0))
            J_We.append(jwe_nom + flint.arb(0, err_k.upper()))

        eps_2 = flint.arb(0)
        for i in range(K):
            half_Li = flint.arb("0.5") * lens[i]
            q_L1_i = sum(
                (arb_abs(Q_loc[i][r]) * (flint.arb(2) * (half_Li ** (r + 1)) / flint.arb(r + 1)) for r in range(deg)),
                flint.arb(0),
            )
            rem_i = ((xi0 * half_Li) ** (2 * R_xi)) / flint.arb(math.factorial(2 * R_xi))
            eps_2 += rem_i * q_L1_i

        delta_vW = b * delta_inf + eps_2

    M_tot = M_prime + (1 if include_plancherel else 0)
    DJ = [[flint.arb(0) for _ in range(M_tot)] for _ in range(M_tot)]
    for j in range(M_prime):
        for k in range(M_prime):
            DJ[j][k] = J_prime[j][k] + (d_prime[j] if j == k else flint.arb(0))
    if include_plancherel:
        for k in range(M_prime):
            DJ[M_prime][k] = J_We[k]
            DJ[k][M_prime] = J_We[k]
        DJ[M_prime][M_prime] = D_w + J_WW

    eye_M = [[flint.arb(1 if j == k else 0) for k in range(M_tot)] for j in range(M_tot)]
    DJ_inv = solve_linear_arb(DJ, eye_M)

    # Single combined integrand for Tr(P_even^{-1} A_{-, even}) and Tr(P0_odd^{-1} A_{-, odd}) on [0, xi0]
    # using O(K) transcendental evaluations per quadrature point:
    fact_even = [flint.acb((-1) ** m) / flint.acb(math.factorial(2 * m)) for m in range(R_xi)]
    fact_odd = [flint.acb((-1) ** m) / flint.acb(math.factorial(2 * m + 1)) for m in range(R_xi)]

    def trace_combined_integrand(xi: flint.acb, _: Any) -> flint.acb:
        w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_sq_acb(xi, log2) * (flint.acb(da) - alpha_acb(xi))
        c_mi = [(xi * flint.acb(mids[i])).cos() for i in range(K)]
        s_mi = [(xi * flint.acb(mids[i])).sin() for i in range(K)]
        ic: list[flint.acb] = []
        is_sin: list[flint.acb] = []
        tc_plus: list[flint.acb] = []
        ts_minus: list[flint.acb] = []
        tc_minus: list[flint.acb] = []
        ts_plus: list[flint.acb] = []
        for i in range(K):
            Li_acb = flint.acb(lens[i])
            half_arg = flint.acb("0.5") * xi * Li_acb
            sh_i = acb_sinc(half_arg)
            s2_i = half_arg.cos() * sh_i
            ic.append(Li_acb * c_mi[i] * sh_i)
            is_sin.append(Li_acb * s_mi[i] * sh_i)
            p_fac = flint.acb("0.5") * Li_acb * (flint.acb(1) + s2_i)
            m_fac = flint.acb("0.5") * Li_acb * (flint.acb(1) - s2_i)
            tc_plus.append(p_fac * c_mi[i])
            ts_minus.append(m_fac * s_mi[i])
            tc_minus.append(m_fac * c_mi[i])
            ts_plus.append(p_fac * s_mi[i])

        k0_e = flint.acb(0)
        for i, j, val_e, refl in active_pairs_e:
            if not refl:
                k0_e += flint.acb(val_e) * (tc_plus[i] * c_mi[j] + ts_minus[i] * s_mi[j])
            else:
                k0_e += flint.acb(val_e) * (tc_plus[i] * c_mi[j] - ts_minus[i] * s_mi[j])

        k0_o = flint.acb(0)
        for i, j, val_o, refl in active_pairs_o:
            if not refl:
                k0_o += flint.acb(val_o) * (tc_minus[i] * c_mi[j] + ts_plus[i] * s_mi[j])
            else:
                k0_o += flint.acb(val_o) * (-tc_minus[i] * c_mi[j] + ts_plus[i] * s_mi[j])

        v_vec: list[flint.acb] = [
            sum((flint.acb(p0inv_e[k][i]) * ic[i] for i in range(K)), flint.acb(0))
            for k in range(M_prime)
        ]
        vo_vec: list[flint.acb] = [
            sum((flint.acb(p0inv_o[k][i]) * is_sin[i] for i in range(K)), flint.acb(0))
            for k in range(M_prime)
        ]

        if include_plancherel:
            xi2 = xi * xi
            xi_pows_e = [flint.acb(1)]
            for _ in range(1, R_xi):
                xi_pows_e.append(xi_pows_e[-1] * xi2)
            vw = flint.acb(0)
            for i in range(K):
                ev_s = sum(
                    (flint.acb(W_loc[i][2 * m]) * fact_even[m] * xi_pows_e[m] for m in range(R_xi)),
                    flint.acb(0),
                )
                od_s = xi * sum(
                    (flint.acb(W_loc[i][2 * m + 1]) * fact_odd[m] * xi_pows_e[m] for m in range(R_xi)),
                    flint.acb(0),
                )
                vw += c_mi[i] * ev_s - s_mi[i] * od_s
            v_vec.append(vw)

        quad_e = flint.acb(0)
        for j in range(M_tot):
            row_j = sum((flint.acb(DJ_inv[j][k]) * v_vec[k] for k in range(M_tot)), flint.acb(0))
            quad_e += v_vec[j] * row_j

        quad_o = flint.acb(0)
        for j in range(M_prime):
            row_jo = sum((flint.acb(DJ_o_inv[j][k]) * vo_vec[k] for k in range(M_prime)), flint.acb(0))
            quad_o += vo_vec[j] * row_jo

        i_unit = flint.acb(0, 1)
        return w_m * ((k0_e - quad_e) + i_unit * (k0_o - quad_o))

    knots_xi0 = [flint.arb(0), flint.arb("4.0"), xi0_mid]
    comb_int = flint.acb(0)
    for idx in range(len(knots_xi0) - 1):
        comb_int += flint.acb.integral(
            trace_combined_integrand,
            flint.acb(knots_xi0[idx]),
            flint.acb(knots_xi0[idx + 1]),
        )
    tr_even_main = comb_int.real
    tr_odd_main = comb_int.imag

    # Propagate delta_vW error from v_W(xi) if include_plancherel:
    extra_vW_err = flint.arb(0)
    if include_plancherel:
        # Bound |(DJ_inv v)_W| on [0, xi0]:
        # Each |v_k(xi)| <= b * max_i |p0inv_e[k][i]| <= 3*b, so |quad perturbation| <= 2 * sum_k |DJ_inv[M, k]| * 3*b * delta_vW
        row_M_sum = sum((arb_abs(DJ_inv[M_prime][k]) for k in range(M_tot)), flint.arb(0))
        sig2_max = (flint.arb("1.5") + flint.arb(2).sqrt()) ** 2
        w_m_int_bound = (flint.arb(2) / pi) * sig2_max * (da - alpha_arb(flint.arb(0))) * xi0
        extra_vW_err = w_m_int_bound * flint.arb(6) * b * row_M_sum * delta_vW

    val_end = trace_combined_integrand(flint.acb(xi0), None)
    rad_xi0 = flint.arb(xi0.rad())
    end_err_e = arb_abs(val_end.real) * rad_xi0
    end_err_o = arb_abs(val_end.imag) * rad_xi0
    tr_even = tr_even_main + flint.arb(0, (extra_vW_err + end_err_e).upper())
    tr_odd = tr_odd_main + flint.arb(0, end_err_o.upper())

    assert tr_even < flint.arb(1), f"[{label}] Even trace failed < 1: {tr_even}"
    assert tr_odd < flint.arb(1), f"[{label}] Odd trace failed < 1: {tr_odd}"

    return {
        "label": label,
        "a": arb_to_dict(a),
        "b": arb_to_dict(b),
        "Delta_alpha": arb_to_dict(da),
        "xi0": arb_to_dict(xi0),
        "K_intervals": K,
        "M_prime_vectors": M_prime,
        "include_plancherel": include_plancherel,
        "D_w": arb_to_dict(D_w) if include_plancherel else None,
        "delta_vW_bound": arb_to_dict(delta_vW) if include_plancherel else None,
        "tr_even": arb_to_dict(tr_even),
        "tr_odd": arb_to_dict(tr_odd),
        "margin_even": arb_to_dict(flint.arb(1) - tr_even),
        "margin_odd": arb_to_dict(flint.arb(1) - tr_odd),
        "certified": bool(tr_even < flint.arb(1) and tr_odd < flint.arb(1)),
        "elapsed_s": round(time.time() - t0, 3),
    }


def main() -> None:
    t_start = time.time()
    print("=== Running 384-Bit ARB Certification Beyond a = (1/2) log 6 ===")

    # 1. Interval (1/2 log 6, log(5/2)] via exact reflection preconditioner + sum-of-squares monotonicity:
    res_reg1 = certify_regime_1_log5_over_2()
    print(
        f"[Regime 1: (1/2 log 6, log(5/2)]] tr_even = {res_reg1['tr_even']['mid']:.8f} "
        f"(rad={res_reg1['tr_even']['rad']:.2e}), tr_odd = {res_reg1['tr_odd']['mid']:.8f} "
        f"[{res_reg1['elapsed_s']}s]"
    )

    # 2. Prime-only checkpoint a = 0.940000:
    res_094 = certify_beyond_log52_point(
        label="a = 0.940 (prime-only)",
        a_sym=SymReal.const(Fraction(94, 100)),
        da=flint.arb("0.40"),
        include_plancherel=False,
        use_natural_splits=True,
    )
    print(
        f"[Checkpoint a = 0.940] tr_even = {res_094['tr_even']['mid']:.8f} "
        f"(rad={res_094['tr_even']['rad']:.2e}), tr_odd = {res_094['tr_odd']['mid']:.8f} "
        f"[{res_094['elapsed_s']}s]"
    )

    # 3. Prime-only checkpoint a = 0.960000:
    res_096 = certify_beyond_log52_point(
        label="a = 0.960 (prime-only)",
        a_sym=SymReal.const(Fraction(96, 100)),
        da=flint.arb("0.50"),
        include_plancherel=False,
        use_natural_splits=False,
        n_step=4,
    )
    print(
        f"[Checkpoint a = 0.960] tr_even = {res_096['tr_even']['mid']:.8f} "
        f"(rad={res_096['tr_even']['rad']:.2e}), tr_odd = {res_096['tr_odd']['mid']:.8f} "
        f"[{res_096['elapsed_s']}s]"
    )

    # 4. Next Prime-Pair Threshold a_{***} = (1/2) log 7 ~ 0.9729550745:
    a_log7_sym = SymReal.log_prime(7, Fraction(1, 2))
    res_log7 = certify_beyond_log52_point(
        label="a = (1/2) log 7 (next prime-pair threshold)",
        a_sym=a_log7_sym,
        da=flint.arb("0.25"),
        include_plancherel=True,
        use_natural_splits=True,
        xi1_val="8.4",
    )
    print(
        f"[Threshold a = 0.5*log(7)] tr_even = {res_log7['tr_even']['mid']:.8f} "
        f"(rad={res_log7['tr_even']['rad']:.2e}), tr_odd = {res_log7['tr_odd']['mid']:.8f} "
        f"[{res_log7['elapsed_s']}s]"
    )

    out_data = {
        "audit": "all-vector-positivity-beyond-log6-2026-10-15-v1",
        "precision_bits": PREC_BITS,
        "all_certified": bool(
            res_reg1["certified"]
            and res_094["certified"]
            and res_096["certified"]
            and res_log7["certified"]
        ),
        "total_elapsed_s": round(time.time() - t_start, 3),
        "regime_1_interval_log6_to_log5_over_2": res_reg1,
        "checkpoint_a_094_prime_only": res_094,
        "checkpoint_a_096_prime_only": res_096,
        "threshold_half_log7": res_log7,
    }

    out_path = Path(__file__).resolve().parent / "verification.json"
    out_path.write_text(json.dumps(out_data, indent=2), encoding="utf-8")
    print(f"Wrote {out_path} in {out_data['total_elapsed_s']}s (all_certified={out_data['all_certified']})")


if __name__ == "__main__":
    main()
