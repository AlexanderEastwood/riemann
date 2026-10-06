# Independent review 03: pole implication and bounded locator protocol

**Decision: GO for the bounded diagnostic after its deterministic protocol
and matched controls pass; NOT READY for an original zero certificate.**
This is a route-validation experiment, not an all-height lower bound.
There is no requirement to know a zero before attempting this bounded
discovery. The declaration of a pole requires more than a small sampled
denominator or a sampled winding number.

Reviewed main: `bc3ff0c962c485ac8104ce8cd832c119c260c871` (PR79).
Read AGENTS, the current brief, PR79 reviews 03/05/06 and PR78's original
quotient, independent algebra and admission records. The coordinator owns
the refreshed full conclusion/dependency review. This independent review
does not replay historical certificates. Both missing-original evidence
groups remain OPEN. No original computation, scan, new row, thaw,
manuscript version, external prior-art import or outreach was undertaken
for this note.

**Wall check: Distinct test.** Closest results: PR78's rejected positive
sech-power representation and PR79's conditional pole obstruction.
What changes: seek an uncancelled zero of the *complete original* M in one
fixed rectangle, which would reject general positive definiteness of C/M.
PR78 excluded only a particular sufficient representation; PR79 did not
locate such a zero. The original signed first-Laguerre estimate remains
the same open gap.

## 1. Dependency edge and its limits

Use exactly the original completed theta kernel and full real integrals:

```text
Theta(x)=sum_(n in Z) exp(-pi*n^2*x), Re x>0,
h(z)=exp(z/2)*Theta(exp(2z)),
phi(z)=(h''(z)-h(z)/4)/4,
M(z)=int_R phi(s+z)*phi(s-z) ds,
C(z)=int_R s^2*phi(s+z)*phi(s-z) ds,
k(z)=C(z)/M(z),
K(xi)=int_R k(t)*exp(i*xi*t) dt.
```

Jacobi inversion gives even phi on `abs(Im z)<pi/4`; conjugation preserves
the original coefficients. Uniform double-exponential bounds establish
holomorphic M/C there. The real-axis integrand is strictly positive, and
on the imaginary axis it is an absolute square. Hence

```text
M(x)>0,
M(i*y)=int_R abs(phi(s+i*y))^2 ds>0, abs(y)<pi/4.
```

PR79's complete, sector-uniform saddle asymptotic makes M zero-free at
both distant ends of each closed substrip. Its remaining zeros there are
finite. The quotient is integrable on horizontal lines that avoid its
poles. These are material analytic premises, not consequences of a finite
theta cutoff or of a bounded numerical search.

If one original M zero is uncancelled by C, conjugation and evenness give
upper poles. There is a lowest positive pole height b: it is the minimum
of a nonempty finite pole set in a closed substrip extending above one
given pole. Select a horizontal line above b but below the next height.
The residue theorem, including every pole and multiplicity, gives the
large-positive-frequency leading term

```text
K(xi)=exp(-b*xi)*xi^(m-1)*(T(xi)+O(1/xi))
      +O(exp(-eta*xi)),
```

where m is the maximal pole order at height b. T is a nonzero real
trigonometric polynomial, with distinct nonzero frequencies given by
the real parts of those poles. Imaginary-axis positivity excludes a
constant frequency. Its mean is zero and its mean square is positive;
both signs therefore recur a fixed distance from zero at arbitrarily
large frequencies. The smaller errors do not remove these signs.

Thus the complete implication is

```text
original M(z0)=0 and C(z0)!=0, abs(Im z0)<pi/4
  => k has a nonremovable pole
  => K takes both signs
  => k is not positive definite.
```

The Fourier constants also check independently by putting
`u=s+t, v=s-t`, whose Jacobian is 2:

```text
Fourier(M)(xi)=X(xi/2)^2/2,
Fourier(C)(xi)=L1[X](xi/2)/4,
L1[X](r)=(1/pi)*int_R X(r-xi/2)^2*K(xi) dxi.
```

Negative K does not force the convolution negative. A successful pole
certificate would exclude only this quotient-PD sufficient construction.
It would not exclude the original `J=16*L1[X]>=0` target, and first
Laguerre alone is not an RH proof. A pole-free compact rectangle does
not establish global absence of poles or positive definiteness.

## 2. Independent derivative and complete-tail check

For `Re u>=0`, differentiation of the complete original series gives

```text
phi'(u)=sum_(n>=1)
 [-4*pi^3*n^6*exp(13u/2)+15*pi^2*n^4*exp(9u/2)
  -(15/2)*pi*n^2*exp(5u/2)]*exp(-pi*n^2*exp(2u)).
```

Reflection requires `phi'(-u)=-phi'(u)`, including the sign in a
piecewise evaluator. The derivative to use in an argument principle is

```text
M'(z)=int_R [phi'(s+z)*phi(s-z)
             -phi(s+z)*phi'(s-z)] ds.
```

The second term has a minus sign. For fixed `a<pi/4`, put

