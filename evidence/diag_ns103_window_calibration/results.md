# NS-103: window sensitivity of the plain Weil form, calibrated on Davenport-Heilbronn

**This directory holds diagnostics, not certificates.** Floating point (numpy,
mpmath), no interval bounds. Nothing here is a bound, a G2 statement or an RH
statement. The object is the classical Weil explicit-formula quadratic form
restricted to tests of support [-lambda, lambda]; it is **not** the
manuscript's semilocal Sonine form, and no transfer between the two is claimed.

Proposal gate: `PROPOSAL.md` (filled before the row was claimed).

## Question

At which window lambda does the Weil form restricted to tests supported in
[-lambda, lambda] first detect a known off-line zero, and how does that window
depend on the zero's offset delta = Re(rho) - 1/2 and height T? The
Davenport-Heilbronn function (Titchmarsh 10.25) supplies the off-line zeros;
zeta, whose form must stay nonnegative in this range, supplies the control on
the pipeline.

## Explicit formula used

For a completed function Lambda(s) = N^{s/2} Gamma((s+mu)/2) D(s) with
D = sum c_n n^{-s}, c_1 = 1, -D'/D = sum Lambda_D(n) n^{-s}, Lambda(s) =
Lambda(1-s), and a real test h supported in [-X, X] with
hhat(s) = int h(x) e^{(s-1/2)x} dx:

    sum_rho hhat(rho) = [poles](hhat(0) + hhat(1))
                        - sum_n Lambda_D(n) n^{-1/2} (h(log n) + h(-log n))
                        + h(0) log N
                        - gamma h(0)
                        + int_0^inf [2h(0) e^{-2x} - e^{-(1/2+mu)x}(h(x)+h(-x))] / (1 - e^{-2x}) dx.

Zeta: N = 1/pi, mu = 0, poles at 0 and 1. Davenport-Heilbronn: N = 5/pi,
mu = 1, entire; c_n = 2 Re(a chi(n)) takes the values 1, kappa, -kappa, -1, 0
for n = 1, 2, 3, 4, 0 mod 5, and Lambda_D(n) follows from the exact recursion
c_n log n = sum_{d|n} Lambda_D(d) c_{n/d} (mpmath, 30 digits). For
h = g cross-correlated with g the left side is sum over zeros of
ghat(rho) conj(ghat(1 - conj rho)); it is nonnegative for every g iff all zeros
lie on the line (Weil). A pair (rho, 1 - conj rho) off the line contributes
2 Re[ghat(1/2+delta+iT) conj(ghat(1/2-delta+iT))], which can be negative.

Basis: g_j(y) = sin(alpha_j (y + lambda)) on [-lambda, lambda],
alpha_j = j pi / (2 lambda), j = 1..K, with alpha_K >= FMAX. All prime-side
and archimedean matrix entries reduce to K one-dimensional sums or integrals
(closed forms in `weil_window.py`); parity sectors decouple exactly.

## Validation (`validate.py`, `validation.json`)

| Check | Result |
|---|---|
| Closed-form sine correlations vs quadrature (5 pairs) | agree to 1e-8 |
| Zeta: explicit formula vs sum over first 40 zeros, two modulated Gaussians | differ by 1.2e-14 and 6.4e-18 |
| Davenport-Heilbronn zeros below height 60: sign changes on the line vs winding number on [-0.5, 1.5] x [0.05, 60] | 28 and 28.000 |
| Davenport-Heilbronn: explicit formula (recursive Lambda_D) vs sum over those 28 zeros, two tests | differ by 9.3e-15 and 1.6e-15 |
| Sine-basis matrix entries vs generic functional on the same h (4 entries, zeta, lambda 1.5) | agree to 1e-5 relative (quadrature limit of the check) |
| Zeta form over the whole scan | min eigenvalue / lambda between -1e-12 and +1e-6: zero at working precision, never negative beyond noise |

The off-line zeros used, located by Newton iteration from literature
neighbourhoods and validated by residual (about 1e-22):

| Height T | delta = Re rho - 1/2 |
|---|---|
| 85.699348 | 0.308517 |
| 176.702461 | 0.224258 |
| 114.163343 | 0.150830 |
| 166.479306 | 0.074356 |

## Results

**Scan (`run_scan.py`, `scan.json`; FMAX = 130).** Min eigenvalue divided
by lambda (the form per unit L2 norm of g):

| lambda | zeta | Davenport-Heilbronn | resonant frequency of the negative direction |
|---|---|---|---|
| 1.0 | -1e-15 | +4e-5 | none |
| 1.5 | -7e-15 | +4e-16 | none |
| 2.0 | -4e-14 | -0.756 | 84.6 |
| 3.0 | -1e-13 | -3.68 | 86.5 |
| 4.0 | -4e-13 | -10.64 | 85.2 |
| 5.0 | -1e-12 | -24.72 | 85.3 |

Convergence (`refine.json`): at lambda = 4 the Davenport-Heilbronn value is
-10.6435 with FMAX 130 and panel 0.01, -10.6435 with panel 0.004, -10.680 with
FMAX 200. Stable to the reported digits; the FMAX change adds a little freedom.

