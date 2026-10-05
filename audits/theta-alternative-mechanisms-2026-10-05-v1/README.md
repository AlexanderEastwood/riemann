# Six-agent alternative theta mechanism audit

[Rendered report](theta-alternative-mechanisms-2026-10-05-v1.html) · [Review record](review-record.json) · [Proposal record](PROPOSAL.md)

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–78.**
No original all-height signed estimate is obtained. The three methods expose
an unestimated heat source, reject an unrestricted sector-matrix condition,
and leave a contour density unestimated. A separate useful rejection criterion
emerges: any uncancelled interior pole of the complete original quotient C/M
would rule out its positive definiteness. No such pole has been located.

Alex explicitly requested this six-agent continuation after PR78. Three
proposers assessed auxiliary heat, modular duplication and direct quotient
contours; three independently checked algebra, complex analysis, controls and
admission. Reviewed remote: `221ceec9da825bdc787111447badad961860760a`.
The 104-node/14-input review concerns conclusions and dependencies, not a
replay of all historical proofs or certificates. Both recovery groups stay OPEN.

## Exact outcomes

For the auxiliary Gaussian family `H_a=Fourier(exp(a*u^2)*phi)`, let
`Q_a=L1[H_a]`, `S_a=L1[H_a']` and G_a be the ordinary heat kernel. Then

```text
partial_a Q_a = -Q_a'' + 2*S_a,
Q_0 = G_A*Q_A - 2*integral_0^A G_a*S_a da, A=1/8.
```

The endpoint normalization is checked against the literature's scaled kernel.
It has nonnegative Q_A; no lower uniform margin is assumed. The source is
subtractive in the required direction and has no independent arithmetic
estimate. It is already positive at r=0. A locally bounded relative-source
bound also imposes an unproved restriction near multiple zeros. This auxiliary
heat clock is not the original nonlinear Jacobi evolution; neither route is
generally excluded.

The completed theta2/theta3/theta4 sectors are exact translates of the original
completed kernel. Their full Hermitian Laguerre matrix has inertia `(2+,1-)`
whenever X is nonzero. This rejects unrestricted sector-matrix positivity.
Subtracting the known phase correction leaves precisely `L1[X]*A*A^*`.
All pair sectors and lower moments are retained; nonlinear and infinite
duplication methods remain unexcluded but have no supplied estimating cone.

For the contour analysis, define the complete original functions

```text
M(z)=integral_R phi(s+z)*phi(s-z) ds,
C(z)=integral_R s^2*phi(s+z)*phi(s-z) ds,
k=C/M, K(xi)=Fourier(k)(xi).
```

M and C are holomorphic on `abs(Im z)<pi/4`; M is positive on both coordinate
axes. The complete complex saddle estimate makes M zero-free at distant
horizontal ends of every closed substrip. Its remaining zeros there are finite.
A nonremovable pole of k creates a leading oscillating residue contribution
to K. The lowest poles have no zero frequency because none is imaginary-axis;
their nonzero mean-zero trigonometric sum forces both signs. This includes
multiple poles and all complete tails.

```text
M(z0)=0, C(z0)!=0, abs(Im z0)<pi/4
  => k has a nonremovable pole
  => K changes sign
  => k is not positive definite.
```

This rejects only a sufficient certificate. In the exact transfer

```text
L1[X](r)=(1/pi)*integral_R X(r-xi/2)^2*K(xi) dxi,
```

a sign-changing K can still yield a nonnegative result. The original J,
first Laguerre, RH, G2 and the cofinal arithmetic bounds remain open.
Pole absence also does not imply positive definiteness; an explicit analytic
control in review 05 demonstrates that distinction.

## Next proposal, with its limits

A bounded locator is useful in principle because it now has a complete
rejection decision. An already known or externally supplied root is **not**
required by AGENTS. The review's possible discovery domain is
`1/8<=Re z<=2`, `1/8<=Im z<=5/8`, with at most a 9-by-9 grid, four selected
cell refinements and twelve refinement steps per cell. Cap discovery, including
controls, at 90 minutes; do not expand the region after a null result. This
domain is a tractability choice, not evidence of a zero there.

Before running, a separate completed protocol must fix the evaluator,
complete-integral error handling, exact cell-selection/stopping rule and
matched control implementation. Use an uncancelled-pole control and a
removable-pole control, so detecting M=0 alone cannot reject k. Diagnostic
artifacts belong under `evidence/diag_*`; floating phase winding is not a
zero certificate. A promising box then needs complete Arb argument-principle
and C-nonvanishing enclosures, uniform tails, and two-precision replay.
Initial certification budget: at most two hours for one specified box.

No witness means inconclusive. A certified uncancelled pole closes the general
quotient-PD sufficient construction, beyond PR78's particular mixture; it does
not disprove J. Failure to exclude zero in C is inconclusive, not cancellation.
No locator or certificate was run in this paper round.

## Six focused notes

1. [Auxiliary heat and the source term](reviews/01-heat.md).
2. [Completed duplication sectors](reviews/02-duplication.md).
3. [Original complex quotient and residue criterion](reviews/03-contour.md).
4. [Independent heat and duplication algebra](reviews/04-algebra.md).
5. [Independent complete-tail and contour check](reviews/05-contour-check.md).
6. [Admission, controls and bounded locator scope](reviews/06-admission.md).

The synthesis resolves an admission wording difference: review 03's suggested
externally supplied box is an option, not a prerequisite for all diagnostic
discovery. An instantiated box is required for an immediate certificate;
a bounded locator requires its own prior protocol and control screen.

No research row, node, thaw, sign scan, interval certificate or manuscript
version. Current budget: six paper reviews and one audit PR. No automatic
unbounded search, neighboring mixture or global route pivot follows.
