"""Exact admission checks for specified toy constructions, never an RH test.

The hyperbolic calculation checks a finite-dimensional trace numerator. It
does not construct an analytic flat trace on a global arithmetic space.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import isqrt, lcm, prod
from typing import Sequence


@dataclass(frozen=True)
class HyperbolicCase:
    label: int
    repetition: int
    rates: tuple[Fraction, ...]
    grading_shift: int


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def exterior_supertrace(eigenvalues: Sequence[Fraction]) -> Fraction:
    """Enumerate exterior powers, independently of the determinant product."""
    return sum(
        (Fraction((-1) ** degree) * prod(subset)
         for degree in range(len(eigenvalues) + 1)
         for subset in combinations(eigenvalues, degree)),
        Fraction(0),
    )


def check_hyperbolic(case: HyperbolicCase) -> dict[str, object]:
    if not 2 <= case.label <= 1000 or not 1 <= case.repetition <= 32:
        raise ValueError("label or repetition outside bounded check range")
    if not 1 <= len(case.rates) <= 3 or case.grading_shift not in (0, 1):
        raise ValueError("invalid hyperbolic-pair count or grading shift")
    if any(a <= 0 or a > 2 or a.denominator > 8 for a in case.rates):
        raise ValueError("rates must be positive bounded rationals")
    # Choose actual repetitions making every eigenvalue and half-density
    # rational. We record this m; it is not the input repetition index.
    m = 2 * lcm(*(a.denominator for a in case.rates)) * case.repetition
    eigenvalues: list[Fraction] = []
    for rate in case.rates:
        exponent = m * rate
        assert exponent.denominator == 1
        multiplier = Fraction(case.label ** exponent.numerator)
        eigenvalues.extend((1 / multiplier, multiplier))
    numerator = exterior_supertrace(eigenvalues)
    determinant = prod((1 - x for x in eigenvalues), start=Fraction(1))
    half_exponent = m * sum(case.rates, Fraction(0)) / 2
    assert half_exponent.denominator == 1
    half_density = Fraction(1, case.label ** half_exponent.numerator)
    weight = Fraction((-1) ** case.grading_shift) * numerator / abs(determinant) * half_density
    target = -Fraction(1, case.label ** (m // 2))
    exponent_condition = sum(case.rates, Fraction(0)) == 1
    sign_condition = (len(case.rates) + case.grading_shift) % 2 == 1
    return {
        "kind": "hyperbolic_local_weight",
        "dimension_real": 2 + 2 * len(case.rates),
        "label": case.label,
        "label_is_prime": is_prime(case.label),
        "actual_repetition_m": m,
        "rates": [str(a) for a in case.rates],
        "grading_shift": case.grading_shift,
        "normalized_weight_without_log_label": str(weight),
        "target_without_log_label": str(target),
        "exterior_trace_equals_determinant": numerator == determinant,
        "candidate_condition_holds": weight == target,
        "symbolic_rate_and_parity_condition": exponent_condition and sign_condition,
        "test_passed": numerator == determinant and (weight == target) == (exponent_condition and sign_condition),
        "scope": "Exact finite algebra only; composite labels can also match. No global trace, gamma/poles, positivity or RH transfer.",
    }


def passive_prime_factor(label: int, twice_shift: int) -> dict[str, object]:
    """At a=twice_shift/2, y=a+3/2, both Euler exponents are integers."""
    if not 2 <= label <= 1000 or not 1 <= twice_shift <= 8:
        raise ValueError("invalid bounded prime-factor parameters")
    ratio = (1 - Fraction(1, label ** (2 + twice_shift))) / (1 - Fraction(1, label**2))
    return {
        "kind": "independent_passive_prime_port",
        "label": label,
        "a": str(Fraction(twice_shift, 2)),
        "y": str(Fraction(twice_shift + 3, 2)),
        "ratio": str(ratio),
        "candidate_condition_holds": ratio <= 1,
        "test_passed": ratio > 1,
        "scope": "Rejects this independently passive Euler-factor architecture; says nothing against a coupled completed system.",
    }


def quotient_deck_map(label: int, power: int) -> dict[str, object]:
    if not 2 <= label <= 1000 or not 1 <= power <= 32:
        raise ValueError("invalid bounded quotient parameters")
    # Log coordinates for C*/label^Z: translation by power*log(label)
    # reduces to zero modulo its real period. The circle period stays implicit.
    shift_in_period_units = Fraction(power)
    reduced_shift = shift_in_period_units % 1
    return {
        "kind": "elliptic_deck_map",
        "label": label,
        "power": power,
        "reduced_shift_in_period_units": str(reduced_shift),
        "candidate_condition_holds": reduced_shift != 0,
        "test_passed": reduced_shift == 0,
        "scope": "Ordinary quotient map is the identity; labeled return/groupoid data would be extra structure.",
    }


def primitive_support(labels: Sequence[int]) -> dict[str, object]:
    """For a proposed primitive list, compare its log-derivative coefficients.

    Coefficients are represented in the independent prime-log basis. This
    detects both an extra log(6) primitive and duplicate log(4) weight.
    """
    if len(labels) > 32 or any(not 2 <= n <= 1000 for n in labels):
        raise ValueError("invalid primitive labels")
    primes = [n for n in labels if is_prime(n)]
    faults: list[dict[str, object]] = []
    for n in labels:
        if not is_prime(n):
            d, factors = n, {}
            for p in range(2, n + 1):
                while d % p == 0:
                    factors[str(p)] = factors.get(str(p), 0) + 1
                    d //= p
                if d == 1:
                    break
            faults.append({"primitive_label": n, "extra_log_coefficient": factors,
                           "type": "duplicates_prime_power" if len(factors) == 1 and int(next(iter(factors))) in primes else "extra_primitive_support"})
    repeated = len(set(labels)) != len(labels)
    return {
        "kind": "primitive_support",
        "labels": list(labels),
        "faults": faults,
        "repeated_primitive_labels": repeated,
        "candidate_condition_holds": not faults and not repeated,
        "scope": "Exact support check on the supplied finite primitive list, not a global construction or analytic continuation.",
    }


def run_checks(workers: int = 2) -> dict[str, object]:
    if not 1 <= workers <= 4:
        raise ValueError("workers must be in 1..4")
    labels = (2, 3, 5, 7, 11, 4, 6)
    designs = (((Fraction(1),), 0),
               ((Fraction(1), Fraction(1)), 0),
               ((Fraction(1, 2), Fraction(1, 2)), 1),
               ((Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)), 0))
    cases = [HyperbolicCase(p, m, rates, shift)
             for rates, shift in designs for p in labels for m in range(1, 5)]
    if workers == 1:
        rows = [check_hyperbolic(case) for case in cases]
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            rows = list(pool.map(check_hyperbolic, cases))
    rows.extend(passive_prime_factor(p, a2) for p in labels for a2 in (1, 2, 3))
    rows.extend(quotient_deck_map(p, k) for p in labels for k in range(1, 5))
    fixtures = (((2, 3, 5), True, False), ((2, 3, 4), False, False),
                ((2, 3, 6), False, False), ((2, 2, 3), False, True))
    for primitive_labels, expected_condition, expected_repeat in fixtures:
        row = primitive_support(primitive_labels)
        row['expected_candidate_condition'] = expected_condition
        row['expected_repeated_labels'] = expected_repeat
        row['test_passed'] = (row['candidate_condition_holds'] == expected_condition
                              and row['repeated_primitive_labels'] == expected_repeat)
        rows.append(row)
    return {
        "classification": "Exact local construction/admission checks; no RH candidate certified",
        "arithmetic": "Python Fraction and integers; no floating-point comparisons",
        "workers": workers,
        "case_count": len(rows),
        "all_checks_consistent": all(row["test_passed"] for row in rows),
        "controls": {
            "composite_labels": "Same local geometry with 4 or 6; local weight pass is insufficient to identify prime support",
            "dimension_lift": "Unit-rate 6D lift fails; chosen normalized rates/parity can restore weight algebra only",
            "davenport_heilbronn": "Not applicable to local determinant/deck/individual Euler-factor algebra: the analogue lacks the specified prime-product geometry. No generic completed-function positivity inference is tested or passed.",
            "ns94_ns100_ns101": "No circle-count or theta-positivity inference attempted; their broader symmetry-only warnings retained",
        },
        "rows": rows,
    }
