# NS-53 independent mathematical review — 2026-09-22

Reviewer: NS-52 agent. Reviewed `evidence/ns53_nb_blocks/proof.tex` in the shared worktree after its first complete draft. This is an internal review, not a new result or a numerical certificate.

**Disposition: no MAJOR or MINOR mathematical finding.** The following checks were performed analytically, with no finite numerical approximation substituted for asymptotic control.

1. **Framework and criterion.** The space L²(0,∞), χ=1_(0,1), and rho_n(x)={1/(nx)} match Báez-Duarte's integer-dilation criterion ([primary source](https://arxiv.org/abs/math/0202141)). The paper's abstract expressly uses this space and the natural-number dilation subclass. The draft correctly treats convergence, rather than an optimal rate, as the required conclusion.
2. **Arithmetic entries.** Substitution y=1/x gives the stated Gram integral. On each [j,j+1), both floor functions are constant; integrating the resulting quadratic divided by y² gives every term in the Gram series. The [0,1) contribution is 1/(mn). The expression for b_n follows from splitting the integral at 1 and the identity ∫_1^K {t}/t² dt=1+log K−H_K. The diagonal partial-sum formula was checked algebraically and tends to log(2π)−γ by Stirling. Each cell is nonnegative; the warning not to separate divergent pieces is essential and present.
3. **Finite independence and positive residual.** The jump at the smallest integer with nonzero coefficient proves finite independence. For exact representation of χ, integer jump matching would force all coefficients to equal −μ(n), contradicting a prime beyond the finite support. Thus E_N>0 and every residualized finite Gram matrix is positive definite.
4. **Schur complement and cross terms.** z_n=(I−P_N)rho_n has Gram S=D−CᵀG⁻¹C and residual correlations h=b_B−CᵀG⁻¹b. The projection gain hᵀS⁻¹h and coefficient update are correct. Replacing h by b_B or S by D would be wrong; the text explicitly avoids both substitutions.
5. **Trace bound.** 0<S≤D gives λ_max(S)≤tr D=κΣ_(N<n≤M)1/n. Consequently gain≥||h||²/(κΣ1/n)≥||h||²/(κ log(M/N)). Both inequality directions are correct. Here κ=log(2π)−γ is local to NS-53 and unrelated to NS-52's heat coefficient κ=1/4; the sections define them explicitly.
6. **Raw Möbius penalty.** The affine residual B_j−Ay and B_j=0 for 1≤j≤N give the exact lower bound (N+1)|Σ_(n≤N)μ(n)/n|² on the unsmoothed approximation's error. The text does not transfer this lower bound to the optimized distance.
7. **Asymptotic implication.** RBC implies E_(qN)≤(1−α_j)E_N; Σα_j=∞ gives convergence. α_j=1/[2(j+1)] indeed gives E_(q^j)=O(j^−1/2) and hence E_N=O((log N)^−1/2). RBC is clearly marked unproved and only sufficient, not equivalent to RH or a consequence of RH. No hidden assumption about zeros, cancellation, numerical solves, or Gram conditioning enters the finite identities.

NOTE: the exact relative-gain criterion in the concluding paragraph is a reformulation of convergence, not a new arithmetic estimate; the draft says so. Its equivalence follows from E_N>0 and E_(N_(j+1))/E_(N_j)=1−gain/E_(N_j), together with the standard infinite-product criterion.

Scope: this review does not verify a manuscript build or validate any future numerical implementation. Parent owns integration and publication.
