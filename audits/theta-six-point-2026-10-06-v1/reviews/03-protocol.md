# Agent 03 — fixed six-point protocol and implication review

**Decision: GO for the single preregistered diagnostic, after the draft
proposal and matched controls.** No original evaluation was performed by
this reviewer. A negative floating form is a candidate only; complete Arb
validation is required before rejecting the original quotient's positive
definiteness. A finite positive matrix leaves that property undecided.

Reviewed main `0da30a5c92203e45c452df87b68a93d86b7e5fd7` (PR80), current
AGENTS, the new brief, PR78's nonlocal-centering review, PR79's contour
scope, PR80's outcome and relevant PR77 score/moment/control reviews.
The parent reviewed the full 104-node register and 14 demands; that
conclusions/dependency review is inherited, not a fresh historical proof
or certificate replay. Both missing-original recovery groups stay OPEN.
This agent previously implemented the PR80 evaluator and is reused here
as protocol reviewer; it is not an independent evaluator implementation.
The separate direct-term evaluator and final reviewers cover that role.

**Wall check: Distinct test.** Closest PR78--80, NS100/101. What changes:
test the actual real finite-matrix condition for `k=C/M`, which can fail
without a complex pole. No theta coefficients, integration domain or
original signed lower target are changed. Success would reject the
quotient-PD sufficient certificate only; failure to find a negative form
on these six points ends this diagnostic without deciding that certificate.
The original all-height first-Laguerre inequality is the same open gap.

## Exact rejection edge and its limits

Use the complete original functions

```text
M(t)=int_R phi(s+t)*phi(s-t) ds,
C(t)=int_R s^2*phi(s+t)*phi(s-t) ds,
k(t)=C(t)/M(t),
t_j=j/4, j=0,...,5,
B_ij=k(t_i-t_j).
```

The original real kernel is positive and even; hence `M(t)>0`,
`C(t)>0`, and k is a well-defined real even continuous function.
Consequently B is real symmetric Toeplitz and uses exactly the six
values `k(0),k(1/4),...,k(5/4)`. Negative arguments are supplied by
the proved evenness, not new evaluations. For a nonzero rational v,

```text
Q(v)=sum_(i,j=0)^5 v_i*v_j*k((i-j)/4)<0
  => k is not positive definite on R.
```

This is the defining finite-matrix condition for positive definiteness;
there is no missing transform, asymptotic, zero-location or cofinal
bridge in this rejection. The six original arithmetic ratios must,
however, actually be enclosed before a negative sign is proved.

PR78's implication `k PD => C=M*k PD => L1[X]>=0` remains one-way.
Here M is already an autocorrelation. Rejecting k-PD does not reject
C-PD, because the entrywise product of M's matrices with indefinite
k matrices can still be positive semidefinite. It therefore does not
imply a negative original Laguerre value, an off-line zeta zero, or a
failure of RH or G2. Conversely, a positive B does not prove k-PD:
that assertion quantifies over every finite set of real nodes and all
coefficient vectors, not one six-point set.

## Fixed candidate selection and replay

The 128-bit real symmetric eigensolver's first column in ascending
eigenvalue order selects a vector only. Normalize its largest absolute
component to one, make the first maximal component positive, and round
each coordinate to the nearest multiple of `2^-32`, ties to even.
Archive the resulting six integer numerators and denominator `2^32`.
The same exact rational vector is used at both precisions. Degeneracy
does not invalidate any resulting rational form; the deterministic
library output is the selection rule, not a uniqueness theorem. The
normalization guarantees a nonzero coordinate before and after rounding.

With `p=128,256`, define

```text
Q_p=v^T*B_p*v,
S_p=k_p(0)*||v||_2^2,
q_p=Q_p/S_p,
epsilon=2^-40.
```

The admitted diagnostic candidate must satisfy all of the following:

- The original wrapper has passed realness, finite-value and positive-M
  checks; it must not silently discard a material imaginary residue.
- The same nonzero rational v has `Q_p < -epsilon*S_p` at both
  precisions, with positive `k_p(0)`.
- For all six entries,
  `abs(k_256(j/4)-k_128(j/4)) <= epsilon*max(abs(k_128(0)),abs(k_256(0)))`.
- `abs(q_256-q_128)<=epsilon`.

Coordinator code check: the preregistered implementation at commit
1b9efc9 uses <= for the two agreement tests; only the negative-margin
inequality is strict. This corrects the reviewer's initial transcription,
not the protocol or computation. A failed gate is inconclusive. Scaling v cannot
manufacture the margin: both Q and S scale quadratically. The eigenvalue
and its sign remain diagnostic; the rational form is the possible
certificate object. Re-evaluating an already fixed v is not another
search. No new spacing, longer stencil, adapted vector at 256 bits,
adjacent test or renewed pole search follows a null outcome.

Precision agreement is not a total error bound. In particular, the
entrywise discrepancy tolerance would permit a form discrepancy as
large as six times that scale by `||v||_1^2<=6||v||_2^2`; the separate
form-agreement gate is useful operationally, but even both gates do not
bound a shared quadrature bias. No eigensolve or midpoint solve proves
the eventual sign.

