"""Independent mpmath implementation of d_N (Cholesky), run at two precisions."""
import sys, time
from math import gcd
from mpmath import mp, mpf, log, pi, euler, cot, cholesky, matrix, nstr, sqrt

def run(dps, NMAX):
    mp.dps = dps
    L2 = log(2*pi); gam = euler
    def V(h, k):
        return sum(mpf((m*h) % k)/k*cot(pi*m/k) for m in range(1, k)) if k > 1 else mpf(0)
    cache = {}
    def gc(h, k):
        if (h, k) not in cache:
            H, K = mpf(h), mpf(k)
            cache[(h, k)] = (L2-gam)/2*(1/H+1/K) + (K-H)/(2*H*K)*log(H/K) - pi/(2*H*K)*(V(h, k)+V(k, h))
        return cache[(h, k)]
    G = matrix(NMAX, NMAX)
    for m in range(1, NMAX+1):
        for n in range(m, NMAX+1):
            g = gcd(m, n); v = gc(m//g, n//g)/g
            G[m-1, n-1] = v; G[n-1, m-1] = v
    b = matrix([(log(n)+1-gam)/n for n in range(1, NMAX+1)])
    out = {}
    for N in range(1, NMAX+1):
        GN = G[:N, :N]; bN = b[:N]
        Lc = cholesky(GN)            # G = L L^T
        # solve L y = b, then d^2 = 1 - |y|^2
        y = matrix(N, 1)
        for i in range(N):
            s = bN[i]
            for j in range(i):
                s -= Lc[i, j]*y[j]
            y[i] = s/Lc[i, i]
        d2 = 1 - sum(y[i]**2 for i in range(N))
        out[N] = d2
    return out

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    t0 = time.time(); a = run(50, NMAX); t1 = time.time(); b = run(80, NMAX); t2 = time.time()
    mp.dps = 80
    C = 2 + euler - log(4*pi)
    print(f"# mpmath Cholesky: dps=50 ({t1-t0:.1f}s) vs dps=80 ({t2-t1:.1f}s)")
    print(f"# {'N':>3} {'d_N^2 (dps 80)':>40} {'|dps50-dps80|':>14} {'d_N^2 log N / C':>20}")
    worst = mpf(0)
    for N in range(1, NMAX+1):
        diff = abs(a[N]-b[N]); worst = max(worst, diff)
        print(f"  {N:>3} {nstr(b[N], 36):>40} {nstr(diff, 3):>14} {nstr(b[N]*log(N)/C, 16):>20}")
    print(f"# max |dps50 - dps80| over N<={NMAX}: {nstr(worst, 3)}")
