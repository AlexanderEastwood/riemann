# Independent audit of PR73: pair algebra and reflected-prefix boundary

Reviewed scientific baseline: `5434d96f0034f842b0229f1d69dbbf3fb7fea270`
(merged PR73). Working HEAD at completion of the reading pass:
`971c8bd02c834cf31ab98ea2a50060289fbece40`. The intervening diff adds only
the six-agent brief, review record and task entry; it changes no mathematical
dependency. The coordinator refreshed the remote and reviewed the entire
104-node conclusion register. I read current agent/proposal instructions,
README status, the applicable ZERO-GEOMETRY register and freeze, the missing
evidence ledger, PR72/73 reports and the four supporting mathematical notes
named in the brief. This is an independent paper audit of the specified
claims, not a historical certificate replay or independent validation of
the external source's computer-assisted curvature theorem.

**Wall check: Same open gap.** Closest results: NS100/101, PR72/73.
What changes: no arithmetic hypothesis. The exact validation question is
whether PR73's mixed form, original pair clock, fixed-prefix asymptotic and
full-tail correction have the asserted signs, constants and domains.
The dependency is the complete original first-Laguerre target
`L1[X](r)>=0` for every real `r`, equivalently positive definiteness of
`C`; this is only a necessary first-order part of the original radial-sign
program, not the full all-order or RH criterion.

## Verdict and findings

No factor, sign or missing-regularity defect was found in those PR73 claims
under their stated fixed-prefix and complete-theta hypotheses. In
particular, `-8*delta_M^2*r^-6` and the net correction
`+8*delta_M^2*r^-6` are correct.

Two distinctions should remain explicit in subsequent use:

1. The positive **net correction** includes the cross terms between the
   prefix and tail. The tail's own first-Laguerre expression is eventually
   negative; it is not a positive summand.
2. Cancellation of every algebraic boundary term proves rapid frequency
   decay, not its sign. A direct smooth, positive, strictly log-concave,
   double-exponentially decaying control below has all odd boundary
   derivatives zero and nevertheless has a negative first-Laguerre value.
   It does not preserve the original arithmetic or Jacobi initial-value
   problem. This is a control on a possible overinterpretation, not a
   counterexample to PR73 or to the original theta target.

## 1. Fourier and mixed-form constants

Take the Fourier convention
`X(r)=integral phi(u)*exp(i*r*u) du`, with the complete real even Schwartz
kernel `phi`. Symmetrizing the product defining `L1` gives

```text
L1[X](r) = (1/2) integral integral
           (u-v)^2 phi(u) phi(v) exp(i*r*(u+v)) du dv.
```

Replace `v` by `-v`, then set `u=s+t, v=s-t`. The latter substitution
has absolute Jacobian `2`, and `(u+v)^2/2=2*s^2`. Consequently

```text
L1[X](r) = 4 integral C(t) exp(2*i*r*t) dt
         = 4 integral C(t) cos(2*r*t) dt,
C(t) = integral s^2 phi(s+t) phi(s-t) ds.
```

The complete integrands and the derivatives/moments used here are
absolutely integrable. `C` is a real even Schwartz function. Fourier
inversion/positive definiteness therefore makes its nonnegative transform
equivalent to all finite positive-semidefinite matrices, with no need to
weaken the quantifier to sampled frequencies or finitely many shifts.
The scaling by `2` covers the entire real frequency line.

For the mixed form, fix any finite number of arbitrary real shifts and
complex coefficients. Use the inner product linear in its first argument.
Putting `s=y-(x_i+x_j)/2` in a matrix entry yields

```text
C((x_i-x_j)/2)
 = integral [y-(x_i+x_j)/2]^2 phi(y-x_i) phi(y-x_j) dy.
```

Expand the square as
`(y-x_i)*(y-x_j)+(x_i-x_j)^2/4`. The second contribution after summation is

```text
(1/4) [<D2,D0> + <D0,D2> - 2*<D1,D1>]
 = (1/2) Re<D2,D0> - (1/2)||D1||^2.
```

