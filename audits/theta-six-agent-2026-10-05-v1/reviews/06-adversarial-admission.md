# Agent 6 — adversarial admission decision

Reviewed mathematical baseline: `5434d96f0034f842b0229f1d69dbbf3fb7fea270`
(merged PR73). Working audit HEAD: `971c8bd02c834cf31ab98ea2a50060289fbece40`.
The coordinator refreshed the remote again during this review; the scientific
baseline was unchanged. I read the current agent/proposal gate, register and
continuation scopes, current checkpoints/freeze and evidence ledger, the
shared brief, relevant PR72/73 and NS100/101 records, and reviews 01–05.
The coordinator's full review is recorded in the brief. This is an independent
paper check of the stated dependencies and calculations, not a replay of all
historical proofs, computations or external curvature certificates. Both
original-evidence recovery groups remain OPEN.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR72/73.**
What changes: an explicit smooth-completion error bound, an analytically
rejected local certificate, a positive Bessel-reference margin and a direct
first-Laguerre control screen can be assessed. What remains unchanged: the
complete original arithmetic lower-sign estimate is absent. The exact target
is `L1[X](r)=X'(r)^2-X(r)*X''(r)>=0` for every real r, equivalently positive
definiteness of the complete associated kernel C. This first-Laguerre target
alone is not RH, G2 or the cofinal signed-arithmetic floor.

## Decision and severity

**Admit zero original-theta sign candidates. Stop before any scan.**
The notes contain useful supporting estimates and scoped rejections. They
do not, individually or together, provide a complete original-theta sign
method. This verdict follows from the dependency checks below, not from
agreement between agents.

| Finding | Severity and disposition |
|---|---|
| No proved original lower comparison or lower-reference margin with the required complete error comparison | **Admission blocker.** Already disclosed in the notes; not a newly found error in their claims. No computation or row follows. |
| Global regularity of review 02's quotient needs pointwise `p'(t)<0`, not just the bare phrase strict log-concavity | **Minor formulation correction, resolved.** The coordinator changed the premise to an explicit conditional assumption. The diagonal rejection does not depend on it. |
| Review 03 controls `X-X_M`; review 04's margin belongs to a different Bessel reference | **Mandatory scope restriction.** Substituting the Bessel margin into the smooth-completion transfer would introduce an unproved comparison. No note actually makes that substitution. |
| Review 05 proves a sufficient parameter range in the NS101 family, not the fixed historical parameter 2 | **Mandatory quantifier restriction.** The final note states this correctly. No fixed-2 claim is admitted. |

No unresolved major algebra, factor, sign or boundary defect was found in
the particular supporting calculations checked below. This does not validate
every theorem or source mentioned in the repository.

## 1. Review 03: the strip estimate survives the audit

Keep its notation: `a=pi/4`, `v=pi/8`, `B=pi/sqrt(2)`,
`d=pi/(4*sqrt(2))`, `beta=pi/(2*sqrt(2))`, and

```text
w(z)=1/(1+exp(-2*a*sinh(2z))),
Delta_M(z)=w(z)*T_M(z)+w(-z)*T_M(-z).
```

The second term cannot be omitted. The identity for Delta uses the complete
theta reciprocity, analytically continued inside `|Im z|<pi/4`; it does
not declare the individual Gaussian summands even.

I recalculated the denominator argument. With `q=exp(-2*a*sinh(2z))`,
`u=Re z>=0`, and `|Im z|<=v`, the stated division at u-star gives either
`|q|<=1/2` or

```text
|continuous exponent argument of q|
 <= sqrt(pi^2/8+log(2)^2) < pi/2.
