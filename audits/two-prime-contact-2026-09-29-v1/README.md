# Two-prime connected contact construction: outcome and scope

2026-09-29, v1. **Structural construction and interpretation audit of PR69's next-step recommendation.** Reviewed base: `eb4e1809178cb583575ea1f1bf2e0bf51c27b8e8`. All 104 conclusion records and 14 continuation inputs, current instructions/status/freeze board, missing-original ledger and relevant PR69 notes were reviewed. This is not a new audit or replay of every historical proof. Both historical original-evidence recovery groups remain OPEN.

**Wall check: Same open gap.** Closest: PR69's contact assembly and OPERATOR-BRIDGES, with NS47/94/100/101 scopes preserved. A finite connected geometry can be constructed without mixed periodic orbits. It does not supply the closed completed weighted spectral realization or the actual cofinal arithmetic estimate. No research row or thaw is claimed. The [pre-verification plan](plan.json) states the interpretation question and generic-period control.

## 1. A connected four-dimensional construction

Let t have period one, let x∈R, and write

    T0=log 2, T1=log 3, a=1/T0, c=1/T1,
    b(x)=x(1−x)/(x²−x+1),
    v(x)=(a+c)/2+(a−c)cos(πx)/2.

On the connected exact symplectic four-manifold

    W=T*(S¹×R), λ=τdt+y dx, ω=dλ,
    H=v(x)τ+b(x)y,

use ι_X ω=−dH. The Hamiltonian is linear in the fiber variables, so λ(X)=H. The energy surface Y={H=1} is the global graph

    τ=A(x,y)=(1−b(x)y)/v(x),
    α=A dt+y dx,
    R=v∂t+b∂x−[v′A+b′y]∂y.

Because v is between the positive numbers a and c, Y is a connected smooth three-manifold, diffeomorphic to S¹×R². Direct calculation gives

    α(R)=1, ι_R dα=0,
    α∧dα=(1/v)dt∧dy∧dx.

The base coefficients and their first derivatives are bounded, and the fiber equation is linear with bounded coefficients along each base trajectory. Thus the flow exists for every real time. This is a noncompact model; no compactness or Anosov theorem is imported.

The only zeros of b are 0 and 1. Every other x trajectory is strictly monotone and cannot be periodic. At those two roots, v′=0 and b′=+1,−1 respectively, so periodicity in the y equation forces y=0. There are exactly two primitive closed orbits, with periods T0,T1 and conserved momenta τ=T0,T1. The transverse infinitesimal matrices have eigenvalues ±1; the return maps, including their shear, have eigenvalues p,p⁻¹ for p=2,3. There is no mixed closed orbit at log6 or any other period.

Full recurrence and the local return calculation are reviewed in [construction-review.md](construction-review.md). The construction works equally for arbitrary distinct positive assigned periods: primality is not used to make the space or exclude mixed returns. It encodes the selected arithmetic labels rather than deriving them.

## 2. What the connection does not do

The coordinate τ is conserved because H is independent of t. The two periodic circles have different τ values, so **no full lifted trajectory connects them asymptotically in both time directions**. Base trajectories between x=0 and x=1 do connect the two base circles, but their cotangent lifts satisfy

    y=(1−τv(x))/b(x).

For fixed τ, a bounded limit at x=0 requires τ=T0; a bounded limit at x=1 requires τ=T1. Those cannot both hold. Every such lift escapes to fiber infinity at at least one end. Topological connectedness has not supplied interaction between the two trapped orbit components.

The globally invariant vertical contact line is stable at the first orbit and unstable at the second. It cannot simply be called one common unstable line. Each orbit has a local unstable half-density producing the desired p^(−m/2); existence or nonexistence of a suitable global unstable splitting is not settled by that switch alone.

There is nevertheless a global **assigned** smooth transport on compactly supported horizontal forms:

    U_s=e^(−s/2) φ_(−s)*,  ι_R u=0.

It preserves C_c^∞ and has generator −Lie_R−1/2. With a compact spatial cutoff equal to one near both closed circles and time tests compactly supported away from zero, its alternating local flat trace is

    −Σ_(p=2,3) Σ_(m≥1) (log p)p^(−m/2) δ(s−m log p).

The uniform damping is a chosen scalar cocycle, not a demonstrated globally induced unstable half-density. This smooth transport and cutoff distribution do not provide a Fredholm realization, positive Hilbert trace or the complete Weil identity. The finite two-prime Laplace series can itself be continued meromorphically; that elementary continuation does not construct the missing operator theory.

