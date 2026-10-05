# Review 9 — positivity notions and the missing implication

**Verdict: PASS for the distinctions in the draft; OPEN for the required
all-height inequality.** No independent arithmetic estimate follows from
the Green operator or a legitimate autocorrelation/Bochner argument.

Reviewed baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208` (PR75), as
recorded in the shared brief. I read the current AGENTS review/proposal
instructions, this audit's brief and complete derivation, PR74 reviews
01 and 05 on associated kernels and the NS101 control, and PR75's relevant
positivity scope. The coordinator owns the full register/dependency review;
this is an independent paper review of the positivity implications, not a
replay of historical computations or a new scan.

**Wall check: Same open gap.** Closest: NS100/101 and PR74/75. What changes:
the primitive has legitimate ordinary transforms, but no new implication
from its positivity to the complete first-Laguerre sign has been obtained.
The original theta arithmetic and distinguished Jacobi IVP remain outside
the generic structural argument.

## 1. Separate the positivity assertions

Use the draft's convention `Y(r)=integral f(u)*exp(i*r*u) du` and `a=1/2`.
For a function `k`, translation positive definiteness means

```text
sum_(i,j) c_i*conjugate(c_j)*k(x_i-x_j) >= 0
for every finite list of real x_i and complex c_i.
```

It is not the assertion `k(x)>=0` at each point.

| Object or assertion | What is established | What does not follow |
| --- | --- | --- |
| `G_a(u)=exp(-a*abs(u))/(2*a)` | Pointwise positive; its convolution operator preserves nonnegative functions; it is also a positive self-adjoint operator on `L2`. | Applying it to a pointwise positive input does not make the output's Fourier transform pointwise nonnegative. |
| `phi>0`, `f=4*G_a*phi` | `f>0`, with the decay and envelope in (3)-(4). | Neither `f` nor `phi` is thereby proved translation-positive-definite. |
| `Y=Fourier(f)` | `Y` is translation-positive-definite as a function of frequency. | `Y(r)>=0`, `L1[Y](r)>=0`, or the corrected inequality (10). |
| `A0(t)` | Pointwise positive and translation-positive-definite in `t`. | Positivity of the different weighted kernel `A2`, or of the corrected differential combination, in the translation-positive-definite sense. |
| `A2(t)` | Pointwise positive, smooth, integrable with all needed derivatives. | Translation positive definiteness of `A2`. |
| Translation positive definiteness of `A2` | Equivalent here to `L1[Y](r)>=0` for all real `r`. | By itself, the corrected inequality for all `abs(r)<1/2`. |
| `K=(partial_t^2-1)^2*A2-4*(partial_t^2+1)*A0=256*C` | Exact smooth, rapidly decaying complete expression. It is pointwise positive because the original `phi` is positive. | Translation positive definiteness of `K` or `C`; this is the missing first-Laguerre target. |

The `L2` operator positivity of `G_a` is independently transparent from

```text
<g,G_a*g> = (1/(2*pi))*integral |Fourier(g)(r)|^2/(a^2+r^2) dr >= 0.
```

This quadratic-form statement must not be confused with pointwise sign
after applying the differential inverse `a^2-partial_u^2`.

For the frequency-positive-definite assertion about `Y`, no abstract
theorem needs to be assumed:

```text
sum_(i,j) c_i*conjugate(c_j)*Y(r_i-r_j)
 = integral f(u)*abs(sum_i c_i*exp(i*r_i*u))^2 du >= 0.
```

The same fact holds for `X` because `phi>0`. Thus requiring both `X` and
`Y` to be positive definite in frequency is still a shared property of
the NS101 control, not the missing sign estimate.

## 2. The legitimate autocorrelation and its precise limit

The substitution `x=s+t` gives

```text
A0(t) = integral f(x)*f(x-2*t) dx.
```

Consequently `A0` really is a Gram kernel: its matrices are represented
by the translates `f(x-2*t_i)`. Its Fourier transform is

```text
Fourier(A0)(omega) = Y(omega/2)^2/2 >= 0.
```

These statements validate the first identity of (8), including the
frequency scaling. They do not require theta arithmetic.

For `A2`, the extra weight prevents the same fixed-family Gram proof.
In fact

```text
A2((x_i-x_j)/2)
 = integral [y-(x_i+x_j)/2]^2*f(y-x_i)*f(y-x_j) dy.
