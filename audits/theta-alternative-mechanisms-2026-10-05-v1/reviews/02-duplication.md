# Review 02 — complete duplication sectors do not supply a positive recurrence

**Decision: no candidate admitted.** The standard parity/character duplication
identities give an exact complete recurrence, but no independent estimating
step. In particular, an unrestricted positive-semidefinite matrix of the
completed three-sector Laguerre blocks is impossible, even for the original
theta function. This is a scoped rejection of one possible cone, not a
closure of nonlinear duplication methods or of the original target.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR75/77/78.**
What changes: a paper check of completed parity-sector recurrence and its
candidate matrix order; no new arithmetic sign input survives.

Reviewed baseline `221ceec9da825bdc787111447badad961860760a`; current AGENTS,
BRIEF, checkpoints, relevant register/frozen-input scopes, MISSING, PR75's
addition derivation, PR77 reviews 01–03 and PR78 stops. The coordinator's
full-register review is inherited, not a historical proof replay. Both
original-evidence recovery groups remain OPEN. No scan was run.

## Exact original sectors, without identifying the two moduli

Let `a=log(2)`, `D=(d_u^2-1/4)/4`, and, for `j=2,3,4`, define

```text
h_j(u)=exp(u/2)*theta_j(0 | i*exp(2u)),
phi_j=D h_j,                         X_j(r)=int_R phi_j(u)*exp(i*r*u)du.
phi_3=phi,                          X_3=X=xi(1/2+i*r)/2.
```

