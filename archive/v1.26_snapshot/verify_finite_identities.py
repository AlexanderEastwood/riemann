#!/usr/bin/env python3
"""Check the v1 finite identities using complex vectors and a real CCM matrix.

Run beside check_sampler.py: python verify_finite_identities.py
These are reproducible floating-point algebra checks, not analytic proofs.
"""
from pathlib import Path
import json
import numpy as np
from check_sampler import weil_matrix


def main():
    length, cutoff = 4.0, 16
    w = weil_matrix(length, cutoff)
    n = np.arange(-cutoff, cutoff + 1)
    d = np.diag(2 * np.pi * n / length)
    eta = np.ones(len(n))
    beta = (d @ w - w @ d)[:, cutoff]
    comm = d @ w - w @ d
    ip = lambda x, y: np.vdot(y, x)  # first slot linear
    rng = np.random.default_rng(20260920)
    x = rng.normal(size=len(n)) + 1j * rng.normal(size=len(n))
    x /= np.linalg.norm(x)
    mu = 0.23 + 1.7j
    y = 1j * d @ x - mu * x
    b = ip(x, eta)
    a0 = 0.7
    t = w + a0 * np.eye(len(n))
    k0 = rng.normal(size=len(n))
    k = (k0 + k0[::-1]) / 2
    k += eta
    a = ip(k, eta)
    q = 1j * b / a
    residual = d @ w @ k
    mismatch = y - q * d @ k
    raw = rng.normal(size=w.shape) + 1j * rng.normal(size=w.shape)
    s = (raw + raw.conj().T) / 2
    v = rng.normal(size=len(n)) + 1j * rng.normal(size=len(n))
    v -= np.mean(v)  # eta(v)=0
    a_rho = 1j * d - mu * np.eye(len(n))
    kshell = cutoff // 2
    shell = np.where(np.abs(n) > kshell,
                     np.sqrt(length)/(2*kshell), 0.0)
    df, dbf = 1.2+0.4j, -0.2+0.7j
    graph = 1j * d @ shell * df - shell * dbf
    errors = {
        'physical_rank_two_commutator': np.linalg.norm(
            comm - np.outer(beta, eta) + np.outer(eta, beta)),
        'general_lyapunov': abs(mu.real * ip(s @ x, x)
            + np.real(ip(s @ y, x)) + 0.5j * ip((d @ s-s @ d) @ x, x)),
        'shifted_residual': abs(2*mu.real*ip(t @ x, x)
            + 2*np.real(ip(t @ y+1j*b*beta, x))),
        'candidate_decomposition': np.linalg.norm(t @ y+1j*b*beta
            -t @ mismatch-q*(residual+a0*d @ k)),
        'unshifted_pairing': abs(mu.real*ip(w @ x, x)
            +np.real(ip(w @ mismatch, x)) + np.real(q*ip(residual, x))),
        'boundary_annihilating_test': abs(ip(w @ y+1j*b*beta, v)
            -ip(w @ x, a_rho.conj().T @ v)),
        'graph_defect_pairing': abs(ip(w @ graph, v)
            -(1j*df*ip(d @ w @ shell, v)
              -1j*np.sqrt(length)*df*ip(beta, v)-dbf*ip(w @ shell, v))),
        'exact_shell_endpoint': abs(np.sum(shell)/np.sqrt(length)-1),
        'shell_derivative_norm': abs(np.linalg.norm(d @ shell)**2
            -np.pi**2*(14*kshell+9+1/kshell)/(3*length)),
    }
    result = {
        'description': 'Complex-vector algebra checks; floating point, not certified bounds.',
        'first_slot_linear': True,
        'L': length, 'N': cutoff,
        'absolute_errors': {k: float(v) for k,v in errors.items()},
        'tolerance': 1e-10,
        'passed': all(v < 1e-10 for v in errors.values()),
    }
    Path(__file__).with_name('finite_identity_checks.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    assert result['passed']


if __name__ == '__main__':
    main()
