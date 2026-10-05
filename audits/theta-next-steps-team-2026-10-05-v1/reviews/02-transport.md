# Next-step review 02: complete pair transport

**Decision: STOP the currently specified transport mechanism. No independent
estimating lemma is admitted.** The complete original Jacobi evolution remains
unexcluded, but PR76 does not give it a positivity-preserving generator on the
required integrated observables.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR72–76.** What changes:
nothing in the arithmetic input or required inequality. This is an admission
assessment of whether the repaired primitive creates a usable transport
mechanism, not another attempt to derive or compute its sign. The generic
separation-clock justification is already defeated under its stated shared
hypotheses. That scoped stop is not a proved wall for the original Jacobi IVP.

## Reviewed record and scope

The coordinator refreshed and reviewed remote commit
`18d324703969b5bcc9aa94043cfd90a6e8211f34`; the shared local interpretation
checkout reports HEAD `32f599ced1abb2bf2376a715042e6e4101591639`. I read the
current AGENTS section 0 and proposal/relevance gate, README checkpoints,
NEXT_STEPS frozen inputs and October 5 entries, the ZERO-GEOMETRY and
HEAT-TRANSPORT register scopes, evidence/MISSING.md, PR76's derivation and
review 06, PR72's two source/transfer notes, PR73's current README, and PR74's
review 02. The coordinator's full-register review is inherited; this is not
an independent replay of every historical proof. Both original-evidence
recovery groups remain OPEN. No new external theorem is imported here.

The exact target and domain remain

```text
p(r) = r^2 + 1/4,
X(r) = p(r)*Y(r)/4,
J(r) = p(r)^2*(Y'(r)^2-Y(r)*Y''(r))
       + 2*(r^2-1/4)*Y(r)^2 >= 0,  every r in R.
```

Here Y is the transform of the complete original smooth primitive f from
PR76, not a prefix or substituted kernel. The assertion includes zeros of
Y and r=+/-1/2 without division. Since J=16*L1[X], this is precisely the
first Laguerre inequality. It is not RH, an all-order Laguerre criterion, G2,
or the cofinal signed-Weil floor.

## The transport cone is already identified; its generator is missing

The complete associated kernel is

```text
C(t) = integral_R s^2*phi(s+t)*phi(s-t) ds,
L1[X](r) = 4*integral_R C(t)*cos(2*r*t) dt.
```

With the complete decay and inversion hypotheses established in the existing
record, the required sign is equivalent to positive definiteness of C:
every finite matrix `[C(t_i-t_j)]` must be positive semidefinite for arbitrary
real nodes and arbitrary complex coefficient vectors. Pointwise C>=0,
pointwise pair positivity and positivity of the primitive are different
properties. They do not establish this matrix condition.

PR76 review 06 already checked the natural factor-separation family

```text
C_lambda(t) = integral_R s^2*phi(s+lambda*t)*phi(s-lambda*t) ds
            = C(lambda*t),  0 <= lambda <= 1.
```

Its lambda=0 value is the positive constant C(0). For every lambda>0,
however, arbitrary real nodes can be rescaled by 1/lambda, so positive
definiteness of C_lambda is equivalent to the final target. Its reduced
evolution `partial_lambda C_lambda=(t/lambda)*partial_t C_lambda` is singular
at lambda=0. The constant endpoint does not define an independent positive
initial state for a well-posed evolution to lambda=1. Changing the clock
or replacing phi by the positive primitive does not repair this fact.

In particular, taking small positive lambda is not a weaker all-matrix
lemma: it already assumes the full all-height conclusion. Taking finitely
many nodes instead changes the quantifier and requires an unprovided uniform
limit. No smaller separation scan is recommended.

## What the original arithmetic actually supplies

The archived Jacobi data are specific, not merely reflection symmetry:

```text
da/dL=(U+a^2-1)/2,
dU/dL=2*U*(a+chi),
dchi/dL=a*chi-U,
a(0)=chi(0)=0,
U(0)=Gamma(1/4)^8/(64*pi^4),
phi'(u)/phi(u)=2*P(2u).
```

P is the rational logarithmic-slope function of the distinguished state in
PR72's support note; its clock is L=2u. This particular orbit and its original
single-lattice theta coefficients exclude the exact NS101 reciprocal
mixture. They could, in principle, supply an additional signed estimate.

But closure of the two pointwise state vectors is not closure of their
integrated pair observables. PR72 gives, with complete integrals,

```text
A_s(r) = integral_0^infinity phi(s+t)*phi(s-t)*cos(2*r*t) dt,
B_s(r) = integral_0^infinity P(2*(s+t))*P(2*(s-t))
                         *phi(s+t)*phi(s-t)*cos(2*r*t) dt,
partial_s^2 A_s(r) + 4*r^2*A_s(r) = 16*B_s(r).
```

Differentiation of B introduces the next mixed moment containing the
Jacobi vector field applied to P. That moment has no independently supplied
lower estimate. It is signed both through the slope product across t=s and
through the cosine. The modular state at one clock does not provide the
initial values of all these integrated observables: even the coincident
pair integral samples all clocks 2s.

