"""Check C = 2 + gamma - log(4 pi) = sum_rho 1/|rho|^2 (RH form) numerically, and show how much of C
comes from the low zeros. Uses mpmath.zetazero for the first M zeros, tail via the Riemann-von Mangoldt
density: sum_{gamma>T} 1/(1/4+gamma^2) ~ (1/2pi) int_T^inf log(t/2pi)/t^2 dt = (log(T/2pi)+1)/(2 pi T).
Each zero rho = 1/2 + i gamma is paired with its conjugate: contributes 2/(1/4+gamma^2)."""
from mpmath import mp, mpf, zetazero, log, pi, euler, nstr
import time
mp.dps = 20
C = 2 + euler - log(4*pi)
M = 2000
t0 = time.time()
s = mpf(0); marks = {10:None, 100:None, 500:None, 1000:None, 2000:None}
for n in range(1, M+1):
    g = zetazero(n).imag
    s += 2/(mpf(1)/4 + g**2)
    if n in marks:
        T = g
        tail = (log(T/(2*pi)) + 1)/(2*pi*T)
        marks[n] = (float(T), float(s), float(s/C), float(s + tail))
print(f"C = {nstr(C, 20)}   ({time.time()-t0:.0f}s for {M} zeros)")
print(" n_zeros   gamma_n     partial sum   fraction of C   partial+tail estimate")
for n, (T, ps, fr, est) in marks.items():
    print(f" {n:>7} {T:>10.3f} {ps:>14.8f} {fr:>14.5f} {est:>16.8f}")
