# Actual signed NB gain: coefficient-recovery mechanism audit

Internal working note, 2026-09-30. This is bounded paper work, not a new candidate screen, theorem row, thaw, manuscript edit, publication, or numerical certificate.

**Verdict: no new arithmetic lower estimate obtained. Wall check: Same open gap — NB-GAIN, closest NS53/61/87.** The concrete attempted mechanism was to combine the original arithmetic coefficient recovery with forced Möbius-size new coefficients and the actual full refit. Two precise deficiencies emerge: recovery bounds the projected Gram in the direction that gives an **upper**, rather than lower, inverse-Gram bound; even an idealized Möbius new-block contribution to the recovery certificate has only a dyadically summable scale. Neither deficiency is an upper bound on the actual gain or a closure of original NB-GAIN.

## Source and review scope

Read the assignment brief first. The coordinator refreshed the public source at commit `769359298fada57711b6895c4bde3fabe2cc5168`; this reviewer confirmed that exact HEAD in read-only checkout `/private/tmp/riemann-prime-folding-review-20260930`. Read AGENTS, the conclusion register/status inventory and continuation scopes, relevant current README/checkpoint and NEXT_STEPS entries, and the missing-evidence ledger. This is a conclusions/dependency review, not a replay of every historical proof. Both original-evidence recovery groups stay open.

Direct proof dependencies checked:

- `evidence/ns53_nb_blocks/proof.tex`: exact Schur gain, optimizer update and scope of RBC; distinguish its unsmoothed target from the q=2 target below.
- `evidence/v159/ns61/proof.tex`: fixed q=2 criterion, complete average/trace bound, retained old-new correction, missing lower correlation.
- `evidence/v163/ns78/proof.tex`: complete norm/sample comparison and exact divisor inverse, including exterior eta and all cells.
- `evidence/v161/ns74/proof.tex`: same-Gram unitary control, altered loads and finite-statistics scope.
- `evidence/v166/ns83/proof.tex`: logarithmic lower floor and cumulative relative-gain restriction; imported historical dual-vector theory was not independently reconstructed here.
- `evidence/ns86_optimized_arithmetic/argument.tex`: original divisor/potential identities and hypothetical off-line-zero annihilator.
- `evidence/ns87_joint_tail/argument.tex`: complete corrected finite observations, inverse metric, safe step and polynomial tail cutoff.
- `evidence/v162/ns75/proof.tex`: exact next-block derivative-jump cancellation and its finite failure as unit-step descent.
- `evidence/ns98_projected_cost/argument.tex`: actual projected signed cross cost remains unestimated.

Local prior-audit dependencies read in the primary workspace: `audits/nb-six-review-2026-09-30-v1/reviewer-1-coefficients.md`, `coordinator-proof-check.md`, `reviewer-2-observations.md` and `reviewer-6-adversarial.md`. The weighted coefficient lemma below is **that prior checked corollary**, not a result first proved by this note. Some broad combined reading output was truncated; no claim is made of revalidating every registry proof or line. No external theorem is newly imported; the elementary squarefree count used below is proved here.

## 1. Exact setting, including the entire refit

Fix q=2 once and for all. Let H=L2((0,infinity),dt/t²), a_n(t)=A(t/n), A(z)=integral_0^z {u}du/u, and tau(t)=1_(t>=1)log t. Real coefficients are unrestricted. Let f_N=Pi_N tau, r_N=tau-f_N, E_N=||r_N||², c_N=G^(-1)b. Norms and every Gram entry include the complete domain.

For arbitrary integers M>N>=1, let G be the old Gram, C the old/new block and D the new Gram. Set

    h=b_new-CᵀG⁻¹b_old,
    S=D-CᵀG⁻¹C >0,
    y=S⁻¹h,
    u=-G⁻¹Cy.

The actual optimizer increment has coefficient vector (u,y): old coefficients c_N+u and new coefficients y. Thus

    f_M-f_N = sum_(m<=N) u_m a_m + sum_(N<n<=M) y_n a_n,
    Delta_(N,M)=E_N-E_M = ||f_M-f_N||² = yᵀSy = hᵀS⁻¹h.    (1)

