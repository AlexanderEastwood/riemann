# Independent algebra review — nonlocal quotient and original tail

**Decision:** the precise positive-sech-power mixture proposed in review 01 is excluded by the original theta tail. Its nonlocal centering identity and conditional positivity transfer are correct. This is a rejection of that mixture class only: neither positive definiteness of the quotient itself nor the complete original first-Laguerre target is decided.

Reviewed baseline: `670864385024041d24612cf620054c1975473928`; scope commit `b914ac47e8006951a22d030e920d592243e7e0fe`. Read AGENTS, the current admission brief, proposer reviews 01 and 03, and PR77 review 01. The coordinator's conclusion-register review is inherited; I did not replay historical proofs or certificates. Both missing-original recovery groups remain OPEN. This was an independent paper derivation, with no numerical computation, scan, certification or imported theorem.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101 and PR76–77.** The specific new hypothesis examined is a positive Laplace representation for the conditional pair variance. Its rejection supplies a scoped admission decision, not an estimate for the still-open complete target.

## 1. Original series and complete saddle reduction

For nonnegative x, write the exact original kernel as

```text
phi(x)=sum_(n>=1) 2*pi^2*n^4*exp(9*x/2)
        *[1-3/(2*pi*n^2*exp(2*x))]*exp(-pi*n^2*exp(2*x)),
phi(-x)=phi(x).
```

Every displayed summand is positive for x>=0. For `Z=pi*exp(2*x)` tending to infinity, factoring out the n=1 term bounds the relative remainder by `C*exp(-3*Z)`: the polynomial factors n^4 are summable against the gaps `(n^2-1)*Z`. This observation applies uniformly on any region whose smallest Z tends to infinity.

Set `w(s,t)=phi(s+t)*phi(s-t)`, `M=int_R w ds`, `C=int_R s^2*w ds` and `k=C/M`. For t large, restrict initially to `abs(s)<=t/2`. Evenness replaces the second kernel argument by t-s, so both arguments are at least t/2. Put `A=2*pi*exp(2*t)`. The complete product is

```text
w(s,t)=4*pi^4*exp(9*t)*exp(-A*cosh(2*s))
       *[1-6*cosh(2*s)/A+9/A^2]
       *[1+O(exp(-c*exp(t)))].                    (1)
```

The factor in square brackets is the **full product of the two n=1 polynomial prefactors**, not a deleted correction. Indeed their separate factors are `1-3*exp(-2*s)/A` and `1-3*exp(2*s)/A`. Both remain uniformly positive on this central region when t is sufficiently large.

The complement is negligible even relative to the very small central mass. A complete theta bound of the form `phi(x)<=K*exp(-c0*exp(2*abs(x)))` follows by absorbing its polynomial factors into a slightly weaker exponential. Since

```text
max(abs(s+t),abs(s-t))=t+abs(s),
```

the zeroth and second moment tails over `abs(s)>t/2` are bounded by polynomial factors times `exp(-c1*exp(3*t))`. The central mass is of order `exp(9*t-A)/sqrt(A)`. Therefore the tail-to-central ratio is smaller than every inverse power of A. The absolute exterior tails of the model in (1) also have this property, even where that model's polynomial factor changes sign. It is consequently legitimate to extend **the saddle model's** integrals to the whole s-line. No original lattice summand has been unfolded to the whole line.

Now use `y=2*s` and then `y=x/sqrt(A)`. Up to order 1/A, the Gaussian integrand correction is

```text
exp(-A*cosh(y))=exp(-A)*exp(-x^2/2)
               *[1-x^4/(24*A)+O(A^-2*polynomial(x))],
1-6*cosh(y)/A+9/A^2 = 1-6/A+O(A^-2*polynomial(x)).
```

These expansions have controlled integrated remainders by splitting off a shrinking saddle neighborhood and using the exponential outside it. With standard centered Gaussian moments `E[x^2]=1`, `E[x^4]=3`, `E[x^6]=15`, the two model integrals are

```text
I_0=exp(-A)*sqrt(2*pi/A)*[1-49/(8*A)+O(A^-2)],
I_2=exp(-A)*sqrt(2*pi)*A^(-3/2)*[1-53/(8*A)+O(A^-2)],
k(t)=I_2/(4*I_0)+negligible
    =1/(4*A)-1/(8*A^2)+O(A^-3).                  (2)
```

