# NS-43 concentration subtask — internal coordination note

Analytic work only. No numerical experiment, certificate, G2, or RH claim.

## Findings

1. **Proved equivalence, actual physical setup:** arbitrary finite dyadic
   superlevel minorants have source-compressed ordinary lower edges increasing
   to the complete form's lower edge at each fixed window. Along a prescribed
   cofinal family, existence of arbitrary finite adaptive comparisons with a
   uniform floor is equivalent, up to any fixed additive epsilon, to the
   unknown uniform complement floor itself. The proof uses fixed-window
   physical support and the coercive frequency symbol; it does not infer
   convergence of lower edges from strong resolvent convergence alone.

2. **Proved scoped obstruction, nonarithmetic model:** exact scalar upper and
   lower concentration bounds for every set need not determine the signed
   lower edge. A three-outcome commuting model has the best scalar lower bound
   `-t/5` but actual signed lower edge `+t/10`. A second model with identical
   scalar data has actual edge `-t/5`. Both can carry the same exact rank-one
   source. This closes a general claim that optimizing all sets plus their
   separate scalar concentrations is complete. It does not close the physical
   arithmetic concentration route.

3. **Existing proved implication under open inputs:** QG plus a separate
   source-admissible bounded-energy all-Borel packet forces the negative level
   count to diverge for bounded loss. It does not obstruct arbitrary growing
   level count. NS-40's separated-band criterion concerns only the growth
   clause; it supplies neither the packet nor a signed lower bound.

## Recommended priority

Do not rank routes by an unsupported numerical probability of proving RH.
For useful progress toward the stated target, pursue a concrete joint signed
operator estimate only if it has an explicit arithmetic input that can be
proved independently. Merely optimizing an unrestricted hierarchy is the
same open problem. CAE has the same issue, by v1.51. QG and further bounded-K
diagnostics rank below such a signed estimate for positivity progress: they
test the complexity of a possible proof, not its sign.

CCM has a distinct convergence/transfer input and should be assessed by the
separate CCM agent. Nothing proved here makes concentration more likely than
CCM. Retain concentration as open with a named joint signed estimate missing;
close only the exact-reformulation shortcut and the general scalar-completeness
claim, if they are represented as separate proposals. Do not close a merely
blocked arithmetic route.

## Scope and reproducibility

`concentration_operator_collapse-v2.tex` is the final proof version. It adds
the explicit nonzero form-domain hypothesis used to make the lower edge
finite, and explains why the actual logarithmic-growth symbol and one
source constraint satisfy it. The original
`concentration_operator_collapse.tex` is preserved.
All arguments are elementary consequences of the repository's complete symbol
and source conventions; no external theorem or new literature assertion is
used. The finite countermodel is exact rational arithmetic, not a simulation.
No manuscript, map, board, or prior evidence file was edited by this subtask.
The parent owns integration and the actual manuscript build.
