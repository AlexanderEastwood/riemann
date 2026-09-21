# Scoped meta-obstructions for the remaining G2 estimate

September 21, 2026. Complete analytic result; no new arithmetic-window computation.

The requested universal slogan needs a mathematical restriction. We prove
two precise versions and give a counterexample to its unrestricted meaning.
We do **not** prove that every location-independent estimate fails, or that
all ten recorded closures are instances of one theorem.

## 1. Actual-symbol density-relaxation theorem

Use a=log(lambda), I_a=(-a,a), the unitary Fourier transform after zero
extension, and the original complete beta_a with the strict prime cutoff,
5/4 digamma reference, logarithmic diagonal and all original scale factors.
The form domain consists of physical L2 functions with finite
integral log(2+|xi|)|F_a f|^2. No Fourier cutoff is introduced.

For every physical unit vector, the reflection-averaged density

    p_f(xi) = (|F_a f(xi)|^2 + |F_a f(-xi)|^2)/2

has mass one, height at most a/pi and total variation at most 2a. Reflection
averaging does not alter its beta_a pairing. This statement holds on the
full physical space, hence also on the actual rank-one source complement.
It does not identify that complement with C_a^low.

Let R_a contain all these densities from the full space or the complete
source complement, and also the explicit even probe

    p*_a(xi) = a/(2pi) [w(2a(xi-gamma0)) + w(2a(-xi-gamma0))].

Here w is exactly the v1.37 endpoint-vanishing cutoff probe, not a new
arithmetic test and not a squared Paley–Wiener transform. Every sound
nonnegative budget B_a satisfying

    integral beta_a p >= -B_a     for every p in R_a

must tend to infinity. Proof: a bounded cofinal subsequence bounds all
complete physical forms (or their complete small-residual complement),
so the existing v1.36 reduction implies RH. Under RH, v1.37 gives

    integral beta_a p*_a = (a/pi) J_a <= -a/(6pi^2)

eventually, contradicting that subsequence. The linear rate is conditional;
the absence of every bounded cofinal subsequence is unconditional.

The mass/height/variation relaxation is an explicit instance: p*_a has
mass one, height <=a/pi, and variation <=2a/pi. This is the essential
test of the hypothesis. We do not silently assume arbitrary constraints
are insensitive: sharp local derivative and source-dependent evaluation
bounds may exclude the probe, and are not covered.

With separate sector bounds, the proof gives unconditional divergence of
their maximum. It does not derive separate-sector RH implications.

## 2. Exact full-distribution bound

The optimal mass-and-height-only lower certificate is

    ell_cap(a,b) = inf { integral b p : p>=0, integral p=1, p<=a/pi }
                 = (a/pi) integral_0^(pi/a) b^up(s) ds.

This uses the complete distribution of positive and negative symbol
values and is invariant under all measure-preserving rearrangements of b.
It is the strongest bound sound for every density with these two
constraints, not merely a bound from the minimum or the total negative mass.
The threshold-filling proof is included in the manuscript. For the actual
arithmetic beta_a,

    ell_cap(a,beta_a) -> -infinity.

Adding the stated total-variation constraint still fails by the explicit
probe, although the same rearrangement formula is not claimed for that
smaller class. This is a rigorous extension of the v1.37 scalar obstruction
to full-distribution and derivative-budget relaxations.

## 3. Protected finite-head spectral-orientation theorem

Let M_a=M_(beta_a) on frequency L2. Let E_a be any finite physical head
whose transformed columns belong to D(M_a), and protect the finite space

    S_a = F_a E_a + M_a F_a E_a.

A bound is called spectral-orientation blind with these protected data
if its claimed lower number must remain valid after every unitary
conjugation U* M_a U fixing S_a and preserving the operator domain.
It suffices to require this only for U-I of finite rank.

The infimum of compression Rayleigh values over those orientations and
smooth ordinary-unit physical vectors perpendicular to S_a equals
ess inf beta_a. Indeed any spectral band below r>ess inf beta_a is
infinite-dimensional. Pick a unit vector there perpendicular to S_a;
rotate one smooth physical Fourier vector into it, and fix the orthogonal
complement. This rotation has finite rank, preserves the operator/form
domains, and changes the operator by a bounded finite-rank perturbation.
Since it fixes both F_a e and M_a F_a e,

    U* M_a U F_a e = M_a F_a e    (e in E_a).

