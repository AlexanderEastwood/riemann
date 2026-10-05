# Review 4/12: pair operator, Fourier constants and correction term

**Disposition: PASS on the assigned algebra; OPEN on the all-height sign.**

Reviewed baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208` (PR75).
Read the present review brief, `derivation.md`, applicable `AGENTS.md`
instructions, and PR75's `audits/theta-addition-admission-2026-10-05-v1/derivation.md`.
This is an independent paper check of equations (7)-(10) and their boundary
premises, not a replay of every registered conclusion or certificate. The
parent supplied the register/dependency review; this reviewer did not
repeat it. No scan, symbolic computation, new sign candidate or certificate.

**Wall check: Same open gap.** Closest: NS100/101 and PR74/75.
The subtraction repairs the ordinary-transform domain, while the complete
first-Laguerre signed obligation is unchanged. The following identities
do not provide an estimating method for that obligation.

## 1. Pair operator and 256

Let `u=s+t`, `v=s-t`, and `F(s,t)=f(u)f(v)`. Holding the other original
coordinate fixed gives

```text
partial_u=(partial_s+partial_t)/2,
partial_v=(partial_s-partial_t)/2.
```

Since `phi=(1/4-partial_u^2)f/4`, the two negative signs in the product
cancel. Thus

```text
phi(u)phi(v)
 = [((partial_s+partial_t)^2-1)
    *((partial_s-partial_t)^2-1)] F/256
 = [partial_s^4-2*partial_s^2*partial_t^2+partial_t^4
    -2*partial_s^2-2*partial_t^2+1] F/256.
```

In the polynomial multiplication, write `A=partial_s^2+partial_t^2-1`
and `B=2*partial_s*partial_t`; the commuting product is `A^2-B^2`.
This explicitly retains the mixed derivative. Integrability and vanishing
boundaries follow from the stated exponential bounds for all derivatives
of f. Two integrations by parts give `integral s^2 F_ss=2*A_0`; four
give `integral s^2 F_ssss=0`. Consequently equation (7) is exactly

```text
256*C=(partial_t^2-1)^2*A_2-4*(partial_t^2+1)*A_0.
```

**PASS.** Neither the mixed term nor the old PR75 boundary issue is hidden
in the factor 256.

## 2. The Jacobian and the two Fourier identities

The absolute determinant of `(s,t)->(u,v)` is 2, so
`ds dt=du dv/2`, `s=(u+v)/2`, and `2rt=r(u-v)`. Evenness and reality of f
make Y real and even on the real axis. Fubini is justified, also with
second moments. Therefore

```text
integral A_0(t)*exp(2irt)dt=Y(r)*Y(-r)/2=Y(r)^2/2.
```

For `A_2`, the prefactor is `1/8`, from the Jacobian and `s^2`.
The square moments are `-Y''(r)` and `-Y''(-r)`, while the first moments
are `-iY'(r)` and `-iY'(-r)=iY'(r)`. Hence

```text
integral A_2(t)*exp(2irt)dt
 =[-2*Y(r)*Y''(r)+2*Y'(r)^2]/8
 =L1[Y](r)/4.
```

The imaginary parts vanish. In particular the cross moments have a plus
sign, not a minus sign. Applying the same derivation directly to phi gives
`integral C(t)*cos(2rt)dt=L1[X](r)/4`, independently checking the final
normalization. **PASS on equation (8).**

## 3. Correction term in equations (9)-(10)

Set `p=r^2+1/4`. Transforming equation (7), using the legitimate decaying
`A_j` and their derivatives, gives

```text
256*integral C(t)*cos(2rt)dt
 =(4*r^2+1)^2*L1[Y]/4-2*(1-4*r^2)*Y^2
 =4*p^2*L1[Y]+8*(r^2-1/4)*Y^2.
```

Multiplication by `4/256` therefore gives

```text
16*L1[X]=p^2*L1[Y]+2*(r^2-1/4)*Y^2.
```

An independent product expansion verifies it: the two `p*p'*Y*Y'`
cross terms cancel, giving `L1[pY]=p^2*L1[Y]+(p'^2-p*p'')*Y^2`.
Here `p'^2-p*p''=2*(r^2-1/4)` and `X=pY/4`.

Since p is strictly positive for real r, rearranging yields exactly
equation (10). **PASS.** The multiplier correction is essential; dropping
it changes the target, especially for `abs(r)<1/2`.

## 4. Exceptional real heights and signs

- At `r=0`, equation (10) is `L1[Y](0)>=8*Y(0)^2`. This point is
  consistent with strict positivity of the original moments. Let
  `F_j=integral u^j*f(u)du`, `m_j=integral u^j*phi(u)du`, for j=0,2.
  Integrating `(1/4-partial_u^2)f=4*phi` gives
  `F_0=16*m_0` and `F_2=8*F_0+16*m_2`. Since Y is even,
  `L1[Y](0)=F_0*F_2`, so
  `L1[Y](0)-8*Y(0)^2=256*m_0*m_2>0`.
  This is a point check from the positive-kernel premises, not an
  all-height estimate or a new research target.
- At `abs(r)=1/2`, p=1/2 and the correction vanishes:
  `L1[X]=L1[Y]/64`. Thus first-Laguerre positivity of the two transforms
  is equivalent at exactly those two heights.
- The real zeros of X and Y agree, with multiplicity, because p>0. At
  such a zero, `X'=p*Y'/4` and
  `16*L1[X]=p^2*Y'^2>=0`; multiple zeros may give equality. Equation
  (10) remains regular without dividing by either transform.
- For `abs(r)>1/2`, `L1[Y]>=0` would suffice, but need not be necessary,
  because the correction in (9) is nonnegative. For `abs(r)<1/2`, the
  required positive margin cannot be dropped. Pointwise positivity of
  `A_2` does not supply its Fourier-transform sign in either region.

**PASS on all requested exceptional-point checks.** The draft's claims
are correctly scoped; the r=0 moment calculation could be added as an
optional normalization check, but no correction is required.

## 5. Comparison with PR75 without dropping cross terms

Put `g(u)=2*cosh(u/2)`, so `f=g-h`. Then

```text
F=f(u)f(v)=h(u)h(v)-g(u)h(v)-h(u)g(v)+g(u)g(v).
```

The full pair operator annihilates each displayed term containing a g
factor because `(partial_u^2-1/4)g=0` (or the v analogue). Thus
`P F=P H` exactly. PR75 instead used `R=H-2*cosh(s)`, with
`P[2*cosh(s)]=0`; hence `P F=P R=P H`.

These equalities concern the complete two-variable differential operator.
They do not permit separately integrating or transforming growing cross
terms. The advantage of the present subtraction is that the complete F
and its required weighted derivatives are integrable in both variables.
PR75's M_j remain growing; nothing here retroactively justifies their
separate ordinary transforms. Equation (9)'s correction is the exact
remaining effect of recovering X from its decaying primitive's transform.

## Decision

No algebraic defect was found in the assigned formulas. This review
supports publication of the boundary repair and exact corrected target
as an audit. It supplies no independent all-height lower bound, no RH
implication from first-Laguerre positivity, and no escape from the matched
NS101 structural obstruction. The original nonlinear arithmetic estimate
remains open.
