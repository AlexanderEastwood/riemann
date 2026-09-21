# Next steps — shared task board

One line per task. **Claim a task by writing your name in `owner` before you
start, in its own small commit**, so the other agent does not duplicate it.
Update `status` in the same commit as the work. Keep done items; record the
version that did them. Nothing here is a claim about G2 or RH.

Status vocabulary: `open` · `claimed` · `in-progress` · `done (vN.NN)` ·
`closed — no angle` · `blocked (reason)`.

| ID | task | owner | status | done when |
|---|---|---|---|---|
| NS-1 | Recover the two OPEN evidence groups: v1.28 λ=5 disproof (`g2_lambda5_transfer`, `g2_block_metric`); v1.31–v1.34 concentration/closures (`g2_weighted_concentration`, `g2_schatten_no_go`, `g2_nested_commutator`, `g2_primitive_transport`) → `evidence/v128/`, `evidence/v131..134/` + manifests | Codex (Astra) | claimed | `evidence/MISSING.md` has no OPEN rows; the six map nodes lose their EVIDENCE MISSING flag |
| NS-2 | Semantic lock: reproduce one CCM §6 numerical value (arXiv:2511.22755) from `assembly_general.py`; report value, precision, any normalization discrepancy (a discrepancy is the better outcome) | Codex (Astra) | claimed | value + precision + discrepancy statement under `lane/semantic-lock` |
| NS-3 | Manuscript positioning: cite Zhu (2608.24827) and Groskin (2607.02828); add the `a = log λ` translation table beside the λ=4 result; cite Zhu at `prop:v125-cutoff-cost` as the same doubly-exponential family; add the CCM `μ_λ` paragraph from `COMPARISON.md` | Codex (Astra) | claimed | v1.40 with those passages; no new results required |
| NS-4 | Meta-obstruction for arithmetic-blind estimates | Astra | done (v1.39) | Two scoped theorems (`thm:v139-probe-relaxation`, `thm:v139-protected-orbit`); blanket "all ten closures" claim refuted by explicit positive counterexample |
| NS-4b | Coverage table: which of the ten closures each v1.39 theorem covers, which it does not, and why; check the live concentration mechanism is outside both theorems' classes | Codex (Astra) | claimed | table in the manuscript or `evidence/v139/`; concentration route explicitly excluded |
| NS-5 | Certify simple-even ground of the **complete** `W_4` (CCM Thm 5.10 / CvS Thm 6.1 hypothesis) with the `prop:v117` machinery; numerically the gap is 8 orders (`evidence/diag_circle_split/`) | Astra | done (v1.40) | `prop:v140-ground4`, `cor:v140-real-zeros`: 1024/1280-bit complete shifted inertia; 0<mu0<2.454e-75, mu1>1e-73; complete ground transform has only real zeros |
| NS-6 | Krein–Langer / truncated-moment framing of the wall (in `COMPARISON.md` addendum) → integrate into the goals section | Claude (agent) | claimed | one paragraph in the manuscript, cited |
| NS-7 | Toeplitz-plus-Hankel asymptotics: does Basor–Ehrhardt / Szegő–Widom for `T(φ) ± H(φ)` sections reproduce the certified `lmin` decay rate (3.6e-38 → 6e-129, λ=3→8)? | Claude | closed — answered at diagnostic level | `evidence/diag_circle_split/results.md`: sign is arithmetic (phase on the resolution lattice); size is a fixed O(0.02–0.04) cancellation whose residual collapses at the Landau–Widom scale (Zhu's law gives the order, not the constant: within 1.3 orders at λ=3, ~1.9 orders above the certified μ0 at λ=4; λ=6,8 compressions unconverged); rigorous T±H asymptotics (Basor–Ehrhardt) left open |
| NS-8 | Nyman–Beurling–Báez-Duarte assessment + `d_N` table | Claude | closed — no angle | `evidence/diag_routes/nb/`; d_N certified to N=600; no finite equivalent; Burnol Thm 3.1 recorded as semantic lock |
| NS-9 | Li / Keiper assessment + `λ_n` table + support analysis | Claude | closed — no angle | `evidence/diag_routes/li/`; Li class ∩ PW_a = {0}; corollary W_4≥0 ⇒ λ_n^{[log 16]} ≥ 0 |
| NS-10 | de Bruijn–Newman assessment + one Polymath15 reproduction | Claude | closed — no angle | `evidence/diag_routes/dbn/`: no bridge in either direction; barrier verification reproduced from scratch; arXiv id is 1904.12438 |
| NS-11 | de Branges / Hermite–Biehler route | Claude | closed — no angle | dictionary recorded in `COMPARISON.md`; no positivity mechanism (Suzuki 2606.09096, Conrey–Li) |
| NS-12 | Function-field / Hodge / F_1 route | Claude | closed — no angle | nothing finite transfers; the operator side gave NS-5 |
| NS-14 | CCM step (b) at finite λ: compute the real zeros of `ξ̂_3` and `ξ̂_4` from the certified ground vectors (NS-5 makes them provably real) and compare with γ_1, γ_2, … = 14.13, 21.02, 25.01, …; also the zero spacing vs λ | Claude | closed — answered | `evidence/diag_ns14_zeros/`: the real zeros of ξ̂_λ are the sinc lattice 2πk/L (exact: ξ̂ = sin(zL/2)·R(z), ground mass at n ≤ 2); no tracking of zeta zeros at λ=3,4; n90 = 2,2,3,3 at λ=3,4,6,8 — step (b) has not begun |
| NS-13 | Standing rule: do **not** compute λ = 10, 12 windows or floors past λ=8 | — | rule | `prop:v121-cofinal-rh`, `prop:v138-shifted-floor` |
| NS-15 | Review current evidence, dependencies and active work; recommend the next NS to tackle | Codex | done (v1.40 review; no new result) | Recommend NS-2 next: reproduce CCM section 6 at lambda=sqrt(12), N=120, with the exact normalization dictionary, two-precision replay and a discrepancy statement. NS-14 is already in progress; NS-4b's table and concentration exclusion already exist in v139/adversarial_review.md sections 6–7. Follow with NS-3/6, correcting the stale comparison; retain NS-1 as blocked. The next analytic target remains a uniform finite signed-concentration floor in both parities, with all couplings controlled. |

## Lanes

```
lane/concentration     the live mechanism (prop:v131-concentration)
lane/bounded-floor     v1.36 reduction; floors certified through λ=8
lane/semantic-lock     NS-2
lane/circle-toeplitz   NS-7  (Claude)
lane/odd-sector        odd-parity obligations
lane/window-scaling    window behaviour; closed to new windows by NS-13
```

Add a row before starting anything not listed. Remove nothing.
