# `evidence/v138/`

Manuscript v1.38 — CERTIFICATE bundle: complete finite lower floors `W_lambda >= -8 I` at lambda=5, 6, 8 in both parity sectors (`prop:v138-three-floors`), replayed from the saved exact dyadic witnesses (`dyadic_witnesses.npz`, `replay_b256.json`), plus the shifted scalar-tail cutoff-cost certificate (`prop:v138-shifted-floor`).

**Start here:** [`REPRODUCE.md`](REPRODUCE.md), [`research_report.md`](research_report.md), [`adversarial_review.md`](adversarial_review.md)

**Manifest:** [`v1.38_manifest.json`](../../manifest/v1.38_manifest.json)

## Files

- `REPRODUCE.md` (2 KB) — Reproduce the v1.38 finite-floor certificates
- `adversarial_review.md` (12 KB) — Adversarial review: complete finite lower floors at lambda=5,6,8
- `assembly_general.py` (3 KB) — Arb enclosures of the actual Weil Fourier coefficients at integer lambda.
- `cutoff_cost.py` (1 KB) — Fresh outward certificate for shifted scalar-tail cutoff thresholds.
- `cutoff_thresholds.json` (10 KB) — (no description in file)
- `dyadic_witnesses.npz` (1.5 MB) — (no description in file)
- `initial_certificates.json` (7 KB) — (no description in file)
- `new_section.tex` (7 KB) — A fixed finite-floor experiment and its cutoff cost
- `pack_and_replay.py` (4 KB) — Replay exactly the saved dyadic witnesses at a fresh, higher precision.
- `replay_b256.json` (6 KB) — (no description in file)
- `research_report.md` (10 KB) — Complete finite-floor test — v1.38
- `shifted_floor.py` (6 KB) — Complete shifted Weil-form certificates; no positive weighted-tail metric. Uses the archived, audited Arb coefficient assembly without modification.
