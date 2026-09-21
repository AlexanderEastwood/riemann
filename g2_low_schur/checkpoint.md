## Current research checkpoint: September 21, 2026 — v1.20 low-mode Schur revision

**Established in this revision:** a structured inverse bound that reuses the certified signed tail factors; a finite-row version with every infinite residual row enclosed; an ordinary-error criterion with the growing-head and congruence scales explicit; and convergent upper approximations to the actual infinite far-tail inverse at lambda=4. The latter have rigorously certified contraction factors66/67 (even, n>512) and334/335 (odd, n>1536).

**Not established:** the effective low-head sign at lambda=4 or a lower bound−o(1) on unbounded windows. **No G2 sign gap was closed.** Weak G1 and all existing certificates remain in their previous scope. The explicit sampler graph defect remains. No RH proof is claimed. The complete manuscript retains the requested version label1.20.

### Recovery and selected obligation

Fresh authoritative reads/materialization recovered the complete current manuscript, log, notes, validation and cumulative historical bundle. Starting versions were20 for the manuscript/notes/validation and21 for the log/bundle. The recovered181-member bundle has SHA256 `2b7f003e1e7d10f47780708e87892cc739de4f5eea6a621746e1be716fd8f597`. It is preserved cumulatively. The selected target was the actual33-dimensional low Schur matrix at lambda4:17 even and16 odd coordinates, with the complete positive complement Q16 already certified. No raw finite-matrix positivity was substituted for this inverse-corrected target.

### Attempt1: the scalar tail inverse loses too much

Using the exact lower tail bound T>=10^(-8)D_arch, construct a768-bit finite solve on17..256 for the17-dimensional even head. Every residual row through2048 and the infinite directional moment Gram (order64) was included. The resulting lower matrix failed at its first LDL pivot, approximately−27684.1. This is failure of an enclosure, not a negative Weil direction.

A noncertifying high-precision diagnostic of the signed K_X matrix shows eigenvalues down to about2.83e−75. This explains the need to preserve directional cancellations. Merely dividing an ordinary residual by the coarse tail floor is insufficient.

### Proved structured inverse estimate

Split a certified tail as T=[[F,B*],[B,U]], U>=D_g>=gamma I. For the saved finite-support Z, set R=B−UZ and K_Z=F−B*Z−Z*B+Z*UZ. If L_lower<=K_Z−R*D_g^(-1)R and C L_lower C*>=mu I>0, then for r=(h,k),

`<T^(-1)r,r> <= ||D_g^(-1/2)k||² + mu^(-1)||C(h−Z*k−R*D_g^(-1)k)||²`.

Both signs inside the last norm are minus. The proof uses a closed lower form on the possibly larger D(D_g^(1/2)) domain, followed by inverse order; it does not assume the second triangular change preserves D(U^(1/2)). If the saved certificate belongs to T−cD, its factors give an upper bound on T^(-1) by inverse order. The shifted residual is never relabeled as an unshifted one.

The finite-row implementation encloses the omitted mixed Gram by an operator Cauchy–Schwarz bound and matrix Young inequality. All Fourier signs are represented through the normalized parity basis. Finite-column remote Grams are valid despite the whole weighted operator not being Hilbert–Schmidt. The prior320-bit tail witness hashes and congruence margins are checked before reuse.

### Attempts2–4 and adversarial falsification of the current majorants

The structured even calculation uses inner head17..512, saved solve support513..1024, J4096, moment order64,768-bit arithmetic, and mu=0.9999999999. The outer actual-W solve support was enlarged successively to256,512,1024. The last expansion crosses the inner head boundary; this is valid because J exceeds both support cutoffs. Outer residuals belong to W, while inner factors belong to W−10^(-8)D.

A preliminary Young parameter10^(-8) made the remote mixed bound much worse (first pivot about−144198); it was replaced by1 after inspecting the explicit rho U_k term, not by increasing precision. With parameter1, the first pivots were positive but the second pivots still failed:

| outer solve cutoff M | first pivot | second pivot |
|---|---:|---:|
|256|0.0001185083|−2.79577e−5|
|512|0.0011263500|−1.56760e−6|
|1024|0.0017430178|−4.71642e−7|

These values are interval enclosure outputs; none is a Weil Rayleigh value.

An adversarial agent then tested the optimistic ceiling K_X−V_J, which omits all the further positive inverse penalties. Exact160-bit dyadic test vectors prove a strictly negative value for that ceiling in every case:

