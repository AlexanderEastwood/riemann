# `evidence/v126/`

HISTORICAL SNAPSHOT — the complete extracted original **v1.26** cumulative bundle (468 files, byte-for-byte against the release ZIP per the [recovery record](../../manifest/README_v126_evidence_recovery.md)); manuscript v1.26, 170 pages, PDF and TeX at this root with dated aliases.

This snapshot holds the project's only positive result, `W_4 >= 0` in both parity sectors: even sector in [`g2_simultaneous/`](g2_simultaneous/) (v1.25), odd sector in [`g2_odd_complement/`](g2_odd_complement/) (v1.26). Both are marked RESTORED in [../MISSING.md](../MISSING.md).

Root-level `check_*.py` / `*_checks.json` pairs are floating-point or rational-model convention checks (not certificates, per their docstrings). The remaining `g2_*` bundles (v1.11–v1.24) are byte-identical to [`../v124/`](../v124/), except that `g2_low_schur/` carries one extra witness file and `g2_window_resolution/` exists only here.

**Start here:** [`README_v126.md`](README_v126.md), [`REPRODUCE_v121.md`](REPRODUCE_v121.md)

**Manifest:** [`v1.26_manifest.json`](../../manifest/v1.26_manifest.json), [`v1.26_evidence_recovery.json`](../../manifest/v1.26_evidence_recovery.json), [`README_v126_evidence_recovery.md`](../../manifest/README_v126_evidence_recovery.md)

## Subdirectories

- [`audits/`](audits/) — historical audit documents
- [`g2_certificate/`](g2_certificate/) — v1.12 finite Weil matrix certificate (lambda=3, N=64)
- [`g2_deep_next/`](g2_deep_next/) — v1.14 endpoint / closed-operator continuation
- [`g2_deep_research/`](g2_deep_research/) — G2 research assessment note
- [`g2_ground_order/`](g2_ground_order/) — v1.17 complete ground ordering at lambda=3
- [`g2_growing_sign/`](g2_growing_sign/) — v1.19 unsigned prime-norm obstruction (analytic)
- [`g2_inverse_refinement/`](g2_inverse_refinement/) — v1.22 inverse refinement
- [`g2_low_schur/`](g2_low_schur/) — v1.20 low-head Schur correction at lambda=4
- [`g2_mixed_complete/`](g2_mixed_complete/) — v1.23 complete mixed correlations
- [`g2_odd_complement/`](g2_odd_complement/) — v1.26 complete odd-sector sign at lambda=4
- [`g2_posterior_trial/`](g2_posterior_trial/) — v1.24 complete Schur-direction certificate
- [`g2_schur_cancellation/`](g2_schur_cancellation/) — v1.21 finite K positivity and source-complement cancellation
- [`g2_schur_directional/`](g2_schur_directional/) — v1.16 complete fixed-window positivity at lambda=3
- [`g2_signed_tail/`](g2_signed_tail/) — v1.15 operator residual and sharp Fourier tail at lambda=3
- [`g2_simultaneous/`](g2_simultaneous/) — v1.25 complete even-sector certificate at lambda=4
- [`g2_source_certificate/`](g2_source_certificate/) — v1.13 exact-source certificate (lambda=3, N=64)
- [`g2_spectral_pilot/`](g2_spectral_pilot/) — v1.11 numerical spectral pilot (not a certificate)
- [`g2_uniform_endpoint/`](g2_uniform_endpoint/) — v1.18 continuum endpoints and complement reduction (analytic)
- [`g2_weighted_signed/`](g2_weighted_signed/) — v1.20 signed energy control on the complete lambda=4 tail
- [`g2_window_resolution/`](g2_window_resolution/) — post-v1.25 finite window-resolution diagnostics at lambda=8
- [`history/`](history/) — historical manuscript snapshots

## Files

