# Fixed six-point theta quotient screen

**No negative witness. The bounded diagnostic is inconclusive for general
positive definiteness of k=C/M.** The original matrix has positive numerical
eigenvalues at128/256bits, and its one frozen rational test vector has
positive form. No complete original certificate was attempted or warranted
by the protocol. The original first-Laguerre estimate remains open.

**Wall check: Distinct test.** Closest PR78–80, NS100/101.
This tests a direct real-axis necessary condition for PD, without requiring
a complex pole. No new arithmetic lower estimate, NS row, thaw or manuscript
version follows. Both original-evidence recovery groups remain OPEN.

The full104-node register and14continuation demands were reviewed at main
0da30a5c92203e45c452df87b68a93d86b7e5fd7; no change since PR80. This was a
conclusion/dependency review, not replay of every historical proof.

## Fixed question and outcome

For t_j=j/4,j=0,...,5 use the complete original M,C and
B_ij=(C/M)(t_i-t_j). A rigorous negative rational quadratic form would
exclude general quotient PD by definition. It would not refute original
Laguerre positivity: quotient PD is a sufficient construction only.

The original matrix's diagnostic eigenvalues at256bits are approximately

```text
0.000528173, 0.001520214, 0.004401079,
0.012635149, 0.036318801, 0.092077142.
```

The frozen dyadic vector's quadratic form is approximately0.001688861,
positive at both precisions. Entrywise and normalized-form agreement gates
passed. These are numerical observations, not rigorous lower bounds.
A positive finite matrix does not establish PD for arbitrary real points
and arbitrary matrix sizes. No candidate reached the conditional Arb stage.

## Protocol and controls

[Draft PR81](https://github.com/AlexanderEastwood/riemann/pull/81) contained
the [filled proposal](PROPOSAL.md) before original computation, at commit
1b9efc9. Six arguments only,128/256bits, one rational vector selected from
128bits and reused. No variation of spacing, stencil size or coefficients.
The original run completed12evaluations in about3.09seconds.

The Gaussian positive control and the entire pole-free non-PD control
passed through the same matrix/witness pipeline. The latter gave a stable
negative form, demonstrating the test can catch a failure without a pole.
Neither control supplies original arithmetic evidence. All NS/DH hypothesis
matches and mismatches are explicit in the proposal and review03.

Complete lattice and real-integration tails are retained as analytic
formulas evaluated in ordinary arithmetic. The numerical finite quadrature,
roundoff and ratio errors are not enclosed. No midpoint eigensolve is a
certificate. Independent replay and final reviews are recorded separately.

## Disposition

**Stop this screening round and shelve further quotient falsification
screens until independent analytic input appears.** Do not infer PD from
these finite matrices or enlarge the stencil after this result. PR80's
pole search and this direct six-point test remain separately scoped nulls.
Neither closes the original nonlinear theta route. No new positive
estimating method or all-height lower bound has been obtained.

See [diagnostic record](../../evidence/diag_theta_six_point/results.md),
[original values](../../evidence/diag_theta_six_point/original.json),
[matrix output](../../evidence/diag_theta_six_point/original-screen.json),
and [matched controls](../../evidence/diag_theta_six_point/controls.json).

## Independent replay

A separate direct-term, unnormalized implementation with adaptive tanh-sinh
quadrature (256bits,36theta terms,R=5) reproduced all six original quotients
and the same fixed rational form. The largest observed relative quotient
difference is below3.85e-69. This supports stability at these six arguments;
it is not an error bound or a proof of finite/global PD. No additional
point or stencil was used. See [review04](reviews/04-independent.md) and
[replay output](../../evidence/diag_theta_six_point/independent.json).
