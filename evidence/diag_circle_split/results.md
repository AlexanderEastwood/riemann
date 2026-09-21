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

---

## Ground-state energy budget (`budget.py`) — NS-7 answered at the diagnostic level

Exact split of the ground eigenvector's energy, `lmin = v'Dv + v'T'v + v'Hk·v`
(residual ≤ 1e-259; N=256 at λ=3,4 with 768-bit assembly / 260 digits, N=64 at
λ=6,8 with 2048 bits / 600 digits):

| λ | parity | lmin | v'Dv (crests) | v'T'v | v'Hk·v | peak n | n50 | n90 | mass n≤8 |
|--:|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | even | 2.73e-38 | +0.0421 | −0.0216 | −0.0205 | 1 | 1 | 2 | 100% |
| 3 | odd  | 1.00e-34 | +0.0448 | −0.0433 | −0.0015 | 2 | 2 | 3 | 100% |
| 4 | even | 2.83e-75 | +0.0353 | −0.0218 | −0.0135 | 1 | 1 | 2 | 100% |
| 4 | odd  | 4.01e-71 | +0.0407 | −0.0401 | −0.0006 | 2 | 2 | 3 | 100% |
| 6 | even | 1.83e-109 | +0.0200 | −0.0136 | −0.0064 | 1 | 1 | 3 | 100% |
| 6 | odd  | 1.25e-105 | +0.0209 | −0.0207 | −0.0002 | 3 | 3 | 4 | 100% |
| 8 | even | 6.26e-129 | +0.0241 | −0.0176 | −0.0065 | 1 | 1 | 3 | 100% |
| 8 | odd  | 4.42e-125 | +0.0285 | −0.0284 | −0.0001 | 3 | 3 | 5 | 100% |

1. **The three pieces stay O(0.02–0.045) while lmin falls 38 → 129 orders.** The
   collapse is the sharpening of a fixed-size cancellation, not a property of
   any positive operator. `v'Dv` tracks `min_n d_n` (0.041, 0.033, 0.020,
   0.022) to ~10%: the ground state is essentially the lowest lattice mode(s),
   sitting on the crests, and the two commutator couplings cost exactly what
   the crests hold. The "forced spread to high frequency" idea is wrong: 100%
   of the mass is at n ≤ 8 at every window, 90% at n ≤ 2–5.
2. **Parity structure.** Odd sector: Hankel term negligible and shrinking
   (−0.0015 → −0.0001); the balance is purely diagonal vs Toeplitz commutator,
   matching to 3–4 digits. Even sector: split between the two, the Hankel
   share falling 49% → 38% → 32% → 27% with λ.
3. **Rate.** Zhu's Landau–Widom law, −ln λ_min(L) ~ 2π²N(T*)/ln N(T*), T* = 2πe^{2L}, against the best available upper bounds on μ0:

   | λ | Zhu law log10 λ_min | best upper bound on μ0 (log10) | source | gap (orders) |
   |--:|--:|--:|:--|--:|
   | 3 | -38.9 | -37.6 | compression N=256 | +1.3 |
   | 4 | -72.7 | -74.6 | CERTIFIED mu0 < 2.454e-75 (prop:v140-ground4) | -1.9 |
   | 6 | -175.9 | -181.7 | compression N=36 head, M=256 tail (earlier run; unconverged in M) | -5.8 |
   | 8 | -326.4 | -128.2 | compression N=64 (far from converged) | +198.2 |

   Read the gap column as "measured minus law" in orders of magnitude. At λ=3
   the law is within 1.3 orders. At λ=4 the *certified* μ0 lies about 1.9
   orders **below** the law. At λ=6 and 8 the only values in hand are finite
   compressions that are not converged in the cutoff (earlier M-sweep), so
   they are loose upper bounds and cannot test the law; the law itself
   predicts 1e-176 and 1e-327 there — below double-precision range, which is
   why a naive float evaluation divided by zero. Zhu's law is an empirical
   fit with a "~"; the honest statement is that it gives the right *scale of
   collapse* (tens to hundreds of orders) at these windows, not the constant.
   An earlier line in this file claiming agreement "to ~20× at all four
   windows" was wrong and is superseded by this table.

**NS-7 verdict (as corrected by the retraction below).** Sign: arithmetic — the prime-free assembled form is negative O(1) and the primes restore positivity (exact); the "KMS on the line symbol" sentence is withdrawn. Size: a lowest-lattice-mode
ground whose crest energy ≈ min d_n is cancelled by the commutator couplings to
the last digit, the residual at the Landau–Widom *scale* (the law gives the order of collapse, not the constant). Nothing here is a
bound; all of it is exact arithmetic on certified compressions.

---

## RETRACTION (later the same day): the off-grid "line symbol" is not a symbol

The sections above titled "Correction and two further diagnostics" claimed that
`β_λ(t)` evaluated between lattice points is the Fourier-multiplier symbol of
`W_λ`, that Kac–Murdock–Szegő therefore predicts 4 → 11 negative eigenvalues,
and that the negative lobes are sub-resolution. **All three claims are
withdrawn.** The decisive test (`levels.py`): with the actual ground vector and
Plancherel verified to 0.996,

    λ=3:  (1/2π)∫_{β<0} β|f̂|² = −0.674,  (1/2π)∫_{β>0} β|f̂|² = +0.254,  sum = −0.42   (true q = 2.7e-38)
    λ=4:                          −0.628                         +0.242         −0.39   (true q = 2.8e-75)

A sum of −0.4 against a true value of ~0 cannot be a normalization error. The
function scanned was the analytic continuation in `n` of the *diagonal* `d_n`
(the circle multiplier's values), which coincides with nothing between lattice
points: the pole term is rank-two, not a multiplier, and the prime terms are
compressed shifts. The manuscript's line symbol `β_a` (`prop:v130-remainder`,
`eq:v135-full-symbol`) is a different object with a different archimedean
normalization (`ψ(5/4+iξ/2)`, continuum kernel). No KMS statement was tested.

**What survives from this lane:** the exact matrix split `D + T' + Hk`; the
ground-state energy budget (exact); the prime-free control (exact); positivity
of the lattice diagonal (a fact about the assembled operator). What does not:
every sentence about the "line symbol", its negative measure, its lobes, KMS,
and sub-resolution. The correct version of the level-split experiment must use
the manuscript's own `β_a`; it has not been done.
