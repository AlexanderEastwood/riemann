# `evidence/v126/g2_spectral_pilot/`

Manuscript remained v1.11 at this checkpoint (September 20, 2026) — numerical spectral pilot of the actual finite Weil matrix with the repaired prolate source. A `g2_*` directory by name, but its scripts state "Numerical evidence only … not rigorous error enclosures" and "Not a certificate".

The files here are byte-identical to [`evidence/v124/g2_spectral_pilot/`](../../v124/g2_spectral_pilot/).

**Start here:** [`G2_Spectral_Pilot_Report.md`](G2_Spectral_Pilot_Report.md), [`research_checkpoint.md`](research_checkpoint.md)

## Files

- `G2_Spectral_Pilot_Report.md` (15 KB) — G2 finite Weil spectral pilot
- `audit_g2_spectral.py` (2 KB) — Reproduce refinement and direct-correlation checks after the pilot runs.
- `check_g2_endpoint_moments.py` (3 KB) — Independent exact polynomial Mellin integration of the Galerkin source. The moment formula is exact for the finite Legendre polynomial.
- `check_g2_spectral.py` (10 KB) — Actual finite Weil matrix / repaired prolate source pilot. Numerical evidence only: quadrature and Galerkin comparisons are not rigorous error enclosures.
- `check_g2_spectral_mp.py` (6 KB) — High-precision continuation of the actual Weil/source experiment. All estimates are numerical, not interval certified. Requires the companion check_g2_spectral.py.
- `check_g2_spectral_wide.py` (3 KB) — N=64 refinement; both parity sectors retained. Not a certificate.
- `g2_direct_form_checks.json` (1 KB) — (no description in file)
- `g2_endpoint_moment_checks.json` (8 KB) — (no description in file)
- `g2_spectral_checks.json` (28 KB) — (no description in file)
- `g2_spectral_mp_checks.json` (2.2 MB) — (no description in file)
- `g2_spectral_pilot_validation.json` (2 KB) — (no description in file)
- `g2_spectral_refinement_differences.json` (836 B) — (no description in file)
- `g2_spectral_wide_checks.json` (2 KB) — (no description in file)
- `research_checkpoint.md` (7 KB) — Current research checkpoint: September 20, 2026 — actual finite Weil spectral pilot; manuscript remains v1.11
