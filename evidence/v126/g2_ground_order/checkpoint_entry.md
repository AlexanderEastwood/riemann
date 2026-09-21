## Current research checkpoint: September 21, 2026 — v1.17 complete ground ordering at one window

**Closed an additional fixed-window obligation:** the complete canonical Weil operator at lambda=3 has a simple even ground state, with `0<mu0<3.644e-38`, every other even eigenvalue greater than `1e-34`, and every odd eigenvalue greater than `1e-36`. Consequently the full next eigenvalue is greater than `1e-36`. The exact normalized P64 p3 has ordinary ground-angle sine less than `0.01931`. **No growing-window G2 gap was closed; RH remains open.**

### Starting point and selected obligation

Fresh reads of the saved v1.16 complete manuscript, persistent log and evidence bundle confirmed the prior checkpoint. v1.16 already proved complete fixed-window positivity, including all omitted modes. The selected next obligation was its recorded shifted-operator test: establish parity, simplicity and separation of the actual lowest state, then connect the exact projected source by a quantitative ordinary overlap bound. We retained the first-slot-linear convention, physical basis, literal Fourier cut, separate logarithmic diagonal and all parity factors. The corrected sampler and its graph defect were not altered.

### Exact shifted identity and certified inertia

For each exact threshold a, the implementation shifts every actual diagonal `d_n` and every tail inverse weight `g_n` by a. It uses the unchanged frozen exact dyadic witness Z from v1.16. With `G=(I_head,-Z)^T`, the identities are

`K_Z(a)=K_Z(0)-a(I+Z*Z)`, `R(a)=R(0)+aZ`.

Every finite residual row through J=4096 is recomputed, including the middle rows affected by the shift. Remote rows have no diagonal entry, so their moment Gram majorant is unchanged; its inverse weight is still shifted. The full bound is

`S_a >= L_a = K_Z(a)-sum R_n(a)*R_n(a)/(g_n-a)-U_remote/(g_(J+1)-a)`.

All inverse weights are positive. Interval LDL continues through negative pivots and requires every pivot to exclude zero. The exact successful tests are:

| Sector | Threshold | N / M / J / moment order | Pivot signs | Precision replays |
|---|---:|---|---|---|
| Even | 1e-34 | 256 / 512 / 4096 / 80 | 1 negative, 256 positive | 768 and 896 bits |
| Odd | 1e-36 | 512 / 1024 / 4096 / 100 | all 512 positive | 768 and 896 bits |

The one negative even pivot is at zero-based index 24. Its size, and every other pivot size, is NOT an eigenvalue estimate. Witness hashes are unchanged from v1.16: even `993c5b325c1cc7dce64c1dbdab9384dd54dea6a480cce8739cf623e9e8bce43c`; odd `4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea` (SHA256 of uncompressed exact witness JSON). Each 896-bit replay reuses precisely the same witness as its 768-bit run.

### Matching trial direction and actual spectral conclusion

The signed inertia is for a LOWER Schur form. Its negative pivot alone supplies no negative direction of the exact shifted operator. The required matching direction comes from the existing exact rational, finitely supported even candidate u at N=64. Its full-form Rayleigh quotient is exactly its finite-compression quotient, alpha=5.312381700586359...e-38.

A separately verified finite correction uses `z=(C-alpha I)^(-1)r`, with z orthogonal to u, and `v=(u-z)/sqrt(1+||z||^2)`. Direct expansion proves the exact identity

`beta=QW3(v,v)=alpha-<z,r>/(1+||z||^2)`.

The prior finite inverse certificate and a new direct 768-bit enclosure both imply beta<3.644e-38 (new enclosure 3.643399656992330629578...e-38). Thus the complete even shifted operator has at least one negative direction. Its lower Schur form has positive second eigenvalue, so min--max allows at most one nonpositive even level. Square completion on the established form domain transfers negative index, and kernels correspond. Hence exactly one even eigenvalue lies below 1e-34, and none equals that threshold. The odd certificate puts all odd levels strictly above 1e-36. Compact resolvent, the old full positivity certificate, and beta<1e-36 identify the global ground as simple and even.

