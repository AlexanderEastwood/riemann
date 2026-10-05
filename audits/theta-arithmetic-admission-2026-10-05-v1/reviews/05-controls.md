# Reviewer 05 — matched controls, arithmetic hypotheses and source audit

**Decision: no candidate admitted; no unresolved MAJOR issue found in the three stop decisions.** The nonlocal attempt has a concrete sufficient estimate and a complete transfer, but its proposed positive sech-power representation fails a necessary condition on the original kernel. The divisor and Riemann–Siegel attempts retain correct arithmetic identities but supply no separate signed estimating step. Their failure to qualify is not a demand that an admitted conjecture already be proved.

Reviewed baseline: `670864385024041d24612cf620054c1975473928`, local scope commit `b914ac47e8006951a22d030e920d592243e7e0fe`. Read AGENTS, the admission brief and review record, all three proposer notes, PR77's factorization/control findings, the relevant continuation and missing-evidence records, and the two control scripts as source only. The coordinator's full-register review is inherited; historical proofs and numerical certificates were not replayed. Both original-evidence recovery groups remain OPEN.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76–77.** What changes: a specific sufficient nonlocal mixture class is assessed on the original coefficients, and two complete arithmetic regroupings are checked for genuine estimating content. The narrow mixture rejection does not settle general positive definiteness or the complete first-Laguerre inequality.

## 1. Nonlocal construction: the object and the rejected class

The distinction between the complete pair C and its normalized second moment is essential:

```text
w(s,t)=phi(s+t)*phi(s-t),
M(t)=int_R w(s,t)ds, C(t)=int_R s^2*w(s,t)ds,
k(t)=C(t)/M(t), M(t)>0.
```

The positivity of the denominator follows from the original strictly positive real kernel, not from Fourier positivity. The centering construction gives `partial_s V=(s^2-k(t))*w` and zero flux at both infinite endpoints for each fixed t. It therefore supplies the claimed residual `k((u-v)/2)` exactly. It does not prove that residual positive definite.

The conditional transfer is nevertheless complete: M is a scaled autocorrelation of phi; if k is positive definite, their product C is positive definite. C is integrable and its Fourier transform is continuous, so nonnegative transform density gives `L1[X](r)>=0` at every real r, including zeros. This uses the full C and automatically retains PR76's low-height correction in J. No additional sign estimate is hidden in the transfer.

I independently checked the proposed sufficient class and its rejection. For a>0, elementary beta integration gives

```text
int_R sech(2t)^a*exp(i*r*t)dt
 =2^(a-2)*Gamma(a/2+i*r/4)*Gamma(a/2-i*r/4)/Gamma(a).
```

This is positive; a=0 is the constant positive-definite member. Thus a finite positive mixture would indeed suffice. PR77's positive-Gaussian-mixture obstruction concerned C, whose decay is double exponential; it does **not** decide this sech-power mixture of the different quotient k.

For the original n=1 tail, write A=2*pi*exp(2t). Factoring both summands gives exactly

```text
w(s,t) ~ 4*pi^4*exp(9t)*exp(-A*cosh(2s))
         *[1-6*cosh(2s)/A+9/A^2].
```

The coefficients 6 and 9 are correct. On the proposer's growing central interval the other lattice terms are uniformly exponentially smaller; outside it the complete tails are negligible relative to the central integral. With `y=2s=x/sqrt(A)`, the first Gaussian correction is `-6-x^4/24`. The zeroth and second moments therefore have corrections `-49/8` and `-53/8`, giving

```text
k(t)=1/(4A)-1/(8A^2)+O(A^-3).
Q(z)=k(arcosh(exp(z))/2)
    =exp(-z)/(16*pi)-exp(-2z)/(128*pi^2)+O(exp(-3z)).
```

A finite nonnegative measure with `Q(z)=int exp(-a*z)dnu(a)` and the displayed leading asymptotic must have no mass below 1 and mass exactly `1/(16*pi)` at 1. It follows that `exp(z)*Q(z)>=1/(16*pi)`. The negative next coefficient contradicts this. No numerical onset or finite sample is involved. This rejects precisely the nonnegative sech-power measure, not arbitrary positive-definite k, signed mixtures, or every nonlocal correction.

## 2. Divisor arithmetic and completion signs

For ordinary absolutely convergent Dirichlet products, `Re(s)>1`, symmetrizing the ordered divisors gives

