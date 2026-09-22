ANALYTIC WORKING NOTE: exact identities, proved conditional implications, and explicitly named open inputs; no numerical certificate.

NS-43 bounded CCM selection subtask. The styled report is [ccm-selection-2026-09-22-v2.html](ccm-selection-2026-09-22-v2.html). [selection_note-v2.tex](selection_note-v2.tex) contains the full elementary proofs. The coordinator owns integration, naming, and final node decisions. Preserve CCM step (b) as the sole gold/live map node under the user's explicit instruction; its mathematical target remains open. Proposed closed statuses apply only to new scoped child inferences, not to step (b).

Preliminary conclusion: the available absolute residual, a simple real-zero fixed-window ground, vanishing ground energy, and ordinary strong-resolvent collapse do not by themselves select the Gaussian radical. The countermodel meets those abstract premises exactly, including compact-resolvent operators on increasing intervals and uniform ground tightness; it explicitly does not impose arithmetic support consistency, the Weil/CvS distribution identity, or positivity improving semigroups. It is not an arithmetic disproof.

Recommended concrete input: an independent COMPLETE second-eigenvalue separator beta_a > alpha_a for the explicit normalized cutoff Gaussian radical p_a, at a scale satisfying C_R(a) ||(A_a-alpha_a)p_a||/(beta_a-alpha_a) -> 0 for every fixed R>0. Here C_R(a)=sqrt((exp(2Ra)-1)/(2pi R)) is the ordinary Fourier evaluator envelope. This yields ordinary and locally uniform entire selection with a specified phase and normalization. An even-sector separator must be paired with odd ordering when the real-zero theorem needs a global ground. Alternatives are a Rayleigh-excess/gap estimate plus weighted tightness, or a complete evaluator-dual estimate on the actual spectral complement.

Existing source trace (all references are the live manuscript at this task's base):

- lem:v115-source-mass, prop:v115-absolute-residual: repaired-source ordinary limit and complete residual, not ground selection.
- G2.1 and G2.3: monotone ground energy and the weaker residual/ground-overlap test; bounded or vanishing complete ground energies are already RH-strength targets in this arithmetic setting.
- cor:v140-real-zeros: complete simple global ground at lambda=4; not a cofinal theorem.
- prop:v143-resolution and prop:v143-fixed-window-meaning: one fixed-window evaluator budget and its scoped limitations; not a general impossibility result.
- prop:v135-growing-radical: complete growing near-radical block, including an even reflected block; prevents a uniform or polynomial source-complement separator.
- lem:v136-total-radicals, prop:v136-resolvent-collapse: dense fixed translated radicals and ordinary zero-resolvent limit; no unique direction.
- prop:v136-bounded-floor: complete cofinal lower floor is already the target, not a new independent selection estimate.
- lem:v150-weight and eq:v150-mellin: positive Gaussian arithmetic weight and exact transform proportionality to Xi.

No new windows, zero numerics, tail metric, manuscript edits, map edits, board edits, commits, or pushes were made by this subtask. The task was claimed by the coordinator before delegation.

Stable proposed labels: prop:ns43-ccm-rayleigh-selection; prop:ns43-ccm-residual-selection; prop:ns43-ccm-evaluator-selection; prop:ns43-ccm-source-separation; prop:ns43-ccm-nonselection; prop:ns43-ccm-coarse-profile.

The cutoff is pinned to v1.35's fixed boundary profile, with derivatives bounded uniformly in a. The normalized cutoff is the central growing-block column, so eq:v135-block-residual gives ||A_a p_a|| <= epsilon_a and |alpha_a| <= epsilon_a directly. Arbitrary smooth cutoff families are not asserted to have this residual rate.

A separately assigned bounded NS-45 review is recorded in [ns45_review.md](ns45_review.md), with the redirected frozen-verifier transcript. It found no MAJOR/MINOR, reproduced the existing certificate byte-for-byte, and changed no author files. This ancillary review does not change the analytic classification or claims of the CCM selection note.

Version 2 is the integration candidate. It explicitly resets S5 to the full both-parity Weil form on zero-extended L²(R), defines the final full ground as min(even,odd), and records q[f] >= (alpha-||r||)||f||² from the complete cross term. The relative rate is needed for profile selection, not this S4 floor consequence. The original selection_note.tex and HTML v1 remain unchanged so previously delivered links retain their original content.