This independently reproduces PR73's exact formula with `||E||^2` for the
first contribution. There is no hidden real-coefficient restriction;
Hermitian symmetry is exactly what produces the real part. Coincident
shifts cause no problem. The resulting all-coefficient inequality is
equivalent to the required positive definiteness, not an established
lower bound. Dropping either signed contribution is unjustified.

## 2. Nonlinear clock, derivatives and regularity

One can check the clock without the external curvature theorem. Set

```text
L=2u,
H(L)=exp(L/4)*Theta(exp(L))=(A(L)/pi)^(1/4),
H'/H=a/4,
a'=(U+a^2-1)/2.
```

The complete theta differential identity gives

```text
phi(L/2)=H''(L)-H(L)/16
        =H(L)*[U+(3/2)*(a^2-1)]/8
        =H(L)*d(L)/8.
```

Here `H>0` and `phi>0` on every finite real clock, so `d>0`. Differentiating
its logarithm gives precisely

```text
P = a/4 + d'/d,
d' = 2*U*(a+chi)+(3*a/2)*(U+a^2-1).
```

Thus `phi'(u)=2*P(2u)*phi(u)` and `P1=V(P)` is an `L` derivative, not a
`u` derivative. The given modular initial data give `P(0)=0` directly.
With `Pplus=P(2*(s+t))` and `Pminus=P(2*(s-t))`, the independent chain rule
is

```text
(log K)_t  = 2*(Pplus-Pminus),
(log K)_tt = 4*(P1plus+P1minus),
K_tt = 4*[(Pplus-Pminus)^2+P1plus+P1minus]*K.
```

The plus sign in front of `P1minus` is correct: the minus in
`Pplus-Pminus` cancels the derivative of its negative clock. Equivalently,

```text
K_tt = phi''(s+t)*phi(s-t)
       -2*phi'(s+t)*phi'(s-t)
       +phi(s+t)*phi''(s-t).
```

The last form supplies dominated differentiation without assuming bounds
on the separately growing slope variables. For `t` in any compact real
interval, complete theta derivative envelopes give an integrable common
majorant after multiplication by `s^2`. Consequently the asserted `C''`
formula is valid for every finite real `t`, locally uniformly in `t`.
No artificial cut or boundary occurs at `s=t` or `s=-t`.

The derivation needs the distinguished analytic theta trajectory. It must
not replace it by arbitrary branches of the squared Jacobi equation or
divide by `chi` at its zero. The supporting source audit already records
this distinction. The source's negative real `P1`/curvature information,
even if granted, does not fix the sign of the displayed combination or
of its oscillatory transform.

## 3. Fixed reflected-prefix asymptotic

Let `M>=1` be an integer held fixed, and let `f_M` be PR73's positive
half-line sum. Write `a_n=pi*n^2`. Direct differentiation of one term at
zero gives

```text
b_n = exp(-a_n)*[-4*a_n^3+15*a_n^2-(15/2)*a_n].
```

For `a>=4`, the bracket divided by `a` is negative: it equals `-23/2`
at `4` and its derivative `-8*a+15` is negative thereafter. For every
`n>=2`, `a_n>4`. Gaussian summability permits differentiating the full
series near zero. Smooth evenness of the complete kernel gives

```text
sum_(n>=1) b_n=0,
delta_M=f_M'(0)=-sum_(n>M) b_n>0.
```

Thus the reflected prefix is continuous with an upward cusp. Smoothness
of each half-line summand is sufficient for the following integrations
by parts; smoothness across the reflected cusp is not assumed.

For any smooth rapidly decreasing half-line function `h`, repeated
integration by parts gives

```text
integral h(u)*cos(r*u) du
 = -h'(0)/r^2 + h'''(0)/r^4 + O(r^-6),
integral h(u)*sin(r*u) du
 = h(0)/r - h''(0)/r^3 + O(r^-5),
```

