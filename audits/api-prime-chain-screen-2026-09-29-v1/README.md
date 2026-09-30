# API prime-chain admission audit

[Readable report](../api-prime-chain-screen-2026-09-29-v1.html).

The proposed first-zero exclusion using only the positive prime-chain
operator bounds is stopped by the existing NS57 control. Changing only
`w_2` by `-log(2)/100` preserves the original chain bounds for every prime,
yet NS57 supplies a complete nonnegative first-zero window with a nonzero
nullvector. The report gives a two-case all-frequency bound, not an
extrapolation from samples. NS57's inherited analytic dependencies are
explicit; no first-zero location or new Weil certificate is computed.

**Wall check: Known wall** for this bounds-only inference; **Same open gap**
for original KERNEL-API and arguments retaining the exact Euler recurrence
or arithmetic radical identity. No new research row, node, thaw or version.

## Replay

From a Git checkout retaining base commit
`9db64fdfdc1237005c071f777088291df254ac72`, use Python with
`mpmath==1.3.0` and Maxima:

```sh
.venv/bin/python audits/api-prime-chain-screen-2026-09-29-v1/screen.py --dps 50 --output /tmp/api-chain-50.json
.venv/bin/python audits/api-prime-chain-screen-2026-09-29-v1/screen.py --dps 80 --output /tmp/api-chain-80.json
maxima --very-quiet -b audits/api-prime-chain-screen-2026-09-29-v1/check_identities.mac
pyright --project audits/api-prime-chain-screen-2026-09-29-v1/pyrightconfig.json
```

Choose fresh output paths; the script refuses to overwrite files. The
Davenport–Heilbronn interface is pinned by commit and source hash; its
not-applicable result is a hypothesis mismatch, not a passed control.
The matched NS57 control preserves the literal prime/gamma/pole family
needed by the bounds-only inference, but not the exact Euler recurrence.
