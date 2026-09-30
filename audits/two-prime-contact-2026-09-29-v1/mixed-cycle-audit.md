# Connectedness and mixed cycles: two-prime construction audit

2026-09-29. Read the PR69 geometric-swarm contact specification, its README/next-decision text, and the current route scope in the isolated checkout (`eb4e1809178cb583575ea1f1bf2e0bf51c27b8e8` at this read). This note owns only the formal mixing audit and correction of that earlier framing; the parent separately constructs and checks the contact model. No numerical scan, global contact-flow trace theorem, research row or arithmetic estimate is claimed.

**Wall check: Same open gap.** Closest: PR69's connected contact assembly specification, OPERATOR-BRIDGES/WEIL-FLOOR. What changes: distinguish topological connectedness from recurrent two-way symbolic communication, and test a specified model rather than unspecified “generic” gluing. Success can settle a local assembly requirement; it cannot supply global completion or positivity transfer.

## 1. The exact scalar model

Work first in formal power series in independent commuting variables X,Y, with fixed scalar u,v. Attach each state's roof to its outgoing transitions:

    M(X,Y) = [[X, uX],
              [vY, Y]].

The determinant and independent reference are

    D = det(I−M) = (1−X)(1−Y) − uvXY,
    D₀ = (1−X)(1−Y),
    Z = 1/D,                  Z₀ = 1/D₀.

All determinants have constant term one, fixing the formal logarithm. Therefore

    log Z − log Z₀
      = −log[1−uvXY/((1−X)(1−Y))]
      = Σ_(k≥1) (uv)^k/k · X^kY^k/[(1−X)^k(1−Y)^k].

In particular,

    [XY](log Z−log Z₀) = uv.

For a,b≥1 the complete mixed coefficient is

    [X^aY^b](log Z−log Z₀)
      = Σ_(k=1)^min(a,b) ((uv)^k/k)
          binom(a−1,k−1) binom(b−1,k−1).

**Exact scalar conclusion:** `Z=Z₀` as formal series if and only if `uv=0`. If u,v are nonnegative and both are positive, every displayed mixed coefficient is strictly positive. Thus nonnegative bidirectional communication cannot preserve the independent two-factor Euler product in this model. No cancellation can remove even its first mixed term. For signed scalar couplings the same exact factorization condition follows from the XY coefficient; this is not a statement about graded or matrix-valued couplings.

If u=0 or v=0, M is triangular and its determinant is exactly D₀. A one-way transition can occur without a mixed **closed** itinerary. The model can have connected underlying undirected graph while preserving the independent determinant. Connectivity and recurrent mixing are already distinct at this elementary level.

## 2. What produces log(6), and what does not

Set `X=exp(−sT₂)`, `Y=exp(−sT₃)` with `T₂=log 2`, `T₃=log 3`. The shortest mixed closed word uses one transition in each direction and has roof sum `T₂+T₃=log 6`. The two choices of starting point are canceled by the factor 1/2 in the `tr(M²)/2` expansion, leaving uv as its coefficient in log Z. Consequently its additional contribution to the logarithmic-derivative distribution is

    −∂s(log Z−log Z₀) = uv·log(6)·6^(−s) + higher mixed terms.

The independent prime-power logarithmic derivative has no such primitive contribution. With the centered negative-sign convention used for the contact Weil term, the sign and half-weight change together; the unwanted support does not disappear. The formal identities also hold analytically sufficiently far to the right, where the matrix logarithm series converges, with the branch tending to zero as Re s tends to infinity.

A real connecting region need not have these roofs. If traversal introduces additional travel time, even an existing mixed orbit generally has a different period. An actual contact-flow conclusion requires a return map, allowed itineraries, roof function, and a theorem relating them to closed orbits. None follows from connectedness. Likewise, no topology or probability model defining “generic connecting dynamics” was supplied in PR69. Its sentence asserting generic mixed itineraries should be read as a warning about an architecture, not a proved genericity statement or a guarantee of an orbit exactly at log 6.

The scalar nonnegative screen does not exclude graded cancellations, matrix-valued holonomy, excluded itineraries, nonrecurrent connections, or a different trace operation. Each changes a hypothesis and needs its own construction. A negative coefficient, considered alone, is not such a construction.

## 3. Why connected contact geometry can avoid mixing

For the parent's proposed base field

    V = v(x)∂t + b(x)∂x

on a cylinder, suppose b has exactly the simple zeros 0 and 1, with fixed nonzero sign on every component of their complement. Every trajectory with nonconstant x is strictly monotone in x. It cannot be periodic, and uniqueness prevents crossing an equilibrium x-value in finite time. Thus any periodic base orbit lies on x=0 or x=1. With t of period one, prescribing `v(0)=1/log2` and `v(1)=1/log3` gives the desired base periods.

The cotangent lift projects to this base flow. Hence a periodic lifted orbit must also project to a constant-x base orbit. Checking the fiber equations can establish which periodic lifts actually exist; monotonicity alone does not count them or their trace weights. Once that check is completed, connectedness of the contact energy hypersurface is fully compatible with two prescribed periodic components and no mixed return. A trajectory traveling toward another invariant component is not a periodic orbit visiting both. This escape from the scalar obstruction removes recurrent bidirectional communication rather than canceling its weights.

The same reasoning works with arbitrary positive assigned periods. Calling them log2 and log3 is arithmetic input supplied to the geometry, not a property that distinguishes primes. Additional prime labels, original archimedean/pole data, the global trace/domain, and the eventual signed estimate remain separate obligations.

## 4. Forward correction and next decision

Preserve PR69 and correct its broad framing forward: **a connected assembly need not create mixed primitives; a recurrent bidirectional scalar transition architecture with positive weights creates mixed contributions under the specified roof model.** The earlier request to list recurrent components was sound. Treating mere connectedness as the decisive obstruction was too weakly specified.

If the parent's monotone contact construction verifies the two orbits and original local weights, that completes this two-prime no-mixed-return prerequisite. The next task is then a specific global transport/completion question, with all analytic limits and arithmetic terms retained. It is not another attempt to eliminate log6 merely because the space is connected.

**Final wall: Same open gap.** The formal mixing obstruction is scoped exactly; connectedness is not an RH wall. No global spectral or positivity transfer follows from avoiding mixed cycles.
