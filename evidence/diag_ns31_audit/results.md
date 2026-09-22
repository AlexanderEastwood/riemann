DIAGNOSTIC, NOT A CERTIFICATE. NS-31 adversarial audit replays.

The delivered report is [the versioned HTML audit](../../audits/circle-symbol-lane-2026-09-22-v2.html).
This directory contains numerical illustrations used to audit definitions and claims.
No interval certificate, complete-space positivity, G2 or RH claim is made.

Run from the repository root with the existing Python environment (mpmath, numpy,
scipy, python-flint). Set OPENBLAS_NUM_THREADS=1 and VECLIB_MAXIMUM_THREADS=1 for the
float eigensolves. The archived assembly generates its normal sequence caches on demand.
No original diagnostic script or report is modified.

- `replay_identity.py`: independent adaptive mpmath quadrature of lambda=4 even (0,1)
  and odd (1,2), retaining oscillatory tails. `identity.json` contains both cutoffs
  and both asymptotic orders. This is numerical, not a tail enclosure.
- `replay_lp.py 3 4 6 8`: replays all archived uniform and weighted dual cells, saves
  the vectors, dual multipliers and every primal constraint slack in `lp_l*.json`.
  Failed projected optimizer attempts are preserved; they are not witnesses.
- `replay_source.py`: normalization from complex to real-even modes; high-precision
  source residual, projection costs, explicit feasible pure and mixed repairs.
  Run after `replay_lp.py`. See `source_projection.json`.
- `replay_pencil.py 6 8`: fixes the original quadrature and N=96 while replaying the
  arithmetic at 120/180 digits. Saves all eigenvalues and threshold neighbors.
- `replay_misc.py`: 20/200-bin histogram distinction, sliding concentration function,
  reversed centered-comb profile, and scans beyond the original tail cutoff.
- `replay_extra.py`: independent 50-digit mpmath values at the violating tail points,
  Lorentzian transfer in the constant mode, and attempted c=0.5 dual tests. Positive
  gaps support infeasibility only at lambda=3,6; negative gaps at 4,8 prove nothing.
- `replay_max_constant.py`: independent column-generation primal/dual calculation.
  Feasible mixtures at lambda=4 and 8 have c>0.5, refuting the original blanket
  infeasibility claim. The saved vectors/weights permit direct constraint replay.
- `wminus_tail_output.txt`: rerun of the original `diag_true_symbol/wminus_tail.py`.
- Build, existing-manifest verification, and pyright output are archived separately.

The original reports and code were inspected in full. This audit did not repeat the
entire historical comb optimization or all finite-ground eigensolves. It performed
the specifically requested quadrature, constraint, projection and precision checks,
and targeted computations needed to exhibit discrepancies. No new lambda was added.

`inventory.json` records source snapshot hashes and artifact checksums. It is an
integrity inventory for a diagnostic, not a mathematical certificate.
