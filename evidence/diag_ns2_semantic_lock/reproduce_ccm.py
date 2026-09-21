#!/usr/bin/env python3
"""NS-2 semantic lock: reproduce Connes-Consani-Moscovici, *Zeta spectral triples*
(arXiv:2511.22755, section 6) from this repository's Weil-form assembly.

Diagnostic; not a certificate.  Midpoint eigensolves (mpmath) are used; the
matrix entries themselves are Arb balls from the repository's formulas.

What CCM print in section 6 (their Figure 1 and the table on pp. 26-27) are the
differences |gamma_k - z_k| between the ordinates gamma_k of the first zeta zeros
and the eigenvalues z_k of D_log^{(lambda,N)}.  By their Theorem 5.10 (iii) those
eigenvalues are the real zeros of

    xi_hat(z) = 2 L^{-1/2} sin(zL/2) sum_{|j|<=N} xi_j / (z - 2 pi j / L),

where xi = (xi_j) is the lowest eigenvector of the (2N+1)x(2N+1) matrix
tau_{n,m} = QW_lambda(V_n, V_m) in the orthonormal basis V_n, |n| <= N.

This script:
  1. assembles tau from `assembly_general.sequences` / `block` (copied out of
     evidence/v124/g2_schur_cancellation/ into a cache directory so the JSON
     caches never land in evidence/), or from the transcription `sequences_M`
     below when lambda^2 = M is an integer that is not a perfect square
     (lambda = sqrt 12, sqrt 13, sqrt 14);
  2. takes the lowest eigenvector (checking that it is even and simple);
  3. finds the zeros of xi_hat near the first zeta zeros and prints
     |gamma_k - z_k| next to CCM's printed values.

Run from the repository root with the project venv, e.g.

    .venv/bin/python evidence/diag_ns2_semantic_lock/reproduce_ccm.py --M 9 --N 120 --bits 1024 --dps 220 --nzeros 20
    .venv/bin/python evidence/diag_ns2_semantic_lock/reproduce_ccm.py --M 12 --N 120 --bits 1024 --dps 220 --nzeros 50
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
import tempfile
import time
from pathlib import Path

import mpmath as mp
from flint import acb, arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SRC = ROOT / "evidence" / "v124" / "g2_schur_cancellation" / "assembly_general.py"

# CCM's printed values.  Figure 1 (lambda = 3, N = 120): first twenty zeros.
CCM_L3_N120 = [
    1.6e-34, 2.1e-31, 1.5e-29, 8.3e-27, 1.3e-25, 1.2e-23, 7.5e-22, 6.6e-21, 1.2e-18,
    8.8e-18, 7.3e-17, 2.2e-15, 9.7e-14, 2.7e-13, 6.3e-12, 5.6e-11, 2.9e-10, 1.2e-9,
    5.6e-8, 2.4e-7,
]
# Table pp. 26-27 (N = 120): columns lambda = sqrt12, sqrt13, sqrt14; rows k = 1..50.
CCM_TABLE = {
    12: [3.41e-50, 5.89e-47, 5.18e-45, 4.2e-42, 7.84e-41, 1.07e-38, 9.42e-37, 1.05e-35,
         3.25e-33, 2.99e-32, 3.76e-31, 1.87e-29, 1.28e-27, 4.47e-27, 2.18e-25, 2.76e-24,
         2.3e-23, 1.59e-22, 1.59e-20, 9.55e-20, 2.36e-19, 6.7e-18, 5.24e-17, 8.4e-16,
         1.94e-15, 2.42e-14, 6.05e-13, 1.26e-12, 3.15e-12, 2.72e-11, 3.57e-10, 1.7e-9,
         2.33e-9, 1.2e-7, 2.89e-7, 4.1e-7, 9.11e-7, 2.78e-6, 3.53e-5, 1.83e-4, 1.67e-4,
         2.97e-4, 2.19e-3, 4.35e-3, 1.19e-2, 1.27e-2, 2.87e-2, 1.43e-1, 1.98e-1, 9.02e-2],
    13: [2.44e-55, 4.5e-52, 4.16e-50, 3.65e-47, 7.11e-46, 1.06e-43, 1.0e-41, 1.19e-40,
         4.12e-38, 3.98e-37, 5.5e-36, 3.04e-34, 2.29e-32, 8.46e-32, 4.82e-30, 6.61e-29,
         6.08e-28, 4.66e-27, 5.5e-25, 3.54e-24, 9.75e-24, 3.31e-22, 2.86e-21, 5.32e-20,
         1.33e-19, 2.07e-18, 5.94e-17, 1.34e-16, 4.09e-16, 4.21e-15, 6.61e-14, 3.6e-13,
         5.66e-13, 4.03e-11, 1.04e-10, 1.85e-10, 4.92e-10, 1.94e-9, 3.24e-8, 2.0e-7,
         2.12e-7, 5.66e-7, 5.49e-6, 1.35e-5, 5.3e-5, 6.88e-5, 3.01e-4, 2.0e-3, 3.01e-3,
         2.04e-3],
    14: [1.07e-60, 2.08e-57, 2.0e-55, 1.89e-52, 3.81e-51, 6.13e-49, 6.17e-47, 7.66e-46,
         2.94e-43, 2.96e-42, 4.42e-41, 2.68e-39, 2.19e-37, 8.43e-37, 5.48e-35, 8.02e-34,
         8.02e-33, 6.73e-32, 9.11e-30, 6.19e-29, 1.86e-28, 7.38e-27, 6.89e-26, 1.45e-24,
         3.89e-24, 7.23e-23, 2.33e-21, 5.58e-21, 2.01e-20, 2.39e-19, 4.33e-18, 2.62e-17,
         4.6e-17, 4.23e-15, 1.16e-14, 2.45e-14, 7.53e-14, 3.61e-13, 7.44e-12, 5.24e-11,
         6.22e-11, 2.23e-10, 2.64e-9, 7.51e-9, 3.8e-8, 5.65e-8, 3.66e-7, 2.98e-6, 5.34e-6,
         4.78e-6],
}
CCM_TABLE[9] = CCM_L3_N120


def load_assembly(cache_dir: Path):
    """Copy assembly_general.py into cache_dir and import it from there."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    dst = cache_dir / "assembly_general.py"
    # atomic copy: several runs may share the cache directory concurrently
    fd, tmp = tempfile.mkstemp(dir=cache_dir, suffix=".py")
    with open(fd, "wb") as fh:
        fh.write(SRC.read_bytes())
    Path(tmp).replace(dst)
    spec = importlib.util.spec_from_file_location("assembly_general_ns2", dst)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def pairs_M(M: int) -> list[tuple[int, int]]:
    """Prime powers 1 < m <= M with their prime, i.e. the support of Lambda(m) on
    CCM's range 1 < k <= exp(L) = lambda^2.  Same test as assembly_general.pairs
    but with the CCM endpoint k = lambda^2 included (its term vanishes exactly,
    because q(U_n,U_m)(L) = 0)."""
    out = []
    for m in range(2, M + 1):
        for p in range(2, m + 1):
            if m % p == 0:
                k = m
                while k % p == 0:
                    k //= p
                if k == 1:
                    out.append((m, p))
                break
    return out


