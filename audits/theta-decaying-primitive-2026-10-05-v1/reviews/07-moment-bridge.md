# Review 7 — local moments do not supply the all-height correction

**Disposition: PASS for the local identities and NS101 match; OPEN for
the all-height estimate.** No original arithmetic estimating method is
admitted by this review.

Reviewed scientific baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208`
(PR75); local audit scope commit
`edc65638cc5e761a0290b38d54ff0b9bac140697`.
I read the current AGENTS proposal/relevance requirements, this audit's
REVIEW_BRIEF and derivation, the ZERO-GEOMETRY scope, and PR74's complete
moment control proof in `reviews/05-matched-controls.md`. The coordinator
owns the refreshed repository-wide conclusions/dependency review. This
review is limited to moment-to-height transfer; it does not claim a replay
of historical proofs, certificates, or all other reviewers' questions.

**Wall check: Same open gap.** Closest results: NS101 and PR74/75.
What changes: the regularized transform has a polynomial correction that
must be retained even at height zero. Local moment information checks that
correction, but supplies no new bound at arbitrary height. The structural
inference from positive moments alone meets the existing NS101 obstruction.

## 1. The correction at the origin is checked exactly

Use complete moments, without a cutoff or evaluated numerical constants:

```text
m_j = integral_R u^j*phi(u) du, j=0,2,4,
nu_j = integral_R u^j*f(u) du, j=0,2,
p(r) = r^2+1/4,
Y(r) = 4*X(r)/p(r).
```

The relevant even moments are strictly positive and finite. Evenness gives
`X'(0)=Y'(0)=0`, while differentiating the exact relation (5) gives

```text
nu_0 = Y(0) = 16*m_0,
nu_2 = -Y''(0) = 16*m_2+128*m_0
                     = 16*m_2+8*nu_0.
```

Equation (10) at zero is therefore `nu_0*nu_2 >= 8*nu_0^2`.
Its exact left-minus-right value is

```text
nu_0*(nu_2-8*nu_0) = 256*m_0*m_2 > 0.
```

This agrees with (9), since `L1[X](0)=m_0*m_2` and `p(0)^2=1/16`.
Positivity of `f` alone would give `nu_0*nu_2>0`, not the stronger
corrected threshold `nu_2>=8*nu_0`. The latter here follows from the exact
resolvent relation and positivity of the original `phi`.

## 2. What finite local moment information actually supplies

The elementary inequality `cos(v)>=1-v^2/2` yields, on the original
complete kernel,

```text
X(r) >= m_0-r^2*m_2/2,
-X''(r) >= m_2-r^2*m_4/2.
```

Thus the unevaluated interval

```text
r^2 <= min(m_0/m_2, m_2/m_4)
```

has `X(r)>=m_0/2`, `-X''(r)>=m_2/2`, and consequently

```text
L1[X](r) = X'(r)^2+X(r)*(-X''(r)) >= m_0*m_2/4 > 0.
```

This is a generic local consequence of complete positive even moments,
included solely to quantify the scope of the proposed bridge. It is not
a new arithmetic estimate, an evaluated height range, or a newly claimed
research result. Through (9), it gives a positive corrected (10) margin
only on that same interval. It gives no lower estimate outside it.

Even having every ordinary even moment positive does not repair this.
For any positive even kernel with entire transform `X`,

```text
X(i*y) = sum_(k>=0) m_(2k)*y^(2k)/(2k)!.
```

All coefficients of `abs(X(i*y))^2=X(i*y)^2` are positive. Hence every
generalized Laguerre coefficient at the single center `r=0` is positive,
not just the first one. Positive Hankel moment matrices and the usual
moment log-convexity inequalities are also generic consequences of a
positive measure. These origin/measure facts do not assert the signs of
the generalized Laguerre expressions at other real centers. For `Y`, the
analogous origin series is confined to its analytic strip; the actual
poles at `+/-i/2` must not be omitted.

This is not a claim that exact complete moment data can never determine
the transform. They can determine it under appropriate determinacy or
analytic hypotheses. The missing step is an all-height sign estimate from
that data, rather than generic positivity of the data or coefficients at
one center.

## 3. NS101 matches these moment hypotheses exactly

For the recorded positive reciprocal mixture, with `B_beta` as in (11),

```text
m_0,beta = 5*m_0/B_beta,
m_2,beta = (5*m_2+2*beta^2*m_0)/B_beta,
m_4,beta = (5*m_4+12*beta^2*m_2+2*beta^4*m_0)/B_beta.
```

These follow by changing variables in each of the two translated complete
integrals. All complete even moments are positive; the local bounds in
section 2 and the origin generalized Laguerre signs therefore also hold
for this family. Its positive primitive shares the exact resolvent
relation, so

```text
nu_2,beta-8*nu_0,beta = 16*m_2,beta > 0.
```

Despite these matched properties, PR74's previously recorded estimate is

```text
L1[X_beta](pi/beta)
 <= -(beta^2-3*k)*m_0^2/(2*B_beta^2) < 0,
k=m_2/m_0,
beta >= max(2, pi*sqrt(k)).
```

Using (9), the difference between the two sides of (10) for `Y_beta` is
exactly `16*L1[X_beta]/p^2`, and is negative there. This is a direct
first-Laguerre control, not an inference from off-axis zeros.

There is no contradiction with local positivity: the moment ratios and
the guaranteed local interval depend on `beta`. For example
`m_2,beta/m_0,beta = k+2*beta^2/5`; the local radius shrinks at order
`1/beta`, while the negative witness also moves at that order. Continuity
for each fixed function is not a common positive neighborhood for the
whole varying family.

The control changes the original single-lattice coefficients and fails
the normalized original Jacobi IVP. It consequently rejects the inference
from the shared moment/primitive properties, but does not reject an
estimate that uses those distinguished arithmetic or IVP hypotheses at
an essential step. No control pass for such an estimate is claimed.

## 4. The precise missing uniform input

An admissible continuation would need an independently estimated lower
bound for the complete expression

```text
J(r) = p(r)^2*(Y'(r)^2-Y(r)*Y''(r))
       +2*(r^2-1/4)*Y(r)^2 = 16*L1[X](r),
for every real r.
```

For a local-to-global proof, that means either a sign-preserving
propagation mechanism using the original arithmetic/IVP, or signed lower
margins with controlled errors on a family of neighborhoods covering the
entire real axis. Ordinary moment positivity supplies neither. Bounds on
absolute derivatives can control remainders locally, but do not create a
positive signed margin at a new center. Since the complete transform and
its derivatives tend to zero, a fixed absolute error allowance also
cannot simply replace the needed comparison at arbitrarily high centers.
No division by `Y` at its zeros is allowed in this transfer.

Requiring `J(r)>=0` again, or positive definiteness of the complete
associated kernel, would only restate the target. This review identifies
no independent original-coefficient estimate for it.

**Final disposition:** retain (9)-(12) and their scopes. If mentioning
origin positivity in the report, retain its polynomial correction and
label its consequence local. No scan, new proposal, research row,
manuscript version, thaw, or computation budget follows. The original
theta all-height first-Laguerre question remains open.
