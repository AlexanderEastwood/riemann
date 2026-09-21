# Adversarial review of the growing-window probe

This review concerns `window_scaling_probe.py` and the proposed cutoff consequence for lambda=3,4,5,6,8. It does not transplant the fixed-window inverse certificates, mu, or rho to a new window.

## 1. The scalar far-bound obstruction is rigorous

Write L=2 log(lambda), fix c=10^(-8), and suppose the particular far bound uses

\[
 g_{N+1}=(1-c)\{\log((N+1)/L)-E_L(t_{N+1})\}-\kappa_N,
 \quad t_{N+1}=2\pi(N+1)/L,
\]

where E_L is nonnegative and

\[
 \kappa_N\ge P_\phi(\lambda)\ge\|T_{\rm pr}\|.
\]

Then g_(N+1)>0 necessarily implies

\[
 N+1>L\exp\{P_\phi(\lambda)/(1-c)\}.
\]

Using the manuscript's already proved unsigned-prime scale
`||T_pr||/lambda -> 1`, every family passing this scalar gate satisfies

\[
 \liminf_{\lambda\to\infty}
 \frac{\log((N(\lambda)+1)/L)}{\lambda}
 \ge\frac1{1-c}.
\]

The factor 1/(1-c) is correct. With outer cut lambda^2, the intervening finite block in this architecture must therefore have an exponentially growing number of coordinates. This is a restriction of the specific place-by-place scalar diagonal majorant. It is not a necessary cutoff for actual Weil positivity, a lower bound on the complexity of every possible structured algorithm, a failure of all cofinal constructions, or a disproof of a growing-window theorem.

The threshold routine uses a freshly evaluated prime bound at each lambda. Its gamma(N) is strictly increasing for N>=1: the logarithm increases, every positive reciprocal term in E_L decreases, and the reciprocal terms in kappa_N decrease. The interval signs at N and N-1 therefore certify the first integer passing this implemented gate.

The saved 320-bit table is consistent with the formulas:

| lambda | first even N | first odd N |
|---|---:|---:|
| 3 | 44 | 209 |
| 4 | 283 | 1360 |
| 5 | 1502 | 7224 |
| 6 | 7488 | 36021 |
| 8 | 124442 | 598623 |

These thresholds certify only the indicated remote block. They do not supply the intervening finite Schur comparison.

## 2. Finite Galerkin prerequisites and scope

The initial `solve(M)` implementation interval-certifies the positivity of the finite Schur matrix after solving with T_M, but does not also test T_M>0. Positivity of the Schur matrix alone does not imply positivity of T_M.

Before using `K_ret-S_omit` as a PSD finite correction or invoking finite Galerkin monotonicity, add a positivity certificate for the retained and omitted-test finite tail matrices. An applicable complete positive tail theorem would also suffice, but it is not available automatically at the new windows. This issue was sent to the parent for correction.

**Resolved in the updated probe:** each finite tail now has an explicit interval positivity gate, either by an exact frozen congruence and interval Gershgorin inequalities or by interval LDL. The saved 4096-bit runs at lambda=3,4,5,6 pass these gates and their finite head gates. Lambda=8 remains unresolved at the interval-metric stage; it is not counted as a sign certificate or a negative result.

Even after those finite gates pass, comparing the finite correction to an infinite Schur correction requires the corresponding positive/coercive complete tail prerequisite. The probe establishes no such outer-tail prerequisite at lambda=5,6,8. Its finite diagnostics must not be presented as complete inverse upper bounds or cofinal errors.

The diagnostic flag about unavailable complete inverse bounds should say “unavailable in this probe,” so the finite-only lambda=4 calculation does not appear to retract the separately proved complete certificate there.

## 3. Invariant margins and conditioning are different quantities

For positive K and Hermitian correction U, the generalized eigenvalues of `(U,K)` and

\[
 \delta=1-\lambda_{\max}(K^{-1/2}UK^{-1/2})
\]

are invariant under every common invertible head congruence. This follows directly from the generalized eigenvalue equation or its determinant. The script's Cholesky-based generalized-eigenvalue calculation computes that quantity numerically.

By contrast, `lambda_min(K-U)/lambda_min(K)` and `||U||/lambda_min(K)` are only dimensionless under common scalar rescaling. They are not invariant under a general change of head coordinates. They can be reported, but with the chosen normalization stated. The script's `cond(V)` is an additional numerical diagnostic, not an interval-certified condition number.

The simplest separation example is

\[
 K=\operatorname{diag}(1,\epsilon),\qquad
 U=\operatorname{diag}(\delta,\epsilon(1-\eta)),
 \quad 0<\epsilon\le1,\quad0<\delta\le1-\eta<1.
\]

Its best directional headroom is 1/delta, its worst generalized margin is eta, and a K-normalizing congruence has condition epsilon^(-1/2). These quantities can vary independently. Thus a very favorable single direction cannot diagnose the complete head sign or conditioning. Taking eta negative also leaves the favorable direction intact while destroying the full sign.

The probe's exclusion of generalized corrections below 10^(-14) when reporting its “best nonzero” direction is a numerical reporting threshold, not a mathematical gap or certificate. It should be made explicit when reporting that statistic.

## Assessment

The analytic exponential-cutoff consequence is supported, with the narrow method-specific scope above. The finite probes can inform a growing-window study after their finite-tail positivity prerequisites are checked. Neither finite dimensionless margins nor the existing fixed-window pass establishes the uniform signed estimate still required for G2.
