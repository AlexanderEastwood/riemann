# NS-105 proposal (pre-registered in draft PR before the claim)

```
Proposal: Evaluate the transform F of the unchanged archived normalized even
  trial (v1.26 column 16, modes 0-4096; the same f as v1.42/1.43 and NS104)
  on a dense grid of heights t in [0, 400], away from the zeta ordinates, at
  1024 bits with a 1280-bit replay on a subset. Report the envelope of |F(t)|
  per height band, the heights of F's real sign changes versus the zeta
  ordinates, and the ratio of the envelope above the NS104-corrected
  crossover 32 pi = 100.53 to the envelope below it.

Shared-input group: DISTINCT diagnostic of an existing certificate (CCM-LIMIT
  for relevance, frozen; no thaw attempted). Closest nodes: simpleeven4,
  groundzero4resolution (v1.40-1.43), NS104 (values at gamma_j +/- 0.01 only),
  NS103 (plain-form near-null count). NS104 evaluated F only at and beside
  the zeta ordinates; it does not report F between them or above gamma_64.

Arithmetic input beyond the functional equation: the exact original zeta
  prime weights, gamma and pole terms frozen into the archived W4 trial.
  No new arithmetic estimate is proposed.

Control screen: not applicable, with the same concrete mismatch NS104
  recorded: no matched Davenport-Heilbronn W4 trial, Schur certificate or
  normalization exists. The unchanged controls/example_screen.py is not a
  screen of this prediction. NS100/101 controls have no archived ground.
  No positivity implication is admitted through this exception.

Wall check: Distinct test (spectral profile of an archived object).
  Closest result: NS104; v1.40-1.43. What changes: the sampled set (between
  and beyond the ordinates, not at them) and the question (where the
  transform's mass sits, not whether it vanishes at zeros).

Stated predictions, falsifiable on this object:
  P1. The envelope of |F(t)| decays roughly exponentially in t from the
      first ordinates onward, and is below 1e-30 for all t above 100.53
      (NS104 slopes: 3e-3 at gamma_1, 1e-24 at gamma_29, 7e-37 at gamma_64).
  P2. Below 100.53, the real sign changes of F occur only near zeta
      ordinates: the count of sign changes on [0, T] equals N(T) for
      T <= 100, with each change within 0.05 of an ordinate.
  P3. Above 100.53, F continues to change sign near every ordinate as far
      as the envelope stays above the working precision.

What success changes: the archived ground-transform structure (real zeros,
  zero near gamma_1) is then described as a type-(log 4) function whose
  mass sits below the crossover and which avoids the roughly 30 ordinates
  there. That is a description of the certified object, not a convergence
  statement and not an RH or G2 claim. It would sharpen the v1.40-1.43
  scope paragraph added by NS104.
What failure changes: if the envelope above 100.53 is comparable to the
  envelope below, or sign changes appear away from ordinates, the
  spectral-confinement reading is rejected and recorded; NS104's finite
  finding stands unchanged. No route opens or closes either way.

Budget: one bounded scan (about 1600 grid points plus midpoints), one PR,
  no new eigensolve, cutoff, window or precision search.
Version bump expected: no (diagnostic; evidence/diag_ns105_trial_spectrum).
```
