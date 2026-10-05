# Proposer 01 — explicit nonlocal centering, rejected mixture estimate

**Decision: no candidate admitted.** An explicit Volterra construction
does produce a nonlocal residual with the complete boundary cancellation.
The proposed positive-mixture estimate for that residual fails a necessary
condition from the original theta tail. This is a paper admission rejection,
not a new NS claim or a closure of general nonlocal certificates.

Reviewed remote baseline: `670864385024041d24612cf620054c1975473928`;
local scope commit: `b914ac47e8006951a22d030e920d592243e7e0fe`. Read AGENTS,
the current admission brief/record, applicable frozen-input and missing-evidence
entries, and PR77 reviews 01, 02, 06. The coordinator's complete-register
review is inherited, not independently replayed. Both missing-original
recovery groups remain OPEN. No external theorem is imported to establish
the rejection below.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–77.** The
specific changed hypothesis assessed is a positive mixture for the original
pair's conditional second moment, rather than the failed score Gram or
local drift residual. The displayed asymptotic rejects this mixture class.
It does not decide positive definiteness of that conditional moment itself.

## Exact nonlocal construction and conditional transfer

Use the original complete even theta kernel, with all coefficients one:

```text
phi(u)=sum_(n>=1) [2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2)]
                   *exp(-pi*n^2*exp(2u)), u>=0;
phi(-u)=phi(u).
w(s,t)=phi(s+t)*phi(s-t),
M(t)=int_R w(s,t) ds > 0,
C(t)=int_R s^2*w(s,t) ds,
k(t)=C(t)/M(t).
```

There is no prefix, coefficient choice, clock deformation or transform
division. In particular `M(t)>0` everywhere. Write
`s=(u+v)/2`, `t=(u-v)/2`, `b=phi'/phi`, and define

```text
V(s,t)=int_(-infinity)^s [a^2-k(t)]*w(a,t) da,
h(u,v)=V(s,t)/w(s,t).
```

This is an actual construction, not an unspecified correction. Since
`(partial_u+partial_v)=partial_s`, it gives exactly

```text
R_h(u,v)=(u+v)^2/4-(partial_u+partial_v)h-[b(u)+b(v)]h
         =k((u-v)/2).
```

The defining centering gives `V(-infinity,t)=V(+infinity,t)=0` for
every fixed real t. These are precisely the flux boundaries in PR77's
complete integration-by-parts bridge, including arbitrary fixed translates.
The relevant integrals are absolutely convergent by the complete theta
tails. Symmetry in u,v follows from evenness in t. Thus an independent proof
that k is positive definite would supply this nonlocal certificate. Equivalently,
M is already an autocorrelation, and the pointwise product `C=M*k` is positive
definite whenever k is. The exact existing transfer is

```text
L1[X](r)=4*int_R C(t)*cos(2*r*t)dt >= 0,
J(r)=16*L1[X](r)>=0, every real r.
```

Zeros and the low-height polynomial correction are retained automatically.
This proves only the first Laguerre target conditionally, not RH or G2.
The construction alone estimates no sign: k positive definite is the
additional unproved input, not a consequence of conditional centering.

## The concrete estimator assessed

The proposed sufficient arithmetic lemma was

```text
k(t)=int_[0,infinity) sech(2*t)^a dnu(a), all real t,
nu a finite nonnegative measure, nu([0,infinity))=k(0).
```

Each power with `a>0` is positive definite: substitution `x=exp(4t)`
in its Fourier integral gives

```text
int_R sech(2t)^a*exp(i*r*t)dt
 =2^(a-2)*abs(Gamma(a/2+i*r/4))^2/Gamma(a) > 0.
```

The `a=0` member is the constant kernel. Positive mixtures therefore give
the required matrix inequality and the complete transfer above.

The planned estimating method was a positive Laplace representation of
the exact original-lattice quotient

```text
Q(z)=k(0.5*arcosh(exp(z))), z>=0;
Q(z)=int exp(-a*z) dnu(a).
```

This is the positive-power/positive-Laplace class, not arbitrary positive
definite k. The first original-coefficient feasibility check is its large-z
asymptotic. That check fails before a positive density or derivative-sign
argument can be attempted. Thus no unsupported claim that such a method
will work is being made.

## Original-lattice tail rejects the proposed class

Let `t -> +infinity` and `A=2*pi*exp(2t)`. In `abs(s)<=t/2`, both
positive kernel arguments `t+s,t-s` tend uniformly to infinity. Their
complete series gives the dominant product

