# `evidence/v126/g2_window_resolution/`

Post-v1.25 checkpoint — DIAGNOSTIC: finite window-resolution audit at lambda=8 (heads 36 and 64, cuts 256/384/512, 4096 bits). `window_resolution_checkpoint.md` states it "does not add a complete lambda8 sign certificate or prove G2/RH", and `window_resolution_probe.py` that "every sign here is finite dimensional". Linked from the research map for the scalar far majorant (`prop:v125-cutoff-cost`).

**Start here:** [`window_resolution_checkpoint.md`](window_resolution_checkpoint.md), [`review_window_resolution.md`](review_window_resolution.md)

**Manifest:** [`v1.26_manifest.json`](../../../manifest/v1.26_manifest.json), [`v1.26_evidence_recovery.json`](../../../manifest/v1.26_evidence_recovery.json), [`README_v126_evidence_recovery.md`](../../../manifest/README_v126_evidence_recovery.md)

## Files

- `head_reduction_audit.py` (1 KB) — Physical one-dimensional head audit by exact finite shorting.
- `mixed_refinement.py` (6 KB) — Directional mixed inverse diagnostic, with exact frozen inputs and Arb actions. Finite-prefix mixed values are explicitly NOT complete-tail certificates.
- `package_resolution_checkpoint.py` (3 KB) — (no description in file)
- `posterior_trial.py` (6 KB) — Finite preconditioned trials, verified by the COMPLETE new Weil residual. Candidate iteration is not a positivity proof. All gates include remote rows.
- `refine_inverse.py` (5 KB) — Reproducible Arb experiments for the complete lambda=4 tail inverse. Finite-prefix experiments are not certificates of the complete Schur sign.
- `resolution_l8_h36_cuts256_384_b4096_k256_forms.json` (2.0 MB) — (no description in file)
- `resolution_l8_h36_cuts256_384_b4096_k256_forms_constant_head.json` (2 KB) — (no description in file)
- `resolution_l8_h36_cuts256_384_b4096_k256_metric_256_384.json` (954 KB) — (no description in file)
- `resolution_l8_h36_cuts256_384_b4096_k256_report.json` (2 KB) — (no description in file)
- `resolution_l8_h64_cuts256_384_512_b4096_k256_forms.json` (10.7 MB) — (no description in file)
- `resolution_l8_h64_cuts256_384_512_b4096_k256_forms_constant_head.json` (3 KB) — (no description in file)
- `resolution_l8_h64_cuts256_384_512_b4096_k256_metric_256_384.json` (3.2 MB) — (no description in file)
- `resolution_l8_h64_cuts256_384_512_b4096_k256_metric_384_512.json` (3.1 MB) — (no description in file)
- `resolution_l8_h64_cuts256_384_512_b4096_k256_report.json` (3 KB) — (no description in file)
- `review_window_resolution.md` (12 KB) — Adversarial review: finite window resolution at lambda=8
- `simultaneous_trial.py` (9 KB) — Complete matrix Schur verification of independently frozen finite trials. No finite-solve convergence or positivity is used as a certificate.
- `window_resolution_checkpoint.md` (6 KB) — Post-v1.25 window-resolution checkpoint — September 21, 2026
- `window_resolution_probe.py` (3 KB) — Cutoff/head resolution audit. Every sign here is finite dimensional.
- `window_scaling_probe.py` (7 KB) — Growing-window diagnostics. Finite corrections are NOT complete tail uppers. Fresh analytic far-cut bounds are independently certified at every window.
