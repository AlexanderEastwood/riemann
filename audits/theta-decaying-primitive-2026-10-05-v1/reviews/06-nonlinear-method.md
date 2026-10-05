# Review 06: can the original Jacobi flow transport the pair sign?

**Disposition: OPEN target; STOP this proposed estimating mechanism.**
No independent original-arithmetic estimate survives this bounded review.
The boundary repair in the draft does not supply a positivity-preserving
evolution for its corrected expression (10).

Reviewed remote baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208`
(PR75); local audit scope commit `edc6563`. I read the review brief,
draft derivation, AGENTS proposal/relevance rules, current ZERO-GEOMETRY
record, evidence ledger, PR72's two Jacobi source/transfer notes, PR73's
pair report, and PR74's local nonlinear certificate review. I also checked
the stated source scope and Jacobi-system definitions in
[Planat--Sole, arXiv:2608.19160v1, Sections 1 and 5](https://arxiv.org/html/2608.19160v1).
The coordinator's all-node review is inherited, not represented here as my
independent review of every historical proof. No source certificates were
replayed. Both original-evidence recovery groups remain OPEN.

**Wall check: Same open gap.** Closest: NS100/101, PR72--75. The precise
question is whether the distinguished real-clock evolution can transport
positive definiteness from coincident factors to the complete shifted
pair. This is a paper applicability check, not a proposed new sign lemma
or an attempted proof of one.

## 1. The one mechanism assessed

Keep the complete original kernel and its normalization:

```text
C(t) = integral_R s^2*phi(s+t)*phi(s-t) ds,
L1[X](r) = 4*integral_R C(t)*cos(2*r*t) dt.
```

The draft's corrected requirement (10) is exactly `L1[X](r)>=0` at every
real height. Equivalently, the complete kernel C must be positive definite:

```text
sum_(i,j) c_i*conj(c_j)*C(t_i-t_j) >= 0
for every m>=1, every (t_1,...,t_m) in R^m,
and every (c_1,...,c_m) in C^m.
```

The possible transport mechanism is: start with coincident factors and
separate their two Jacobi clocks while preserving this matrix cone. A
concrete way to expose the proposed clock is

```text
C_lambda(t) = integral_R s^2*phi(s+lambda*t)*phi(s-lambda*t) ds
            = C(lambda*t),                  0<=lambda<=1.
```

At lambda=0 the kernel is the positive constant C(0), so every matrix is
positive semidefinite. The proposal would need a legitimate evolution
from that positive initial kernel to lambda=1, whose positivity follows
from independently estimated properties of the actual Jacobi orbit.
The equality above is only an examination of this transport interpretation;
it is not a new research candidate or an estimate.

## 2. What the original arithmetic contributes, and what it does not

PR72's checked clock is `L=2u`; write `P` for the logarithmic derivative
in that clock and `V` for its three-state vector field. The kernel slope
is `phi'(u)/phi(u)=2*P(2u)`. At the separated clocks, differentiation uses
the multiplier

```text
2*t*[P(2*(s+lambda*t))-P(2*(s-lambda*t))].
```

Thus an arithmetic step beyond NS101 would have to use the **distinguished
trajectory and its fixed initial data** to prove that the integrated,
weighted multiplier generates an inward-pointing evolution for every
finite matrix and every coefficient vector. A scalar sign of P or V(P)
does not do this: the required property is a sign of arbitrary mixed
quadratic forms, not of individual entries. The source's real-kernel
curvature cone is a different cone and a different target.

Two concrete problems prevent this from becoming an estimating method:

1. For every fixed lambda>0, positive definiteness of `C_lambda` is already
   equivalent to positive definiteness of C: arbitrary real nodes remain
   arbitrary after division by lambda. There is no weaker intermediate
   all-matrix claim to propagate through positive lambda values.
2. The generic reduced evolution is
   `partial_lambda C_lambda=(t/lambda)*partial_t C_lambda` for lambda>0.
   It is singular at lambda=0. The constant limiting kernel does not supply
   a well-posed, positivity-preserving initial-value problem there. All
   smooth complete associated kernels have this constant limit, including
   the NS101 family that fails the actual first-Laguerre target in PR74's
   stated parameter range.

