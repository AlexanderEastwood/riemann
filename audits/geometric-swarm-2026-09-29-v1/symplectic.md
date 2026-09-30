# Prime-period contact blocks and a connected six-dimensional completion

Internal construction/admission note, 2026-09-29. Reviewed remote baseline
`b5bd5fa`, current AGENTS.md, OPERATOR-BRIDGES/WEIL-FLOOR/ZERO-GEOMETRY,
NS47's actual signed lift and controls/README.md; the parent completed the
all-conclusions/status/evidence review. No historical computation was replayed.

**Wall check: Same open gap.** Closest: OPERATOR-BRIDGES, NS47 and NS94/100/101.
What changes is a specified contact model carrying the actual prime-power
periods and weights. No new signed arithmetic estimate or global positivity
transfer is supplied. These are construction specifications, not research-row
claims, thaws, novelty claims or proposed numerical scans.

| Candidate | Geometry and actual arithmetic | First independent decision | Status |
|---|---|---|---|
| A: prime-period blocks | Explicit disconnected exact symplectic 4-manifold; periods log p, hyperbolic multiplier p, geometric half-density weight p^(-m/2) | Can its naturally weighted graded transport be completed with the original archimedean/pole contribution and a genuine positive realization? | Local object specified; global bridge absent |
| B: connected completion | Proposed connected exact symplectic 6-manifold assembled from prime tubes with total unstable exponent one | Can two tubes be connected without an uncancelled mixed primitive orbit? | Gluing and completion unconstructed |

## A. An explicit four-dimensional arithmetic object

For each prime p set T_p=log p and

    W_p = T*(R/T_p Z) × R²,
    λ = τ dt + y dx,     ω = dλ,
    H = τ + xy,          ι_(X_H)ω = −dH.

Then X_H=∂t+x∂x−y∂y and λ(X_H)=H. On Y_p={H=1},

    α = (1−xy)dt + y dx,
    R = ∂t+x∂x−y∂y,
    φ_s(t,x,y) = (t+s,e^s x,e^(−s)y).

Here α(R)=1 and ι_R dα=0; α∧dα=dt∧dy∧dx never vanishes. These are local
algebraic checks, not an arithmetic inequality. The only closed orbit has
x=y=0, primitive period T_p, and forward transverse return map
diag(p,p^(-1)). Every repetition m has period m log p. The countable
disjoint union W=⊔_p W_p remains a smooth four-dimensional manifold, but it
is disconnected and noncompact. The prime list is input; this construction
does not explain the primes' distribution.

There is a concrete candidate transport beyond attaching arbitrary weights.
On Y_p use horizontal exterior forms (ι_R u=0), tensored with the unstable
covector half-density line L=|E_u*|^(1/2), and U(s)=φ_(−s)*. The initial
domain is C_c^∞(Y_p; Λ^k Ann(R)⊗L), k=0,1,2; its infinitesimal expression
is −Lie_R, including the induced bundle action. No closed Hilbert-space
realization is asserted. The unstable direction expands by e^s; pullback
on L therefore contributes e^(−s/2). This is induced by the chosen flow,
not an independently fitted nonunitary flat-line holonomy for each prime.
It nevertheless is not a unitary coefficient system, and choosing these
local expansion rates has encoded arithmetic rather than derived it.

The standard local flat-trace formula has numerator tr(Λ^k P), denominator
|det(I−P)|, and primitive period T_p. With the inverse-return convention
P=diag(p^(−m),p^m), the alternating numerator is det(I−P)<0. Thus the local
graded orbit contribution is

    −(log p) p^(−m/2) δ(s−m log p),     m≥1.

The sign is negative for every repetition, not an alternating sign in m.
This cancellation uses all exterior degrees; it is not a positive ordinary
trace. The compactly supported time distribution on s>0 is locally finite:
only finitely many p,m have m log p in a bounded interval. A spatial cutoff
equal to one near the central orbit suffices for the local trace. These
observations justify an orbit-encoding target, not global spectral identities.

