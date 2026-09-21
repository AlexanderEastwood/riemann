# v1.42 — one complete-ground local zero at the existing lambda=4 window

Certified computation plus the proved spectral-energy projection implication.
The complete ground transform has a unique simple real zero in
`(gamma_1 - 1/10, gamma_1 + 1/10)`. This is a local enclosure, not a claim
that it is the first transform zero or that its discrepancy from gamma_1
has a known sign. G2 and RH remain open.

The substantive change is the **complete even-sector separator 1e-67**.
The old global separator 1e-73 makes the same endpoint test inconclusive.
No new window, eigensolve, trial support, residual cutoff or tail assembly
is introduced. All archived infinite-tail errors remain in the inherited
Schur comparison. The ordinary error bounds compare the unit trial with
its nonzero **orthogonal ground projection**, which need not be unit norm.

- `new_section.tex`: complete proof and scope.
- `certify_ground_zero.py`: interval verifier at 1024/1280 bits.
- `ground_zero_b1024.json`, `ground_zero_b1280.json`: saved gates and input hashes.
- `check_independent.py`, `independent_checks.json`: second implementation
  using principal determinants and direct centered cosine integrals; no
  independent-agent or external audit is claimed.
- `scope_review.md`: same-agent proof and provenance review.
- `research-report-2026-09-21-v1.html`: original report, before task-ID reconciliation.
- `research-report-2026-09-21-v2.html`: current user-facing report (NS-18).
- `integration_checks.json`: concurrent-main preservation and unchanged source checks.
- `build_report.json`: actual manuscript build and diagnostics.

Replay from the repository root, writing fresh files:

```sh
.venv/bin/python -B evidence/v142/certify_ground_zero.py --bits 1024 --output /tmp/ground-zero-1024-replay.json
.venv/bin/python -B evidence/v142/certify_ground_zero.py --bits 1280 --output /tmp/ground-zero-1280-replay.json
.venv/bin/python -B evidence/v142/check_independent.py --output /tmp/ground-zero-check-replay.json
python3 tools/verify_manifest.py v142
./manuscript/build.sh
```

The verifier refuses to overwrite an output. Use new paths for later runs.
The second implementation also checks the archived reports and dependency
hashes. Python 3.14.6 and python-flint 0.9.0 were used.

Inherited evidence: exact v1.25/v1.26 frozen even trial, saved complete even
residual enclosures at 768/896 bits, and v1.40 simple-even ground theorem.
Only the small inherited final gates are replayed; this is explicitly not
a fresh evaluation of every old residual row. Cutoff convergence is not an
assumption: the old analytic remote bound covers the entire tail.
NS-1's two missing historical evidence groups remain OPEN and are not used
by this new result.

The original NS-17 claim commit is preserved; the completed task is NS-18
after reconciliation with concurrent main. Its separate documentation task
NS-17 remains open. No mathematical claim changed during reconciliation.
