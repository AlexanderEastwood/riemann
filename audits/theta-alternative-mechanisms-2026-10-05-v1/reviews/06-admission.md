# Review 06 — admission decision and a scoped quotient falsification test

**Decision: stop the three proposed sign estimators; retain a potentially
admissible bounded diagnostic for the quotient, subject to its own completed
proposal and controls.** No computation is authorized or performed by this
review. A conjecture does not need a proof before admission. Here the problem
is that heat and contour formulas supply no estimating technique, while the
specified duplication cone is false. The quotient pole implication does,
however, supply a complete rejection decision that an experiment could test.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–78.**
No original all-height signed estimate is obtained. The conditional pole
obstruction is useful route assessment, not a positivity estimate. A future
fixed-domain pole diagnostic could be classified **Distinct test** against
PR78: it tests general positive definiteness of `k=C/M`, rather than the
already rejected positive sech-power mixture. It would not test RH.

Reviewed baseline `221ceec9da825bdc787111447badad961860760a`, scope commit
`b5147e82803cccdb641bcb611b3c90c3c76cf51e`; AGENTS, BRIEF/review record,
reviews 01–04, PR78 conclusions and the proposal template. The coordinator
owns the full-register refresh. This is an admission/dependency audit, not
historical proof replay. Both original-evidence recovery groups remain OPEN.

## 1. Decisions on the three mechanisms

**Heat: stop this formulation.** The complete identity

```text
Q_0 = G_A*Q_A - 2*integral_0^A G_a*S_a da,
Q_a=L1[H_a], S_a=L1[H_a'], A=1/8
```

has the correct adverse source and literature scaling. A coefficient-level
upper estimate for the accumulated source could qualify as an unproved
candidate. None is supplied; its comparison with `G_A*Q_A` merely restates
`Q_0>=0`. The shortcut `S_a<=0` fails at zero height, and a bounded
`S_a/Q_a` comparison imports restrictions near possible multiple zeros.
This auxiliary Gaussian clock is not the original nonlinear Jacobi clock.
No claim that the latter route has been excluded follows.

**Duplication: reject the unrestricted sector cone; defer an unspecified
nonlinear alternative.** The exact original sectors satisfy
`v=A(r)*X(r)`. Their full Hermitian Laguerre matrix is congruent to a fixed
matrix with inertia `(2 positive, 1 negative)` whenever `X!=0`. Its
all-sector positivity is false for the original data. Subtracting the known
phase contribution leaves `L1[X]*A*A^*`, which is exactly the scalar target.
Nonlinear or infinite refinement would need an actual invariant signed
inequality and a complete derivative-controlling limit. No such proposal
is present. Negative sector inertia is not negative original `L1[X]`.

**Contour positivity: stop this formulation.** Moving the complete quotient
integral to an interior horizontal line exposes every residue and a signed
boundary density. A pole-free strip, an absolute tail bound, or a contour
identity alone estimates no lower sign. Requiring the shifted integral to
have the desired sign in a pole-free strip is equivalent to requiring the
original Fourier sign. There is no independent arithmetic estimator here.

## 2. The pole implication has a complete, narrower decision edge

Retain the original completed theta kernel and complete real-s integrals:

```text
M(z)=integral phi(s+z)*phi(s-z) ds,
C(z)=integral s^2*phi(s+z)*phi(s-z) ds,
k=C/M, K(xi)=integral_R k(t)*exp(i*xi*t) dt.
```

Review 03's strip argument gives holomorphic M/C on `abs(Im z)<pi/4`,
positive M on both coordinate axes, finitely many zeros on closed
substrips, and integrable horizontal quotient lines avoiding poles.
The complex saddle estimates and the complete tails are material premises;
a finite theta prefix cannot replace them.

An uncancelled denominator zero in that strip gives an upper-half-plane
pole by symmetry. The lowest upper pole height has finitely many poles;
none lies on the imaginary axis. Shifting above that height gives the
leading Fourier contribution

```text
exp(-b*xi)*xi^(m-1)*T(xi),
```

where T is a nonzero real trigonometric polynomial with no constant term.
Its positive and negative values recur away from zero; the smaller
polynomial and exponential terms do not remove both signs. Thus

```text
original M zero with C nonzero, abs(Im z)<pi/4
  => K changes sign => k is not positive definite.
```

This is not a claim that such a zero exists. Nor does it contradict the
original target: `K>=0` is sufficient, not necessary, in

