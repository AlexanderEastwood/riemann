# Review 11 — source transfer, normalization and quantifiers

**PASS for the draft's source-scope conclusion; OPEN for equation (10).**
Reviewed scientific baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208`
(PR75), with scope scaffold `edc65638cc5e761a0290b38d54ff0b9bac140697`.
Read AGENTS section 0 and proposal gate, REVIEW_BRIEF, derivation equations
(1)-(12), the applicable ZERO-GEOMETRY register scope, PR72's source-chain
note, PR74's arXiv-method review, and the primary arXiv passages cited below.
The parent performed the full 104-node review. I did not replay historical
proofs or external interval certificates. No scan or new candidate proof.

**Wall check: Same open gap.** Closest: NS100/101 and PR74/75. The primitive
repairs the transform domain but does not estimate the signed expression.

## Bounded source findings

[Csordas 1309.0055v2](https://arxiv.org/html/1309.0055v2): Definition 1.2(v)
requires super-Gaussian decay of every derivative. Theorem 3.5 gives
admissibility of associated kernels, not their positive definiteness;
Theorem 3.7 needs every associated order for its real-zero criterion.
Remark 2.1 and Theorem 4.2 concern moment/Turan consequences. Theorem 4.5
applies to the original theta kernel. Open Problem 4.7 asks first-Laguerre
positivity at every real height. Open Problem 4.14 concerns a different,
real-kernel second concavity. These are distinct quantified statements.

[Planat–Sole 2608.19160v1](https://arxiv.org/html/2608.19160v1), Theorem 1.1
and Section 7, state second-level concavity for
`s(t)=Phi(sqrt(t))`, `t>0`, with a double-Turan consequence for normalized
coefficients. Its nonlinear Jacobi phase space is in the real kernel
coordinate. This is not a claimed all-frequency first-Laguerre inequality
for the Fourier transform. I checked statement/scope here, not its finite
certificate implementation.

## Independent application to this draft

The following calculations use the draft's definitions. They prevent an
otherwise tempting import of a theorem with the wrong object or clock.

1. **The primitive is outside the stated entire-transform class.** Equation
   (1) gives `f(u) ~ exp(-abs(u)/2)`. Consequently no `epsilon>0` makes
   `f(u)=O(exp(-abs(u)^(2+epsilon)))`. This already fails the decay premise;
   deciding the separate monotonicity premise is unnecessary. Equation (5)
   gives actual poles of `Y=4X/(r^2+1/4)` at `r=+/-i/2`, because
   `X(+/-i/2)=1/4`. So the mismatch is substantive, not notation.
   Equation (8), however, follows by ordinary integrals and remains valid.

2. **An associated-kernel identity is not its sign estimate.** With the
   draft's `A_2`, equation (8) gives
   `L1[Y](r)=4*integral A_2(t)*cos(2*r*t) dt`. Positivity of `A_2(t)`
   does not assign a sign to this cosine integral. Even establishing the
   stronger `L1[Y]>=0` would prove (10) only on `abs(r)>=1/2`; inside that
   interval the correction is positive and must be estimated. A theorem
   for the original `phi` does not automatically become one for its
   nonlocal resolvent `f=4*G_(1/2)*phi`.

3. **Correct theta normalization.** Comparing the explicit theta series
   gives `phi(u)=Phi(u/2)`. If `H(x)=integral_0^infinity Phi(v)*cos(x*v) dv`,
   then direct substitution and evenness give

   ```text
   X(r)=4*H(2*r),
   L1[X](r)=64*L1[H](2*r),
   C(t)=8*K_1(t/2),
   K_1(v)=integral_R w^2*Phi(w+v)*Phi(w-v) dw.
   ```

   Thus the whole-height question matches after positive scaling. It
   does not become the real-coordinate curvature question merely because
   both use the notation `L1`.

4. **Coefficient/origin versus arbitrary frequency.** Let
   `F_c(z)=H(i*sqrt(z))`. Since H is even, this is unambiguous through its
   entire power series. For `x!=0`, direct chain rule gives

   ```text
   H(x)=F_c(-x^2),
   L1[H](x)=4*x^2*L1[F_c](-x^2)
             +2*F_c(-x^2)*F_c'(-x^2).
   ```

   Inequalities involving derivatives of `F_c` at zero do not bound this
   expression at every `-x^2<=0`. Even an all-real-argument lower bound
   for `L1[F_c]` alone would leave the displayed product term. The
   primitive's equation (10) has the analogous explicit correction.
   No missing pointwise or signed-transform comparison is supplied by
   restating coefficient inequalities.

## Source presentation caution: do not copy a half-line factor

In the retrieved HTML, the source definitions and coefficients are:

```text
(3.11): F(x)=integral_R exp(i*t*x)*varphi(t) dt.
(3.7):  K_n(t)=integral_R varphi(s+t)*varphi(s-t)*s^(2n) ds.
(3.14): L_n(x;F)=[2*2^(2n)/(2n)!]*integral_R K_n(t)*cos(2*x*t) dt.
(4.1):  H(x)=integral_0^infinity Phi(t)*cos(x*t) dt.
(4.6):  K_n(t;Phi)=integral_R Phi(s+t)*Phi(s-t)*s^(2n) ds.
(4.7):  L_n(x;H)=[2*2^(2n)/(2n)!]*integral_R K_n(t)*cos(2*x*t) dt.
```

The HTML's last coefficient repeats the full-line convention despite the
displayed half-line H. I record this as a source-presentation normalization
caution, not a finding that the underlying mathematical theorem is defective.
I have not checked PDF/source versions or an erratum. The draft does not
depend on the ambiguous displayed coefficient.

An independent check suffices. Put `F=2H`, the full-line transform. Then
`L1[F]=4*L1[H]`, while a direct pair change of variables gives
`L1[F](x)=4*integral_R K_1(t)*cos(2*x*t) dt`. Therefore the half-line
version is `L1[H](x)=integral_R K_1(t)*cos(2*x*t) dt`. Combined with the
scaling above, it gives exactly the draft's
`L1[X](r)=4*integral_R C(t)*cos(2*r*t) dt`. No draft factor correction
is required. Any later source quotation should name the transform
convention and rederive its prefactor.

## Disposition

The source exclusion in Section 3 is correctly narrow. It does not prohibit
using elementary Fourier or resolvent identities for f, and does not
exclude a future inequality derived from the distinguished original theta
trajectory. The draft retains the actual correction, all heights and zeros.
The existing NS101 family matches the positive-primitive/envelope/tail
properties but changes the original coefficients and IVP; no source theorem
checked here replaces that lost hypothesis with an all-height estimate.

No arXiv theorem reviewed here establishes (10) from the proposed premises.
The missing step is an independent bound for its complete corrected
expression, using original theta arithmetic or the distinguished IVP.
This is a bounded applicability check, not an exhaustive search or an
assertion about the current global literature status. No new research row,
thaw, manuscript version, RH/G2 assertion, certificate or scan follows.
