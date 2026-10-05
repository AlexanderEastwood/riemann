# Review 02: a local divergence/SOS estimate for the original nonlinear pair

Reviewed baseline: `5434d96f0034f842b0229f1d69dbbf3fb7fea270` (merged PR73), refreshed by the coordinator in this isolated worktree. I read the shared brief, current agent/proposal rules, conclusion-register scopes, ZERO-GEOMETRY demand, current checkpoints and evidence ledger, NS100/101 arguments, PR72's report and its two source/transfer notes, and PR73's version-2 report. The coordinator's full 104-node review is recorded in the brief. No historical proof or external certificate was replayed; both original-evidence recovery groups remain OPEN.

**Wall check: Same open gap.** Closest results: NS100/101 and PR72/73. The question here is whether a concrete local sum-of-squares certificate, after subtracting an exact total derivative, controls the complete mixed form for every finite set of translates and coefficients. The proposed certificate uses the original nonlinear logarithmic slope, rather than reflection symmetry. It fails analytically on the original theta tail. This is a stop for the specified certificate, not for the integrated target or every divergence/SOS method.

## 1. Exact question, domain and dependency

Use the complete original smooth even kernel `phi`, and set

```text
p(u) = phi'(u)/phi(u) = 2*P(2u),
p'(u) = 4*P1(2u),  P1=V(P),

C(t) = integral_R s^2*phi(s+t)*phi(s-t) ds.
```

Here `P` and `V` are exactly the rational state function and distinguished Jacobi vector field in the brief, including the specified initial data and the clock `L=2u`. The factor `d` is positive at finite real clocks. No finite theta prefix replaces `phi`.

The target is, for every integer `m>=1`, every `x_1,...,x_m` in `R`, and every `c` in `C^m`,

```text
Q = sum_(i,j) c_i*conj(c_j)*C((x_i-x_j)/2) >= 0.          (1)
```

This implies, and by the complete associated-kernel identity is equivalent to, `L1[X](r)>=0` for every real `r`. This is only the first Laguerre target, not RH or the all-order criterion. There are no source/parity restrictions on the coefficient vector in (1).

The estimating mechanism tested below is stronger than (1): make the integrand a nonnegative quadratic form after a specified exact integration by parts. Unlike another notation for (1), this gives a pointwise certificate that can fail while (1) remains true. It also exposes exactly where the original `P` and `V(P)` would have to establish a sign.

## 2. A coefficient-uniform certificate and its boundary conditions

For a real variable `y`, write

```text
u_i=y-x_i,   f_i(y)=phi(u_i),
w(u,v)=(u+v)^2/4,
D=partial_u+partial_v,
S(u,v)=p(u)+p(v).
```

The midpoint change of variables gives the exact entrywise identity

```text
C((x_i-x_j)/2) = integral_R f_i(y)*f_j(y)*w(u_i,u_j) dy. (2)
```

Let `h(u,v)` be a real symmetric differentiable function such that, for every fixed pair of shifts,

```text
phi(y-x_i)*phi(y-x_j)*h(y-x_i,y-x_j) -> 0
as y -> both infinities,
```

and with the resulting derivatives integrable. Define

```text
R_h(u,v) = w(u,v)-D h(u,v)-S(u,v)*h(u,v).               (3)
```

The derivative of `f_i*f_j*h` is exactly `f_i*f_j*(D h+S h)`. Therefore

```text
Q = integral_R sum_(i,j) c_i*conj(c_j)*f_i*f_j*
                    R_h(u_i,u_j) dy.                  (4)
```

**Sufficient estimating lemma.** If `R_h` is a positive-semidefinite kernel on `R x R`—all its finite matrices, with no restriction on their size or real nodes—then (4) proves (1). Indeed the positive diagonal factors `f_i` preserve positive semidefiniteness, and integration preserves the nonnegative quadratic form. This proof treats arbitrary complex coefficients and the complete tails. No finite minor check substitutes for its quantifier.

This lemma is generic calculus. The arithmetic obligation is to construct `h` for which (3) is positive semidefinite using `p=2P(2u)` on the original trajectory. Positivity of the displayed scalar entries would not suffice.

Even `h=0` already fails locally: at `u=1,v=2`, the matrix of `w` is

