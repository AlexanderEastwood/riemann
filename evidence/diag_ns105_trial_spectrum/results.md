# NS-105: spectral profile of the archived lambda=4 trial between and beyond the ordinates

**Diagnostic of the frozen finite trial, not a certificate and not a complete-ground statement.**
Arb evaluation (1024 bits, replayed at 1280 bits) of the unchanged archived
normalized even trial, column 16, modes 0-4096, the same object NS104 and
v1.42/1.43 use, through the v1.42 loader. No new eigensolve, cutoff, window,
zero-tail bound, G2 or RH claim. Pre-registered in draft PR #59 before the row
claim; the unchanged proposal is `PROPOSAL.md`.

## Question and predictions

NS104 evaluated the trial transform F only at the zeta ordinates and 0.01 to
either side. This scan samples F on the grid t = 0.05, 0.10, ..., 400 and asks
where its mass sits and where its real sign changes are. `PROPOSAL.md` stated
three predictions before the run:

- P1: |F| decays roughly exponentially and is below 1e-30 for all t above the
  NS104-corrected crossover 32 pi = 100.53.
- P2: below 100.53, F changes sign only near zeta ordinates, with count N(T).
- P3: above 100.53, F keeps changing sign near every ordinate as long as the
  envelope stays above working precision.

## Results (`scan_trial.py`, `scan-1024bits.json`, `scan-1280bits.json`)

**Envelope.** Maximum of |F| per 20-unit band, log10:

| band | log10 max abs F |
|---|---|
| 0-20 | -0.062 |
| 20-40 | -3.974 |
| 40-60 | -9.549 |
| 60-80 | -15.135 |
| 80-100 | -19.692 |
| 100-120 | -24.251 |
| 120-140 | -28.338 |
| 140-160 | -32.43 |
| 160-180 | -34.897 |
| 180-200 | -36.943 |
| 200-220 | -37.6 |
| 220-240 | -37.769 |
| 240-260 | -37.849 |
| 260-280 | -37.947 |
| 280-300 | -38.03 |
| 300-320 | -38.255 |
| 320-340 | -38.256 |
| 340-360 | -38.484 |
| 360-380 | -38.36 |
| 380-400 | -38.6 |

The decay is close to exponential, 0.20 to 0.28 decades per unit height
between 20 and 160, and then flattens. Above 200 the profile sits on a
plateau: max 2.51e-38, median 2.07e-39, i.e. 0.51 and 0.042 times
sqrt(rho) = 4.95e-38, where rho = 2.4536e-75 is the trial Rayleigh quotient.
The interval radii are below 1e-304 everywhere, so the plateau is the
trial's actual transform, not precision noise.

**Sign changes versus ordinates.** A sign change is counted when both
neighbouring grid values exclude zero at working precision.

| T | sign changes of F below T | N(T) | changes within 0.05 of an ordinate |
|---|---|---|---|
| 50.0 | 10 | 10 | 10 |
| 100.0 | 29 | 29 | 29 |
| 100.53 | 29 | 29 | 29 |
| 150.0 | 52 | 52 | 52 |
| 200.0 | 79 | 79 | 73 |
| 300.0 | 126 | 138 | 85 |
| 400.0 | 172 | 202 | 89 |

No sign change below 100 is unmatched. Between 150 and 200, 21 of 27 changes
are within 0.05 of an ordinate. Above 200 the counts fall below N(T) and the
matching stops: the last matched change is at 396.3 (ordinate 200), but most
changes there are not near ordinates.

**Replay.** 1280 bits with identical parameters (`validate_replay.py`,
`validation.json`): all 8000 intervals overlap, midpoints differ by at
most 0.00e+00 absolutely, sign-change heights and all counts are
identical, and the envelope table is identical to three decimals.

## Reading against the predictions

- **P1: shape confirmed, threshold wrong.** The envelope is exponential-like,
  but crosses 1e-30 at t = 118.8, not at 100.53; at the crossover it is
  3.4e-25. The ratio of the maximum above the crossover to the maximum below
  it is 4.0e-25. The 1e-30 figure in the proposal was a guess and is recorded
  as missed.
- **P2: confirmed.** 29 sign changes below 100, N(100) = 29, every one within
  0.05 of an ordinate, none elsewhere.
- **P3: confirmed with a sharper end point than proposed.** The one-to-one
  matching continues to about 150 and degrades between 150 and 200, which is
  exactly where the envelope reaches the sqrt(rho) plateau. It does not
  continue "as long as precision allows"; it continues as long as |F| exceeds
  the residual-energy scale. Below the plateau F is no longer forced to
  vanish at ordinates.

## What this describes, and what it does not

The archived trial is a function supported in [-log 4, log 4] whose transform
carries essentially all of its mass below height about 150, decays
exponentially through that range, vanishes near every zeta ordinate there
(29 below the crossover, 52 below 150), and then sits at the level allowed by
its energy budget. That is a description of this finite object, consistent
with reading the small Rayleigh quotient as "avoid the ordinates where the
mass is, spend the budget elsewhere". It is not a proof of a null-space
mechanism, not a statement about the complete ground xi_4 (NS104: no transfer
of trial roots beyond gamma_1 under the displayed bounds), not a convergence
statement, and it supplies no arithmetic estimate. Nothing here bears on
zeros of zeta beyond what v1.40-1.43 already certify.

## Wall check

**Wall check: Distinct test** of a stated prediction on an archived object;
**Same open gap** for CCM-LIMIT. Closest: NS104, v1.40-1.43, NS103. What
changed: the sampled set and the question. No group thawed; no route opened
or closed; no version.

## Replay

```
cd <repo root>
.venv/bin/python evidence/diag_ns105_trial_spectrum/scan_trial.py --bits 1024 --output /tmp/ns105-1024.json   # ~70 s
.venv/bin/python evidence/diag_ns105_trial_spectrum/scan_trial.py --bits 1280 --output /tmp/ns105-1280.json   # ~90 s
.venv/bin/python evidence/diag_ns105_trial_spectrum/validate_replay.py
```
Fresh output paths are required. Depends on `evidence/v142/certify_ground_zero.py`
and the v1.26 witness archive; hashes are recorded in the scan JSON.