This is the complete NS53/61 block formula. In particular y is not a prescribed Möbius vector, and u is not optional. Tails, small eigenvalues and all cross terms remain in (1).

## 2. A rigorously checkable consequence, and the inverse-direction failure

The prior local weighted coefficient corollary says, for every finite real v,

    sum_n |v_n|²/n⁴ <= B ||sum_n v_n a_n||²,
    B=1536 zeta(2)².                                       (2)

Its proof uses NS78 divisor inversion and a bounded Dirichlet convolution operator; it takes absolute values of Möbius coefficients. It is regularity/conditioning, not signed cancellation.

Define positive diagonal matrices

    W_old=diag_(1<=m<=N)(m⁻⁴),
    W_new=diag_(N<n<=M)(n⁻⁴),
    L=W_new + CᵀG⁻¹W_old G⁻¹C.

For every real new coefficient vector v, the residualized synthesis has full coefficient vector (-G⁻¹Cv,v). Applying (2), with no optimization assumption on v, gives

    vᵀLv <= B vᵀSv,  hence  S >= B⁻¹ L.                  (3)

Here L is positive definite because W_new is. This calculation retains the exact old refit and complete true energy. Inverting the positive matrices reverses their order:

    S⁻¹ <= B L⁻¹,
    Delta_(N,M) <= B hᵀL⁻¹h.                              (4)

Therefore the tempting implication “better coefficient coercivity supplies the desired lower inverse-Gram gain” has the wrong direction. It supplies (4), an upper estimate in the residual-correlation variable h. A lower gain from a metric comparison needs an **upper** bound on S (as NS61 already supplies), followed by an independent lower estimate for the corrected h. The latter is unchanged.

Substitution of the actual, still unknown y into (3) also gives the valid lower bound

    Delta_(N,M) >= B⁻¹ [sum_(m<=N)|u_m|²/m⁴
                          +sum_(N<n<=M)|y_n|²/n⁴].        (5)

This is not contradictory to (4): (5) is in optimized coefficient coordinates y=S⁻¹h and (4) is in correlation coordinates h. Obtaining a lower bound on the right side of (5) remains an independent estimating task. Relabeling y as an arithmetic object does not estimate it.

## 3. Quantified test of the strongest simple new-block heuristic

Take M=2N. Even suppose, counterfactually as an unproved model hypothesis on the ACTUAL optimizer, that the new coefficients were exactly

    y_n=-mu(n),  N<n<=2N.

The new-block contribution in (5) would be exactly

    b_N = (1/B) sum_(N<n<=2N) mu(n)²/n⁴
        = [7/(24 B zeta(2))] N⁻³ + O(N^(-7/2)).           (6)

Elementary arithmetic justification: mu(n)²=sum_(d²|n)mu(d). Summing through x gives

    Q(x)=sum_(n<=x)mu(n)²
        =sum_(d<=sqrt(x))mu(d) floor(x/d²)
        =x/zeta(2)+O(sqrt(x)).

The floor errors total O(sqrt(x)), and the omitted absolutely convergent d⁻² tail contributes O(sqrt(x)). Partial summation against x⁻⁴ on (N,2N] gives (6), since integral_N^(2N) x⁻⁴ dx=7/(24N³). This calculation uses only squarefree density, not cancellation in the signs of mu.

The same order lower contribution follows if the new-block weighted distance to -mu is at most theta<1 times its weighted norm. The triangle inequality gives a factor (1-theta)². That closeness is NOT established for y. Fixed-index convergence is not a growing-block estimate, and even identification of every actual optimizer coefficient limit with -mu is already RH-equivalent in the prior audit.

The scale issue is independent of proving that strong coefficient hypothesis. NS83 gives E_N>=c/log N eventually for some c>0. Consequently the normalized certificate in (6), by itself, satisfies

    0<=b_N/E_N=O((log N)/N³),
    sum_j b_(2^j)/E_(2^j) < infinity.                      (7)

Thus even this idealized new-block piece cannot establish the needed nonsummable relative lower bound. Equation (7) bounds the size of this **particular certificate**, not the actual relative gain. The real gain could be much larger, through old refit or small-eigenvalue amplification. No upper bound Delta=O(N⁻³) is claimed.

