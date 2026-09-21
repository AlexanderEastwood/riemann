"""Arb-ball -> mpmath conversion used by the diagnostics here (midpoints only; not a certificate)."""
import mpmath as mp


def tomp(A, dps: int) -> mp.matrix:
    n, m = A.nrows(), A.ncols()
    mp.mp.dps = dps
    return mp.matrix([[mp.mpf(A[i, j].str(dps - 5, radius=False)) for j in range(m)] for i in range(n)])
