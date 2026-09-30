# NS57: independent review of bounded-perturbation detection

Reviewed base: `b55d13ef6975e14a1f5b3cffe82381a68d64d943`.
Reviewer: delegated mathematical reviewer, 2026-09-29.
Scope: the negative perturbation directions and their transfer to compact
smooth tests, specialized to `delta_2=-log(2)/100`. This is a dependency
audit, not new RH research, a numerical test, or a new research row.

**Verdict:** no defect found in these two links. The construction gives
real negative compact smooth tests in each parity, conditional on the
explicit archived realization and radical inputs listed below. It does
not itself prove the subsequent first-zero theorem, locate a first zero,
or establish a sign for the original Weil form.

**Wall check: Same open gap** for original KERNEL-API. This audit validates
part of NS57's existing control dependency; it provides no new arithmetic
estimate and does not strengthen PR #63's scoped bounds-only obstruction.

## 1. Source provenance and boundaries

The following bytes were read at the reviewed base and hashed locally:

| Source | SHA256 |
| --- | --- |
| `evidence/v156/proof.tex` | `c6ebe402b4555ec18384457f6a24222170a20599ec889dd9848b9d2019b8a384` |
| `evidence/v136/new_section.tex` | `78e5f6cb2fe60bff4b6edd41594e8499d815cf4cd20b9d96eb0dec7b628828a3` |
| `evidence/v136/adversarial_review.md` | `2075651e73d84fc3b3c698853e96914ac29a2a301324f750c1aeba40230d2cbd` |
| `evidence/v135/new_section.tex` | `95b12e631f5f55c987ca8ddfdb1c8712b2a40bbaa01967ec29157742769b77fa` |

Relevant labels are `lem:ns57-bounded-detection`, `lem:ns57-symbol-signs`,
`cor:ns57-finite-weight-negative`, `lem:v136-total-radicals`,
`prop:v135-growing-radical`, `eq:v135-gaussian-tail`, and
`eq:v135-weighted-tail`. The earlier independent v1.36 review explicitly
checks arbitrary real translates, ordinary rather than form-norm density,
complete residuals, parity, and fixed-vector quantifiers. I reconstructed
the needed argument below rather than treating that earlier verdict as
a replacement for it.

Inherited, not independently reproved here:

- The canonical complete local operator `A_a` and closed form `q_a`, their
  support-consistent compact-test realization, and its full archimedean,
  prime, and pole formula. The inner product is linear in its first slot;
  the Fourier transform is unitary.
- The original Gaussian source `phi` is real, even, nonzero, smooth and
  ordinary-L2 normalized, with the derivative tail estimate in v1.35.
  Its normalization is not used as a sign premise.
- Every real translate of this source is a polarized global radical:
  `W phi(.-t)=0` distributionally against compact logarithmic tests.
  This arithmetic identity is an input. I have not rederived the Gaussian
  source construction, Poisson summation, or its underlying radical theorem.

No bounded-floor implication, strong-resolvent limit, quantitative v1.53
sensitivity rate, compact-resolvent theorem, or first-eigenvalue continuity
is needed for these two links. Their validity is not being re-audited here.

## 2. Explicit negative directions, with real and parity checks

Put `d=log(2)/100>0`, `ell=log(2)`, and `delta_2=-d`. With the v1.56
convention `(T_t f)(x)=f(x+t)`, the exact perturbation is

`B=d(T_ell+T_-ell)` and `q_delta[f]=q[f]+<Bf,f>`.

Indeed, `-2 delta_2 Re<T_ell f,f>=2d Re<T_ell f,f>`; no sign has been
lost by changing conventions for translation. Since `T_t*=T_-t`, B is
bounded self-adjoint, preserves real functions, and commutes with
reflection. Its Fourier multiplier is `b(xi)=2d cos(ell xi)` and
`||B||=2d`. The modified coefficient remains strictly positive:
`w_2+delta_2=log(2)(1/sqrt(2)-1/100)>0`.

Choose a real smooth Fourier bump `eta` of L2 norm one, with compact
support in

`J=(2 pi/(3 ell),4 pi/(3 ell))`.

On J and its reflection, `b<=-d`. These intervals are disjoint. Set

`v_even_hat(xi)=(eta(xi)+eta(-xi))/sqrt(2)`,

`v_odd_hat(xi)=i(eta(xi)-eta(-xi))/sqrt(2)`.

Both have norm one. Their Fourier Hermitian symmetry
`v_hat(-xi)=conjugate(v_hat(xi))` gives real physical vectors; their
reflection parities are respectively even and odd. Plancherel gives
`<Bv_sigma,v_sigma><=-d` in each sector. Thus there is no need here to
assume independence of prime logarithms, invoke a mean-value limit, or
infer odd negativity from an even test. These are initially ordinary L2
(in fact Schwartz) vectors, not compact physical Weil tests.

## 3. One fixed finite radical combination comes before the window limit

The v1.35 tail gives every exponential moment of phi, so its Fourier
transform is entire and not identically zero. Its real zeros have measure
zero. If a vector is orthogonal to every translate, Fourier uniqueness
applied to the L1 product of its transform with the conjugate transform
of phi makes that vector zero. Consequently the finite complex translate
span is dense in ordinary L2. This is not a density statement in any
global Weil form norm.

