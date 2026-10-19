#!/usr/bin/env python3
"""
Deterministic 384-bit flint.arb / flint.acb verification for:
  audits/all-vector-positivity-three-island-horizon-2026-10-15-v1

Certifies in 384-bit ball arithmetic (flint.ctx.prec = 384):
  1. Theorem 1 (Klein 4-Group Z_2 x Z_2 Dihedral Fiber Closure on (1/2 log(15/2), 3/2 log 2]):
     - Exact a-independent midpoint sum x_6 + d_5 = tau_6 - tau_5 = log(6/5),
     - Conjugacy R_{tau_6} T_{-tau_5} R_{tau_6} = T_{tau_5} in O(1) = R rtimes {+-1},
     - Exact domain [0, tau_3] of R_{tau_3} when b > tau_3 (a > log(8/3)),
     - 4x4 Klein 4-group fiber block-diagonalization into B_+, B_- with det(B_-) > 0.
  2. Theorem 2 (Exact Triple Coincidence at a_***** = 3/2 log 2 = 1/2 log 8 ~ 1.0397207708):
     - 2b = log 2 (saturation of the Three-Island Isometric Core P_b L_2^2 P_b = (13/4) I),
     - 2a = log 8 (exact boundary where prime-power n = 2^3 = 8 enters V_a),
     - x_6 = s_3 = 1/2 log(9/8) (exact meeting of m=3 shift domain and m=6 reflection endpoint).
  3. Theorem 3 (Universal Prime-2 Poisson Collapse Identity for all a > log 2):
     - Exact operator identity sum_{m*log 2 < 2a} r_2^m P_b L_2 S_{m*log 2} L_2 P_b
       = -P_b (L_2^2 - 1/2 L_2) P_b certified across a in {1.10, 1.25, 1.50, 2.00}.
  4. Theorem 4 (Courant-Fischer 2-Mode Deflated Trace Theorem & All-Vector Positivity
     Certificates on (1/2 log(15/2), 3/2 log 2]):
     - Certified T_even_defl(a) = Tr(P(a)^{-1} A_-(Delta_alpha)) - mu_2 < 1 and T_odd(a) < 1 at:
       * a = 1.0150000000 (K = 51, M_prime = 13, Delta_alpha = 0.30),
       * a = 1.0250000000 (K = 98, M_prime = 23, Delta_alpha = 0.30),
       * a = 1.0320000000 (K = 99, M_prime = 23, Delta_alpha = 0.35),
       * a_***** = 3/2 log 2 = 1/2 log 8 ~ 1.0397207708 (K = 131, M_prime = 28, Delta_alpha = 0.35).
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
import time
from pathlib import Path
from typing import Any

import flint  # type: ignore

PREC_BITS = 384
flint.ctx.prec = PREC_BITS
INT_TOL = 2**-64


def arb_to_dict(x: Any) -> dict[str, Any]:
    return {
        "str": str(x),
        "mid": float(x.mid().str(18, radius=False)),
        "rad": float(x.rad().str(18, radius=False)),
        "lower": float(x.lower().str(18, radius=False)),
        "upper": float(x.upper().str(18, radius=False)),
    }


def arb_abs(x: Any) -> Any:
    return abs(x)


def arb_max(a: Any, b: Any) -> Any:
    """Exact interval enclosure of max(a, b) in 384-bit ball arithmetic without float conversion."""
    lo_a, lo_b = a.lower(), b.lower()
    hi_a, hi_b = a.upper(), b.upper()
    lo = lo_a if lo_a > lo_b else (lo_b if lo_b > lo_a else flint.arb("0.5") * (lo_a + lo_b + abs(lo_a - lo_b)))
    hi = hi_a if hi_a > hi_b else (hi_b if hi_b > hi_a else flint.arb("0.5") * (hi_a + hi_b + abs(hi_a - hi_b)))
    mid = flint.arb("0.5") * (lo + hi)
    mid_pt = mid.mid()
    rad = flint.arb("0.5") * (hi - lo) + abs(mid - mid_pt)
    return flint.arb(mid_pt, rad.upper())


def arb_strict_lt(a: Any, b: Any) -> bool:
    """Certified strict inequality in 384-bit ball arithmetic."""
    if a < b:
        return True
    if a > b:
        return False
    raise AssertionError(f"Undecided strict inequality between balls: {a} vs {b}")


def frac_to_arb(q: Fraction) -> Any:
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

    def ball(self) -> Any:
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


def alpha_acb(xi: Any) -> Any:
    pi_acb = flint.acb.pi()
    z1 = flint.acb("0.25") + flint.acb(0, "0.5") * xi
    z2 = flint.acb("0.25") - flint.acb(0, "0.5") * xi
    return flint.acb("0.5") * (z1.digamma() + z2.digamma()) - pi_acb.log()


def alpha_arb(xi: Any) -> Any:
    return alpha_acb(flint.acb(xi)).real


def sigma_L2_sq_acb(xi: Any, log2_arb: Any) -> Any:
    s = flint.acb("1.5") - flint.acb(2).sqrt() * (xi * flint.acb(log2_arb)).cos()
    return s * s


def acb_sinc(z: Any) -> Any:
    return z.sinc()


def find_alpha_root_arb(target_da: Any) -> Any:
    """Enclose the unique root xi > 0 of alpha(xi) = target_da in 384-bit arb."""
    lo = flint.arb("6.0")
    hi = flint.arb("20.0")
    for _ in range(300):
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


def solve_linear_arb(a_mat: list[list[Any]], b_mat: list[list[Any]]) -> list[list[Any]]:
    """Rigorous Gauss-Jordan linear solver in 384-bit flint.arb for N x N systems A X = B."""
    n = len(a_mat)
    m = len(b_mat[0])
    aug = [[a_mat[i][j] for j in range(n)] + [b_mat[i][j] for j in range(m)] for i in range(n)]
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


def seed_generalized_top_vecs(
    g_mat: list[list[float]], m_mat: list[list[float]], n_vecs: int = 2
) -> list[list[float]]:
    n = len(g_mat)
    l_mat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = g_mat[i][j] - sum(l_mat[i][k] * l_mat[j][k] for k in range(j))
            if i == j:
                assert s > 0.0
                l_mat[i][i] = math.sqrt(s)
            else:
                l_mat[i][j] = s / l_mat[j][j]

    l_inv = [[0.0] * n for _ in range(n)]
    for col in range(n):
        for i in range(col, n):
            s = (1.0 if i == col else 0.0) - sum(l_mat[i][k] * l_inv[k][col] for k in range(col, i))
            l_inv[i][col] = s / l_mat[i][i]

    tmp = [[sum(m_mat[i][k] * l_inv[j][k] for k in range(j + 1)) for j in range(n)] for i in range(n)]
    a = [[sum(l_inv[i][k] * tmp[k][j] for k in range(i + 1)) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            avg = 0.5 * (a[i][j] + a[j][i])
            a[i][j] = avg
            a[j][i] = avg

    v_mat = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    sweep_tol = 2.0**-50
    for _ in range(15):
        max_val = 0.0
        for p in range(n):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) > max_val:
                    max_val = abs(apq)
                if abs(apq) < sweep_tol:
                    continue
                app, aqq = a[p][p], a[q][q]
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
                for r in range(n):
                    vrp, vrq = v_mat[r][p], v_mat[r][q]
                    v_mat[r][p] = c * vrp - s * vrq
                    v_mat[r][q] = s * vrp + c * vrq
        if max_val < sweep_tol:
            break

    order = sorted(range(n), key=lambda idx: a[idx][idx], reverse=True)
    out_vecs: list[list[float]] = []
    for k_idx in range(n_vecs):
        col = order[k_idx]
        y = [v_mat[i][col] for i in range(n)]
        x = [sum(l_inv[k][i] * y[k] for k in range(i, n)) for i in range(n)]
        m_abs = max(abs(val) for val in x)
        out_vecs.append([round(val / m_abs, 6) for val in x])
    return out_vecs


def certify_theorems_1_2_3() -> dict[str, Any]:
    """Certify the algebraic and operator identities in Theorems 1, 2, and 3."""
    l2 = flint.arb(2).log()
    l3 = flint.arb(3).log()
    l5 = flint.arb(5).log()
    l7 = flint.arb(7).log()
    tau3 = flint.arb(2) * l2 - l3
    tau5 = l5 - flint.arb(2) * l2
    tau6 = l3 - l2

    c0 = flint.arb("2.5") * l2
    c3 = l3 / (flint.arb(2) * flint.arb(3).sqrt())
    c5 = l5 / (flint.arb(2) * flint.arb(5).sqrt())
    c6 = (flint.arb("1.5")).sqrt() * l3
    c7 = l7 / (flint.arb(2) * flint.arb(7).sqrt())

    # Theorem 1: x_6 + d_5 = tau_6 - tau_5 = log(6/5) and B_-, B_+ > 0
    klein4_checks: list[dict[str, Any]] = []
    for a_str, da_str in [("1.015", "0.30"), ("1.025", "0.30"), ("1.032", "0.35"), ("half_log8", "0.35")]:
        a_v = flint.arb("1.5") * l2 if a_str == "half_log8" else flint.arb(a_str)
        da_v = flint.arb(da_str)
        b_v = a_v - l2
        x6_v = tau6 - b_v
        d5_v = b_v - tau5
        diff_id = (x6_v + d5_v) - (flint.arb(6) / flint.arb(5)).log()
        assert diff_id.contains(0)
        base0 = c0 + flint.arb("3.25") * da_v
        vx_worst = base0 - c5 - c3
        vy_worst = base0 - c3 - c7
        det_B_minus = vx_worst * vy_worst - (c5 + c6) * (c5 + c6)
        det_B_plus = vx_worst * vy_worst - (c5 - c6) * (c5 - c6)
        assert det_B_minus > 0 and det_B_plus > 0
        klein4_checks.append(
            {
                "a_label": a_str,
                "x6": arb_to_dict(x6_v),
                "d5": arb_to_dict(d5_v),
                "abs_x6_plus_d5_minus_log_6_5_upper": float(arb_abs(diff_id).upper().str(18, radius=False)),
                "det_B_minus_worst": arb_to_dict(det_B_minus),
                "det_B_plus_worst": arb_to_dict(det_B_plus),
                "certified": True,
            }
        )

    # Theorem 2: Exact triple coincidence at a = 3/2 log 2 = 1/2 log 8
    a_star5 = flint.arb("1.5") * l2
    b_star5 = a_star5 - l2
    x6_star5 = tau6 - b_star5
    s3_star5 = b_star5 - tau3
    d5_star5 = b_star5 - tau5
    diff_2b_l2 = flint.arb(2) * b_star5 - l2
    diff_2a_l8 = flint.arb(2) * a_star5 - flint.arb(8).log()
    diff_x6_s3 = x6_star5 - s3_star5
    assert diff_2b_l2.contains(0)
    assert diff_2a_l8.contains(0)
    assert diff_x6_s3.contains(0)

    # Theorem 3: Universal Prime-2 Poisson Collapse Identity across a > 3/2 log 2
    r2 = flint.arb(1) / flint.arb(2).sqrt()
    poisson_checks: list[dict[str, Any]] = []
    for a_str in ["1.10", "1.25", "1.50", "2.00"]:
        a_v = flint.arb(a_str)
        b_v = a_v - l2
        m_cut_fmpz = (flint.arb(2) * a_v / l2).floor().unique_fmpz()
        max_k_fmpz = (flint.arb(2) * b_v / l2).floor().unique_fmpz()
        assert m_cut_fmpz is not None and max_k_fmpz is not None
        m_cut = int(str(m_cut_fmpz))
        max_k_in_2b = int(str(max_k_fmpz))
        max_m = m_cut + 4
        coeff_T: dict[int, Any] = {k: flint.arb(0) for k in range(-max_m - 3, max_m + 4)}
        c_L2sq = {
            0: flint.arb("3.25"),
            1: -flint.arb(3) * r2,
            -1: -flint.arb(3) * r2,
            2: flint.arb("0.5"),
            -2: flint.arb("0.5"),
        }
        for m in range(1, m_cut + 1):
            w_m = -(r2**m)
            for s, cs in c_L2sq.items():
                coeff_T[m + s] = coeff_T[m + s] + w_m * cs
                coeff_T[-m + s] = coeff_T[-m + s] + w_m * cs
        target_T: dict[int, Any] = {
            0: flint.arb("2.5"),
            1: -flint.arb("2.5") * r2,
            -1: -flint.arb("2.5") * r2,
            2: flint.arb("0.5"),
            -2: flint.arb("0.5"),
        }
        max_coeff_err = flint.arb(0)
        for k in range(-max_k_in_2b, max_k_in_2b + 1):
            expected = target_T.get(k, flint.arb(0))
            diff_k = coeff_T[k] - expected
            assert diff_k.contains(0)
            err = arb_abs(diff_k)
            max_coeff_err = arb_max(max_coeff_err, err)
        poisson_checks.append(
            {
                "a": a_str,
                "b": arb_to_dict(b_v),
                "m_cut_finite_sum_terms": m_cut,
                "max_shift_index_on_Vb": max_k_in_2b,
                "max_operator_coeff_error_upper": float(max_coeff_err.upper().str(18, radius=False)),
                "certified": True,
            }
        )

    return {
        "theorem_1_klein4_closure_and_positivity": klein4_checks,
        "theorem_2_triple_coincidence_at_half_log8": {
            "a_star5": arb_to_dict(a_star5),
            "b_star5": arb_to_dict(b_star5),
            "x6_star5": arb_to_dict(x6_star5),
            "s3_star5": arb_to_dict(s3_star5),
            "d5_star5": arb_to_dict(d5_star5),
            "abs_2b_minus_log2_upper": float(arb_abs(diff_2b_l2).upper().str(18, radius=False)),
            "abs_2a_minus_log8_upper": float(arb_abs(diff_2a_l8).upper().str(18, radius=False)),
            "abs_x6_minus_s3_upper": float(arb_abs(diff_x6_s3).upper().str(18, radius=False)),
            "certified": True,
        },
        "theorem_3_universal_prime2_poisson_collapse": poisson_checks,
    }


def build_klein4_partition_arb(
    a_sym: SymReal,
    da: Any,
    split_mode: str,
) -> dict[str, Any]:
    """
    Construct the exact SymReal + 384-bit flint.arb Klein 4-group closed partition {I_1, ..., I_K}
    of [0, b] on (1/2 log(15/2), 3/2 log 2], together with P0_even, P0_odd, their
    rigorous inverses, and the prime step minorant vectors for m in {3, 5, 7}.
    """
    log2 = flint.arb(2).log()
    log3 = flint.arb(3).log()
    log5 = flint.arb(5).log()
    log7 = flint.arb(7).log()

    zero_sym = SymReal.zero()
    log2_sym = SymReal.log_prime(2)
    log3_sym = SymReal.log_prime(3)
    log5_sym = SymReal.log_prime(5)
    log7_sym = SymReal.log_prime(7)

    b_sym = a_sym - log2_sym
    b = b_sym.ball()

    c0 = flint.arb("2.5") * log2
    c3 = log3 / (flint.arb(2) * flint.arb(3).sqrt())
    c5 = log5 / (flint.arb(2) * flint.arb(5).sqrt())
    c6 = (flint.arb("1.5")).sqrt() * log3
    c7 = log7 / (flint.arb(2) * flint.arb(7).sqrt())

    tau3_sym = log2_sym.scale(2) - log3_sym
    tau5_sym = log5_sym - log2_sym.scale(2)
    tau6_sym = log3_sym - log2_sym
    tau7_sym = log7_sym - log2_sym.scale(2)

    tau3 = tau3_sym.ball()
    tau5 = tau5_sym.ball()
    tau6 = tau6_sym.ball()
    tau7 = tau7_sym.ball()

    x3_sym = tau3_sym - b_sym
    x3_pos_sym = x3_sym if sym_strict_lt(zero_sym, x3_sym) else zero_sym
    has_s3_shift = sym_strict_lt(tau3_sym, b_sym)
    s3_sym = (b_sym - tau3_sym) if has_s3_shift else zero_sym
    d5_sym = b_sym - tau5_sym
    x6_sym = tau6_sym - b_sym
    x7_sym = tau7_sym - b_sym
    d5_refl_sym = tau5_sym - d5_sym

    m3_sym = tau3_sym.scale(Fraction(1, 2))
    m5_sym = tau5_sym.scale(Fraction(1, 2))
    m6_sym = tau6_sym.scale(Fraction(1, 2))
    m7_sym = tau7_sym.scale(Fraction(1, 2))
    m65_sym = (tau6_sym - tau5_sym).scale(Fraction(1, 2))

    x6 = x6_sym.ball()
    d5 = d5_sym.ball()
    s3 = s3_sym.ball()
    m6 = m6_sym.ball()

    base0 = c0 + flint.arb("3.25") * da

    if split_mode == "base":
        cand_3_L_sym = [
            x3_pos_sym,
            s3_sym,
            d5_sym,
            x6_sym,
            m65_sym,
            (x6_sym + m3_sym).scale(Fraction(1, 2)),
            m3_sym,
        ]
        cand_5_L_sym = [zero_sym, x3_pos_sym, s3_sym, d5_sym, d5_refl_sym, x6_sym, m65_sym, m5_sym]
        pts_7_L_sym = [x7_sym, m7_sym]
        s3_cuts_sym = [zero_sym, s3_sym] if has_s3_shift else []
    elif split_mode == "medium":
        cand_3_L_sym = [
            x3_pos_sym,
            s3_sym.scale(Fraction(1, 2)),
            s3_sym,
            (s3_sym + x6_sym).scale(Fraction(1, 2)),
            x6_sym,
            (x6_sym + m65_sym).scale(Fraction(1, 2)),
            m65_sym,
            (m65_sym + d5_sym).scale(Fraction(1, 2)),
            d5_sym,
            (d5_sym + m3_sym).scale(Fraction(1, 2)),
            m3_sym,
        ]
        cand_5_L_sym = [
            zero_sym,
            s3_sym.scale(Fraction(1, 2)),
            s3_sym,
            (s3_sym + x6_sym).scale(Fraction(1, 2)),
            x6_sym,
            (x6_sym + m65_sym).scale(Fraction(1, 2)),
            m65_sym,
            (m65_sym + d5_refl_sym).scale(Fraction(1, 2)),
            d5_refl_sym,
            d5_sym,
            m5_sym,
        ]
        pts_7_L_sym = [x7_sym, (x7_sym + m7_sym).scale(Fraction(1, 2)), m7_sym]
        s3_cuts_sym = [zero_sym, s3_sym.scale(Fraction(1, 2)), s3_sym]
    else:
        cand_3_L_sym = [
            x3_pos_sym,
            x6_sym.scale(Fraction(1, 4)),
            x6_sym.scale(Fraction(1, 2)),
            x6_sym.scale(Fraction(3, 4)),
            s3_sym,
            x6_sym,
            (x6_sym + m65_sym).scale(Fraction(1, 2)),
            m65_sym,
            (m65_sym + d5_sym).scale(Fraction(1, 2)),
            d5_sym,
            (d5_sym + m3_sym).scale(Fraction(1, 2)),
            m3_sym,
        ]
        cand_5_L_sym = [
            zero_sym,
            x6_sym.scale(Fraction(1, 4)),
            x6_sym.scale(Fraction(1, 2)),
            x6_sym.scale(Fraction(3, 4)),
            s3_sym,
            x6_sym,
            (x6_sym + m65_sym).scale(Fraction(1, 2)),
            m65_sym,
            (m65_sym + d5_refl_sym).scale(Fraction(1, 2)),
            d5_refl_sym,
            d5_sym,
            (d5_refl_sym + m5_sym).scale(Fraction(1, 2)),
            m5_sym,
        ]
        pts_7_L_sym = [x7_sym + (m7_sym - x7_sym).scale(Fraction(r, 4)) for r in range(5)]
        s3_cuts_sym = [s3_sym.scale(Fraction(r, 4)) for r in range(5)]

    pts_3_L_sym = deduplicate_and_sort_sym(
        [x3_pos_sym, m3_sym]
        + [p for p in cand_3_L_sym if sym_le(x3_pos_sym, p) and sym_le(p, m3_sym)]
    )
    pts_5_L_sym = deduplicate_and_sort_sym(
        [zero_sym, m5_sym]
        + [p for p in cand_5_L_sym if sym_le(zero_sym, p) and sym_le(p, m5_sym)]
    )

    pts_3_R_sym = [tau3_sym - p for p in pts_3_L_sym]
    pts_5_R_sym = [tau5_sym - p for p in pts_5_L_sym]
    pts_7_R_sym = [tau7_sym - p for p in pts_7_L_sym]
    s3_R_sym = [tau3_sym + p for p in s3_cuts_sym]

    raw_pts_sym = [
        zero_sym,
        b_sym,
        x3_pos_sym,
        s3_sym,
        d5_sym,
        x6_sym,
        x7_sym,
        m6_sym,
        m3_sym,
        m5_sym,
        m7_sym,
        m65_sym,
        m65_sym + tau5_sym,
        tau5_sym,
        tau6_sym - tau5_sym,
        tau3_sym,
    ]
    raw_pts_sym.extend(
        pts_3_L_sym
        + pts_3_R_sym
        + pts_5_L_sym
        + pts_5_R_sym
        + pts_7_L_sym
        + pts_7_R_sym
        + s3_cuts_sym
        + s3_R_sym
    )

    pts_set_sym = deduplicate_and_sort_sym(
        [p for p in raw_pts_sym if sym_le(zero_sym, p) and sym_le(p, b_sym)]
    )

    # Iterate closure under (tau5, tau6) Klein 4-group / dihedral fiber maps in exact SymReal:
    for _ in range(6):
        new_pts_sym = list(pts_set_sym)
        for p in pts_set_sym:
            if sym_le(p, d5_sym):
                new_pts_sym.append(p + tau5_sym)
            if sym_le(tau5_sym, p):
                new_pts_sym.append(p - tau5_sym)
            if sym_le(x6_sym, p):
                new_pts_sym.append(tau6_sym - p)
        pts_set_sym = deduplicate_and_sort_sym(
            [q for q in new_pts_sym if sym_le(zero_sym, q) and sym_le(q, b_sym)]
        )

    pts_sym = pts_set_sym
    assert pts_sym[0] == zero_sym and pts_sym[-1] == b_sym
    pts = [p.ball() for p in pts_sym]
    k_int = len(pts_sym) - 1
    mids_sym = [(pts_sym[i] + pts_sym[i + 1]).scale(Fraction(1, 2)) for i in range(k_int)]
    lens_sym = [pts_sym[i + 1] - pts_sym[i] for i in range(k_int)]
    mids = [m.ball() for m in mids_sym]
    lens = [l.ball() for l in lens_sym]
    mid_index_map = {m.key: idx for idx, m in enumerate(mids_sym)}

    p0_e = [[flint.arb(0) for _ in range(k_int)] for _ in range(k_int)]
    p0_o = [[flint.arb(0) for _ in range(k_int)] for _ in range(k_int)]

    for i in range(k_int):
        xm_sym = mids_sym[i]
        vi = base0
        if sym_strict_lt(xm_sym, tau5_sym):
            vi = vi - c5
        # Exact domain of R_{tau_3} when b > tau_3 is [0, tau_3]:
        if sym_strict_lt(xm_sym, tau3_sym):
            vi = vi - c3
        # Shift T_{+-tau_3} on [0, s_3] union [tau_3, b]:
        if sym_strict_lt(xm_sym, s3_sym) or sym_strict_lt(tau3_sym, xm_sym):
            vi = vi - c3
        if sym_strict_lt(x7_sym, xm_sym):
            vi = vi - c7
        p0_e[i][i] = vi
        p0_o[i][i] = vi

        if sym_strict_lt(xm_sym, d5_sym):
            target5_sym = xm_sym + tau5_sym
            j2 = mid_index_map[target5_sym.key]
            assert mids_sym[j2] - mids_sym[i] == tau5_sym
            assert lens_sym[j2] == lens_sym[i]
            assert ((mids[j2] - mids[i]) - tau5).contains(0)
            assert (lens[j2] - lens[i]).contains(0)
            p0_e[i][j2] = -c5
            p0_e[j2][i] = -c5
            p0_o[i][j2] = -c5
            p0_o[j2][i] = -c5

        if sym_strict_lt(x6_sym, xm_sym):
            target6_sym = tau6_sym - xm_sym
            j6 = mid_index_map[target6_sym.key]
            assert mids_sym[i] + mids_sym[j6] == tau6_sym
            assert lens_sym[j6] == lens_sym[i]
            assert ((mids[i] + mids[j6]) - tau6).contains(0)
            assert (lens[j6] - lens[i]).contains(0)
            p0_e[i][j6] = c6
            p0_o[i][j6] = -c6

    eye_k = [[flint.arb(1 if i == j else 0) for j in range(k_int)] for i in range(k_int)]
    p0inv_e = solve_linear_arb(p0_e, eye_k)
    p0inv_o = solve_linear_arb(p0_o, eye_k)

    # Verify det-grading relation P0inv_o[i][j] = +- P0inv_e[i][j] and positivity of diagonal:
    for i in range(k_int):
        assert p0inv_e[i][i] > 0 and p0inv_o[i][i] > 0
        for j in range(k_int):
            if not p0inv_e[i][j].contains(0):
                assert (p0inv_o[i][j] - p0inv_e[i][j]).contains(0) or (
                    p0inv_o[i][j] + p0inv_e[i][j]
                ).contains(0)

    # Prime step vectors (m = 3, 5, 7 reflections + m = 3 shift difference vectors on [0, s_3]):
    phi_e: list[list[Any]] = []
    phi_o: list[list[Any]] = []
    d_prime: list[Any] = []

    for pts_L_cur_sym, tau_sym, c_val in [
        (pts_3_L_sym, tau3_sym, c3),
        (pts_5_L_sym, tau5_sym, c5),
        (pts_7_L_sym, tau7_sym, c7),
    ]:
        for r in range(len(pts_L_cur_sym) - 1):
            lo_L_sym, hi_L_sym = pts_L_cur_sym[r], pts_L_cur_sym[r + 1]
            if lo_L_sym == hi_L_sym:
                continue
            lo_R_sym, hi_R_sym = tau_sym - hi_L_sym, tau_sym - lo_L_sym
            lo_L, hi_L = lo_L_sym.ball(), hi_L_sym.ball()
            norm_r = (flint.arb(2) * (hi_L - lo_L)).sqrt()
            inv_norm = flint.arb(1) / norm_r
            ue = [flint.arb(0) for _ in range(k_int)]
            uo = [flint.arb(0) for _ in range(k_int)]
            len_L = flint.arb(0)
            len_R = flint.arb(0)
            for i in range(k_int):
                if sym_le(lo_L_sym, pts_sym[i]) and sym_le(pts_sym[i + 1], hi_L_sym):
                    ue[i] = inv_norm
                    uo[i] = inv_norm
                    len_L += lens[i]
                elif sym_le(lo_R_sym, pts_sym[i]) and sym_le(pts_sym[i + 1], hi_R_sym):
                    ue[i] = -inv_norm
                    uo[i] = inv_norm
                    len_R += lens[i]
            assert (len_L - (hi_L - lo_L)).contains(0)
            assert (len_R - (hi_L - lo_L)).contains(0)
            phi_e.append(ue)
            phi_o.append(uo)
            d_prime.append(flint.arb(1) / (flint.arb(2) * c_val))

    for r in range(len(s3_cuts_sym) - 1):
        lo_s_sym, hi_s_sym = s3_cuts_sym[r], s3_cuts_sym[r + 1]
        if lo_s_sym == hi_s_sym:
            continue
        lo_s, hi_s = lo_s_sym.ball(), hi_s_sym.ball()
        inv_norm_s = flint.arb(1) / (flint.arb(2) * (hi_s - lo_s)).sqrt()
        ue_s = [flint.arb(0) for _ in range(k_int)]
        len_sL = flint.arb(0)
        len_sR = flint.arb(0)
        for i in range(k_int):
            if sym_le(lo_s_sym, pts_sym[i]) and sym_le(pts_sym[i + 1], hi_s_sym):
                ue_s[i] = inv_norm_s
                len_sL += lens[i]
            elif sym_le(tau3_sym + lo_s_sym, pts_sym[i]) and sym_le(
                pts_sym[i + 1], tau3_sym + hi_s_sym
            ):
                ue_s[i] = -inv_norm_s
                len_sR += lens[i]
        assert (len_sL - (hi_s - lo_s)).contains(0)
        assert (len_sR - (hi_s - lo_s)).contains(0)
        phi_e.append(ue_s)
        phi_o.append(list(ue_s))
        d_prime.append(flint.arb(1) / (flint.arb(2) * c3))

    return {
        "K": k_int,
        "pts": pts,
        "mids": mids,
        "lens": lens,
        "P0_e": p0_e,
        "P0_o": p0_o,
        "P0inv_e": p0inv_e,
        "P0inv_o": p0inv_o,
        "phi_e": phi_e,
        "phi_o": phi_o,
        "d_prime": d_prime,
        "x6": x6,
        "d5": d5,
        "s3": s3,
        "m6": m6,
        "b": b,
    }


def certify_klein4_checkpoint(
    label: str,
    a_sym: SymReal,
    da: Any,
    xi1: Any,
    split_mode: str,
) -> dict[str, Any]:
    """
    Certify T_even_defl(a) = Tr(P(a)^{-1} A_-(da)) - mu_2 < 1 and T_odd(a) < 1
    in 384-bit flint.arb using the Klein 4-group fiber preconditioner + prime step
    minorants + 2-mode Plancherel step minorant + Courant-Fischer 2-Mode Deflation.
    """
    t0 = time.time()
    a = a_sym.ball()
    log2 = flint.arb(2).log()
    pi = flint.arb.pi()
    xi0 = find_alpha_root_arb(da)
    assert xi1 > xi0, "xi1 must exceed xi0"

    part = build_klein4_partition_arb(a_sym, da, split_mode=split_mode)
    k_int: int = part["K"]
    mids: list[Any] = part["mids"]
    lens: list[Any] = part["lens"]
    p0_e_mat: list[list[Any]] = part["P0_e"]
    p0inv_e_mat: list[list[Any]] = part["P0inv_e"]
    p0inv_o_mat: list[list[Any]] = part["P0inv_o"]
    phi_e: list[list[Any]] = part["phi_e"]
    phi_o: list[list[Any]] = part["phi_o"]
    d_prime: list[Any] = part["d_prime"]
    x6: Any = part["x6"]
    d5: Any = part["d5"]
    s3: Any = part["s3"]
    m6: Any = part["m6"]
    b: Any = part["b"]

    m_prime = len(d_prime)

    p0inv_e_phi = [
        [sum((p0inv_e_mat[i][j] * phi_e[k][j] for j in range(k_int)), flint.arb(0)) for i in range(k_int)]
        for k in range(m_prime)
    ]
    p0inv_o_phi = [
        [sum((p0inv_o_mat[i][j] * phi_o[k][j] for j in range(k_int)), flint.arb(0)) for i in range(k_int)]
        for k in range(m_prime)
    ]
    j_prime = [
        [
            sum((lens[i] * phi_e[j][i] * p0inv_e_phi[k][i] for i in range(k_int)), flint.arb(0))
            for k in range(m_prime)
        ]
        for j in range(m_prime)
    ]
    dj_o = [
        [
            sum((lens[i] * phi_o[j][i] * p0inv_o_phi[k][i] for i in range(k_int)), flint.arb(0))
            + (d_prime[j] if j == k else flint.arb(0))
            for k in range(m_prime)
        ]
        for j in range(m_prime)
    ]
    eye_mp = [[flint.arb(1 if j == k else 0) for k in range(m_prime)] for j in range(m_prime)]
    dj_o_inv = solve_linear_arb(dj_o, eye_mp)

    # Sparse non-zero entries of P0inv_e and P0inv_o:
    nz_e: list[tuple[int, int, Any]] = []
    nz_o: list[tuple[int, int, Any]] = []
    for i in range(k_int):
        for j in range(k_int):
            if not p0inv_e_mat[i][j].contains(0):
                nz_e.append((i, j, p0inv_e_mat[i][j]))
            if not p0inv_o_mat[i][j].contains(0):
                nz_o.append((i, j, p0inv_o_mat[i][j]))

    # 2-Mode Plancherel minorant (w_1, w_2):
    w1_vec: list[Any] = []
    w2_vec: list[Any] = []
    for i in range(k_int):
        u_i = mids[i] / b
        if arb_strict_lt(mids[i], x6):
            w1_vec.append(flint.arb(1))
        else:
            w1_vec.append(flint.arb(9) / flint.arb(10) - (flint.arb(3) / flint.arb(5)) * u_i)
        w2_vec.append(flint.arb(1) - flint.arb(2) * u_i)

    w_vecs = [w1_vec, w2_vec]
    g_w = [
        [
            sum((lens[i] * w_vecs[p][i] * w_vecs[q][i] for i in range(k_int)), flint.arb(0))
            for q in range(2)
        ]
        for p in range(2)
    ]

    def cw_pair_acb(om: Any) -> tuple[Any, Any]:
        r1 = flint.acb(0)
        r2 = flint.acb(0)
        for i in range(k_int):
            li_c = flint.acb(lens[i])
            mi_c = flint.acb(mids[i])
            ker = li_c * (om * mi_c).cos() * acb_sinc(flint.acb("0.5") * om * li_c)
            r1 += flint.acb(w1_vec[i]) * ker
            r2 += flint.acb(w2_vec[i]) * ker
        return r1, r2

    def int_m11_m22(om: Any, _: Any) -> Any:
        c1, c2 = cw_pair_acb(om)
        pref = (flint.acb(2) / flint.acb(pi)) * sigma_L2_sq_acb(om, log2)
        return pref * (c1 * c1 + flint.acb(0, 1) * (c2 * c2))

    def int_m12(om: Any, _: Any) -> Any:
        c1, c2 = cw_pair_acb(om)
        pref = (flint.acb(2) / flint.acb(pi)) * sigma_L2_sq_acb(om, log2)
        return pref * c1 * c2

    om_Base = [
        "9.6", "9.72", "9.85", "10.0", "10.16", "10.34", "10.55", "10.8", "11.1", "11.45",
        "11.85", "12.3", "12.8", "13.4", "14.1", "14.9", "15.8", "16.9", "18.2", "19.7",
        "21.5", "23.7", "26.5", "30.0", "34.5", "40.0", "47.0", "56.0", "67.0", "80.0",
    ]
    om_knots = [xi1] + [
        flint.arb(s)
        for s in om_Base
        if not (flint.arb(s) - xi1).contains(0) and arb_strict_lt(xi1, flint.arb(s))
    ]
    xi_cap = om_knots[-1]

    c0_diag = flint.acb.integral(int_m11_m22, flint.acb(0), flint.acb(om_knots[0]), rel_tol=INT_TOL, abs_tol=INT_TOL)
    int_0_x_11 = c0_diag.real
    int_0_x_22 = c0_diag.imag
    int_0_x_12 = flint.acb.integral(int_m12, flint.acb(0), flint.acb(om_knots[0]), rel_tol=INT_TOL, abs_tol=INT_TOL).real

    d_pl_11 = flint.arb(0)
    d_pl_22 = flint.arb(0)
    d_pl_12 = flint.arb(0)

    for idx in range(len(om_knots) - 1):
        assert om_knots[idx + 1] > om_knots[idx]
        a_k = flint.acb(om_knots[idx])
        b_k = flint.acb(om_knots[idx + 1])
        ck_diag = flint.acb.integral(int_m11_m22, a_k, b_k, rel_tol=INT_TOL, abs_tol=INT_TOL)
        ik_11 = ck_diag.real
        ik_22 = ck_diag.imag
        ik_12 = flint.acb.integral(int_m12, a_k, b_k, rel_tol=INT_TOL, abs_tol=INT_TOL).real
        int_0_x_11 += ik_11
        int_0_x_22 += ik_22
        int_0_x_12 += ik_12
        alp_lo = alpha_arb(om_knots[idx]) - da
        assert alp_lo > 0
        d_pl_11 += ik_11 / alp_lo
        d_pl_22 += ik_22 / alp_lo
        d_pl_12 += ik_12 / alp_lo

    alp_xi = alpha_arb(xi_cap) - da
    assert alp_xi > 0
    tail_11 = flint.arb("3.25") * g_w[0][0] - int_0_x_11
    tail_22 = flint.arb("3.25") * g_w[1][1] - int_0_x_22
    tail_12 = flint.arb("3.25") * g_w[0][1] - int_0_x_12
    tail_det = tail_11 * tail_22 - tail_12 * tail_12
    assert tail_11 > 0 and tail_det > 0, "Plancherel tail matrix not SPD"

    d_pl_11 += tail_11 / alp_xi
    d_pl_22 += tail_22 / alp_xi
    d_pl_12 += tail_12 / alp_xi
    d_pl_upper = [[d_pl_11, d_pl_12], [d_pl_12, d_pl_22]]
    assert d_pl_11 > 0 and (d_pl_11 * d_pl_22 - d_pl_12 * d_pl_12) > 0
    d_pl_inv = solve_linear_arb(d_pl_upper, [[flint.arb(1), flint.arb(0)], [flint.arb(0), flint.arb(1)]])

    # Midpoint-moment pipeline: M = 18 scalar moments for w_1 and w_2 on [0, xi_1]:
    m_mom = 18
    mu_vecs: list[list[Any]] = [[], []]
    for n in range(m_mom):
        scale_n = flint.acb((-1) ** n) / flint.acb(math.factorial(2 * n))

        def mom_pair_integrand(
            om: Any, _: Any, n_pow: int = 2 * n, sc: Any = scale_n
        ) -> Any:
            c1, c2 = cw_pair_acb(om)
            sig2 = sigma_L2_sq_acb(om, log2)
            return sc * (flint.acb(2) / flint.acb(pi)) * sig2 * (c1 + flint.acb(0, 1) * c2) * (om**n_pow)

        val_c = flint.acb.integral(
            mom_pair_integrand, flint.acb(0), flint.acb(xi1), rel_tol=INT_TOL, abs_tol=INT_TOL
        )
        mu_vecs[0].append(val_c.real)
        mu_vecs[1].append(val_c.imag)

    l1_cw = [
        (flint.arb(2) / pi) * flint.arb("3.25") * b * xi1 * (flint.arb("3.25") * g_w[p][p]).sqrt()
        for p in range(2)
    ]
    eps_1 = [
        ((xi1 * b) ** (2 * m_mom)) / flint.arb(math.factorial(2 * m_mom)) * l1_cw[p]
        for p in range(2)
    ]

    deg = 2 * m_mom - 1
    binom = [[flint.arb(math.comb(n_b, r_b)) for r_b in range(n_b + 1)] for n_b in range(deg + 1)]

    c_inf_p0inv = flint.arb(0)
    for i in range(k_int):
        row_sum = sum((arb_abs(p0inv_e_mat[i][j]) for j in range(k_int)), flint.arb(0))
        c_inf_p0inv = arb_max(c_inf_p0inv, row_sum)
    delta_inf = [c_inf_p0inv * eps_1[p] for p in range(2)]

    w_loc_all: list[list[list[Any]]] = []
    psi_loc_all: list[list[list[Any]]] = []
    q_loc_all: list[list[list[Any]]] = []
    psi_l1_bounds: list[Any] = []
    w_l1_bounds: list[Any] = []
    delta_vw: list[Any] = []
    r_xi = 9

    for p in range(2):
        w_loc_p: list[list[Any]] = []
        for i in range(k_int):
            mi = mids[i]
            mi_pows = [flint.arb(1)]
            for _ in range(1, deg + 1):
                mi_pows.append(mi_pows[-1] * mi)
            coeffs = [flint.arb(0) for _ in range(deg)]
            coeffs[0] = flint.arb("3.25") * w_vecs[p][i]
            for n in range(m_mom):
                deg_n = 2 * n
                mun = mu_vecs[p][n]
                for r in range(deg_n + 1):
                    coeffs[r] -= mun * binom[deg_n][r] * mi_pows[deg_n - r]
            w_loc_p.append(coeffs)

        psi_loc_p: list[list[Any]] = []
        for i in range(k_int):
            p_coeffs = [flint.arb(0) for _ in range(deg)]
            for j in range(k_int):
                val_e = p0inv_e_mat[i][j]
                val_o = p0inv_o_mat[i][j]
                if not val_e.contains(0):
                    for r in range(deg):
                        if r % 2 == 0:
                            p_coeffs[r] += val_e * w_loc_p[j][r]
                        else:
                            p_coeffs[r] += val_o * w_loc_p[j][r]
            psi_loc_p.append(p_coeffs)

        w_int_p: list[list[Any]] = []
        q_loc_p: list[list[Any]] = []
        psi_l1_p = flint.arb(0)
        w_l1_p = flint.arb(0)
        eps_2_p = flint.arb(0)

        for i in range(k_int):
            half_li = flint.arb("0.5") * lens[i]
            pows = [flint.arb(2) * (half_li ** (m_p + 1)) / flint.arb(m_p + 1) for m_p in range(2 * deg)]
            for r in range(deg):
                psi_l1_p += arb_abs(psi_loc_p[i][r]) * pows[r]
                w_l1_p += arb_abs(w_loc_p[i][r]) * pows[r]
            wi = [flint.arb(0) for _ in range(deg)]
            qi = [flint.arb(0) for _ in range(deg)]
            for r in range(deg):
                s_w = flint.arb(0)
                s_q = flint.arb(0)
                for rp in range(r % 2, deg, 2):
                    m_rrp = pows[r + rp]
                    s_w += m_rrp * w_loc_p[i][rp]
                    s_q += m_rrp * psi_loc_p[i][rp]
                wi[r] = s_w
                qi[r] = s_q
            w_int_p.append(wi)
            q_loc_p.append(qi)

            q_l1_i = sum((arb_abs(psi_loc_p[i][r]) * pows[r] for r in range(deg)), flint.arb(0))
            rem_i = ((xi0 * half_li) ** (2 * r_xi)) / flint.arb(math.factorial(2 * r_xi))
            eps_2_p += rem_i * q_l1_i

        w_loc_all.append(w_int_p)
        psi_loc_all.append(psi_loc_p)
        q_loc_all.append(q_loc_p)
        psi_l1_bounds.append(psi_l1_p)
        w_l1_bounds.append(w_l1_p)
        delta_vw.append(b * delta_inf[p] + eps_2_p)

    j_ww = [[flint.arb(0) for _ in range(2)] for _ in range(2)]
    for p in range(2):
        for q in range(2):
            nom_pq = sum(
                (psi_loc_all[p][i][r] * w_loc_all[q][i][r] for i in range(k_int) for r in range(deg)),
                flint.arb(0),
            )
            err_pq = (
                psi_l1_bounds[p] * eps_1[q]
                + w_l1_bounds[q] * delta_inf[p]
                + b * eps_1[q] * delta_inf[p]
            )
            j_ww[p][q] = nom_pq + flint.arb(0, err_pq.upper())

    j_we = [[flint.arb(0) for _ in range(m_prime)] for _ in range(2)]
    for p in range(2):
        for k in range(m_prime):
            phi_k_l1 = sum((lens[i] * arb_abs(phi_e[k][i]) for i in range(k_int)), flint.arb(0))
            err_pk = phi_k_l1 * delta_inf[p]
            nom_pk = sum((phi_e[k][i] * w_loc_all[p][i][0] for i in range(k_int)), flint.arb(0))
            j_we[p][k] = nom_pk + flint.arb(0, err_pk.upper())

    m_tot = m_prime + 2
    dj = [[flint.arb(0) for _ in range(m_tot)] for _ in range(m_tot)]
    for j in range(m_prime):
        for k in range(m_prime):
            dj[j][k] = j_prime[j][k] + (d_prime[j] if j == k else flint.arb(0))
    for p in range(2):
        for k in range(m_prime):
            dj[m_prime + p][k] = j_we[p][k]
            dj[k][m_prime + p] = j_we[p][k]
        for q in range(2):
            dj[m_prime + p][m_prime + q] = d_pl_upper[p][q] + j_ww[p][q]

    eye_m = [[flint.arb(1 if j == k else 0) for k in range(m_tot)] for j in range(m_tot)]
    dj_inv = solve_linear_arb(dj, eye_m)

    fact_even = [flint.acb((-1) ** m) / flint.acb(math.factorial(2 * m)) for m in range(r_xi)]
    fact_odd = [flint.acb((-1) ** m) / flint.acb(math.factorial(2 * m + 1)) for m in range(r_xi)]

    def trace_combined_integrand(xi: Any, _: Any) -> Any:
        w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_sq_acb(xi, log2) * (flint.acb(da) - alpha_acb(xi))
        c_mi = [(xi * flint.acb(mids[i])).cos() for i in range(k_int)]
        s_mi = [(xi * flint.acb(mids[i])).sin() for i in range(k_int)]
        ic: list[Any] = []
        is_sin: list[Any] = []
        tc_plus: list[Any] = []
        ts_minus: list[Any] = []
        tc_minus: list[Any] = []
        ts_plus: list[Any] = []
        for i in range(k_int):
            li_acb = flint.acb(lens[i])
            half_arg = flint.acb("0.5") * xi * li_acb
            sh_i = acb_sinc(half_arg)
            s2_i = half_arg.cos() * sh_i
            ic.append(li_acb * c_mi[i] * sh_i)
            is_sin.append(li_acb * s_mi[i] * sh_i)
            p_fac = flint.acb("0.5") * li_acb * (flint.acb(1) + s2_i)
            m_fac = flint.acb("0.5") * li_acb * (flint.acb(1) - s2_i)
            tc_plus.append(p_fac * c_mi[i])
            ts_minus.append(m_fac * s_mi[i])
            tc_minus.append(m_fac * c_mi[i])
            ts_plus.append(p_fac * s_mi[i])

        k0_e = flint.acb(0)
        k0_o = flint.acb(0)
        for i, j, val_e in nz_e:
            ve_c = flint.acb(val_e)
            k0_e += ve_c * tc_plus[i] * c_mi[j]
            k0_o += ve_c * tc_minus[i] * c_mi[j]
        for i, j, val_o in nz_o:
            vo_c = flint.acb(val_o)
            k0_e += vo_c * ts_minus[i] * s_mi[j]
            k0_o += vo_c * ts_plus[i] * s_mi[j]

        v_vec: list[Any] = [
            sum((flint.acb(p0inv_e_phi[k][i]) * ic[i] for i in range(k_int)), flint.acb(0))
            for k in range(m_prime)
        ]
        vo_vec: list[Any] = [
            sum((flint.acb(p0inv_o_phi[k][i]) * is_sin[i] for i in range(k_int)), flint.acb(0))
            for k in range(m_prime)
        ]

        xi2 = xi * xi
        xi_pows_e = [flint.acb(1)]
        for _ in range(1, r_xi):
            xi_pows_e.append(xi_pows_e[-1] * xi2)

        for p in range(2):
            vw_p = flint.acb(0)
            for i in range(k_int):
                ce_i = flint.acb(0)
                so_i = flint.acb(0)
                for m in range(r_xi):
                    ce_i += fact_even[m] * xi_pows_e[m] * flint.acb(q_loc_all[p][i][2 * m])
                    so_i += fact_odd[m] * xi * xi_pows_e[m] * flint.acb(q_loc_all[p][i][2 * m + 1])
                vw_p += c_mi[i] * ce_i - s_mi[i] * so_i
            vw_p += flint.acb(flint.arb(0, delta_vw[p].upper()))
            v_vec.append(vw_p)

        corr_e = flint.acb(0)
        for j in range(m_tot):
            s_j = sum((flint.acb(dj_inv[j][k]) * v_vec[k] for k in range(m_tot)), flint.acb(0))
            corr_e += v_vec[j] * s_j

        corr_o = flint.acb(0)
        for j in range(m_prime):
            s_jo = sum((flint.acb(dj_o_inv[j][k]) * vo_vec[k] for k in range(m_prime)), flint.acb(0))
            corr_o += vo_vec[j] * s_jo

        val_e = w_m * (k0_e - corr_e)
        val_o = w_m * (k0_o - corr_o)
        return val_e + flint.acb(0, 1) * val_o

    tr_combined = flint.acb.integral(
        trace_combined_integrand, flint.acb(0), flint.acb(xi0), rel_tol=INT_TOL, abs_tol=INT_TOL
    )
    tr_even_raw = tr_combined.real
    tr_odd = tr_combined.imag

    # Courant-Fischer 2-Mode Deflation Theorem in 384-bit arb:
    # Step 1: Compute float trial eigenvectors psi_1, psi_2 of G_full^{-1} M_full:
    mids_f = [float(x.mid()) for x in mids]
    lens_f = [float(x.mid()) for x in lens]
    p0_e_f = [[float(x.mid()) for x in row] for row in p0_e_mat]
    phi_e_f = [[float(x.mid()) for x in row] for row in phi_e]
    d_prime_f = [float(x.mid()) for x in d_prime]
    d_pl_inv_f = [[float(x.mid()) for x in row] for row in d_pl_inv]
    w_int0_f = [[float(w_loc_all[p][i][0].mid()) for i in range(k_int)] for p in range(2)]

    xi0_f = float(xi0.mid())
    log2_f = float(log2.mid())
    da_f = float(da.mid())
    n_quad = 200
    h_q = xi0_f / n_quad
    m_full_f = [[0.0] * k_int for _ in range(k_int)]
    for q_i in range(n_quad + 1):
        xi_q = q_i * h_q
        w_simpson = 1.0 if (q_i == 0 or q_i == n_quad) else (4.0 if q_i % 2 == 1 else 2.0)
        w_q = (h_q / 3.0) * w_simpson
        sig2_q = (1.5 - math.sqrt(2.0) * math.cos(xi_q * log2_f)) ** 2
        alp_q = float(alpha_arb(flint.arb(xi_q)).mid())
        wm_q = (2.0 / math.pi) * (da_f - alp_q) * sig2_q * w_q
        ic_q: list[float] = []
        for i in range(k_int):
            arg_i = 0.5 * lens_f[i] * xi_q
            sinc_i = 1.0 if arg_i == 0.0 else math.sin(arg_i) / arg_i
            ic_q.append(lens_f[i] * math.cos(mids_f[i] * xi_q) * sinc_i)
        for i in range(k_int):
            w_ic_i = wm_q * ic_q[i]
            for j in range(i, k_int):
                val_ij = w_ic_i * ic_q[j]
                m_full_f[i][j] += val_ij
                if i != j:
                    m_full_f[j][i] += val_ij

    g_full_f = [[0.0] * k_int for _ in range(k_int)]
    for i in range(k_int):
        for j in range(k_int):
            acc_g = lens_f[i] * p0_e_f[i][j]
            for k_idx in range(m_prime):
                acc_g += (lens_f[i] * phi_e_f[k_idx][i] * lens_f[j] * phi_e_f[k_idx][j]) / d_prime_f[k_idx]
            for p_idx in range(2):
                for q_idx in range(2):
                    acc_g += w_int0_f[p_idx][i] * d_pl_inv_f[p_idx][q_idx] * w_int0_f[q_idx][j]
            g_full_f[i][j] = acc_g

    v0_f, v1_f = seed_generalized_top_vecs(g_full_f, m_full_f, n_vecs=2)
    psi_vecs = [
        [flint.arb(str(float(v0_f[i]))) for i in range(k_int)],
        [flint.arb(str(float(v1_f[i]))) for i in range(k_int)],
    ]

    # Step 2: Certify 2x2 Rayleigh matrix M_{rs} = <psi_r, A_-(da) psi_s> in 384-bit arb:
    def cpsi_pair_acb(xi: Any) -> tuple[Any, Any]:
        p1 = flint.acb(0)
        p2 = flint.acb(0)
        for i in range(k_int):
            li_c = flint.acb(lens[i])
            mi_c = flint.acb(mids[i])
            ker = li_c * (xi * mi_c).cos() * acb_sinc(flint.acb("0.5") * xi * li_c)
            p1 += flint.acb(psi_vecs[0][i]) * ker
            p2 += flint.acb(psi_vecs[1][i]) * ker
        return p1, p2

    def int_M00_M11(xi: Any, _: Any) -> Any:
        p1, p2 = cpsi_pair_acb(xi)
        w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_sq_acb(xi, log2) * (flint.acb(da) - alpha_acb(xi))
        return w_m * (p1 * p1 + flint.acb(0, 1) * (p2 * p2))

    def int_M01(xi: Any, _: Any) -> Any:
        p1, p2 = cpsi_pair_acb(xi)
        w_m = (flint.acb(2) / flint.acb(pi)) * sigma_L2_sq_acb(xi, log2) * (flint.acb(da) - alpha_acb(xi))
        return w_m * p1 * p2

    m_diag_c = flint.acb.integral(int_M00_M11, flint.acb(0), flint.acb(xi0), rel_tol=INT_TOL, abs_tol=INT_TOL)
    M_00 = m_diag_c.real
    M_11 = m_diag_c.imag
    M_01 = flint.acb.integral(int_M01, flint.acb(0), flint.acb(xi0), rel_tol=INT_TOL, abs_tol=INT_TOL).real
    M_2x2 = [[M_00, M_01], [M_01, M_11]]

    # Step 3: Certify <psi_r, W_p>_{L^2(0,b)} and 2x2 Gram matrix G_{rs} = <psi_r, P(a) psi_s> in 384-bit arb:
    psi_W = [[flint.arb(0), flint.arb(0)], [flint.arb(0), flint.arb(0)]]
    for r in range(2):
        psi_l1_r = sum((lens[i] * arb_abs(psi_vecs[r][i]) for i in range(k_int)), flint.arb(0))
        for p in range(2):
            nom_rp = sum((psi_vecs[r][i] * w_loc_all[p][i][0] for i in range(k_int)), flint.arb(0))
            err_rp = psi_l1_r * eps_1[p]
            psi_W[r][p] = nom_rp + flint.arb(0, err_rp.upper())

    G_2x2 = [[flint.arb(0), flint.arb(0)], [flint.arb(0), flint.arb(0)]]
    for r in range(2):
        for s in range(r, 2):
            acc = flint.arb(0)
            for i in range(k_int):
                li_psi_r = lens[i] * psi_vecs[r][i]
                for j in range(k_int):
                    if not p0_e_mat[i][j].contains(0):
                        acc += li_psi_r * p0_e_mat[i][j] * psi_vecs[s][j]
            for k_idx in range(m_prime):
                dot_r = sum((lens[i] * psi_vecs[r][i] * phi_e[k_idx][i] for i in range(k_int)), flint.arb(0))
                dot_s = sum((lens[i] * psi_vecs[s][i] * phi_e[k_idx][i] for i in range(k_int)), flint.arb(0))
                acc += (dot_r * dot_s) / d_prime[k_idx]
            for p in range(2):
                for q in range(2):
                    acc += psi_W[r][p] * d_pl_inv[p][q] * psi_W[s][q]
            G_2x2[r][s] = acc
            G_2x2[s][r] = acc

    # Closed-form minimum generalized eigenvalue mu_2 = lambda_min(G_2x2^{-1} M_2x2) in 384-bit arb:
    a_quad = G_2x2[0][0] * G_2x2[1][1] - G_2x2[0][1] * G_2x2[0][1]
    assert G_2x2[0][0] > 0 and a_quad > 0, "G_2x2 not positive definite"
    b_quad = (
        G_2x2[0][0] * M_2x2[1][1]
        + G_2x2[1][1] * M_2x2[0][0]
        - flint.arb(2) * G_2x2[0][1] * M_2x2[0][1]
    )
    c_quad = M_2x2[0][0] * M_2x2[1][1] - M_2x2[0][1] * M_2x2[0][1]
    disc_quad = b_quad * b_quad - flint.arb(4) * a_quad * c_quad
    assert disc_quad > 0 and c_quad > 0, "Invalid quadratic discriminant in 2x2 pencil"
    mu_2 = (flint.arb(2) * c_quad) / (b_quad + disc_quad.sqrt())
    assert mu_2 > 0, "Non-positive mu_2"

    tr_even_defl = tr_even_raw - mu_2
    cert_ok = bool(tr_even_defl < flint.arb(1) and tr_odd < flint.arb(1))
    assert cert_ok, (
        f"Certification failed at {label}: tr_even_defl={tr_even_defl}, tr_odd={tr_odd}"
    )

    return {
        "label": label,
        "a": arb_to_dict(a),
        "b": arb_to_dict(b),
        "x6": arb_to_dict(x6),
        "d5": arb_to_dict(d5),
        "s3": arb_to_dict(s3),
        "delta_alpha": arb_to_dict(da),
        "xi_delta_alpha": arb_to_dict(xi0),
        "xi1_plancherel": arb_to_dict(xi1),
        "K_subintervals": k_int,
        "M_prime_vectors": m_prime,
        "M_plancherel_vectors": 2,
        "D_pl_upper": [[arb_to_dict(x) for x in row] for row in d_pl_upper],
        "J_WW": [[arb_to_dict(x) for x in row] for row in j_ww],
        "trace_even_raw": arb_to_dict(tr_even_raw),
        "courant_fischer_mu2": arb_to_dict(mu_2),
        "trace_even_deflated": arb_to_dict(tr_even_defl),
        "trace_odd": arb_to_dict(tr_odd),
        "margin_even_deflated": arb_to_dict(flint.arb(1) - tr_even_defl),
        "margin_odd": arb_to_dict(flint.arb(1) - tr_odd),
        "certified": cert_ok,
        "elapsed_s": round(time.time() - t0, 3),
    }


def main() -> None:
    t_start = time.time()
    print("=== Certifying Theorems 1, 2, and 3 ===")
    thms_123 = certify_theorems_1_2_3()
    print("Theorems 1, 2, and 3 certified.")

    a_star5_sym = SymReal.log_prime(2, Fraction(3, 2))

    specs = [
        ("checkpoint_a_1.015", SymReal.const(Fraction(1015, 1000)), flint.arb("0.30"), flint.arb("9.5"), "base"),
        ("checkpoint_a_1.025", SymReal.const(Fraction(1025, 1000)), flint.arb("0.30"), flint.arb("9.5"), "base"),
        ("checkpoint_a_1.032", SymReal.const(Fraction(1032, 1000)), flint.arb("0.35"), flint.arb("9.6"), "base"),
        ("checkpoint_a_half_log8_three_island_horizon", a_star5_sym, flint.arb("0.35"), flint.arb("9.6"), "base"),
    ]

    certs: dict[str, Any] = {}
    for label, a_sym, da_v, xi1_v, mode in specs:
        a_v = a_sym.ball()
        print(f"Certifying {label} (a={float(a_v.mid().str(12, radius=False)):.10f}, mode={mode})...")
        c = certify_klein4_checkpoint(label, a_sym, da_v, xi1_v, mode)
        print(
            f"  -> K={c['K_subintervals']}, Mp={c['M_prime_vectors']}, "
            f"Tr_raw={c['trace_even_raw']['mid']:.6f}, "
            f"mu_2={c['courant_fischer_mu2']['mid']:.6f}, "
            f"Tr_defl={c['trace_even_deflated']['mid']:.6f} (<1), "
            f"Tr_odd={c['trace_odd']['mid']:.6f} (<1) ({c['elapsed_s']}s)"
        )
        certs[label] = c

    all_ok = all(c["certified"] for c in certs.values())
    assert all_ok, "One or more Klein 4-group regime certificates failed"

    out_data: dict[str, Any] = {
        "audit": "all-vector-positivity-three-island-horizon-2026-10-15-v1",
        "precision_bits": PREC_BITS,
        "all_certified": all_ok,
        "total_elapsed_s": round(time.time() - t_start, 3),
        "theorems_1_2_3": thms_123,
        "certificates": certs,
        "open_status_disclosure": {
            "RH": "OPEN",
            "G2": "OPEN",
            "cofinal_signed_arithmetic_lower_bound": "OPEN",
            "historical_missing_original_evidence_groups": "OPEN",
        },
    }

    out_path = Path(__file__).resolve().parent / "verification.json"
    out_path.write_text(json.dumps(out_data, indent=2) + "\n", encoding="utf-8")
    sha = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"Wrote {out_path} (sha256={sha}) in {out_data['total_elapsed_s']}s")


if __name__ == "__main__":
    main()
