Diagnostic evidence (2026-09-21, Claude). Not a certificate; see results.md.
`split.py` reproduces the table. Run from the repo root with the project venv:

    .venv/bin/python evidence/diag_circle_split/split.py

It imports `assembly_general.py` from `evidence/v124/g2_schur_cancellation/`
and that module caches `sequences_v3_*.json` beside itself; delete any new
cache files before committing, or point the import at a scratch copy.