Thus it preserves the entire source action and residual, not just a
Rayleigh value. The actual finite Fourier source proxy meets the domain
hypothesis. Both parities can be protected and treated separately. The
head dimension may grow with a, provided it is finite at each a.

The multiplier's essential infimum tends to -infinity by v1.37. Therefore
no orientation-universal lower bound with these data supplies a cofinal
finite floor. This is a theorem about information insufficient to certify
a compression, **not a finite-rank repair of the physical Weil form**.

Critical limit: U* M_a U generally is not a multiplication operator.
The theorem does not create a rearranged prime sequence or refute a method
that retains the physical multiplier structure. No negative physical
Weil test or uniform bound on the adversarial perturbation is asserted.

## 4. Why the unrestricted slogan is false

Let D_a>0 and let E_a be any set with

    |E_a| = pi/[2a(D_a+1)],     b_a=1-(D_a+1)1_Ea.

The elementary physical height bound proves q_b[f]>=||f||^2/2 for every
location and shape of E_a, even as D_a tends to infinity. This is a
location-blind positive estimate with divergent negative depth. The
actual arithmetic theorem therefore needs its signed cutoff-probe
pairing; negative minima alone cannot prove a distribution-blind no-go.

## 5. Candidate register / novelty and dependencies

**ID:** G2.6-META-01. **Status:** proved scoped obstruction, not a live
positive mechanism. **Proposed conclusion tested:** every estimate
insensitive to arithmetic location is incapable of a cofinal sign.
**Result:** two explicit versions are proved; unrestricted wording rejected.

**Closest prior proposals:** v1.37 scalar primitive and pointwise no-gos;
v1.32 negative-only Schatten tests; prior finite-source/metric repairs.
**Essential extension:** arbitrary sound density relaxations admitting the
explicit forbidden probe, including the optimal full-histogram benchmark;
and exact preservation of finite graph columns under a domain-preserving
adversarial spectral orientation. These are formula-level continuations
of information-loss obstructions, not renamed positivity mechanisms.

**What is not covered:** the existing signed Schur/structured inverse
retains actual cross-correlations. Concentration Schatten quantities retain
frequency geometry; they are not merely multiplier spectral data.
Dyadic metrics fix physical partitions. Common-Gram factorizations retain
relative channel alignment. Picone transforms retain jump geometry. Their
failure or success does not follow from the new hypotheses without an
additional proof of blindness. The adversarial review includes a ten-row
coverage audit. Scalar prime-norm domination is covered only to the extent
that a particular application satisfies the exact universal-orientation
hypothesis; its existing arithmetic essential-norm theorem remains separate.

**Primary-literature screen:**

- Fan and Pall, *Imbedding conditions for Hermitian and normal matrices*,
  Canadian Journal of Mathematics 9 (1957), 298–304, Theorem 1:
  <https://doi.org/10.4153/CJM-1957-036-1>. This is the classical finite
  spectral-compression ancestor; our elementary infinite-dimensional proof
  explicitly protects a finite graph subspace and domains.
- Lieb and Loss, *Analysis*, second edition (2001), Section 1.14, bathtub
  principle: <https://www.ams.org/publications/authors/books/postpub/gsm-14-R>.
  The variational rearrangement principle is classical; its formula is
  reproved here for the stated class. The arithmetic divergence application
  uses the existing project probe and bounded-floor results.

These ingredients are known in the literature. The precisely scoped
arithmetic application and protected-data audit are new within the inspected
project record. Worldwide novelty and publication readiness are unresolved.

## 6. Adversarial checks and remaining target

The independent review tested domain preservation, source-action protection,
parity, all normalization constants, the non-multiplier scope, and the
logical use of RH only after deriving it from a hypothetical cofinal floor.
It rejected the claim that all ten closures follow, and the stronger claim
that the probe passes every physical differential constraint.

The exact-rational script checks source-column preservation for zero and
nonzero residuals under a finite unitary swap, and a positive mass-cap
counterexample. It does not substitute a numerical diagnostic for the
requested analytic result. There is no new fixed-window computation.

The precise remaining G2 input is still the complete signed joint
concentration inequality with one uniform finite ordinary lower constant,
both parities, and all physical blocks/couplings not subordinate to the
actual source complement. A successful estimate must impose realizability
or geometric constraints strong enough to exclude the forbidden probes or
orientations. These theorems do not prove such a constraint.

The centered-sampler graph defect, endpoints and all transfer limitations
are unchanged. **No G2 sign gap is closed; RH remains unproved.**
