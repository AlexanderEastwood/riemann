# Review 04 — independent heat and duplication algebra check

**Decision: the displayed identities check, but neither note supplies an
independent arithmetic estimating technique.** The heat comparison retains
an adverse source. The unrestricted three-sector Hermitian cone is false
away from zeros of the original X. These conclusions concern the stated
mechanisms, not every heat, duplication or nonlinear Jacobi argument.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–78.**
What changes: independent checking of the auxiliary heat clock, completed
sector recurrence and their conditional transfers. No original signed
estimate is obtained. A conjectural lemma need not already be proved to
qualify, but neither an equivalent target nor a false sufficient condition
provides an estimating method.

Reviewed baseline: `221ceec9da825bdc787111447badad961860760a`; scope commit:
`b5147e82803cccdb641bcb611b3c90c3c76cf51e`. I read AGENTS, the new BRIEF and
review record, reviews 01/02, PR77's transport review and the relevant
frozen-input and missing-evidence scopes. The coordinator's full-register
review is inherited; this is an independent algebra/dependency check, not
a replay of all historical proofs or computations. Both original-evidence
recovery groups remain OPEN.

## Heat: normalization, sign and complete transfer

Keep the original even kernel phi and the complete integrals

```text
H_a(r)=int_R exp(a*u^2)*phi(u)*exp(i*r*u)du,
Q_a=H_a'^2-H_a*H_a'',   S_a=H_a''^2-H_a'*H_a'''.
```

All primes mean r derivatives. Double-exponential decay justifies every
displayed differentiation and convolution on compact real a intervals.
These functions are Schwartz on the real r line. The Gaussian parameter
a is not the original nonlinear Jacobi clock L=2u.

The literature normalization really is

```text
Phi_lit(v)=phi(2v),
H_a(r)=4*H_lit,4a(2r),
Q_a(r)=64*L1[H_lit,4a](2r).
```