**First detection window per zero (`law.py`, `law.json`; FMAX = 200,
lambda step 0.1).** lambda* is the first lambda at which a direction with
negative eigenvalue below -1e-9 lambda resonates within 4 of the zero's height.

| T | delta | lambda* observed | 1/(2 delta) | (1/2) log(T / 2pi) | lambda* minus that |
|---|---|---|---|---|---|
| 85.70 | 0.3085 | 1.9 (a -2e-7 precursor at 1.8) | 1.62 | 1.31 | 0.59 |
| 114.16 | 0.1508 | 2.2 | 3.31 | 1.45 | 0.75 |
| 176.70 | 0.2243 | 2.3 | 2.23 | 1.67 | 0.63 |
| 166.48 | 0.0744 | 2.4 | 6.72 | 1.64 | 0.76 |

The offset-based guess 1/(2 delta) in `PROPOSAL.md` is refuted for the two
smaller offsets (predicted 3.3 and 6.7, observed 2.2 and 2.4). The height-based
law lambda* = (1/2) log(T / 2pi) + 0.6 to 0.8 fits all four, with the smaller
offsets at the top of that band. The stated prediction interval [1.6, 6.5] held
for the first zero (1.9) but for the wrong reason.

**Magnitude versus offset.** At lambda = 4 the negative eigenvalues per unit
norm are -10.68, -4.49, -1.97, -0.43 for delta = 0.3085, 0.2243, 0.1508,
0.0744, i.e. -(112, 89, 87, 78) delta^2. The detection mechanism is the second
order term: choose ghat to vanish at 1/2 + iT with a large derivative, so that
2 Re[ghat(1/2+delta+iT) conj ghat(1/2-delta+iT)] is about -delta^2 |ghat'|^2.
The window does not need 2 delta lambda of order one; it needs enough
band-limited degrees of freedom to annihilate the on-line zeros near T.

**Near-null space of the zeta form (`refine.json`, `law.json`).** With
frequencies up to FMAX = 130, the number of eigenvalues below 1e-10 is 68 of
170 (lambda 2), 150 of 253 (lambda 3), 233 of 336 (lambda 4), 284 of 418
(lambda 5); the rank stays near 103, about twice the roughly 43 zeta zeros
below 130 plus a boundary band. With FMAX = 400 the near-null directions
resonate up to frequency 74 at lambda 1.5, 262 at lambda 2, and at least 382
(basis limit) at lambda 2.5, against 2 pi e^{2 lambda} = 126, 343, 933. This
is the Paley-Wiener count: an entire function of exponential type lambda
restricted to frequencies below F has about 2 lambda F / pi real degrees of
freedom while the zeros below F impose about 2 N(F) conditions, so directions
that vanish at every zero below F exist once (1/2pi) log(F/2pi) < lambda/pi,
i.e. F < 2 pi e^{2 lambda}. Their residual energy comes from zeros above F and
is far below working precision here. Detection of an off-line zero at height T
starts when T sits at roughly a quarter of that crossover height, which is the
+0.7 in the law above.

## What this does and does not say

- It is a diagnostic law for the **plain** window-restricted Weil form:
  an off-line zero at height T is visible to tests of support lambda once
  lambda exceeds about (1/2) log(T / 2pi) + 0.7, almost independently of its
  offset, with the negative energy scaling like the offset squared. Equivalently,
  a window lambda tests zeros up to height of order e^{2 lambda}, and positivity
  at window lambda is a statement about that height range only. This is
  `prop:v121-cofinal-rh` (finite windows do not accumulate) made quantitative
  for this form: the height reached grows exponentially in lambda, and
  `prop:v125-cutoff-cost` says lambda itself costs exponentially.
- The near-null count is a possible explanation to **test**, not a claim, for
  the size of the certified complete-form ground (mu_0 below 2.5e-75 at
  lambda = 4 in v1.40): a type-lambda direction that vanishes at every zero
  below the crossover has energy only from zeros above it. Whether the
  manuscript's semilocal Sonine form has the same degree-of-freedom count is
  for the manuscript's prolate discussion to settle; nothing is transferred here.
- No new arithmetic estimate, no uniform floor, no cofinal statement, no
  G2 or RH claim. The Davenport-Heilbronn coefficients are the only arithmetic
  input that differs from zeta, and the form detects that difference exactly as
  Weil's criterion says it must.

## Wall check

**Wall check: Distinct test.** Closest result: `prop:v121-cofinal-rh`,
NS-100 controls. What changed: the object (a function with known off-line
zeros) and the question (detection window versus height and offset). Outcome:
a measured law, one refuted guess (the 1/(2 delta) scaling), one hypothesis
handed to the manuscript lane (the near-null count versus the 1e-75 ground).
No route opened or closed.

## Replay

```
cd <repo root>
.venv/bin/python evidence/diag_ns103_window_calibration/validate.py   # ~3 min
.venv/bin/python evidence/diag_ns103_window_calibration/run_scan.py   # seconds
.venv/bin/python evidence/diag_ns103_window_calibration/refine.py
.venv/bin/python evidence/diag_ns103_window_calibration/law.py
```
Requires numpy 2.5, mpmath 1.4, and `controls/davenport_heilbronn.py`.