For either of the fixed real vectors above, take a finite translate
approximation and then apply its bounded real-part and parity projections.
Because phi is real and even, the resulting `h_sigma` is still a finite
linear combination of real translates, is real, has the requested parity,
and can satisfy `||h_sigma-v_sigma||<1/16`.

Boundedness now provides a numerical margin without any unbounded-form
continuity assumption:

`|<Bh,h>-<Bv,v>| <= ||B|| ||h-v|| (||h||+||v||)`

`< (2d)(1/16)(33/16)=33d/128`.

Therefore `<Bh_sigma,h_sigma><-95d/128<-d/2`. Fix this finite combination,
including every coefficient and translate center, at this point. It will
not depend on the later growing window. The proof needs no uniform bound
on those coefficients as an approximation tolerance changes.

## 4. Complete cutoff transfer, including the exterior rows

Use the original even physical cutoff `chi_a` and set `g_a=chi_a h_sigma`.
It is real, has the same parity, and is smooth with support strictly inside
`I_a=(-a,a)`. It converges to `h_sigma` in ordinary L2. The smooth compact
test is in the actual operator domain: the complete fixed-window
archimedean action maps it to L2, and the remaining fixed-window prime and
pole contributions are bounded operators. Boundedly perturbing this
operator leaves its domain unchanged.

Here is the part of the complete residual estimate checked from v1.35.
For any one of the finitely many fixed translate centers t, eventually
`|t|<=a/2`. Write `r_(a,t)=(1-chi_a)phi(.-t)` on the whole line. The cutoff
and Gaussian derivative bound give

`||r_(a,t)||_(H1)+sup_x e^(2|x|)(|r_(a,t)(x)|+|r'_(a,t)(x)|)`

`<= C exp(-pi e^a/(4e^2)) =: delta_a`.

The exterior-tail derivation uses only `|t|<=a/2`, not membership in the
spaced lattice used for the separate growing-Gram theorem. On the tail,
`X=e^(2|x-t|)>=e^a/e^2` and `e^(2|x|)<=e^a X<=e^2 X^2`; the Gaussian
absorbs these polynomial factors. Thus no lattice Gram estimate or
increasing-rank argument is imported into this fixed-combination proof.

The inherited global radical identity yields
`A_a(chi_a phi(.-t))=-W r_(a,t)` on I_a. Every term of the right side is
retained:

- The archimedean multiplier is bounded by `C(1+|xi|)`, giving L2 norm
  at most `C delta_a` from the H1 bound.
- Every prime row, including `n>e^(2a)`, is covered by
  `sum_(n>=2) Lambda(n)n^(-1/2)|r_(a,t)(x +/- log n)|`
  `<=delta_a e^(2|x|) sum_(n>=2) Lambda(n)n^(-5/2)`.
  The latter sum converges absolutely, including prime powers. Thus
  its L2 norm on I_a is at most `C sqrt(a)e^(2a)delta_a`.
- Both pole kernels are kept. Absolute values bound each integral by
  `C delta_a e^(|x|/2)`, since `e^(+/-y/2)e^(-2|y|)` is integrable.
  In particular the negative odd pole term has not been silently deleted
  or made positive; only a residual norm is being bounded.

These estimates give a complete operator residual tending to zero,
with the weaker convenient bound
`||A_a(chi_a phi(.-t))||<=C sqrt(a)exp(-e^a/100)`.
The finite fixed coefficient sum then gives `||A_a g_a||->0`, with a
constant allowed to depend on the already fixed h_sigma. There is no
finite-head approximation or interchange with a divergent prime sum.

## 5. Compact negative tests and exact quantifier order

As a consequence of the preceding domain and residual facts,

`|q_a[g_a]|=|<A_a g_a,g_a>|<=||A_a g_a|| ||g_a|| -> 0`.

Ordinary convergence and boundedness of B also give
`<BE_a g_a,E_a g_a> -> <Bh_sigma,h_sigma><-d/2`.
Choose a sufficiently large finite a so that the first absolute value is
less than d/8 and the second expression differs from its limit by less
than d/8. Then

`q_(delta,a)[g_a]<-d/4<0`.

The negative value ensures that g_a is nonzero. It is the required real
compact smooth negative test in that parity; support consistency makes
it a test of the perturbed global compact-test form as well. The entire
construction is repeated in the other parity, or the larger of the two
finite window thresholds is chosen.

The order is: fix delta; choose a negative ordinary vector; choose and
fix a finite radical approximation with a strict bounded-B margin; only
then increase a until cutoff and complete residual errors are small.
No limit of coefficients depending on a, no graph-norm density, no
uniform positive spectral gap, and no assumption of RH enters this step.

The conclusion is exactly the negative-test input to NS57. Turning it
into a finite nonnegative first-zero window requires the separately
reviewed small-window positivity, continuity and compact-resolvent links.
Those links and the original source/radical construction remain explicit
dependencies of any use of the complete control theorem.