```

The displayed nonnegative weight depends on both matrix indices. It
cannot be pulled out as one common nonnegative integration measure. With
`f_i(y)=f(y-x_i)` and complex coefficients, define

```text
D0=sum_i c_i*f_i,
D1=sum_i c_i*x_i*f_i,
D2=sum_i c_i*x_i^2*f_i,
E=sum_i c_i*(y-x_i)*f_i.
```

Direct expansion gives the same mixed-form obstruction recorded in PR74:

```text
sum_(i,j) c_i*conjugate(c_j)*A2((x_i-x_j)/2)
 = ||E||_2^2 + (1/2)*Re<D2,D0> - (1/2)*||D1||_2^2.
```

The last two terms are not an established nonnegative contribution.
Replacing this expression by `||E||_2^2` would change the kernel.

Equation (8) correctly identifies its Fourier sign:

```text
Fourier(A2)(2*r)=L1[Y](r)/4.
```

Because `A2` is pointwise positive, its Fourier transform is itself a
positive-definite function of frequency. That statement permits negative
pointwise values. It is not the converse assertion that `A2` is positive
definite in its translation variable. Fourier inversion and the stated
integrability make the latter equivalent to the required pointwise
nonnegativity of `L1[Y]`.

As a bare logical illustration, `q(r)=3+2*cos(beta*r)` is positive
definite (the Fourier transform of three positive point masses) and
pointwise positive, but `L1[q](pi/beta)=-2*beta^2<0`. This is only an
elementary explanation of the logical distinction; the fully matched
smooth primitive control is the existing NS101 family in draft (11)-(12).

## 3. The corrected target has an additional low-frequency obligation

Write `p=r^2+1/4`. Equations (7)-(9) give

```text
Fourier(K)(2*r)=64*L1[X](r),
16*L1[X](r)=p^2*L1[Y](r)+2*(r^2-1/4)*Y(r)^2.
```

Thus translation positive definiteness of `K` is precisely the all-real
first-Laguerre target. It is not a new estimate furnished by the inverse
operator.

There are two distinct unproved steps if one tries to proceed through
`A2` alone:

1. Establish `L1[Y]>=0`, or equivalently translation positive definiteness
   of `A2`, using something beyond the shared positive-kernel structure.
2. For `abs(r)<1/2`, establish the stronger margin

```text
L1[Y](r) >= 2*(1/4-r^2)/(r^2+1/4)^2*Y(r)^2.
```

For `abs(r)>=1/2`, step 1 would suffice; below that threshold it does not.
At `abs(r)=1/2` the correction vanishes. At a zero of `Y`, the formula is
regular and `L1[Y]=Y'^2>=0`. These special points cannot replace the
all-real quantifier.

The operator reading reaches the identical restriction: the first term
in `Fourier(K)(omega)` has multiplier `(omega^2+1)^2` on `Fourier(A2)`,
whereas the second has multiplier `4*(omega^2-1)` on the already
nonnegative `Fourier(A0)`. Its negative low-frequency part cannot be
dropped. A convolution identity alone supplies neither required margin.

## 4. Matched control and admission decision

Draft (11) preserves the positive Green representation, pointwise
positivity, the unit exponential tail, the envelope, frequency positive
definiteness of `X_beta` and `Y_beta`, pointwise positivity of both
`A0_beta` and `A2_beta`, and translation positive definiteness of
`A0_beta`. The complete corrected identities remain valid. The recorded
PR74 sufficient parameter range nevertheless gives a strict negative
value of `L1[X_beta]`.

That is the precise reason no implication from this collection of
structural properties to the corrected target can be valid. It does not
assert that the original `A2` fails positive definiteness, nor that the
original corrected target fails. The control changes the single-lattice
coefficients and loses the distinguished Jacobi IVP.

**Missing edge:** a bound for the complete corrected expression, or an
equivalent matrix inequality retaining the mixed terms, at every real
height using an original arithmetic/IVP hypothesis absent from the
control. No such estimate or method is supplied by these positivity
arguments. No new candidate, scan, research row or manuscript version is
warranted from this audit.

**Final wall check: Same open gap.** The generic structural shortcut is
stopped by the existing NS101 matched control; the original arithmetic
theta route remains unexcluded.