The factor four follows from evenness followed by u=2v; both derivative
scale factors must also be retained. Thus A=1/8 corresponds to literature
parameter 1/2. The real-zero endpoint used in review 01 is supported by
[Polymath, arXiv:1904.12438v2, equations (1), (3), (4) and introduction](https://arxiv.org/html/1904.12438v2).
That endpoint's real entire order-one factorization gives Q_A>=0,
including multiple zeros. No assertion of a strict lower margin is needed.
The source supplies reality toward larger literature parameter; it does
not give preservation in the reverse direction required here.

Direct differentiation gives

```text
partial_a H_a=-H_a'',
Q_a''=H_a''^2-H_a*H_a'''',
partial_a Q_a=-Q_a''+2*S_a.
```

With tau=A-a the source therefore enters with a minus sign. The solution
formula is

```text
Q_0=G_A*Q_A-2*int_0^A G_a*S_a da,
G_a(r)=(4*pi*a)^(-1/2)*exp(-r^2/(4*a)),  G_0*F=F.
```

The convolution parameter in the integrand is a, not A-a: changing back
from the Duhamel time tau gives exactly that orientation. Consequently an
all-real-r upper estimate for the integrated source by G_A*Q_A would
prove Q_0>=0 and J=16*Q_0>=0. The stated comparison is itself equivalent
to this target. An independently useful coefficient estimate for the
source could qualify, but none is supplied.

The elementary favorable-source substitute S_a<=0 is false for the
original kernel, because evenness gives

```text
S_a(0)=H_a''(0)^2>0.
```

The alternative bound S_a<=b(a,r)*Q_a with locally bounded b hides an
extra multiplicity restriction. At a zero r0 of H_a of order m>=2, put
x=r-r0 and H_a=c*x^m+O(x^(m+1)). Then

```text
Q_a=m*c^2*x^(2*m-2)+O(x^(2*m-1)),
S_a=m^2*(m-1)*c^2*x^(2*m-4)+O(x^(2*m-3)),
S_a/Q_a ~ m*(m-1)/x^2.
```

Such a locally bounded comparison cannot include that zero. This is not
a claim that the original X has a multiple zero; it identifies an
unproved simplicity consequence of the proposed bound. Singular-potential
versions need their own domain and transfer analysis.

I also checked the complete double-integral signs. Gaussian convolution
contributes exp(-a*(u+v)^2), combining with the two original deformation
weights to give exp(-2*a*u*v). The Q and S multipliers are, respectively,
`(u-v)^2/2` and `-u*v*(u-v)^2/2`. Their source sign changes with u*v;
the remaining phase is exp(i*r*(u+v)). Integrating the a weight in the
Duhamel formula reconstructs Q_0 exactly, rather than exposing a new
positive sum. A fixed phase-free absolute budget cannot suffice when its
comparison endpoint tends to zero as |r| increases. This only excludes
that crude budget, not estimates retaining arithmetic cancellation.

## Duplication: completed sectors and boundary terms

Use a separate symbol ell=log(2) and

```text
D=(d_u^2-1/4)/4,
h_j(u)=exp(u/2)*theta_j(0|i*exp(2u)), phi_j=D h_j,
X_j(r)=int_R phi_j(u)*exp(i*r*u)du.
```

The theta conventions in [Kharchev–Zabrodin I, arXiv:1502.04603v2](https://arxiv.org/html/1502.04603v2)
agree with the note: theta2 sums half-integers; theta4 alternates the
integer sum; theta1 vanishes at zero argument. Partitioning integers by
parity directly gives

```text
theta3(x)=theta3(4*x)+theta2(4*x),
theta4(x)=theta3(4*x)-theta2(4*x),
phi2(u)=sqrt(2)*phi(u-ell)-phi(u),
phi4(u)=sqrt(2)*phi(u+ell)-phi(u).
```

Here theta_j(x) abbreviates theta_j(0|i*x). Translation commutes with D.
The last two identities prove complete decay of the signed sectors,
including all polynomial moments and derivatives, without Fourier
transforming the growing uncompleted h_j. There are no omitted boundary
contributions. At u=s+t and u=s-t the two moduli stay unequal; parity
decomposition does not replace either one by the other.

In the recurrence for `K_bc,j(t)=int s^j phi_b(s+t)phi_c(s-t)ds`, the
translation is s_new=s+ell. Hence the moment factor is
`(s_new-ell)^j`. The second-moment recurrence must retain
`K_bc,2-2*ell*K_bc,1+ell^2*K_bc,0`, summed over all four pair sectors.
Those signs and the factor 1/2 in review 02 check. The recurrence alone
is an identity, not an order-preserving estimate.

## Hermitian block: determinant and exact scope

The positive-exponent Fourier convention gives

```text
v=(X3,X2,X4)^T=A*X,
A=(1,sqrt(2)*exp(i*ell*r)-1,sqrt(2)*exp(-i*ell*r)-1)^T.
```

The phi sectors are real, although their transforms need not be real.
The change of variables from (s,t) to (u,v) has Jacobian 1/2, yielding

```text
4*int K_bc,2(t)*exp(2*i*r*t)dt
 = X_b'*conj(X_c')-(X_b''*conj(X_c)+X_b*conj(X_c''))/2.
```

Thus the matrix S in the note is Hermitian and has the stated factorization
`S=V*B*V^*`, `V=[v,v',v'']`, with B eigenvalues 1,1/2,-1/2. Since the
first row of `[A,A',A'']` is (1,0,0), its determinant reduces immediately
to the lower 2-by-2 block:

```text
det[A,A',A'']=-4*i*ell^3,
det V=-4*i*ell^3*X^3.
```

Congruence therefore proves inertia (2 positive, 1 negative) wherever
X!=0. This directly excludes S>=0 as an all-height sufficient condition.
At X=0, v=0 and S=|X'|^2*A*A^*, so the note also handles simple and
multiple zeros correctly. The negative eigenvalue away from zeros says
nothing by itself about the original theta3 diagonal L1[X].

Finally the mixed X*X' terms cancel in the expansion, giving

```text
S=L1[X]*A*A^*+X^2*(A'*A'^*-(A''*A^*+A*A''^*)/2).
```

Subtracting this explicit phase term leaves a rank-one matrix whose
positivity is exactly L1[X]>=0. That correction does not estimate the
scalar. The same algebra works for any real base X; original theta
arithmetic has not produced an extra signed inequality at this step.

## Disposition

No material algebra error found in reviews 01/02. Their stops are justified:
heat needs an independent accumulated-source estimate, while duplication
needs a different, specified signed comparison than the excluded full
matrix cone. A nonlinear or infinite-level scheme would additionally
need its invariant inequality and complete derivative-controlling limit;
the identities do not supply them. NS101 shares the generic algebra but
not the literal original coefficients/IVP; that mismatch is not a pass.
NS100's per-slice obstruction is not enlarged here. NB rate controls do
not transfer to this theta target.

**Final wall check: Same open gap.** Only the stated all-sector cone and
favorable-source shortcut are rejected. First Laguerre, RH, G2 and the
cofinal arithmetic bound remain open. One paper review; zero numerical
scans, interval certificates, new rows, versions or outreach. Only this
assigned internal note was written.