The formula and convention come from [Dyatlov–Zworski, §2.2 and Appendix B](https://math.berkeley.edu/~zworski/zeta.pdf).
Their global meromorphic-continuation theorem assumes a compact smooth
Anosov flow with orientable stable/unstable bundles. Our disjoint noncompact
union does not meet that theorem. Its local fixed-point calculation must not
be promoted by citation to a global Fredholm determinant.

The Laplace series of the displayed orbit distribution is ζ'/ζ(z+1/2)
only in Re z>1/2. Crossing that boundary requires analytic continuation,
domain control and the missing completion; damping alone supplies none.

For a bounded local algebra batch, k hyperbolic pairs of positive rates a_j
give, with r=p^m>1 and a global grading shift b,

    T_p (−1)^(k+b) r^(−Σ_j a_j/2).

The target requires Σ_j a_j=1 and k+b odd. Equal unit rates reproduce it
only for k=1; equal rates 1/k and a chosen parity shift are a changed model.
Replacing p by the composite 6 preserves every local identity while adding
an unwanted primitive log 6 term. Adding a block labelled 4 alongside 2
duplicates the period 2 log 2 with an extra primitive weight log 4. This is
an exact label-indifference control, not a false RH analogue or a spectral
test. General analytic trace existence remains unproved.

## B. A six-dimensional connected completion problem

Use local blocks W_p^(6)=T*(R/T_p Z)×R⁴ with

    λ₆=τdt+y dx+v du,     H₆=τ+(xy+uv)/2.

Their five-dimensional contact energy surfaces have two unstable exponents
1/2, hence total unstable half-density weight e^(−s/2), exactly as above.
The inverse-return determinant now has positive sign; one uniform parity
shift of the transverse exterior grading restores the required negative
prime contribution. Increasing dimension without this accounting would
change the coefficient. The extra directions are a proposed place to attach
connecting handles, not evidence that dimension itself helps RH.

The ambitious object is a connected, noncompact, locally finite exact
symplectic assembly of these tubes plus an archimedean end. It must preserve
the specified primitive orbits and supply an explicit transport complex on
the connecting region. Generic connecting dynamics creates extra primitive
orbits with mixed itineraries; periods log 2+log 3 cannot be silently counted
as prime powers. Either such orbits are absent, or their full graded
contributions must cancel by a geometric chain-level mechanism specified
before inspecting spectra. No such assembly or mechanism is supplied here.

The first independent construction test is just the p=2,p=3 assembly:
produce an exact contact connecting model, list every recurrent component,
and prove whether mixed-orbit contributions vanish for every repetition.
Success licenses work on locally finite assembly only; failure stops that
gluing mechanism. It does not test RH. Finite-dimensional handle existence
or a diagram is insufficient. This is a structural construction test, not
a zero-fitting experiment or a permitted numerical candidate screen.

## The complete conditional dependency, including the missing bridge

For either candidate the proposed chain is OPERATOR-BRIDGES → WEIL-FLOOR →
v1.36's RH implication. Every following obligation remains open:

1. Construct the global space, invariant bundle transport and an explicitly
   closed operator domain; control escape, all added orbits and all ends.
2. Establish the full distributional explicit-formula identity on the
   original admissible test class, including both time directions, the
   original gamma factor, poles, trivial-zero terms and regularization at
   zero. Match multiplicities and exclude unrecorded spectral terms.
3. Construct a positive geometric realization of the *complete* semilocal
   form. A precise sufficient specification is, for every a in a cofinal
   family and f in D(q_a)∩u_a^⊥ in the even sector and every f in the odd
   D(q_a), an identity q_a[f]=||B_a J_a f||²+E_a[f], with
   E_a[f]≥−C||f||² for one finite C independent of a and parity. Supply
   domains, source transfer, all exterior terms and cross terms. This is
   the unchanged floor obligation, not a newly proved estimate.
4. Verify the existing transfer from the actual even source complement to
   the full form and invoke v1.36 with its hypotheses intact. No positive
   spectral gap or decay rate is substituted for that theorem.

Step 3 is where arithmetic must do work beyond naming orbit lengths. NS47
already gives an exact signed Clifford lift; rewriting a supertrace as that
lift cannot establish the missing floor. Self-adjointness of a positive
subchannel also does not establish positivity of the complete signed form.

## Controls, scope and stopping decisions

The original positive Euler coefficients Λ(p^m)=log p and periods m log p
are the arithmetic input beyond the functional equation. Davenport–Heilbronn
and NS100/101 do not preserve this literal Euler/gamma package, so they are
not matched counterexamples to its full conditional realization. That is
not a passed screen. Generic local block creation, graded determinant
cancellation, reflection symmetry or exactness can be reproduced after
changing periods/weights: none may be claimed to distinguish zeta. NS94
already excludes its scoped symmetry-only inference. NS57 finite arithmetic
perturbations should additionally screen any eventual positivity mechanism
that ignores the exact repetition law. No new inequality or scan ran here.

Stop if the construction fits each repetition separately, discards a gamma,
pole or exterior term, equates a supertrace with a positive trace, or invokes
fixed damping to obtain a uniform undamping estimate contrary to NS47.
Exact Lagrangians need not be calibrated; calibration needs additional metric
and closed-form data. Capacity monotonicity needs a specified embedding and
capacity, and supplies no signed Weil estimate by itself.

Modern tools make the construction question meaningful, not settled:
[Faure–Tsujii's 2024 contact-flow analysis](https://arxiv.org/abs/2102.11196)
gives asymptotic resonance bands and, under isolation, concentration and a
Weyl law—not exact alignment of all resonances or prime realization.
[Kuipers–Hummel–Richter](https://arxiv.org/abs/1307.6055) match the oscillatory
prime contribution using quantum graphs while retaining a different smooth
density and spectrum. That is a direct warning to preserve the completion.

**Final wall classification: Same open gap.** The useful output is an
explicit arithmetic local model and a sharply specified global construction
problem. No admission pass, signed floor, G2 or RH result follows.

## Bounded peer review: arithmetic-geometry.md

**No MAJOR issue found; two MINOR clarifications requested.** This review
checked the source object's definitions and theorem scope, not all upstream
proofs or a future arithmetic transfer.

The elliptic quotient C*/p^Z=C/(2πiZ+log(p)Z) is genuine; multiplication by
p^k descends to the identity, while z↦z^n induces multiplication by n of
degree n². The simultaneous two-prime flow has no common positive period.
The note's real dimension four for a complex surface and Krull dimension
three for its integral model are correctly distinguished.

[Yuan–Zhang Theorem 1.3](https://arxiv.org/html/1304.3538v1) supplies the
stated nonpositive intersection under integrability, nefness, bigness and
generic-fiber orthogonality. The proposed P¹×P¹ is normal, geometrically
connected and projective; the metrized differences have trivial underlying
bundles. No stronger equality characterization was used.

**MINOR 1:** Fix the log-norm sign and normalization before describing an
exact metric transfer. One choice is
u_n,v=−log(||x₁||_(φ_n*L)/||x₁||_L), giving the displayed max ratio on the
x₁≠0 chart, with |p|_p=p^(-1) and the standard Q place weights. State that
finite real coefficients use continuity of the intersection quadratic form
from rational coefficients.

**MINOR 2:** Local valuation dependence is already visible from u_n,v.
The proposed test has independent content only if it asks whether that
information survives the actual intersection pairing and the quotient by
constant/base-pullback metric classes. Confirming that the input potentials
are nonzero would not settle this. These clarifications were sent to the
author; no edits were made in their file.

Separate spectral-lane cross-review found no correction in the oscillator
trace/domain, Suzuki ratio and shifted-pole implication, or passive local
Euler-port rejection. Primary-source abstracts were checked for the Suzuki
shift restriction and the stated CCM convergence limitations.

## Read-only batch-runner review

Reviewed `tools/geometry_swarm/checks.py` without running or editing it.
The inverse-return eigenvalues, exterior-power enumeration, determinant
sign, unstable half-density exponent and common grading shift match the
local model above. Rationalizing the actual repetition by twice the least
common denominator makes both the orbit weight and target rational. The
reported repetition is the resulting m, not the fixture's repetition index.
For the passive port, p=2, a=1/2, y=2 gives (1−2^(-3))/(1−2^(-2))=7/6.
The primitive-label examples correctly target an extra log 6 orbit, an
extra log 4 primitive coefficient at an existing prime-power period, and
duplicate primitive labels.

No mathematical MAJOR issue found in those calculations. Two implementation
clarifications were requested from the parent: replace floating `n**0.5`
in the bounded primality helper with integer `isqrt` to match the claimed
exact-arithmetic scope; and replace the unconditional `test_passed=True`
in primitive-support checks with explicit expected calibration outcomes
or a clearly weaker execution-only label. Neither issue changes the stated
four fixture outcomes, but the latter otherwise weakens the aggregate
consistency claim.

The planned 112 hyperbolic, 21 passive-port, 28 deck-map and four support
cases total 165 deterministic calibration fixtures. They are not 165
independent promising hypotheses or evidence for a global analytic trace.

**Resolution verified:** The parent replaced the primality helper with
`math.isqrt` and now checks each support fixture against explicit expected
candidate-condition and duplicate-label outcomes. Read-only inspection of
the corrected source and `exact-run-2/checks.json` confirms the four intended
support dispositions and 165 recorded `test_passed: true` entries. This was
inspection of the parent's corrected replay, not a separate rerun. Both
review findings are resolved for the stated calibration scope.
`local-batch-review.json` correctly preserves and distinguishes the weaker
pre-correction `exact-run-1` record. Global trace and RH limitations remain.
