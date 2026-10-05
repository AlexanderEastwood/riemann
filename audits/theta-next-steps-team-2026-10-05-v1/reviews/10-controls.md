# Reviewer 10 — original arithmetic and matched-control admission

**Decision: no specified next arithmetic lemma is admitted.** The original
single-lattice/Jacobi data genuinely distinguish the function from NS101.
They do not supply a signed estimate. Reviews 01–08 contain useful scoped
rejections, representations and conditional transfers, but no surviving
independently estimating hypothesis with a supplied arithmetic mechanism.

Reviewed baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34` (PR76),
refreshed by the coordinator. Read AGENTS's gates, current checkpoints,
NEXT_STEPS freeze, relevant map scopes, MISSING, PR76's derivation and
control review, PR72's Jacobi transfer, NS100/101 and reviews 01–08. The
coordinator's complete-register review is inherited. This is an admission
and scope audit, not historical proof replay. Both recovery groups stay OPEN.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76.** What
changes: assess the newly specified divided-difference, phase and factor
claims against their exact hypotheses. No new arithmetic assumption or
complete sign estimate survives. Their narrow failures do not close the
original Jacobi route.

## What actually distinguishes the original

The original is `Theta(v)=1+2*sum_(n>=1) exp(-pi*n^2*v)`: one integer-square
lattice, exactly the stated coefficients, and the fixed normalization.
NS101 instead uses

```text
Theta_beta(v)=[3*Theta(v)+exp(-beta/2)*Theta(exp(-2beta)*v)
                         +exp(beta/2)*Theta(exp(2beta)*v)]/B,
B=3+2*cosh(beta/2), beta>0.
```

Its slowest positive exponent is `kappa=pi*exp(-2beta)<pi`, with coefficient
`c=2*exp(-beta/2)/B`. PR72/76's normalized Jacobi-equation residual is
`c^2*kappa^4*(kappa^2-pi^2)*exp(-2*kappa*v)+o(exp(-2*kappa*v))`, hence is
eventually nonzero. It cannot solve the original equation or distinguished IVP:

```text
a'=(U+a^2-1)/2, U'=2U(a+chi), chi'=a*chi-U,
a(0)=chi(0)=0, U(0)=Gamma(1/4)^8/(64*pi^4), clock L=2u.
```

This is a concrete hypothesis mismatch. Identifying the solution uniquely
does not bound its oscillatory two-shift integral. Merely appending this
IVP to a generic argument without using it in the estimating step adds
no sign information.

Conversely, NS101 retains reciprocity, smooth positive even differential
kernel, complete pair calculus, and PR76's positive primitive, strict
exponential envelope and unit leading tail. With `k=m2/m0>0`, it satisfies

```text
L1[X_beta](pi/beta)
 <= -(beta^2-3k)*m0^2/(2B^2)<0,
beta>=max(2,pi*sqrt(k)).
```

This is the matched failure of the shared-property inference. It is not
inferred merely from off-axis zeros; the historical beta=2 member is not
separately decided. No control pass follows from its IVP mismatch.

## Transfer that an admitted hypothesis must actually complete

For the complete original object, retain

```text
p=r^2+1/4, X=pY/4,
J=p^2*(Y'^2-Y*Y'')+2*(r^2-1/4)*Y^2=16*L1[X],
C(t)=integral_R s^2*phi(s+t)*phi(s-t)ds,
L1[X](r)=4*integral_R C(t)*cos(2rt)dt.
```

An independently derived factorization
`C(t)=sum_j(g_j*tilde(g_j))(2t)`, with `g_j in L2` and
`sum_j ||g_j||_2^2<infinity`, would give positive definiteness, then
`J(r)>=0` for **every real r** by the continuous complete transform.
This transfer includes zeros and the negative correction when `|r|<1/2`;
it needs no quotient by Y. The same transfer is available for review 01's
residual-kernel certificate if every finite residual matrix is positive
semidefinite and all integration boundaries vanish.

Neither review supplies the requisite original-arithmetic factors or
residual. A square root of the unknown nonnegative Fourier transform,
positive definiteness of C itself, or equivalent phase monotonicity simply
assumes the missing sign. The first-Laguerre conclusion alone is not RH.

## Narrow checks of the new proposed walls

**01 — score divided differences.** Its necessary two-node determinant is
correct. For `b=phi'/phi`, `z=pi*exp(2u)`, the complete original tail gives
`b=-2z+9/2+O(1/z)` and `b'=-4z+O(1/z)`. With finite `kappa0=-b'(0)`,

```text
det D|_{0,u}=kappa0*(-b'(u))-b(u)^2/u^2
           =-4z^2/u^2+O(z)+O(z/u^2)<0 eventually.
```

This rejects the specified all-real-node positive-semidefinite score
kernel on the original object. It does not reject scalar score monotonicity,
every two-point invariant, local restricted inequalities, or arbitrary
integration corrections. Two-node success would not have supplied the
required all-matrix certificate anyway. This rejection is not itself an
estimate toward J.

**05 — phase and canonical systems.** For fixed epsilon>0,
`theta'=epsilon*J/[16*(X^2+epsilon^2*X'^2)]` wherever its phase exists.
Thus its sign is exactly the old target. At common zeros the denominator
vanishes; the undivided J identity remains valid. Requiring
`-epsilon*X'/X` to be Herglotz in the upper half-plane is stronger: its
analyticity already excludes upper-half-plane zeros of X. Neither that
requirement nor an unspecified positive Hamiltonian is an independent
arithmetic input. This does not exclude an independently constructed,
correctly identified arithmetic canonical system.

**06 — factor classes.** Smooth even C has `C'(0)=0`, `C(0)>0` and tends
to zero, contradicting convexity on the entire positive half-line.
Positive triangular mixtures are therefore excluded. Its double-exponential
upper tail also contradicts every nonzero positive Gaussian scale mixture:
some finite parameter interval has mass m>0, forcing `C(t)>=m*exp(-At^2)`.
Both arguments are sound for precisely those classes. Neither excludes
general autocorrelations, eventual convexity, signed mixtures, or positive
definiteness. Review 06 explicitly preserves those limits.

## Controls and stop budget

NS100 is an original-kernel counterexample to per-slice positivity, not
to the complete integrated C. Davenport–Heilbronn changes coefficients,
conductor/completion and Jacobi data; positivity of its differential kernel
and this primitive envelope has not been established here. Generic calculus
may apply, but it is not a matched instance of the full original premises.
A mismatch in either control cannot certify admission.

Reviews 02–04 and 07–08 leave, respectively, a generator inequality, signed
lattice regrouping, local prime-plus-residue bound, unbounded-degree
critical-value estimate, and original/reference comparison unprovided.
Those are missing inputs, not newly specified methods for obtaining them.

**No-candidate stop:** zero computation/scan budget and no additional
open-ended proof allocation. Only upon receiving one explicit estimating
formula, allow at most **two hours of paper admission**: establish its
original-arithmetic step, full conditional transfer and matched controls.
Success admits that concrete lemma for proof work; proving it with the
transfer would establish J only. Failure stops that formula without an
adjacent variation. No row, thaw, manuscript version, commit or outreach.

**Final wall check: Same open gap.** RH, G2 and the cofinal signed-arithmetic
lower bound remain open.