The proof does not confuse a finite-compression gap with a complete-operator gap. The author-hosted source consulted for min--max and its form-domain version was G. Teschl, Mathematical Methods in Quantum Mechanics (2009), Section 4.3, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf. The square-completion and index argument is written explicitly in the manuscript.

### Exact projected-source overlap

All non-ground even spectrum lies above 1e-34. Positivity and the corrected trial energy imply `sin angle(v,xi0)<sqrt(3.644e-38/1e-34)`. The finite correction contributes less than .000216 in rank-one projector norm. Their sum is below .019305264 and hence .01931.

The exact source certificate gives `||P64 p3-c||<2.60e-36`; direct rational normalization gives `||c||>0.65172555`. Elementary ball geometry bounds the normalized-vector distance by less than 4e-36. This fits inside the displayed angular margin and transfers the claim to the exact normalized projected source. It does not transfer a tiny energy by an ordinary perturbation bound, nor does it identify the unprojected source with the ground. The earlier certified 137.4%–137.5% relative endpoint error at N64 is unchanged.

### Failed or insufficient attempts, retained as failures

1. The odd lower Schur matrix at the stronger shift 1e-34 had one negative pivot (index 85). This failed to certify the desired odd lower threshold. It does NOT prove that an actual odd level lies below 1e-34. The weaker sufficient threshold 1e-36 passed and suffices to order the ground.
2. The exact candidate's complete centered residual was enclosed between 3.3368484596e-19 and 3.8871364266e-19, including all rows through 4096 and a remote moment bound. Dividing this by the available tiny separation gives an ineffective ordinary residual/gap estimate, of order 1e15 even with the larger even threshold. The successful overlap argument instead uses independently proved positivity and the trial energy.
3. Neither the ordinary angle nor simple ground ordering controls the physical endpoint trace. No endpoint claim, uniform spectral theorem, or RH implication was inferred from the fixed-window computation.

### Adversarial review and evidence integrity

Two internal agents independently checked the trial normalization, signed-inertia direction, zero-threshold exclusion, parity ordering, form-domain square completion and overlap geometry. The same exact witnesses passed higher-precision replays. This is a computer-assisted proof with analytic infinite-tail bounds and outward intervals, not proof-assistant verification or external peer review.

An integrity check found the prior saved v1.16 ZIP truncated (33,355,678 bytes, missing its central directory). The manuscript, PDF, log and individual evidence files were intact. All 37 v1.16 reproducibility files were checked against their previously recorded SHA256 values, with no mismatches; both dyadic witnesses decompressed correctly. The cumulative archive was rebuilt from the valid v1.15 bundle plus those checked files and the v1.16 root documents. The recovered v1.16 archive is 42,113,921 bytes with 118 intact members. The present v1.17 archive is built from that recovered base using a temporary file, flush/fsync and atomic rename, followed by an independent ZIP CRC check. No mathematical evidence was reconstructed from unverified numerical output.

### Manuscript integration and next concrete step

The complete manuscript is v1.17. The abstract, status, Section 20 proof, Section 32 goals, reproduction appendix and bibliography are updated; all 72 historical claim dispositions and prior labels are retained. Failed sufficient tests stay in this log rather than appearing as negative Weil-form results.

The next substantive target is a larger physical window: generalize the coefficient assembly and weighted prime-tail constants, build a complete low-mode block certificate, and measure how the signed inverse correction and remote moments scale. The eventual obligation is an independently justified error bound along an unbounded window sequence, not a list of successful fixed examples. Endpoint stability for actual ground vectors, uniform source-block control, the sampler graph defect and full-strip transfer remain separate. G2 and RH remain open; no publication or outside contact occurred.