def sequences_M(M: int, J: int, bits: int, K: int = 96):
    """Transcription of assembly_general.sequences with lambda^2 = M (integer),
    so that lambda = sqrt(M) need not be an integer.  Every formula is the
    original one with

        2 log(lambda)      -> log(M)
        lambda^{-(4k+1)}   -> M^{-2k} / sqrt(M)
        lambda^{-4}        -> M^{-2}
        pairs(lambda)      -> pairs_M(M)

    Returns (L, b, d, a) with b_n, d_n = a_n(arch) + pole + prime, a_n(arch),
    n = 0..J, exactly as the original.
    """
    ctx.prec = bits
    L = arb(M).log()
    pi = arb.pi()
    h = (L / 4).sinh() ** 2
    rootM = arb(M).sqrt()
    pw = [(arb(m).log(), arb(p).log() / arb(m).sqrt()) for m, p in pairs_M(M)]
    ks = [(2 * k + arb(1) / 2, arb(1) / (arb(M) ** (2 * k) * rootM)) for k in range(K)]
    aK = 2 * K + arb(1) / 2
    eK = arb(1) / (arb(M) ** (2 * K) * rootM)
    lam4inv = arb(1) / (arb(M) ** 2)
    es = eK / (2 * aK * (1 - lam4inv))
    ed = 2 * eK / (L * aK * aK * (1 - lam4inv))
    bs, ds, ars = [], [], []
    for n in range(J + 1):
        t = 2 * pi * n / L
        z = acb(arb(1) / 4, -t / 2)
        ps = z.digamma()
        tri = z.polygamma(1)
        s = -ps.imag / 2
        a = ps.real - pi.log() + tri.real / (2 * L)
        for c, e in ks:
            den = c * c + t * t
            s -= e * t / den
            a -= 2 / L * e * (c * c - t * t) / (den * den)
        s += arb(0, es.upper())
        a += arb(0, ed.upper())
        den = L * L + 16 * pi * pi * n * n
        b = 32 * L * h * n / den + (s + sum(((t * y).sin() * w for y, w in pw), arb(0))) / pi
        d = a + 32 * L * h * (L * L - 16 * pi * pi * n * n) / (den * den) \
            - 2 * sum(((t * y).cos() * (1 - y / L) * w for y, w in pw), arb(0))
        bs.append(b)
        ds.append(d)
        ars.append(a)
    return L, bs, ds, ars


