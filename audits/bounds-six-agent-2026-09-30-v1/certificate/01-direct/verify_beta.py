#!/usr/bin/env python3
"""Fresh direct Arb certificate of one existing fixed-parameter beta claim.

No frequency/window search occurs. This is new evidence, not recovery of
certify_beta4_negative.py. All certificate inputs are integers or rationals;
flint's ball-valued log/sqrt/cos/sin and acb.digamma enclose every rounding error.
Run with the repository .venv Python; outputs.json is written beside this file.
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any

import flint
from flint import acb, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
SOURCE = Path('/private/tmp/riemann-prime-folding-review-20260930')
EXPECTED_COMMIT = '769359298fada57711b6895c4bde3fabe2cc5168'
PRECISIONS = (192, 320)
DECIMAL_DENOMINATOR = 10**45


def sha256(path: Path) -> str:
    """Hash exact source bytes rather than an extracted/transcribed equation."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prime_power_base(n: int) -> int | None:
    """Return the prime p if n=p**k, otherwise None, by exact integer division."""
    for candidate in range(2, n + 1):
        if n % candidate == 0:
            remainder = n
            while remainder % candidate == 0:
                remainder //= candidate
            return candidate if remainder == 1 else None
    return None


def fraction_from_flint(q: fmpq) -> Fraction:
    return Fraction(int(q.p), int(q.q))


def rational_json(q: Fraction) -> dict[str, str]:
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def exact_ball_endpoints(x: arb) -> tuple[Fraction, Fraction]:
    """lower/upper are directed dyadic endpoints, exported without float casts."""
    return fraction_from_flint(x.lower().fmpq()), fraction_from_flint(x.upper().fmpq())


def ball_json(x: arb) -> dict[str, Any]:
    lo, hi = exact_ball_endpoints(x)
    return {'display_only': x.str(70), 'lower_dyadic': rational_json(lo),
            'upper_dyadic': rational_json(hi)}


def decimal_string(integer: int, places: int) -> str:
    """Format an exact rational integer/10**places, never a floating midpoint."""
    digits = str(abs(integer)).rjust(places + 1, '0')
    return ('-' if integer < 0 else '') + digits[:-places] + '.' + digits[-places:]


def outward_decimal_enclosure(x: arb) -> dict[str, Any]:
    lo, hi = exact_ball_endpoints(x)
    lower_n = (lo.numerator * DECIMAL_DENOMINATOR) // lo.denominator
    upper_n = -((-hi.numerator * DECIMAL_DENOMINATOR) // hi.denominator)
    lower = Fraction(lower_n, DECIMAL_DENOMINATOR)
    upper = Fraction(upper_n, DECIMAL_DENOMINATOR)
    # The comparisons certify strict inequalities for every value in x.
    assert x > arb(fmpq(lower.numerator, lower.denominator))
    assert x < arb(fmpq(upper.numerator, upper.denominator))
    return {'lower': rational_json(lower), 'upper': rational_json(upper),
            'lower_decimal_exact': decimal_string(lower_n, 45),
            'upper_decimal_exact': decimal_string(upper_n, 45), 'strict': True}


def evaluate(bits: int) -> dict[str, Any]:
    ctx.prec = bits
    powers = [(m, prime_power_base(m)) for m in range(2, 16)]
    powers = [(m, p) for m, p in powers if p is not None]
    assert powers == [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7),
                      (8, 2), (9, 3), (11, 11), (13, 13)]
    assert prime_power_base(16) == 2 and all(m < 16 for m, _ in powers)

    z = acb(fmpq(5, 4), fmpq(1, 2))
    psi_real = z.digamma().real
    log_pi = arb.pi().log()
    archimedean = psi_real - log_pi
    terms: list[dict[str, Any]] = []
    prime_sum = arb(0)
    for m, p in powers:
        term = 2 * arb(p).log() / arb(m).sqrt() * arb(m).log().cos()
        prime_sum += term
        terms.append({'m': m, 'prime_base': p, 'term': ball_json(term)})

    # L=2 log4=log16 exactly. An antiderivative of exp(t/2)cos(t) is
    # exp(t/2)*((1/2)cos(t)+sin(t))/(5/4). Endpoint zero contributes -4/5
    # after multiplying the integral by 2. exp(L/2)=4 exactly.
    length = arb(16).log()
    continuum = (16 * length.cos() + 32 * length.sin() - 4) / 5
    # Independent expression of the SAME integral via its complex exponential.
    rate = acb(fmpq(1, 2), 1)
    continuum_complex = (2 * ((rate * length).exp() - 1) / rate).real
    assert continuum.overlaps(continuum_complex)
    beta = archimedean - prime_sum + continuum
    low_historical = arb(fmpq(-64784909, 100000000))
    high_historical = arb(fmpq(-6321938, 10000000))
    threshold = arb(fmpq(-3, 5))
    gate = bool(beta > low_historical and beta < high_historical
                and high_historical < threshold)
    return {
        'precision_bits': bits, 'digamma_argument_exact': {'real': '5/4', 'imag': '1/2'},
        'strict_endpoint': 16, 'included_prime_powers': [m for m, _ in powers],
        'endpoint_16_excluded': True, 'terms': terms,
        'psi_real': ball_json(psi_real), 'log_pi': ball_json(log_pi),
        'archimedean': ball_json(archimedean), 'prime_sum_with_factor_two': ball_json(prime_sum),
        'continuum_with_factor_two': ball_json(continuum),
        'continuum_complex_expression': ball_json(continuum_complex),
        'continuum_expressions_overlap': True, 'beta': ball_json(beta),
        'outward_rational_enclosure': outward_decimal_enclosure(beta),
        'historical_reported_interval_verified': gate,
        'beta_strictly_below_minus_three_fifths': bool(beta < threshold),
    }