```text
[ 1    9/4 ]
[ 9/4  4   ],  determinant=-17/16.
```

For instance the real vector `(2,-1)` has quadratic value `-1`. The positive `phi` factors do not change inertia. This is an exact pointwise algebra check, not a negative value of the integrated form.

## 3. Strongest tested choice: cancel the actual nonlinear drift

A Gaussian gives a useful calibration. If `phi(u)=exp(-kappa*u^2/2)`, `kappa>0`, choose

```text
h_G(u,v)=-(u+v)/(4*kappa).
```

Then `S=-kappa*(u+v)` and (3) becomes the constant kernel `1/(2*kappa)`, which is positive semidefinite. Thus the mechanism is an actual all-coefficient proof in that case; its transfer is not circular.

For the original nonlinear orbit, the direct adaptive replacement is

```text
h_*(u,v) = w(u,v)/S(u,v).                              (5)
```

It cancels the drift term `S*h_*` exactly rather than comparing it with a constant Gaussian slope. With `s=(u+v)/2`, `t=(u-v)/2`, this is

```text
h_*(s+t,s-t) = s^2/[p(s+t)+p(s-t)].
```

For the global regularity discussion, assume explicitly `p'(t)<0` for every real t (pointwise negative logarithmic second derivative, stronger than the bare phrase strict log-concavity). Then the denominator vanishes only at `s=0`. There the quotient has the smooth removable behavior

```text
h_*(s+t,s-t) = s/[2*p'(t)]+O_t(s^3).
```

This conditional regularity statement does not use the un-replayed second-level certificates of the newer source. No global curvature theorem is needed for the rejection below. In any case, the failure below takes place at large positive diagonal arguments, where the quotient is defined directly from the complete theta asymptotic; it does not depend on a global strict-curvature premise.

For any fixed shift difference, `h_*` grows at most polynomially times `exp(-2*|s|)` at the ends. The complete double-exponential `phi` factors therefore make both boundary terms zero and every required derivative integrable. There is no cutoff or artificial boundary at either modular crossing.

The residual that would have to be positive semidefinite is explicitly

```text
R_*(u,v) = -D[w/S]
         = -(u+v)/S
           + ((u+v)^2/4)*(p'(u)+p'(v))/S^2.            (6)
```

Every entry of (6) uses the genuine six-state, two-clock evolution through `P(2u), P(2v), V(P)(2u), V(P)(2v)`. No extra moment-closure hypothesis has been introduced.

## 4. The original arithmetic tail rejects this certificate

A positive-semidefinite residual must at least have nonnegative diagonal entries. Formula (6) gives

```text
R_*(u,u) = -u/p(u) + u^2*p'(u)/(2*p(u)^2)
         = u*[u*P1(2u)-P(2u)]/[2*P(2u)^2].            (7)
```

The second equality checks both clock factors. In particular, for `u>0`, this certificate requires the concrete original-orbit inequality

```text
u*V(P)(2u) >= P(2u).                                  (8)
```

It is false at large `u`.

To see this without a scan, put `z=pi*exp(2u)`. From the complete original theta series on its positive half-line,

```text
phi(u) = 2*pi^2*exp(9u/2-z) *
         [1-3/(2z)+O(exp(-3z))].                      (9)
```

The `n>=2` terms give the last error. Gaussian summability and the gap from `n^2=1` to `n^2=4` justify differentiating its relative remainder; each fixed derivative introduces at most a polynomial in `z`. Consequently

```text
p(u)  = -2z + 9/2 + O(1/z),
p'(u) = -4z + O(1/z).
```

Substitution into (7) yields the controlled complete-kernel asymptotic

```text
R_*(u,u) = (u-u^2)/(2*pi*exp(2u))
           + O(u^2*exp(-4u)),  as u -> +infinity.       (10)
```

Thus `R_*(u,u)<0` for all sufficiently large `u`. No numerical threshold is asserted. The required positive-semidefinite kernel fails already its one-point condition. Multiplication by the strictly positive `phi(u)^2` cannot repair that failure.

Equation (9) is an asymptotic of the complete original sum with differentiated error control. It is not a reflected finite-prefix model of the Fourier transform, and does not use the invalid full-line termwise unfolding discussed in NS101. No small real-space remainder is promoted to a uniform-height Fourier error.