The constant `-6/A` from the original polynomial prefactor contributes to both moment corrections and cancels from their ratio at this order. Retaining it is nevertheless necessary to validate the individual coefficients.

Finally, `z=log(cosh(2*t))` gives

```text
exp(2*t)=2*exp(z)-(1/2)*exp(-z)+O(exp(-3*z)),
Q(z)=k((1/2)*arcosh(exp(z)))
    =exp(-z)/(16*pi)-exp(-2*z)/(128*pi^2)+O(exp(-3*z)). (3)
```

Both proposed coefficients and the sign of the second coefficient check independently. No finite onset height is asserted.

## 2. Necessary-condition rejection

Suppose the proposed representation held:

```text
Q(z)=int_[0,infinity) exp(-a*z) dnu(a), z>=0,
nu finite and nonnegative.
```

The finite limit `exp(z)*Q(z)->c=1/(16*pi)` forces all mass onto `[1,infinity)`. Any positive mass in `[0,1-epsilon]` would make the limit infinite. Dominated convergence on `[1,infinity)` then gives `nu({1})=c`. Hence

```text
exp(z)*Q(z)=c+int_(1,infinity) exp(-(a-1)*z)dnu(a) >= c.
```

Equation (3) is strictly smaller than c for every sufficiently large z. This contradiction excludes this exact positive mixture. It does not exclude signed representations, other positive-definite families, or positive definiteness of k. None of those is automatically admitted as a replacement.

## 3. Volterra factors, boundaries and transfer

Let `b=phi'/phi`, `s=(u+v)/2`, `t=(u-v)/2` and

```text
V(s,t)=int_(-infinity)^s [a^2-k(t)]*w(a,t) da,
h(u,v)=V(s,t)/w(s,t).
```

Because `M>0`, k is defined everywhere. Exact centering gives both limits `V(-infinity,t)=V(+infinity,t)=0`. Moreover,

```text
partial_u+partial_v=partial_s,
partial_s(log w)=b(u)+b(v),
(partial_u+partial_v)h+[b(u)+b(v)]h=s^2-k(t).
```

Thus the residual is precisely `R_h(u,v)=k((u-v)/2)`. Symmetry follows from evenness of w and k in t. For every fixed pair of translates, the integration-by-parts flux is V at fixed t; both boundaries vanish. Absolute integrability of the differentiated flux follows from `(s^2-k)w`. No boundedness assumption on h itself is necessary for this identity.

Independently, M is an autocorrelation evaluated at twice its argument and is positive definite. If k were positive definite, the Schur product property would make `C=M*k` positive definite. Its complete theta decay makes C integrable; its Fourier transform would therefore be nonnegative. The checked factors are

```text
L1[X](r)=4*int_R C(t)*cos(2*r*t)dt,
J(r)=16*L1[X](r).
```

This conditional bridge retains zeros, mixed terms and the low-height correction. It proves only first-Laguerre positivity, not RH. The centering construction does not prove its missing positive-definiteness premise.

## 4. Independent cross-check of proposer 03

For fixed N, direct differentiation of `P_N=2*sum a_n*cos(v_n)`, with `v_n'=w_n` and `v_n''=theta''`, reproduces all three terms in its double-sum formula for `Q_d[P_N]`: the ratio coefficient `(w_n+w_m)^2-2*d`, product coefficient `(w_n-w_m)^2-2*d`, and `2*theta''*sin(sigma_nm)`. Its full remainder correction is the exact quadratic expansion. The Hardy normalization `X=-A*Z` gives `J=16*A^2*Q_d[Z]` with no division by a vanishing transform. Fixed-N differentiation followed by evaluation at the cutoff is the correct scope.

The phase-free coefficient budget `4*S_0*S_2~128*N` and leading ratio diagonal `(4/3)*log(N)^3` also check. They reject the stated absolute-budget argument, not the actual oscillatory sum or every Poisson method. A compatible pointwise signed comparison remains missing.

**Admission decision:** no algebraic repair changes either proposer's stop decision. Review 01's sufficient class is contradicted by original data; review 03 has not supplied its decisive signed estimate. Zero computation budget, no row, no thaw, no manuscript version. General nonlocal certificates and the original complete target remain open.
