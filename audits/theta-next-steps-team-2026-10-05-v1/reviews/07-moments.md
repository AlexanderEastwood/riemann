# Review 7 — complete moments, Jensen transfer and the absent estimate

Reviewed remote baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34`
(PR76), in the coordinator's isolated worktree. I read AGENTS/proposal
requirements, current README/NEXT_STEPS, relevant ZERO-GEOMETRY map scope,
the missing-original ledger, PR74's matched-control proof, PR76's derivation
and moment review, and the September 29 Jensen audit. The coordinator owns
the repository-wide review. This is a paper dependency assessment, not a
historical proof/certificate replay. Both original-evidence groups stay OPEN.

**Wall check: Same open gap.** Closest results: NS100's Jensen proposal,
NS101, PR74 and PR76. What changes: specify the integration constants and
critical-value inequalities omitted by a proposed backward-in-shift
transfer. No new original-coefficient estimate is supplied. **Disposition:
no candidate admitted; stop the moment/Jensen shortcut.**

## Exact original input and target

Keep the complete original integer-square theta series, its positive even
differential kernel `phi`, and

```text
m_(2n) = integral_R u^(2n)*phi(u) du,
a_n = n!*m_(2n)/(2n)!,                 n = 0,1,2,...,
X(r) = sum_(n>=0) a_n*(-r^2)^n/n! = xi(1/2+ir)/2,
p(r) = r^2+1/4,                       Y(r)=4*X(r)/p(r),
J(r) = p(r)^2*(Y'(r)^2-Y(r)*Y''(r))
       +2*(r^2-1/4)*Y(r)^2 = 16*(X'(r)^2-X(r)*X''(r)).
```

The target is `J(r)>=0` for **every real r**, including zeros. The
factorial normalization in `a_n` is essential; raw moment log-convexity
is a different inequality. PR76 already proves origin positivity and a
bounded local interval from `m_0,m_2,m_4`. Neither covers all heights.
Work with entire `X`; meromorphic `Y` has poles at `+/-i/2` and cannot
silently replace it in an entire-function theorem.

## A complete transfer exists, but its arithmetic premises are unproved

Define the normalized Jensen polynomials

```text
P_(d,n)(z) = sum_(j=0)^d binom(d,j)*a_(n+j)*z^j.
P'_(d,n)(z) = d*P_(d-1,n+1)(z).
```

For the simple-critical-point case, suppose `P_(d-1,n+1)` has distinct
negative roots `c_1<...<c_(d-1)`. The exact additional inequalities for
`P_(d,n)` to have only real roots are

```text
(-1)^(d-i) * [a_n + d*integral_0^(c_i) P_(d-1,n+1)(t) dt] >= 0,
i=1,...,d-1.                                                   (*)
```

The bracket is precisely `P_(d,n)(c_i)`. Alternating critical values,
together with the leading coefficient's signs at the two infinities,
give the required roots by monotonicity and the intermediate value
theorem, counting a zero extremum twice. Necessity follows from
interlacing. Multiple critical roots require the corresponding
multiplicity conditions; no strict-root premise may be inferred from
weak inequalities during an induction. Strict versions of (*) are a
sufficient induction premise but stronger than necessary.

Already `d=2` requires
`a_(n+1)^2>=a_n*a_(n+2)`: ordinary normalized Turan inequalities settle
this degree only. Their validity cannot replace (*) for unbounded degree.
The derivative recurrence discards `a_n`; differentiation universality
does not bound the lost constant against the alternating integral areas.
For a concrete algebraic warning, `z^2+1` has a real-rooted derivative
but fails its single required critical-value sign.

If an independent argument supplied negative real roots for
`P_(d,0)` for every `d>=1`, set

```text
Q_d(r) = P_(d,0)(-r^2/d).
```

These have real roots and satisfy `Q_d'^2-Q_d*Q_d''>=0` on the real line.
Because `binom(d,j)/d^j -> 1/j!` and is at most `1/j!`, the absolutely
convergent complete moment series gives `Q_d -> X` locally uniformly in
the complex plane; Cauchy's formula supplies convergence of two
derivatives. Passing to the limit proves `J(r)>=0` at each arbitrary
real `r`. This transfer needs neither division by `X` nor an all-height
fixed absolute margin. Its **missing premise** is unshifted all-degree
hyperbolicity, an RH-strength obligation, not an easier moment bound.
The first-Laguerre conclusion alone is not RH.

## Prior-art and matched-control scope

[Holland, arXiv:2608.08682v1, Theorem 1.1](https://arxiv.org/html/2608.08682v1#S1)
states hyperbolicity in `n^3*log(n+2)^2>=K*d^5`. Its coefficients are
`gamma(n)=2*a_n` in our normalization. The positive scaling changes no
roots. That region excludes `n=0,d>=1`; its proof supplies no estimates
for the successive missing critical values (*). The September 29 audit
already records this backward-in-shift gap. This source check imports
the stated scope, not a fresh verification of its proof.

[Csordas, arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2)
separates the first Laguerre inequality from the complete real-zero
criterion. No full positive-definite matrix hierarchy is being proposed
here as an easier estimate.

NS101 shares complete positive moments, their Hankel positivity,
origin generalized-Laguerre positivity and the primitive relation.
PR74 nevertheless proves, with `k=m_2/m_0`,

```text
L1[X_beta](pi/beta)
 <= -(beta^2-3*k)*m_0^2/(2*B_beta^2) < 0,
beta>=max(2,pi*sqrt(k)), B_beta=3+2*cosh(beta/2).
```

Thus those shared moment properties cannot supply the target. No claim
is made that this control satisfies all normalized Turan inequalities,
Holland's complete quantitative region, or (*). It changes the original
lattice coefficients and Jacobi IVP. Any proposed proof of (*) must use
those original data at an identifiable estimating step; their mere
appearance in `a_n` supplies no such step. NS100 excludes per-slice
positivity, which the conditional transfer above never assumes.

## Decision and bounded future budget

The exact missing inequalities (*) are **gap identification**, not an
admitted arithmetic candidate. No mechanism estimates their alternating
areas using the original integer-square coefficients. Stop: no new scan,
computation, row, thaw or manuscript version.

Only if an explicit original-coefficient estimate for (*) is proposed,
allow a **two-hour paper admission audit**: check its unbounded-degree
quantifiers and multiplicities, identify the arithmetic step, then compare
NS101 premises. Success would admit that particular estimate for further
proof review, not prove it or RH; failure leaves the present stop intact.
Do not spend this budget on more eventual-hyperbolicity tables.

**Final wall check: Same open gap.** RH, G2, the cofinal signed-arithmetic
lower bound, and the original all-height first-Laguerre sign remain open.
