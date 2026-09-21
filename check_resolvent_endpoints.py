"""Rational-model check of the corrected resolvent endpoint asymptotics.

This model contains no zeta zeros and tests no RH or Weil-form assertion.
The moderate numerical cutoff is not the much larger theorem cutoff.
"""
import json
from pathlib import Path
import numpy as np

SIGMA, A, M = 2.0, 4.0, 6
MU = 0.2 + 1.3j
P = 0.5 - MU.conjugate()
Q = SIGMA - 0.5


def hminus(s):
    return (SIGMA + A)**M / ((SIGMA - s) * (s + A)**M)


def endpoint_pair(length, cutoff):
    """Sum Fourier pairs in chunks, retaining the exact shell correction."""
    h0 = hminus(0.5)
    hs0 = np.array([(0.5 - P) * h0, h0], dtype=complex)
    raw = hs0 / length
    resolved = hs0 / (-MU.conjugate() * length)
    for start in range(1, 2 * cutoff + 1, 50000):
        n = np.arange(start, min(start + 50000, 2 * cutoff + 1))
        t = 2 * np.pi * n / length
        parity = np.where(n % 2, -1, 1)
        hp, hn = hminus(0.5 + 1j*t), hminus(0.5 - 1j*t)
        plus = np.array([(0.5 + 1j*t - P) * hp, hp])
        minus = np.array([(0.5 - 1j*t - P) * hn, hn])
        raw += np.sum(parity * (plus + minus), axis=1) / length
        resolved += np.sum(parity * (
            plus / (-1j*t - MU.conjugate())
            + minus / (1j*t - MU.conjugate())), axis=1) / length
    shell = 0j
    for start in range(cutoff + 1, 2 * cutoff + 1, 50000):
        n = np.arange(start, min(start + 50000, 2 * cutoff + 1))
        t = 2 * np.pi * n / length
        shell += np.sum(-MU.conjugate() / (t*t + MU.conjugate()**2)) / cutoff
    cauchy = np.array([SIGMA - P, 1], dtype=complex)
    corrected = resolved + (cauchy - raw) * shell
    return corrected, shell


def main():
    rows = []
    for length in (4, 6, 8, 10, 12, 14):
        cutoff = int(np.ceil(np.exp(length/2) * length**2))
        endpoints, shell = endpoint_pair(length, cutoff)
        scale = np.exp(MU.conjugate()*length/2) * (1-np.exp(-MU.conjugate()*length))
        minus_error = abs(scale * endpoints[1] / (-hminus(P)) - 1)
        plus_normalized = abs(endpoints[0] / (-np.exp(-Q*length/2)/(1-np.exp(-Q*length))))
        rows.append({"L": length, "K": cutoff,
                     "reflected_residue_relative_error": float(minus_error),
                     "unreflected_pole_normalized_magnitude": float(plus_normalized),
                     "endpoint_ratio_magnitude": float(abs(endpoints[1]/endpoints[0])),
                     "scaled_unreflected_endpoint_magnitude": float(abs(scale * endpoints[0])),
                     "shell_endpoint_magnitude": float(abs(shell))})
    result = {"scope": "Rational transforms only; no zeta zeros, Weil calculation, or RH evidence.",
              "parameters": {"sigma": SIGMA, "a": A, "M": M, "mu": [MU.real, MU.imag]},
              "cutoff": "ceil(exp(L/2)*L**2), deliberately smaller than the theorem cutoff",
              "rows": rows}
    path = Path(__file__).with_name("resolvent_endpoint_checks.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
