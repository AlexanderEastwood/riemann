#!/usr/bin/env python3
"""Numerical illustration only: sharp beta from Gaussian Perron residues.

No ground, head, window certificate or Weil tail is computed.  The left
Perron contour is retained in the identity and bounded analytically in
results.md; it is omitted in this floating-point illustration (<4e-18).
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

import mpmath as mp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'evidence/v124/g2_schur_cancellation'))
sys.path.insert(0, str(ROOT / 'evidence/diag_true_symbol'))
from beta_true import make_beta_true

US = ('0.25', '0.5', '0.75', '1', '1.25', '1.5', '2', '2.5', '3', '4')
SAVED = {
    3: (-.001, -.285, .005, .284, -.012, -.279, .272, -.259, .238, .119),
    4: (-.000, -.687, .001, .695, -.001, -.708, .728, -.757, .797, .935),
    6: (-.010, -.509, .029, .512, -.049, -.515, .520, -.527, .536, .562),
    8: (.000, -.131, -.001, .132, .002, -.134, .138, -.142, .148, .166),
}


def prime_powers(limit: int) -> list[tuple[int, int]]:
    """Return (prime power, base prime), independently of legacy pairs()."""
    primes: list[int] = []
    for n in range(2, limit + 1):
        if all(n % p for p in primes if p * p <= n):
            primes.append(n)
    return sorted((p ** k, p) for p in primes
                  for k in range(1, limit.bit_length()) if p ** k <= limit)


def dec(value: Any) -> str:
    return str(mp.nstr(value, 42))


def gaussian_parts(lam: int, u: str, eps: Any,
                   zeros: list[Any], powers: list[tuple[int, int]]) -> dict[str, Any]:
    x = mp.mpf(lam * lam)
    length = mp.log(x)
    xi = 2 * mp.pi * mp.mpf(u) / length
    s = mp.mpf('.5') - 1j * xi
    def kernel(w: Any) -> Any:
        return mp.exp(length * w + eps * eps * w * w / 2) / w
    zero = 2 * mp.re(mp.fsum(kernel(rho - s) for rho in zeros))
    trivial = 2 * mp.re(mp.fsum(kernel(-2 * n - s) for n in range(1, 10)))
    pole = -2 * mp.re(mp.exp(length * (1 - s)) * mp.expm1(eps * eps * (1 - s) ** 2 / 2) / (1 - s))
    correction = mp.mpc(0)
    endpoint = mp.mpf(0)
    for n, p in powers:
        weight = mp.log(p) * mp.exp(-s * mp.log(n))
        if n == lam * lam:
            endpoint = mp.re(weight)
            continue
        # Evaluate 1-Phi stably on the inside and -Phi on the outside.
        distance = abs(mp.log(x / n)) / (eps * mp.sqrt(2))
        coefficient = mp.erfc(distance) / 2 * (1 if n < x else -1)
        correction += weight * coefficient
    desmooth = -2 * mp.re(correction)
    return {'xi': xi, 'zeros': zero, 'trivial': trivial, 'pole_adjustment': pole,
            'endpoint': endpoint, 'desmoothing_nonendpoint': desmooth,
            'sum_without_left_contour': zero + trivial + pole + endpoint + desmooth}


def sharp_parts(lam: int, u: str, gammas: list[Any]) -> dict[str, Any]:
    length = 2 * mp.log(lam)
    xi = 2 * mp.pi * mp.mpf(u) / length
    x = mp.mpf(lam * lam)
    sharp_zero = 2 * mp.fsum(mp.sin((g + xi) * length) / (g + xi)
                           + mp.sin((g - xi) * length) / (g - xi) for g in gammas)
    cesaro_zero = 2 * mp.fsum((1 - g / 680) * (mp.sin((g + xi) * length) / (g + xi)
                           + mp.sin((g - xi) * length) / (g - xi)) for g in gammas)
    trivial = -2 * mp.re(mp.fsum(mp.exp((-2 * n - mp.mpf('.5') + 1j * xi) * length)
                                / (2 * n + mp.mpf('.5') - 1j * xi) for n in range(1, 60)))
    endpoint_base = {3: 3, 4: 2, 6: None, 8: 2}[lam]
    endpoint = (mp.log(endpoint_base) / lam * mp.cos(xi * length)
                if endpoint_base else mp.mpf(0))
    return {'zeros_400_sharp': sharp_zero, 'zeros_400_height_cesaro': cesaro_zero,
            'trivial_sharp': trivial, 'endpoint': endpoint}


def run(bits: int, dps: int, eps_text: str) -> dict[str, Any]:
    ctx.prec = bits
    balls = acb.zeta_zeros(1, 400)
    count = arb(680).zeta_nzeros()
    assert count == 400
    assert all(z.real == arb('0.5') for z in balls)
    mp.mp.dps = dps
    gammas = [mp.mpf(z.imag.mid().str(dps + 5, radius=False)) for z in balls]
    zeros = [mp.mpf('.5') + 1j * sign * g for g in gammas for sign in (-1, 1)]
    powers = prime_powers(256)
    eps = mp.mpf(eps_text)
    rows: list[dict[str, Any]] = []
    summaries: list[dict[str, Any]] = []
    maximum = mp.mpf(0)
    for lam in (3, 4, 6, 8):
        beta, _ = make_beta_true(lam)
        for u, saved in zip(US, SAVED[lam]):
            parts = gaussian_parts(lam, u, eps, zeros, powers)
            direct = beta(parts['xi'])
            delta = abs(direct - parts['sum_without_left_contour'])
            maximum = max(maximum, delta)
            # The original output has three decimal places, not six.
            rounded_agreement = round(float(direct), 3) == saved
            assert rounded_agreement
            assert delta < mp.mpf('1e-6')
            legacy_xi = float(u) * 2 * math.pi / (2 * math.log(lam))
            legacy_error = abs(direct - beta(legacy_xi))
            sharp = sharp_parts(lam, u, gammas)
            rows.append({'lambda': lam, 'u': u, 'saved_3dp': saved,
                         'direct': dec(direct), 'gaussian_error': dec(delta),
                         'legacy_float_abscissa_error': dec(legacy_error),
                         'saved_rounding_agrees': rounded_agreement,
                         **{key: dec(value) for key, value in parts.items()},
                         **{key: dec(value) for key, value in sharp.items()},
                         'sharp_400_residual': dec(direct - sharp['zeros_400_sharp']
                             - sharp['trivial_sharp'] - sharp['endpoint']),
                         'cesaro_400_residual': dec(direct - sharp['zeros_400_height_cesaro']
                             - sharp['trivial_sharp'] - sharp['endpoint'])})
        length = 2 * mp.log(lam)
        c_raw = 4 * mp.fsum(mp.sin(g * length) / g for g in gammas)
        c_height = 4 * mp.fsum((1 - g / 680) * mp.sin(g * length) / g for g in gammas)
        c_index = 4 * mp.fsum((1 - mp.mpf(k) / 401) * mp.sin(g * length) / g
                              for k, g in enumerate(gammas, start=1))
        at_zero = gaussian_parts(lam, '0', eps, zeros, powers)
        endpoint = at_zero['endpoint']
        trivial0 = sharp_parts(lam, '0', gammas)['trivial_sharp']
        summaries.append({'lambda': lam, 'beta_zero': dec(beta(0)),
                          'archimedean_zero': dec(mp.digamma(mp.mpf(5) / 4) - mp.log(mp.pi)),
                          'endpoint_amplitude': dec(endpoint), 'trivial_zero': dec(trivial0),
                          'zero_sum_amplitude_reconstructed': dec(beta(0) - endpoint - trivial0),
                          'naive_400_raw': dec(c_raw), 'naive_400_height_cesaro': dec(c_height),
                          'naive_400_index_cesaro': dec(c_index)})
    return {'classification': 'NUMERICAL ILLUSTRATION, NOT A CERTIFICATE',
            'bits_zero_input': bits, 'mpmath_dps': dps, 'epsilon': eps_text,
            'number_of_positive_zeros': 400, 'N_680': count.str(10),
            'prime_power_sum_limit': 256, 'left_contour_real_part': -20,
            'left_contour_omitted_analytic_bound': '4e-18',
            'max_absolute_discrepancy': dec(maximum), 'rows': rows, 'summaries': summaries,
            'source_sha256': hashlib.sha256((ROOT / 'evidence/diag_true_symbol/selfsim_output.txt').read_bytes()).hexdigest()}


def main() -> None:
    for bits, dps, eps in ((192, 45, '.025'), (256, 65, '.03')):
        result = run(bits, dps, eps)
        path = OUT / f'check_b{bits}.json'
        path.write_text(json.dumps(result, indent=2) + '\n')
        print(f'{path.name}: {len(result["rows"])} rows, max discrepancy {result["max_absolute_discrepancy"]}', flush=True)
        print(json.dumps(result['summaries'], indent=2), flush=True)


if __name__ == '__main__':
    main()