To make the new-block part of (5) alone supply a/j relative gain for N=2^j, one would need, as a sufficient condition,

    sum_(N<n<=2N)|y_n|²/n⁴ >= B a E_N/j.                  (8)

Using n>N, (8) forces sum_new |y_n|² >= B a N⁴ E_N/j. With the NS83 floor, this is of order at least N⁴/j², or root-mean-square coefficient size at least a constant times N^(3/2)/j. This is a necessary size for USING (8), not a necessary size for actual NB convergence. The established global O(N²) coefficient l2 upper bound does not force or forbid this distribution. The point is that an O(1)-size Möbius coefficient heuristic is far below what this particular coercivity route needs.

## 4. Could the arithmetic jump defects supply the missing lower term?

For original atoms the current divisor defect at a prime p>N is exactly c_N(1), since its only old divisor is 1. More generally NS75 permits cancellation of every next-block defect by appending -delta_n while keeping old coefficients fixed. This is a concrete use of original arithmetic, unlike a generic Gram argument.

However a local derivative jump is not the residual's pairing with a complete atom or a residualized direction. The exact step gains 2<r_N,v>-||v||²; jump cancellation controls neither signed pairing nor complete cost. NS75 already certifies held-old unit-step failures, including a negative pairing at N=256 for its stated direction. After old-space refitting the cancelled jumps need not remain cancelled. These are matched failures of this simple proposed implication, not a theorem excluding all divisor-feedback estimates.

Accordingly no implication from “many forced arithmetic defects” to (8), to a nontrivial old-refit lower term in (5), or to a lower corrected correlation was obtained. The missing step cannot be replaced by assuming local energy removal adds independently across cells: a_n has a complete global tail and the prescribed refit couples the cells.

## 5. Conditional edge, tails and controls

For the actual dyadic optimizer the desired edge remains

    new proved estimates => beta_j <= Delta_(2^j,2^(j+1))/E_(2^j),
    beta_j>=0, sum_j beta_j=infinity => E_N ->0 => RH.

No beta_j with divergent sum is constructed here. Equations (3)-(7) explain why the attempted coefficient-recovery mechanism does not supply one. The missing quantities are actual arithmetic coefficients/correlations, not a discarded numerical tail.

NS87 retains the full old-row correction in its finite observations and the complete inverse S⁻¹. At T=N⁶ its coupled tail error is dyadically summable on the normalized gain scale. That allows a lower arithmetic estimate to transfer if one is proved, but no positivity is created by localization. This note uses complete norms throughout and takes no physical or Mellin cutoff; there is no additional unbounded tail error hidden in (3)-(7).

NS74 matches the Gram/coercivity-only part: unitarily changed atoms preserve the full Gram, refit and (2) for pure combinations, while altering the target loads and leaving a positive approximation floor. It does NOT preserve the original alpha=1 divisor identity, so it is not a universal refutation of an original target-sensitive arithmetic estimate. The original positive-floor possibility is also visible conditionally in NS86's bounded off-line-zero evaluator; no such zero is asserted.

NS83 excludes eventual constant whole-error contraction and eventual a/j with a>1. The attempted scale a/j with 0<a<=1 would be compatible, but remains unproved. No invented rate or effective onset is used. The hypothesis “new coefficients equal -mu” was an analytic stress test of an existing inequality, not an admitted candidate or a new numerical screen; no proposal gate, control replay, row or thaw is claimed.

## Stop decision

Retain the explicit full-refit matrix-order check (3)-(4) and the scoped certificate-scale calculation (6)-(7) as audit bookkeeping. They prevent two invalid inferences from the previously established weighted estimate. They are not a new lower arithmetic estimate or an RH advance. No numerical search is justified by them. An attempt using the old refit must provide a separate arithmetic lower estimate of that term; an attempt using corrected correlations must estimate the full signed pairing with a compatible complete cost. Naming either obligation is insufficient.

**Final classification: Same open gap — NB-GAIN / NS53/61/87.** RH, G2, the actual cofinal signed-arithmetic lower bound and both historical original-evidence recovery groups remain open. No files outside this reviewer's owned directory were edited.
