# Two-modulus theta addition: applicability and boundary audit

Reviewed baseline: `1f09dd8a8587506ea83c0c48573d225b7a323bc1` (PR74).
**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR72–74.**

This is a paper applicability audit, with local algebraic self-review only.
No numerical or symbolic scan, new sign candidate, NS row, thaw or manuscript
version. The complete 104-node conclusion register and 14 input demands were
reviewed; that is not a historical proof/certificate replay. Both original
evidence recovery groups remain OPEN.

Question: can a theta addition identity turn the original two-shift pair
into an independently estimable nonnegative transform? The dependency would
have to reach `L1[X](r)>=0` for EVERY real r, retaining the complete pair.
This first Laguerre condition alone is not RH. A theta identity without a
signed estimating step does not meet that dependency.

## 1. Match the variable before importing an addition formula

Use the definitions

```text
Theta(x) = sum_(n in Z) exp(-pi*n^2*x), x>0,
h(u) = exp(u/2)*Theta(exp(2u)),
D_u = (partial_u^2-1/4)/4,
phi(u) = D_u h(u),
X(r) = integral_R phi(u)*exp(i*r*u) du = xi(1/2+i*r)/2.
```

Theta reciprocity makes h even. The complete phi is positive, smooth, even
and rapidly decaying with all derivatives. For the ordinary two-variable
Jacobi function, `Theta(x)=theta_3(0 | i*x)`. Hence our pair has

```text
tau_+ = i*exp(2s+2t),  tau_- = i*exp(2s-2t),
elliptic arguments both zero, tau_+/tau_-=exp(4t).
```

