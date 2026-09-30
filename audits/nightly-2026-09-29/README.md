# September 29 publication record

This index is internal repository documentation. The three readable research
reports are versioned HTML files, preserved with their original evidence:

- [Cancellation-theorem transfer](../mobius-cancellation-transfer-2026-09-29-v1.html)
- [Prime-scaling admission](../prime-scaling-admission-2026-09-29-v1.html)
- [Jacobi-product admission](../jacobi-product-admission-2026-09-29-v1.html)

These are audits and diagnostics, not new cofinal estimates or interval
certificates. They add no theorem node or manuscript version. NS92–98 and
NS100–101 retain their scoped open inputs; neither whole family is closed.

## Preserve the historical record

The original files are copied byte-for-byte, including the unsuccessful
first Maxima harness output in the prime-scaling audit. Later successful
output is explicitly identified in its validation record. Fields saying
"local only", "no push", or "not published" describe the original test
turns, before Alex authorized publication on September 29. They do not
describe this publication. Historical paths are provenance, not portable
execution instructions. No secret material is needed for replay.

`publication-validation.json` records this integration's replay, checks and
file hashes. Original author checks are not independent mathematical review.
The reports' HTML was parsed but browser rendering was not verified.

## Portable diagnostic replay

Use a Git clone retaining reviewed commit
`f32cadfb7be523a8920b19be57d40d652e39a2ef`, Python and `mpmath==1.3.0`.
From the repository root, with that dependency installed in `.venv`:

```sh
.venv/bin/python audits/nightly-2026-09-29/replay.py prime-scaling --dps 50 --output /tmp/prime-50.json
.venv/bin/python audits/nightly-2026-09-29/replay.py prime-scaling --dps 80 --output /tmp/prime-80.json
.venv/bin/python audits/nightly-2026-09-29/replay.py jacobi-product --dps 50 --output /tmp/jacobi-50.json
.venv/bin/python audits/nightly-2026-09-29/replay.py jacobi-product --dps 80 --output /tmp/jacobi-80.json
maxima --very-quiet -b audits/prime-scaling-admission-2026-09-29-v1/check_identities.mac
maxima --very-quiet -b audits/jacobi-product-admission-2026-09-29-v1/check_identities.mac
```

Choose fresh output paths: replay refuses to overwrite existing evidence.
The wrapper changes only each original script's Git-source location; its
pinned source commit, calculations and output fields are unchanged. The
cancellation audit is a theorem-applicability assessment, not a numerical
experiment; its precise primary-source references and missing hypotheses
are in the original JSON record.

## Standing publication authorization

Alex's September 29 instruction was: "Deploy findings after every test.
Allowed. Deploy tonight's findings and then decide on the next route."
AGENTS.md now records that authorization. Completed failures are published
with their limits, and the research proposal gate remains in force.

No new research route is admitted by this publication. The next-route
assessment follows publication and must state its own wall check.