```text
q=cos(2a), d=pi*q/2,
S_j=sum_(n>=1) n^j*exp(-pi*q*(n^2-1)),
B_alpha(d)=sup_(T>=1) T^alpha*exp(-d*T).
```

The supremum is explicit: set `T0=max(1,alpha/d)`, then
`B_alpha(d)=T0^alpha*exp(-d*T0)`. Valid constants are

```text
K0=2*pi^2*S4*B_(9/4)(d)+3*pi*S2*B_(5/4)(d),
K1=4*pi^3*S6*B_(13/4)(d)+15*pi^2*S4*B_(9/4)(d)
   +(15/2)*pi*S2*B_(5/4)(d).
```

They give `abs(phi(w+i*v))<=K0*exp(-d*exp(2*abs(w)))` and the same
bound for phi' with K1, uniformly for `abs(v)<=a`. Splitting the original
exponent into two halves proves these formulas; they are not empirically
fitted constants. Each positive S_j still needs its own enclosed sum/tail
if evaluated for a certificate.

For `D=d*exp(2R)`, complete real-integration tail bounds are

```text
abs(M tail)  <= K0^2*exp(-D)/D,
abs(M' tail) <= 2*K0*K1*exp(-D)/D,
abs(C tail)  <= K0^2*exp(-D)*(R^2/D+R/D^2+1/(2D^3)).
```

These cover both real-s ends. Use
`max(abs(s+x),abs(s-x))=abs(s)+abs(x)` and
`exp(2*(R+t))>=exp(2R)*(1+2t)`; dropping a positive exponential
term only weakens the bound. This justifies a usable derivative-tail
formula missing from a denominator-only locator. It does not enclose
the finite real-s quadrature error.

For a finite theta prefix, replace S_j by its discarded positive tail
to obtain a remainder constant in the same manner. Complete product
errors must include the remainder from either factor; a single-factor
tail is not automatically the M/C tail. Absolute tolerances also must
be rescaled when an evaluator multiplies M/C by a large nonzero factor.

## 3. Protocol requirements before original evaluations

The brief fixes one domain,

```text
1/8<=Re z<=2, 1/8<=Im z<=5/8,
```

strictly off the axes and inside the justified strip. It is a tractability
choice, not a prediction or a coverage theorem. The caps are a 9-by-9
initial grid, at most four selected cells, at most twelve local refinement
steps per cell, and ninety minutes including controls. A null result
does not authorize a larger domain or neighboring scan.

The code must freeze the following before original use:

1. The rational grid, quadrature/tail/cutoff choices and initial/replay
   precisions; what triggers the cutoff replay.
2. Deterministic ranking of at most four cells, including ties and cells
   whose sampled winding is undefined or whose denominator is too small.
3. The local update, derivative method, safeguard keeping every refinement
   in its selected cell, stopping rules and evaluation budget accounting.
4. The candidate denominator residual criterion and the separate C
   assessment. Small C or unresolved C must be reported as unresolved,
   never as cancellation or as an uncancelled pole.
5. The recorded distinction between raw quadrature error estimates and
   proven complete error bounds. Precision/cutoff agreement is useful
   diagnostics, not a zero certificate.

An analytic nonvanishing normalization of M preserves its zeros and has
zero total winding on a rectangle. Nevertheless, sampled phase differences
can alias severely: the sample winding is not a certified winding of
either normalized or raw M. Record the normalization and do not turn
absence of a sampled winding into absence of a zero.

## 4. Matched controls and applicability

**Uncancelled-pole control:** `M0=z^4+1, C0=1`. The rectangle
`[7/10,18/25]+i*[7/10,18/25]` encloses `(1+i)/sqrt(2)`.
The quotient is integrable on the real axis; its Fourier transform is

```text
pi/sqrt(2)*exp(-abs(xi)/sqrt(2))
 *[cos(abs(xi)/sqrt(2))+sin(abs(xi)/sqrt(2))].
```

This matches the analytic pole/contour/axis-nonvanishing mechanism and
locator geometry. It does not match original theta coefficients or their
double-exponential kernel tails. Rational horizontal decay is sufficient
for this synthetic contour check but is different from theta asymptotics.

**Removable control:** same M0, `C1=M0*exp(-z^2)`. The same denominator
zero is removable; the quotient is entire Gaussian with positive Fourier
density. Run the same denominator location and C-assessment procedure.
A denominator-only detector fails this control. Knowing its analytic
cancellation validates the toy, but the production classifier may return
only 'cancellation/unresolved C' unless it actually proves cancellation.

**NS101:** matches complete smooth kernels, quotient/convolution algebra
and strip regularity; its translated mixture changes the original lattice
and nonlinear initial data. Its negative Laguerre example forces failure
of quotient PD, but not existence of a quotient pole. Requiring this
bounded locator to find one would be an unsupported additional premise.
This is a concrete mismatch, not a passed original-arithmetic control.

**NS100:** its per-slice positivity claim is different from the complete
s-pair quotient. This experiment assumes no positivity of individual
Fourier-transformed slices, so NS100 neither excludes it nor validates it.

