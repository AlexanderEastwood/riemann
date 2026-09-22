DIAGNOSTIC, NOT A CERTIFICATE.

NS-36 corrects the current reading of the circle/symbol diagnostics after NS-31.
Historical reports and replay outputs are preserved. New computations concern
the existing lambda=4, N=256, twenty-bin finite problem only. No all-Borel,
complete-space, cofinal, G2 or RH conclusion follows.


Current interpretation and detailed slacks:
[circle-lane-current-reading-2026-09-22-v1.html](circle-lane-current-reading-2026-09-22-v1.html).

## New lambda=4 result

The original c'=1 pure vector remains infeasible (minimum ratio 0.636).
A different raw pure vector passes the original twenty-bin model with ratio
2.8474145888 and midpoint energy 4.05222239745e-18. Removing the normalized
head direction of a computed raw polynomial source gives energy
4.05885349934e-18 and ratios 2.7852899960 / 2.7805759646 on the original /
refined grids. The source approximations use 90/110 even Legendre modes at
130/170 decimal digits. Their direction distance is 1.3238e-56; this is
stability evidence, not an error enclosure for the actual repaired source.

The head-preserving projection differs from full physical P_a projection.
Exact orthogonality of a head witness would require an enclosure of the actual
head source coefficients (modal error plus repair), not a Fourier-tail estimate.
No such enclosure is produced here. Initial source stdout reports internal
residuals; the updated JSON separately gives replayable 80-digit-export
residuals, about 1e-81. Both remain numerical residuals.

A separate rank-27 subspace produces a source-independent mixed-state
construction: deleting any projected source direction leaves every bin above
its requirement by the exact trace-minus-largest-eigenvalue implication,
evaluated here in float arithmetic with the basis Gram. Ratios are
1.1292203 / 1.1218239 and the midpoint energy budget is 0.3646397. This is not
the tiny-energy pure-state claim and implies no common feasible pure component.

## Replay

Run from the repository root with the existing virtual environment, with
OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1 for reproducibility:

- feasibility_repair.py --raw-search
- feasibility_repair.py --refinement 2
- source_projection.py --validate-lambda3
- source_projection.py --size 90 --digits 130
- source_projection.py --size 110 --digits 170 --refinement 2
- verify_saved_witnesses.py

The source loader agrees with the archived lambda=3 printed coefficient
midpoints within 4.987e-61. All original twenty constraint slacks, frozen
coefficients and source coefficients are in the JSON outputs. The refined grid
subdivides the original weighted intervals, preserves their small gaps, freezes
the bin edges and extends the deepest bin below the original sampled minimum.
All-Borel WLH, global depth and cofinal control are untested.

## Review and archive checks

Astra-2 independently reviewed the formulas, normalization, source convention
and mixed-state deletion inequalities. No major error was found. The two minor
points were addressed: exported residuals are distinguished from internal
precision, and mass screening uses the same Gram normalization as the energy
recheck. Historical results.md files and original scripts remain unchanged from
main318b3ce; directory introductions, task-board summaries and map notes now
point to the qualified current reading.

The actual manuscript build is 242 pages with zero undefined/duplicate
references; v1.49 manifest: 7 ok, none missing/mismatched. No new manuscript
version, complete-operator certificate, G2 or RH claim.
