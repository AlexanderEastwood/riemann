# Review 02 — real boundaries and complete moment transfer

**PASS on the assigned real-variable boundary audit. OPEN on the sign.**

Reviewed scientific baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208`
(PR75). Read AGENTS section 0 and project premise, the present review brief
and complete draft, and PR75's complete `derivation.md`. The parent supplied
the repository-wide conclusions/dependency review; this review independently
checks the following boundary calculations, not all historical proofs or
certificates. No scans, numerical computation, extra agents or external
outreach were used.

**Wall check: Same open gap.** Closest: NS100/101 and PR74/75. What changes:
a globally smooth decaying primitive permits ordinary transforms of the
separate moments. It supplies no sign estimate for the corrected expression.

## 1. Smoothness, endpoints and positivity of the primitive

Equations (1)-(4), draft lines 28-65, are correct with `a=1/2`.
The definition `f=2*cosh(u/2)-h(u)` is global. Theta reciprocity gives
`h(-u)=h(u)`, while its series and every derivative converge locally uniformly
on the real line. Thus `f` is smooth and even, including at zero, and every
odd derivative at zero vanishes. No reflected half-line approximation is
being differentiated.

More explicitly, for each derivative order `k` there is a finite `c_k` such
that

```text
abs(f^(k)(u)) <= c_k*exp(-abs(u)/2),  every real u.
```

On the positive half-line, differentiate the exponentially small series in
(1). Each derivative is a sum of polynomial factors in
`z_n=pi*n^2*exp(2u)` times `exp(u/2-z_n)`, hence is negligible compared with
`exp(-u/2)` at infinity. Compact intervals are controlled by smoothness;
evenness covers the other tail. This proves the derivative bound, the unit
tail ratio, and every claimed weighted integrability assertion.

The Green factor is correct: `G_a=exp(-a*abs(u))/(2*a)`, whose first
derivative has jump `-1`, satisfies `(a^2-d^2)G_a=delta`. At `a=1/2` its
denominator is one. Since `phi` is smooth and has exponentially weighted
integrable tails, `g=4*G_a*phi` is a classical smooth solution of (2), and

```text
abs(g(u)) <= 4*exp(-abs(u)/2)
              * integral_R exp(abs(v)/2)*phi(v) dv.
```

Consequently `g` decays at both ends. The smooth difference `f-g` solves
`w''=a^2*w` and is a linear combination of `exp(a*u)` and `exp(-a*u)`;
decay at both endpoints forces both coefficients to vanish. This justifies
uniqueness without treating the cusp in the Green kernel as a cusp in `f`.
Its distributional delta is precisely the defining source and leaves no
additional atom or boundary term after convolution.

The inherited positivity of `phi` can also be seen directly at `u>=0`:
its nth summand is `exp(u/2)*(2*z_n^2-3*z_n)*exp(-z_n)`, positive since
`z_n>=pi`; reciprocity covers `u<0`. Thus convolution gives `f>0`, and
(1) gives the strict upper envelope `f<exp(-abs(u)/2)`, including zero.

## 2. Explicit pair envelopes and all exchanges

Equation (6), draft lines 93-104, has the correct constants. Writing
`T=abs(t)` and `F(s,t)=f(s+t)*f(s-t)`, the basic envelope is

```text
abs(F(s,t)) <= exp(-max(abs(s),T)).
```

Direct integration gives

```text
integral_R exp(-max(abs(s),T)) ds = 2*(T+1)*exp(-T),
integral_R s^2*exp(-max(abs(s),T)) ds
  = 2*(T^3/3+T^2+2*T+2)*exp(-T).
```

The same bound with a finite derivative-dependent constant holds for every
mixed derivative `partial_s^j partial_t^k F`, by the bound on derivatives
of `f`. This is sufficient simultaneously for:

- differentiation under the `s` integral, with compact-uniform domination;
- absolute Fubini exchanges in both real variables with each polynomial
  weight used in the draft;
- all `s` endpoint terms in (7), since polynomial multiples of derivatives
  vanish at both endpoints;
- all ordinary `t` transforms and `t` integrations by parts, since every
  derivative of either `A_j` obeys a constant times its corresponding
  polynomial-exponential envelope in (6).

Equivalently `f` is a Schwartz function, and so is `F` after the invertible
linear change of coordinates; integrating its weighted `s` slices preserves
that property. The explicit envelopes are stronger information about the
tails and do not conflict with the Schwartz statement.

Therefore `integral s^2*F_ss=2*A_0` and
`integral s^2*F_ssss=0` in (7) are legitimate. Equations (5) and (8) are
ordinary Fourier identities on every real frequency. No interpretation by
finite part, analytic regularization or distributional Fourier transform is
needed for them.

## 3. Exact comparison with PR75: no hidden homogeneous term

An optional strengthening of the exposition is to show explicitly how the
old and new completed products relate. Put `c(u)=2*cosh(u/2)`, so `h=c-f`.
With the old PR75 notation `R=h(s+t)*h(s-t)-2*cosh(s)`,

```text
R(s,t)-F(s,t)
 = 2*cosh(t)-c(s+t)*f(s-t)-c(s-t)*f(s+t).
```

This is a pointwise equality of smooth functions. The right side must be
kept as a complete expression before integration in `s`: its three displayed
terms separately include nonintegrable constants at infinity. Their sum
decays at both `s` endpoints, as follows either from PR75's proven tail for
`R` and the new bound for `F`, or directly from the unit tails of `f`.

The pair operator `P` in PR75 annihilates this entire difference. Each mixed
`c*f` term has one factor killed by `d^2-1/4`; on `2*cosh(t)` the operator
reduces to `(partial_t^2-1)^2`, also zero. Consequently the differential
moment expressions built from old `M_j` and new `A_j` are identical. They
are two complete representations of `256*C`; the replacement is not a
discarding of the old growing terms one at a time. No new delta appears at
`s=0`, `t=0`, `s=t` or `s=-t`, since all underlying functions are smooth.

## Disposition

No correction to (1)-(8), the explicit envelopes or their real boundary
justifications is required. The displayed old/new comparison would make
the absence of hidden terms easier to verify, but is an explanatory addition
rather than a repair. This review does not infer a Laguerre sign from any
envelope. Equation (10) remains the full original sign obligation.
