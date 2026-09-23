# NS97: overlap audit and continuation correction

**Audit and elementary homogeneity check; no new arithmetic lower bound,
no new research-map node and no manuscript version.**

The user's question was whether the latest result was an existing wall.
The answer has two parts: the signed-arithmetic bottleneck was already
open; the exact LCM coefficient class in NS96 was a different scoped test,
not a new fundamental obstacle and not progress on that bottleneck.

`findings.json` compares the literal NS96 claims against NS62/64, NS74,
NS78 and NS95, and separates their scope from the unchanged PR42 target.
NS74 already displays the same Mellin separator and floor function used
by NS96 for a different coefficient class. `normalization-note.tex` checks
the suggested trace-budget continuation:
trace normalization alone leaves all correction rays available if the
step scale is free. A budget on the actual total update is a different
hypothesis and is not excluded by that scaling observation.

Replay the supplemental algebra with:

```sh
maxima --very-quiet -b evidence/ns97_novelty_audit/checks.mac
```

Nine exact checks with Maxima 5.50.0; no interval computation or physical
cutoff is needed for this homogeneity identity. Author audit only.
The original NS96 artifacts are unchanged, including their scope limits.
`turn-review.json` records the 104-conclusion review at main 6c50142.
The versioned HTML report is in `audits/novelty-audit-2026-09-23-v1.html`.

The next accepted proof target is the existing actual-residual joint
lower estimate. A new attempt must name the specific arithmetic term it
will estimate beyond prior results; another normalization, sign-cone
relabeling or finite efficiency calculation does not meet that threshold.
No new successful estimate is supplied in this audit. RH/G2 and both
historical-original evidence groups remain open.