```

Thus `|1+q|>=1/2` in the first part and `>=1` in the second. The constants
in the two weight bounds are valid. The closed strip has no weight poles;
holomorphy and real smoothness are separate facts, and both are addressed.

For `y=exp(2u)>=1`, the two tail estimates reduce to

```text
n^2*y >= (n^2+y)/2,
(d_eta*y+b*n^2/y)/2 >= sqrt(d_eta*b)*n >= beta*n.
```

Here `b=pi*cos(2*Im z)>=B` and `d_eta=a*cos(2*Im z)>=d`.
Both inequalities check. The remaining half of the second exponent retains
`d*y/2`; only a nonnegative term is discarded. Summation over all `n>M`
therefore gives exactly the declared geometric factor
`exp(-beta*(M+1))/(1-exp(-beta))`, with the factor 4 on one half-strip
and factor 8 in the full-line moment constants C_j. These constants are
finite and independent of r and M. No numerical evaluation is needed for
the inequalities to have a precise meaning.

Contour shifting is legitimate for the complete Delta: its strip majorant
decays at both horizontal ends and on the closing vertical pieces. The
polynomial factor after differentiating the transform is bounded by
`(|Re z|+v)^j`, giving

```text
|Dhat_M^(j)(r)| <= C_j exp(-v*|r|-beta*(M+1)), j=0,1,2.
```

The differentiation is of the actual transform, not of its nonsmooth
absolute-value upper envelope. The estimates also hold at r=0. Real-axis
integration by parts for the differential operator has zero endpoint terms:
Delta and its differentiated corrections decay there. Consequently

```text
E_M=X-X_M=-(r^2+1/4)*Dhat_M/4
```

has exactly the epsilon bounds printed in review 03. In particular the
second derivative contains `2*C_0+4*|r|*C_1+(r^2+1/4)*C_2`, all divided
by 4. Those terms are necessary and present.

The quadratic error bounds also check. Expanding either in `(X_M,E_M)`
or `(X,E_M)` gives the three linear terms and both possible quadratic
absolute allowances. Review 03's original-theta A_j constants dominate
the contour-shifted moments by the complete theta series, with evenness
used for the other half-strip. Thus its fully specified bound (13) is
valid without unknown X_M values.

The quantifier is genuinely

```text
for every integer M>=1 and every real r, the fixed-M derivative bounds hold.
```

One may therefore select any integer M(r) pointwise afterward. One may
not call the derivatives of `r -> X_(M(r))(r)` the fixed-M derivatives.
No derivative-of-M error was found in the note. In particular, for
`M(r)>=ceil(|r|)+M_0`, its exponent rates are `pi/4+beta` and
`pi/4+2*beta`, with polynomial degrees at most 2 and 4. Both exceed
`pi/2`, as asserted. This is an absolute approximation estimate; it
establishes no lower scale for L1.

I also checked the two endpoint/shape claims. The homogeneous mode at
negative infinity contributes -1 to the weighted boundary bracket, so
the preserved normalization is 1/4. For fixed M the slower artificial
tail is negative after applying D, with leading term
`-a^2*exp(9u/2-a*exp(2u))`. Neither its real-space negativity nor its
cancellation by the complete tail decides the transform's L1 sign.

**Surviving support:** a specified smooth reciprocal approximation with
uniform complete error bounds. **Missing premise:** an independently
proved `L1[X_M](r)>=B_M(r)` or the corresponding Btilde comparison on
every required height, including any zero-margin locations. Mere
nonnegativity of L1[X_M] would not pay a positive absolute error budget.

## 2. Review 02: the local certificate is correctly rejected

For fixed shifts, the simultaneous derivative is
`D=partial_u+partial_v`, not a derivative of their difference. The exact
entrywise integration by parts gives

```text
R_h=w-Dh-(p(u)+p(v))*h,
w=(u+v)^2/4.
```

The integral boundary term is zero under the displayed hypotheses. The
sufficient condition is positivity of every finite residual matrix for
arbitrary real nodes and complex coefficients. Entrywise positivity,
finitely many minors or the original diagonal energies cannot replace
this condition. Positive phi factors preserve matrix inertia.

For `h_*=w/(p(u)+p(v))`, direct differentiation gives

```text
R_*(u,u)=-u/p(u)+u^2*p'(u)/(2*p(u)^2)
        =u*[u*P1(2u)-P(2u)]/[2*P(2u)^2].
```

Both clock factors, `p(u)=2P(2u)` and `p'(u)=4P1(2u)`, are correct.
The complete theta tail gives, for `z=pi*exp(2u)`,

