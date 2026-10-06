# Diagnostic only — not an interval certificate

The original six-point matrix has positive numerical eigenvalues at128/256
bits. The one frozen rational test vector has a positive form at both
precisions. There is no negative diagnostic candidate and no Arb stage.
This is inconclusive for general positive definiteness of k=C/M. The
original first-Laguerre target remains open. Stop this screening round;
no stencil/spacing enlargement or new manuscript version.

The exact stencil is t_j=j/4,j=0,...,5, B_ij=k(abs(i-j)/4). All six complete
original quotient values retain the full M,C lattice/real-tail accounting.
Finite quadrature, roundoff and ratio errors remain unbounded diagnostics.
Source, control and wrapper hashes are in original.json. Protocol was
published in draftPR81, commit1b9efc9, before original evaluation.

## Reproduction

Python3.14.6, mpmath1.3.0. From repository root, using the existing .venv:

```text
.venv/bin/python evidence/diag_theta_six_point/matrix_screen.py --output evidence/diag_theta_six_point/controls.json
.venv/bin/python evidence/diag_theta_six_point/original_screen.py --controls evidence/diag_theta_six_point/controls.json --output evidence/diag_theta_six_point/original.json --deadline-utc 2026-10-06T15:59:00Z --preregistered-pr https://github.com/AlexanderEastwood/riemann/pull/81 --authorized-original
.venv/bin/python evidence/diag_theta_six_point/matrix_screen.py --input evidence/diag_theta_six_point/original.json --output evidence/diag_theta_six_point/original-screen.json
```

These commands document the archived execution. Preserve its outputs; use
new output names and a separately admitted deadline for any later replay.
The one original run took about3.09seconds,12quotient evaluations total,
six per precision. No alternative stencil or extra original argument.

## Frozen rational direction and observations

The witness numerators (common denominator2^32) were
[-1209425521,3095606301,-4294967296,4294967296,-3095606301,1209425521].
Orientation is chosen before dyadic rounding, so a rounded tie at +/-1
need not have its first component positive. Sign orientation does not
change the quadratic form.

At256bits, the computed minimum eigenvalue is approximately
0.00052817273088790117508, and the frozen form approximately
0.00168886096494128373566. These are diagnostic values, not certified
lower bounds. The128/256bit entry/form agreement gates passed.

Controls used the identical six-point pipeline. Gaussian minimum eigenvalue
approximately1.29538e-5; pole-free non-PD control exp(-t^2)(1+t^2) minimum
eigenvalue approximately-0.110628 and fixed rational form approximately
-0.415568. These controls validate the finite matrix/witness pipeline,
not original theta quadrature or global PD.

## Independent replay of the same six arguments

```text
.venv/bin/python evidence/diag_theta_six_point/independent_replay.py --approved
```

The separate direct-summand implementation imports neither the primary
kernel nor matrix code. It integrates raw M,C using256bits,36theta terms,
R=5 and adaptive tanh-sinh. Exactly the same six real arguments and the
same rational vector were used, with no new candidate selection. Runtime
about13.61seconds. Largest observed relative quotient discrepancy from the
primary256bit values is below3.85e-69; the same form remains positive,
with observed relative discrepancy below1.18e-69. These are empirical
agreement figures, not complete error enclosures. The input/code hashes,
complete analytic truncation majorants and all comparisons are archived.
No certificate stage is warranted by this outcome.

For an independent replay, copy this evidence directory to a new local-run
directory and execute its copied independent_replay.py there. That script
reads its neighboring archives and writes independent.json next to itself.
Do not execute it in the historical archive after publication; preserve
the executed source and output hashes.
