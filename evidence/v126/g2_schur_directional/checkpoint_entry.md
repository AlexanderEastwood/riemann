## Current research checkpoint: September 21, 2026 — v1.16 complete fixed-window positivity

**Closed: the signed head/complement positivity obligation for the complete canonical Weil form at lambda=3, including both parity sectors and every omitted Fourier mode. G2 along unbounded windows and RH remain open.** The full manuscript is v1.16, 129 pages, with 32 main sections, two appendices, 407 unique labels and all 72 historical claim dispositions retained.

### Starting point and selected obligation

Fresh reads of the saved v1.15 manuscript, research log, notes and bundle confirmed the current versions before work began. v1.15 supplied the canonical logarithmic-domain operator, a positive entire Fourier tail, ordinary source mass and a small full source residual. It did not certify the signed head/complement correction. This continuation targeted that concrete missing fixed-window estimate, following the previous log's proposed inverse-action/moment route. Three internal agents supplied an independent numerical pilot, the remote-moment proof and an adversarial audit. No positivity, zero-location or RH assumption was introduced.

### Proved: a stronger independent arithmetic tail bound

Proposition 20.22 applies the positive-weight Schur test to the actual truncated prime translations on [0,L], L=2 log 3. With phi(x)=cosh(x-log 3), the exact prime norm bound is

`m3=(85/116)w2+(65/87)w3+(193/232)w4+(137/145)w5+(35/29)w7`, where `wm=Lambda(m)/sqrt(m)`.

It is between 2.6890557719319011796 and 2.6890557719319011797. On each physical shift interval the weighted ratio is monotone; its one-sided endpoint values are rational combinations of the six actual prime-power weights. All comparisons and resulting tail constants were enclosed by 256-bit Arb arithmetic. The m=8 term is included wherever active; the full-length m=9 shift is exactly zero as an L2 operator. This improves the entire-tail bounds at N=256 to more than .4970 for all vectors and 2.0690 for even vectors, and at N=512 to more than 1.1907 for all vectors.

Proposition 20.23 preserves the frequency-dependent archimedean diagonal rather than replacing it by its minimum. With the base cut N retained in all norm losses, `T >= Dg`, where

`g_n=log(|n|/L)-E_L(2*pi*|n|/L)-kappa`.

The constant kappa is m3 plus the common archimedean error; the odd/full case also retains pi/2 and the negative-pole tail cost. The positive weights increase with |n|. The variational inverse formula gives `T^(-1) <= Dg^(-1)` on the entire infinite complement. This is stronger than substituting a scalar gap into every residual row. It does not infer inverse order from positivity of a remote subblock alone.

### Proved: a directional bound for every remote residual row

Proposition 20.24 starts from the exact off-diagonal identity `W_nm=(b_n-b_m)/(n-m)`, keeping the separate diagonal for finite rows. For a finite lift G supported in |m|<=M, it retains the moments

`S_j=sum (m/M)^j G_m`, `T_j=sum (m/M)^j b_m G_m`.

The exact finite geometric expansion through order r has a leading Gram built from

`H_jk=M^(j+k)[1+(-1)^(j+k)] zeta(j+k+2,J+1)`.

The PSD upper bound is `(1+tau)[2B_*^2 S*HS+2T*HT]+(1+tau^(-1))delta^2 G*G`, where

`delta^2=8B_*^2 c_(M,r) M^(2r) zeta(2r+2,J+1)/(1-M/(J+1))^2`,

and `c_(M,r)=sum_(|m|<=M)(|m|/M)^(2r)`. The factor eight, both signed tails, the zero Fourier mode and every normalized parity sqrt(2) factor were independently checked. This is a quadratic-form bound for all input directions, not independent entrywise errors or a scalar norm times the identity.

Proposition 20.25 combines this with the exact signed identity. For `G=I_head-Z`, `R=Q_N W G`, and `K_Z=F-B*Z-Z*B+Z*TZ`, it proves

`K >= K_Z-sum_(N<|n|<=J) R_n*R_n/g_n-U_remote/g_(J+1)`.

All finite residual rows are present, including the nonzero middle residual from freezing an interval solve to a dyadic matrix. Z has finite support and therefore belongs to the proved operator domain. Square completion extends a finite lower certificate to the whole closed form.

### Computer-assisted result: complete coercivity at lambda=3

Proposition 20.26 certifies the actual complete Weil form, not just a Fourier compression. It uses the following exact parameters:

| Sector | Head dimension | N | M | J | r | Positive LDL pivots |
|---|---:|---:|---:|---:|---:|---:|
| Even | 257 | 256 | 512 | 4096 | 80 | 257 |
| Odd | 512 | 512 | 1024 | 4096 | 100 | 512 |

The two certificates use tau=1/1000000 and the earlier conservative global sequence bound B_*≈2.118745185946. The geometric remainder factors are below 1.656e-148 and 3.288e-124 respectively. These factors bound only the geometric remainders; the much larger leading moment Grams are included in full.

