# Complete finite-floor test — v1.38

September 21, 2026. Starting snapshot: complete v1.37, GitHub commit `c623b21aca132a3b87a95dc19e24da9393f56a00`. The saved canonical ChatGPT copies remain behind at v1.34 after transfer failures; the verified GitHub source is used. Delivery remains LaTeX only.

## Outcome

The requested weaker experiment succeeds: both parity sectors at lambda=5,6,8 have **complete ordinary lower floor -8**, using the same fixed parameters. Every omitted Fourier row is enclosed. The frozen trial quotients are positive and below 1e-16, so each sector's spectral edge is bracketed between -8 and 1e-16. No certified negative physical trial was found.

The lambda=8 floor also bounds all smaller physical windows by support consistency and zero extension. Thus a finite list of floors is not additional evidence of a cofinal theorem; the intermediate windows test the same construction's cost and enclosure headroom.

No G2 sign gap was closed. RH is not proved.

## What changed, and what was held fixed

The practical improvement is to use the finite-floor theorem literally: choose a **moderate fixed additive shift delta=8**, rather than trying to certify positivity or a tiny error of 0.001. This allows a much smaller remote split. It does not revive the disproved lambda=5 inequality W>=1e-8 D on Q16.

Compared with the old positivity pipeline, this experiment changes the target to W+8I, uses a head ending at 256, and uses Z=0 instead of any CG or structured inner solve. The same procedure and the following parameters were then used for every lambda/parity case:

| Parameter | Frozen value |
|---|---|
| Ordinary additive shift delta | 8 |
| Fourier head cutoff N | 256 |
| Explicit residual cutoff J | 4096 |
| Moment order r | 16 |
| Remote Young parameter tau | 1/10 |
| Trial solve Z | 0 |
| Even head | 0 through 256, dimension257 |
| Odd head | 1 through 256, dimension256 |
| Archimedean series terms | 64, plus analytic remainder |
| Initial arithmetic | Arb160 bits |
| Replay arithmetic | Arb256 bits, identical dyadic witnesses |

The window length L=2log(lambda), prime list, coefficients, separate logarithmic diagonal, prime norm, tail weights, moment matrices and congruence proposals were freshly evaluated per window. Those evaluations are part of the fixed procedure. No lambda=4 constant was reused. The construction transferred without window-specific retuning **within this three-window test**. Delta=8 and N=256 were selected for this finite range; they are not asserted as an unbounded-window rule.

## Exact inequality and physical scope

Use the canonical closed Weil form on H_a=L2(-a,a), a=log(lambda), with unitary Fourier transform of the zero extension and logarithmic form domain. The physical Fourier head is the existing orthonormal even/odd basis; no prolate-source or source-L2 norm transfer is used. In the first-slot-linear convention, the block adjoints and real quadratic orders are unchanged.

For W=[[F,B*],[B,T]], suppose T>=D_g and g_(N+1)+delta>0. A general finite solve obeys

    K_delta=K_Z+delta(I+Z*Z),
    R_delta=R-delta Z.

The remote rows beyond the support of Z are unchanged. Therefore

    L_delta=K_delta - sum_(N<n<=J) R_delta,n*R_delta,n/(g_n+delta)
            - U_J/(g_(J+1)+delta) >= 0

implies W>=-delta I on the complete form domain. In this test Z=0, so K_delta=F+delta I and R_delta=B. The moment theorem is used with M=N<J and G the orthonormal head embedding; G*G=I. Its proof does not need a nonempty intermediate solve block. The lower enclosure includes both the leading remote moment Gram and the geometric remainder.

Both parities are certified. Hence the bound applies to every physical subspace, including C_a^low where it is defined, without identifying it with the larger rank-one complement. No centered sampler is used, and its explicit graph defect is neither removed nor bypassed in any transfer claim.

## Certificate margins and spectral brackets

Let U_delta=K_delta-L_delta. The generalized margin is

    h=1-lambda_max(U_delta,K_delta).

The exact dyadic congruence C verifies C L_delta C* >=mI and C K_delta C*<=MI, with m=999/1000. Thus h>=m/M. The table displays downward-rounded lower bounds; it does not display resolution margins or exact generalized eigenvalues.

| lambda | even h lower | odd h lower | complete ordinary floor | each parity's trial upper |
|---|---:|---:|---:|---:|
|5|0.8430|0.9190|-8|<1e-16|
|6|0.7166|0.7620|-8|<1e-16|
|8|0.2474|0.1022|-8|<1e-16|

Exact rational M bounds, even then odd, are: lambda5=(1185,1087)/1000, lambda6=(1394,1311)/1000, lambda8=(4037,9772)/1000. The corresponding bounds on h are exactly999 divided by these integer numerators.

