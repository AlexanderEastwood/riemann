# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.37**.

**G2 and the Riemann Hypothesis remain open.** The update proves an
obstruction to a scalar sufficient estimate, not a negative Weil-form test.

## Current manuscript

- [Complete LaTeX](fixed_space_prime_action_v1.tex)
- [Research log and candidate register](RH_G1_G2_research_log.md)
- [Revision notes](v1_revision_notes.md)
- [Checksums and provenance](github_sync/v1.37_manifest.json)

There is one live manuscript at the root. Delivery is **LaTeX only** at the
author's request. Previous PDFs and superseded evidence are historical
material in the [archive](archive/README.md) and Git history.

## New in v1.37

v1.36 showed that one uniform finite ordinary lower floor on the complete
small-residual complement would suffice. v1.37 tests whether the older
scalar primitive estimate could meet this weaker target.

It cannot: for the exact arithmetic symbol, its optimal scalar error
`a Delta(beta_a)` tends to infinity. The pointwise infimum of `beta_a`
also tends to minus infinity. Both conclusions are unconditional.

The proof uses a nonnegative frequency probe whose Fourier transform
vanishes at the two physical cutoff endpoints. Under RH its pairing with
the exact symbol retains a negative cutoff side lobe around a zero.
Any bounded cofinal scalar certificate would itself imply RH via v1.36,
then contradict that pairing. The linear rates are RH-conditional; no
unconditional linear rate is asserted.

The probe is not a physical squared Paley--Wiener transform. Therefore
these scalar obstructions do not refute positivity of the physical form.
The signed concentration estimate, retaining favorable and unfavorable
levels jointly, remains open in both parities. No G2 sign gap was closed.

- [Proof and novelty report](g2_scalar_budget_no_go/research_report.md)
- [Proof excerpt](g2_scalar_budget_no_go/new_section.tex)
- [Independent adversarial review](g2_scalar_budget_no_go/adversarial_review.md)
- [Probe checks](g2_scalar_budget_no_go/check_probe.py)
- [Check results](g2_scalar_budget_no_go/probe_results.json)

The result is a continuation and rejection of a prior proposal, not a new
positive mechanism. The ingredients are classical; worldwide novelty is
not claimed. Numerical quadrature is diagnostic and not a proof.

## Saved-copy and reproduction status

Canonical ChatGPT file replacements for the current LaTeX, log and notes
failed during transfer. Those saved copies remain v1.34; use this repository
for v1.37. No stale saved-file link is labelled current.

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

## Validation

Independent mathematical adversarial review passed. The complete source
passed three draft-mode LaTeX validation runs without warnings or unresolved
references. **No PDF was generated.** Exact analytic constants are supplied
in the proof; separate standard-library quadrature checks the probe scaling.
