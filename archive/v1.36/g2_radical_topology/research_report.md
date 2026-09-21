# G2.6-RAD-03: dense radicals and the uniform finite-floor reduction

Status: proved reductions and no-go results; no independent signed arithmetic lower bound. G2 and RH remain open.

## Main improvement

For a cofinal family of complete physical windows, it now suffices to prove

\[
q_a[f]\ge-C_*\|f\|_2^2,\qquad f\perp\operatorname{Ran}P_a,
\qquad C_*<\infty\text{ independent of }a,
\]

where P_a is the actual rank-one repaired source or the v1.35 growing radical block, and its already established full operator residual tends to zero. Both parities must be controlled. The finite constant need not tend to zero. This is a sharper sufficient reduction, not a proof of its hypothesis and not a new independent positivity mechanism.

The key proved dichotomy is: either all compact smooth Weil tests are nonnegative, or the complete lower spectral edge tends to minus infinity. If q[f]=-d<0, approximate f in ordinary norm by a finite combination h of translated Gaussian radicals. For w_a=f-chi_a h, the complete residual calculation gives q_a[w_a] -> -d while ||w_a|| -> ||f-h||. Arbitrarily close ordinary approximation amplifies the negative normalized form without bound. The coefficients and required window need not be uniform in approximation accuracy; no effective amplification rate is claimed.

## Domain and exact ingredients

- H=L2(R,dx), I_a=(-a,a), a=log(lambda), first-slot-linear pairing; J_a is zero extension.
- The local operator is the canonical self-adjoint complete Weil operator, with its logarithmic form domain and both pole signs. Smooth compactly supported functions form a core by prop:v118-log-dirichlet.
- The Gaussian radical phi from v1.35 is ordinary-unit normalized, even and double-exponentially decaying. All its real translates are polarized radicals.
- Its Fourier transform is a nonzero entire function, hence nonzero almost everywhere on the real line. Fourier uniqueness proves the span of all real translates is dense in ordinary L2. Reflected translates give dense even and odd spans.
- For every fixed finite translate combination h, the v1.35 exterior-remainder proof gives ||W_a(chi_a h)|| -> 0 and chi_a h -> h. All global prime rows, including those beyond lambda^2, enter that proof. No finite Fourier cutoff occurs.
- These are not claims of density in a global form topology or of uniform approximation coefficients. No global positive closed Weil realization is assumed.

## Further proved obstructions

1. The operators A_a=W_a direct-sum zero on L2(I_a^c) converge strong-resolvent to zero, unconditionally. The same is true after assigning zero to a removed block with ||A_a P_a|| -> 0. The bounded perturbation has norm at most 3||A_a P_a||.
2. Ordinary strong-resolvent convergence therefore cannot be the missing sign input. It does not imply convergence of fixed compact-test form values or control the lower spectral edge.
3. Uniformly bounded positive comparisons B_a, compressed off the actual source, satisfying q_a[f]>=<B_a f,f>-eta_a||f||² with eta_a->0 must tend strongly to zero after zero extension. This rules out any nonzero persistent bounded comparison on the limiting source complement, not all moving matrix metrics.
4. If the actual physical C_a^low removes only even image columns, every odd reflected radical cutoff lies in it exactly. The same strong disappearance is required on every fixed odd vector, regardless of the rank of the even image block. There is no identification of C_a^low with the whole source complement.
5. A fixed closed nonnegative comparison form, with all projected cutoff tests in its domain, must vanish on phi-perp. It can remain nonzero on the source direction. An unspecified domain intersection is insufficient.

## Falsification and sharpness

The exact support-consistent countermodels q_±(x)=±|sum x_k|² on finite sequences share a dense radical and the same zero strong-resolvent limit. Their n-coordinate matrices are ±11*, with nonzero eigenvalue ±n. Thus the negative model has arbitrarily negative lower edges while the positive model is nonnegative. A common finite lower bound distinguishes them; density and resolvent convergence alone do not.

For f=e1, h=e1-(1/m)sum_{k=2}^{m+1}e_k is an exact radical, ||f-h||²=1/m, and q_-(f-h)/||f-h||²=-m. `check_topology_countermodels.py` checks these identities with exact fractions for m=2,4,16,64,256. These are abstract countermodels, not arithmetic numerics or a new finite-window certificate.