- `README_v126.md` (650 B) — Complete working manuscript v1.26
- `REPRODUCE_v121.md` (1 KB) — Complete manuscript v1.21 reproduction
- `RH_G1_G2_research_log.md` (224 KB) — RH manuscript research log
- `band_cut_checks.json` (12 KB) — (no description in file)
- `bv_radical_passage_checks.json` (3 KB) — (no description in file)
- `check_band_cut.py` (4 KB) — Sharp-band transform checks; rational model only, no zeta/Weil claims.
- `check_bv_radical_passage.py` (2 KB) — Convention check for the primitive-tail proof, not proof evidence for RH. The compact even test source h(x)=x^2-(5/3)x^4, |x|<=1, has h(0)=0, integral h=0 and a nonzero e…
- `check_copoisson_adjoint.py` (4 KB) — Regularized co-Poisson adjoint checks; no zero or RH experiment. python3 check_copoisson_adjoint.py > copoisson_adjoint_checks.json The toy source is D phi, phi=(t-1)^3(2…
- `check_fredholm_shell.py` (3 KB) — Floating-point Fredholm sign/scale checks, not an RH experiment. Usage: python3 check_fredholm_shell.py > fredholm_shell_checks.json Interval data are arbitrary complex p…
- `check_full_projection.py` (4 KB) — Full Fourier projection: finite identities and holomorphic rational check. No zeta zeros or Weil matrix are used.
- `check_prolate_source.py` (3 KB) — High-precision Legendre-Galerkin illustrations, not interval certificates. Even angular PSWFs solve -((1-x*x)y')' + c*c*x*x*y = theta*y on [-1,1], with L2 norm one.
- `check_resolvent_endpoints.py` (3 KB) — Rational-model check of the corrected resolvent endpoint asymptotics. This model contains no zeta zeros and tests no RH or Weil-form assertion.
- `check_sampler.py` (5 KB) — Finite CCM checks for the sampler compatibility note. Requires numpy, scipy, mpmath. Run: python3 check_sampler.py Outputs sampler_checks.json beside this file.
- `check_section19_metric.py` (5 KB) — Finite first-slot-linear metric checks; rational model, not zeta zeros. The model has a length-two Jordan chain at mu and one further eigenvector.
- `check_weil_action.py` (4 KB) — Actual finite Weil action at the first known critical-line zero. Uses the historical arithmetic matrix implementation, including its logarithmic diagonal.
- `copoisson_adjoint_checks.json` (2 KB) — (no description in file)
- `finite_identity_checks.json` (625 B) — description: Complex-vector algebra checks; floating point, not certified bounds.
- `fixed_space_prime_action_v1.pdf` (1.2 MB) — (no description in file)
- `fixed_space_prime_action_v1.tex` (532 KB) — \textbf{Fixed-Space Prime Compatibility in Burnol's Sonine Quotients
- `fixed_space_prime_action_v1_26.pdf` (1.2 MB) — (no description in file)
- `fixed_space_prime_action_v1_26.tex` (532 KB) — \textbf{Fixed-Space Prime Compatibility in Burnol's Sonine Quotients
- `fredholm_shell_checks.json` (5 KB) — (no description in file)
- `full_projection_checks.json` (6 KB) — (no description in file)
- `prolate_source_checks.json` (3 KB) — (no description in file)
- `resolvent_endpoint_checks.json` (2 KB) — (no description in file)
- `sampler_checks.json` (6 KB) — description: Floating-point illustrations; not certified bounds.
- `section19_metric_checks.json` (5 KB) — (no description in file)
- `v121_SHA256SUMS.json` (3 KB) — (no description in file)
- `v1_revision_notes.md` (56 KB) — Revision notes - full manuscript v1.26
- `v1_validation.json` (113 KB) — (no description in file)
- `verify_finite_identities.py` (3 KB) — Check the v1 finite identities using complex vectors and a real CCM matrix. Run beside check_sampler.py: python verify_finite_identities.py These are reproducible floatin…
- `weil_action_checks.json` (3 KB) — (no description in file)
