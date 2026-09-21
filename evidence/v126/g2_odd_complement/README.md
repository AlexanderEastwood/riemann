# `evidence/v126/g2_odd_complement/`

Manuscript v1.26 — CERTIFICATE bundle: the complete odd-sector sign at lambda=4 — a direction-complement certificate (768/896 bits), a directional M=8192 certificate (1024/1280 bits) and the binding certificate `complete_lambda4_v126_certificate.json`. Together with [`../g2_simultaneous/`](../g2_simultaneous/) this gives `W_4 >= 0` in both parities (`prop:v126-odd-complement`, `prop:v126-full-window`). Marked RESTORED in [../../MISSING.md](../../MISSING.md).

**Start here:** [`README_odd_complement.md`](README_odd_complement.md), [`review_rank_one_trial.md`](review_rank_one_trial.md)

**Manifest:** [`v1.26_manifest.json`](../../../manifest/v1.26_manifest.json), [`v1.26_evidence_recovery.json`](../../../manifest/v1.26_evidence_recovery.json), [`README_v126_evidence_recovery.md`](../../../manifest/README_v126_evidence_recovery.md)

## Subdirectories

- [`input/`](input/) — v1.25 input manuscript
- [`renders/`](renders/) — contact-sheet renders

## Files

- `README_odd_complement.md` (3 KB) — v1.26: complete positivity at lambda = 4
- `build_complete_pdf.py` (1 KB) — Compile in a fresh directory; install only a closed, parseable full PDF.
- `certify_odd_full_window.py` (3 KB) — Bind the complete complement and directional certificates to one Schur form.
- `complete_lambda4_v126_certificate.json` (2 KB) — (no description in file)
- `direction_complement_certificate.py` (3 KB) — Complete old-metric complement bound for an exact frozen dyadic direction. All matrices are outward-certified complete residual ingredients, not cut tails.
- `direction_complement_lemma.tex` (2 KB) — Proposed proof insertion only; no numerical gate is asserted here.
- `direction_complement_progress.txt` (1 KB) — (no description in file)
- `direction_complement_replay_progress.txt` (1 KB) — (no description in file)
- `direction_complement_report_b768.json` (1 KB) — (no description in file)
- `direction_complement_report_b896.json` (1 KB) — (no description in file)
- `directional_M8192_progress.txt` (1 KB) — 8192 {'step': 4, 'recursive_residual2': '[0.009948444871571556819380617683084827237970 +/- 2.56e-43]'} 11.7
- `directional_M8192_verify_b1024_progress.txt` (2 KB) — verified exact head 83.9
- `directional_M8192_verify_b1280_progress.txt` (2 KB) — verified exact head 119.2
- `directional_M8192_verify_progress.txt` (586 B) — Traceback (most recent call last):
- `directional_odd_M8192_s24_report_b1024_J65536.json` (2 KB) — (no description in file)
- `directional_odd_M8192_s24_report_b1280_J65536.json` (2 KB) — (no description in file)
- `directional_odd_M8192_s24_witness.json.gz` (604 KB) — (no description in file)
- `directional_tail_repair.py` (7 KB) — Frozen one-direction finite trials; complete residual verification is separate. The old head and normalization remain exact. PCG is proposal-only.
- `finish_v126_sign.py` (9 KB) — (no description in file)
- `joint_remote_gate.py` (3 KB) — Whole-head certificate with one joint remote Gram, retaining its cross block.
- `localized_error_insert.tex` (2 KB) — (no description in file)
- `mixed_refinement.py` (6 KB) — Directional mixed inverse diagnostic, with exact frozen inputs and Arb actions. Finite-prefix mixed values are explicitly NOT complete-tail certificates.
- `odd_complement_insert.tex` (6 KB) — A complete complement bound and a reduced odd-sector target
- `odd_s16_ordinary_error_progress.txt` (4 KB) — (no description in file)
- `package_v126.py` (8 KB) — (no description in file)
- `posterior_trial.py` (6 KB) — Finite preconditioned trials, verified by the COMPLETE new Weil residual. Candidate iteration is not a positivity proof. All gates include remote rows.
- `quantify_head_error.py` (2 KB) — Certified ordinary-head lower errors, never positivity from an inconclusive bound.
- `rank_one_joint_progress.txt` (938 B) — (no description in file)
- `rank_one_odd_verify_b768_progress.txt` (4 KB) — verified column odd 1 / 16 seconds 13.9
- `rank_one_trial.py` (3 KB) — One finite residual repair of a proposed bad direction; full verification separate.
- `rank_one_trial_progress.txt` (1 KB) — rank-one step 1 [0.0001828208367839724611749556276781974985955 +/- 4.97e-44] 6.3
- `refine_inverse.py` (5 KB) — Reproducible Arb experiments for the complete lambda=4 tail inverse. Finite-prefix experiments are not certificates of the complete Schur sign.
- `render_v126.py` (1 KB) — (no description in file)
- `review_rank_one_trial.md` (18 KB) — Adversarial review: one repaired direction and the complete complement
- `simultaneous_odd_M4096_s16_normalized_ingredients_b768.json` (5.5 MB) — (no description in file)
- `simultaneous_odd_M4096_s16_normalized_ordinary_error_b768.json` (4 KB) — (no description in file)
- `simultaneous_odd_M4096_s16_normalized_report_b768.json` (3 KB) — (no description in file)
- `simultaneous_odd_M4096_s16_normalized_witness.json.gz` (5.1 MB) — (no description in file)
- `simultaneous_odd_M4096_s32_normalized_ingredients_b768.json` (5.5 MB) — (no description in file)
- `simultaneous_odd_M4096_s32_normalized_joint_lower_b768.json` (105 KB) — (no description in file)
- `simultaneous_odd_M4096_s32_normalized_joint_report_b768.json` (938 B) — (no description in file)
- `simultaneous_odd_M4096_s32_normalized_report_b768.json` (3 KB) — (no description in file)
- `simultaneous_odd_M4096_s32_normalized_witness.json.gz` (5.1 MB) — (no description in file)
- `simultaneous_trial.py` (9 KB) — Complete matrix Schur verification of independently frozen finite trials. No finite-solve convergence or positivity is used as a certificate.
- `window_scaling_probe.py` (7 KB) — Growing-window diagnostics. Finite corrections are NOT complete tail uppers. Fresh analytic far-cut bounds are independently certified at every window.
