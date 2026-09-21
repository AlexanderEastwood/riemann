Diagnostic (semantic lock); not a certificate.

**Bottom line.** The semilocal Weil form assembled by
`evidence/v124/g2_schur_cancellation/assembly_general.py` reproduces
Connes–Consani–Moscovici's §6 numbers (arXiv:2511.22755v1) at every printed
digit: at λ = 3, N = 120 all twenty Figure 1 differences |γ_k − z_k| (ratio
here/CCM between 0.97 and 1.01, CCM print two figures); at λ = √12, √13, √14,
N = 120 all 150 table entries (ratios within 0.5 % of 1, CCM print three
figures), including the headline 2.44 × 10⁻⁵⁵ (here 2.43629 × 10⁻⁵⁵) and
1.07 × 10⁻⁶⁰ (here 1.06515 × 10⁻⁶⁰).  Assembly at 1024 and 1536 bits with
eigensolves at 220 and 300 digits give identical values.  No normalization
discrepancy was found in anything §6 can see: the relative weights and signs
of the pole, prime and archimedean terms, the L = 2 log λ Fourier geometry,
the √2 zero-mode factor and the parity reduction are all pinned (a 1e-8
relative change in the prime weight moves the first difference from 1e-34 to
1e-7).  What §6 cannot see, and what therefore remains unlocked, is a common
scalar factor or identity shift of QW_λ: the zeros of ξ̂ are invariant under
τ → cτ + sI, and CCM print no eigenvalue with digits (Figure 4 gives
ln ε_λ by eye only; ours match it to the resolution of the plot).

Files: `results.md` (quotes, convention dictionary, tables, verdict),
`reproduce_ccm.py` (script; run from the repo root with `.venv/bin/python`),
`runs/*.json` (raw outputs of the eight runs).
