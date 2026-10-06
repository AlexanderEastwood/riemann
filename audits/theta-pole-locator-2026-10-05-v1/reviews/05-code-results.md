# Review 05 — independent code and archived-result audit

Reviewed baseline `bc3ff0c962c485ac8104ce8cd832c119c260c871`, AGENTS, this
audit's BRIEF and PROPOSAL, `theta_eval.py`, `locator.py`, the complete
`controls.json` and the completed `original.json`. The parent recorded
preregistration commit `728cc6c` and pre-run code commit `0604699`.
The coordinator owns the full-register review. This is a code/result audit,
not a replay of historical proofs. Both missing-original recovery groups
remain OPEN. This agent made **no original theta evaluation or scan**.
The separate independent evaluator assessment belongs to review 04.

**Wall check: Distinct test.** Closest PR78/79. The specified question is
whether one bounded locator produces a candidate uncancelled original
denominator zero. Such a later certified pole would exclude the general
quotient-PD sufficient construction. The completed diagnostic supplies no
such candidate. Original Laguerre positivity remains the same open gap;
there is no new signed estimate, thaw, NS row or manuscript version.

## Implementation and formulas

The finite lattice recurrence starts with `q=exp(-pi*exp(2*u))` and advances
`q^(n^2)` by the ratio `q^(2*n+1)`. The coefficients are unchanged. With
`t=pi*exp(2*u)` the derivative is correctly

```text
phi'(u)=exp(u/2)*[-4*t^3*S6+15*t^2*S4-(15/2)*t*S2].
```

Negative real parts use complete-kernel evenness and odd derivative parity.
The two finite sums at the reflection seam need not match exactly, so the
numerical integrand is not itself an exact analytic replacement for phi.
The recorded lattice majorant accounts for this truncation discrepancy;
the code does not differentiate the reflection switch.

The common normalization
`B=exp(2*pi*exp(2*z)-9*z)/(4*pi^4)` is entire and nonzero. The code applies it
to both M and C, retains the minus sign in the second shifted derivative,
and includes `(B'/B)*m` with `B'/B=4*pi*exp(2*z)-9`. Errors in the normalized
derivative are charged both the M' error and this factor times the M error.
The product and derivative-product integrands are even in the integration
variable, so multiplication by two on the positive half-line is correct.

The geometric Gaussian tail ratio decreases with its index. The condition
`b*(N+1)^2>=13/4`, `b=pi*cos(2*abs(Im z))`, suffices for all displayed
omitted polynomial-exponential terms to take their largest real-part
majorant at zero. The envelope maxima use the maximum of
`t^alpha*exp(-d*t)` for `t>=1`, with `d=b/2`. Product truncation bounds
`2*L0*E0+E0^2` and `2*(L0*E1+L1*E0+E0*E1)` retain both cross terms.
The real-tail factors follow from
`max(abs(s+x),abs(s-x))=abs(s)+abs(x)>=abs(s)` and
`exp(2*(R+t))>=exp(2*R)*(1+2*t)`; the C tail retains its quadratic weight.
No algebraic omission was identified in these formulas.

These are analytic truncation majorants **evaluated in ordinary floating
arithmetic**, not interval enclosures. Neither quadrature error nor roundoff
is bounded. In the archived 171-call original run the largest reported
normalized M lattice majorant is about `4.5864e-223`, and the largest M
real-tail majorant about `2.3554e-604`, both at initial vertex `(8,8)`.
Small truncation estimates do not bound the omitted numerical errors or
turn 128/256-bit precision settings into that many accurate digits.

## Protocol compliance and controls

The code implements the frozen four-corner principal-phase ranking, its
explicit unresolved-corner fallback, and deterministic residual/index
tie-breaks. The selected cells alone are replayed; replay does not rerank or
enlarge the grid. Newton candidates are halved at most 16 times to remain
inside the same selected cell. There are at most 12 evaluated iterates per
cell and precision. The final endpoint is the last point actually evaluated:
the iteration-12 proposed update is not silently substituted for that point.

The two archived controls each contain 154 evaluations and reproduce the
same denominator root in cell `(2,2)`. The uncancelled control meets the
sampled-numerator gate. The removable control has the same stable
approximate denominator root but fails numerator separation and receives
the honest label `approximate_root_numerator_unresolved_no_pole_claim`.
This checks cancellation sensitivity for these controls, not universal
locator reliability and not original theta arithmetic.

Additional non-original checks by this reviewer:

- A zero remaining time budget stops before any evaluation, preserving an
  inconclusive result and zero call count.
- A synthetic exact-zero corner sets `winding_unresolved=True`.
- Every archived original refinement endpoint, M value and C value equals
  the final corresponding step record, and every step remains in its
  selected cell. Every step count respects the cap.

The budget guard acts before each evaluator call, so one running call may
finish after the clock expires. This is disclosed in review 02. The present
run finished far below the remaining allocation; there is no actual budget
overrun. The CLI received 4200 remaining seconds, and the original run took
approximately 48.46 seconds. The parent owns the earlier implementation and
control-time accounting.

## Actual original result

The completed archive contains exactly:

```text
81 initial grid evaluations
40 initial local evaluations (12,10,8,10)
10 unique replay-corner evaluations
40 replay local evaluations (12,10,8,10)
171 total; no recorded evaluator exception
```

All 64 sampled corner windings round to zero. Selected cells, in order, are
`(0,7)`, `(1,7)`, `(0,6)`, `(0,5)`. At both precisions every refinement stops
because its Newton proposal would leave its cell after the allowed
halvings. The 256-bit endpoint residuals relative to their corner scales
are approximately `0.03914`, `0.54809`, `0.49443`, and `0.64851`, far above
the required `2^-40`. All four endpoint comparisons meet the location
agreement test, but **agreement of stalled paths is not agreement of roots**.
No cell is marked promising for certification.

The strongest allowed conclusion is:

> This fixed diagnostic found no stable approximate original denominator
> root meeting its own residual gate. It is inconclusive and provides no
> original pole or zero-free certificate.

In particular, zero four-corner winding is not zero true winding: phase may
alias between sampled vertices even when the normalization is nonzero.
The locator refines only four cells, enforces cell containment, and can miss
zeros both inside the registered box and outside it. Stable nonzero C
samples along these non-root paths establish no uncancelled pole. Neither
the null result nor the independent precision replay proves zero-freeness,
positive definiteness, cancellation, or a sign for the original Laguerre
target.

## Disposition

**Accept the archived bounded diagnostic and its inconclusive label.** No
major code or record-consistency issue was identified for that scope.
Do not start the optional certificate stage: the prerequisite candidate is
absent. Stop this bounded test without extending the domain or moving to
an adjacent scan. Any future computation needs a separately specified
decision-changing input; this null archive does not supply one.

A genuine certificate would still require complete outward-rounded Arb
integrals/tails, verified boundary nonvanishing, a positive integer argument
count, and numerator exclusion on the certified root region, at two
precisions. Those requirements have not been met or attempted here.
