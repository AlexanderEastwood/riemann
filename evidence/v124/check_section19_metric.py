"""Finite first-slot-linear metric checks; rational model, not zeta zeros.

The model has a length-two Jordan chain at mu and one further eigenvector.
It tests exact source/shell annihilation, the pulled-back Lyapunov identity,
the commutator variance formula, and the compressed-generator source.
Floating-point checks are not proofs or evidence for RH.
"""
import json
from pathlib import Path
import numpy as np


def main():
    rows = []
    for length in (8.0, 16.0, 32.0):
        band = 3.0
        core = int(np.floor(band * length / (2 * np.pi)))
        shell = max(16, 4 * core)
        n = np.arange(-2 * shell, 2 * shell + 1)
        t = 2 * np.pi * n / length
        phase = np.where(n % 2 == 0, 1.0, -1.0)
        z = phase / np.sqrt(length) / (2.0 + 1j * t)**3
        mu, nu = 0.23 + 0.7j, 0.37 + 1.4j
        jcore = np.column_stack((z / (1j * t - mu),
                                 z / (1j * t - mu)**2,
                                 z / (1j * t - nu)))
        b = np.diag([mu, mu, nu])
        b[0, 1] = 1
        eta = np.array([1.0, 0.0, 1.0])
        defect_coefficient = np.array([1.2 + 0.4j, -0.2 + 0.7j, 0.6 - 0.1j])
        c = np.where(np.abs(n) > shell, np.sqrt(length) / (2 * shell), 0.0)
        j = jcore + np.outer(c, defect_coefficient)
        r = (1j * np.outer(t * c, defect_coefficient)
             - np.outer(c, defect_coefficient @ b))
        y = np.outer(z, eta) + r
        p = np.diag((np.abs(t) <= band).astype(float))
        q = p @ z
        q /= np.linalg.norm(q)
        s = p - np.outer(q, q.conj())
        comm = t[:, None] * s - s * t[None, :]
        g = j.conj().T @ s @ j
        ell = g @ b + b.conj().T @ g
        budget = (-1j * j.conj().T @ comm @ j
                  - j.conj().T @ s @ y - y.conj().T @ s @ j)
        mean = np.vdot(q, t * q).real
        h = (t - mean) * q
        variance = np.linalg.norm(h)**2
        comp = s @ (t[:, None] * s)
        projected = s @ j
        new_source = -1j * np.outer(h, q.conj() @ j)
        values = {
            'graph_identity': np.linalg.norm(1j * t[:, None] * j - j @ b - y),
            'self_adjoint_metric': np.linalg.norm(s - s.conj().T),
            'projection_identity': np.linalg.norm(s @ s - s),
            'source_annihilation': np.linalg.norm(s @ z),
            'shell_graph_annihilation': np.linalg.norm(s @ r),
            'lyapunov_budget': np.linalg.norm(ell - budget),
            'commutator_only_budget': np.linalg.norm(ell + 1j * j.conj().T @ comm @ j),
            'commutator_variance': abs(np.linalg.norm(comm, 2)**2 - variance),
            'projected_graph_source': np.linalg.norm(1j * comp @ projected - projected @ b - new_source),
        }
        assert max(values.values()) < 1e-10, values
        eig = np.linalg.eigvalsh(g)
        assert eig[0] > 0
        denominator_bound = mu.real**2 + (band + abs(mu.imag))**2
        ratio = 1 - mu.real**2 / denominator_bound
        grid = np.linspace(-band, band, 1001)
        xi = 1 - (mu.real**2 + (grid - mu.imag)**2) / denominator_bound
        polynomial_errors = []
        for order in (0, 1, 2, 4):
            poly = ((-mu.real - 1j * (grid - mu.imag)) / denominator_bound
                    * sum(xi**j for j in range(order + 1)))
            resolvent = 1 / (1j * grid - mu)
            remainder = resolvent - poly
            identity_error = np.max(np.abs(remainder - resolvent * xi**(order + 1)))
            bound = ratio**(order + 1) / abs(mu.real)
            assert identity_error < 1e-12
            assert np.max(np.abs(remainder)) <= bound + 1e-12
            polynomial_errors.append({'m': order, 'identity_error': float(identity_error),
                                      'max_grid_error': float(np.max(np.abs(remainder))),
                                      'proved_upper_bound': float(bound)})
        rows.append({'L': length, 'core_index': core, 'shell_index': shell,
                     'errors': {k: float(v) for k, v in values.items()},
                     'pullback_min_eigenvalue': float(eig[0]),
                     'commutator_norm': float(np.sqrt(variance)),
                     'graph_error_norm': float(np.linalg.norm(r)),
                     'polynomial_resolvent_checks': polynomial_errors,
                     'source_free_lyapunov_norm': float(np.linalg.norm(ell, 2)),
                     'eigenvector_relative_defect': float(abs(ell[0, 0]) / g[0, 0].real)})
    result = {'scope': 'Rational-model finite algebra checks only; no zeta zeros, Weil positivity or RH claim.',
              'first_slot_linear': True, 'jordan_chain_length': 2, 'rows': rows}
    Path(__file__).with_name('section19_metric_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