Use the exact integer, half-integer and alternating integer coefficients of
these theta constants. The fourth half-characteristic has
`theta_1(0|tau)=0`, so its completed sector is identically zero; it is not a
discarded nonzero contribution. All moduli have positive imaginary part.
The defining series and modular reflection conventions are in
[Kharchev–Zabrodin I, sections 2.1, 2.2 and 2.6](https://arxiv.org/html/1502.04603v2).
The identities below follow directly by partitioning even and odd integers,
not by applying a common-modulus addition theorem to unequal moduli.

```text
theta_3(0|i*x)=theta_3(0|4*i*x)+theta_2(0|4*i*x),
theta_4(0|i*x)=theta_3(0|4*i*x)-theta_2(0|4*i*x),       x>0.

phi_3(u)=[phi_3(u+a)+phi_2(u+a)]/sqrt(2),
phi_4(u)=[phi_3(u+a)-phi_2(u+a)]/sqrt(2).              (1)
```

Apply (1) separately at `u=s+t` and `u=s-t`. Their modulus ratio remains
`exp(4t)`; it has not been set to one. The operator D commutes with these
translations. At either real end the growing leading exponential of each
h_j is annihilated by D; modular reflection exchanges the 2 and 4 sectors.
Alternatively, solving (1) gives the exact completed identities

```text
phi_2(u)=sqrt(2)*phi(u-a)-phi(u),
phi_4(u)=sqrt(2)*phi(u+a)-phi(u).                      (2)
```

Thus all completed sectors and polynomially weighted derivatives decay
at both ends. All integrations below are ordinary complete integrals with
vanishing boundaries. No transform of an uncompleted growing h_j is used.
The characteristic sectors are signed; their positivity is not assumed.

For `j=0,1,2` set

```text
K_bc,j(t)=int_R s^j*phi_b(s+t)*phi_c(s-t)ds.
```

Applying (1) to both factors and translating `s` gives

```text
K_33,j(t)=(1/2)*sum_(b,c in {3,2}) sum_(l=0)^j
           binom(j,l)*(-a)^(j-l)*K_bc,l(t).           (3)
```

All four pair sectors and all lower moments remain. In particular the
second-moment recurrence contains `K_bc,2-2*a*K_bc,1+a^2*K_bc,0`.
Deleting the first or zeroth moment is not a positive recurrence for the
actual target `C=K_33,2`.

## Why the natural unrestricted matrix cone fails

Fourier transforming (2), with the displayed positive-exponent convention,
gives, at every real r,

```text
v=(X_3,X_2,X_4)^T=A*X,
A=(1, sqrt(2)*exp(i*a*r)-1, sqrt(2)*exp(-i*a*r)-1)^T.  (4)
```

The complete pair Fourier matrix is Hermitian:

```text
S_bc=4*int_R K_bc,2(t)*exp(2*i*r*t)dt
    =X_b'*conj(X_c')
      -[X_b''*conj(X_c)+X_b*conj(X_c'')]/2.
```

The factors follow from `u=s+t`, `v=s-t`, whose Jacobian is 1/2.
The mixed terms are included. In matrix notation,

```text
S=v'*v'^*-(v''*v^*+v*v''^*)/2 = V*B*V^*,
V=[v,v',v''],
B=[[0,0,-1/2],[0,1,0],[-1/2,0,0]].                  (5)
```

This tests one precise sufficient candidate: `S(r)>=0` in Hermitian matrix
order for every real r, with the exact original coefficients. Its (3,3)
sector would give `L1[X]>=0`, hence `J>=0`. A hoped-for method was to
propagate this matrix order through duplication/reflection, retaining all
sectors. That candidate already fails on the original data:

```text
det[A,A',A'']=-4*i*a^3,
det V=-4*i*a^3*X^3.
```

Whenever `X(r)!=0`, V is invertible. B has eigenvalues `1,1/2,-1/2`,
so congruence in (5) gives S two positive and one negative eigenvalue.
At a zero of X, `S=|X'|^2*A*A^*>=0`, including a multiple zero. No
division by X was needed, and the proposed all-height matrix condition
fails away from zeros regardless of the unknown sign of its original
diagonal entry. This is not a negative value of `L1[X]`.

Subtracting the known phase correction does not supply an alternative
estimate. Direct expansion of (4) yields

```text
S=L1[X]*A*A^*+X^2*B_A,
B_A=A'*A'^*-(A''*A^*+A*A''^*)/2.
```

The corrected matrix is positive semidefinite exactly when `L1[X]>=0`,
since A's first component is one. Calling that corrected matrix positive
just repeats the scalar target. No finite constant-matrix closure is
proposed or used.

## Infinite residue refinement and nonlinear duplication remain separate

Keeping finer sectors does not justify dropping their interactions. For
`m=2^k`, `0<=b<m`, define the complete residue series

```text
T_b,m(x)=sum_(n=b mod m) exp(-pi*n^2*x),
Phi_b,m=D[exp(u/2)*T_b,m(exp(2u))].

Phi_b,m=Phi_b,2m+Phi_(b+m),2m,
sum_(b=0)^(m-1) Phi_b,m=phi.                        (6)
```

The full additive-character representation is

```text
T_b,m(x)=(1/m)*sum_(l=0)^(m-1) exp(-2*pi*i*l*b/m)
                    *sum_n exp(2*pi*i*l*n/m)*exp(-pi*n^2*x).
```

No character is removed. For each fixed m, Poisson summation gives the
small-x leading term `1/(m*sqrt(x))`; D kills its corresponding exponential.
Together with the large-x series this justifies the completed transforms
at each finite level. It does not give a uniform-in-m norm bound: the dual
Gaussian scale includes `m^2*x`.

Writing `F_b,m=Fourier(Phi_b,m)`, (6) yields exact block aggregation of
the Hermitian quadratic S(F) from (5). The original scalar is the sum
of *all* entries. Positive diagonal bounds or separate sector tail bounds
leave the cross entries unestimated. An infinite-level argument would
need a specified cone or signed quadratic estimate, an invariant refinement
inequality in that order, and a uniform convergence bound in a norm
controlling two r derivatives. None has been supplied here. These are
additional open inputs, not consequences of the partition identity.

Likewise nonlinear Landen identities for squares of constants may define
a different state and cone; the rejection (5) does not exclude them.
Their differentiated complete pair comparison is currently unspecified.
The unequal-modulus identity in
[Kharchev–Zabrodin II, Proposition 3.1](https://arxiv.org/html/1510.02699v1)
requires positive-integer modulus multiples and positive imaginary part;
it matches `exp(4t)=n1/n2`, not all shifts via an unproved derivative limit.
It supplies no estimating cone in this audit.

## Controls, conditional transfer and stop

NS100 excludes a per-slice sign requirement; (3) retains the full integral.
NS101 changes the literal original lattice/IVP. However (2), (4) and (5)
can be formed from any smooth real even base kernel, including its mixture:
their algebra alone cannot distinguish it. The claimed sector-matrix
positivity fails directly on the original, so no numerical control command
is needed to reject it. Davenport–Heilbronn does not have the original
coefficient/completion hypotheses; NS74/83 concern different NB targets.
These mismatches are not passes of a sign screen.

A successful independent signed estimate for the complete recurrence would
give `L1[X]>=0`, equivalently
`J=(r^2+1/4)^2*(Y'^2-Y*Y'')+2*(r^2-1/4)*Y^2>=0`, at every real r.
First Laguerre alone is not RH. Here the unrestricted matrix estimate is
false and the corrected scalar estimate has no method; no candidate
survives. Budget: one bounded paper review, zero computation. Stop without
a row, thaw or version. The broader nonlinear arithmetic route stays open.

**Final wall check: Same open gap; the specific all-sector matrix cone is
rejected. Closest: PR75/77/78 and NS100/101.**