The PR72 closure obstruction excludes finite constant-matrix linear/affine
systems containing its specified complete zero-frequency slice. It does
not exclude variable-coefficient, nonlinear or infinite systems. Nothing in
this assessment enlarges that obstruction. PR74's actual local alternative,
the drift-cancelling residual `h=w/(p(u)+p(v))` in that note's slope notation,
fails on the original large-coordinate diagonal. It therefore cannot serve
as the missing invariant inequality either; arbitrary corrected or nonlocal
certificates remain outside that specific failure.

## Why a heat or positivity label cannot fill the transfer

Ordinary heat-flow preservation of nonnegative real-space functions is
about a different cone from positive definiteness of the complete associated
kernel. The signed cosine transform is not an order-preserving map for
pointwise comparisons. The original Jacobi clock has not been identified
with a heat generator on C or on the corrected target J. Such an identification,
its direction, domain, initial data and invariant-cone statement would all
need proof; no heat theorem is imported on the strength of terminology.

Similarly, f>0 implies that its transform Y is positive definite in the
frequency variable, not that Y is pointwise positive or that L1[Y]>=0.
Even a separate proof of L1[Y]>=0 would still need
`p^2*L1[Y] >= 2*(1/4-r^2)*Y^2` for |r|<1/2: the positive
right-hand threshold offsets a negative polynomial term in J. Transport
must recover the complete J, retaining both terms.
PR76's meromorphic Y is also not silently placed in an entire-transform
class. These are applicability checks, not additional sign obstructions.

## Matched control and exact stop

- **NS101 / PR74–76:** the exact translated mixture has the same smooth
  positive primitive, envelope, unit leading exponential tail, complete pair
  identities, constant coincident-factor limit and dilation evolution. For
  beta>=max(2,pi*sqrt(m2/m0)), the already recorded complete-moment argument
  proves its corrected J is negative at r=pi/beta. This directly rejects the
  implication from those shared hypotheses to positivity transport. It does
  not rely only on off-axis zeros. The mixture changes the original theta
  coefficients and fails the distinguished Jacobi IVP; it is not a
  counterexample to an IVP-specific generator estimate. That mismatch is not
  a control pass.
- **NS100:** its negative original cosine slice rules out a generator argument
  that silently assumes every A_s is nonnegative. It does not rule out the
  complete s^2-weighted integral or a valid signed invariant inequality.
- **Davenport–Heilbronn:** the original conductor, coefficients and completion
  differ, so it is not an instance of the specified Jacobi IVP. No sampled
  control pass or first-Laguerre conclusion is claimed for it.
- **HEAT-TRANSPORT / NS52 and NB controls:** these have different targets and
  domain/rate hypotheses. The exterior-cluster estimate and NB exclusions
  are not transferred to this pair problem.

Thus the precise existing obstruction matches the available structural
transport proposal, while the original arithmetic generator inequality is
an open input. There is no surviving proposed lemma here whose success
would be independently testable before that input is supplied.

## Admission decision and bounded budget

**No new transport research is recommended from these inputs alone.** The
following is a completeness test for a future supplied mechanism, not a
candidate lemma or a renamed version of J>=0. Budget at most **two hours of
paper review**, allocated as follows:

1. **30 minutes:** specify the actual nonsingular evolution and the complete
   observables on which it closes; identify its original theta/arithmetic
   coefficient dependence. A scalar Jacobi ODE or formal moment hierarchy
   alone fails this step.
2. **45 minutes:** exhibit an independently known positive initial object
   and a concrete generator estimate at every null matrix direction. The
   estimate must cover arbitrary real translates and complex coefficient
   vectors, with the regularity/uniqueness needed for cone invariance. The
   full signed estimate may not be assumed as a premise.
3. **30 minutes:** prove the final identification with complete C, or with
   J including its correction, retaining the two infinite tails, mixed
   terms and all real heights. A finite matrix or bounded-height statement
   needs an explicit uniform extension.
4. **15 minutes:** screen the full implication against NS101 and NS100 with
   exact hypothesis matching; reject any claim based only on a mismatch.

Stop at the first missing dependency; do not use the rest of the budget for
nearby clocks, larger matrices or coefficient scans. The present proposal
already stops at step 1 and supplies no starting generator for a new session.
These are all missing transfer steps, not implied deliverables of a two-hour
proof attempt.

**Success consequence:** a complete original-data cone certificate would
prove the stated first-Laguerre target through the displayed identity; it
would not prove RH. **Failure consequence:** reject that specified mechanism
and retain the open original target. Current outcome: no independently
established generator, invariant inequality or arithmetic lower bound;
retain the ZERO-GEOMETRY freeze and do not fund a sign computation.

Only this assigned internal note was written. No calculation run, scan,
certificate, new research row/node, manuscript version, commit, push, outreach
or agent spawn. Other work in the shared checkout was preserved.

**Final wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR72–76.**
RH, G2 and the actual cofinal signed-arithmetic lower bound remain open.
