# NS100 independent route reassessment

Independent assessment requested by Alex; bounded algebra and one complete
interval sign check. No RH proof, cofinal bound, new manuscript version or
worldwide novelty claim.

- `argument.tex`: complete theta-slice calculation, all series and physical tails,
  domination for continuity, and the exact geometric control.
- `proposals.json`: ranked research screens, actual first results, stop conditions.
- `sources.json`: primary-source novelty screen and exact claim scope.
- `turn-review.json`: reviewed repository conclusions and limitations.
- `certify_slice.py`: one fixed theta-transform value; python-flint 0.9.0.
- `slice-256bits.json`, `slice-384bits.json`, `slice-cutoff-384bits.json`: replay.
- `checks.mac`, `checks-output.txt`: nine exact algebra checks.
- `diagnostics.txt`: touched Python type diagnostics.
- `source-bindings.json`: reviewed scientific-source hashes.
- `self-review.json`: scope and proof checks.

Run from the repository root:

```
.venv/bin/python evidence/ns100_reassessment/certify_slice.py --bits 256 --output /tmp/ns100-256.json
.venv/bin/python evidence/ns100_reassessment/certify_slice.py --bits 384 --output /tmp/ns100-384.json
.venv/bin/python evidence/ns100_reassessment/certify_slice.py --bits 384 --terms 8 --cutoff 4 --output /tmp/ns100-cutoff.json
maxima --very-quiet -b evidence/ns100_reassessment/checks.mac
pyright evidence/ns100_reassessment/certify_slice.py
```

The per-slice positivity shortcut fails for the actual theta kernel.
The complete weighted integral has not been assigned a sign. The two are
not interchangeable. Positive-definite associated-kernel criteria are
classical; see Csordas (2014), Theorem 4.6 and Open Problem 4.7.
