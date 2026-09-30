# Connected two-prime contact construction: structural review

2026-09-29. Reviewed baseline `eb4e180`, current AGENTS.md and PR69's
symplectic construction note. The parent reviewed all 104 registered nodes
and 14 continuation groups. This is an analytic construction audit of the
specified two-prime assembly obligation, not a numerical scan, new research
row, thaw, historical-proof revalidation or novelty claim.

**Wall check: Same open gap.** Closest: PR69's local assembly question and
OPERATOR-BRIDGES. The concrete change is a connected four-dimensional
ambient symplectic manifold with exactly two primitive closed Reeb orbits
and their assigned prime periods. The infinite-prime completion, original
archimedean/pole terms and signed positivity transfer remain absent.

## Disposition

The proposed model passes the stated connectedness, completeness, contact
and two-primitive-orbit checks. The complete recurrent and nonwandering
sets are precisely the two closed circles; the full compactly trapped set
is also their union. A crucial distinction is that the base connecting
trajectories do **not** lift to heteroclinic Reeb trajectories between the
two circles. The cotangent coordinate τ is conserved and has different
values on the circles.

Local unstable half-densities give the specified weight at each circle,
despite the stable/unstable exchange. A global smooth weighted transport
and its cutoff flat-trace distribution can be defined using a chosen
constant scalar cocycle. No global geometrically induced unstable line,
Fredholm realization or positive Weil transfer has thereby been proved.

## Hamiltonian, contact form and completeness

Let a=1/log2, c=1/log3, so a>c>0, and put

    b(x)=x(1−x)/(x²−x+1)=1/(x²−x+1)−1,
    v(x)=(a+c)/2+(a−c)cos(πx)/2.

On W=T*(S¹×R), with t modulo one, take

    λ=τdt+y dx,    ω=dλ,    H=v(x)τ+b(x)y,
    ι_(X_H)ω=−dH.

The equations are

    ṫ=v(x),    ẋ=b(x),    τ̇=0,
    ẏ=−v′(x)τ−b′(x)y.

Since v>0, H=1 is regular and has the global graph
τ=(1−b(x)y)/v(x). Hence Y={H=1} is connected and diffeomorphic to S¹×R²;
its ambient W has real dimension four and Y has real dimension three.
Fiberwise homogeneity gives λ(X_H)=H, so R=X_H|_Y is its Reeb field.
In graph coordinates,

    α=((1−by)/v)dt+y dx,
    α∧dα=(1/v)dt∧dy∧dx.

In particular the contact volume never vanishes.

The bound x²−x+1≥3/4 gives −1<b≤1/3; also c≤v≤a.
Thus the base vector field is complete. The derivatives b′ and v′ are
globally bounded. Along each base trajectory τ is constant and the y
equation is linear with bounded coefficients on every finite time interval,
so its solutions cannot blow up in finite time. The full Hamiltonian flow
and the restricted Reeb flow are complete in both time directions.

## Closed orbits, recurrence, trapping and connecting trajectories

The only zeros of b are 0 and 1. Off these levels x is strictly monotone:
decreasing on (−∞,0), increasing on (0,1), decreasing on (1,∞).
Consequently a closed or recurrent trajectory must have x=0 or x=1.
Here v′=0 and b′(0)=1, b′(1)=−1, so y evolves as e^(−s)y at x=0
and e^s y at x=1. Nonzero y is neither closed nor recurrent. The two
primitive closed circles are therefore

    γ₂: x=0, y=0, τ=log2,     period T₂=log2;
    γ₃: x=1, y=0, τ=log3,     period T₃=log3.

There is no primitive mixed orbit of period log6, and no other primitive
orbit. Repetitions of these circles remain present with periods m log p.

This also identifies the **nonwandering set**, not just periodic points.
Away from x=0,1, a sufficiently small x-interval has a uniform bound on
crossing time and cannot be revisited. Near x=j and y₀≠0, choose a small
neighborhood on which ẏ has the strict sign of −b′(j)y₀. While an orbit
remains in its x-interval, it crosses the y-band in one direction within a
uniform finite time. If it leaves the x-interval, scalar x-monotonicity
prevents a return. These points are wandering. Thus Ω(R)=γ₂∪γ₃.

For x≠0,1, energy conservation gives the useful exact trajectory relation

    y(x)=(1−τv(x))/b(x),    τ constant.

Base trajectories in (0,1) approach 0 backward and 1 forward. Bounded y
near 0 requires τ=log2; bounded y near 1 requires τ=log3. No trajectory
meets both requirements. For τ=log2, the lifted trajectory tends to γ₂
backward and y→+∞ as x→1 forward. For τ=log3, it has y→−∞ as x→0
backward and tends to γ₃ forward. All other τ escape in y at both ends.
Outside [0,1], x escapes to infinity in one time direction. At x=j with
y≠0, y escapes in one time direction. Therefore the maximal invariant set
of trajectories contained in a compact subset of Y for all time is exactly
γ₂∪γ₃. Neither homoclinic nor inter-circle heteroclinic trajectories occur.
Calling the base paths heteroclinic is appropriate; applying that description
to full Reeb paths joining the closed circles would be incorrect.