Other sharpness checks: escaping rank-one projections have norm one but strong limit zero; unbounded comparisons n²|e_n><e_n| show why uniform operator boundedness cannot be omitted. A source-direction comparison shows why the fixed closed-form conclusion is only vanishing on phi-perp.

An independent adversarial agent checked the dense-translate proof, the arbitrary-center extension of the v1.35 residual, resolvent identities, domains of deleted blocks, both proofs of the finite-floor criterion, parity restrictions, and the distinction between ordinary and form topology. Its report is `adversarial_review.md`.

## Candidate register and novelty screen

**ID:** G2.6-RAD-03.

**Classification:** continuation of RAD-02 and a stronger conditional reduction/no-go; not registered as a new live positivity mechanism. The stable positive-comparison shortcut is rejected. CAP-01b remains a conditional route, now with a bounded-error sufficient target.

**Nearest project proposal:** v1.35's uniformly separated growing lattice of radicals, which gave O(log lambda) near-zero modes and excluded positive polynomial gaps. The new ingredient is totality of all fixed real translates in ordinary L2, together with support consistency of the complete form. A single fixed lattice was not asserted total. This produces an actual strong-resolvent limit and negative amplification, not another eigenvalue count or constant improvement.

**Other formula/dependency comparisons:** signed Schur/residual and structured-inverse routes seek upper bounds on omitted corrections; none is used to infer sign here. Scalar prime-norm, finite-rank repair, dyadic pair norms and common-Gram routes seek positive comparisons or norm bounds; the current results instead constrain their possible limits. Source-only residual arguments are explicitly falsified by q_±. Picone/capacity, continuum cancellation and signed concentration retain arithmetic sign information; the new argument does not replace that information. Negative-only Schatten bounds, commuting-channel assumptions, Cotlar regrouping and primitive transport remain subject to their previous obstructions.

**Primary-literature screening (September 21, 2026):**

- [Wiener, Tauberian Theorems (1932), original article](https://archive.org/download/wiener-1938/wiener1932.pdf): classical translation-density ancestry. The L2 uniqueness proof needed here is supplied in full; no priority claim is made.
- [Connes--Consani, Spectral triples and zeta-cycles, Section 3](https://arxiv.org/abs/2106.01715): the radical structure is classical and already used by the project.
- [Suzuki, Weil's quadratic form via the screw function, v2](https://arxiv.org/html/2606.09096v2), Section 7: discusses derivative operators in Weil-metric quotient completions and a strong-resolvent expectation there. Those are different operators and Hilbert spaces from the ordinary-L2 Weil operators treated here. This distinction prevents a false contradiction or claimed resolution of that conjecture.
- [Connes--van Suijlekom (2025)](https://doi.org/10.1007/s00220-025-05493-1): finite-window quadratic forms and real-zero constructions are nearby context, not an input establishing the cofinal signed floor.
- Searches for a bounded-below Weil criterion also located [Kim et al., v2](https://arxiv.org/abs/2607.24830v2), Section 3.7 of its PDF studies an RMS residual built from a zero sum with factors exp(2a(rho-s))/(rho-s), excluding neighborhoods of ordinates and using finite zero lists in its numerical checks. That is different from a lower bound for the complete Rayleigh form over every physical ordinary-unit test. The present proof uses radical totality and no inserted zero list; that paper is not used to certify the arithmetic floor or worldwide novelty.

The precise specialization is new within the inspected project register. Worldwide novelty is unresolved; an unsuccessful search does not establish it. The manuscript supplies self-contained proofs and makes no priority claim.

## Exact remaining lemma and next step

Construct an explicit arithmetic signed concentration hierarchy with

\[
-D_a P_a+\sum_j w_{a,j}\mathcal C_{a,u}(G_{a,j})\succeq-C_*P_a
\]

on the even source complement, and the corresponding bound with one finite constant on the full odd sector, along a cofinal family. Equivalently pursue the complete complement inequality at the start of this report. The form domain, both parities and the ordinary normalization must be retained. A finite list of windows, a constant depending on a, or a bound only on each fixed vector does not suffice.

The next arithmetic attempt should therefore ask for a uniform O(1) signed lower error before trying to optimize it to o(1). Existing absolute prime-norm estimates grow with lambda and do not prove this. No candidate arithmetic proof has survived yet; the reduction has narrowed what must be estimated without supplying that estimate.

The source sampler, endpoint shell and explicit graph defect are untouched. No lambda=8 calculation was attempted. **No G2 sign gap was closed, and RH is not proved.**