with the derivatives and decay needed for the displayed remainder.
Every weighted derivative of `f_M` has that integrability. Apply these
identities separately to `f_M`, `u*f_M` and `u^2*f_M`. In particular,
`(u*f_M)''(0)=2*delta_M`, `(u^2*f_M)'(0)=0`, and
`(u^2*f_M)'''(0)=6*delta_M`. The resulting three estimates are

```text
X_M   = -2*delta_M*r^-2 + O_M(r^-4),
X_M'  =  4*delta_M*r^-3 + O_M(r^-5),
X_M'' = -12*delta_M*r^-4 + O_M(r^-6).
```

These are estimates of the differentiated transforms, not derivatives
of an uncontrolled remainder. Multiplication gives the coefficients
`16-24=-8`, hence

```text
L1[X_M] = -8*delta_M^2*r^-6 + O_M(r^-8).
```

Because `delta_M>0`, for every fixed `M` there exists a finite `R_M` such
that this is strictly negative for all `r>R_M`. No numerical onset or
uniformity in `M` follows from this assertion. Negative heights follow
by evenness. The all-height nonnegative-prefix certificate is therefore
excluded for exactly this reflected construction.

The more general odd-boundary statement also has the correct sign. If
the first nonzero odd right derivative has order `2k+1`, put
`nu=2k+2` and `c=2*(-1)^(k+1)*h^(2k+1)(0)`. Under the corresponding
weighted differentiable remainders, `X=c*r^-nu+...` gives
`L1[X]=-nu*c^2*r^(-2*nu-2)+...`. It cannot be applied to a repair whose
odd derivatives all vanish, or without the differentiated remainder
hypotheses.

## 4. What the full-tail correction actually says

Put `T_M=X-X_M`, the transform of the complete omitted reflected tail.
The original complete kernel is Schwartz, so `X`, `X'` and `X''` decay
faster than every inverse power. For fixed `M` this implies

```text
T_M   =  2*delta_M*r^-2 + O_M(r^-4),
T_M'  = -4*delta_M*r^-3 + O_M(r^-5),
T_M'' = 12*delta_M*r^-4 + O_M(r^-6).
```

Retaining the cross terms explicitly gives

```text
L1[X] = L1[X_M] + L1[T_M] + B_M,
B_M = 2*X_M'*T_M' - X_M*T_M'' - T_M*X_M'',

L1[T_M] = -8*delta_M^2*r^-6 + O_M(r^-8),
B_M     = 16*delta_M^2*r^-6 + O_M(r^-8).
```

Therefore PR73's **net** formula is correct:

```text
L1[X]-L1[X_M] = 8*delta_M^2*r^-6 + O_M(r^-8).
```

The omitted tail is positive in the real variable, but its own
first-Laguerre expression is negative at sufficiently large height.
Calling that term a positive remainder would be false. The positive
cross term is essential, and the three leading coefficients sum to zero.

Smooth evenness in fact cancels the entire algebraic boundary expansion,
not only the first `r^-6` contribution. Equivalently,
`L1[X]=O_N(r^-N)` for every fixed `N`. This is a valid stronger decay
statement, already implicit in the Schwartz observation, but it gives
no lower sign bound: it places the remaining expression below every
fixed algebraic scale.

The fixed-`M` error is not `o(r^-6)`. It also cannot be used without a
new uniform estimate for `M=M(r)`. A changing integer prefix must further
distinguish evaluations of the fixed-prefix derivative integrals from
derivatives of the possibly discontinuous composite `X_{M(r)}(r)`.
None of these observations excludes a correctly controlled growing
prefix or a globally smooth completion.

## 5. Paper control for an overstrong boundary-cancellation inference

This is a separate generic control, not NS101's reciprocal mixture.
Its only purpose is to test the inference from perfect boundary
cancellation, positivity and real log-concavity to first-Laguerre sign.
No theta-specific hypothesis is used in that inference.

Define

```text
k(u) = [3*exp(-u^2/3)+exp(-(u-1)^2/3)+exp(-(u+1)^2/3)]/sqrt(3*pi),
Y(r) = integral k(u)*exp(i*r*u) du
     = exp(-3*r^2/4)*(3+2*cos r).
```

