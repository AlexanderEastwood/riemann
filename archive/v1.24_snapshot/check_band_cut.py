"""Sharp-band transform checks; rational model only, no zeta/Weil claims."""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad

T = 3.0
mu = 0.23 + 0.7j


def source(t):
    return (2.0 + 1j * t) ** -3


def root(t):
    return source(t) / (1j * t - mu)


def integral(fun):
    return quad(lambda t: float(np.real(fun(t))), -T, T, epsabs=1e-12)[0] + 1j * quad(
        lambda t: float(np.imag(fun(t))), -T, T, epsabs=1e-12
    )[0]


alpha = integral(lambda t: root(t) * np.conj(source(t))) / integral(
    lambda t: abs(source(t)) ** 2
)
rows = []
for N in [8, 16, 32, 64, 128, 256]:
    L = 2 * np.pi * N / T  # fixed physical band, both endpoints exactly sampled
    n = np.arange(-N, N + 1)
    t = 2 * np.pi * n / L
    z, f = source(t), root(t)
    alpha_L = np.vdot(z, f) / np.vdot(z, z)  # first-slot-linear <f,z>
    a = f - alpha_L * z
    endpoint = lambda x: root(x) - alpha_L * source(x)
    orth = abs(np.vdot(z, a) / L)
    results = []
    for v in [0.5, -0.5, 0.23 + 0.7j]:
        q = a / (1j * t - v)
        alternating = np.sum((-1.0) ** n * q)
        H = -2 * np.sinh(v * L / 2) * alternating / L
        scaled = (-1.0) ** N * L * H / np.sinh(v * L / 2)
        C = endpoint(T) / (1j * T - v) + endpoint(-T) / (-1j * T - v)
        C_limit = (root(T) - alpha * source(T)) / (1j * T - v) + (
            root(-T) - alpha * source(-T)
        ) / (-1j * T - v)
        error = abs(scaled + C)
        # Exact telescoping second-difference representation of the remainder.
        delta2 = np.sum(q[:-2:2] - 2 * q[1:-1:2] + q[2::2])
        error_identity = abs(scaled + C + delta2)
        assert error_identity < 3e-13
        assert orth < 1e-13
        results.append({
            "v": [float(np.real(v)), float(np.imag(v))],
            "transform_abs": float(abs(H)),
            "scaled_remainder_abs": float(error),
            "L_times_scaled_remainder": float(L * error),
            "exact_second_difference_error": float(error_identity),
            "limiting_endpoint_coefficient_abs": float(abs(C_limit)),
        })
    # Direct numerical integration independently checks the finite transform
    # at the smallest size; it is only a convention check, not a certificate.
    direct_errors = []
    if N == 8:
        def physical(y):
            return np.sum(a * np.exp(1j * t * y)) / L
        for v in [0.5, -0.5]:
            direct = quad(lambda y: np.real(physical(y) * np.exp(-v*y)), -L/2, L/2, epsabs=1e-11)[0]
            direct += 1j * quad(lambda y: np.imag(physical(y) * np.exp(-v*y)), -L/2, L/2, epsabs=1e-11)[0]
            exact = -2 * np.sinh(v*L/2) * np.sum((-1.0)**n * a/(1j*t-v))/L
            direct_errors.append(float(abs(direct-exact)))
            assert abs(direct-exact) < 1e-10
    def transform(v):
        return -2 * np.sinh(v * L / 2) * np.sum((-1.0) ** n * a / (1j * t - v)) / L

    v = mu
    v_sharp = -np.conj(v)
    C_v = endpoint(T) / (1j * T - v) + endpoint(-T) / (-1j * T - v)
    C_sharp = endpoint(T) / (1j * T - v_sharp) + endpoint(-T) / (-1j * T - v_sharp)
    pair_exact = transform(v) * np.conj(transform(v_sharp))
    pair_edge = -(np.sinh(v * L / 2) ** 2) * C_v * np.conj(C_sharp) / L**2
    pair_relative_error = abs(pair_exact / pair_edge - 1)

    rows.append({"N": N, "L": float(L), "ordinary_norm_squared": float(np.vdot(a,a).real/L),
                 "source_orthogonality_error": float(orth), "alpha_error": float(abs(alpha_L-alpha)),
                 "direct_quadrature_errors": direct_errors, "tests": results,
                 "reflected_pair": {
                     "v": [float(v.real), float(v.imag)],
                     "v_sharp": [float(v_sharp.real), float(v_sharp.imag)],
                     "exact": [float(pair_exact.real), float(pair_exact.imag)],
                     "edge_leading": [float(pair_edge.real), float(pair_edge.imag)],
                     "relative_error": float(pair_relative_error),
                     "pair_sum": float(2 * pair_exact.real),
                     "edge_pair_sum": float(2 * pair_edge.real),
                     "endpoint_product_abs": float(abs(C_v * np.conj(C_sharp))),
                 }})

output = {"scope": "Rational-source convention checks only. No zeta zeros, Weil matrix, certified bounds or RH evidence.",
          "T": T, "mu": [mu.real, mu.imag], "rows": rows}
Path(__file__).with_name("band_cut_checks.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