This does not rule out a different nonsingular arithmetic evolution. It
shows why “start on the positive diagonal and run the original ODE” is not
one as stated. In particular the modular initial state of the original
three-state ODE is not initial data for all complete matrix observables:
even at lambda=0 the integral ranges over the full clock `2*s`.

## 3. Additional inputs required for a genuine transport proof

Such a proof would need all of the following, none supplied by this audit:

- A closed, nonsingular evolution on complete pair observables (possibly
  infinite dimensional), with a specified domain and controlled tails.
  The scalar Jacobi vector field alone is not a closed evolution for these
  integrated observables; PR72 records the next mixed moment it introduces.
- Initial positive definiteness for every matrix size in that evolution,
  at a nonsingular initial parameter, justified independently of the final
  first-Laguerre inequality.
- An inward-cone inequality at every possible zero direction, retaining
  every complex coefficient vector and real translate. Precisely, if M is
  a boundary positive-semidefinite matrix along the chosen evolution, one
  needs a justified generator condition on `c^*M'c` whenever `Mc=0`, with
  the regularity needed to infer invariance. Naming this condition is not
  establishing it.
- An explicit use of the distinguished Jacobi data to establish that
  generator condition, and a proved identification of the final kernel
  with the original complete C. All mixed terms and both infinite tails
  must remain. No finite set of matrix minors supplies the quantifier.

The unresolved item is the third, with no independent estimating mechanism
for it from the fourth. The current regularization only resolves transform
domains. It neither provides a closed generator nor supplies an initial
positive kernel at a nonsingular parameter. Accordingly this list is a
precise stop report, not a conditional candidate offered for a new scan.

## 4. Existing nearby attempts and matched control

PR72 already found that integrating the two-clock Jacobi dynamics creates
an unestimated signed moment and then a hierarchy. Its exclusion concerns
finite constant-matrix closures containing a specified slice; it does not
exclude all nonlinear or infinite evolutions. It nevertheless prevents
silently treating the original three-state closure as closure after
integration.

PR74 review 02 assessed an actual local alternative: remove a total
derivative using the original logarithmic slope and require the residual
kernel to be positive semidefinite. Its explicit drift-cancelling choice
fails already on the original large-coordinate diagonal. The positive
primitive does not repair that original-phi certificate. Applying a new
certificate to the primitive would also have to retain the polynomial
correction in draft (9)--(10); proving only `L1[Y]>=0` would miss the
positive right-hand side in `abs(r)<1/2`.

NS101/PR74 supplies a matched control for the generic transport inference:
its complete positive even kernels have the same constant diagonal limit,
the same dilation identity, and the draft's positive primitive, envelope,
unit tail and corrected algebra. Its first-Laguerre target fails for the
already recorded beta range. Therefore those shared ingredients cannot
justify transport from lambda=0. It changes the original coefficients and
does not solve the distinguished Jacobi IVP, so it does **not** refute an
actual IVP-specific generator inequality. That missing hypothesis is a
concrete mismatch, not a passed control.

NS100 excludes per-slice positivity; this review retains the integrated
pair and does not infer a complete sign from slice signs. Davenport--
Heilbronn has different coefficients, conductor and completion and is not
a matched original-IVP model. NS74/83 concern NB coefficient/rate domains
and are not controls of the present matrix evolution. No new control was
run and no sampled pass is asserted.

## 5. Decision

**No independent method is admitted.** Stop the direct “positive initial
diagonal plus Jacobi clock” transport proposal. The repaired primitive is
useful algebra and boundary accounting, but it does not change this stop.
An original-arithmetic invariant-cone estimate remains possible in
principle and unprovided here. There is no basis for funding a numerical
orbit scan, a larger matrix table, or source-certificate replay from this
review alone.

Success of a separately supplied complete generator certificate would
prove only the stated first-Laguerre target through this dependency, not
RH or the all-order criterion. The present failure changes route selection
only: it rejects this transport justification and admits no replacement.
Budget: one paper review, now complete; no computation budget follows.
Only this assigned internal note was written. No row, thaw, manuscript
version, commit, push, outreach, or extra agent was started.

**Final wall check: Same open gap -- ZERO-GEOMETRY, NS100/101 and PR72--75.**
