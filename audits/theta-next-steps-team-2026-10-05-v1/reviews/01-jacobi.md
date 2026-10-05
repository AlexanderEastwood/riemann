# Review 01 — original Jacobi IVP: no next estimating lemma admitted

**Recommendation: retain the distinguished IVP as an unexcluded source of
arithmetic information, but do not fund another orbit or sign scan.** No
independently estimating two-point invariant with a complete transfer
survives this review. A concrete possible building block — positive
semidefiniteness of the original score's divided-difference kernel — fails
analytically on the original theta trajectory. This is a narrow feasibility
finding, not a closure of the IVP route or a new research row.

Reviewed baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34`, refreshed by
the coordinator. Read current instructions/checkpoints, applicable
register/frozen-input scopes, evidence ledger, PR72's Jacobi notes, PR74's
nonlinear review and PR76's derivation/review 06. The coordinator's complete
register review is inherited; historical proofs were not replayed. Both
original evidence-recovery groups remain OPEN.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101 and PR76.** What
changes: a paper check of whether a two-point matrix inequality extracted
from the actual logarithmic slope could strengthen scalar IVP curvature.
No changed arithmetic assumption or new complete sign estimate is admitted.
The check below rejects one building block; it does not promote an
equivalent expression for the desired sign into a lemma.

## Exact target and original data

Use the complete smooth, positive, even theta kernel `phi`, the PR76
primitive `f`, and the transforms

```text
X(r) = integral_R phi(u)*exp(i*r*u) du = xi(1/2+i*r)/2,
Y(r) = integral_R f(u)*exp(i*r*u) du,
p(r) = r^2+1/4,                    X=p*Y/4.

