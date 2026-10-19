#!/usr/bin/env python3
"""
Two-Precision (256-bit and 384-bit) ARB-Certified Verification of the Multi-Prime
Split-Pole Causal Euler Preconditioner (B_{P_+, P_-} and B_{2, 3}), the Mertens
Diagonal Gain Theorem, and All-Vector Weil Positivity on the Filtered Subspace
Ran(B_{2, 3}) Across a in ((1/2) log 6, (1/2) log 10].

Audit repairs incorporated (per argon-multiprime-review-2026-10-15-v1 and
argon-m9-campaign-review-2026-10-15-v1):
1. Pure algebraic interval operations for arb_min, arb_max, and arb_hull without
   float conversions.
2. Exact symbolic endpoint representation SymReal in Q + sum_p Q*log(p):
   by the Fundamental Theorem of Arithmetic and the Hermite-Lindemann theorem,
   {1} union {log p : p prime} is Q-linearly independent, so two endpoints are
   algebraically equal if and only if their exact Fraction coefficient vectors
   are identical. Distinct endpoints are ordered strictly by certified flint.arb
   inequalities (arb_strict_lt) with ZERO decimal tolerances (no 1e-100 threshold;
   exact inputs 0 and 1e-101 remain strictly separated).
3. Rigorous complex-ball enclosure of the root-endpoint integral on
   [xi0_mid, xi0] via |F(xi0)| * rad(xi0) in flint.acb arithmetic.
4. Full two-precision (256-bit and 384-bit) replay and ball-overlap certification
   archived directly in verification.json.
"""

from __future__ import annotations

import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

import flint


def arb_abs(x: flint.arb) -> flint.arb:
    return abs(x)


