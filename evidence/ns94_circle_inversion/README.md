# NS94: tangent circles and zero counts

Classification: exact geometric identities and a polynomial countermodel
to a symmetry/count inference. No numerical zeta experiment or RH result.

The linked Zhao handout was read in full, with its relevant diagrams checked.
Its original bytes are not republished here; source URL/hash and precise scope
are in sources.json. The earlier local Maxima copy did not contain the PDF.
Exterior similarity is derived directly, not attributed to the handout.

See `argument.tex`, `checks.mac` (standalone ordinary Maxima, no Clifford
package), and `../../audits/tangent-circles-and-rh-2026-09-23-v1.html`.
Run the worksheet with `maxima --no-init --very-quiet --quit-on-error
--batch=evidence/ns94_circle_inversion/checks.mac`; all 23 exact checks pass.
The figure is an illustration of exact rational-coordinate control points,
not a computation of zeta zeros. The source plot can be regenerated with
make_figure.py; floating plot coordinates do not enter the proof.

The formal note separates inversions in each circle, both orders of a
successive pair, and inward/outward interpretations of the 0/1 variant.
The positive power-product statistic is only a location detector; its
vanishing at every height is an unproved RH-equivalent target. No general
geometric route is excluded. Review is by the author only.
