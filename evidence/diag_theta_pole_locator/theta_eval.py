"""Diagnostic complete-theta M/C evaluator; quadrature is NOT certified.

Analytic truncation majorants are evaluated in ordinary mpmath arithmetic.
They are not outward-rounded interval enclosures.  The original integrals
are approximated by fixed composite Gauss-Legendre quadrature.  Precision,
lattice and quadrature replay is diagnostic, never a zero certificate.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

import mpmath as mp


def _gaussian_sum_tail(power: int, cutoff: int, b: Any) -> Any:
    """Majorize sum_(n>cutoff) n**power exp(-b*n*n), b real positive."""
    n = mp.mpf(cutoff + 1)
    ratio = ((n + 1) / n) ** power * mp.exp(-b * (2 * n + 1))
    if not (0 <= ratio < 1):
        raise ValueError("The geometric tail ratio is not below one")
    return n**power * mp.exp(-b * n * n) / (1 - ratio)


def _polynomial_exponential_max(power: Any, d: Any) -> Any:
    """The supremum of t**power exp(-d*t) for real t>=1."""
    t = max(mp.mpf(1), power / d)
    return t**power * mp.exp(-d * t)


def _envelopes(a: Any) -> tuple[Any, Any, Any]:
    """Return K0,K1,d for |phi^(j)(w+iv)|<=Kj exp(-d exp(2|w|))."""
    b = mp.pi * mp.cos(2 * a)
    d = b / 2
    sums: dict[int, Any] = {}
    for power in (2, 4, 6):
        sums[power] = mp.fsum(
            mp.mpf(n) ** power * mp.exp(-b * (n * n - 1))
            for n in range(1, 33)
        ) + mp.exp(b) * _gaussian_sum_tail(power, 32, b)
    k0 = (
        2 * mp.pi**2 * sums[4] * _polynomial_exponential_max(mp.mpf(9) / 4, d)
        + 3 * mp.pi * sums[2] * _polynomial_exponential_max(mp.mpf(5) / 4, d)
    )
    k1 = (
        4 * mp.pi**3 * sums[6] * _polynomial_exponential_max(mp.mpf(13) / 4, d)
        + 15 * mp.pi**2 * sums[4] * _polynomial_exponential_max(mp.mpf(9) / 4, d)
        + mp.mpf(15) / 2 * mp.pi * sums[2]
        * _polynomial_exponential_max(mp.mpf(5) / 4, d)
    )
    return k0, k1, d


def phi_pair(u: Any, cutoff: int) -> tuple[Any, Any]:
    """Evaluate a finite original lattice for phi and its analytic derivative.

    The negative-real half-plane is evaluated by exact full-kernel evenness;
    the separately bounded finite-lattice discrepancy is retained below.
    No derivative of the numerical reflection switch is taken.
    """
    derivative_sign = 1
    if mp.re(u) < 0:
        u = -u
        derivative_sign = -1
    t = mp.pi * mp.exp(2 * u)
    q = mp.exp(-t)
    term = q
    ratio = q**3
    step = q**2
    s2 = mp.mpc(0)
    s4 = mp.mpc(0)
    s6 = mp.mpc(0)
    for n in range(1, cutoff + 1):
        n2 = n * n
        s2 += n2 * term
        s4 += n2 * n2 * term
        s6 += n2 * n2 * n2 * term
        term *= ratio
        ratio *= step
    factor = mp.exp(u / 2)
    phi = factor * (2 * t * t * s4 - 3 * t * s2)
    derivative = factor * (
        -4 * t**3 * s6 + 15 * t * t * s4 - mp.mpf(15) / 2 * t * s2
    )
    return phi, derivative_sign * derivative


@lru_cache(maxsize=8)
def _quadrature_nodes(bits: int, order: int) -> tuple[tuple[Any, Any], ...]:
    """Cache ordinary high-precision nodes and weights; no enclosure claim."""
    with mp.workprec(bits):
        nodes, weights = mp.gauss_quadrature(order, "legendre")
        return tuple((nodes[j], weights[j]) for j in range(order))


def _error_metadata(z: Any, cutoff: int, radius: Any, normalization: Any) -> dict[str, Any]:
    """Analytic majorants, floating evaluations only, excluding quadrature error."""
    a = abs(mp.im(z))
    b = mp.pi * mp.cos(2 * a)
    if b * (cutoff + 1) ** 2 < mp.mpf(13) / 4:
        raise ValueError("The uniform lattice-tail monotonicity condition fails")
    tails = {power: _gaussian_sum_tail(power, cutoff, b) for power in (2, 4, 6)}
    e0 = 2 * mp.pi**2 * tails[4] + 3 * mp.pi * tails[2]
    e1 = 4 * mp.pi**3 * tails[6] + 15 * mp.pi**2 * tails[4] + mp.mpf(15) / 2 * mp.pi * tails[2]
    k0, k1, d = _envelopes(a)
    l0 = k0 * mp.exp(-d)
    l1 = k1 * mp.exp(-d)
    product_error = 2 * l0 * e0 + e0 * e0
    derivative_product_error = 2 * (l0 * e1 + l1 * e0 + e0 * e1)
    lattice_m = 2 * radius * product_error
    lattice_c = 2 * radius**3 / 3 * product_error
    lattice_d = 2 * radius * derivative_product_error
    big_d = d * mp.exp(2 * radius)
    real_m = k0 * k0 * mp.exp(-big_d) / big_d
    real_c = real_m * (radius * radius + radius / big_d + 1 / (2 * big_d * big_d))
    real_d = 2 * k0 * k1 * mp.exp(-big_d) / big_d
    scale = abs(normalization)
    log_derivative = abs(4 * mp.pi * mp.exp(2 * z) - 9)
    return {
        "status": "analytic majorants evaluated as floating numbers; NOT interval bounds",
        "quadrature_error": "NOT bounded: fixed Gauss-Legendre approximation and replay only",
        "roundoff_error": "NOT bounded: ordinary mpmath arithmetic",
        "normalized_lattice_m": scale * lattice_m,
        "normalized_lattice_c": scale * lattice_c,
        "normalized_lattice_dm": scale * (lattice_d + log_derivative * lattice_m),
        "normalized_real_tail_m": scale * real_m,
        "normalized_real_tail_c": scale * real_c,
        "normalized_real_tail_dm": scale * (real_d + log_derivative * real_m),
        "phi_lattice_tail": e0,
        "phi_derivative_lattice_tail": e1,
        "envelope_K0": k0,
        "envelope_K1": k1,
        "envelope_d": d,
    }


def evaluate(z: Any, bits: int = 128, replay: bool = False) -> dict[str, Any]:
    """Return normalized m=B*M, c=B*C, dm=(B*M)' plus diagnostic metadata.

    Initial: 128 bits, lattice n<=24, GL48 per [0,1/8,1/4,1/2,1,2,4].
    Replay: 256 bits, lattice n<=32, GL96, extra final endpoint 9/2.
    The caller controls when an ORIGINAL evaluation is authorized.
    """
    if bits < 128:
        raise ValueError("This protocol requires at least 128 working bits")
    with mp.workprec(bits):
        z = mp.mpc(z)
        if abs(mp.re(z)) > 2 or abs(mp.im(z)) > mp.mpf(5) / 8:
            raise ValueError("Outside the registered evaluator range")
        cutoff = 32 if replay else 24
        order = 96 if replay else 48
        endpoints = [mp.mpf(0), mp.mpf(1) / 8, mp.mpf(1) / 4, mp.mpf(1) / 2,
                     mp.mpf(1), mp.mpf(2), mp.mpf(4)]
        if replay:
            endpoints.append(mp.mpf(9) / 2)
        normalization = mp.exp(2 * mp.pi * mp.exp(2 * z) - 9 * z) / (4 * mp.pi**4)
        values_m: list[Any] = []
        values_c: list[Any] = []
        values_d: list[Any] = []
        nodes = _quadrature_nodes(bits, order)
        for left, right in zip(endpoints[:-1], endpoints[1:]):
            half = (right - left) / 2
            center = (right + left) / 2
            for node, weight in nodes:
                s = center + half * node
                plus, dplus = phi_pair(s + z, cutoff)
                minus, dminus = phi_pair(s - z, cutoff)
                scaled_weight = 2 * half * weight * normalization
                product = scaled_weight * plus * minus
                values_m.append(product)
                values_c.append(s * s * product)
                values_d.append(scaled_weight * (dplus * minus - plus * dminus))
        m = mp.fsum(values_m)
        c = mp.fsum(values_c)
        dm = mp.fsum(values_d) + (4 * mp.pi * mp.exp(2 * z) - 9) * m
        return {
            "m": m,
            "c": c,
            "dm": dm,
            "metadata": {
                "classification": "diagnostic, not a certificate",
                "bits": bits,
                "lattice_cutoff": cutoff,
                "gauss_legendre_order_per_segment": order,
                "positive_half_segments": endpoints,
                "normalization": "B=exp(2*pi*exp(2*z)-9*z)/(4*pi^4), analytic and nonzero",
                "derivative": "dm=(B*M)' includes B' contribution",
                "majorants": _error_metadata(z, cutoff, endpoints[-1], normalization),
            },
        }
