from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent
old=(B/'input/RH_G1_G2_research_log.md').read_text()
entry=r'''## Current research checkpoint: September 21, 2026 - full manuscript v1.22

**Selected obligation:** Step 1 of the user's plan: bound the complete lambda=4 low-mode Schur correction, starting from the signed inverse refinement. Freshly recovered the authoritative v1.21 manuscript, research log and cumulative evidence bundle. Replayed the exact dyadic negative witnesses for the old optimistic ceilings K_X-V_J at outer support256,512,1024. Their signs reproduce; they are failures of those majorants, not negative Weil directions.

**Established analytically and with interval constants:** Retaining parity signs sharpens the complete shifted far sandwiches from m=67 to20 on even n>512 and from335 to90 on odd n>1536. The ratios are below19.215607 and89.840960, respectively, verified at320and384bits. The positive even pole tail contributes at most hL^3/(12pi^4 N^3); the odd limiting Hilbert matrix and odd pole term are nonpositive in an upper bound. The shift cD acts only on the exact archimedean diagonal. The new inverse-polynomial error factors are(19/20)^k and(89/90)^k. These constants apply at one fixed window; they assert no growing-window uniformity.

**Established finite-prefix estimate:** For H=D_g^(-1/2)UD_g^(-1/2)-I>=0, prefix p, omitted q, a=<Hp,p>, v=||p||^2, ||q||^2<=E, and Q_JHQ_J<=nu_J Q_J, positivity gives <H(p+q),p+q> >= [sqrt(a)-sqrt(nu_J E)]_+^2. Thus the complete first inverse-polynomial contribution is bounded above by v+E minus one twentieth of this square in the even sector. A matrix Young version and a relative matrix-tail version are proved; scalar positive parts must not be replaced by an unjustified matrix positive part. The remote nu_J retains the original kappa_N in D_g and improves only the far remainder at J.

**Concrete certified progress:** On the archived even head direction formerly obstructing the diagonal majorant, using the frozen support256 solve, the complete shifted far energy now satisfies

`<U^(-1)k,k> < 5.758e-20 < 6.469e-20 < K_X(v,v)`.

This gate includes every residual row beyond J65536 using the order64 infinite moment bound. The enclosed values are K=6.4692843941586476e-20, prefix V=6.9332416283028267e-20, prefix <Hp,p>=4.0338113722023497e-19, remote norm-squared upper3.4797080872158321e-21, remote H norm upper1.987323729731466, complete first-polynomial upper5.7578877881088833e-20. The strict remaining budget exceeds7.11396606049e-21. Identical exact dyadic inputs replay at768and896bits. This removes the old far-energy obstruction on ONE direction only. The refined mixed square has NOT been included, and no simultaneous head-matrix sign is certified.

### Attempts and failures retained as research history

- J4096: prefix V6.81404407434e-20, AP3.97732748593e-19, remote norm bound1.12794423584e-19 and nu4.04915505817. The reverse-triangle lower improvement is zero; the resulting far upper1.80934864327e-19 exceeds K. This is an inconclusive enclosure, not failure of the true inverse or even of the first polynomial.
- J16384: AP4.02588642283e-19 and the complete AP lower1.69260219267e-19 are positive, but the far upper7.93789328887e-20 still exceeds K. Extending the certified prefix, rather than increasing precision, resolves this particular enclosure obstruction atJ65536.
- A scalar refinement cannot be subtracted from the old structured energy while freezing its mixed term. For any U^(-1)<=Q_*<=D_g^(-1), the valid whole bound is k*Q_*k+mu^(-1)||C(h-Z*k-R*Q_*k)||^2. Both appearances must change. The original finite certificate survives because K_Z-R*Q_*R>=K_Z-R*D_g^(-1)R>=L_lower. Its closed-form/domain justification is supplied in the manuscript.
- The adverse review also derived a sharper scalar bound using prefix-tail orthogonality and a first-polynomial failure test. These auxiliary directions are recorded in adversarial_first_inverse_review.md. They are not asserted as completed G2 work.

### Verification and scope

The new matrix actions use four outward Arb polynomial products for the exact Toeplitz divided-difference and Hankel parts; a dense25row calculation independently checks indexing and the opposite-sign parity diagonal. The original assembly's archimedean-series remainder, logarithmic diagonal, Fourier normalization and shift are retained. No floating sign decision, zero list or RH assumption enters the directional gate. The adverse agent checked the pole factors, original kappa_N, scalar/matrix distinction, convolution indexing and general Q_* form-domain argument. Its request to state nu>=0 explicitly was incorporated.

The complete manuscript is v1.22,156pages. The title/status, abstract, Section20 proofs, Section32 targets and reproduction appendix were integrated together. All466 prior labels and72 historical claim dispositions are retained. Weak G1, the physical endpoint, first-slot-linear convention and explicit sampler graph defect remain unchanged. The revised complete PDF compiles with resolved references and no box warnings; final visual inspection is recorded in the validation file.

**No G2 sign gap was closed.** The entire low-mode Schur matrix at lambda4 is still open, as are the cofinal growing-window estimates. No RH proof is claimed.

### User-supplied whole-head LDL proposal

During this work the user relayed Claude's suggestion to replace a theta_X eigenvalue estimate by interval LDL. The equivalence is correct when K_X is positive definite and C_X is the COMPLETE r*T^(-1)*r: theta_X<=1 iff K_X-C_X>=0. The manuscript now states the concrete sufficient gate: construct a form-order upper enclosure Cbar_X>=C_X and certify K_X-Cbar_X>=0. Strict positive LDL pivots suffice and prove a stronger strict inequality. An entrywise upper bound is not a form-order upper enclosure; an interval containing a zero pivot is not a semidefinite certificate. For a tail compression, r_M*T_M^(-1)*r_M<=C_X, so its uncorrected finite LDL sign does not close the infinite-tail gap. The reported crude upper bound about1.75 and numerical theta about0.9998 were not supplied as replayable complete-tail matrices and are not imported as certificates.

The user then reported positive interval LDL for ret:omit64:96,64:128,64:160,64:192, claiming the complete S_infinity and noting that the64:160 minimum pivot1.3832e-58 matches F-68's finite nmax160 low_block. The source code and an enclosure of modes beyond omit were not supplied or recovered by the targeted file search. Agreement with a finite low_block is consistent with finite Schur-complement associativity and does not by itself establish inclusion of the infinite remainder. The claim is recorded as user-reported, pending inspection of the actual correction upper enclosure. If that enclosure really covers the complete tail and the correct whole-head form, the LDL result would close the fixed-lambda4 sign; it would still not establish growing-window uniformity or RH. No categorical claim is made that the user's computation omitted the tail; its scope is not evidenced by the supplied table.

### Next concrete step

Evaluate C(h-Z*k-R*Q_1*k) for the same frozen head direction, where Q_1=D_g^(-1/2)(I-H/20)D_g^(-1/2). Enclose remote correlations jointly rather than discarding them or treating small ordinary residual norm as sufficient. The mixed square divided by mu must fit within the certified remaining7.11396606049e-21 budget (or a sharper inverse polynomial must be used). Then extend to the whole17-dimensional even head and16-dimensional odd head through a simultaneous Gram/congruence certificate. Only after complete fixed-window sign gates should a growing-window estimate be claimed; the actual head dimension, C norm, mu and arithmetic rescaling must remain in that estimate. A cofinal complete-Weil lower error tending to zero would imply RH directly; the conditional Riesz/evaluator route retains its separate assumptions.

---

'''
assert old.startswith('# RH manuscript research log\n')
(B/'RH_G1_G2_research_log.md').write_text('# RH manuscript research log\n\n'+entry+old.split('\n',1)[1].lstrip())
notes='''# Revision notes - full manuscript v1.22

September21,2026. Complete156-page working manuscript; no G2 sign gap closed.

- Proved sharper full far-inverse constants20even/90odd atlambda4, replacing67/335 for the same operator and weights.
- Proved finite-prefix scalar and matrix estimates with every omitted residual row enclosed.
- Certified a complete far-energy comparison on one previously obstructing even head direction: upper5.758e-20 is below trial energy6.469e-20. This does not include the structured mixed term or certify the entire head matrix.
- Proved that an improved inverse must replace both inverse occurrences in the structured bound, retaining the original finite certificate and closed form domains.
- Added the user's whole-head LDL acceptance test, requiring a form-order upper enclosure of the complete correction; no eigenvalue estimate is necessary.
- Integrated the abstract, current status, Section20, Section32 and reproduction appendix; preserved all72 historical claims and all prior labels.
- Checked constants at320/384bits and the exact same directional witnesses at768/896bits. Internal adverse review checked signs, parity/scale factors, complete remote terms and form domains.

Still open: refined mixed correction, simultaneous low-head Schur sign, and uniform estimates on growing windows. No RH proof or new global positivity claim.

---

'''
(B/'v1_revision_notes.md').write_text(notes+(B/'input/v1_revision_notes.md').read_text())
readme='''# Reproduce v1.22 inverse refinement

Run from this directory after extracting the cumulative bundle. Requires Python, python-flint (Arb), and LaTeX for the full PDF.

```sh
python3 refine_inverse.py --mode constants --bits 320
python3 refine_inverse.py --mode constants --bits 384
python3 refine_inverse.py --mode probe --bits 768 --J 65536
python3 refine_inverse.py --mode probe --bits 896 --J 65536
python3 integrate_v122.py
python3 build_complete_pdf.py
```

The scripts reuse the archived g2_low_schur exact witnesses and assembly. Large65536-coefficient caches are reproducible in about2minutes and are omitted from this increment. The complete original bundle and its earlier evidence remain preserved. The smaller exploratory probe reports are retained, with their inconclusive scope explicit.

The directional gate is ONE far-energy bound. It is not the full low-mode Schur sign, a mixed-term certificate, a uniform-window estimate, or RH.
'''
(B/'README_inverse_refinement.md').write_text(readme)
print('Research checkpoint and revision notes written.')
