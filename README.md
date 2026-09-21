# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.38**.

**G2 and the Riemann Hypothesis remain open.** This update tests a common finite lower floor; it does not prove the required cofinal bound.

## Current manuscript

- [Complete LaTeX](fixed_space_prime_action_v1.tex)
- [Research log and candidate register](RH_G1_G2_research_log.md)
- [Revision notes](v1_revision_notes.md)
- [Checksums and provenance](github_sync/v1.38_manifest.json)

One live manuscript remains at the root. Delivery is **LaTeX only**. Previous PDFs, superseded evidence and provenance are in the [archive](archive/README.md) and Git history.

## New in v1.38

Both complete parity forms at lambda = 5, 6, 8 satisfy **W>=-8I**. The same parameters work throughout: additive shift 8, head cutoff 256, explicit residual cutoff 4096, moment order 16, Young parameter 1/10 and zero solve. Each window's coefficients and tail constants are freshly evaluated. No disproved positive tail metric is used.

The six certificates include the infinite tail and pass at 160 bits, then at 256 bits with the identical frozen dyadic witnesses. Each finite-support trial has a certified positive Rayleigh quotient below 1e-16. Therefore the true spectral edges lie between -8 and 1e-16; their signs are not determined.

| lambda | even generalized-margin lower | odd generalized-margin lower |
|---|---:|---:|
|5|0.8430|0.9190|
|6|0.7166|0.7620|
|8|0.2474|0.1022|

These are lower bounds for `1-lambda_max(U,K)` of the shifted certificate, not resolution margins or whitening row margins. Their decline does not establish a falling physical spectral edge.

A shift of 0.001 barely lowers the old cutoff cost. A shift of 8 makes the lambda = 8 remote gates pass already at N = 43 even and N = 204 odd. This is a substantial finite computational saving. The proved requirement `N+1>L exp(M_phi-delta)` still makes the same scalar comparison exponential in lambda for every bounded shift. No new arithmetic cancellation mechanism is claimed.

- [Research report and exact remaining target](g2_finite_floor/research_report.md)
- [Analytic proof](g2_finite_floor/new_section.tex)
- [Higher-precision complete certificates](g2_finite_floor/replay_b256.json)
- [Frozen dyadic witnesses](g2_finite_floor/dyadic_witnesses.npz)
- [Adversarial review](g2_finite_floor/adversarial_review.md)
- [Reproduction instructions](g2_finite_floor/REPRODUCE.md)

The lambda = 8 lower floor transfers down to all 1 < lambda ≤ 8 by physical support consistency. A bounded interval is still not a cofinal family. **No G2 sign gap was closed.**

## Saved-copy and reproduction status

Canonical ChatGPT file replacements for the current LaTeX, log and notes
failed during transfer. Those saved copies remain v1.34; use this repository
for v1.38. No stale saved-file link is labelled current.

The original **v1.26 cumulative reproduction bundle has been recovered**.
It includes both missing final λ=4 certificate directories:

- [Complete even-sector evidence (`g2_simultaneous`)](archive/v1.26_snapshot/g2_simultaneous/)
- [Complete odd-sector evidence (`g2_odd_complement`)](archive/v1.26_snapshot/g2_odd_complement/)
- [Original cumulative ZIP and checksum](https://github.com/AlexanderEastwood/riemann/releases/tag/v1.26-evidence)
- [Recovery provenance and replay scope](github_sync/README_v126_evidence_recovery.md)

The extracted snapshot preserves every original file and its relative
layout. Final saved-ingredient proof gates and the exact shared-head check
were replayed successfully; this publication did not regenerate witnesses
or rerun every residual assembly. The historical bundle is not the current
manuscript.

The complete later v1.34 cumulative ZIP remains unavailable. Restoring the
v1.25/v1.26 positivity evidence does not reconstruct that later archive or
constitute a complete cumulative reproduction release for the current work.

**Two of four tracked evidence gaps remain open:** the λ=5 disproof
witnesses through v1.28 and the v1.31–v1.34 concentration evidence and
diagnostics. See [the evidence availability ledger](evidence/MISSING.md)
for the two restored groups and the two remaining open groups.


## Validation

The mathematical setup was adversarially reviewed. Every complete floor and frozen trial was replayed with outward arithmetic at higher precision. Source validation uses LaTeX draft mode. **No PDF is generated or delivered.**
