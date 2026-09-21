# Symbol / Toeplitz / Hankel split of the windowed Weil matrix — DIAGNOSTIC

**Status: diagnostic, not a certificate.** Direct eigenvalues (mpmath `eigsy`) of
explicitly assembled matrices; no linear solves; Arb assembly at 768 bits
(λ ≤ 4) and 2048 bits (λ ≥ 5), extraction at 260/600 digits. The split
reproduces `assembly_general.block()` exactly (max entry error 0, asserted).
`lmin(FULL)` agrees with the certified compression values already in the
manuscript (e.g. 3.6434e-38 at λ=3, `prop:v117-ground-order`).

Exact decomposition of the Fourier-basis window matrix:

    FULL = D + T' + Hk
    D    = diag(d_n)                       sampled symbol (multiplier at t_n = 2πn/L)
    T'   = (b_n − b_m)/(n − m),  n ≠ m     window commutator, Toeplitz-structured
    Hk   = ±(b_n + b_m)/(n + m)            reflection term, Hankel-structured; sign = parity;
           incl. its diagonal ±b_n/n and the zero-mode √2·b_{n+m}/(n+m)

| λ | parity | N | min d_n | lmin(D+T') | lmin(D+Hk) | lmin(FULL) |
|--:|:--|--:|--:|--:|--:|--:|
| 3 | even | 64 | +0.04086 | +2.32e-15 | −0.0287 | +3.6434e-38 |
| 3 | odd  | 64 | +0.04170 | +2.32e-15 | −0.2878 | +1.3133e-34 |
| 4 | even | 64 | +0.03314 | +1.08e-28 | −0.0276 | +3.7381e-72 |
| 4 | odd  | 64 | +0.03395 | +1.08e-28 | −0.3293 | +3.0700e-68 |
| 4 | even | 256 | +0.03314 | +7.62e-29 | −0.0279 | +2.8303e-75 |
| 4 | odd  | 256 | +0.03395 | +7.62e-29 | −0.3526 | +4.0068e-71 |
| 5 | even | 64 | +0.02867 | +1.69e-40 | −0.0251 | +1.2289e-94 |
| 5 | odd  | 64 | +0.02918 | +1.69e-40 | −0.3575 | +8.5287e-91 |
| 6 | even | 64 | +0.01966 | +3.79e-49 | −0.0193 | +1.8343e-109 |
| 6 | odd  | 64 | +0.01976 | +3.79e-49 | −0.3648 | +1.2503e-105 |
| 8 | even | 64 | +0.02243 | +3.11e-61 | −0.0294 | +6.2550e-129 |
| 8 | odd  | 64 | +0.02276 | +3.11e-61 | −0.3749 | +4.4195e-125 |

## What it shows

1. The reflection (Hankel) term alone drives the form negative by O(1):
   about −0.03 (even) and −0.35 (odd), flat in λ.
2. The Toeplitz-structured commutator supplies exactly enough positivity to
   cancel that down to 10^-75 (λ=4) … 10^-129 (λ=8). The certified positivity
   is a cancellation between a Toeplitz kernel and a Hankel kernel to
   seventy-plus orders. This localizes `prop:v121-complement-cancellation`
   to the two kernels of the commutator [M_b, H] in `prop:v114-weil-core`.
3. The parity sectors are literally T(φ)+H(φ) and T(φ)−H(φ) — the classical
   Toeplitz-plus-Hankel pencils (Basor–Ehrhardt), which is the right theory
   for their determinant/eigenvalue asymptotics.

## A pre-registered prediction that FAILED

Predicted: Szegő on the symbol would be wrong-signed (since v1.37 proves
inf β_a → −∞). Observed: min d_n ≈ +0.02…+0.04 at every window. Cause: the
diagonal samples the symbol at spacing 2π/L ≈ 1.5, while the negative lobes
near a zero have width ~1/T ≈ 0.25, so the samples never land on them. The
symbol-only estimate is wrong in SIZE by ~73 orders of magnitude, not in
sign. For a floor/decay question that is the same failure — but it is not
the one predicted, and it is recorded as such.

---

## Correction and two further diagnostics (later the same day)

**The "failed prediction" above was itself wrong.** The diagonal `d_n` is the
symbol sampled at the lattice `t_n = 2πn/L`, and those points sit on the
positive *crests* of a symbol that is deeply negative between them. Scanning
`β_λ(t)` on a fine grid (`symbol_scan.py`, `scan2.py`; validated against
`sequences()` to `|β(t_n) − d_n| ≤ 1.5e-14`):

| λ | L | min β | at t | negative measure (2-sided) | KMS count (L/2π)·\|neg\| | certified negative eigenvalues |
|--:|--:|--:|--:|--:|--:|--:|
| 3 | 2.197 | −4.86 | 0.55 | 11.88 | 4.15 | 0 |
| 4 | 2.773 | −5.65 | 0.52 | 13.40 | 5.91 | 0 |
| 6 | 3.584 | −6.54 | 0.47 | 14.18 | 8.09 | 0 |
| 8 | 4.159 | −6.91 | 0.43 | 16.02 | 10.60 | 0 |

Since `W_λ = P_a M_{β_a} P_a` (prop:v130-remainder), Kac–Murdock–Szegő
predicts `(L/2π)·|{β<0}|` negative eigenvalues. **So the symbol-only estimate
is wrong-signed, by 4 → 11 eigenvalues, growing ≈ 2.5 per unit L.** This is
a numerical instance of the v1.39 information-loss obstruction.

Lobe geometry: every negative lobe lies at `t < 13`, none near a zeta zero
(nearest is 14.13); the lobes recur with period exactly `2π/L` — the lattice
period — with the lattice points on the crests; the deep lobes have
`width × L ≈ 4.5–5.4`, i.e. about 0.8 of one Fourier resolution cell `2π/L`
of the window, at every λ tested. Depths fall geometrically along the train
(λ=4: −5.65, −0.50, −0.15, −0.05, −0.01).

**Prime-free control** (`noprime.py`; same matrix with the prime sum removed):

| λ | lmin with primes (even) | lmin without primes (even) | (odd) |
|--:|--:|--:|--:|
| 3 | +3.6e-38 | −0.68 | −1.53 |
| 4 | +3.7e-72 | −0.94 | −2.27 |
| 6 | +1.8e-109 | −1.25 | −3.81 |
| 8 | +6.3e-129 | −1.46 | −5.44 |

Without primes the window form is negative by O(1), growing with λ. The
primes *deepen* the low-frequency hole of the symbol (β(0.5): −3.6 → −6.8)
and yet flip the operator's sign: they decide it by **phase on the window's
resolution lattice**, not by depth. That is "arithmetic location" as a number.
The super-exponential collapse of the positive `lmin` is therefore the residual
of an O(1)-vs-O(1) cancellation, not a Landau–Widom property of a positive
archimedean operator; the *rate* remains the open part of NS-7.