J(r) = p(r)^2*(Y'(r)^2-Y(r)*Y''(r))
       +2*(r^2-1/4)*Y(r)^2 = 16*L1[X](r).
```

The domain is **every real r**, including zeros of Y and the region
`abs(r)<1/2`. The corrected second term is retained throughout.

To avoid confusing the frequency polynomial p with the real-kernel score,
write

```text
b(u) = phi'(u)/phi(u) = 2*P(2u),
b'(u) = 4*V(P)(2u).
```

Here V is the actual Jacobi vector field, with real clock `L=2u`:

```text
a'=(U+a^2-1)/2,   U'=2*U*(a+chi),   chi'=a*chi-U,
a(0)=chi(0)=0,    U(0)=Gamma(1/4)^8/(64*pi^4).
```

The source's particular trajectory and initial data were checked against
[Planat–Solé, arXiv:2608.19160v1, Proposition 5.3](https://arxiv.org/html/2608.19160v1#S5.SS1).
Its Theorem 1.1 concerns second-level concavity in a **real kernel
coordinate**, not the sign of `J(r)`. No source interval certificate or
global curvature theorem is used in the rejection below.

## The concrete two-point strengthening screened on paper

Scalar monotonicity of the score, even if supplied everywhere, gives
entrywise signs for the symmetric divided difference

```text
D(u,v) = -(b(u)-b(v))/(u-v),    u != v,
D(u,u) = -b'(u).
```

An appealing stronger arithmetic lemma would assert that D is a positive
semidefinite kernel on the entire real line:

```text
sum_(i,j) c_i*conj(c_j)*D(u_i,u_j) >= 0
for every finite set of real nodes and every complex coefficient vector.
```

This is an independently falsifiable statement about the exact original
IVP, not the target J in different notation. It would provide a possible
Gram building block for an integration-by-parts certificate. It is **not**
by itself an established sufficient condition for J, and no such
implication is assumed in this audit.

This candidate building block fails its necessary two-point condition.
Evenness gives `b(0)=0`; smoothness gives a finite `kappa0=-b'(0)`. Thus

```text
det [ D(0,0) D(0,u); D(u,0) D(u,u) ]
 = kappa0*(-b'(u)) - b(u)^2/u^2.                  (1)
```

Put `z=pi*exp(2u)`. The **complete original theta series** has

```text
phi(u) = 2*pi^2*exp(9*u/2-z)
         *[1-3/(2*z)+O(exp(-3*z))],   u -> +infinity.
```

The omitted `n>=2` terms and their first two differentiated relative
remainders are bounded by a polynomial in z times `exp(-3*z)`. Consequently

```text
b(u)  = -2*z+9/2+O(1/z),
b'(u) = -4*z+O(1/z).
```

Substitution in (1) gives

```text
det = -4*z^2/u^2 + O(z) + O(z/u^2) < 0
for all sufficiently large real u.
```

No numerical onset is asserted. This also avoids assuming the sign of
`kappa0`: if it were negative the diagonal condition already failed; for
every finite value the displayed large-u determinant is negative.

The original arithmetic step is the `n=1` exponential and the `n>=2`
square-lattice gap in the differentiated complete theta sum. No reflected
prefix, full-line unfolding or uniform Fourier-error assertion is used.

Therefore an original-IVP proof cannot obtain the desired coefficient
uniformity by declaring this score divided difference positive
semidefinite. Reparameterizing the clocks would require a new complete
transfer, including its weights; it is not automatically a repair.

## What a sufficient pre-integration certificate would still require

The exact existing bridge is useful for stating what has not been
delivered. For any real symmetric function h with vanishing complete
integration-by-parts boundaries, define

```text
R_h(u,v) = (u+v)^2/4
           -(partial_u+partial_v)*h(u,v)
           -(b(u)+b(v))*h(u,v).
```

If `R_h` were a positive-semidefinite kernel for all real nodes, then for
arbitrary real shifts x_i and complex coefficients c_i the complete
identity

```text
sum_(i,j) c_i*conj(c_j)*C((x_i-x_j)/2)
 = integral_R sum_(i,j) c_i*conj(c_j)
   *phi(y-x_i)*phi(y-x_j)*R_h(y-x_i,y-x_j) dy,

C(t)=integral_R s^2*phi(s+t)*phi(s-t) ds
```

would be nonnegative. The associated-kernel identity then gives
`L1[X](r)>=0`, hence `J(r)>=0` at every real r. This is a sufficient
conditional transfer to the exact requested target, without a division by
Y or loss of the low-height correction.

Missing inputs: construct h independently of the desired sign, justify
its complete boundaries, and prove positivity of **every finite residual
matrix** using original arithmetic. Scalar signs, two-by-two minors and
samples do not supply this. This dependency checklist is not a recommended
experiment; no such certificate is available.

PR74 already rejects its specified drift-cancelling h on the original
diagonal tail. The present divided-difference check rejects a different
potential Gram building block before attempting to construct another h.
It does not claim to exclude every correction or every two-point
invariant. In particular, an inequality only about two points need not
give the unrestricted matrix statement required by this bridge.

Even complete success of this bridge proves only the first Laguerre
target. An all-order criterion or a separate valid implication to RH
would remain an additional open input. No transfer to G2 or the cofinal
Weil floor is claimed.

## Controls, decision and bounded budget

**NS100:** the negative slice belongs to the original trajectory itself.
The conditional bridge above integrates the complete pair and never
requires every slice's cosine transform to be nonnegative. Thus NS100
does not exclude the bridge, but it forbids replacing the missing matrix
comparison by per-slice positivity.

**NS101:** its reciprocal mixture retains the generic pair algebra and
the positive primitive but fails the corrected J sign in the recorded
parameter range. It does not solve the distinguished original Jacobi IVP.
Thus it refutes a transfer based only on those shared structural
properties, not a future genuinely IVP-specific estimate. Its mismatch
is not a successful control pass. The rejection in (1) instead uses the
original theta kernel itself, so no analogue mismatch is involved.

**Closest findings:** PR72's signed-moment hierarchy, PR74's failed local
drift certificate, and PR76 review 06's failed separation-clock transport.
No evolution/closure proposal is added. IVP uniqueness identifies the
function without estimating its signed integral.

**Decision:** no next estimating lemma admitted from this lane. Stop the
divided-difference positivity idea and do not replace it automatically by
nearby coefficient choices. The actual J target and the possibility of a
different arithmetic invariant remain open. A future paper proposal must
arrive with a specific new invariant and its full conditional transfer,
not merely the distinguished initial data.

**Success/failure rule and budget:** at most **one hour of paper
feasibility work** for this pre-integration check; no computational budget.
A surviving independently sufficient certificate would justify a new
admission assessment, still only toward first-Laguerre positivity. The
analytic failure here removes this building block from that assessment;
it changes no arithmetic lower bound. Do not extend the budget to orbit
sampling, finite matrices or source-certificate replay without a new
downstream lemma. No scan, row, thaw, version, commit, outreach or agent
was started. Only this assigned internal note was written.

**Final wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76.**