```text
D(s)=zeta*zeta''-zeta'^2=sum c(n)*n^(-s),
c(n)=1/2*sum_(d|n) [2*log(d)-log(n)]^2.
```

For `n=prod p^a`, divisor exponents are independently uniform on `0,...,a`. Their centered second moments are `a*(a+2)/3`. Thus

```text
c(n)=d(n)/6*sum_(p^a || n) a*(a+2)*(log p)^2.
```

In particular c(p)=log(p)^2. This is a valid Euler-coefficient identity, not a positivity theorem for a critical-line transform. It is not necessary to assume c itself multiplicative.

Let `g=pi^(-s/2)*Gamma(s/2)`, `A=s*(s-1)*g/2`, and `C_A=(log A)''`. Product differentiation gives

```text
C_A=-1/s^2-1/(s-1)^2+psi1(s/2)/4,
xi*xi''-xi'^2=A^2*(D+C_A*zeta^2).
```

Since `X(r)=xi(1/2+i*r)/2`, each r derivative contributes i, and consequently `J=4*(xi*xi''-xi'^2)=p^2*g^2*(D+C_A*zeta^2)`. Both the sign and factor are correct. The original gamma and polynomial contributions cannot be dropped. The expression is undivided at zeta zeros. Absolute convergence in Re(s)>1 does not authorize termwise evaluation on Re(s)=1/2. The proposed two-shift completed product is a legitimate starting object, but no completed Voronoi identity or sign-producing remainder theorem is actually supplied or relied upon.

## 3. Riemann–Siegel scope and source validity

The fixed-N quadratic identity retains both ratio and product phases, the `2*theta''*sin(sigma_nm)` term, and both `-2*d` terms. Direct differentiation confirms these signs. The complete remainder correction also retains all cross products and orders zero through two. Taking derivatives at fixed N before selecting the usual square-root cutoff avoids falsely differentiating a floor function.

Here `R_N=Z-P_N` is an exact definition. No asymptotic Riemann–Siegel error theorem is imported, and no admissible uniform derivative bounds or positive margin follow merely from naming that expansion. The balanced dual scale explains why automatic smallness is unjustified; it does not prove every Poisson method fails. None of the three notes imports a new external result claimed to close an estimate. The beta integral, finite variance identity and product differentiation are derived in the notes. Any future specialized summation or derivative theorem must be checked against an actual arXiv statement, including its range and remainder; there is currently no source-based admission to endorse.

## 4. Matched screens and remaining scope

- **NS100:** all three preserve the complete paired object. They do not assert nonnegative individual slices. Its actual negative-slice control therefore blocks a slice-positivity shortcut but does not decide any of these complete expressions.
- **NS101:** its positive translated kernel shares the Volterra centering identity, positive M, generic autocorrelation transfer, complete pair calculus and undivided product rules. Its known first-Laguerre failure excludes deriving the target from those properties alone. It changes the original integer-square lattice and distinguished Jacobi data; it also lacks the exact zeta divisor coefficients and original Hardy sum/remainder. Those are concrete mismatches for the arithmetic proposals, not passed screens. The original-tail mixture rejection is an additional direct necessary-condition check on the intended object.
- **Davenport–Heilbronn:** conductor 5, odd-character coefficients and gamma factor `Gamma((s+1)/2)` differ from the conductor-one expressions. Its full positivity premises for the k construction have not been established here. Generic completion or differentiation identities may match, but the full literal arithmetic hypotheses do not. Moreover off-axis zeros alone do not establish failure of the weaker first-Laguerre inequality. The existing example script samples a different horizontal-growth expression; running it unchanged would not screen these proposals.
- **NS74/83:** these concern full NB target sensitivity and fixed-smoothing dyadic convergence rates. None of the three attempts asserts an NB projection gain, coefficient cost, or convergence rate. They are not applicable; no NB transfer is claimed.
- **PR73:** its fixed reflected-prefix failure does not cover an exact infinite divisor completion or a growing fixed-N Hardy identity with complete remainder. It does block substituting the old finite reflected theta prefix for either complete object.

**Disposition and budget:** no control script or sign scan was run, because no surviving estimating candidate is ready for computation. The bounded paper review is complete. The mixture class is stopped; the other two lack a signed arithmetic estimating mechanism and a compatible remainder comparison. No row, thaw, manuscript version, commit or outreach. First-Laguerre positivity, RH, G2 and the separate cofinal arithmetic input remain open.

**Final wall check: Same open gap.** The reviewed narrow failure is sound; it supplies no new bound on the original complete target.