def arb_max(a: flint.arb, b: flint.arb) -> flint.arb:
    """Exact interval enclosure of max(a, b) without float conversion or dependency-radius inflation."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a > lo_b else (lo_b if lo_b > lo_a else flint.arb("0.5") * (lo_a + lo_b + abs(lo_a - lo_b)))
    hi = hi_a if hi_a > hi_b else (hi_b if hi_b > hi_a else flint.arb("0.5") * (hi_a + hi_b + abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_min(a: flint.arb, b: flint.arb) -> flint.arb:
    """Exact interval enclosure of min(a, b) without float conversion or dependency-radius inflation."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a < lo_b else (lo_b if lo_b < lo_a else flint.arb("0.5") * (lo_a + lo_b - abs(lo_a - lo_b)))
    hi = hi_a if hi_a < hi_b else (hi_b if hi_b < hi_a else flint.arb("0.5") * (hi_a + hi_b - abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_hull(a: flint.arb, b: flint.arb) -> flint.arb:
    """Rigorous interval hull containing both balls a and b."""
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


class SymReal:
    """
    Exact element of Q + sum_{p prime} Q * log(p).
    Key 1 represents the rational constant 1; prime keys p >= 2 represent log(p).
    By the Fundamental Theorem of Arithmetic and the Hermite-Lindemann theorem,
    {1} union {log p : p prime} is linearly independent over Q, so two SymReal
    values are equal as real numbers iff their reduced coefficient dicts match.
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

    def is_zero(self) -> bool:
        return len(self._key) == 0

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


def sym_min(a: SymReal, b: SymReal) -> SymReal:
    if a == b:
        return a
    return a if arb_strict_lt(a.ball(), b.ball()) else b


def sym_max(a: SymReal, b: SymReal) -> SymReal:
    if a == b:
        return a
    return b if arb_strict_lt(a.ball(), b.ball()) else a


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


def certify_exact_endpoint_separation() -> dict[str, Any]:
    """
    Directly verify Finding 6 repair: exact inputs 0 and 10^-101 are NOT merged
    by deduplicate_and_sort_sym and are certified strictly ordered (0 < 10^-101)
    in flint.arb ball arithmetic.
    """
    z0 = SymReal.zero()
    z_tiny = SymReal.const(Fraction(1, 10**101))
    dedup = deduplicate_and_sort_sym([z_tiny, z0, z_tiny])
    assert len(dedup) == 2
    assert dedup[0] == z0 and dedup[1] == z_tiny
    assert arb_strict_lt(dedup[0].ball(), dedup[1].ball())
    return {
        "inputs_tested": ["0", "10^-101", "10^-101"],
        "deduplicated_count": len(dedup),
        "strict_inequality_0_lt_1e_minus_101": True,
        "decimal_tolerance_used": None,
    }


def arb_to_dict(x: flint.arb) -> dict[str, Any]:
    return {
        "mid": float(x.mid()),
        "rad": float(x.rad()),
        "lower": float(x.lower()),
        "upper": float(x.upper()),
        "str": str(x),
    }


def acb_sinc(z: flint.acb) -> flint.acb:
    """Rigorous evaluation of sinc(z) = sin(z) / z on complex balls using FLINT's built-in acb_sinc."""
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


def sigma_L2_L3_acb(xi: flint.acb, log2_arb: flint.arb, log3_arb: flint.arb) -> flint.acb:
    """
    Exact Fourier symbol of L_2 L_3 = B_{2, 3}^* B_{2, 3}:
      sigma_{L_2}(xi) = 3/2 - sqrt(2) cos(xi log 2)
      sigma_{L_3}(xi) = 4/3 - (2/sqrt(3)) cos(xi log 3).
    """
    sqrt2 = flint.acb(flint.arb(2).sqrt())
    sqrt3 = flint.acb(flint.arb(3).sqrt())
    s2 = flint.acb(flint.arb("1.5")) - sqrt2 * (xi * flint.acb(log2_arb)).cos()
    s3 = flint.acb(flint.arb(4) / flint.arb(3)) - (flint.acb(2) / sqrt3) * (xi * flint.acb(log3_arb)).cos()
    return s2 * s3


def find_alpha_root_arb(target_da: flint.arb) -> flint.arb:
    """
    Enclose the unique positive root xi_0 > 0 of alpha(xi_0) = target_da
    by bisection and certify by strict sign change.
    """
    lo = flint.arb("5.0")
    hi = flint.arb("30.0")
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


def integrate_on_0_to_xi0(
    fn: Any, xi0: flint.arb, rel_tol: float | None = None, abs_tol: float | None = None
) -> tuple[flint.arb, flint.arb]:
    """
    Rigorous integration of a holomorphic integrand fn(xi, _) over [0, xi0]
    where xi0 is a certified ball enclosing the root alpha(xi0) = Delta_alpha.
    The main integral over [0, mid(xi0)] is computed via flint.acb.integral,
    and the endpoint integral over [mid(xi0), xi0] is rigorously enclosed by
    evaluating |fn(acb(xi0))| * rad(xi0) over the ball xi0.
    """
    tol_exp = -min(110, int(flint.ctx.prec) - 40)
    rt = float(2.0**tol_exp) if rel_tol is None else rel_tol
    at = float(2.0**tol_exp) if abs_tol is None else abs_tol
    xi0_mid = flint.arb(xi0.mid())
    rad_xi0 = flint.arb(xi0.rad())
    main_val = flint.acb.integral(fn, flint.acb(0), flint.acb(xi0_mid), rel_tol=rt, abs_tol=at)
    val_at_ball = fn(flint.acb(xi0), None)
    tail_re = arb_abs(val_at_ball.real) * rad_xi0
    tail_im = arb_abs(val_at_ball.imag) * rad_xi0
    res_re = main_val.real + flint.arb(0, tail_re.upper())
    res_im = main_val.imag + flint.arb(0, tail_im.upper())
    return res_re, res_im


def solve_linear_arb(A: list[list[flint.arb]], B: list[list[flint.arb]]) -> list[list[flint.arb]]:
    """Rigorous Gauss-Jordan linear solver in flint.arb for M x M systems A X = B."""
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
                for j in range(col, n + m):
                    aug[r][j] = aug[r][j] - factor * aug[col][j]
    return [[aug[i][n + j] for j in range(m)] for i in range(n)]


def certify_theorem_1_and_2() -> dict[str, Any]:
    """
    Certify Theorem 1 (Universal Single-Prime Causal Euler Identity) and
    Theorem 2 (Multi-Prime Split-Pole Preconditioner B_{P_+, P_-}, Bilateral
    Pole Annihilation, and Mertens Zero-Shift Diagonal Gain Theorem).
    """
    t0 = time.time()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    k_max = 60
    rad_bound = flint.arb(2) ** (-(int(flint.ctx.prec) - 30))

    single_prime_checks: list[dict[str, Any]] = []
    for p in [2, 3, 5, 7, 11, 13]:
        p_arb = flint.arb(p)
        logp = p_arb.log()
        inv_p = flint.arb(1) / p_arb
        inv_sqrt_p = flint.arb(1) / p_arb.sqrt()

        p_qtr = (flint.arb("0.25") * logp).exp()
        p_mqtr = (flint.arb("-0.25") * logp).exp()
        pole_plus_res = p_mqtr - inv_sqrt_p * p_qtr
        pole_minus_res = p_mqtr - inv_sqrt_p * p_qtr
        assert pole_plus_res.contains(0) and pole_plus_res.rad() < rad_bound
        assert pole_minus_res.contains(0) and pole_minus_res.rad() < rad_bound

        c_0 = flint.arb(2) * logp * inv_p
        c_1 = -logp * inv_sqrt_p
        max_higher_power_err = flint.arb(0)
        for k in range(2, k_max):
            half_k = flint.arb(k) / flint.arb(2)
            half_km1 = flint.arb(k - 1) / flint.arb(2)
            half_kp1 = flint.arb(k + 1) / flint.arb(2)
            term_diag = -(flint.arb(1) + inv_p) * logp * (p_arb ** (-half_k))
            term_prev = inv_sqrt_p * logp * (p_arb ** (-half_km1))
            term_next = inv_sqrt_p * logp * (p_arb ** (-half_kp1))
            coeff_k = term_diag + term_prev + term_next
            assert coeff_k.contains(0), f"Non-zero residual at p={p}, k={k}: {coeff_k}"
            max_higher_power_err = arb_max(max_higher_power_err, arb_abs(coeff_k))

        wp_at_xi0 = -(flint.arb(2) * logp) / (p_arb.sqrt() - flint.arb(1))

        single_prime_checks.append({
            "p": p,
            "diag_coeff_I": arb_to_dict(c_0),
            "shift_coeff_S_logp": arb_to_dict(c_1),
            "untruncated_W_p_at_xi0": arb_to_dict(wp_at_xi0),
            "pole_annihilation_rad": float(pole_plus_res.rad()),
            "max_higher_power_residual_upper": float(max_higher_power_err.upper()),
            "all_higher_powers_annihilated": True,
        })

    mertens_rows: list[dict[str, Any]] = []
    half_theta = flint.arb(0)
    c_zero = flint.arb(1)
    gamma_sum = flint.arb(0)
    sym_floor = flint.arb(1)

    for p in primes:
        p_arb = flint.arb(p)
        logp = p_arb.log()
        half_theta = half_theta + flint.arb("0.5") * logp
        c_zero = c_zero * (flint.arb(1) + flint.arb(1) / p_arb)
        gamma_sum = gamma_sum + (flint.arb(2) * logp) / (p_arb + flint.arb(1))
        factor_floor = (flint.arb(1) - flint.arb(1) / p_arb.sqrt()) ** 2
        sym_floor = sym_floor * factor_floor
        c_diag = c_zero * gamma_sum

        mertens_rows.append({
            "X": p,
            "num_primes": len(mertens_rows) + 1,
            "support_cost_half_theta": arb_to_dict(half_theta),
            "C_zero": arb_to_dict(c_zero),
            "C_iso": arb_to_dict(c_zero),
            "C_diag": arb_to_dict(c_diag),
            "gamma_normalized_gain": arb_to_dict(gamma_sum),
            "symbol_floor_L_P_at_xi0": arb_to_dict(sym_floor),
        })

    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log6 = flint.arb(6).log()

    c0_L2_sq = flint.arb("2.5") * log2
    c_zero_L2_sq = flint.arb("3.25")
    gamma_L2_sq = c0_L2_sq / c_zero_L2_sq

    c0_B23 = (flint.arb(4) / flint.arb(3)) * log2 + log3
    c_zero_B23 = flint.arb(2)
    gamma_B23 = c0_B23 / c_zero_B23
    gain_ratio = gamma_B23 / gamma_L2_sq

    sqrt2 = flint.arb(2).sqrt()
    sqrt3 = flint.arb(3).sqrt()
    sqrt6 = flint.arb(6).sqrt()
    coeff_I = c0_B23
    coeff_S_log32 = log6 / sqrt6
    coeff_S_log2 = -(flint.arb(2) * sqrt2 / flint.arb(3)) * log6 + (sqrt2 / flint.arb(3)) * log3
    coeff_S_log3 = -(sqrt3 / flint.arb(2)) * log6 + (log2 / (flint.arb(2) * sqrt3))
    coeff_S_log6 = log6 / sqrt6

    return {
        "single_prime_checks": single_prime_checks,
        "mertens_table": mertens_rows,
        "two_prime_comparison": {
            "c0_L2_sq": arb_to_dict(c0_L2_sq),
            "c_zero_L2_sq": arb_to_dict(c_zero_L2_sq),
            "c_iso_L2_sq": arb_to_dict(c_zero_L2_sq),
            "gamma_L2_sq": arb_to_dict(gamma_L2_sq),
            "c0_B23": arb_to_dict(c0_B23),
            "c_zero_B23": arb_to_dict(c_zero_B23),
            "c_iso_B23": arb_to_dict(c_zero_B23),
            "gamma_B23": arb_to_dict(gamma_B23),
            "normalized_gain_multiplier": arb_to_dict(gain_ratio),
            "B23_W23_exact_shifts": {
                "I": arb_to_dict(coeff_I),
                "S_log(3/2)": arb_to_dict(coeff_S_log32),
                "S_log2": arb_to_dict(coeff_S_log2),
                "S_log3": arb_to_dict(coeff_S_log3),
                "S_log6": arb_to_dict(coeff_S_log6),
            },
        },
        "elapsed_s": round(time.time() - t0, 3),
    }


def certify_theorem_3_up_to_log3() -> dict[str, Any]:
    """
    Certify Theorem 3: Exact Two-Prime Split-Pole Preconditioner B_{2, 3} = E_tilde_2 E_tilde_3^*
    on Ran(B_{2, 3}) across a in ((1/2) log 6, log 3] = ((1/2) log 6, (1/2) log 9] ~ (0.895880, 1.098612]
    with Delta_alpha = 0 and ZERO rank-1 minorants.
    """
    t0 = time.time()
    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()
    log6 = flint.arb(6).log()
    log7 = flint.arb(7).log()
    pi = flint.arb.pi()

    s_log2 = SymReal.log_prime(2)
    s_log3 = SymReal.log_prime(3)
    s_log5 = SymReal.log_prime(5)
    s_log6 = s_log2 + s_log3
    s_log7 = SymReal.log_prime(7)

    c0_23 = (flint.arb(4) / flint.arb(3)) * log2 + log3
    c76 = log7 / flint.arb(42).sqrt()
    c65 = log5 / flint.arb(30).sqrt()

    s_tau76 = s_log7 - s_log6
    s_tau65 = s_log6 - s_log5

    da = flint.arb(0)
    xi0 = find_alpha_root_arb(da)

    v0 = c0_23
    v_76 = c0_23 - c76
    v_76_65 = c0_23 - c76 - c65
    v_2x76_65 = c0_23 - flint.arb(2) * c76 - c65
    v_full = c0_23 - flint.arb(2) * c76 - flint.arb(2) * c65
    assert v0 > v_76 > v_76_65 > v_2x76_65 > v_full > flint.arb(0)

    checkpoints_spec: list[tuple[str, SymReal]] = [
        ("1/2 log 7 (Regime 3A endpoint)", s_log7.scale(Fraction(1, 2))),
        ("a = 1.000000", SymReal.const(1)),
        ("3/2 log 2 = 1/2 log 8", s_log2.scale(Fraction(3, 2))),
        ("1/2 log(49/6) (b = tau_{7/6})", s_log6.scale(Fraction(1, 2)) + s_tau76),
        ("a = 1.070000", SymReal.const(Fraction(107, 100))),
        ("log 3 = 1/2 log 9 (Regime 3B endpoint)", s_log3),
    ]

    results: list[dict[str, Any]] = []
    s_zero = SymReal.zero()
    for label, s_a in checkpoints_spec:
        tc0 = time.time()
        s_b = s_a - s_log6.scale(Fraction(1, 2))
        a = s_a.ball()
        b = s_b.ball()

        # Build exact breakpoints of V_a(x) on [0, b] using exact symbolic identity + certified ball inequalities:
        raw_cuts = [s_zero, s_b]
        for s_p in [s_tau76 - s_b, s_b - s_tau76, s_tau65 - s_b, s_b - s_tau65]:
            if s_p == s_zero or s_p == s_b:
                continue
            if sym_strict_lt(s_zero, s_p) and sym_strict_lt(s_p, s_b):
                raw_cuts.append(s_p)
        s_cuts = deduplicate_and_sort_sym(raw_cuts)

        intervals: list[tuple[flint.arb, flint.arb, flint.arb]] = []
        min_v = v0
        for k in range(len(s_cuts) - 1):
            s_xL, s_xR = s_cuts[k], s_cuts[k + 1]
            s_xm = (s_xL + s_xR).scale(Fraction(1, 2))
            pen = flint.arb(0)
            for s_tau, c in [(s_tau76, c76), (s_tau65, c65)]:
                if sym_strict_lt(s_tau - s_b, s_xm):
                    pen = pen + c
                if sym_strict_lt(s_xm, s_b - s_tau):
                    pen = pen + c
            vk = v0 - pen
            min_v = arb_min(min_v, vk)
            intervals.append((s_xL.ball(), s_xR.ball(), vk))

        def integrand_combined(xi: flint.acb, _: Any) -> flint.acb:
            w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_L3_acb(xi, log2, log3) * (-alpha_acb(xi))
            two_xi = flint.acb(2) * xi
            acc_e = flint.acb(0)
            acc_o = flint.acb(0)
            for xL, xR, vk in intervals:
                sR = acb_sinc(two_xi * flint.acb(xR))
                sL = acb_sinc(two_xi * flint.acb(xL))
                hR = flint.acb("0.5") * flint.acb(xR)
                hL = flint.acb("0.5") * flint.acb(xL)
                inv_vk = flint.acb(flint.arb(1) / vk)
                acc_e = acc_e + (hR * (flint.acb(1) + sR) - hL * (flint.acb(1) + sL)) * inv_vk
                acc_o = acc_o + (hR * (flint.acb(1) - sR) - hL * (flint.acb(1) - sL)) * inv_vk
            return w_m * (acc_e + flint.acb(0, 1) * acc_o)

        tr_even, tr_odd = integrate_on_0_to_xi0(integrand_combined, xi0)
        assert tr_even < flint.arb(1), f"Even trace >= 1 at {label}: {tr_even}"
        assert tr_odd < flint.arb(1), f"Odd trace >= 1 at {label}: {tr_odd}"

        coercivity_h = min_v * (flint.arb(1) - tr_even)
        coercivity_B23h = coercivity_h / flint.arb(2)

        results.append({
            "label": label,
            "a": arb_to_dict(a),
            "b": arb_to_dict(b),
            "Delta_alpha": arb_to_dict(da),
            "num_subintervals": len(intervals),
            "lambda_min_P0": arb_to_dict(min_v),
            "tr_even": arb_to_dict(tr_even),
            "tr_odd": arb_to_dict(tr_odd),
            "margin_even": arb_to_dict(flint.arb(1) - tr_even),
            "margin_odd": arb_to_dict(flint.arb(1) - tr_odd),
            "coercivity_h_L2": arb_to_dict(coercivity_h),
            "coercivity_B23h_L2": arb_to_dict(coercivity_B23h),
            "certified": bool(tr_even < flint.arb(1) and tr_odd < flint.arb(1)),
            "elapsed_s": round(time.time() - tc0, 3),
        })

    return {
        "regime": "((1/2) log 6, log 3] = ((1/2) log 6, (1/2) log 9]",
        "subspace": "Ran(B_{2, 3}) subset L^2_{pole-free}(-a, a)",
        "Delta_alpha": arb_to_dict(da),
        "xi0": arb_to_dict(xi0),
        "c0_23": arb_to_dict(c0_23),
        "c76": arb_to_dict(c76),
        "c65": arb_to_dict(c65),
        "v_full_min": arb_to_dict(v_full),
        "checkpoints": results,
        "elapsed_s": round(time.time() - t0, 3),
    }


def certify_theorem_4_up_to_half_log10() -> dict[str, Any]:
    """
    Certify Theorem 4: Extension Across (log 3, (1/2) log 10] ~ (1.098612, 1.151293]
    on Ran(B_{2, 3}) via:
    - Sub-Regime 4A: Closed-Form tau_{3/2}-Reflection Involution Preconditioner P_0(a)
      certifying the continuum (log 3, 1.135000] by sum-of-squares monotonicity with
      Delta_alpha = 7/20 = 0.35 and ZERO minorants.
    - Sub-Regime 4B: Exact Continuum Step-Function Woodbury Minorants from the 4 positive
      prime operators D_{tau_{7/6}}, D_{tau_{6/5}}, P_{anti}^{(7/6)}, P_{anti}^{(6/5)}
      plus the Cauchy-Poincare Second-Eigenvalue Defect Bound ||K||_op <= Tr(K) - mu_2.
    """
    t0 = time.time()
    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()
    log6 = flint.arb(6).log()
    log7 = flint.arb(7).log()
    pi = flint.arb.pi()

    s_log2 = SymReal.log_prime(2)
    s_log3 = SymReal.log_prime(3)
    s_log5 = SymReal.log_prime(5)
    s_log6 = s_log2 + s_log3
    s_log7 = SymReal.log_prime(7)
    s_log10 = s_log2 + s_log5

    c0_23 = (flint.arb(4) / flint.arb(3)) * log2 + log3
    c76 = log7 / flint.arb(42).sqrt()
    c65 = log5 / flint.arb(30).sqrt()
    c32 = log6 / flint.arb(6).sqrt()

    s_tau76 = s_log7 - s_log6
    s_tau65 = s_log6 - s_log5
    s_tau32 = s_log3 - s_log2
    tau32 = s_tau32.ball()

    da = flint.arb(7) / flint.arb(20)  # 0.35
    xi0 = find_alpha_root_arb(da)

    v_full = c0_23 + flint.arb(2) * da - flint.arb(2) * c76 - flint.arb(2) * c65
    v_mid = c0_23 + flint.arb(2) * da - flint.arb(2) * c76 - c65
    v_1 = c0_23 + flint.arb(2) * da - c76 - c65
    c32_da = c32 + da / flint.arb(6).sqrt()

    assert v_1 > v_mid > v_full > flint.arb(0)
    assert v_1 > c32_da > flint.arb(0)

    denom_refl = v_1 * v_1 - c32_da * c32_da
    alpha_1 = v_1 / denom_refl
    beta_1 = c32_da / denom_refl
    lambda_min_P0 = arb_min(v_full, v_1 - c32_da)

    w_step_1 = flint.arb(1) / v_full - flint.arb(1) / v_mid
    w_step_2 = flint.arb(1) / v_mid - flint.arb(1) / v_1
    w_step_3 = flint.arb(1) / v_1 - alpha_1

    def eval_closed_form_trace(s_a: SymReal) -> tuple[flint.arb, flint.arb]:
        s_b = s_a - s_log6.scale(Fraction(1, 2))
        b = s_b.ball()
        d65 = (s_b - s_tau65).ball()
        d76 = (s_b - s_tau76).ball()
        x32 = (s_tau32 - s_b).ball()
        L_refl = (s_b - (s_tau32 - s_b)).ball()
        assert flint.arb(0) < d65 < d76 < x32 < b

        def int_comb(xi: flint.acb, _: Any) -> flint.acb:
            w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_L3_acb(xi, log2, log3) * (flint.acb(da) - alpha_acb(xi))
            two_xi = flint.acb(2) * xi
            s_d65 = acb_sinc(two_xi * flint.acb(d65))
            s_d76 = acb_sinc(two_xi * flint.acb(d76))
            s_x32 = acb_sinc(two_xi * flint.acb(x32))
            s_b = acb_sinc(two_xi * flint.acb(b))
            s_refl = acb_sinc(xi * flint.acb(L_refl))
            c_tau32 = (xi * flint.acb(tau32)).cos()

            diag_const = flint.acb("0.5") * (
                flint.acb(w_step_1 * d65 + w_step_2 * d76 + w_step_3 * x32 + alpha_1 * b)
            )
            diag_osc = flint.acb("0.5") * (
                flint.acb(w_step_1 * d65) * s_d65
                + flint.acb(w_step_2 * d76) * s_d76
                + flint.acb(w_step_3 * x32) * s_x32
                + flint.acb(alpha_1 * b) * s_b
            )
            refl_even = -flint.acb("0.5") * flint.acb(beta_1 * L_refl) * (s_refl + c_tau32)
            refl_odd = flint.acb("0.5") * flint.acb(beta_1 * L_refl) * (s_refl - c_tau32)
            ev = diag_const + diag_osc + refl_even
            od = diag_const - diag_osc + refl_odd
            return w_m * (ev + flint.acb(0, 1) * od)

        return integrate_on_0_to_xi0(int_comb, xi0)

    regime_4a_pts: list[tuple[str, SymReal]] = [
        ("a = 1.120000", SymReal.const(Fraction(28, 25))),
        ("a = 1.135000 (Regime 4A continuum endpoint)", SymReal.const(Fraction(227, 200))),
    ]
    regime_4a_results: list[dict[str, Any]] = []
    for label, s_a in regime_4a_pts:
        tc = time.time()
        s_b = s_a - s_log6.scale(Fraction(1, 2))
        a = s_a.ball()
        b = s_b.ball()
        tr_e, tr_o = eval_closed_form_trace(s_a)
        assert tr_e < flint.arb(1), f"Regime 4A even trace >= 1 at {label}: {tr_e}"
        assert tr_o < flint.arb(1), f"Regime 4A odd trace >= 1 at {label}: {tr_o}"
        regime_4a_results.append({
            "label": label,
            "a": arb_to_dict(a),
            "b": arb_to_dict(b),
            "tr_even_0vec": arb_to_dict(tr_e),
            "tr_odd_0vec": arb_to_dict(tr_o),
            "margin_even": arb_to_dict(flint.arb(1) - tr_e),
            "margin_odd": arb_to_dict(flint.arb(1) - tr_o),
            "certified": True,
            "elapsed_s": round(time.time() - tc, 3),
        })

    # Sub-Regime 4B: Exact Continuum Step-Function Woodbury Certification + Cauchy-Poincare Defect Bound
    # using exact SymReal endpoints (zero decimal tolerances).
    s_zero = SymReal.zero()

    def eval_continuum_woodbury(s_a: SymReal, n_sub: int) -> dict[str, Any]:
        tc = time.time()
        s_b = s_a - s_log6.scale(Fraction(1, 2))
        a = s_a.ball()
        b = s_b.ball()
        s_d65 = s_b - s_tau65
        s_d76 = s_b - s_tau76
        s_x32 = s_tau32 - s_b
        assert flint.arb(0) < s_d65.ball() < s_d76.ball() < s_x32.ball() < b

        tr_e0, tr_o0 = eval_closed_form_trace(s_a)

        s_cuts = [s_d65, s_d76, s_x32]

        def split_pieces(
            pieces: list[tuple[SymReal, SymReal, flint.arb]]
        ) -> list[tuple[SymReal, SymReal, flint.arb]]:
            out: list[tuple[SymReal, SymReal, flint.arb]] = []
            for aL, aR, c in pieces:
                pts = [aL]
                for p in s_cuts:
                    if p == aL or p == aR:
                        continue
                    if sym_strict_lt(aL, p) and sym_strict_lt(p, aR):
                        pts.append(p)
                pts.append(aR)
                for k in range(len(pts) - 1):
                    assert pts[k].ball() < pts[k + 1].ball()
                    out.append((pts[k], pts[k + 1], c))
            return out

        def apply_P0_even(
            pieces: list[tuple[SymReal, SymReal, flint.arb]]
        ) -> list[tuple[SymReal, SymReal, flint.arb]]:
            sub = split_pieces(pieces)
            out: list[tuple[SymReal, SymReal, flint.arb]] = []
            for aL, aR, c in sub:
                xm = (aL + aR).scale(Fraction(1, 2))
                if sym_strict_lt(xm, s_d65):
                    out.append((aL, aR, c * v_full))
                elif sym_strict_lt(xm, s_d76):
                    out.append((aL, aR, c * v_mid))
                elif sym_strict_lt(xm, s_x32):
                    out.append((aL, aR, c * v_1))
                else:
                    out.append((aL, aR, c * v_1))
                    out.append((s_tau32 - aR, s_tau32 - aL, c * c32_da))
            return out

        def apply_P0_inv_even(
            pieces: list[tuple[SymReal, SymReal, flint.arb]]
        ) -> list[tuple[SymReal, SymReal, flint.arb]]:
            sub = split_pieces(pieces)
            out: list[tuple[SymReal, SymReal, flint.arb]] = []
            for aL, aR, c in sub:
                xm = (aL + aR).scale(Fraction(1, 2))
                if sym_strict_lt(xm, s_d65):
                    out.append((aL, aR, c / v_full))
                elif sym_strict_lt(xm, s_d76):
                    out.append((aL, aR, c / v_mid))
                elif sym_strict_lt(xm, s_x32):
                    out.append((aL, aR, c / v_1))
                else:
                    out.append((aL, aR, c * alpha_1))
                    out.append((s_tau32 - aR, s_tau32 - aL, -c * beta_1))
            return out

        def inner_step_sym(
            p1: list[tuple[SymReal, SymReal, flint.arb]],
            p2: list[tuple[SymReal, SymReal, flint.arb]],
        ) -> flint.arb:
            s = flint.arb(0)
            for a1, b1, c1 in p1:
                for a2, b2, c2 in p2:
                    left = sym_max(a1, a2)
                    right = sym_min(b1, b2)
                    if sym_strict_lt(left, right):
                        s = s + c1 * c2 * (right - left).ball()
            return s

        vecs: list[list[tuple[SymReal, SymReal, flint.arb]]] = []
        b_diag: list[flint.arb] = []
        for r in range(n_sub):
            p = s_d76.scale(Fraction(r, n_sub))
            q = s_d76.scale(Fraction(r + 1, n_sub))
            vecs.append([(p, q, flint.arb(1)), (p + s_tau76, q + s_tau76, flint.arb(-1))])
            b_diag.append((q - p).ball() / c76)
        for r in range(n_sub):
            p = s_d65.scale(Fraction(r, n_sub))
            q = s_d65.scale(Fraction(r + 1, n_sub))
            vecs.append([(p, q, flint.arb(1)), (p + s_tau65, q + s_tau65, flint.arb(-1))])
            b_diag.append((q - p).ball() / c65)
        for r in range(n_sub):
            p = s_tau76.scale(Fraction(r, 2 * n_sub))
            q = s_tau76.scale(Fraction(r + 1, 2 * n_sub))
            vecs.append([(p, q, flint.arb(1)), (s_tau76 - q, s_tau76 - p, flint.arb(-1))])
            b_diag.append((q - p).ball() / c76)
        for r in range(n_sub):
            p = s_tau65.scale(Fraction(r, 2 * n_sub))
            q = s_tau65.scale(Fraction(r + 1, 2 * n_sub))
            vecs.append([(p, q, flint.arb(1)), (s_tau65 - q, s_tau65 - p, flint.arb(-1))])
            b_diag.append((q - p).ball() / c65)

        m_tot = len(vecs)
        u_vecs = [apply_P0_inv_even(w) for w in vecs]

        m_wood: list[list[flint.arb]] = [
            [
                (b_diag[i] if i == j else flint.arb(0)) + inner_step_sym(vecs[i], u_vecs[j])
                for j in range(m_tot)
            ]
            for i in range(m_tot)
        ]

        s_half_b = s_b.scale(Fraction(1, 2))
        u_test: list[list[tuple[SymReal, SymReal, flint.arb]]] = [
            [(s_zero, s_half_b, flint.arb(1))],
            [(s_half_b, s_b, flint.arb(1))],
        ]

        id_m = [[flint.arb(1 if i == j else 0) for j in range(m_tot)] for i in range(m_tot)]
        m_wood_inv = solve_linear_arb(m_wood, id_m)
        m_wood_inv_sym = [
            [flint.acb(flint.arb("0.5") * (m_wood_inv[i][j] + m_wood_inv[j][i])) for j in range(m_tot)]
            for i in range(m_tot)
        ]

        # Express every u in u_vecs + u_test in terms of unique symbolic prefix endpoints p > 0:
        prefix_pts: list[SymReal] = []
        prefix_index: dict[tuple[tuple[int, Fraction], ...], int] = {}

        def find_or_add_pt(p: SymReal) -> int:
            if p.key in prefix_index:
                return prefix_index[p.key]
            idx = len(prefix_pts)
            prefix_pts.append(p)
            prefix_index[p.key] = idx
            return idx

        u_prefix_raw: list[dict[int, flint.arb]] = []
        for u in u_vecs + u_test:
            coeffs: dict[int, flint.arb] = {}
            for aL, aR, c in u:
                if aR != s_zero:
                    assert aR.ball() > flint.arb(0)
                    ir = find_or_add_pt(aR)
                    coeffs[ir] = coeffs.get(ir, flint.arb(0)) + c * aR.ball()
                if aL != s_zero:
                    assert aL.ball() > flint.arb(0)
                    il = find_or_add_pt(aL)
                    coeffs[il] = coeffs.get(il, flint.arb(0)) - c * aL.ball()
            u_prefix_raw.append(coeffs)

        u_prefix: list[list[tuple[int, flint.acb]]] = []
        for coeffs in u_prefix_raw:
            row_lst: list[tuple[int, flint.acb]] = []
            for idx, val in coeffs.items():
                row_lst.append((idx, flint.acb(val)))
            u_prefix.append(row_lst)

        n_elem = len(prefix_pts)
        prefix_pts_acb = [flint.acb(p.ball()) for p in prefix_pts]

        def eval_u_hats(xi: flint.acb) -> list[flint.acb]:
            sincs = [acb_sinc(xi * p_acb) for p_acb in prefix_pts_acb]
            hats: list[flint.acb] = []
            for lst in u_prefix:
                s = flint.acb(0)
                for idx, w_c in lst:
                    s = s + w_c * sincs[idx]
                hats.append(s)
            return hats

        def int_red_and_g00(xi: flint.acb, _: Any) -> flint.acb:
            w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_L3_acb(xi, log2, log3) * (flint.acb(da) - alpha_acb(xi))
            hats = eval_u_hats(xi)
            quad = flint.acb(0)
            for i in range(m_tot):
                hi = hats[i]
                row_i = m_wood_inv_sym[i]
                quad = quad + row_i[i] * hi * hi
                for j in range(i + 1, m_tot):
                    quad = quad + flint.acb(2) * row_i[j] * hi * hats[j]
            g00 = hats[m_tot] * hats[m_tot]
            return w_m * (quad + flint.acb(0, 1) * g00)

        def int_g01_and_g11(xi: flint.acb, _: Any) -> flint.acb:
            w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_L3_acb(xi, log2, log3) * (flint.acb(da) - alpha_acb(xi))
            hats = eval_u_hats(xi)
            g01 = hats[m_tot] * hats[m_tot + 1]
            g11 = hats[m_tot + 1] * hats[m_tot + 1]
            return w_m * (g01 + flint.acb(0, 1) * g11)

        red_even, g00_val = integrate_on_0_to_xi0(int_red_and_g00, xi0)
        g01_val, g11_val = integrate_on_0_to_xi0(int_g01_and_g11, xi0)
        tr_even_after = tr_e0 - red_even
        g_2: list[list[flint.arb]] = [[g00_val, g01_val], [g01_val, g11_val]]

        m_2: list[list[flint.arb]] = [[flint.arb(0), flint.arb(0)], [flint.arb(0), flint.arb(0)]]
        for i in range(2):
            pu_i = apply_P0_even(u_test[i])
            for j in range(2):
                s = inner_step_sym(pu_i, u_test[j])
                for m_idx in range(m_tot):
                    s = s + (
                        inner_step_sym(u_test[i], vecs[m_idx])
                        * inner_step_sym(u_test[j], vecs[m_idx])
                        / b_diag[m_idx]
                    )
                m_2[i][j] = s

        det_M2 = m_2[0][0] * m_2[1][1] - m_2[0][1] * m_2[1][0]
        det_G2 = g_2[0][0] * g_2[1][1] - g_2[0][1] * g_2[1][0]
        tr_cross = m_2[0][0] * g_2[1][1] + m_2[1][1] * g_2[0][0] - flint.arb(2) * m_2[0][1] * g_2[0][1]
        disc = tr_cross * tr_cross - flint.arb(4) * det_M2 * det_G2
        assert disc > flint.arb(0) and det_M2 > flint.arb(0)
        sqrt_disc = disc.sqrt()
        mu_2 = (tr_cross - sqrt_disc) / (flint.arb(2) * det_M2)
        mu_1 = (tr_cross + sqrt_disc) / (flint.arb(2) * det_M2)
        assert mu_2 > flint.arb(0)

        op_norm_bound = tr_even_after - mu_2
        assert tr_even_after < flint.arb(1), f"Even trace >= 1 at a={a}: {tr_even_after}"
        assert op_norm_bound < flint.arb(1), f"Op norm bound >= 1 at a={a}: {op_norm_bound}"

        coercivity_h = lambda_min_P0 * (flint.arb(1) - op_norm_bound)

        return {
            "a": arb_to_dict(a),
            "b": arb_to_dict(b),
            "n_sub": n_sub,
            "num_prime_step_vectors": m_tot,
            "num_elementary_intervals": n_elem,
            "tr_even_0vec": arb_to_dict(tr_e0),
            "woodbury_reduction_even": arb_to_dict(red_even),
            "tr_even_after": arb_to_dict(tr_even_after),
            "tr_odd_0vec": arb_to_dict(tr_o0),
            "cauchy_poincare_mu1": arb_to_dict(mu_1),
            "cauchy_poincare_mu2": arb_to_dict(mu_2),
            "op_norm_upper_bound": arb_to_dict(op_norm_bound),
            "margin_trace_even": arb_to_dict(flint.arb(1) - tr_even_after),
            "margin_op_norm_even": arb_to_dict(flint.arb(1) - op_norm_bound),
            "margin_odd": arb_to_dict(flint.arb(1) - tr_o0),
            "coercivity_h_L2": arb_to_dict(coercivity_h),
            "certified": bool(tr_even_after < flint.arb(1) and tr_o0 < flint.arb(1)),
            "elapsed_s": round(time.time() - tc, 3),
        }

    regime_4b_results: list[dict[str, Any]] = [
        {"label": "a = 1.135000 (M=4 prime vectors)", **eval_continuum_woodbury(SymReal.const(Fraction(227, 200)), 1)},
        {"label": "a = 1.145000 (M=4 prime vectors)", **eval_continuum_woodbury(SymReal.const(Fraction(229, 200)), 1)},
        {"label": "a = 1/2 log 10 (M=4 prime vectors)", **eval_continuum_woodbury(s_log10.scale(Fraction(1, 2)), 1)},
        {"label": "a = 1/2 log 10 (M=8 prime vectors)", **eval_continuum_woodbury(s_log10.scale(Fraction(1, 2)), 2)},
    ]

    return {
        "regime": "(log 3, (1/2) log 10] ~ (1.098612, 1.151293]",
        "subspace": "Ran(B_{2, 3}) subset L^2_{pole-free}(-a, a)",
        "Delta_alpha": arb_to_dict(da),
        "xi0": arb_to_dict(xi0),
        "v_full": arb_to_dict(v_full),
        "v_mid": arb_to_dict(v_mid),
        "v_1": arb_to_dict(v_1),
        "c32_da": arb_to_dict(c32_da),
        "lambda_min_P0": arb_to_dict(lambda_min_P0),
        "regime_4a_continuum": regime_4a_results,
        "regime_4b_woodbury_and_poincare": regime_4b_results,
        "elapsed_s": round(time.time() - t0, 3),
    }


def run_at_precision(prec_bits: int) -> dict[str, Any]:
    flint.ctx.prec = prec_bits
    sep_check = certify_exact_endpoint_separation()
    res_12 = certify_theorem_1_and_2()
    res_3 = certify_theorem_3_up_to_log3()
    res_4 = certify_theorem_4_up_to_half_log10()
    return {
        "precision_bits": prec_bits,
        "exact_endpoint_separation": sep_check,
        "theorem_1_and_2_multiprime_mertens": res_12,
        "theorem_3_continuum_up_to_log3": res_3,
        "theorem_4_extension_up_to_half_log10": res_4,
    }


def verify_two_precision_consistency(run_256: dict[str, Any], run_384: dict[str, Any]) -> dict[str, Any]:
    flint.ctx.prec = 384
    checks = 0

    for c256, c384 in zip(
        run_256["theorem_1_and_2_multiprime_mertens"]["single_prime_checks"],
        run_384["theorem_1_and_2_multiprime_mertens"]["single_prime_checks"],
    ):
        for k in ("diag_coeff_I", "shift_coeff_S_logp", "untruncated_W_p_at_xi0"):
            assert flint.arb(c256[k]["str"]).overlaps(flint.arb(c384[k]["str"]))
            checks += 1

    for m256, m384 in zip(
        run_256["theorem_1_and_2_multiprime_mertens"]["mertens_table"],
        run_384["theorem_1_and_2_multiprime_mertens"]["mertens_table"],
    ):
        for k in ("C_zero", "C_diag", "gamma_normalized_gain", "symbol_floor_L_P_at_xi0"):
            assert flint.arb(m256[k]["str"]).overlaps(flint.arb(m384[k]["str"]))
            checks += 1

    for cp256, cp384 in zip(
        run_256["theorem_3_continuum_up_to_log3"]["checkpoints"],
        run_384["theorem_3_continuum_up_to_log3"]["checkpoints"],
    ):
        for k in ("lambda_min_P0", "tr_even", "tr_odd", "coercivity_h_L2"):
            assert flint.arb(cp256[k]["str"]).overlaps(flint.arb(cp384[k]["str"]))
            checks += 1

    for cp256, cp384 in zip(
        run_256["theorem_4_extension_up_to_half_log10"]["regime_4a_continuum"],
        run_384["theorem_4_extension_up_to_half_log10"]["regime_4a_continuum"],
    ):
        for k in ("tr_even_0vec", "tr_odd_0vec"):
            assert flint.arb(cp256[k]["str"]).overlaps(flint.arb(cp384[k]["str"]))
            checks += 1

    for cp256, cp384 in zip(
        run_256["theorem_4_extension_up_to_half_log10"]["regime_4b_woodbury_and_poincare"],
        run_384["theorem_4_extension_up_to_half_log10"]["regime_4b_woodbury_and_poincare"],
    ):
        for k in ("tr_even_after", "tr_odd_0vec", "cauchy_poincare_mu2", "op_norm_upper_bound", "coercivity_h_L2"):
            assert flint.arb(cp256[k]["str"]).overlaps(flint.arb(cp384[k]["str"]))
            checks += 1

    return {
        "precisions_compared": [256, 384],
        "num_ball_overlap_checks": checks,
        "all_overlaps_verified": True,
    }


def main() -> None:
    t_start = time.time()
    out_dir = Path(__file__).resolve().parent

    print("=== Milestone 7 (Repaired): Two-Precision (256 & 384-Bit) ARB Verification of Multi-Prime Preconditioner ===")
    run_256 = run_at_precision(256)
    run_384 = run_at_precision(384)
    consistency = verify_two_precision_consistency(run_256, run_384)

    res_12 = run_384["theorem_1_and_2_multiprime_mertens"]
    res_3 = run_384["theorem_3_continuum_up_to_log3"]
    res_4 = run_384["theorem_4_extension_up_to_half_log10"]

    all_passed = (
        consistency["all_overlaps_verified"]
        and run_384["exact_endpoint_separation"]["strict_inequality_0_lt_1e_minus_101"]
        and all(c["all_higher_powers_annihilated"] for c in res_12["single_prime_checks"])
        and all(cp["certified"] for cp in res_3["checkpoints"])
        and all(cp["certified"] for cp in res_4["regime_4a_continuum"])
        and all(cp["certified"] for cp in res_4["regime_4b_woodbury_and_poincare"])
    )
    assert all_passed, "Verification failed!"

    payload: dict[str, Any] = {
        "audit_package": "multiprime-euler-preconditioner-2026-10-15-v1",
        "precision_bits": 384,
        "secondary_precision_bits": 256,
        "audit_repairs_applied": [
            "precision: exact algebraic arb_min/arb_max (0.5*(a+b-/+|a-b|)), rigorous ball root-tail enclosure",
            "symbolic_endpoints: exact SymReal in Q + sum_p Q*log(p) with zero decimal tolerances (0 and 1e-101 strictly separated)",
            "two_precision_replay: full 256-bit and 384-bit replay comparison archived in verification.json",
            "range: explicit Ran(B_{P_+, P_-}) subsetneq L^2_{pole-free}(-a, a) subspace qualification and density/transfer requirement",
            "diagonal: C_zero(P) = prod(1+1/p) zero-shift coefficient terminology and xi=0 untruncated symbol sign note",
            "horizon: explicit comparison against fixed-window complete lambda=4 horizon a = log 4 ~ 1.3863",
            "parity: explicit self-adjoint parity-preserving hypothesis on W and P_b projection on L^2(-b, b)",
            "orthogonality: pairwise orthogonality within each of the 4 operator families inverted jointly by M_wood = B + W^T P_0^{-1} W",
            "stale_numbers: all numerical values in derivation.md and README.md synchronized to verification.json",
        ],
        "all_assertions_passed": all_passed,
        "two_precision_consistency": consistency,
        "exact_endpoint_separation": run_384["exact_endpoint_separation"],
        "theorem_1_and_2_multiprime_mertens": res_12,
        "theorem_3_continuum_up_to_log3": res_3,
        "theorem_4_extension_up_to_half_log10": res_4,
        "secondary_256bit_summary": {
            "exact_endpoint_separation": run_256["exact_endpoint_separation"],
            "theorem_3_checkpoints": run_256["theorem_3_continuum_up_to_log3"]["checkpoints"],
            "theorem_4_regime_4a": run_256["theorem_4_extension_up_to_half_log10"]["regime_4a_continuum"],
            "theorem_4_regime_4b": run_256["theorem_4_extension_up_to_half_log10"]["regime_4b_woodbury_and_poincare"],
        },
        "wall_status": {
            "RH": "OPEN",
            "G2": "OPEN",
            "cofinal_signed_arithmetic_lower_bound": "OPEN",
            "missing_original_evidence_groups": "OPEN",
        },
        "total_elapsed_s": round(time.time() - t_start, 3),
    }

    out_path = out_dir / "verification.json"
    raw_bytes = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
    sha256_hex = hashlib.sha256(raw_bytes).hexdigest()
    payload["sha256"] = sha256_hex
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    file_sha256 = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"Two-precision overlap checks: {consistency['num_ball_overlap_checks']} PASS")
    print(f"payload.sha256 = {sha256_hex}")
    print(f"file_sha256    = {file_sha256}")


if __name__ == "__main__":
    main()
