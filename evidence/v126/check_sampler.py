#!/usr/bin/env python3
"""Finite CCM checks for the sampler compatibility note.

Requires numpy, scipy, mpmath. Run: python3 check_sampler.py
Outputs sampler_checks.json beside this file. Numerical checks are illustrative,
not proofs or certified interval bounds. No hypothetical off-line zero is used.
The test transform is H(s)=kappa(s)*zeta(s), a global Weil-radical output.
"""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.special import roots_legendre

SIGMA, A, M = 2.0, 4.0, 6
mp.mp.dps = 30


def prime_powers(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    powers, weights = [], []
    for p in np.flatnonzero(sieve):
        k = int(p)
        while k <= limit:
            powers.append(k)
            weights.append(np.log(p) / np.sqrt(k))
            k *= int(p)
    order = np.argsort(powers)
    return np.log(np.asarray(powers)[order]), np.asarray(weights)[order]


def weil_matrix(length, nmax, extra_nodes=0):
    """CCM real symmetric matrix, with the separate correct diagonal."""
    npos = np.arange(nmax + 1)
    tpos = 2*np.pi*npos / length
    nodes, weights = roots_legendre(2*nmax + 300 + extra_nodes)
    y = (nodes + 1)*length/2
    w = weights*length/2
    rho = np.exp(y/2) / (2*np.sinh(y))
    sin = np.sin(tpos[:, None]*y)
    cos = np.cos(tpos[:, None]*y)
    jumps, prime_w = prime_powers(int(np.floor(np.exp(length))))
    phase = tpos[:, None]*jumps
    point_b = 32*length*np.sinh(length/4)**2*npos / (length**2 + 16*np.pi**2*npos**2)
    bpos = point_b + (sin @ (w*rho) + np.sin(phase) @ prime_w)/np.pi
    pole_diag = (32*length*np.sinh(length/4)**2
                 * (length**2-16*np.pi**2*npos**2)
                 / (length**2+16*np.pi**2*npos**2)**2)
    prime_diag = 2*np.cos(phase) @ ((1-jumps/length)*prime_w)
    arch_diag = ((2*(1-y/length)*cos - 2*np.exp(-y/2)) @ (w*rho)
                 + np.log(4*np.pi) + float(mp.euler)
                 + np.log(np.tanh(length/2)))
    diagpos = pole_diag-prime_diag-arch_diag
    b = np.concatenate((-bpos[:0:-1], bpos))
    diag = np.concatenate((diagpos[:0:-1], diagpos))
    n = np.arange(-nmax, nmax+1)
    distance = n[:, None]-n[None, :]
    matrix = np.divide(b[:, None]-b[None, :], distance,
                       out=np.zeros(distance.shape), where=distance != 0)
    np.fill_diagonal(matrix, diag)
    return matrix


def hardy_samples(length, nmax):
    vals = []
    for n in range(nmax+1):
        s = mp.mpf('0.5') + 2j*mp.pi*n/length
        kappa = (SIGMA*(SIGMA+A)**M/(SIGMA-1)
                 * (s-1)/((s+A)**M*(SIGMA-s)))
        vals.append(complex(kappa*mp.zeta(s)))
    pos = np.array(vals)
    return np.concatenate((pos[:0:-1].conj(), pos))/np.sqrt(length)


def quadratic(w, x):
    return float(np.vdot(x, w @ x).real)


def main():
    nmax = 512
    target = float(SIGMA*mp.zeta(SIGMA))
    rows = []
    for length in [4.0, 6.0, 8.0, 10.0]:
        wfull = weil_matrix(length, nmax)
        samples = hardy_samples(length, nmax)
        for shell_start in [64, 128, 256]:
            cutoff = 2*shell_start
            sl = slice(nmax-cutoff, nmax+cutoff+1)
            w = wfull[sl, sl]
            n = np.arange(-cutoff, cutoff+1)
            raw = samples[sl]
            centered = raw * np.where(n % 2 == 0, 1, -1)
            shell = np.where(np.abs(n) > shell_start,
                             np.sqrt(length)/(2*shell_start), 0.0)
            delta = lambda x: complex(np.sum(x)/np.sqrt(length))
            defect = target-delta(centered)
            repaired = centered + defect*shell
            d_shell_norm2 = np.linalg.norm(2*np.pi*n/length*shell)**2
            exact_d_shell_norm2 = np.pi**2*(14*shell_start+9+1/shell_start)/(3*length)
            assert abs(delta(shell)-1) < 1e-13
            assert abs(delta(repaired)-target) < 1e-12
            assert np.isclose(d_shell_norm2, exact_d_shell_norm2, rtol=1e-13)
            rows.append(dict(L=length, N=cutoff, shell_start=shell_start,
                endpoint_target=target, raw_endpoint=delta(raw).real,
                centered_endpoint=delta(centered).real,
                repaired_endpoint=delta(repaired).real,
                raw_form=quadratic(w,raw), centered_form=quadratic(w,centered),
                repaired_form=quadratic(w,repaired),
                correction_norm=float(abs(defect)*np.linalg.norm(shell)),
                correction_derivative_norm=float(abs(defect)*np.sqrt(d_shell_norm2))))
        print(json.dumps(rows[-1]), flush=True)
    # Resolve the concrete quadrature risk by increasing nodes on a representative matrix.
    w1=weil_matrix(6.0,128)
    w2=weil_matrix(6.0,128,400)
    quadrature_difference=float(np.max(np.abs(w1-w2)))
    assert quadrature_difference < 1e-8
    result=dict(description='Floating-point illustrations; not certified bounds.',
                transform='H(s)=kappa(s)*zeta(s); no off-line zeros inserted',
                sigma=SIGMA,a=A,M=M,mpmath_digits=mp.mp.dps,
                max_matrix_quadrature_difference=quadrature_difference,rows=rows)
    Path(__file__).with_name('sampler_checks.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