```text
p=-2z+9/2+O(1/z),  p'=-4z+O(1/z),
R_*(u,u)=(u-u^2)/(2*pi*exp(2u))+O(u^2*exp(-4u)).
```

The Gaussian gap from n=1 to n=2 permits the stated differentiated
relative remainder; this is not differentiation of an arbitrary big-O.
The leading term is negative eventually, so the local residual cannot
be positive semidefinite. The fixed Gaussian predecessor also fails by
its displayed original-tail diagonal. These are analytic failures of
these certificate choices, with no numerical threshold asserted.

The initially phrased global removability needs `p'(t)<0` at every real
t: strict concavity as a bare definition can permit isolated second
derivative zeros. This was raised and corrected forward in review 02.
Under the explicit condition, the quotient's expansion at the crossing
is valid and its double-exponential weighted endpoint terms vanish.
Crucially, the large-positive-diagonal calculation is defined and rejects
the candidate even without any global curvature theorem. There is no
remaining dependence on an un-replayed curvature certificate for this
rejection.

The negative residual is not a negative value of the integrated Q. A
one-translate integral remains C(0)>0; compensation elsewhere is allowed.
No exclusion of every divergence correction or nonlocal method follows.

## 3. Review 04: the reference margin is real, the transfer is absent

I read [Gasper, arXiv:0801.2996v1](https://arxiv.org/html/0801.2996v1),
especially (2.6), directly. Its y-squared coefficient supplies review 04's
margin after the frequency rescaling. With
`B_a(r)=K_(ir/2)(a)`, the transform kernel is `exp(-a*cosh(2u))` and
the chain-rule factor in L1 is 1/4. The positive square integral converges
at both endpoints and is strictly positive for each real r, including
reference zeros. This does not claim a constant positive frequency floor.

The independently derived crude lower bound also checks. With
`nu=r/2`, `V=max(2a,nu^2,1)`, integration by parts gives
`integral u^2 exp(-v*cosh u)du<=K_0(v)/v`. The elementary cosine bound
then gives `K_(i nu)(v)>=K_0(v)/2` for `v>=nu^2`. On `[V,2V]`, the
stated elementary K_0 bound and integration length V yield

```text
m_a(r) >= [log(2)/(16V)] exp(-4V-2).
```

The constants and domains are consistent. Its very fast decay does not
make it a practical original-theta comparison automatically.

The perturbation formula in review 04 is exact for real-valued functions
on the real axis. Its sufficient lower comparison (T) may omit epsilon_1
squared because `(E')^2` is nonnegative. Review 03 bounds an absolute
difference and correctly retains that allowance. The two formulas are
not in conflict. Neither divides by a reference at a zero.

The source's shifted Pólya sum is a different reference: the extra term
in (3.3) cannot be dropped on the basis of its conjectured positivity.
The separate real-zero argument does not supply an error from original
theta to that reference. I checked this scope directly in Gasper; I did
not independently re-audit every other paper in review 04's bounded
source table.

**Non-composition warning:** review 03 controls `X-X_M`, while this lane
would need `X-kappa*B_a` or the Pólya difference. No estimate for
`X_M-kappa*B_a`, or lower margin for X_M, is supplied. Thus combining
the two supporting results still leaves an explicit additional unproved
bridge. A smooth kernel, common endpoint normalization, a real-tail match
or a generic real-zero reference theorem does not fill it.

## 4. Review 05: direct control failure with the correct quantifiers

I expanded the product independently. For
`q_beta(r)=3+2cos(beta*r)` and `X_beta=q_beta*X/B_beta`,

```text
B_beta^2 L1[X_beta]
 =q_beta^2 L1[X]+2*beta^2*(2+3cos(beta*r))*X^2.
```

At `r=pi/beta`, this is `L1[X]-2*beta^2*X^2`. The proof then uses
only the complete positive moments `m0,m2`, with `k=m2/m0>0`. For
`beta^2>=pi^2*k`, the moment bounds give `X>=m0/2` and

```text
L1[X]/X^2 <= 4*r^2*k^2+2*k <=6*k<2*beta^2.
```

The advertised explicit upper bound
`-(beta^2-3k)*m0^2/(2*B_beta^2)` follows with the correct inequality
direction, since its coefficient is negative and `X^2>=m0^2/4`.
There is no assumption of the original L1 sign or of any zero's location.
The real division is safe because this argument proves X positive at
the selected point.

Consequently every
`beta>=max{2,pi*sqrt(m2/m0)}` yields a direct negative L1 value while
retaining the NS101 family's critical-strip restriction on its added
zeros. The constants are exact full moments, not estimated finite
prefixes. This is a sufficient analytic parameter range; it is not a
numerically located threshold or a separately established assertion for
the historical beta=2 member.

This control retains the general reciprocal positive-mixture structure,
smooth even boundary matching, endpoint normalization and generic pair
identities. It changes the original lattice and fails the normalized
original Jacobi IVP. Hence it directly rejects the general-properties
inference to first-Laguerre positivity, while leaving an estimate using
the distinguished original arithmetic open. No inference from off-axis
zeros to negative first Laguerre has been used.

Review 01's separate smooth log-concave countermodel likewise checks:
the Gaussian Fourier multiplier gives the printed negative value at pi,
and complete moment domination preserves that strict sign after small
positive double-exponential damping. It matches different hypotheses;
it must not be silently combined with NS101 to claim one model satisfying
every property of both. Neither model has the original Jacobi data.

## 5. Final rendered-report claim and scope check

I read the coordinator's `theta-six-agent-2026-10-05-v1.html` report.
Its central claims match the reviewed notes: the new bound controls
`X-X_M`, the Bessel reference is a different object, a zero margin cannot
absorb a positive absolute allowance, and the reciprocal-family threshold
does not decide the historical beta=2 member. The conditional global
quotient regularity and unconditional diagonal rejection are separated.
The report admits no original-theta sign method and makes no first-Laguerre
to RH inference.

One minor wording correction was requested and verified: the initial
phrase that every calculation retains the original kernel was too broad
for deliberately changed references and controls. The corrected text
says the target retains the complete original kernel and explicitly
identifies approximations and controls. This is resolved. No further
claim/scope correction is required by this check. I did not independently
repeat the coordinator's manuscript-build or browser-layout validation.

## 6. Exact stop and bounded next step

The required all-coefficient original comparison remains

```text
||D1||^2 <= 2||E||^2+Re<D2,D0>
```

for every finite set of real translates and every complex coefficient
vector. Equivalently, the original complete L1 is nonnegative at every
real height. There are no source/parity exceptions that shrink this
quantifier. The existing fixed-prefix closure is not uniform in a growing
cutoff; the new smooth estimates do not reopen that closed fixed family.

The control record is now sharper, and the approximation budget is
explicit. Neither is a positive estimate of the original mixed form.
NS100's actual negative slice continues to exclude only per-slice sign;
Davenport–Heilbronn has different arithmetic/completion and does not
match the original IVP; NS74/83 are NB controls with different domains.
These mismatches are not control passes. No generic inference is admitted
on the strength of a missing match.

No current proposal meets all five admission needs: a complete exact
estimate of the original target, an arithmetic estimating method, its
uniform range, a complete dependency and matched controls. The original
Jacobi equations identify an object but have not estimated the missing
signed comparison. Listing an additional unproved inequality does not
make it a method.

**Budget:** zero for scans, model fitting, larger cutoffs or certificate
replays. A future supplied candidate may receive one bounded paper
admission review only if it states an independently estimable signed
inequality or a complete reference/error comparison, with the actual
original arithmetic step and all-height scope. Such success would prove
the first-Laguerre target only; failure would stop that specified method.
There is no recommendation to try an adjacent variation automatically.

Only this assigned internal note was written. No numerical or symbolic
scan, research row, manuscript change, commit, push or outreach was made.
Other agents' edits were preserved. The one minor phrasing correction
was communicated to and applied by the coordinator in review 02.

**Final wall check: Same open gap.** Zero sign candidates admitted.
Supporting estimates survive in their stated scopes; the complete original
first-Laguerre lower sign, RH, G2 and the actual cofinal signed-arithmetic
lower bound remain open.
