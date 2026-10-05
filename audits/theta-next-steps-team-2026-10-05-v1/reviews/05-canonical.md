# Reviewer 05 — canonical systems and phase: no independent candidate admitted

**Recommendation: stop this lane within the proposed 1–4 hour next-step budget.**
The explicit phase construction below returns exactly the target. Promoting
it to a positive canonical system requires a stronger, unproved global
condition. I found no specified arithmetic construction that makes either
condition easier. This is a scoped feasibility decision, not a theorem
excluding canonical-system methods.

**Wall check: Same open gap — ZERO-GEOMETRY and OPERATOR-BRIDGES.**
Closest results: NS100/101, PR76, and the existing shifted/unshifted
de Branges comparison. What changes: no independent arithmetic input.
The audit question is whether a phase or Hamiltonian supplies positivity
without assuming the target or real zeros. The answer for the concrete
constructions assessed here is no.

Reviewed remote baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34`;
local explanatory commits are additional scope records. Read AGENTS's
proposal/relevance gates, current README/checkpoints and NEXT_STEPS,
the two named continuation scopes, COMPARISON's de Branges discussion,
the September 29 spectral-geometry assessment, PR76's complete derivation,
and MISSING. The coordinator records the complete-register review and
remote refresh. No historical proof replay; both original-recovery groups
remain OPEN. No scan, certificate, research row, thaw or manuscript version.

## The actual phase construction

Keep the complete original theta function and put

```
p(r)=r²+1/4,  X=pY/4=xi(1/2+ir)/2,
J=p²(Y'²-YY'')+2(r²-1/4)Y²=16(X'²-XX'').
```

For any **fixed** epsilon>0 define the entire function
`E_epsilon(z)=X(z)+i*epsilon*X'(z)`. On a real interval where
`E_epsilon` is nonzero, write `E_epsilon=|E_epsilon| exp(-i*theta)`.
Then the explicit phase derivative is

```
theta'(r)=epsilon*(X'²-XX'')/(X²+epsilon² X'²)
         =epsilon*J(r)/(16*(X²+epsilon² X'²)).
```

Thus phase monotonicity is the missing first-Laguerre sign, with a positive
denominator. Epsilon changes its weight, not its sign. At a common real
zero of X and X', the phase formula is undefined; the undivided polynomial
identity for J still applies. Multiple zeros must not be silently excluded.
No original Jacobi coefficient or IVP estimate occurs in this conversion.

The corresponding formal real-axis kernel is

```
K_epsilon(r,s)=epsilon*[X(r)X'(s)-X'(r)X(s)]/[pi*(r-s)],
K_epsilon(r,r)=epsilon*J(r)/(16*pi).
```

Naming this a reproducing kernel does not establish its positivity. Its
diagonal sign is already the requested estimate; a positive de Branges
kernel would require additional global compatibility. The first Laguerre
inequality alone is not an RH criterion.

## What a genuine positive realization would require

With `A=X`, `B=-epsilon*X'`, the relevant meromorphic quotient is
`m=B/A=-epsilon*X'/X`. If m is analytic in the upper half-plane with
nonnegative imaginary part, then away from zeros of A

```
|E_epsilon|²-|E_epsilon^sharp|²=4*|X|²*Im(m).
```

This is a global Hermite–Biehler/Herglotz condition, not the real-axis
slope inequality. Every zero of X creates a nonremovable logarithmic-
derivative pole with its multiplicity. Upper-half-plane analyticity of m,
together with real symmetry, therefore already excludes all nonreal zeros
of X. It imports an RH-strength input.

An independent canonical construction would have to specify a spectral-
parameter-independent Hamiltonian H(t), its interval, local integrability
and positive semidefiniteness, initial and endpoint conditions, and the
exact endpoint identity with `(X,-epsilon*X')` after a fixed normalization.
Singular endpoints require justified limits; invoking a self-adjoint
spectrum additionally requires its closed domain. None of those missing
arithmetic identifications is supplied by choosing an arbitrary positive
matrix H. A realization of another entire function does not transfer.

Y cannot be substituted as an entire endpoint function: it has actual
poles at ±i/2. On its nonzero locus the correct quotient is

```
-X'/X = -Y'/Y - p'/p.
```

The last term cancels the primitive's artificial logarithmic-derivative
poles. Differentiating on the real axis recovers `J/(p²Y²)`, including the
polynomial correction. Dropping that term changes the problem.

## Existing shifted constructions do not fill this gap

[Suzuki, arXiv:1204.1827v2](https://arxiv.org/html/1204.1827v2),
§1.1, states the entire-function Hermite–Biehler hypothesis and its real-zero
consequence. Proposition 1.2 equates zero-freeness in
`Re(s)>1/2+omega_0` with innerness of
`xi(1/2-omega-iz)/xi(1/2+omega-iz)` for **every** `omega>omega_0`.
Theorem 2.3 constructs the stated canonical system for `omega>1`;
§1.2 records unconditional innerness for `omega>=1/2`.
Neither range approaches zero shift. These precise source scopes were
checked; no extension to small shifts is assumed.

Separately, COMPARISON's fixed-window construction permits a spectral shift
strictly below the bottom. Its positive shifted space does not determine
the unshifted bottom's sign. Positive local extensions also require an
independent identification with the prescribed global arithmetic function.
These are separate missing bridges, not an impossibility result.

## Controls and decision

The NS101 translated-mixture family retains every generic phase/kernel
identity above and PR76's positive primitive, envelope and unit tail, yet
has negative J in the previously proved parameter range. It therefore
rejects a sign argument using only those properties. It changes the
single-lattice coefficients and original Jacobi IVP, so it does not exclude
an independently derived arithmetic Hamiltonian. Davenport–Heilbronn is
only a symmetry control here; its different arithmetic is not treated as
a matched original-theta control. No new control computation is warranted.

**No-candidate stop:** do not allocate another 1–4 hours to phase plots,
positive-metric choices, or recreating the shifted system. A future proposal
would change this decision only by supplying a concrete original-arithmetic
coupling and endpoint identity with independently justified positivity.
Success at that admission gate would justify examining that specified
construction, not establish J or RH automatically. Failure leaves this
lane stopped; it does not justify an adjacent parameter variation.

**Final wall check: Same open gap.** The signed theta estimate, the separate
operator bridges, RH, G2 and the cofinal signed-arithmetic lower bound remain
open.