## Controls at the actual fixed stencil

The matrix worker's archived `controls.json` applies the identical
eigensolver, dyadic rule, matrix construction, thresholds and replay.
It reports both controls passing. I independently evaluated only these
two synthetic functions at 256 bits, with no original-theta calls.

For `g(t)=exp(-t^2)`, the Fourier transform is
`sqrt(pi)*exp(-xi^2/4)>0`; its matrices at distinct real nodes are
positive definite. The fixed-stencil diagnostic minimum eigenvalue is
approximately `0.00001295378716671633`. The simple integer vector
`(1,-5,10,-10,5,-1)` gives `Q=0.01661337882091812>0` diagnostically.

For `f(t)=exp(-t^2)*(1+t^2)`, the transform is

```text
sqrt(pi)*exp(-xi^2/4)*(3/2-xi^2/4),
```

which changes sign. Non-PD globally alone would not guarantee detection
by this particular stencil, so I also checked the fixed matrix. Its
diagnostic minimum eigenvalue is approximately `-0.1106279603778422`.
The same integer vector gives `Q=-0.05763479916984081` diagnostically.
Its exact form, with `q=exp(-1/16)`, is

```text
8*Q=2016-3570*q+2400*q^4-1125*q^9+320*q^16-41*q^25.
```

The matrix pipeline's chosen dyadic vector is different and gives its
own recorded negative form; the independent integer-vector calculation
is only a synthetic cross-check, not an alternative original search.
These floating signs are not interval certificates.

Both controls share real even smooth integrable functions, a positive
value at zero, the exact stencil and the same finite-matrix inference.
The entire negative toy has no poles, illustrating why PR80's inconclusive
pole locator does not decide this test. It is positive on the real axis
and on the imaginary axis within `abs(Im t)<pi/4`, but it lacks the
original theta coefficients, Jacobi data and quotient asymptotic. Neither
toy checks original theta quadrature or supplies arithmetic evidence.

NS100 excludes positivity of individual original shifted slices, whereas
this test uses a ratio of complete integrals and assumes no per-slice PD.
NS101 shares complete kernels and the conditional quotient/convolution
algebra, but changes the original lattice and Jacobi IVP. Its known
negative first-Laguerre values force failure of its own quotient-PD
sufficient condition; they do not guarantee a negative form on these
six particular points. Requiring this stencil to detect NS101 without
such a witness would impose an unsupported control target.

Davenport--Heilbronn shares generic real-Hermitian matrix logic only
after a corresponding well-defined quotient has been supplied. Its
coefficients, conductor, gamma factor and completion differ from this
original theta pair; the actual original quotient is not instantiated
by the unchanged DH or example derivative screens. These are explicit
mismatches, not passes. NS74's NB target/inner-factor sensitivity and
NS83's fixed-smoothing dyadic-rate restriction have different functions,
coefficient classes and quantifiers. No NB gain claim is made here.

## Closest previous exclusions do not decide B

- PR77's score divided-difference Gram failure concerns the unbounded
  score `phi'/phi` and different matrix entries. It is not a matrix
  identity for the conditional second moment k.
- Positive ordinary moment/Hankel matrices for phi or C express
  moment-square positivity; they do not prove translation-matrix PD
  for C or for its quotient by M. The PR77 Jensen audit retains the
  missing all-degree critical-value estimates. No moment shortcut is
  imported here.
- PR77's positive Gaussian-mixture exclusion concerns C's
  double-exponential tail. PR78 rejects a positive sech-power mixture
  for k. Neither excludes general k-PD by itself.
- PR79 gives a sufficient pole-based rejection of k-PD, but does not
  make poles necessary for its failure. PR80's bounded search was
  inconclusive, not a pole-free theorem. This real quadratic form has
  a direct rejection edge that does not depend on either pole outcome.

This is validation of one already specified sufficient construction,
not a new sign-producing arithmetic estimate or a thaw of ZERO-GEOMETRY.

## Conditional certificate and stop rule

Only an admitted original negative diagnostic vector opens the bounded
certificate task. At each of the same six rational arguments, Arb must
enclose the complete M and C, all omitted lattice and real-integration
tails, finite quadrature error and roundoff. Each M denominator enclosure
must exclude zero before interval division. Preserve the exact rational
vector; then enclose

```text
Q=d_0*k(0)+2*sum_(l=1)^5 d_l*k(l/4),
d_l=sum_(i=0)^(5-l) v_i*v_(i+l),
```

with exact rational coefficients. A strictly negative upper endpoint at
each of two working precisions proves the finite rejection. An indefinite
or zero-containing final interval is inconclusive. No eigenvalue enclosure
or matrix inversion is needed; there must be no midpoint linear solve.

Budget remains one hour for this diagnostic including controls, and at
most two hours for one fixed candidate's complete validation if admitted.
No candidate means no certificate attempt and stop this stencil. No row,
thaw, manuscript version, external outreach or original evaluation by
this reviewer. **Final wall check: Distinct test; original signed target
still the same open gap.**
