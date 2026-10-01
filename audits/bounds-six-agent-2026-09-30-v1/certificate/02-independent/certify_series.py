"""Independent fixed beta certificate; no digamma, gamma, or Euler-constant call.

Run with the repository .venv/bin/python. All numerical operations use Arb balls.
Digamma is evaluated by DLMF 5.7.6 with a proved monotone integral tail.
Euler's constant uses its harmonic/log defining limit and an explicit 1/M bound.
The continuum integral uses an exponential power series and geometric tail.
No favorable parameter search occurs: a=log(4), xi=1, m<16 only.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import flint
from flint import arb, ctx

BASE = Path(__file__).resolve().parent
SOURCE = Path('/private/tmp/riemann-prime-folding-review-20260930/manuscript/fixed_space_prime_action_v1.tex')
GAMMA_TERMS = 4096
DIGAMMA_TERMS = 1024
EXP_TERMS = 40


def fmt(x: arb) -> str:
    """Print an enclosing decimal ball, not an unqualified midpoint."""
    return x.str(40, radius=True, more=True)


def gamma_interval(m: int) -> arb:
    """0 < H_m-log(m)-gamma < 1/m by telescoping integral comparison."""
    harmonic = arb(0)
    for k in range(1, m + 1):
        harmonic += arb(1) / k
    upper = harmonic - arb(m).log()
    lower = upper - arb(1) / m
    return lower.union(upper)


def digamma_real(kmax: int, gamma: arb) -> tuple[arb, arb]:
    """Re psi(5/4+i/2)=-gamma+sum f(k), with integral <= tail <= integral+f(K).

    f(x)=1/(x+1)-(x+5/4)/((x+5/4)^2+1/4)
        =(1/4)/((x+1)(x+5/4))
         +(1/4)/((x+5/4)((x+5/4)^2+1/4)).
    Each positive summand decreases on x>=0, proving the integral test.
    """
    a, b2 = arb(5) / 4, arb(1) / 4
    partial = arb(0)
    for k in range(kmax):
        t = arb(k) + a
        # Positive decomposition avoids needless cancellation.
        partial += (a - 1) / ((k + 1) * t) + b2 / (t * (t * t + b2))
    t = arb(kmax) + a
    f_k = (a - 1) / ((kmax + 1) * t) + b2 / (t * (t * t + b2))
    integral = (t * t + b2).log() / 2 - arb(kmax + 1).log()
    assert integral > 0
    tail = integral.union(integral + f_k)
    return -gamma + partial + tail, tail


def strict_prime_powers(cutoff: int) -> list[tuple[int, int]]:
    """Enumerate m=p^j strictly below cutoff by elementary exact integers."""
    result: list[tuple[int, int]] = []
    for p in range(2, cutoff):
        if any(p % d == 0 for d in range(2, p)):
            continue
        m = p
        while m < cutoff:
            result.append((m, p))
            m *= p
    return sorted(result)


def continuum_series(length: arb, terms: int) -> tuple[arb, arb]:
    """Enclose integral_0^L exp(t/2)cos(t)dt using Re exp((1/2+i)t).

    Terms k=0..K-1 are Re(c^k)L^(k+1)/(k+1)!.
    For n>=K, absolute term <= L(|c|L)^n/(n+1)!.
    Consecutive ratios <= |c|L/(K+2)<1, giving the explicit geometric bound.
    """
    real, imag = arb(1), arb(0)
    power, factorial = length, 1
    result = arb(0)
    for k in range(terms):
        result += real * power / factorial
        real, imag = real / 2 - imag, real + imag / 2
        power *= length
        factorial *= k + 2
    radius_c = arb(5).sqrt() / 2
    u = radius_c * length
    ratio = u / (terms + 2)
    assert ratio < 1
    first = length * (u ** terms) / factorial
    error = first / (1 - ratio)
    # The union encloses every signed remainder in [-error,error].
    return result + (-error).union(error), error


def certify(bits: int) -> dict[str, Any]:
    """One complete proof replay at a fixed working precision."""
    ctx.prec = bits
    gamma = gamma_interval(GAMMA_TERMS)
    psi, psi_tail = digamma_real(DIGAMMA_TERMS, gamma)
    pp = strict_prime_powers(16)
    assert pp == [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3), (11, 11), (13, 13)]
    prime_sum = arb(0)
    components: list[dict[str, Any]] = []
    for m, p in pp:
        term = arb(p).log() / arb(m).sqrt() * arb(m).log().cos()
        prime_sum += term
        components.append({'m': m, 'prime_base': p, 'term': fmt(term)})
    length = arb(16).log()
    continuum, remainder = continuum_series(length, EXP_TERMS)
    # pi/log/cos are elementary Arb operations. No gamma-related function used.
    log_pi = arb.pi().log()
    beta = psi - log_pi - 2 * prime_sum + 2 * continuum
    historical_lower = -arb(64784909) / 100000000
    historical_upper = -arb(6321938) / 10000000
    threshold = -arb(3) / 5
    checks = {
        'strict_endpoint_16_excluded': all(m < 16 for m, _ in pp),
        'beta_above_reported_lower': bool(beta > historical_lower),
        'beta_below_reported_upper': bool(beta < historical_upper),
        'beta_below_minus_three_fifths': bool(beta < threshold),
    }
    return {
        'bits': bits,
        'gamma_interval': fmt(gamma),
        'digamma_real_interval': fmt(psi),
        'digamma_tail_interval': fmt(psi_tail),
        'log_pi': fmt(log_pi),
        'prime_powers': components,
        'prime_sum': fmt(prime_sum),
        'continuum_integral': fmt(continuum),
        'continuum_tail_bound': fmt(remainder),
        'beta_interval': fmt(beta),
        'beta_lower_endpoint_ball': fmt(beta.lower()),
        'beta_upper_endpoint_ball': fmt(beta.upper()),
        'threshold_margin': fmt(threshold - beta),
        'checks': checks,
    }


def main() -> None:
    """Save both fixed-precision certificates, including source hashes and scope."""
    results = [certify(128), certify(256)]
    record: dict[str, Any] = {
        'classification': 'Fixed existing-claim validation only; no RH or physical-window negativity claim',
        'reviewed_commit': '769359298fada57711b6895c4bde3fabe2cc5168',
        'source_file': str(SOURCE),
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_flint_version': flint.__version__,
        'independence': 'No direct certificate read. No digamma, gamma or Euler-constant library calls. Positive digamma series, harmonic-limit bound, and continuum Taylor series with explicit remainders.',
        'fixed_counts': {'gamma_harmonic_terms': GAMMA_TERMS, 'digamma_terms': DIGAMMA_TERMS, 'exponential_terms': EXP_TERMS},
        'external_formula_source': 'https://dlmf.nist.gov/5.7.E6',
        'historical_original_recovery': 'OPEN; this is newly generated replacement evidence only',
        'runs': results,
        'all_checks_pass': all(all(r['checks'].values()) for r in results),
    }
    (BASE / 'certificate.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, indent=2))
    if not record['all_checks_pass']:
        raise SystemExit('A stated gate failed. Do not reinterpret or search for a favorable point.')


if __name__ == '__main__':
    main()
