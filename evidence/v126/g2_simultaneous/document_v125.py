from pathlib import Path
import json
B=Path(__file__).resolve().parent
far=json.loads((B/'window_scaling_far_cuts_b384.json').read_text())
rows=[]
for lam in [3,4,5,6,8]:
 p=B/f'window_scaling_l{lam}_even_r256_o384_b4096.json'
 r=json.loads(p.read_text());f=next(x for x in far if x['lambda']==lam)
 margin=r['dimensionless_generalized_margin_FINITE']
 label=f'{margin:.6g}' if margin>0 else 'below double-precision resolution; see diagnostic record'
 rows.append(f"| {lam} | {r['head_dimension']} | {label} | {r['log10_condition_V_diagnostic']:.5f} | {r['reference_first_column_headroom_FINITE']:.6g} | {f['sectors']['even']['first_positive_N']} | {f['sectors']['odd']['first_positive_N']} |")
table='\n'.join(['| Window | Head dimension | Finite relative margin | log10 cond(V) | Reference-column headroom | First admissible even N | First admissible odd N |','|---:|---:|---:|---:|---:|---:|---:|']+rows)
report='''# Growing-window diagnostics for v1.25

The complete even certificate at lambda=4 is separate from this finite study. Its rigorous generalized margin exceeds 0.62629 and includes every residual row. The following margins instead compare **finite** Schur complements at retained/test cutoffs 256/384, with even heads through lambda squared. They omit all modes beyond 384 and are not complete inverse upper bounds. In particular, the finite lambda4 margin below is not supposed to equal the complete-trial margin.

'''+table+'''

The finite eliminations and head signs are interval-positive at 4096 bits with 192 archimedean series terms. Displayed condition numbers and margins are midpoint numerical diagnostics, except any separately stated rational or interval threshold in the JSON records. The far-cut columns are rigorous scalar analytic thresholds, freshly verified at each window at both 320 and 384 bits. They certify only the remote block, not the growing intervening head or inner inverse factors.

The generalized relative margin is invariant under a common invertible head congruence. Separate ratios of minimum eigenvalues and the displayed condition of V depend on coordinates. The reference column is the first canonical head direction after its specified energy normalization; it is not the archived v1.24 physical direction. The latter has complete headroom >12.1284 for the new lambda4 trial, compared with about22.71 for the old single-column trial. Trial dependence is distinct from congruence dependence.

The finite margins decline from lambda3 through lambda6. At lambda8, computing 1-theta in double precision rounds the margin to zero and produces tiny signed artifacts; these are not negative-form certificates. The interval head test is positive. An independently replayed frozen-vector Rayleigh upper and interval LDL lower give the rigorous finite bracket 5.697e-101 < margin < 5.755e-101. This resolves the finite scale without interpreting binary64 signs. It is not an infinite-tail or asymptotic conclusion. Large head condition numbers mean ordinary coordinates cannot be compared by raw pivots. Neither the observed decline nor the positive finite signs settle the complete growing-window estimate.

The method-specific cutoff theorem is stronger than extrapolating this table: for fixed c<1 the present scalar far weights require N+1 > L exp(M_phi/(1-c)), hence liminf log((N+1)/L)/lambda >= 1/(1-c). This proves an exponential cost for this majorant, not a general impossibility result.

Next: improve the signed far comparison or build and bound the growing inner witnesses at this cost. A complete odd lambda4 certificate remains a separate local target. A cofinal ordinary-error estimate tending to zero remains the RH target. No unverified lambda4 constants were transferred to another window.
'''
(B/'window_scaling_report.md').write_text(report)
entry='''## Current research checkpoint: September 21, 2026 - full manuscript v1.25

**Local obligation closed:** the COMPLETE even-parity Weil form at lambda=4 is strictly positive/coercive on its form domain. This covers the whole 17-dimensional outer head and every infinite tail mode. It extends v1.24's one-direction result; it does not establish the odd sector, full W4 positivity, G2, or RH.

**Exact identity and certificate:** for the actual frozen trial matrix G, V=P16 G, E=Q16 W4 G and K=G* W4 G, V* S_infinity V=K-E* T^(-1)E. The actual V is interval-certified invertible. All trial columns are finite Fourier vectors in the operator domain; completing the coercive tail square is valid on the closed form domain. The complete tail floor and archimedean shift are the previously certified ones, with the shift used only to upper-bound the inverse; K and E remain unshifted.

**Witness:** normalize the old even trial by its head energy BEFORE generating 16 finite preconditioned-CG corrections, support4096, candidate512bits. Freeze both the rounded base and corrections as exact dyadics. Rounding the base defines a nearby exact trial, not an assumed exact old congruence; the actual head is checked. Reconstruct the same frozen coefficients at768/896bits, retain all residual cross-Grams throughJ65536, and enclose every omitted row by the order64 moment theorem. With mu=.9999999999, rho<.165102333 and tau=.1, all17 pivots of K-U_tau are positive, the smallest >.7645944101. This is a coordinate pivot, not an ordinary spectral gap. Independently certify the exact rational gate U_tau < (1-62629/100000)K at both precisions. This gives complete generalized margin >.62629. Nine dense physical-row checks and provenance checks are retained.

**Joint remote estimate proved:** one joint Gram Gamma >= [Y,y]*[Y,y], together with 0<=L_Y<=Y*Y and A0=mu I+L_Y-Gamma_YY>0, yields complete inverse upper V_J+Gamma_kk+(H-Gamma_Yk)* A0^(-1)(H-Gamma_Yk). Its proof applies the joint Gram to(-z,x) in a variational supremum. A shared cross block is essential. Adversarial review corrected the printed hypothesis to L_Y>=0, needed for the scalar inverse corollary. Implementations already used L_Y=0. An optional768bit joint-Gram check has smallest pivot >.7892519172 using the scalar denominator and >.7892519657 with the full denominator; these are additional checks, not prerequisites for the main two-precision even result.

**Failed or inconclusive attempts:** independently corrected unscaled even columns did not give a positive whole-head gate; the energy-scaled-before-CG construction resolved that problem. Odd4step and16step trials atsupport4096 remain inconclusive (best gates fail around head indices4/5 and10/11 respectively). These are failures of majorants, not negative Weil vectors. The canonical even and odd4step trials give only ordinary negative-error bounds of1e-17 and1e-12, respectively. They do not prove exact signs. No whole-space epsilon4=0 is claimed. The odd witness has its own certified inner factors and remote rho about.041200151; even constants were not transplanted to it.

**Growing-window work:** priority shifted per the user's request to lambda=3,4,5,6,8. Fresh scalar far thresholds give evenN44,283,1502,7488,124442 and oddN209,1360,7224,36021,598623. Both positive-at-N and negative-at-N-1 gates replay at320/384bits; monotonicity proves minimality for this formula. Analytically proved that the present scalar far bound forces exponential cutoff growth, using the previously established prime norm/lambda ->1. This restriction belongs to this majorant, not every possible G2 method.

'''+table+'''

**Finite diagnostic scope:** the displayed Schur study uses heads throughlambda² and fixed cuts256/384, not the full4096/65536 pipeline. Every finite eliminated tail and resulting finite head is interval-positive. All omitted modes beyond384 remain absent from this probe; these finite correction matrices are not complete upper bounds. Complete growing-window witnesses, mu/rho/moment constants and ordinary error rates are still missing. Conditions and raw-energy logs are diagnostics, not lower eigenvalue certificates. The reference-column headroom in this table is not the old v1.24 direction. Healthy one-direction headroom alone does not distinguish conditioning from other bad directions. The simple diagonal counterexample in the manuscript makes these quantities independent.

**Numerical reliability:** early2048bit scaling attempts and interval-LU lambda8 solves had broad interval metrics and were rejected. A verified preconditioned solve resolves finite lambda8 positivity; the double-precision subtraction1-theta cannot resolve its very small relative margin. A100-digit inverse-metric proposal, followed by a frozen-vector Rayleigh upper and an independent interval LDL lower, rigorously brackets the FINITE generalized margin between5.697e-101 and5.755e-101. The metric/probe witness is saved and replayed. Thus a substantial loss is present for these fixed cuts, but neither an infinite correction nor an asymptotic decline has been certified. An adverse review caught an unsafe floating maximum in the auxiliary trace bound; it was replaced by the analytic upper1+65e-20 from the certified normalized metric, and the saved trace bound was regenerated. Decimal serialization of the normalized metric widened intervals enough to defeat naive LDL; replay uses a certified triangular congruence before LDL and a separate frozen-vector Rayleigh upper, so the bracket survives reloading its witness. This did not affect the main lower gate or Rayleigh upper. The local python-flint generic power of a tiny zero-centred ball could return NaN; using x*x in the new LDL avoids false inconclusive gates. Prior positive gates could not have accepted NaN, so this was not a discovered false-positive certificate. Candidate floats select congruences only; every accepted proof gate is outward interval arithmetic.

**Review and integration:** independent adverse review checked full operator/form-domain implication, dyadic actual-head rank, scale/parity/zero-mode factors, complete residual majorants and rational margin. The L_Y hypothesis correction was applied before final integration. Full v1.25 retains all496prior labels,72historical ledger dispositions and the explicit sampler graph defect. The complete166page PDF was compiled and all pages rendered, with new proofs/tables inspected at full size. No publication or external contact.

**Next concrete target:** produce complete window-specific inner inverse certificates and a controlled residual-family estimate, or improve the signed far comparison to avoid the current exponential head cost. Do not extrapolate the five finite windows or reuse lambda4 mu/rho without proof. Finishing oddlambda4 remains a separate local milestone. The local even sign gap is closed; no global G2 sign gap or RH proof is closed.

---

'''
p=B/'RH_G1_G2_research_log.md';old=p.read_text();head='# RH manuscript research log\n\n';assert old.startswith(head);p.write_text(head+entry+old[len(head):])
notes='''# Revision notes - full manuscript v1.25

September21,2026. Complete166-page working manuscript.

- Certified strict positivity of the entire even-parity Weil form at lambda4, including every infinite residual row, using a simultaneous17-column frozen trial. The odd sector remains open.
- Certified complete generalized margin >0.62629 for the same witness at768/896bits. Coordinate LDL pivots are not identified with ordinary spectral gaps.
- Proved a joint-remote-Gram estimate retaining correlated residual terms; stated its required positive lower-Gram hypothesis explicitly after adverse review.
- Proved exponential cutoff cost for the current scalar far majorant and freshly certified its thresholds at lambda3,4,5,6,8.
- Recorded a separate finite-only growth study, condition numbers and declining margins. It does not supply missing complete tail certificates or a cofinal error estimate.
- Integrated abstract, status, proofs, next targets and reproduction appendix; preserved all496prior labels and72historical claim dispositions. Compiled and visually checked the full PDF.

One local complete even-sector sign obligation is closed. Full lambda4 positivity, growing-window G2 and RH remain unproved. Weak G1, physical endpoint, Fourier cut, logarithmic diagonal, scale factors and explicit sampler graph defect are preserved.

---

'''
p=B/'v1_revision_notes.md';p.write_text(notes+p.read_text())
print('Updated notes, log, and finite scaling report.')