## 3. The natural scalar spectrum is exactly the wrong kind

On each of the three open strips x<0, 0<x<1, x>1, set

    u=log|x/(1−x)|−x,         du/dx=1/b,
    θ=t−F(x) mod1,           F′=v/b,
    τ=(1−by)/v.

The map x↦u covers R on each strip. Direct substitution yields the exact contact normal form

    α=du+τdθ,    R=∂u,
    |α∧dα|=dθ dτ du.

The two excluded planes have contact-volume measure zero. The entire scalar L² model is therefore the direct sum of three translation channels

    L²(S¹×R_τ×R_u, dθ dτ du).

Its Koopman generator D=−i∂u, on the vector-valued H¹ domain in u, has purely absolutely continuous spectrum R and no eigenvalues. This is an exact characterization of **this scalar contact-volume realization**, not a no-go for every weighted, anisotropic or resonant realization. Periodic orbit distributions and ordinary Hilbert traces are different operations.

See [transfer-audit.md](transfer-audit.md) for the complete unitary/domain argument and the remaining conditional edge to WEIL-FLOOR. No prime-zero spectrum, gamma/pole completion, source/parity transfer or cofinal signed bound follows.

## 4. Correcting the earlier mixed-orbit warning

In the precisely specified scalar two-state model

    M=[[X,uX],[vY,Y]],
    det(I−M)=(1−X)(1−Y)−uvXY,

the independent Euler factors are preserved exactly iff uv=0. A one-way connection is triangular and preserves the determinant. Bidirectional positive scalar coupling introduces a nonzero mixed XY term; with additive roofs log2 and log3 its shortest mixed period is log6. Actual geometric transit times can change that period. Neither recurrence nor an additive roof follows from connectedness.

[The mixing audit](mixed-cycle-audit.md) gives all mixed coefficients and distinguishes scalar positive coupling from graded or matrix cancellation. PR69's unspecified “generic connecting dynamics” was an architecture warning, not a genericity theorem. Its connectedness prerequisite was too weak to establish arithmetic interaction. This forward clarification preserves the earlier record.

## 5. Verification, sources, and decision

[check.mac](check.mac) and [its clean-start saved output](check-clean-output.txt) verify 25 exact algebraic identities in Maxima 5.50.0: contact/Reeb equations, conserved momentum, local characteristic polynomials, the straightening Jacobian and the scalar mixing determinant. They do not independently prove completeness, classify every recurrent orbit, or establish the spectral theorem; those arguments are supplied in the notes. This is symbolic verification, not a numerical RH certificate. No GPU generation or larger parameter scan was run. The first run loaded the existing user initialization before `kill(all)`; [that output](check-output.txt) is preserved. After review identified this provenance limitation, the same 25 identities were replayed successfully with `--no-init --quit-on-error`; the clean-start output is authoritative.

Reproduce from the repository root:

```sh
maxima --no-init --quit-on-error --very-quiet --batch=audits/two-prime-contact-2026-09-29-v1/check.mac
```

The only external theorem used for the cutoff orbit-distribution interpretation is the standard local nondegenerate flat-trace calculation: [Dyatlov–Zworski, §2.2 and Appendix B](https://math.berkeley.edu/~zworski/zeta.pdf). Their global theorem assumes a compact Anosov flow; those hypotheses do not hold here. The coordinate, recurrence and scalar-spectrum arguments above are explicit for this model. No literature novelty claim is made.

Davenport–Heilbronn and NS100/101 are not matched instances of this finite prescribed contact object, and no generic completed-function positivity implication is tested. This is **not** a control pass. The applicable control is stronger for this interpretation question: arbitrary positive periods yield the same geometry. NS47 is retained as a constraint on any eventual ordinary-L²-closable positive comparison with a bounded remainder; it is not invoked to exclude all alternative realizations.

**Stop/continuation decision:** Do not spend another round on mere connectedness or larger prime lists in this model. The finite no-mixed-return construction succeeds, while the natural scalar spectral interpretation fails exactly. A next research candidate must supply a specific completed weighted realization and its arithmetic transfer; a smooth transport or finite Euler product alone does not meet that requirement. All freeze conditions, 104 node records and 14 continuation demands remain unchanged. No new row, manuscript version, new RH estimate or general geometric closure.

**Final wall: Same open gap.** One geometric prerequisite is resolved, and the precise scalar realization is inadequate. The global arithmetic bridge remains open.
