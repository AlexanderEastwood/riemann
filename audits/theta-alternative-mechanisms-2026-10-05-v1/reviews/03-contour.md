# Proposer 03 — complete quotient contour, no signed estimator

**Decision: no candidate admitted.** A direct contour formula retains an
unestimated signed boundary integral and every nonremovable denominator
zero. A small zero-free strip is already available qualitatively. Widening
it alone does not estimate the Fourier sign. No mixture family, numerical
screen, certificate, research row, thaw or manuscript version is proposed.

Reviewed remote baseline: `221ceec9da825bdc787111447badad961860760a`
(PR78); local scope commit: `b5147e82803cccdb641bcb611b3c90c3c76cf51e`.
Read AGENTS, this audit's brief, PR78 reviews 01/04/06, PR77 review 06,
and PR76's pair-algebra review. The coordinator owns the refreshed complete
register review; no historical proof or certificate replay is claimed here.
Both missing-original recovery groups remain OPEN. No external prior-art
theorem is imported; the following is a paper contour/dependency audit.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–78.**
What changes: examine complex shifts and the spectral density of the
original conditional second moment directly, without a positive-mixture
ansatz. The arithmetic Fourier-sign estimate remains absent.

## 1. Exact object and legitimate complex domain

Keep all original coefficients:

```text
Theta(x)=sum_(n in Z) exp(-pi*n^2*x), Re x>0,
h(z)=exp(z/2)*Theta(exp(2z)),
phi(z)=(h''(z)-h(z)/4)/4,
M(z)=int_R phi(s+z)*phi(s-z) ds,
C(z)=int_R s^2*phi(s+z)*phi(s-z) ds,
k(z)=C(z)/M(z).
```

The connected strip containing the real axis on which the displayed theta
series converges absolutely is `S: abs(Im z)<pi/4`, because
`Re exp(2z)=exp(2 Re z)*cos(2 Im z)>0`. Jacobi inversion gives
`h(-z)=h(z)` and hence even phi throughout S, by analytic continuation
from the real axis. Reality gives `phi(conj z)=conj phi(z)`.
On every closed substrip, the original series on the positive real side,
and this reflection on the negative side, give uniform double-exponential
tails. Consequently the displayed complete real-s integrals and their
derivatives converge locally uniformly throughout S. M and C are
holomorphic, even and real under conjugation there; k is meromorphic.

This is the exact domain justified by these formulas, not a claim that
every possible continuation stops at its boundary. At `Im z=pi/4`, theta
summands lose their exponential n-decay; the differentiated series does
not even have terms tending to zero. Boundary continuation, Abel limits
and any boundary integrability require separate arguments. No integral
on that edge, or beyond it, is used. No growing h-factor is transformed
separately; completing to phi precedes both integrals.

There are no denominator zeros on either coordinate axis inside S:

```text
M(x)>0, x real;
M(iy)=int_R abs(phi(s+iy))^2 ds>0, abs(y)<pi/4.
```

The second equality uses conjugation, not pointwise positivity at complex
arguments. It also gives `C(iy)>0`. Neither identity excludes zeros with
both nonzero real and imaginary parts.

## 2. Uniform tails and what zero-freeness already supplies

PR78's saddle calculation extends uniformly to each closed substrip
`abs(Im z)<=a<pi/4` as `Re z->+infinity`. Put `A=2*pi*exp(2z)`.
In `abs(s)<=Re z/2`, use evenness on the second factor. The complete
product equals

```text
4*pi^4*exp(9z)*exp(-A*cosh(2s))
 *[1-6*cosh(2s)/A+9/A^2]*(1+O(exp(-c_a*exp(Re z)))).
```

Here `Re A>=cos(2a)*abs(A)>0`. The relative lattice remainder is
uniform; outside this central region the full absolute tail is bounded
by a polynomial factor times `exp(-c'_a*exp(3 Re z))`. The complex
Gaussian saddle has magnitude comparable to `exp(-Re A)/sqrt(abs A)`;
thus these errors are negligible also relative to M. The square root
below is its continuous branch in the right half-plane:

```text
M(z)=2*pi^4*exp(9z-A)*sqrt(2*pi/A)*(1+O(A^-1)),
k(z)=1/(4A)-1/(8A^2)+O(A^-3).
```

Evenness supplies the opposite end. In particular, M has no zeros at
sufficiently large `abs(Re z)` on a fixed closed substrip. Its remaining
zeros there are finite. Since none is real, compactness already gives
some unspecified `a0>0` for which M is zero-free on `abs(Im z)<=a0`.
Merely asking for such a strip adds no new sign-producing input.

On every horizontal line avoiding its poles, k is integrable with
exponential end decay. Its real-axis derivatives have the same property,
by the available small holomorphic strip and Cauchy estimates. Ordinary
Fourier inversion is therefore legitimate.

## 3. Complete contour formula, residues and scaling

Define the real even spectral density

```text
K(xi)=int_R k(t)*exp(i*xi*t)dt.
```

For `xi>=0`, choose `0<eta<pi/4` with no pole on the upper line.
The vanishing vertical sides and the residue theorem give exactly

```text
K(xi)=exp(-eta*xi)*int_R k(x+i*eta)*exp(i*xi*x)dx
      +2*pi*i*sum_(0<Im z_j<eta) Res_(z=z_j)[k(z)*exp(i*xi*z)].
```

