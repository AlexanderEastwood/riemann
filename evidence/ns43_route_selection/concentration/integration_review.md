# v1.52 integration — bounded independent mathematical review

Scope: `evidence/v152/route_selection.tex` and `research-map.json`, with
text comparisons against the owned concentration proof and reviewed final
CCM v2. This is not a new replay of NS-45, a review of package manifests,
or an assertion that the integrated manuscript has built.

## Ranked findings

- **MAJOR: none within this bounded scope.** The intended concentration
  result applies to the actual symbol, the CCM v2 hypotheses survive
  integration, and the new closures remain scoped to specified methods
  or abstract inferences rather than their open arithmetic parent routes.
- **MINOR M1, resolved: explicit form-domain hypothesis for the generalized
  adaptive proposition.** The proof makes its lower spectral edge finite
  by testing a nonzero vector in `S_a ∩ D(q_a)`. Continuity, evenness,
  a lower bound and growth to infinity alone would not guarantee that
  such a compactly supported form-domain vector exists for an arbitrary
  much faster growing multiplier. The actual Weil symbol has logarithmic
  growth, so the intended assertion is valid. Resolved in the new owned
  `concentration_operator_collapse-v2.tex`: it explicitly assumes a
  nonzero form-domain vector and explains the actual-symbol justification.
  Root inserted this version into the composite; my exact text check
  confirms that the entire final v2 body is present unchanged.
- **MINOR M2, resolved: reversed map wording about transform masking.** The original
  `bumpstrength.note` ended “For arbitrary probes only common-transform-zero
  masking is excluded.” The proposition instead forces a possible off-line
  zero to be a common transform zero; it does not exclude that masking.
  The final note now says boundedness permits off-line zeros only at
  common transform zeros and does not exclude that masking. I checked
  the corrected JSON directly.

No outstanding MAJOR, MINOR, or actionable NOTE remains within this scope.

## Concentration proof and actual hypotheses

The initially integrated concentration proof matched the original body
exactly; the only additional lines after it were the following CCM source
comments. The v2 addition just described is necessary only to make the
generalized statement's already used hypothesis explicit.

For the actual fixed-window symbol, the prime sum is finite, the continuum
correction decays at infinity, and the digamma real part grows
logarithmically. Thus the symbol is continuous, even, bounded below and
tends to positive infinity, while growing only logarithmically. Compact
smooth physical tests have finite form energy. In the even sector two
independent smooth even tests leave a nonzero kernel of the single source
functional; nonzero smooth odd tests require no source constraint.

The lower-edge convergence proof does not make the invalid inference
from strong-resolvent convergence to convergence of lower edges. It first
obtains a uniform Fourier-tail bound on near-minimizing unit vectors from
the coercive capped symbols. Fixed physical support makes restriction to
a bounded frequency interval a compact integral map. These two facts
give a strongly convergent unit subsequence in the same closed parity
and source space. Bounded-form convergence at each fixed minorant and
monotone convergence then prove the lower-edge limit. No compactness
constant uniform in the window is claimed or needed: complexity is
selected separately at each window and has no effective bound.

Consequently the unrestricted hierarchy remains an exact existence
reformulation, not a new cofinal arithmetic estimate. The scalar-set
counterexample remains explicitly finite and nonarithmetic. QG plus its
separate admissible packet still obstructs only bounded level count.

## CCM integration comparison

I compared the entire integrated CCM body to
`ccm/selection_note-v2.tex`. Apart from removal of the user-facing node
recommendations and extra whitespace, the only differences were the
intended substitutions of literal printed label strings by `ref` or
`eqref`. The explicit fixed cutoff, complete-domain mixed terms, S4
elementary floor, full both-parity reset in S5, and final definition of
the full ground as the minimum over parities are preserved. The abstract
model's missing arithmetic support consistency and lack of strict
positivity on the whole growing interval remain stated.

## Map scope

The map was parsed and checked directly:

- `circle` is `open`, with exactly “measurement lane; closure claims
  withdrawn after NS-31; geometry and exact identities retained”.
- The unique `live` node is `stepb`.
- `concentration`, `capacityweight`, and `relativeselection` retain their
  blocked/open-input status. No successful cofinal estimate is asserted.
- `adaptiveidentity` is a proved equivalence, not a proved floor.
- `scalarsetshortcut` is closed only as a general scalar-completeness
  inference; `absoluteselection` only as an inference from its listed
  nonarithmetic abstract premises; `coarseprofile` only under the stated
  scale and full-form liminf hypotheses.
- The `w5` and `blockmetric` titles name their particular comparisons,
  and their notes distinguish fresh witnesses from missing original
  evidence and comparison failure from the sign of the complete form.
  NS-44 has its separate replay review; NS-45's gates were not rerun in
  this bounded integration pass.
- `capacitychannels` keeps the specified weight, unchanged signed terms,
  and sub-endpoint restrictions. Its open parent is retained. The new
  `bumpstrength` node records a conditional obstruction, not a proved
  discrepancy bound; M2 corrects the final qualification in its note.

No other unjustified new closure was found in the reviewed map changes.

## Final pinned sources and integration

| Item | SHA256 |
|---|---|
| Final owned concentration v2 | `6320c6f77d81f98a3496bb6043af71f036c1e49be728a519ed91cfce1955031a` |
| Reviewed CCM v2 | `3c4135cdea011f07184a68afd54c45e389cb53f982ebb11cd33b0de08ebd9286` |
| Final reviewed composite | `d1673ceed4912cad67cb6c7fe79ca15c3ea0d24dc0aec7d27c2458e611cc39d5` |
| Final reviewed map | `cab2794142fcff0aa7828bd77822772b374d81e51146e3078ea2b22183ab7f4a` |

The final concentration v2 body is an exact substring of the composite.
The integrated CCM body is exactly the reviewed v2 after the permitted
label-to-reference substitutions, omission of node recommendations and
whitespace normalization. Circle and sole-live-node checks passed again
on the final map. Root retains responsibility for generated diagrams,
manifest generation and the actual manuscript build; this review makes
no claim about a build still running at handoff.