def arb_to_mpf(x: arb, digits: int) -> mp.mpf:
    return mp.mpf(x.mid().str(digits, radius=False))


def max_rad(xs) -> float:
    return max(float(x.rad().str(5, radius=False)) for x in xs)


def zeros_of_xi_hat(v_even, L: mp.mpf, gammas, dps: int, scan_step: float = 0.05):
    """v_even: lowest eigenvector in the even parity basis (index 0..N), i.e.
    xi_0 = v_0, xi_{+-j} = v_j / sqrt 2 for j >= 1.  Returns the zero of
    S(z) = sum_j xi_j/(z - 2 pi j/L) nearest each gamma_k (bracketed), plus a
    count of all sign changes of xi_hat on [0, gamma_max + 1]."""
    mp.mp.dps = dps
    N = len(v_even) - 1
    s2 = mp.sqrt(2)
    a = [2 * mp.pi * j / L for j in range(N + 1)]
    xi0 = v_even[0]
    xi = [v_even[j] / s2 for j in range(1, N + 1)]

    def S(z):
        tot = xi0 / z
        for j in range(1, N + 1):
            tot += xi[j - 1] * 2 * z / (z * z - a[j] * a[j])
        return tot

    def xihat(z):
        return 2 / mp.sqrt(L) * mp.sin(z * L / 2) * S(z)

    # Bracket the ENTIRE function xihat (sin(zL/2) cancels the poles of S at the
    # lattice 2 pi j / L, which can fall inside a bracket, e.g. at lambda = sqrt 12)
    # and bisect: ~ (dps + 7) * log2(10) steps of 2N+1 terms each, no tolerance
    # heuristics.  Real zeros of xihat below 2 pi N / L are exactly the zeros of S.
    roots = []
    for g in gammas:
        d = mp.mpf("0.01")
        lo, hi = g - d, g + d
        flo, fhi = xihat(lo), xihat(hi)
        tries = 0
        while flo * fhi > 0 and tries < 6:
            d *= 2
            lo, hi = g - d, g + d
            flo, fhi = xihat(lo), xihat(hi)
            tries += 1
        if flo * fhi > 0:
            roots.append(None)
            continue
        target = mp.mpf(10) ** (-(dps - 3))
        while hi - lo > target:
            mid = (lo + hi) / 2
            fm = xihat(mid)
            if fm == 0:
                lo = hi = mid
                break
            if fm * flo < 0:
                hi, fhi = mid, fm
            else:
                lo, flo = mid, fm
        roots.append((lo + hi) / 2)

    # coarse scan for extra real zeros of xi_hat below the last zeta zero used
    with mp.workdps(30):
        top = float(gammas[-1]) + 1.0
        zmax = a[N] if N < len(a) else None
        n_scan = int(top / scan_step)
        prev = None
        sign_changes = []
        for i in range(1, n_scan + 1):
            z = mp.mpf(i) * scan_step
            f = xihat(z)
            if prev is not None and f * prev < 0:
                sign_changes.append(float(z))
            prev = f
    return roots, sign_changes


