# `evidence/`

Evidence for the manuscript: one directory per manuscript version (`vNNN/` holds only what that version added) plus `diag_*/` diagnostics that are not certificates. Conventions are in [REPO_LAYOUT.md](../REPO_LAYOUT.md); artifacts that are cited but absent are listed in [MISSING.md](MISSING.md).

`v124/` and `v126/` are extracted historical bundles (cumulative snapshots of the v1.24 and v1.26 releases). `v135/`–`v139/` are per-version increments. Nothing here is a certificate unless the files in its own directory say so.

## Subdirectories

- [`diag_circle_split/`](diag_circle_split/) — Diagnostic evidence (2026-09-21, Claude). Not a certificate; see results.md.
- [`diag_routes/`](diag_routes/) — alternative-route diagnostics
- [`v124/`](v124/) — historical snapshot of the v1.24 bundle
- [`v126/`](v126/) — historical snapshot of the original v1.26 bundle
- [`v135/`](v135/) — v1.35 growing radical blocks (analytic)
- [`v136/`](v136/) — v1.36 dense radicals and the uniform finite-floor reduction (analytic)
- [`v137/`](v137/) — v1.37 scalar primitive budget no-go (analytic)
- [`v138/`](v138/) — v1.38 finite floors at lambda=5,6,8
- [`v139/`](v139/) — v1.39 scoped meta-obstructions (analytic)

## Files

- `MISSING.md` (3 KB) — Evidence availability ledger
