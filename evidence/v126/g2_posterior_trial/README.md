# `evidence/v126/g2_posterior_trial/`

Manuscript v1.24 — CERTIFICATE bundle: a complete Schur-direction certificate from a finite preconditioned trial (M=4096, 4 and 16 steps), verified by the complete Weil residual at 768 and 896 bits with frozen witnesses.

The files here are byte-identical to [`evidence/v124/g2_posterior_trial/`](../../v124/g2_posterior_trial/).

**Start here:** [`posterior_replay_README.md`](posterior_replay_README.md), [`posterior_integration_review.md`](posterior_integration_review.md)

## Subdirectories

- [`input/`](input/) — v1.23 input manuscript
- [`renders/`](renders/) — contact-sheet renders

## Files

- `adversarial_posteriori_refinement.md` (10 KB) — Complete residual verification after a finite higher-degree proposal
- `build_complete_pdf.py` (1 KB) — Compile in a fresh directory; install only a closed, parseable full PDF.
- `integrate_v124.py` (4 KB) — (no description in file)
- `mixed_probe_J65536_b768.json` (3 KB) — (no description in file)
- `mixed_probe_J65536_b896.json` (3 KB) — (no description in file)
- `mixed_refinement.py` (6 KB) — Directional mixed inverse diagnostic, with exact frozen inputs and Arb actions. Finite-prefix mixed values are explicitly NOT complete-tail certificates.
- `package_v124.py` (5 KB) — (no description in file)
- `posterior_check_M4096_s16_J65536_b768.json` (1 KB) — (no description in file)
- `posterior_check_M4096_s16_J65536_b896.json` (2 KB) — (no description in file)
- `posterior_check_M4096_s4_J65536_b768.json` (1 KB) — (no description in file)
- `posterior_check_M4096_s4_J65536_b896.json` (2 KB) — (no description in file)
- `posterior_insert.tex` (5 KB) — A complete Schur-direction certificate from a finite trial
- `posterior_integration_review.md` (2 KB) — Final adversarial review of the v1.24 insertion
- `posterior_replay_README.md` (1 KB) — Complete directional certificate replay
- `posterior_trial.py` (6 KB) — Finite preconditioned trials, verified by the COMPLETE new Weil residual. Candidate iteration is not a positivity proof. All gates include remote rows.
- `posterior_witness_M4096_s16.json.gz` (157 KB) — (no description in file)
- `posterior_witness_M4096_s4.json.gz` (157 KB) — (no description in file)
- `refine_inverse.py` (5 KB) — Reproducible Arb experiments for the complete lambda=4 tail inverse. Finite-prefix experiments are not certificates of the complete Schur sign.
- `render_v124.py` (993 B) — (no description in file)