| M | certified ceiling quadratic value, approximately |
|---|---:|
|256|−3.4475968e−21|
|512|−1.1146930e−19|
|1024|−7.20037e−59|

The standalone `check_structured_ceiling.py` verifies input hashes and recomputes these quadratic forms in Arb; the witnesses replay at896bits. Holding each solve fixed, changing Young's parameter or moment order cannot rescue that certificate. Increasing J only increases V_J, so it cannot rescue the same candidate either. This is a rigorous obstruction to these particular inverse majorants, **not evidence of a negative Weil test and not a disproof of positivity**. Exploratory eigensolver diagnostics remain labeled numerical.

### Proved replacement for the diagonal far inverse

The failed ceiling test directs the next step at the actual far inverse rather than another unsigned remote bound. If D_g<=U<=mD_g, let A=D_g^(-1/2)U D_g^(-1/2), S=I−A/m, and

`P_k(A)=m^(-1) sum_(j=0)^(k−1) S^j + S^k`.

The spectral theorem proves A^(-1)<=P_(k+1)<=P_k<=I and

`0<=P_k−A^(-1)=S^k(I−A^(-1))<=(1−1/m)^k I`.

Thus the conjugated polynomials give decreasing complete inverse upper bounds. The first is

`U^(-1)<=D_g^(-1)−m^(-1)D_g^(-1)(U−D_g)D_g^(-1)`.

This retains a signed arithmetic correction to the diagonal inverse. The polynomial is an operator on the full far tail; its evaluation has not been replaced by an unjustified finite power.

The needed actual upper sandwich is now proved at lambda4. The existing lower archimedean bound was strengthened to the two-sided estimate

`|a_n−log(|n|/L)|<=E_L(|t_n|)`.

The new upper half follows from Binet at w=5/4+it/2: Re log w−log(t/2)<=25/(8t²), the recurrence real terms are negative, and25/8<7/2. The prior absolute trigamma and exponential-tail bounds finish it.

The complete bounded remainder obeys

`||R_0||<=C_R=2*pi*B_*+32*h_L/L+2*P_4 <34.450462`.

Adversarial normalization review corrected a preliminary pole bound32h/L² to the correct32h/L before integration. The obsolete preliminary constants60/301 are not results and their draft JSON is excluded from the evidence archive.

For g_n=(1−c)(log(n/L)−E_L(t_n))−kappa, c=10^(-8),

`U<=D_g+[kappa+2(1−c)E_L(t_*)+C_R]I`.

The ratio1+[...]/g_(N+1) is rigorously below66.76640 for the evenN512 tail and334.71708 for the oddN1536 tail. Therefore m=67 and335 are valid for the complete infinite tails. `certify_far_inverse.py` proves the strict gates independently at320 and384bits. This closes the upper-sandwich prerequisite for a convergent arithmetic inverse refinement at this one window. It closes no low-head or G2 sign gap.

### Uniform scales and next concrete work

The structured estimate yields the sufficient ordinary lower error

`alpha_lambda+e_lambda²+t_lambda²/mu_lambda`.

Here alpha controls the signed outer K_X, and e and t are **operator norms on the entire outer head**. If only columnwise residual bounds delta are available, their operator norm squared can be d_lambda delta²; equal columns show that factor is sharp. A negative congruence bound CLC*>=−eta I converts to ordinary error eta||C^(-1)||², not eta. All these factors remain separate from the previously proved eta C_lambda/(1+eta) weighted-to-ordinary conversion.

The inverse-polynomial error on a residual matrix Y is bounded by(1−1/m)^k Y*D_g^(-1)Y. A growing-window application therefore needs the actual m_lambda and residual operator norm, for example ||D_g^(-1/2)Y||² exp(−k_lambda/m_lambda)->0. The integers67/335 are not asserted uniformly in lambda.

**Next concrete step:** certify the signed quadratic correction from the first inverse polynomial, including its entire remote contribution, on the fragile low-head directions. If insufficient, add further monotone inverse-polynomial terms with a certified full-operator remainder. Reuse the saved exact ceiling witnesses to measure which loss is actually reduced. Prove the full low-head sign before attempting ground ordering; then identify independent arithmetic estimates for a cofinal window family. Do not repeat precision-only or Young-parameter-only experiments on the already falsified candidates. The odd low-head sign also remains unproved; no even-only result is extrapolated to the complete form.

---