For `q=3+2*cos r`, direct differentiation gives

```text
L1[Y](r) = exp(-3*r^2/2)*[(3/2)*q(r)^2+4+6*cos r],
L1[Y](pi) = -(1/2)*exp(-3*pi^2/2)<0.
```

The kernel is smooth, positive and even. The Gaussian mixture identity
for the logarithmic second derivative is
`(log k)''=-2/3+(4/9)*Var_u(c)`, with centers `c` in `{-1,0,1}`.
Their variance is at most `1`, so `(log k)''<=-2/9` everywhere.

To retain double-exponential rather than Gaussian real tails, take

```text
k_eta(u)=k(u)*exp(-eta*cosh(2*u)),  eta>0.
```

Every such kernel is positive, even, real analytic, Schwartz, and has
double-exponential tails with all polynomially weighted derivatives.
It is strictly log-concave since
`(log k_eta)''<=-2/9-4*eta*cosh(2*u)`. All odd derivatives at zero vanish.
Dominated convergence against `|u|^j*k(u)`, for `j=0,1,2`, gives
`Y_eta^(j)(pi)->Y^(j)(pi)` as `eta` decreases to zero. Therefore there
exists `eta_0>0` such that `L1[Y_eta](pi)<0` for every
`0<eta<eta_0`. This is an analytic open-parameter assertion, not a
sample, certified decimal threshold or numerical scan. Positive scalar
normalization can impose any chosen positive total integral without
altering this sign.

This control has no original one-lattice coefficients or distinguished
Jacobi IVP. For small `eta<pi`, its leading real decay coefficient is
`eta/2` instead of the original `pi`, so it is not the original theta
kernel. No original normalized theta differential equation, modular
completion, or critical-strip zero restriction is asserted for it.
It refutes only the generic boundary/shape inference; it does not
settle any estimate using the original trajectory. In particular it
does not replace or predetermine the separate NS101 first-Laguerre test.

## Controls, consequences and bounded next step

- **NS100:** the original kernel's per-slice positivity already fails.
  That excludes a per-slice argument, not the `s^2`-integrated pair.
- **NS101:** shares the generic pair and mixed-form identities but fails
  the original normalized Jacobi equation. Its off-axis zeros alone
  cannot be used to infer a negative first-Laguerre value.
- **Reflected prefixes:** match the first `M` original coefficients and
  their full half-line tails but lose smooth modular-point cancellation
  and the original IVP. The fixed-prefix exclusion is a known wall for
  precisely that proposed certificate.
- **Davenport-Heilbronn:** different coefficients, conductor and
  completion; it is not an instance of the distinguished original IVP.
- **Smooth control above:** matches the boundary, positivity, strict
  real log-concavity and tail properties involved in the possible generic
  inference. It loses the original arithmetic and IVP. Its first-Laguerre
  failure is direct, not deduced from off-axis zeros.

Audit success validates the formulas and the scope of the fixed-prefix
stop. A failed check would have required a forward correction; none is
needed for the audited mathematical claims. The two scope clarifications
above prevent invalid strengthened readings. No independent estimate of
the original complete mixed quadratic form follows.

The remaining comparison is still

```text
||D1||^2 <= 2*||E||^2 + Re<D2,D0>
```

for every finite real shift family and complex coefficient vector, using
the original arithmetic trajectory. Boundary cancellation is insufficient
for that comparison. The next admissible budget is one bounded paper
review of a supplied orbit-specific inequality and its complete transfer;
without such an inequality, allocate no scan or certificate-replay budget.
This audit itself is complete. No manuscript edit, new research row,
commit, push, outreach, numerical scan or symbolic scan was performed.

**Final wall check: Same open gap.** The fixed reflected-prefix certificate
is excluded; the complete original first-Laguerre inequality, stronger
radial-sign target, cofinal signed arithmetic floor, G2 and RH remain open.