def main() -> None:
    commit = subprocess.check_output(['git', '-C', str(SOURCE), 'rev-parse', 'HEAD'],
                                     text=True).strip()
    assert commit == EXPECTED_COMMIT, 'Source commit changed; review before replay.'
    manuscript = SOURCE / 'manuscript/fixed_space_prime_action_v1.tex'
    text = manuscript.read_text()
    for marker in ('eq:v130-r-symbol', 'eq:v130-beta', 'prop:v132-global-index'):
        assert marker in text
    previous_precision = ctx.prec
    try:
        runs = [evaluate(bits) for bits in PRECISIONS]
    finally:
        ctx.prec = previous_precision
    sources = ['AGENTS.md', 'research-map.json', 'README.md', 'NEXT_STEPS.md',
               'evidence/MISSING.md', 'manuscript/fixed_space_prime_action_v1.tex',
               'evidence/ns38_archival_disclosure/claim_changes.json']
    output: dict[str, Any] = {
        'classification': 'Fresh certified computation of a fixed existing claim; not original-evidence recovery',
        'wall_check': 'Same open gap; NS38 / prop:v132-global-index; no new cofinal arithmetic estimate',
        'source_commit': commit, 'source_root': str(SOURCE),
        'source_sha256': {name: sha256(SOURCE / name) for name in sources},
        'verifier_sha256': sha256(Path(__file__)),
        'python_version': platform.python_version(), 'python_flint_version': flint.__version__,
        'method': 'Direct acb.digamma and Arb elementary functions, exact rational inputs, directed dyadic endpoint export',
        'formula': 'Re psi(5/4+i/2)-log(pi)-2 sum_(2<=m<16) Lambda(m)/sqrt(m)*cos(log(m))+(16 cos(log16)+32 sin(log16)-4)/5',
        'runs': runs,
        'same_outward_rational_interval_at_both_precisions':
            runs[0]['outward_rational_enclosure'] == runs[1]['outward_rational_enclosure'],
        'all_gates_pass': all(run['historical_reported_interval_verified'] and
                              run['beta_strictly_below_minus_three_fifths'] for run in runs),
        'scope': [
            'One point: a=log4, xi=1. No parameter scan.',
            'This validates the numerical premise of the full-line negative-index implication.',
            'It gives no compact physical-window negative test and does not contradict certified W4 positivity.',
            'Both historical original-evidence groups remain recovery OPEN.',
            'RH, G2 and cofinal signed-arithmetic lower bounds remain open.',
        ],
    }
    (HERE / 'outputs.json').write_text(json.dumps(output, indent=2) + '\n')
    assert output['all_gates_pass']
    assert output['same_outward_rational_interval_at_both_precisions']
    print(json.dumps({'all_gates_pass': output['all_gates_pass'],
                      'precisions': PRECISIONS,
                      'enclosure': runs[0]['outward_rational_enclosure']}, indent=2))


if __name__ == '__main__':
    main()
