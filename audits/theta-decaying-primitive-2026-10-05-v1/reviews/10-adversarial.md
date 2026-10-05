# Review 10: adversarial constants, exceptional points, and scope

**Disposition: PASS on the paper identities and the matched control margin;
CORRECTION to review-status wording; OPEN on the original all-height sign.**

Reviewed scientific baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208`
(PR75). Working HEAD when read: `edc65638cc5e761a0290b38d54ff0b9bac140697`.
I read AGENTS section 0, this audit's brief and derivation (1)-(12), the
relevant ZERO-GEOMETRY register entry, PR75's complete pair/boundary
derivation, PR74's complete-moment control and its adversarial review.
The parent performed the full register review; I did not independently
replay every historical proof or certificate. No scan or computation was
run. Source applicability was checked directly against
[Csordas, arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2), Definition
1.2 and Section 2. This file is internal review working material.

**Wall check: Same open gap.** Closest: NS100/101 and PR74/75. The change
repairs ordinary-transform domain accounting; no new original-arithmetic
lower bound has been supplied. An existing matched control defeats only
the stated generic primitive-positivity inference.

## 1. Positivity and the resolvent are not circular

The argument assumes the inherited complete original phi is positive;
it does not assume its Fourier transform has a Laguerre sign. This premise
can also be checked directly: for u>=0, put w_n=pi*n^2*exp(2u). Applying
the displayed differential operator termwise to the convergent theta
series gives

```text
phi(u)=sum_(n>=1) exp(u/2-w_n)*w_n*(2*w_n-3) > 0.
```

Here w_n>=pi>3/2; reciprocity gives the negative half-line. Thus using
positive phi in the Green representation does not import the desired
transform sign. The Green multiplier is correct: at a=1/2,
exp(-a*abs(u))/(2*a)=exp(-abs(u)/2), and the right side of the equation
is 4*phi. The difference of the two decaying solutions has the form
c_plus*exp(u/2)+c_minus*exp(-u/2); decay at both ends kills both
coefficients. No extra homogeneous or point-mass term can be retained.

The strict upper envelope in (4) uses the strictly positive theta tail in
(1), while its strict lower bound uses the Green representation. These
are separate justifications, and both hold at u=0. Reflecting the exact
smooth h is legitimate; reflecting a finite series here would not be the
same argument.

## 2. Pair constants and the polynomial correction

The bounds in (6) have the correct constants. The product envelope is
exp(-max(abs(s),T)), T=abs(t). Its central interval contributes
2*T*exp(-T) for A_0 and 2*T^3*exp(-T)/3 for A_2; the two exterior
intervals contribute 2*exp(-T) and
2*(T^2+2*T+2)*exp(-T), respectively.

The u=s+t, v=s-t Jacobian is 1/2. Including s^2=(u+v)^2/4 gives
the factor 1/8 for the second moment. Its square terms yield -2*Y*Y''
and its cross terms yield +2*Y'^2, proving the factor 1/4 in (8).
This relies on the stated even real f, not on arbitrary noneven kernels.

Independently expanding the product gives

```text
L1[p*Y]=p^2*L1[Y]+(p'^2-p*p'')*Y^2,
p=r^2+1/4,
p'^2-p*p''=2*(r^2-1/4).
```

Thus (9) and (10) are correct. The positive correction required inside
abs(r)<1/2 cannot be removed. The pair calculation neither estimates nor
changes this obligation.

Exceptional real points cause no division problem:

- p>=1/4 on the real axis, so division by p^2 in (10) is always safe.
- At Y=0, L1[Y]=Y'^2 and (9) still holds, including multiple zeros.
- At abs(r)=1/2 the correction vanishes; there is no singularity.
- At r=0, the stated moment expansion gives
  L1[Y](0)-8*Y(0)^2=256*m0*m2>0. This single point cannot be promoted
  to the all-height assertion.

The regularization changes the entire-transform class: the complex zeros
of p are genuine poles of Y, not removable singularities. In particular
X(+/-i/2)=1/4, so the residues of Y=4X/p are -i at i/2 and +i at -i/2.
On either boundary of the convergence strip one spatial tail has a
nondecaying oscillatory leading term. Its ordinary improper integral
fails even away from the pole; analytic continuation at those other
boundary points is a different operation. The draft distinguishes them.

## 3. The control margin survives the full corrected target

Write k=m2/m0>0 and r_beta=pi/beta. For beta^2>=pi^2*k,

```text
X(r_beta)>=m0/2,
L1[X](r_beta)/X(r_beta)^2<=6*k,
B_beta^2*L1[X_beta](r_beta)
  =L1[X](r_beta)-2*beta^2*X(r_beta)^2.
```

The negative coefficient is important: from X^2>=m0^2/4 one gets the
upper bound

```text
L1[X_beta](r_beta)
 <= -(beta^2-3*k)*m0^2/(2*B_beta^2)<0.
```

No inequality direction is reversed. Strictness follows from k>0 and
pi^2>3. The additional beta>=2 restriction is inherited from the control
family's zero-strip discussion, not needed for this moment inequality.
There is no claim here for the particular beta=2 member when its moment
condition is not established.

More explicitly, define the exact corrected-target difference

```text
D_beta(r)=L1[Y_beta](r)
          -2*(1/4-r^2)*Y_beta(r)^2/p(r)^2.
```

Equation (9), applied to the complete control, gives the full margin

```text
D_beta(r_beta)=16*L1[X_beta](r_beta)/p(r_beta)^2
 <= -8*(beta^2-3*k)*m0^2
       /(B_beta^2*p(r_beta)^2) < 0.
```

This is simply the existing control margin transferred through an exact
identity. It is not a new estimate for original X. It works whichever
side of abs(r)=1/2 contains r_beta.

The envelope is genuinely retained, rather than merely asymptotic:
triangle inequalities give
exp(u/2)*exp(-abs(u-beta)/2)<=exp(beta/2) for u>=0, and the other
shift contributes exp(-beta/2). The weighted sum is bounded by precisely
B_beta. For u>beta all three leading terms sum to B_beta, so the leading
tail coefficient is exactly one after division. Positivity and evenness
also survive. These facts do not require the original nonlinear IVP.

Constants in derivative and shifted-tail remainder bounds can depend on
the chosen beta. This should be explicit if any summary uses the word
"uniform": the draft proves each fixed control shares the hypotheses,
not a beta-uniform family of every derivative bound. There is no
contradiction between positive L1 at r=0 for each fixed beta and its
negative value at r=pi/beta as beta grows.

## 4. Scope and wording corrections

1. The opening statement "Review is local self-review, not a fresh
   independent review" is stale once the requested twelve-agent review is
   integrated. Replace it with the actual review scope, retaining the
   disclaimer that historical certificates were not replayed.
2. Do not label (10) an obtained lower estimate. It is exactly the
   unchanged first-Laguerre target. The explicit envelopes in (4)/(6) are
   valid bounds, but do not imply (10).
3. The control closes the inference from the enumerated shared primitive
   premises to (10), not the original theta question. It changes the
   single-lattice coefficients and the distinguished nonlinear IVP.
   The draft's final section correctly preserves that distinction.
4. The cited admissible-kernel hypothesis includes super-Gaussian decay of
   every derivative. Exponential f fails that requirement. This excludes
   direct use of that stated class, not every real-variable theorem or
   every possible meromorphic argument. First-Laguerre positivity alone
   remains weaker than an all-order real-zero criterion.

No fatal mathematical defect found in the bounded audit. No surviving
independent original-arithmetic sign method is identified by this review.
No scan, row, thaw, manuscript version or general route closure follows.
