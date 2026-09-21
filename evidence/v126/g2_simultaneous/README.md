# `evidence/v126/g2_simultaneous/`

Manuscript v1.25 — CERTIFICATE bundle: the complete even-sector certificate at lambda=4 (simultaneous complete Schur verification of frozen finite trials, M=4096, 16 steps, 768/896 bits; certified relative margin), plus growing-window diagnostics (`window_scaling_*`) that are finite-dimensional and, per `window_scaling_probe.py`, "NOT complete tail uppers". `prop:v125-even-complete`; marked RESTORED in [../../MISSING.md](../../MISSING.md).

`simultaneous_replay_README.md` says odd positivity remains open; that describes the v1.25 checkpoint — the odd sector is closed in [`../g2_odd_complement/`](../g2_odd_complement/).

**Start here:** [`simultaneous_replay_README.md`](simultaneous_replay_README.md), [`simultaneous_integration_review.md`](simultaneous_integration_review.md), [`adversarial_simultaneous_review.md`](adversarial_simultaneous_review.md), [`window_scaling_report.md`](window_scaling_report.md)

**Manifest:** [`v1.26_manifest.json`](../../../manifest/v1.26_manifest.json), [`v1.26_evidence_recovery.json`](../../../manifest/v1.26_evidence_recovery.json), [`README_v126_evidence_recovery.md`](../../../manifest/README_v126_evidence_recovery.md)

## Subdirectories

- [`input/`](input/) — v1.24 input manuscript
- [`renders/`](renders/) — contact-sheet renders

## Files

- `adversarial_simultaneous_review.md` (12 KB) — Simultaneous complete Schur verification and sharper remote bounds
- `adversarial_window_scaling_review.md` (5 KB) — Adversarial review of the growing-window probe
- `build_complete_pdf.py` (1 KB) — Compile in a fresh directory; install only a closed, parseable full PDF.
- `complete_even_relative_margin_b768.json` (2 KB) — (no description in file)
- `complete_even_relative_margin_b896.json` (2 KB) — (no description in file)
- `complete_margin.py` (2 KB) — Certified generalized margin and diagnostics for the complete even certificate.
- `document_v125.py` (12 KB) — (no description in file)
- `integrate_v125.py` (7 KB) — (no description in file)
- `joint_remote_gate.py` (3 KB) — Whole-head certificate with one joint remote Gram, retaining its cross block.
- `mixed_probe_J65536_b768.json` (3 KB) — (no description in file)
- `mixed_probe_J65536_b896.json` (3 KB) — (no description in file)
- `mixed_refinement.py` (6 KB) — Directional mixed inverse diagnostic, with exact frozen inputs and Arb actions. Finite-prefix mixed values are explicitly NOT complete-tail certificates.
- `package_v125.py` (7 KB) — (no description in file)
- `posterior_trial.py` (6 KB) — Finite preconditioned trials, verified by the COMPLETE new Weil residual. Candidate iteration is not a positivity proof. All gates include remote rows.
- `quantify_head_error.py` (2 KB) — Certified ordinary-head lower errors, never positivity from an inconclusive bound.
- `refine_inverse.py` (5 KB) — Reproducible Arb experiments for the complete lambda=4 tail inverse. Finite-prefix experiments are not certificates of the complete Schur sign.
- `render_v125.py` (1 KB) — (no description in file)
- `replay_finite_margin.py` (2 KB) — Replay the finite lambda8 generalized-margin bracket; no complete-tail claim.
- `simultaneous_even_M4096_s16_ingredients_b768.json` (273 KB) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_ingredients_b768.json` (2.1 MB) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_ingredients_b896.json` (2.2 MB) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_joint_lower_b768.json` (118 KB) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_joint_report_b768.json` (937 B) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_ordinary_error_b768.json` (2 KB) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_report_b768.json` (2 KB) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_report_b896.json` (2 KB) — (no description in file)
- `simultaneous_even_M4096_s16_normalized_witness.json.gz` (5.4 MB) — (no description in file)
- `simultaneous_even_M4096_s16_ordinary_error_b768.json` (4 KB) — (no description in file)
- `simultaneous_even_M4096_s16_report_b768.json` (3 KB) — (no description in file)
- `simultaneous_even_M4096_s16_witness.json.gz` (5.0 MB) — (no description in file)
- `simultaneous_insert.tex` (10 KB) — A simultaneous complete Schur certificate
- `simultaneous_integration_review.md` (3 KB) — Final adversarial integration review: v1.25
- `simultaneous_odd_M4096_s16_normalized_ingredients_b768.json` (5.5 MB) — (no description in file)
- `simultaneous_odd_M4096_s16_normalized_report_b768.json` (3 KB) — (no description in file)
- `simultaneous_odd_M4096_s16_normalized_witness.json.gz` (5.1 MB) — (no description in file)
- `simultaneous_odd_M4096_s4_normalized_ingredients_b768.json` (5.5 MB) — (no description in file)
- `simultaneous_odd_M4096_s4_normalized_ordinary_error_b768.json` (4 KB) — (no description in file)
- `simultaneous_odd_M4096_s4_normalized_report_b768.json` (3 KB) — (no description in file)
- `simultaneous_odd_M4096_s4_normalized_witness.json.gz` (5.1 MB) — (no description in file)
- `simultaneous_replay_README.md` (3 KB) — v1.25 complete even certificate and growth audit
- `simultaneous_trial.py` (9 KB) — Complete matrix Schur verification of independently frozen finite trials. No finite-solve convergence or positivity is used as a certificate.
- `window_scaling_far_cuts_b320.json` (3 KB) — (no description in file)
- `window_scaling_far_cuts_b384.json` (3 KB) — (no description in file)
- `window_scaling_l3_even_r256_o384_b4096.json` (1 KB) — (no description in file)
- `window_scaling_l4_even_r256_o384_b4096.json` (2 KB) — (no description in file)
- `window_scaling_l5_even_r256_o384_b4096.json` (2 KB) — (no description in file)
- `window_scaling_l6_even_r256_o384_b4096.json` (2 KB) — (no description in file)
- `window_scaling_l8_even_r256_o384_b4096.json` (4 KB) — (no description in file)
- `window_scaling_l8_margin_bracket_b4096.json` (1 KB) — (no description in file)
- `window_scaling_l8_metric_witness_b4096.json` (1.1 MB) — (no description in file)
- `window_scaling_probe.py` (7 KB) — Growing-window diagnostics. Finite corrections are NOT complete tail uppers. Fresh analytic far-cut bounds are independently certified at every window.
- `window_scaling_report.md` (3 KB) — Growing-window diagnostics for v1.25