For comparison, keeping the fixed Gaussian `h_G` instead of (5) also fails: its diagonal residual is

```text
R_G(u,u)=u^2+1/(2*kappa)+u*p(u)/kappa,
```

which is eventually negative for every fixed `kappa>0`. The adaptive choice (5) removes this much larger drift mismatch, but its derivative still has the wrong diagonal sign in (10). Hence simply replacing the Gaussian constant by the actual local nonlinear slope does not make a certificate.

## 5. What remains missing, and what has not been excluded

The failed step is the specific implication from the original Jacobi evolution to the positive-semidefinite residual in (6). It is not merely unproved: (10) refutes it for that choice of `h`. Stop this local drift-cancellation ansatz.

This result does **not** refute (1). For a single translate, the integral of the locally negative residual in (4) is still `C(0)>0`; its other regions compensate. Nor does the result exclude every `h`: adding a correction changes both `D h` and `S h`. A successful correction would need an independently proved Gram representation or comparison for **all** residual matrices, or an explicitly nonlocal integrated comparison. Repairing a diagonal asymptotic, preserving a few derivatives, or verifying finitely many minors would leave that requirement open.

The exact vector field supplies all entries and derivatives in (6), but it supplies no known cone preserved across arbitrary translate combinations. The present attempt gives no lower bound for the remaining complete mixed form and no independent partial estimate with a positive transfer to `L1`. It should therefore be recorded as an analytic admission failure, not as an arithmetic advance.

## 6. Matched controls and disposition

- **NS100 original-slice control:** retained. This construction integrates the `s^2`-weighted pair and never assumes the excluded positivity of every cosine slice. The negative slice does not settle (1); the present ansatz has its own direct failure on the original orbit.
- **NS100 log-concave order-two model:** the generic integration-by-parts lemma also applies when its boundary hypotheses hold, but an all-matrix residual sign has not been proved for that model. Its recorded negative radial sign is not silently treated as a first-Laguerre counterexample. Gaussian success above is a calibration of the mechanism, not a claim that ordinary log-concavity is sufficient.
- **NS101 reciprocal mixture:** shares the generic identities (2)–(4), but fails the normalized original Jacobi equation by PR72's checked leading-exponential residual. Its off-axis zeros alone do not decide its first Laguerre sign. No transfer of the required positive-semidefinite residual to this model is claimed. The analogous double-exponential tail would also defeat the specific local quotient (5); that is a certificate failure, not an `L1` conclusion.
- **PR73 reflected prefix:** does not satisfy smooth modular matching or the original IVP, and is not used. Its fixed-prefix all-height exclusion remains intact. The calculation (9) keeps the complete original kernel and estimates only a real-coordinate tail needed to reject (6).
- **PR72 constant-matrix closure:** not attempted; (6) keeps variable nonlinear state functions. Its failure is independent of that finite constant-matrix restriction.
- **Davenport–Heilbronn:** different original coefficients, conductor and completion, hence not an instance of the specified Jacobi IVP. No control pass or first-Laguerre failure is inferred for it here.
- **NS74/83:** NB coefficient/rate controls, with different targets and domains; not direct controls on (1).

**Success consequence, had the residual been positive semidefinite:** equations (2)–(4) would have proved the complete first Laguerre inequality at every real height, with no extra unproved transfer. **Actual failure consequence:** reject only `h=w/(p(u)+p(v))` and its fixed Gaussian predecessor as pointwise PSD certificates. The original complete comparison remains open.

**Bounded next budget:** no scan, certificate replay or enlargement follows from this failure. A later continuation would first need one explicit corrected or nonlocal certificate with an analytic all-coefficient estimating mechanism; at most one bounded paper-admission session should assess such a supplied candidate before any computation. This note supplies no such replacement candidate and does not recommend trying nearby variations automatically.

No numerical or symbolic scan, row claim, manuscript change, commit, push or outreach. Only this assigned internal note was written; other agents' files were preserved.

**Final wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR72/73.** The tested local nonlinear certificate fails; the complete first Laguerre inequality, RH, G2 and the cofinal signed-arithmetic lower bound remain open.
