# Adversarial review of the v1.21 insertions

Reviewed only `schur_insert.tex`, `cancellation_insert.tex`, `rh_route_insert.tex`, and `audit_appendix_insert.tex`, using the previously validated witnesses and the saved 768/896-bit certificate outputs. No new numerical experiment or broad manuscript audit was performed.

**Outcome:** no blocking mathematical error found. Two small abstract-theorem wording corrections are recommended below.

## Finite trial and Schur statements

For T bounded below by a positive constant, T^-1 B has range in D(T), so both the square identity and the residual identity are legitimate operator products on the finite head. The adjoints and cross terms agree with the first-slot-linear convention.

The compression identity for K_X is exact when X takes values in the retained finite tail space. Positivity certified there is positivity of the complete trial form K_X and gives the stated local alpha=0. It does not imply positivity of the exact infinite Schur complement, because the positive inverse-residual correction is still subtracted. The proposition and appendix preserve this distinction.

Nested finite tail spaces whose union is a form core give monotone convergence of the inverse quadratic forms by the stated variational argument. Finite dimensionality of the head then gives convergence in matrix norm of S_M down to S_infinity. The warning that finitely many positive compressions do not establish the limiting sign is correct.

The semidefinite remark uses the necessary form factorization condition Ran B contained in Ran T^(1/2). The minimal preimage C=T^(-1/2)B is bounded because the head is finite dimensional, and the displayed form square is valid. It correctly avoids treating kernel orthogonality or closure of the range as sufficient.

The local alpha=0 certificate is restricted to lambda=4, X=0, and the specified frozen solves through mode 256. The appendix's four conservative pivot bounds agree with both saved outputs; their stated interpretation as pivots rather than eigenvalue lower bounds is essential and correct.

**Small wording corrections:**

- State explicitly that P_M is an **orthogonal** projection.
- In the general compression proof, replace “every vector has finite support” by “every trial lies in the head plus the retained finite tail space.” An arbitrary finite-dimensional subspace of D(T) need not consist of finitely supported Fourier vectors. The compression identity itself is valid without that stronger claim.

## Exact-source cancellation statement

The real algebraic construction x=(-a_2,a_1) gives exact orthogonality to the archived candidate. The projector perturbation bound applies to that same candidate, with the source dependency matched by hash. Projecting and renormalizing changes the unit vector by less than 2 delta, and each finite Hermitian quadratic form changes by less than 4 delta times its compressed operator norm.

The new positive lower bound for the final vector, 2.5829853e-31, is smaller than the saved 896-bit lower enclosure. The displayed upper bound 2.5858415e-31 and the two strict 0.4 bounds also follow from the full interval outputs. Exact orthogonality to P_64 p_3 implies exact orthogonality to p_3 because the final vector lies in E_64.

The final ratio bound is numerically consistent: q_W<3e-31 and q_np>0.4 imply q_W/q_np<7.5e-31. The text correctly calls this near-cancellation rather than an additional null vector or a negative direction, retains the pole term in the nonprime comparison, and makes no invariant-subspace or infinite-residual assertion.

## Cofinal implication

The direct RH implication is valid under its stated hypothesis about the complete unshifted semilocal Weil forms, with errors measured in the common ordinary norm. Every fixed smooth compactly supported test eventually lies inside all the windows, zero extension preserves its norm and global Weil value, and sending epsilon_j to zero proves positivity for every such test. The standard compact-support Weil criterion then applies. No additional Riesz realization or evaluator hypothesis is needed for this direct route.

This statement does not prove its hypothesis. The new fixed-window trial certificates and cancellation witness do not supply a cofinal signed lower estimate, and the insertions do not claim otherwise.

The witness tables and appendix retain their internal computer-assisted status and the dependency on the exact-source certificate. No uniform G2 sign gap or RH claim has been established by these insertions.
