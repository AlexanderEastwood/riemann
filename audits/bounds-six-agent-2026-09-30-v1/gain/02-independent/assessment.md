# Independent gain review 02 — structured-phase cancellation import

**Outcome: no independent arithmetic lower-gain mechanism admitted. Stop without a numerical candidate.** I checked whether unconditional Möbius orthogonality to structured phases supplies a different entry into the signed projected cost. The explicit transfer below still loses a factor of N, before addressing the separate residual numerator. This is a bounded applicability assessment, not a theorem that the method cannot be adapted.

**Wall check: Same open gap.** Closest results: NS53/61/87 for actual optimized gain; NS92/93/98 for the selected Möbius cost and companion margin. What changes: a source-level check of Davenport/Green–Tao structured-phase estimates, rather than repeating the already-audited Chowla, short-interval or cotangent substitutions. No new cofinal estimate, thaw or RH advance.

## Scope reviewed

Reviewed public commit `769359298fada57711b6895c4bde3fabe2cc5168`, in `/private/tmp/riemann-prime-folding-review-20260930`. The current AGENTS, full conclusion/input register, README, freeze conditions and evidence ledger were reviewed earlier in this same independent review session and retained unchanged. For this assignment I reread NS87, NS91, NS93/98, their inherited NS92 cost bounds, and the prior `nb-bottleneck-team` literature feasibility, Möbius-cancellation-transfer and Estermann applicability audits. I did not read gain01, run a numerical screen, revalidate historical certificates, or recover either missing-original group.

## Target and the genuinely arithmetic source

Keep the original fixed q=2 space, target `tau(t)=1_(t>=1) log(t)`, atoms `a_n(t)=A(t/n)`, actual projection Pi_N and residual r_N. With E_N=||r_N||², the complete old/new Gram blocks give

\[
H_N=D-C^TG^{-1}C,\qquad h_n=\langle r_N,(I-\Pi_N)a_n\rangle,
\qquad \Delta_N=h^TH_N^{-1}h.
\]

The selected vector remains `d_n=-mu(n)log(2N/n)` for `N<n<=2N`, with exact complete cost K_N=d^TH_Nd and numerator ell_N=d^Th. The cost contains the entire old refit; it is not replaced by a raw fractional-part kernel.

[Green–Tao, *The Möbius function is strongly orthogonal to nilsequences*, Annals 175 (2012), equation (1.1) and Theorem 1.1, pp. 542–543](https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p03-p.pdf) records the uniform Davenport estimate

\[
\sup_{\alpha\in\mathbb R}\left|\sum_{n\le X}\mu(n)e(\alpha n)\right|
\ll_A X(\log X)^{-A}\quad(A>0).
\]

Its nilsequence extension retains dimension, filtration degree, rationality and Lipschitz-complexity dependence; the constant is ineffective. I read the stated quantitative theorem, not merely its abstract. Neither statement permits arbitrary N-dependent residual weights at unchanged cost. The Möbius cancellation is the arithmetic step: a generic coefficient sequence can align with a phase and defeat it.

## Explicit attempted transfer, including the scale loss

Put alpha=log 2 and B_N(m,n)=N(H_N)_(m,n). Suppose, as an additional UNPROVED kernel approximation, that on the full new block

\[
B_N(m,n)=\sum_{\nu}c_{\nu,N}e(\xi_{\nu,N}m+\eta_{\nu,N}n)+R_N(m,n),
\quad L_N=\sum_\nu|c_{\nu,N}|,\quad \|R_N\|_\infty\le\epsilon_N.
\]

A finite double Fourier expansion always exists with R=0. That fact gives no useful bound on L_N and is not an arithmetic estimate. It is not established here that the changing Schur complement has small Fourier/nilsequence complexity.

Partial summation transfers Davenport's estimate to the fixed logarithmic taper, whose supremum and total variation are bounded independently of N. For every fixed A,

\[
\sup_\xi\left|\sum_{N<n\le2N}\mu(n)\log(2N/n)e(\xi n)\right|
\ll_A N(\log N)^{-A}.
\]

Substituting the COMPLETE projected kernel and keeping signs until this estimating step gives

\[
0\le K_N\ll_A L_N\frac{N}{\log^{2A}N}+\alpha^2N\epsilon_N.
\]

The remainder bound follows from `||d||_1<=alpha N`; the prefactor 1/N is retained. Thus even the favorable hypothetical bounds `L_N=O(log^B N)` and `epsilon_N=0` leave an allowance `N/log^(2A-B)N`, not O(1). Averaging it over `N=2^j`, `J<=j<2J`, does not turn it into a bounded allowance. This does **not** imply that K_N diverges. Taking A=A(N) is not permitted by a theorem with A-dependent constants and onset.

A sufficient completion of this particular transfer would need bounded dyadic-index means of `L_N N/log^(2A)N + N epsilon_N` for one fixed A, or a more targeted bilinear estimate that avoids the displayed loss. Neither was derived. Replacing linear phases by nilsequences additionally requires verified complexity control and does not automatically improve the logarithmic saving. No such representation or cancellation estimate for the original optimized residual was found.

## The companion input and inverse-metric error cannot be skipped

Even a completed bounded-average cost estimate would only supply MOBIUS-COST. For example, with the actual signed ell_N define `r_j=(ell_(2^j)/E_(2^j))_+`. A compatible sufficient pair is

\[
\sum_{j=J}^{2J-1}K_{2^j}\le CJ,
\qquad \sum_{j=J}^{2J-1}r_j\ge\varepsilon J
\]

for fixed C,epsilon>0 and every sufficiently large dyadic J. Exact line search gives gamma_j>=r_j²E_(2^j)/K_(2^j); the inherited critical-zero lower bound and weighted Cauchy–Schwarz then give persistent aggregate gain, as in NS93. Directions with zero cost are omitted. This is the existing conditional edge, not a new criterion. The source above supplies no lower bound for ell_N and no substitute for the second hypothesis. NS74 specifically blocks treating a Gram/cost estimate alone as original-target gain; NS83's restrictions still apply.

For a direct full-block approach, a convenient sufficient condition for a model observation vector h_* at scale sqrt(E_N/log N) is

\[
\|h-h_*\|_{H_N^{-1}}=o\!\left(\sqrt{E_N/\log N}\right)
\]

and an independent positive lower estimate for ||h_*|| at that scale in the SAME metric. Little-o is not necessary: if ||h_*||_(H^-1)>=b sqrt(E_N/log N) and ||h-h_*||_(H^-1)<=a sqrt(E_N/log N) for fixed 0<=a<b, the reverse triangle inequality already gives Delta_N>=(b-a)^2 E_N/log N. Entrywise logarithmic savings are not either of these statements; converting them introduces the full inverse-Gram loss. NS87 already makes the complete physical tail harmless at T=N^6, with old-coordinate rows retained. That localization does not estimate the interior. For the selected direction, NS91's grouped tail at N^6 is likewise negligible; no margin bound for its remaining interior pairing was obtained here.

## Decision

The actual arithmetic source is valid and different from the prior literal imports, but its direct use does not meet the scale or the target. Do not compute Fourier complexity, a larger Möbius table or a new phase scan on the strength of this note. A reopening needs an independently motivated kernel/correlation estimate strong enough after the explicit losses and a compatible actual numerator mechanism. I found none in this bounded attempt and recommend no next numerical candidate.

The hypotheses of Davenport–Heilbronn and the theta controls do not match this literal original Möbius/atom construction; no control pass is claimed. NS74/83 are the relevant existing safeguards. RH, G2, the signed cofinal gain input and both historical original-evidence gaps remain open.
