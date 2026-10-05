# Review 1 — original primitive, normalization and endpoint audit

Verdict: **PASS for equations (1)–(5), their complete-kernel premises, and
the normalization and r=0 consequences checked below. OPEN for the
all-height corrected Laguerre estimate.** No mathematical correction was
found in this assigned scope. The optional r=0 calculation below would
make the draft easier to check.

Wall check: **Same open gap.** Closest: NS100/101 and PR74/75. What changes:
the growing primitive is replaced by a decaying one; no original-arithmetic
signed estimate is added. This review validates an identity and its domains,
not a positivity-transfer claim.

## Scope actually reviewed

Reviewed baseline reported by the parent: commit
`d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208` (PR75). I read AGENTS.md through
its research-review and proposal-gate requirements; this audit's
REVIEW_BRIEF.md and complete derivation.md; PR75's original h/phi/X
definitions; and PR74's complete-moment control argument in
`reviews/05-matched-controls.md`. The parent performed the register-wide
104-node/14-demand review. I did not independently replay that global
review, prior certificates, or the manuscript. This is an independent
paper check of the assigned primitive questions. No scan, new certificate,
numerical threshold, or fresh sign candidate was attempted.

Line references refer to the draft read for this review: Section 1 at
lines 15–83, pair bounds at lines 93–104, transfer at lines 136–160, and
complex-domain statement at lines 164–169.

## 1. The factor xi/2 is correct

Use the conventional completed function

```text
xi(s) = s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)/2.
```

Write x=exp(2u), y_n=pi*n^2*x. Differentiating the complete h gives

```text
phi(u) = sum_(n>=1) exp(u/2)*(2*y_n^2-3*y_n)*exp(-y_n).
```

The n=0 summand exp(u/2) is annihilated by h''-h/4. For
`s=1/2+i*r`, substituting x=exp(2u) into the full-line transform and
integrating each of the two summands gives, initially for Re(s)>1,

```text
X(r) = pi^(-s/2)*zeta(s)*
       [Gamma(2+s/2) - (3/2)*Gamma(1+s/2)]
     = pi^(-s/2)*zeta(s)*Gamma(s/2)*s*(s-1)/4
     = xi(s)/2.
```

Here `du=dx/(2*x)` accounts for the important factor 1/2. The sum of
absolute integrals of the two summands is finite for Re(s)>1 because it
is a constant times `sum n^(-Re(s))`; thus this calculation does not
assume a termwise interchange on the critical line. The complete phi
has double-exponential tails at both ends, so its transform is entire.
Analytic continuation establishes the stated identity for all r.

Theta reciprocity gives h(-u)=h(u). For u>=0 every displayed summand of
phi is positive since y_n>=pi>3/2. This proves phi>0 there and hence
everywhere by evenness. Its smoothness and all derivative tails follow
from the locally uniformly differentiable theta series and reciprocity.
No curvature theorem or unproved sign condition is used.

## 2. No cusp or lost homogeneous mode in f

The global definition `f(u)=2*cosh(u/2)-h(u)` is smooth and even. The
half-line expansion (1) follows by separating the n=0 term of Theta.
It is not an independently reflected approximation. In particular all
odd derivatives at zero vanish because the original global functions
are smooth and even; the apparent absolute value in the tail formula
does not introduce a delta term.

Every fixed derivative of the theta correction is a sum of a polynomial
in y_n times exp(u/2-y_n). On u>=0 this is smaller than an exponential
times a double-exponential decay. Consequently

```text
f(u) / exp(-abs(u)/2) -> 1,
abs(f^(j)(u)) <= C_j*exp(-abs(u)/2), every fixed j>=0.
```

The constants C_j include a compact neighborhood of zero; no unsupported
uniformity in j is required. Polynomially weighted derivatives are
therefore integrable. Direct differentiation gives
`(1/4-d^2/du^2)*f=4*phi` with the sign in (2) correct.

For a>0, `G_a(u)=exp(-a*abs(u))/(2*a)` has derivative jump -1 at zero.
Thus `(a^2-d^2/du^2)G_a=delta`. At a=1/2 the prefactor 1/(2a) equals
one, so the particular solution is exactly `4*G_a*phi`, as in (3).
Both this convolution and f decay at the two ends. Their difference is
`c_plus*exp(u/2)+c_minus*exp(-u/2)`, and two-ended decay forces both
coefficients to vanish. Hence no homogeneous contribution was lost.

The convolution is strictly positive because G_a and phi are positive.
Equation (1) gives the strict upper bound exp(-u/2) on u>=0; evenness
extends it to all u. This establishes (4), including u=0. As a separate
normalization check, the leading Green-convolution tail is

```text
4*exp(-u/2)*integral_R exp(v/2)*phi(v) dv
 = 4*X(-i/2)*exp(-u/2) = exp(-u/2),
```

because xi(1)=1/2. The opposite end gives the same coefficient using
xi(0)=1/2. This agrees with the direct series rather than assuming the
tail coefficient.

## 3. Ordinary transform and r=0 are regular

Integrating (2) by parts twice yields
`(r^2+1/4)*Y(r)=4*X(r)`; f and f' vanish at both endpoints. For real r
the denominator is strictly positive. This checks (5), without dividing
by X or Y and without any restriction excluding their zeros.

For an explicit r=0 check, put

```text
m0 = integral_R phi(u) du > 0,
m2 = integral_R u^2*phi(u) du > 0.
```

Evenness and the moment integrals give

```text
X(0)=m0, X'(0)=0, X''(0)=-m2,
Y(0)=16*m0, Y'(0)=0, Y''(0)=-128*m0-16*m2,
L1[X](0)=m0*m2>0,
L1[Y](0)-8*Y(0)^2 = 256*m0*m2>0.
```

The coefficient on the right of (10) equals 8 at r=0, so this is a direct
check of the low-height correction term. Omitting that correction would
change the equivalence. The strict r=0 result is already a generic
complete-moment consequence, not a new uniform-height estimate.

The pair-envelope integrals in (6) also check directly: split at
`abs(s)=T=abs(t)` and use
`abs(s+t)+abs(s-t)=2*max(abs(s),T)`. The inside contributions are
`2*T*exp(-T)` and `2*T^3*exp(-T)/3`; the outside contributions are
`2*exp(-T)` and `2*(T^2+2*T+2)*exp(-T)`. Their sums are exactly (6).
The derivative bounds just proved permit the same argument for each
fixed derivative needed in the pair integrations by parts.

## 4. Complex-domain check and remaining gap

The unit positive exponential tails put the ordinary transform in
`abs(Im r)<1/2`. The meromorphic continuation `4*X(r)/(r^2+1/4)` has
uncancelled simple poles at both r=+/-i/2 because X equals 1/4 there.
Its residues are -i at +i/2 and +i at -i/2, matching the unit exponential
tail transform. These statements do not assert that every other point
on the strip boundary is a singularity of the continuation; the ordinary
integral still fails to converge there in the usual improper sense.

The corrected expression in (10) is exactly the all-real first-Laguerre
target, including r=0 and transform zeros. Positive f, its unit tail,
the envelope, and ordinary-transform legitimacy do not supply its sign.
The existing NS101 complete-moment control retains those structural
properties while violating the transferred sign. An original-theta or
distinguished-IVP estimating step absent from that control remains needed.
No such step was obtained in this assigned normalization audit.
