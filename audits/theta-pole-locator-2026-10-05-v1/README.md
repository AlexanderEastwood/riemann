# Bounded original theta quotient-pole diagnostic

**Inconclusive: no original candidate reached the preregistered root threshold.**
This is a diagnostic, not an interval certificate, a zero-free-region result,
or an original first-Laguerre lower bound. No research row, node, thaw or
manuscript version. Both original-evidence recovery groups remain OPEN.

Reviewed main `bc3ff0c962c485ac8104ce8cd832c119c260c871` (PR79).
The full registered conclusions and continuation demands were reviewed;
historical proofs/certificates were not all replayed. The frozen proposal
was in draft [PR80](https://github.com/AlexanderEastwood/riemann/pull/80)
before the original evaluation: commit `728cc6c`; checked evaluator and
controls commit `0604699`.

**Wall check: Distinct test.** Closest PR78/79, NS100/101.
The test seeks an original uncancelled M-zero, which would reject general
quotient PD, beyond PR78's rejected positive sech-power mixture. It supplies
no new arithmetic lower estimate. The original signed theta target remains
the same open gap.

## Outcome

The single rectangle was `1/8<=Re z<=2, 1/8<=Im z<=5/8`.
81 initial points, four selected cells and same-cell 128/256-bit refinements
used 171 evaluations in 48.46 seconds (a runtime observation, not a bound).
Both precision runs stopped each refinement at its allowed cell boundary.
There was no automatic domain extension or second scan.

| Selected cell (zero based) | 256-bit normalized endpoint residual | Stop |
|---|---:|---|
| (0,7) | 0.03914163844 | step leaves cell after 16 halvings |
| (1,7) | 0.54809426972 | step leaves cell after 16 halvings |
| (0,6) | 0.49442807092 | step leaves cell after 16 halvings |
| (0,5) | 0.64851255786 | step leaves cell after 16 halvings |

Residual means `abs(B*M)` divided by the largest corner value in the same
cell, at the same precision. The root-candidate threshold was `2^-40`,
about `9.095e-13`. None passed. The four-corner sampled winding rounded to
zero in all64 cells, which proves nothing about continuous boundary winding.
The minimum in this table is not a lower bound over a cell or region.

The complete original theta coefficients were retained through explicit
lattice remainder and real-integration tail formulas. Their floating
values are not outward-rounded certificates. Finite quadrature and
roundoff are not rigorously bounded; increasing working precision alone
does not bound integration error. Normalizing by a nonzero analytic factor
preserves zeros but does not prevent sampled phase aliasing.

## What this changes

The planned finite falsification attempt is complete without a candidate
for certification. General PD of `k=C/M` remains undecided. A rigorous
uncancelled pole would exclude that sufficient construction, but a signed
Fourier transform of k need not make its convolution with `X^2` negative.
Original `L1[X]>=0`, RH, G2 and cofinal arithmetic inputs remain open.
No original interval certificate was attempted; without a candidate there
was no reason to spend its conditional two-hour budget.

**Stop this bounded test.** Do not widen the box because refinements met its
boundaries, treat the finite null as evidence for PD, or revisit the rejected
sech mixture. A future test needs a separately specified arithmetic input
or analytic estimate and its decision edge; none is supplied by this null.

## Controls, evidence and review

The actual pipeline found the known denominator zero of `z^4+1` in
`[0.7,0.72]^2`. With numerator1 it flagged a candidate needing certification;
with numerator `(z^4+1)*exp(-z^2)` it did not flag an uncancelled pole.
The removable toy therefore tests the important cancellation distinction.
Neither synthetic control supplies original-theta evidence. DH, NS100/101,
NS74/83 hypothesis matches/mismatches are explicit in the
[filled proposal](PROPOSAL.md) and [independent protocol review](reviews/03-protocol.md).

Evidence: [diagnostic record](../../evidence/diag_theta_pole_locator/results.md),
[full original output](../../evidence/diag_theta_pole_locator/original.json),
[controls](../../evidence/diag_theta_pole_locator/controls.json).

Six assigned roles: evaluator, locator/controls, mathematical protocol,
independent endpoint integration, code/results, final admission.
Reviews and final verification are recorded in `review-record.json`.

## Independent replay

A separate direct-term theta implementation with 256-bit adaptive tanh-sinh
integration, 36 lattice terms and real cutoff5 checked the four existing
endpoints, including the analytic normalized derivative. It did not search
for roots or evaluate a new domain. Largest relative differences from the
Gauss-Legendre replay were below8.374e-29 for M,1.404e-26 for C and1.048e-26
for normalized M'. These are observed discrepancies, not error enclosures.
The four sampled values are stable across these methods; no certification
candidate results. [Replay archive](../../evidence/diag_theta_pole_locator/independent.json).