Every matrix entry is enclosed with Arb. The archimedean coefficient evaluation retains the exact digamma/trigamma part and 128 exponentially weighted terms, followed by explicit uniform radii. Every actual shorter prime-power shift and the separate logarithmic diagonal are retained. The new sequence assembly was compared with the previous independent integration certificate through N=64: all 8,321 even/odd entries overlap their reference enclosures. That consistency check supplements the analytic assembly proof.

The exact dyadic midpoint of the intermediate inverse solve is frozen as the witness. Every LDL pivot of the final lower matrix is strictly positive. The minimum pivot is approximately 9.17498693948e-9 (even) and 9.68026341053e-8 (odd). These are **not eigenvalue lower bounds**. Positive finite Schur matrices, the positive entire tails and the boundedly invertible square-completion map establish the existence of an epsilon_3>0 for the full closed form. No numerical value of epsilon_3 is asserted.

An independent agent replayed the identical witnesses at 896 bits, after the original 768-bit checks; all 769 pivots again pass. Their uncompressed exact-witness SHA256 values are:

- Even: `993c5b325c1cc7dce64c1dbdab9384dd54dea6a480cce8739cf623e9e8bce43c`.
- Odd: `4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea`.

The witnesses, every pivot enclosure, assembly code, analytic derivations and replay reports are preserved in the cumulative bundle. This is internal mathematical and computational verification, not external referee review or proof-assistant formalization.

### Attempts that failed, and what those failures mean

1. Finite-output pilots were positive in the even N256/M512/J1024 case, but those calculations omitted every row beyond J. They were not treated as continuum certificates.
2. The first full even scalar-gap budget, with J1024/r128, had a rigorously negative LDL pivot at index 7. Increasing J to 4096/r80 moved the failure to index 28. The later diagonal inverse weighting passed with the same larger J. The earlier failures reject their conservative sufficient bounds, not the Weil operator.
3. The odd finite-output budget at N256 with a scalar gamma=.4970 failed. A larger N512/M1024/J2048 finite-output pilot passed, but its full remote scalar majorant failed at index 23. Even diagonal weighting at N256/M512/J4096 failed at index 41. The successful odd architecture uses N512/M1024/J4096/r100 and the growing diagonal weights.
4. Double-precision eigensolvers can report spurious negative values near 1e-15 where the energy scale is about 1e-38. Float vectors contaminate this energy at about the square of their ordinary error. Only certified ball arithmetic and the analytic tail bounds are used for the new sign result.
5. A sharper remote bound from the asymptotic trigonometric b sequence and exact Lerch sums was considered but not needed. It was not presented as a proved new certificate. Large-order special-function balls would need their own precision budget. Positive Hilbert finite-rank inverse refinements and annular weights are also optional future improvements, not inputs to this result.

### Primary-source research and adverse checks

The recent primary preprint [Weil positivity in compact windows](https://arxiv.org/html/2608.24827v2) was reviewed as an alternative certified-tail strategy. Its revision explicitly retracts an earlier larger-window claim and distinguishes finite-matrix evidence from continuum bounds. No certificate or asymptotic assertion from that paper is used here. The present proof instead controls the actual Fourier operator via physical prime shifts, diagonal inverse order and explicit remote moment Grams.

Adversarial review checked the weighted prime ratios, every finite comparison, archimedean and pole constants, common base-cut losses, inverse order, exact dyadic freezing, all intermediate residuals, source-independent moment inequalities, complex parity normalization, complete diagonal, series tails and the form-domain square completion. No blocking issue was found. An independent run verified both final certificates at higher precision using unchanged witnesses. The original first-slot-linear convention, physical endpoint, Fourier cut and corrected sampler graph defect remain in force.

### Integration and remaining target

The abstract, status, Section 20, Section 32 goals and reproducibility appendix now distinguish completed fixed-window positivity from the unresolved growing-window problem. The new proofs are on pages 67–73; the reproduction summary is on page 124. The full 129-page PDF was rendered and visually inspected, with close review of all new proof pages. One incomplete PNG was rerendered; the PDF itself compiled without warnings. All 407 references/labels are consistent, and all 72 historical ledger dispositions are retained apart from the release heading.

**Next concrete step:** use the same entire-complement machinery for W-aI at a rigorously chosen positive threshold. Subtract a from both the actual diagonal and every tail lower weight. A positive odd certificate plus an even negative-index bound and a certified even trial quotient could establish parity and simplicity of the actual fixed-window bottom. Do not infer its ordering from a source residual or from LDL pivot magnitudes. After that, test a larger window with a complete error budget and seek a uniform estimate rather than extrapolating isolated successes. G2 ultimately needs lower error tending to zero along an unbounded window sequence, or a quantitatively adequate independent ground-space overlap. Source-to-ground endpoint stability, growing-block estimates and alternative metric/shell sign routes remain open. No RH proof is claimed.

