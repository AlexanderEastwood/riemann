# v1.57 — NS-58 translated-radical boundary test

Classification: exact identities and proved implications; the independent
arithmetic sign/rigidity input remains open.

The bounded attempt reached its explicit stop condition. The full exterior
pairing vanishes for all translated radicals exactly when the original
complete operator has the proposed nullvector. No new exclusion estimate
is obtained. Altered-weight controls have an explicit forcing profile,
necessarily nonzero for nonzero tests. Its compactness precludes a uniform
inverse bound on the entire fixed-window parity space, not on a particular
finite-dimensional kernel.

- [Integrated proof fragment](proof.tex)
- [Research report](boundary-pairing-2026-09-22-v1.html)
- [Local self-review](integration-review-2026-09-22-v1.html), not independent
- [Exact finite algebra](exact-checks.mac) and [saved replay](exact-checks-output.txt)
- [Validation](validation.json) and [complete build output](build-output.txt)

The fragment is included verbatim in the live manuscript. Inherited inputs
are its v1.35–v1.36 radical and totality lemmas, v1.18 complete realization,
v1.54 form core/nullvector setup, and v1.56 finite-change symbol result.
No novelty priority claim is made. No new numerical window, tail metric,
interval certificate, uniform floor, API, G2 or RH proof is supplied.

Replay from the repository root:

```sh
maxima --no-init --quit-on-error --very-quiet --batch=evidence/v157/exact-checks.mac
./manuscript/build.sh
python3 tools/verify_manifest.py v157
```

The Maxima checks verify finite algebra only. The complete-domain results
are the analytic arguments in proof.tex. This evidence is incremental.

Actual build: 294 pages, zero undefined/duplicate references, zero overfull
boxes and zero duplicate PDF destinations. The inherited RBC display anchor
was repaired without changing its formula or printed tag; see the local review.