[Kharchev–Zabrodin I, arXiv:1502.04603v2](https://arxiv.org/html/1502.04603v2),
Sections 3.1–3.3 and 4.2, distinguishes the elliptic variables from the
modulus. Its addition identities use a common modulus; its basic bilinear
identities use tau and 2*tau. Substituting s+t and s-t as elliptic variables
would change the object, rather than use an identity for our factors.

There are also valid unequal-modulus identities. [Kharchev–Zabrodin II,
arXiv:1510.02699v1](https://arxiv.org/html/1510.02699v1), Proposition 3.1,
uses moduli n1*tau and n2*tau, positive integers n1,n2, and retains a sum
over residue classes modulo n1+n2. These hypotheses match exp(4t)=n1/n2.
The common-modulus mismatch therefore does NOT exclude all addition methods.
Rational ratios are dense, but an estimate on those ratios would still need
the same sign or a controlled limiting error; the identities alone provide
neither. No uniform complexity bound or derivative transfer in t is imported.

Special loci also do not settle the problem. At t=0 the two moduli agree;
at s=0 they are reciprocal. The latter is exactly a slice of the sort for
which NS100 already prohibits an unconditional positive-slice proof for the
actual original kernel. Neither locus estimates the complete s integral.

## 2. The exact identity that applies for all real shifts

For arbitrary real s,t let x=exp(2s). Absolute convergence of the TWO
Gaussian series at fixed s,t permits the bijective reindexing

```text
k=n+m, l=n-m,
(n,m) in Z^2 <=> (k,l) in Z^2 with k=l (mod 2).

Theta(x*exp(2t))*Theta(x*exp(-2t))
 = sum_(k=l mod 2) exp[-pi*x/2 *
       {cosh(2t)*(k^2+l^2)+2*sinh(2t)*k*l}].             (A)
```

Indeed n=(k+l)/2 and m=(k-l)/2, which gives the quadratic form printed
in (A). No factor of 2 is lost: the map is a bijection onto the parity
sublattice, not onto all of Z^2. Both Gaussian factors, all lattice points,
and both parity cosets remain.

The real quadratic matrix

```text
Q_t = [[cosh(2t), sinh(2t)],
       [sinh(2t), cosh(2t)]]
```

has eigenvalues exp(2t), exp(-2t), and determinant 1. Thus the series
converges for every fixed real s,t, including t=0. Splitting into
(k,l)=2(p,q)+epsilon*(1,1), epsilon=0,1, expresses (A) as the sum of two
genus-two theta constants with Riemann matrix `2*i*x*Q_t` and upper
characteristics `(epsilon/2,epsilon/2)`, lower characteristic zero.
This uses the standard multidimensional series definition in the second
source; it introduces no positivity theorem in the parameter t.

At t=0 the cross term vanishes and the formula reduces to the check

```text
Theta(x)^2 = theta_3(0 | 2*i*x)^2 + theta_2(0 | 2*i*x)^2. (B)
```

For t!=0 the coupling cannot be dropped from (A). For example, k=l=1
corresponds to the original point (n,m)=(1,0); its exponent is
`-pi*x*exp(2t)`, not `-pi*x*cosh(2t)`. This is an exact one-term check,
not a sampled computation. Diagonalizing Q_t over the reals recovers the
original unequal-modulus factors and must also transport the lattice.

Positive definiteness of Q_t concerns the lattice variables k,l. The
required positive definiteness of C concerns matrices formed from arbitrary
real translation differences t. These are different properties. Neither
the dimension, the determinant, nor positivity of each real Gaussian term
supplies the latter.

## 3. Keep the differential kernel and its complete boundaries

Write H(s,t)=h(s+t)*h(s-t). The original pair is obtained by differentiating
the complete object, not by using H as a substitute for phi_+*phi_-:

```text
phi(s+t)*phi(s-t) = (1/256)*P H(s,t),

P = partial_s^4 - 2*partial_s^2*partial_t^2 + partial_t^4
    -2*partial_s^2 -2*partial_t^2 +1.                   (C)
```

To check the factor, each u derivative becomes
`partial_(u+)=(partial_s+partial_t)/2` or
`partial_(u-)=(partial_s-partial_t)/2`. The two original operators are
`((partial_s+partial_t)^2-1)/16` and
`((partial_s-partial_t)^2-1)/16`; their product is P/256.
As a second check, testing on exp(alpha*(s+t)+beta*(s-t)) gives multiplier
`(alpha^2-1/4)*(beta^2-1/4)/16` in either representation.

The unregularized integral of s^2 H diverges, because H~exp(|s|) at both
s ends for fixed t. Instead define the exact smooth subtraction

```text
R(s,t)=H(s,t)-2*cosh(s),
M_j(t)=integral_R s^j*R(s,t) ds, j=0,2.               (D)
```

P annihilates 2*cosh(s), since on a t-independent function it is
`(partial_s^2-1)^2`. This is a smooth subtraction, not exp(|s|) with its
distributional derivatives. For t in each compact interval, complete
theta reciprocity and its Gaussian tails give

```text
R(s,t) = -exp(-|s|) + O_T(exp(c_T*|s|-d_T*exp(2*|s|))),
```

for suitable finite c_T and positive d_T as |s|->infinity, and the needed
derivatives have the same integrable character. Thus (D), differentiation
under its integral, and the following s integrations by parts are valid:

```text
integral_R s^2*R_ss ds = 2*M_0,
integral_R s^2*R_ssss ds = 0.
```

Consequently the COMPLETE associated kernel is

```text
C(t) = integral_R s^2*phi(s+t)*phi(s-t) ds
     = [(partial_t^2-1)^2*M_2(t)
        -4*(partial_t^2+1)*M_0(t)]/256.               (E)
```

These are supporting identities and an explicit boundary treatment, not a
lower bound. The original single-lattice coefficients enter H and its
tail estimates; the differential calculus itself is generic.

There is a second boundary issue if (E) is Fourier transformed. Even after
the s regularization, M_0 and M_2 must not be Fourier transformed separately
as ordinary integrable functions without a new justification. For example,
h(u)>=exp(|u|/2) follows from reciprocity and Theta(x)>=1 at positive x.
For t>=0 this yields H(s,t)>=exp(max(|s|,t)). Integrating the resulting
lower bound for R first on |s|<=t and then on |s|>t proves

```text
M_0(t) >= 2*(t-1)*exp(t), t>=0.                     (F)
```

Both lower integrals converge at each fixed t: the exterior is -exp(-|s|).
In detail their sum is `2*t*exp(t)-4*sinh(t)-2*exp(-t)`, which equals (F).
Thus M_0 grows rather than decays at large t. The COMPLETE bracket in (E),
by its original definition, equals 256*C and is rapidly decaying. Its
cancellations cannot be replaced by ordinary Fourier transforms of the
separate growing moments. A distributional transform, if chosen, would
require its own domain/boundary accounting and still no sign is automatic.

The subtraction is also signed: at (s,t)=(0,0),
`R=Theta(1)^2-2<0`, since `Theta(1)<=1+2/(exp(pi)-1)<6/5`.
At s=0, R(0,t)>=exp(t)-2>0 for t>log(2). This does not assert a negative
C or L1; it prevents simply carrying termwise positivity through the
regularization.

## 4. Exact remaining dependency and matched controls

The target in these coordinates is still

```text
integral_R [(partial_t^2-1)^2*M_2
             -4*(partial_t^2+1)*M_0]*cos(2*r*t) dt >= 0,
for every real r.                                    (G)
```

The complete bracket is kept inside the integral. By (E) and PR73 this
integral is 64*L1[X](r). There is no division by a zero, no parity/source
restriction on the translates, and no assertion that (G) is an independent
estimate. No method controlling the signed cancellation in (G) was obtained.

- **NS100:** its negative original slice excludes replacing (G) by sign of
  each slice. It does not exclude the integrated statement.
- **NS101 / PR74:** the shifted reciprocal mixture retains generic
  differential/associated-kernel calculus and smooth reciprocal completion,
  while directly failing L1 in PR74's complete-moment parameter range. It
  changes the original one-lattice coefficients and Jacobi IVP. The literal
  single-lattice formula (A) is therefore not its unchanged formula; applying
  Gaussian reindexing separately to its mixture terms is only generic algebra.
  No new hypothesis containing original arithmetic plus a signed estimate
  has been supplied here. This mismatch is not a control pass.
- **Davenport–Heilbronn:** different coefficients, conductor and completion;
  no match to the exact original Theta/IVP premises. Generic differential
  algebra alone cannot distinguish it; no applicable sign proof is claimed.
- **PR73/74:** no fixed reflected prefix or drift quotient is used. Avoiding
  their scoped exclusions does not estimate (G). PR74's smooth approximation
  errors and different Bessel margin cannot be substituted for a bound on (G).
- **NS74/83:** NB target/rate hypotheses do not match this theta identity.

## 5. Disposition

**No sign candidate survives admission.** The checked addition formulas
do not supply a comparison for the actual two moduli. The valid lattice
identity and completed moment formula retain exactly the signed comparison
already open. Do not run a lattice, residue-class, dimension or height scan
on the strength of these representations.

Success of a future original-arithmetic estimating inequality for (G), or
the original pair directly, would establish the first-Laguerre target only.
Failure of the literal common-modulus substitution says nothing against
every unequal-modulus or nonlinear method. No broad no-go result is claimed.
Budget used: one bounded two-source applicability and paper-boundary audit,
one findings PR; zero further computation budget without a concrete method.
No external outreach. RH, G2 and the cofinal signed-arithmetic lower bound
remain open.
