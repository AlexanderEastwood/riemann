"""Szego test: split the windowed Weil matrix into
   D  = diag(d_n)                symbol part; Szego says lmin -> inf symbol, and min d_n IS its lmin
   T' = (b_n-b_m)/(n-m) offdiag  window-commutator term, Toeplitz-structured
   Hk = +-(b_n+b_m)/(n+m) + zero-mode sqrt2 b_{n+m}/(n+m)   reflection / Hankel term
   Full = D + T' + Hk  (must equal assembly_general.block exactly)
Which piece carries the sign?  Diagnostic only; direct eigenvalues, no solves."""
import sys, time
sys.path.insert(0, 'evidence/v124/g2_schur_cancellation')  # assembly_general.py; run from repo root; NOTE sequences() caches JSON next to that file
from flint import arb, arb_mat, ctx
from assembly_general import sequences, block
from cert import tomp
import mpmath as mp

def parts(lam, N, parity, bits, dps):
    ctx.prec = bits
    L, b, d, a = sequences(lam, N + 8, bits)
    rows = list(range(0 if parity == 'even' else 1, N + 1)); n_ = len(rows)
    r2 = arb(2).sqrt(); sg = 1 if parity == 'even' else -1
    D = arb_mat(n_, n_); T = arb_mat(n_, n_); H = arb_mat(n_, n_)
    for i, n in enumerate(rows):
        for j, m in enumerate(rows):
            if n == m:
                D[i, j] = d[n]
                if n > 0:
                    H[i, j] = sg * b[n] / n          # (b_n+b_m)/(n+m) at n=m: the Hankel diagonal
            elif n == 0 or m == 0:
                H[i, j] = r2 * b[n + m] / (n + m)          # zero-mode: Hankel-type
            else:
                T[i, j] = (b[n] - b[m]) / (n - m)
                H[i, j] = sg * (b[n] + b[m]) / (n + m)
    full = D + T + H
    ref = block(rows, rows, parity, b, d)
    diff = max(abs((full[i, j] - ref[i, j]).mid()) for i in range(n_) for j in range(n_))
    def lmin(M): mp.mp.dps = dps; return min(mp.eigsy(tomp(M, dps), eigvals_only=True))
    mind = min(float(d[n].mid()) for n in rows)
    assert diff < 1e-30, f"split does not reproduce block(): {diff}"
    return dict(split_error=float(diff), min_d=mind, lmin_D=lmin(D), lmin_DT=lmin(D + T),
                lmin_DH=lmin(D + H), lmin_full=lmin(full), L=float(L.mid()))

print("%-4s %-5s %-4s %-11s %-11s %-11s %-11s %-13s %-8s" % ("lam","par","N","min d_n","lmin D+T'","lmin D+Hk","lmin FULL","split err","secs"))
for lam, N, bits, dps in ((3,64,768,260),(4,64,768,260),(4,256,768,260),(5,64,2048,600),(6,64,2048,600),(8,64,2048,600)):
    for par in ('even','odd'):
        t=time.time(); r = parts(lam, N, par, bits, dps); mp.mp.dps=8
        print("%-4d %-5s %-4d %-11s %-11s %-11s %-11s %-13.1e %-8.0f" % (lam, par, N, "%.5f"%r['min_d'], mp.nstr(r['lmin_DT'],5), mp.nstr(r['lmin_DH'],5), mp.nstr(r['lmin_full'],5), r['split_error'], time.time()-t), flush=True)