## Return-map hyperbolicity and local weight

At γ_p write β=b′(j)∈{1,−1}, d=v″(j)/v(j). The contact-transverse
linearization, in (δx,δy), is

    A_j = [[β,0], [−d,−β]].

The first variation of ṫ vanishes there because v′(j)=0. Hence the
Poincaré return derivative is exp(T_p A_j), with diagonal entries
e^(βT_p),e^(−βT_p) and possible lower shear −d sinh(T_p).
Its eigenvalues are p and p^(−1). Every repetition is nondegenerate.
The finite compact invariant set γ₂∪γ₃ is hyperbolic. This does not make
the entire noncompact contact manifold a compact Anosov system.

At γ₂ the unstable line has direction (1,−d/2), while its stable line
is vertical. At γ₃ the unstable line is vertical and the stable line has
direction (1,d/2). The inverse-return map on either circle has eigenvalues
p^(−m),p^m. Thus its alternating exterior numerator divided by the
absolute determinant is −1 for every m. Pullback on the *local unstable*
covector half-density gives p^(−m/2). The local orbit coefficient is exactly

    −(log p)p^(−m/2),    p∈{2,3}, m≥1.

The shear and exchange of the stable and unstable eigendirections do not
alter this coefficient. The calculation uses the nondegenerate-orbit local
formula with inverse-time convention, as in
[Dyatlov–Zworski §2.2 and Appendix B](https://math.berkeley.edu/~zworski/zeta.pdf).
It is a graded fixed-point contribution, not positivity of an ordinary
trace or the spectrum of a self-adjoint zeta operator.

## What global transport is, and is not, available

There is a global invariant vertical contact line span(∂y). It contracts
at γ₂ and expands at γ₃. Its covector half-density therefore has the
wrong exponent at γ₂ if used uniformly as an unstable density. This
particular global line is not the desired global unstable line.

The change of eigendirections alone does **not** prove that every global
invariant unstable splitting is impossible. In particular, there is no
actual heteroclinic Reeb trajectory connecting the circles on which to
assert a contradictory matching condition. No such global splitting has
been supplied or excluded by this audit. Local unstable lines over the
two-circle hyperbolic set are sufficient for the local weight calculation.

There is nevertheless an explicit, less intrinsic global construction.
Let Ω_h^k(Y) be horizontal forms, ι_Ru=0, and let φ_s be the complete
flow. On smooth compactly supported horizontal forms tensored with a
trivial scalar line, set

    U_s=e^(−s/2)φ_(−s)*,    generator −Lie_R−1/2.

Completeness makes this a well-defined smooth transport group on the stated
test domain. Choose a compactly supported spatial cutoff equal to one near
both circles and take time tests compactly supported in s>0. The cutoff
flat trace has no fixed-point contributions elsewhere and is

    Σ_(k=0)^2 (−1)^k tr_flat(cutoff U_s|Ω_h^k)
      = −Σ_(p=2,3)Σ_(m≥1)(log p)p^(−m/2)δ(s−m log p).

All repetitions are retained; the distribution is locally finite away
from zero. The scalar factor was chosen to reproduce the local half-density
holonomies. It is an assigned damping cocycle, not a demonstrated globally
natural unstable half-density. It does not supply a positive trace,
Fredholm domain, compact resolvent, gamma factor or signed Weil bound.

The separate spectral-lane audit straightens the flow on each open
x-strip. Its coordinates satisfy α=du+τdθ and R=∂u, with u running
over R. I independently checked that identity. This supports its scoped
conclusion that the ordinary contact-volume scalar L² model is translation
with continuous spectrum. It does not exclude every other weighted or
anisotropic realization.

## Remaining obligation and stop/continue decision

The connected two-prime local construction and absence of mixed periodic
support are now explicit. This clears that specific structural prerequisite.
The geometry also works after replacing the two prime periods by arbitrary
distinct positive periods: it has not discovered arithmetic rigidity.

A continuation needs a specified infinite-prime assembly and transport,
control at its noncompact ends and at time zero, the original archimedean
and pole completion, and an independent complete signed positivity transfer.
The present assigned scalar damping cannot be called that transfer. A
compact-Anosov theorem cannot be applied without its hypotheses, and the
local trace cannot be treated as an ordinary positive spectral trace.

**Final wall check: Same open gap.** One concrete finite assembly question
has a positive structural answer; OPERATOR-BRIDGES, WEIL-FLOOR, G2 and RH
remain open. No research-row or theorem-node change is justified by this audit.