```text
w(s,t)=4*pi^4*exp(9t)*exp(-A*cosh(2s))
       *[1-(6/A)*cosh(2s)+9/A^2]
       *[1+O(exp(-c*exp(t)))].                       (1)
```

Here c is some fixed positive constant for sufficiently large t. To justify
the uniform relative remainder, factor out the n=1 term in each original
series: the n>=2 terms have exponent gap at least
`3*pi*exp(2*(t-abs(s)))>=3*pi*exp(t)`; their polynomial coefficients are
absorbed by a smaller positive c. The n=1 polynomial is bounded away from
zero throughout this region for large t.

Outside `abs(s)<=t/2`, the complete bound
`phi(x)<=K*exp(-c0*exp(2*abs(x)))`, for fixed positive K,c0, bounds
the zeroth and second moment tails by a polynomial factor times
`exp(-c1*exp(3t))`. This is negligible relative to the main integral,
whose size is a positive constant times `exp(9t-A)*A^(-1/2)`.
The absolute tails of the model in (1) obey the same needed negligibility.
Consequently its moments can be extended to the full s-line with errors
smaller than every inverse power of A. This uses no forbidden termwise
full-line unfolding of the original theta series.

Put `y=2s`, followed by `y=x/sqrt(A)`. Taylor expansion at the unique
minimum of cosh, with the usual Gaussian-integrable remainder and an
exponentially small outer region, gives

```text
I_j(A)=int_R y^j*exp(-A*cosh(y))
                 *[1-6*cosh(y)/A+9/A^2]dy, j=0,2;
I_0=exp(-A)*sqrt(2*pi/A)*[1-49/(8A)+O(A^-2)],
I_2=exp(-A)*sqrt(2*pi)*A^(-3/2)*[1-53/(8A)+O(A^-2)].
```

The coefficients are directly checkable: the order `A^-1` correction is
`-6-x^4/24`; Gaussian moments `E[x^4]=3`, `E[x^6]=15`
produce `-49/8` and `-53/8`. The nonconstant part of the polynomial
reweight first enters at the next order. Hence the complete original ratio is

```text
k(t)=I_2/(4I_0)+negligible
    =1/(4A)-1/(8A^2)+O(A^-3).
```

Since `z=log cosh(2t)` and
`exp(2t)=2*exp(z)-(1/2)*exp(-z)+O(exp(-3z))`, this becomes

```text
Q(z)=exp(-z)/(16*pi)-exp(-2z)/(128*pi^2)+O(exp(-3z)).  (2)
```

Equation (2) contradicts the proposed positive Laplace representation.
Indeed finite nonnegative nu and `exp(z)Q(z)->c=1/(16*pi)` force
support in `[1,infinity)`: any positive mass below 1 would make that
limit infinite. Dominated convergence then forces `nu({1})=c`.
It follows that `exp(z)Q(z)>=c` for every z>=0, whereas (2) makes it
strictly smaller than c for all sufficiently large z. No onset height is
computed or claimed.

## Controls, scope and stop

NS100 excludes individual slice positivity, which this construction never
uses. NS101 shares positive complete kernels and the Volterra centering
identity, so those generic facts cannot estimate the target. Its translated
mixture changes the original one-lattice tail and Jacobi IVP; no mismatch is
advertised as a control pass. The decisive screen here is a necessary
condition on the original kernel itself. Davenport–Heilbronn has different
coefficients/completion and is not an instance of the exact proposed
original-lattice formula. No off-line-zero inference is made. NB target and
rate controls do not match this first-Laguerre assertion.

**Closest result:** PR77 review 06 excludes positive Gaussian mixtures for
C. That does not already exclude the present positive sech-power mixtures
for the different, exponentially decaying quotient k. PR77's score-Gram and
local-residual failures likewise do not imply (2). The negative second
tail coefficient supplies this candidate-specific rejection.

**Success would have changed:** a positive representation would have supplied
an independently sufficient nonlocal certificate for complete J, with no
further sign estimate. **Actual failure changes:** stop this precise positive
mixture ansatz. General positive definiteness of k, other h, and the original
J target remain open; no adjacent repair is proposed.

**Budget:** this bounded paper feasibility pass is complete. Zero scan or
certification budget; one independent algebra/tail review is appropriate.
No research row, thaw, manuscript version, computation run, commit, outreach
or agent spawn. Only this assigned internal note was written.

**Final wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–77.**
The specified nonlocal positive-mixture candidate is rejected on paper;
the full original arithmetic sign remains unestimated.
