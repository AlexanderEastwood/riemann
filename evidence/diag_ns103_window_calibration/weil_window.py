"""Plain Weil form restricted to tests supported in [-lambda, lambda].

DIAGNOSTIC, NOT A CERTIFICATE. Floating point. This is the classical Weil
explicit-formula quadratic form, not the manuscript's semilocal Sonine form.

Explicit formula used (derived in results.md), for a completed function
Lambda(s) = N^{s/2} Gamma((s+mu)/2) D(s), D = sum c_n n^{-s}, c_1 = 1,
-D'/D = sum Lambda_D(n) n^{-s}, Lambda(s) = Lambda(1-s), and a test
h with hhat(s) = int h(x) e^{(s-1/2)x} dx:

  sum_rho hhat(rho) = [poles] (hhat(0)+hhat(1))
                      - sum_n Lambda_D(n) n^{-1/2} (h(log n) + h(-log n))
                      + h(0) log N
                      + A_mu(h),
  A_mu(h) = -gamma h(0) + int_0^inf [2h(0)e^{-2x} - e^{-(1/2+mu)x}(h(x)+h(-x))]
                                    / (1-e^{-2x}) dx.

zeta: N = 1/pi, mu = 0, poles.   Davenport-Heilbronn: N = 5/pi, mu = 1, entire.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Callable

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss


# ----------------------------------------------------------------- coefficients
def kappa_dh() -> mp.mpf:
    return (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)


def coeffs_dh(nmax: int) -> np.ndarray:
    """c_n = 2 Re(a chi(n)), a = (1 - i kappa)/2, chi(2) = i: values 1, kappa, -kappa, -1, 0 by n mod 5."""
    k = float(kappa_dh())
    table = np.array([0.0, 1.0, k, -k, -1.0])
    n = np.arange(nmax + 1)
    c = table[n % 5]
    c[0] = 0.0
    return c


def lambda_from_coeffs(c: np.ndarray, dps: int = 30) -> np.ndarray:
    """Lambda_D(n) from c_n log n = sum_{d|n} Lambda_D(d) c_{n/d}, exact recursion in mpmath."""
    mp.mp.dps = dps
    nmax = len(c) - 1
    cm = [mp.mpf(0)] + [mp.mpf(float(c[n])) if abs(c[n]) in (0.0, 1.0) else None for n in range(1, nmax + 1)]
    k = kappa_dh()
    for n in range(1, nmax + 1):
        if cm[n] is None:
            cm[n] = k if c[n] > 0 else -k
    lam = [mp.mpf(0)] * (nmax + 1)
    for n in range(2, nmax + 1):
        lam[n] = cm[n] * mp.log(n)
    for d in range(2, nmax + 1):
        ld = lam[d]
        if ld == 0:
            continue
        for m in range(2 * d, nmax + 1, d):
            lam[m] -= ld * cm[m // d]
    return np.array([float(v) for v in lam])


def lambda_zeta(nmax: int) -> np.ndarray:
    lam = np.zeros(nmax + 1)
    sieve = np.ones(nmax + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, nmax + 1):
        if sieve[p]:
            sieve[2 * p::p] = False
            q = p
            while q <= nmax:
                lam[q] = math.log(p)
                q *= p
    return lam


@dataclass
class Completed:
    name: str
    logN: float
    mu: int
    poles: bool
    lam: np.ndarray  # Lambda_D(n), index n


def zeta_data(nmax: int) -> Completed:
    return Completed("zeta", -math.log(math.pi), 0, True, lambda_zeta(nmax))


def dh_data(nmax: int) -> Completed:
    return Completed("davenport-heilbronn", math.log(5 / math.pi), 1, False, lambda_from_coeffs(coeffs_dh(nmax)))


# ------------------------------------------------- generic functional (mpmath)
def weil_generic(data: Completed, h: Callable[[Any], Any], support: float) -> dict:
    """Right-hand side of the explicit formula for a real test h supported in [-support, support]."""
    a = mp.mpf(1) / 2 + data.mu
    h0 = h(mp.mpf(0))
    prime = mp.mpf(0)
    nmax = int(math.exp(support)) + 1
    for n in range(2, min(nmax, len(data.lam) - 1) + 1):
        if data.lam[n] != 0:
            x = mp.log(n)
            prime += mp.mpf(data.lam[n]) / mp.sqrt(n) * (h(x) + h(-x))
    arch = -mp.euler * h0 + mp.quad(
        lambda x: (2 * h0 * mp.exp(-2 * x) - mp.exp(-a * x) * (h(x) + h(-x))) / (1 - mp.exp(-2 * x)),
        [0, 1, support, mp.inf])
    pole = mp.mpf(0)
    if data.poles:
        pole = mp.quad(lambda x: h(x) * mp.exp(-x / 2), [-support, 0, support]) + \
               mp.quad(lambda x: h(x) * mp.exp(x / 2), [-support, 0, support])
    total = pole - prime + h0 * data.logN + arch
    return {"pole": pole, "prime": prime, "arch": arch, "total": total}


# ---------------------------------------------------------- sine-basis window
def _gl_nodes(a: float, b: float, panel: float, order: int = 8) -> tuple[np.ndarray, np.ndarray]:
    xg, wg = leggauss(order)
    npan = max(1, int(math.ceil((b - a) / panel)))
    edges = np.linspace(a, b, npan + 1)
    xs, ws = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        xs.append((hi - lo) / 2 * xg + (hi + lo) / 2)
        ws.append((hi - lo) / 2 * wg)
    return np.concatenate(xs), np.concatenate(ws)


def window_matrix(data: Completed, lam: float, K: int, panel: float = 0.01) -> dict:
    """Weil form on g_j(y) = sin(alpha_j (y+lam)), alpha_j = j pi/(2 lam), j = 1..K.

    Returns the K x K matrix W with W_jk = sum_rho hhat_jk(rho), h_jk = g_j cross-correlated with g_k.
    h_jk(0) = lam delta_jk. Parity sectors (j-k odd) decouple exactly.
    """
    j = np.arange(1, K + 1)
    alpha = j * np.pi / (2 * lam)
    beta = lambda m: m * np.pi / (2 * lam)
    J, Kk = np.meshgrid(j, j, indexing="ij")
    mask = ((J - Kk) % 2 == 0) & (J != Kk)
    with np.errstate(divide="ignore", invalid="ignore"):
        inv_diff = np.where(J != Kk, 1.0 / beta(J - Kk), 0.0)
    inv_sum = 1.0 / beta(J + Kk)

    def assemble(sig: np.ndarray, diag: np.ndarray) -> np.ndarray:
        M = mask * ((sig[None, :] - sig[:, None]) * inv_diff + (sig[:, None] + sig[None, :]) * inv_sum)
        M[np.diag_indices(K)] = diag
        return M

    # prime side: P_jk = sum_n w_n S_jk(log n)
    nmax = int(math.floor(math.exp(2 * lam)))
    n = np.arange(2, min(nmax, len(data.lam) - 1) + 1)
    w = data.lam[n] / np.sqrt(n)
    x = np.log(n)
    keep = w != 0
    w, x = w[keep], x[keep]
    sx = np.sin(np.outer(alpha, x))          # K x M
    cx = np.cos(np.outer(alpha, x))
    sigma = sx @ w
    diag_p = ((2 * lam - x)[None, :] * cx) @ w + 2 * sigma / beta(2 * j)
    P = assemble(sigma, diag_p)

    # archimedean: A_jk = h_jk(0)[psi(a/2) + 2 T_a] + int_0^{2lam} q(x) (2h_jk(0) - S_jk(x)) dx
    a = 0.5 + data.mu
    xq, wq = _gl_nodes(0.0, 2 * lam, panel)
    q = np.exp(-a * xq) / (1 - np.exp(-2 * xq))
    sq = np.sin(np.outer(alpha, xq))
    cq = np.cos(np.outer(alpha, xq))
    sig_a = sq @ (q * wq)
    diag_a = ((2 * lam * (1 - cq) + xq[None, :] * cq - sq / alpha[:, None]) * q[None, :]) @ wq
    A = -assemble(sig_a, np.zeros(K))
    A[np.diag_indices(K)] = diag_a
    tail: Any = mp.quad(lambda t: mp.exp(-a * t) / (1 - mp.exp(-2 * t)), [2 * lam, mp.inf])
    psi_half: Any = mp.psi(0, a / 2)
    A[np.diag_indices(K)] += lam * (float(psi_half) + 2 * float(tail))

    W = -P + A + lam * data.logN * np.eye(K)
    if data.poles:
        xg, wg = _gl_nodes(-lam, lam, panel)
        base = np.sin(np.outer(alpha, xg + lam))
        g0 = base @ (wg * np.exp(-xg / 2))
        g1 = base @ (wg * np.exp(xg / 2))
        W += np.outer(g0, g1) + np.outer(g1, g0)
    return {"W": W, "alpha": alpha, "P": P, "A": A}


def S_closed(lam: float, j: int, k: int, x: float) -> float:
    """h_jk(x) + h_jk(-x) for x >= 0 in closed form (for checking)."""
    aj, ak = j * np.pi / (2 * lam), k * np.pi / (2 * lam)
    if j == k:
        return (2 * lam - x) * np.cos(ak * x) + 2 * np.sin(ak * x) / (2 * ak)
    if (j - k) % 2:
        return 0.0
    bd, bs = (j - k) * np.pi / (2 * lam), (j + k) * np.pi / (2 * lam)
    return (np.sin(ak * x) - np.sin(aj * x)) / bd + (np.sin(aj * x) + np.sin(ak * x)) / bs


def S_numeric(lam: float, j: int, k: int, x: float, npts: int = 20001) -> Any:
    y = np.linspace(-lam, lam, npts)
    gj = np.sin(j * np.pi / (2 * lam) * (y + lam))

    def gk(z):
        inside = (z >= -lam) & (z <= lam)
        return np.where(inside, np.sin(k * np.pi / (2 * lam) * (z + lam)), 0.0)
    h_plus = np.trapezoid(gj * gk(y - x), y)
    h_minus = np.trapezoid(gj * gk(y + x), y)
    return h_plus + h_minus
