# Agent 02: fixed original-theta value wrapper

Reviewed baseline `0da30a5c92203e45c452df87b68a93d86b7e5fd7` (PR80),
AGENTS, the current brief, PR80's evaluator and its derivation record, and the
matched matrix-pipeline interface. The parent owns the current full-register
review. This is a scoped implementation audit, not a replay of all prior proofs.

**Wall check: Distinct test.** Closest PR78-80, NS100/101. A certified negative
quadratic form on one prescribed real-point matrix would reject general PD
of the original quotient without requiring a complex pole. No new all-height
arithmetic estimate is being supplied; original Laguerre positivity stays open.

## Protocol preserved

`original_screen.py` imports the archived `theta_eval.py` without modifying it.
The only requested arguments are `t=j/4`, `j=0,...,5`, each at 128 and 256 bits.
The first pass uses 24 lattice terms, GL48 per segment, and real cutoff4; the
replay uses 32 terms, GL96, and cutoff4.5. These preserve the original complete
arithmetic coefficients with separately recorded analytic truncation majorants.
The complete integral is approximated, not certified. There is no enlarged
stencil, altered spacing, additional precision or domain search.

The common factor is `B=exp(2*pi*exp(2*t)-9*t)/(4*pi^4)`. Both computed factors
contain exactly the same B, so `(B*C)/(B*M)=C/M`. The record retains B, normalized
M/C/M', reconstructed unnormalized M/C, the complex ratio, each original tail
metadata item, and the six real decimal strings consumed by the matrix pipeline.
It checks finite values, sample positivity of M and C, and the imaginary parts
relative to their real parts before taking the real ratio. These are sample
sanity checks, not interval signs. Reconstructed values are also diagnostics.

The archived analytic derivative and its complete-tail majorants are retained
for provenance only. No derivative or root finder is used in the six-point
matrix test. Numerical reflection uses the exact evenness of the full kernel;
finite-series reflection discrepancies remain within the stated lattice-tail
majorants. There is no numerical differentiation across that switch.

## Admission, time budget, and output safeguards

Execution requires all of the following:

- Explicit `--authorized-original`, passed only after the parent gives GO.
- The filled draft PR URL, retained in the output.
- Successful Gaussian and pole-free non-PD control records on exactly the same
  six-point stencil and both prescribed precisions, including replay agreement.
- The fixed `--deadline-utc`; its preceding one-hour budget must include setup
  and controls. The deadline cannot be more than one hour ahead.
- A new output filename; previous original output is never overwritten.

A process alarm interrupts even an individual integral at the deadline. The
record is saved incrementally after each completed point. Exceptions or budget
expiry retain partial output with an explicitly inconclusive status; they do not
produce a matrix decision. Parent must pass only a complete record onward.
The evaluator and wrapper source hashes and matched-control file hash are saved.

## Uncertified errors and conditional certificate needs

Ordinary mpmath values of the lattice and real-tail majorants are not
outward-rounded enclosures. Fixed Gauss-Legendre integration has no rigorous
quadrature-error estimate here, and arithmetic roundoff and ratio error are
unbounded. A cutoff/precision replay measures discrepancy only. The result
cannot certify either a negative eigenvalue or a nonnegative matrix.

Only an admitted negative fixed rational direction could justify the conditional
Arb follow-up. Such a follow-up must enclose all six complete M and C values,
show each denominator's lower endpoint positive, divide intervals, and evaluate
one fixed rational quadratic form at two precisions, including lattice,
real-integration, quadrature and arithmetic errors. A negative midpoint or an
uncertified eigensolve cannot substitute for those requirements. No interval
certificate implementation is built preemptively by this agent.

## Checks completed before original evaluation

- `pyright evidence/diag_theta_six_point/original_screen.py`: 0 errors, 0 warnings.
- CLI help/import exercised without invoking the evaluator.
- The actual matched-control archive passes the wrapper's scope/precision/name
  admission checks.
- All functions touched have type hints. Existing project runtime used; no
  package installed. No original values, numerical scan or certificate run by
  this agent. No git operation, research row, thaw, or manuscript version.