The finite sum includes **all nonremovable poles**, with multiplicity.
A zero of M cancelled by C is removable; no uncancelled zero is dropped.
For a simple pole `z0=a+i*b`, residue `R=C(z0)/M'(z0)`, its upper
partner is `-conj z0`, with residue `-conj R`. Their joint contribution is

```text
-4*pi*exp(-b*xi)*Im(R*exp(i*a*xi)).
```

For a pole of order m with leading Laurent coefficient `a_(-m)`, its
highest residue term is `2*pi*i*a_(-m)*(i*xi)^(m-1)/(m-1)!`
times `exp(i*xi*z_j)`; retain all lower terms too. If any pole exists,
finiteness on closed substrips supplies a lowest upper height b. Choose
eta strictly above b and below every next height. Let m be the largest
order at height b. Pairing the poles gives

```text
K(xi)=exp(-b*xi)*xi^(m-1)*(T(xi)+O(1/xi))+O(exp(-eta*xi)),
```

where the lower polynomial error is absent if m=1. T is a nonzero real
trigonometric polynomial: distinct pole real parts give distinct
frequencies with nonzero leading coefficients. No constant frequency is
present, since `M(iy)>0`. Its mean is zero and its mean square S is
positive. With `B=sup abs(T)>0`, the inequality
`T^2<=B*abs(T)` and zero mean imply that both positive and negative
parts have mean at least `S/(2B)`. Each therefore exceeds
`S/(4B)` along an unbounded sequence. The smaller errors cannot remove
these signs. An interior nonremovable pole would consequently exclude
`K>=0`. This proves a necessary condition, not existence of a pole:
cancellation/absence of every interior pole is necessary, not sufficient,
for positive definiteness.

The frequency factors in the target transfer are

```text
Fourier(M)(xi)=X(xi/2)^2/2,
Fourier(C)(xi)=L1[X](xi/2)/4,
L1[X](r)=(1/pi)*int_R X(r-xi/2)^2*K(xi) dxi.
```

The last formula uses `C=M*k` and the product/convolution factor
`1/(2*pi)`. Thus `K(xi)>=0` for every real xi suffices for
`J(r)=16*L1[X](r)>=0` for every real r, including zeros. There is
no further sign bridge; first Laguerre alone does not establish RH.

## 4. Candidate audit and controls

The five items would be: **expression**, the complete K above;
**coefficients**, exactly the original theta lattice and completion;
**range**, every real xi, yielding every real r; **method**, a contour
shift plus signed residue and boundary-density estimates;
**transfer**, the exact nonnegative convolution just displayed.
The fourth item does not survive: pole locations/cancellations are
unestimated, and even assuming all of them harmless leaves the signed
upper-line integral. Absolute bounds on that integral are upper bounds
on its magnitude, not lower bounds on its real part. Requiring that
part to be nonnegative in a pole-free strip is exactly the same Fourier
sign, multiplied by `exp(eta*xi)`. No independent arithmetic inequality
for it has been obtained. Moving to the unproved boundary limit does
not repair the issue.

PR78's positive-sech-power rejection does not decide this general K.
PR77's Gaussian-mixture rejection concerns C, not k. Their scope does
not exclude a future direct spectral argument.

NS100 rejects per-slice positivity; this proposal never assumes it.
NS101 shares complete smooth kernels, translations preserving the strip,
the generic quotient construction and conditional convolution transfer.
Its known negative-Laguerre range forces its quotient to fail positive
definiteness, but does not identify whether poles or a pole-free signed
density cause that failure. Original coefficients/Jacobi data differ;
this mismatch is not a successful screen. Davenport–Heilbronn shares
generic contour calculus but not the literal original lattice/completion;
its analytic strip must be checked in its own normalization before any
numerical comparison. NS74/83 concern NB target sensitivity and dyadic
rates and do not instantiate this target. No controls computation is
warranted for a positivity claim without the absent sign-producing lemma.

## 5. A bounded falsification edge, not an admitted positivity test

The pole implication does identify a concrete finite rejection certificate:
one verified zero of M in S at which C is nonzero would exclude general
positive definiteness of k. It would **not** exclude `J>=0`, since k
positive definite is only sufficient for that target.

A bounded protocol could take one externally specified compact rectangle
in `Re z>0, 0<Im z<pi/4`, enclose the complete M/C integrals and their
tails with Arb, certify a positive argument-principle zero count for M
with a zero-free boundary, and certify that C is nonzero throughout that
rectangle. All contour subdivisions, errors and two-precision replays
would be retained; an inconclusive enclosure would prove nothing. This
needs no assumption that the zero is simple. Failure to find a zero in
one rectangle says nothing about other rectangles or Fourier positivity.

No such rectangle is supplied by the present paper analysis. Therefore
this is a precise candidate-specific falsification edge for independent
review, not an approved search, a new sign estimator or an automatic
request to scan the strip. Computation budget remains zero.

**Success would change:** an independently controlled nonnegative K
would settle the complete first-Laguerre obligation. **Actual outcome:**
the contour construction only isolates denominator and density obligations;
neither is an arithmetic estimate. Stop this proposal. Budget used: one
bounded paper audit, zero scans/certificates. No automatic boundary scan,
adjacent mixture, row, thaw, version, outreach or commit.

**Final wall check: Same open gap — NS100/101, PR76–78.**