```text
L1[X](r)=(1/pi)*integral X(r-xi/2)^2*K(xi) dxi.
```

A signed K can still produce nonnegative convolution. Success in finding
an uncancelled pole would close the **general quotient-PD sufficient
construction**, a stronger rejection than PR78's mixture failure. Failure
to find one in a bounded region would leave that construction undecided.

## 3. Certificate readiness differs from diagnostic admissibility

No actual candidate rectangle is supplied. Therefore immediate original
zero certification is not ready. But AGENTS does **not** require somebody
to supply a zero before an experiment: that would confuse discovery with
verification. A separately pre-registered bounded locator can satisfy the
gate because the rejection implication above is complete and useful.
An externally supplied rectangle is one option, not a repository rule.

A concrete possible diagnostic scope, for the coordinator to accept or
revise before computation, is the single rational rectangle

```text
1/8 <= Re z <= 2,   1/8 <= Im z <= 5/8.
```

It stays away from the known zero-free coordinate axes and the strip edge,
where the displayed theta series ceases to converge. This is a tractability
choice, not a prediction that a root lies there or a coverage theorem.
Pre-register at most a 9-by-9 evaluation grid, refinement of at most four
cells selected by a stated winding/residual rule, and at most 12 local
refinement steps per cell. No enlarged region or adjacent second scan is
implied by a null result. Initial 128-bit calculations and 256-bit replay
can be diagnostic only; retain original theta coefficients, complete
integral/tail error treatment and cutoff replay. Floating winding estimates
or apparent roots are not certificates.

A subsequent certificate must enclose a specific compact rectangle wholly
inside the strip, prove M nonzero on its entire boundary, and rigorously
enclose `integral_boundary M'/M /(2*pi*i)` around a positive integer.
Prove C nonzero throughout that rectangle, or otherwise rigorously
separate the particular M zero from C zeros. Enclose both lattice and
real-integration tails uniformly on the complex domain. Use Arb interval
arithmetic, two working precisions, no midpoint solves, and explicit
quadrature/subdivision errors. No simplicity assumption is necessary.
An inconclusive C enclosure is not evidence of cancellation.

## 4. Matched controls and budget

Before any original locator, validate the actual pole/cancellation pipeline
on two exact synthetic controls:

```text
M_0(z)=z^4+1, C_0(z)=1,
K_0(xi)=pi/sqrt(2)*exp(-abs(xi)/sqrt(2))
        *[cos(abs(xi)/sqrt(2))+sin(abs(xi)/sqrt(2))].
```

The toy box `7/10 <= Re z, Im z <= 18/25` encloses its upper-right
pole and lies inside the strip. This quotient has a changing Fourier sign.
It shares contour calculus and axis nonvanishing, not theta arithmetic.
For the removable-pole control take `C_1=M_0*exp(-z^2)`. Then
`k_1=exp(-z^2)` has positive Fourier density. A denominator-zero-only
rejection must fail this control. Neither toy supplies original evidence.

NS101 shares quotient/convolution algebra and strip regularity, but changes
the original lattice/IVP. Its known negative Laguerre value forces its own
quotient to fail PD; it does not prove that poles cause that failure.
Do not require a pole locator to find one there without a separate witness.
NS100's per-slice obstruction is not this complete quotient assertion.
Davenport–Heilbronn changes coefficients, gamma factor and completion;
its own complex strip/tails need checking before transplanting this
algorithm. The unchanged `controls/example_screen.py` tests a different
derivative expression and cannot screen this proposal. Record these
mismatches explicitly. NS74/83 constrain NB loads/rates and are inapplicable
to this theta quotient; no NB gain claim is being made.

Current budget: one paper review, zero scans/certificates. A possible later
locator budget is 90 minutes including control implementation, with the
fixed evaluation caps above and artifacts under `evidence/diag_*`. A
promising box would require a separately scoped certificate budget, capped
at two hours initially. Exhaustion or no witness means **inconclusive and
stop**, not PD, not a positive target estimate, and not an automatic wider
search. No row, thaw or manuscript version follows from this review.

**Final disposition:** stop heat, reject the stated sector cone, stop the
unestimated contour positivity claim; retain a potentially admissible
bounded quotient-falsification diagnostic for explicit preregistration.
The original first-Laguerre inequality, RH, G2 and cofinal arithmetic bounds
remain open. **Final wall check: Same open gap.**