**Davenport-Heilbronn and controls/:** generic contour calculus transfers
when its own hypotheses hold, but coefficients, conductor, completion and
gamma factor differ. No DH kernel or complex strip has been substituted
into this original-theta locator. The unchanged example_screen.py tests
a different derivative expression and is not a screen for this test.
Record this as not applicable at the literal arithmetic/evaluator layer;
the two synthetic controls screen the actual finite pole/cancellation
algorithm. Do not relabel a mismatch or an unchanged example as a pass.

**NS74 and NS83:** the former changes NB target/inner factors at fixed
Gram data; the latter bounds fixed-smoothing NB dyadic contraction.
There is no NB Gram, optimized load, error sequence or gain-rate claim
here. Their hypotheses do not instantiate this theta quotient test.

## 5. Certificate readiness and stop consequences

An approximate root is only a candidate. A certificate needs one compact
box, complete Arb enclosures for M, M' and C, lattice and real-integration
tails, and finite quadrature error. It must prove M is nonzero on its
entire boundary and enclose the full argument-principle integral around
a positive integer. C must be nonzero throughout the box, or the relevant
M zero must otherwise be rigorously separated from all C zeros. This
does not require simple M zeros. Two precisions, all errors retained,
no midpoint solves, and a separate two-hour single-box cap apply.

At the time of this paper review these numerical components are not yet
reviewed, so certificate readiness is **NO**. An unresolved C enclosure
is not proof of cancellation. A diagnostic apparent pole does not yet
exclude the quotient-PD construction.

**Success changes:** a certified original uncancelled pole closes the
general quotient-PD sufficient construction; a reproducible diagnostic
candidate merely identifies the next bounded certification box.
**Failure changes:** a null or unstable bounded search records an
inconclusive locator outcome and stops this experiment. It establishes
neither a zero-free strip nor a positive Fourier density; it does not
admit an automatic adjacent search. No new NS row, thaw or manuscript
version is justified by diagnostic-only or failure-only work.

**Final wall check: Distinct test** for bounded quotient-route validation;
the original arithmetic lower-sign target remains **Same open gap**.

## 6. Frozen-protocol and initial implementation follow-up

After the preceding paper check I read the filled PROPOSAL.md and the
first implementations of `locator.py` and `theta_eval.py`, plus the
archived synthetic controls.json. I ran no original evaluation.

The frozen evaluator uses 128 bits / 24 lattice terms / 48 Gauss-Legendre
nodes per segment initially, then 256 bits / 32 terms / 96 nodes on the
same selected cells. Its initial positive-s breakpoints are
`0,1/8,1/4,1/2,1,2,4`; replay appends `9/2`. The full real integral
is twice this positive half. Its integrand is even in real s, including
the differentiated M integrand, by the exact parity of phi/phi'.

The common multiplier

```text
B(z)=exp(2*pi*exp(2z)-9*z)/(4*pi^4)
```

is entire and never zero. It preserves M/C zeros and the quotient;
`(BM)'=B*M'+(4*pi*exp(2z)-9)*B*M`. The implementation includes that
second term. Its real-tail and lattice error majorants are multiplied
by `abs(B)`; the derivative additionally includes the corresponding
logarithmic-derivative times M errors. The displayed series, recurrence
for `exp(-pi*n^2*exp(2u))`, derivative reflection sign, and K0/K1
formulas check. Uniform discarded-lattice estimates use the sufficient
condition `b*(N+1)^2>=13/4`, ensuring every relevant polynomial times
Gaussian is decreasing with `exp(2*abs(Re u))>=1`. The geometric
n-tail ratio decreases with n. Product error bounds retain both factors.

These majorants are evaluated as ordinary mpmath numbers, not outward
rounded intervals. Finite quadrature error and arithmetic roundoff remain
explicitly unbounded. There is consequently no change to the certificate
readiness decision.

The actual ranking is descending absolute rounded sampled winding, then
ascending minimum/maximum corner modulus, then grid indices. A corner
whose modulus is at most `2^(-bits/2)` times the maximum makes its
winding unresolved and numerically assigned zero for ranking; this
fallback must be recorded in the frozen proposal. Twelve evaluated
iterates per selected cell, sixteen allowed halvings, and same-cell
replay are enforced. The endpoint retained at the step cap is the last
point actually evaluated. Residual and numerator thresholds are only
diagnostic selection thresholds and do not enclose functions on boxes.

The archived controls report all three intended decisions: the
uncancelled toy is a promising diagnostic candidate, the removable toy's
denominator root is located, and that removable case is not labelled
an uncancelled pole. Both run the same selection/refinement/classification
path. Their pass validates this tested behavior, not global sensitivity
or original quadrature accuracy.

Two pre-original integration items were sent to the locator owner: its
initial import named `evaluator` while the actual module is `theta_eval`,
and the original runtime must deduct the already-used controls duration
from the ninety-minute combined budget. Neither is a mathematical
obstruction. With those addressed and the unresolved-winding fallback
recorded, **GO for the frozen bounded diagnostic**. A failure of ranking
or precision stability must remain a null/inconclusive outcome, not an
excuse to widen the protocol.
