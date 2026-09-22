# NS-53 — exact block reduction; arithmetic gain remains open

Claim categories: **exact identities**, **proved implications with stated hypotheses**, and **named open input**. No new numerical illustration or certified computation. This is an analytic research checkpoint, not a proof of RH or G2.

## Ownership and reviewed baseline

Assigned to Astra / NS-53 approximation subagent by parent after board claim `fa9fa34`, in `/private/tmp/riemann-ns51-new-routes`. Only `evidence/ns53_nb_blocks/` is edited by this subagent. No manuscript, board, logs, commits, pushes or PRs by the subagent.

Read full AGENTS.md; inspected existing `evidence/diag_routes/nb/README.md`, `compute_dN.py`, and audit A3 in `origin/audit/2026-09-22-conclusions:audits/2026-09-22-conclusions-review.md`. The old archive already supplies high-precision finite distances and Vasyunin-sum Gram entries. They were not rerun or presented as new convergence evidence.

## What had to change

The historical report incorrectly treated the conjecturally sharp rate for the squared distance as a required upper bound. The established strong criterion asks only `E_N=d_N² -> 0`. A slower upper bound, e.g. `O((log N)^(-1/2))`, would suffice. An asymptotic lower bound does not impose a matching upper rate.

Adding a block also requires projecting its vectors off the entire existing span. With old Gram `G`, cross Gram `C`, new Gram `D`, and loads `b,b_B`, use

- `c=G^(-1)b`;
- corrected residual correlations `h=b_B-C^T c`;
- residual Gram `S=D-C^T G^(-1)C`;
- exact gain `E_N-E_M=h^T S^(-1)h`.

The old coefficients change by `-G^(-1)C S^(-1)h`. Treating new dilations as orthogonal, or substituting `D` for `S` in the identity, loses the old/new cross term.

## Results

1. **Exact identity:** elementary convergent arithmetic-cell series for every Gram entry, the load `(log n+1-gamma)/n`, and diagonal `(log(2pi)-gamma)/n`; proofs included. Finite independence and strictly positive finite distance are proved from jumps and Möbius inversion.
2. **Exact identity:** the block improvement and optimal coefficient update above; each test vector has the exact quotient `|w^T h|²/(w^T S w)`.
3. **Proved inequality:** for `kappa=log(2pi)-gamma`,
   `E_N-E_M >= ||h||²/[kappa sum_(N<n<=M)(1/n)] >= ||h||²/[kappa log(M/N)]`.
   No lower bound on the smallest Gram eigenvalue is required for this lower inequality. Small eigenvalues still matter for how much it underestimates the exact gain; the arithmetic numerator is not estimated.
4. **Exact arithmetic identity:** on each interval `j<=1/x<j+1`, the residual is `B_j-A/x`, with `A=sum c_n/n` and `B_j=1+sum_(k<=j)sum_(n|k,n<=N)c_n`. Integrating its square gives the full positive-cell energy decomposition. For the raw Möbius prefix the first `N+1` cells alone cost `(N+1)|sum_(n<=N) mu(n)/n|²`. This does not lower-bound the optimal distance. The raw prefix's failure is already known, not claimed as new.
5. **Proved implication:** the explicitly stated residual block-correlation hypothesis (RBC), with a nonsummable sequence of relative gains, implies convergence. The example hypothetical `alpha_j=1/[2(j+1)]` at `N_j=q^j` gives the sufficient slow rate above.

The general Hilbert-space projection identity is standard; its exact specialization and the arithmetic cell formulas identify the next estimate, rather than supplying it.

## Precise gap and scope

No asymptotic lower bound for the corrected correlations of the **actual optimal residuals** has been proved. The formulas express those correlations in arithmetic terms but do not control their cancellations with the optimal coefficient vector. Proving independent entry bounds or computing further finite distances would not fill this gap.

RBC is a sufficient open input, not asserted equivalent to or implied by RH. The trace lower bound can be too weak: the exact inverse amplifies directions belonging to small eigenvalues of `S`. The exact condition that relative block gains have divergent sum is simply convergence reformulated and is identified as such, not as a new estimate.

The missing step is the asymptotic gain estimate. This establishes **neither** failure of RBC **nor** failure of the approximation object. A block has zero gain exactly when its corrected correlation vector vanishes; strict improvement is not claimed for every block. No new Weil window or tail metric; G2 and RH remain open.

## Primary sources

- Luis Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*, [arXiv:math/0202141v2](https://arxiv.org/abs/math/0202141), [full text, Theorem 1.1 and Introduction](https://arxiv.org/html/math/0202141v2). Confirms exactly the Hilbert space and integer-dilation family used here; also records the failure of the raw Möbius partial sums. Its proof of the constructive RH direction uses RH and is not imported as an unconditional gain estimate.
- Jean-François Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, Advances in Mathematics 170 (2002), 56–70, [DOI](https://doi.org/10.1006/aima.2001.2066), [author preprint](https://arxiv.org/abs/math/0103058). A lower bound, not a mandatory matching upper rate.
- Luis Báez-Duarte, Michel Balazard, Bernard Landreau, Éric Saias, *Sur l'autocorrélation multiplicative de la fonction « partie fractionnaire »*, [author derivations](https://arxiv.org/abs/math/0306251). Relevant established autocorrelation arithmetic; the elementary cell formulas in this checkpoint are proved directly.
- Bernard Landreau and Florent Richard, *Le critère de Beurling et Nyman pour l'hypothèse de Riemann: aspects numériques*, Experimental Mathematics 11 (2002), 349–360, [DOI](https://doi.org/10.1080/10586458.2002.10504480). Existing finite-distance context only, not a convergence theorem.

## Validation responsibility

`proof.tex` is a self-contained manuscript fragment using existing theorem environments and `hyperref`. Parent integrates, runs the actual manuscript build, records pages and undefined/duplicate-reference counts, and manages manifests. This subagent has not replaced that build by source validation.

A standalone wrapper around the proof fragment was compiled successfully on 22 September 2026 UTC: **3 pages, 0 undefined references, 0 duplicate references**. This is a fragment check, not the required complete manuscript build. The HTML's operating-system browser-open attempt failed because this environment has no compatible default browser; the file was subsequently queued in the Codex preview panel.