def run(M: int, N: int, bits: int, dps: int, nzeros: int, K: int, cache_dir: Path,
        use_original: bool | None, out_json: Path | None):
    t0 = time.time()
    lam_is_int = int(round(M ** 0.5)) ** 2 == M
    lam_int = int(round(M ** 0.5)) if lam_is_int else None
    mod = load_assembly(cache_dir)
    if use_original is None:
        use_original = lam_is_int
    if use_original:
        assert lam_is_int, "assembly_general.sequences needs integer lambda"
        L, b, d, a = mod.sequences(lam_int, N, bits, K)
        source = f"assembly_general.sequences(lam={lam_int}, J={N}, bits={bits}, K={K})"
    else:
        L, b, d, a = sequences_M(M, N, bits, K)
        source = f"sequences_M(M={M}, J={N}, bits={bits}, K={K})"
    ctx.prec = bits
    # cross-check the transcription against the original whenever lambda is an integer
    xcheck = None
    if lam_is_int:
        L2, b2, d2, a2 = sequences_M(M, N, bits, K)
        Lo, bo, do, ao = mod.sequences(lam_int, N, bits, K)
        diffs = [abs((x - y).mid()) for x, y in zip(bo + do, b2 + d2)]
        rads = [max(float(x.rad().str(5, radius=False)), float(y.rad().str(5, radius=False)))
                for x, y in zip(bo + do, b2 + d2)]
        worst = max(float(dd.str(5, radius=False)) for dd in diffs)
        xcheck = {"max_abs_mid_diff_b_d": worst, "max_rad": max(rads),
                  "overlap_all": all(x.overlaps(y) for x, y in zip(bo + do, b2 + d2))}
        print(f"[xcheck] sequences_M vs assembly_general.sequences at lambda={lam_int}: "
              f"max |mid diff| = {worst:.3e}, max radius = {max(rads):.3e}, "
              f"all balls overlap = {xcheck['overlap_all']}")

    Teven = mod.block(range(0, N + 1), range(0, N + 1), "even", b, d)
    Todd = mod.block(range(1, N + 1), range(1, N + 1), "odd", b, d)
    ne, no = N + 1, N
    rad_e = max(float(Teven[i, j].rad().str(5, radius=False)) for i in range(ne) for j in range(ne))
    print(f"[assembly] {source}; L = {L.str(20)}; max entry radius (even block) = {rad_e:.3e}; "
          f"{time.time() - t0:.1f}s")

    digits = int(bits * 0.30103) - 2
    mp.mp.dps = dps
    Ae = mp.matrix(ne, ne)
    for i in range(ne):
        for j in range(ne):
            Ae[i, j] = arb_to_mpf(Teven[i, j], digits)
    Ao = mp.matrix(no, no)
    for i in range(no):
        for j in range(no):
            Ao[i, j] = arb_to_mpf(Todd[i, j], digits)
    t1 = time.time()
    Ee, Qe = mp.eigsy(Ae)
    Eo, Qo = mp.eigsy(Ao)
    print(f"[eigsy] even {ne}x{ne} and odd {no}x{no} at dps={dps}: {time.time() - t1:.1f}s")
    ev_e = sorted(range(ne), key=lambda i: Ee[i])
    ev_o = sorted(range(no), key=lambda i: Eo[i])
    eps = Ee[ev_e[0]]
    eps2 = Ee[ev_e[1]]
    eps_odd = Eo[ev_o[0]]
    v = [Qe[i, ev_e[0]] for i in range(ne)]
    # Rayleigh-quotient residual in Arb as a sanity check on the midpoint solve
    vv = arb_mat([[arb(mp.nstr(x, digits))] for x in v])
    num = (vv.transpose() * Teven * vv)[0, 0]
    den = (vv.transpose() * vv)[0, 0]
    rq = num / den
    print(f"[ground] eps_N(even) = {mp.nstr(eps, 12)}  second even = {mp.nstr(eps2, 12)}  "
          f"lowest odd = {mp.nstr(eps_odd, 12)}")
    print(f"[ground] Arb Rayleigh quotient of the midpoint eigenvector: {rq.str(12)}")
    even_simple = (eps < eps_odd) and (eps < eps2)
    print(f"[ground] even-simple (lowest even < lowest odd and < second even): {even_simple}")

    with mp.workdps(max(dps, 120)):
        gammas = [mp.im(mp.zetazero(k)) for k in range(1, nzeros + 1)]
    Lm = mp.mpf(L.mid().str(digits, radius=False))
    t2 = time.time()
    roots, sign_changes = zeros_of_xi_hat(v, Lm, gammas, dps)
    print(f"[zeros] root finding: {time.time() - t2:.1f}s; sign changes of xi_hat on "
          f"[0, gamma_{nzeros}+1]: {len(sign_changes)} (expected {nzeros} if no extra zeros)")
    ccm = CCM_TABLE.get(M)
    rows = []
    print(f"{'k':>3} {'gamma_k':>22} {'|gamma_k - z_k| (here)':>24} {'CCM':>10} {'ratio':>8}")
    for k, (g, r) in enumerate(zip(gammas, roots), 1):
        if r is None:
            print(f"{k:3d} {mp.nstr(g, 18):>22} {'no bracketed root':>24}")
            rows.append({"k": k, "gamma": mp.nstr(g, 30), "z": None, "diff": None,
                         "ccm": (ccm[k - 1] if ccm and k <= len(ccm) else None)})
            continue
        diff = abs(g - r)
        c = ccm[k - 1] if ccm and k <= len(ccm) else None
        ratio = float(diff) / c if c else None
        print(f"{k:3d} {mp.nstr(g, 18):>22} {mp.nstr(diff, 6):>24} "
              f"{(f'{c:.2e}' if c else '-'):>10} {(f'{ratio:.3f}' if ratio else '-'):>8}")
        rows.append({"k": k, "gamma": mp.nstr(g, 40), "z": mp.nstr(r, 40),
                     "diff": mp.nstr(diff, 8), "ccm": c, "ratio": ratio})
    summary = {
        "M": M, "lambda": (lam_int if lam_is_int else f"sqrt({M})"), "N": N, "bits": bits,
        "dps": dps, "K": K, "source": source, "transcription_xcheck": xcheck,
        "L": L.str(40), "max_entry_radius_even": rad_e,
        "eps_N_even": mp.nstr(eps, 40), "second_even": mp.nstr(eps2, 40),
        "lowest_odd": mp.nstr(eps_odd, 40), "rayleigh_arb": rq.str(40),
        "even_simple": bool(even_simple),
        "sign_changes_count": len(sign_changes), "nzeros": nzeros, "rows": rows,
        "runtime_s": time.time() - t0,
    }
    if out_json:
        out_json.write_text(json.dumps(summary, indent=1) + "\n")
        print(f"[out] wrote {out_json}")
    return summary


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--M", type=int, default=9, help="lambda^2 (9, 12, 13, 14)")
    p.add_argument("--N", type=int, default=120, help="Fourier truncation |n| <= N")
    p.add_argument("--bits", type=int, default=1024, help="Arb precision for the assembly")
    p.add_argument("--dps", type=int, default=220, help="mpmath digits for the eigensolve / roots")
    p.add_argument("--nzeros", type=int, default=20)
    p.add_argument("--K", type=int, default=96, help="archimedean series terms (as in the original)")
    p.add_argument("--cache-dir", type=Path, default=Path(tempfile.gettempdir()) / "ns2_assembly_cache")
    p.add_argument("--transcription", action="store_true",
                   help="force sequences_M even when lambda is an integer")
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args(argv)
    sys.stdout.reconfigure(line_buffering=True)
    run(args.M, args.N, args.bits, args.dps, args.nzeros, args.K, args.cache_dir,
        (False if args.transcription else None), args.out)


if __name__ == "__main__":
    main()