All six 160-bit passes were replayed at256 bits using the same C and trial vectors. The saved NPZ contains exact IEEE754 dyadics; converting each value to Arb gives an exact scalar. Each C is checked triangular with nonzero diagonal, and every outward row gate passes. The rounded finite-matrix eigenvalue proposals were negative near machine precision; the exact frozen trial quotients were **positive**. The float signs are not spectral evidence.

All computations took seconds per sector in this environment. Timings are recorded for reproducibility, not promised as hardware-independent complexity.

## Shifted cutoff cost: proved obstruction for this comparison

With c=0, the existing scalar far weights are g_n=log(n/L)-E_L(2pi n/L)-kappa_(lambda,N), where kappa>=M_phi,lambda. Thus their shifted positivity gate requires

    N+1 > L exp(M_phi,lambda-delta).

A fixed shift saves a large constant factor, approximately exp(-delta), but retains the existing asymptotic exponential-in-lambda cost. Since M_phi,lambda>=||T_prime,lambda||~lambda, bounded delta forces liminf log((N+1)/L)/lambda>=1. A polynomial N would instead require delta at least M_phi,lambda-O(log(lambda)). This rules out a polynomial-cost, bounded-floor conclusion from **this scalar comparison**, not from all signed matrix metrics.

Fresh outward thresholds (the smallest admitted N>=1) are:

| lambda | delta=.001 even | delta=.001 odd | delta=8 even | delta=8 odd |
|---|---:|---:|---:|---:|
|5|1501|7217|1|4|
|6|7481|35985|3|14|
|8|124317|598024|43|204|

The chosen N256 covers all delta8 cases. A -.001 target would hardly reduce the old cost, even though it also avoids the false positive weighted metric. Every nonboundary threshold has an outward-positive gate and an outward-negative predecessor. The formulas are monotone in N.

## Failed or exploratory attempts

Before freezing the common-floor protocol, smaller N128 pilots passed complete floors -3 (lambda5 even), -4.5 (lambda5 odd and lambda6 even), and -8 (lambda8 even). A lambda8 even shift7.5 proposal failed the lower-enclosure Cholesky gate, and a lambda5 odd shift4 failed the scalar tail gate. Neither failure is a negative Weil direction. These pilots were not used to infer cross-window stability.

The first replay's optional margin reporting attempted to pick nearly equal interval extrema through binary64 keys. A protective assertion rejected that choice. It was replaced by explicit rational thresholds and strict outward comparisons; every final proof gate and generalized margin passed. The underlying six positivity checks had already passed. This illustrates why the floating ordering is only a proposal, never a proof assumption.

## Candidate register and novelty screening

**G2.6-FF-01 — fixed moderate additive floor. Status: validated finite diagnostic / continuation, not a new independent live arithmetic mechanism.**

- Precise target: W_(lambda_j)>=-C*I with C* finite independent of j along a cofinal family; current certificate proves C*=8 only for1<lambda<=8.
- Assumptions used for current certificates: the proved canonical form/core, coefficient and moment enclosures, shifted scalar tail estimate, and outward arithmetic. No G2, RH, hidden complement positivity, or unjustified source transfer.
- Essential practical change: using a non-small additive shift permitted by v1.36. This relaxes the spectral target; it is not a new factorization or arithmetic cancellation.
- Nearest prior proposals: v1.16 signed Schur/moment certificate, v1.17 shifted inertia, v1.25 cutoff-cost theorem, and v1.36 finite-floor implication. The formulas are direct specializations with Z=0.
- Explicit exclusions: not a new structured inverse, prime norm estimate, finite-rank repair, source-only residual argument, dyadic pair metric, common-Gram factorization, Picone mechanism, or weighted-concentration mechanism. It reuses the existing scalar prime bound and signed Schur correction openly.
- Literature: finite-window lower bounds and verified trial upper bounds are familiar in the nearby primary preprint [Zhu2026v2](https://arxiv.org/html/2608.24827v2), sections1.2,1.3 and5. No external numerical constants or sign claims are imported. The shift and block completion are elementary spectral tools. Neither worldwide novelty nor a project-new positive mechanism is claimed.

## Exact remaining lemma and next step

Prove the existence of one fixed C* and a cofinal family of physical windows for which the complete lower-floor inequality holds, either on both full parities or on a source complement satisfying the already stated residual and coupling hypotheses. A finite list, even a whole bounded interval of windows, supplies no such proof.

For this pipeline the concrete unresolved estimate is L_(C*,lambda)>=0 with a controlled complete correction on an unbounded family. The current scalar remote comparison imposes its exponential cost even after shifting. A useful next analytic target is a signed tail estimate with bounded additive loss that does not replace the prime operator by its growing absolute norm. A declining lower certificate alone cannot diagnose spectral divergence; a negative certified Rayleigh quotient would be needed for actual negative evidence.

The completed experiment answers the cost question positively for5,6,8, but leaves the asymptotic arithmetic problem open.
