# NS-44 independent bounded review — working record

Scope: the new dyadic witnesses and strict interval replay in
`evidence/ns44_metric_replay/`. This review does not recover the absent v1.27
originals, review another tail metric, or test another window.

## Verdict

No MAJOR or MINOR mathematical finding in the inspected certificate.
Both frozen witnesses have strictly positive complete Weil numerator and
strictly negative `q - 10^-8 D` at both 320 and 448 bits. Thus they refute
only the stipulated complete-tail lower comparison, in both parities.
They are not negative Weil directions.

One replay-hardening NOTE was sent to the author and resolved: the final
verifier validates the top-level lambda, tail start, shift, and exact
parity-key set before verification. The frozen witness already had the
correct values. I repeated the entire 320/448-bit replay after this edit;
all output fields again matched the regenerated certificate exactly.
There is no outstanding MAJOR, MINOR, or actionable NOTE in this scope.

## Exact witness and object identity

- Each coefficient is a JSON integer divided by `2^60`. The binary64
  eigensolve selects a proposal only. Verification reconstructs its exact
  dyadic values in Arb and never normalizes it again using floating point.
  The ordinary norms are close to, but not asserted equal to, one; all ratio
  and strict-sign conclusions are homogeneous.
- The recorded indices are exactly 17 through 128, so the witness lies in
  the stipulated literal `Q16` tail. A coefficient that happens to vanish
  does not change that assertion.
- The fourth output of `assembly.sequences` is `a_n = -A_n`, the complete
  archimedean diagonal in `eq:v114-arch-diagonal` and
  `eq:v115-arch-exact`. It is the diagonal used in the denominator.
  The arithmetic/pole diagonal `d_n` is used only in the Weil numerator.
  The code has not substituted `d_n`, a logarithmic approximation, or a
  different frequency-symbol component for this metric.
- The normalized parity vectors have signed Fourier coordinates
  `x_n/sqrt(2)` and `+x_n/sqrt(2)` for even parity, and opposite signs for
  odd parity. Their ordinary norm is `sum x_n^2`, and their metric norm is
  `sum a_n x_n^2`. The omitted common factor of `i` for a real sine basis
  does not change its Hermitian quadratic form.
- The positive-index compressed matrix is therefore
  `d_n + b_n/n` on the even diagonal and `d_n - b_n/n` on the odd diagonal;
  off-diagonal entries are `(b_n-b_m)/(n-m) +/- (b_n+b_m)/(n+m)`.
  Both `block` and the independent signed-index expansion implement these
  conventions, including `b_-n = -b_n`.

## Coefficients and analytic remainders

The fresh sequence call redirects the builder to a newly created empty
temporary directory, once per precision. Thus the certificate does not
load earlier rounded sequence files. The returned Arb objects are retained
before that temporary directory is removed.

The digamma/trigamma expressions match `eq:v115-arch-exact`; complex
conjugation in the code leaves their real parts unchanged. Its sine
coefficient uses the negative imaginary part at `1/4 - i t/2`, giving the
positive full-line sine series. The finite exponential correction then
restricts that integral to the correct Fourier period.

For `c_k = 2k + 1/2`, `e_k = 5^(-4k-1)`, the two elementary estimates

```
|t/(c_k^2+t^2)| <= 1/(2c_k),
|(c_k^2-t^2)/(c_k^2+t^2)^2| <= 1/c_k^2
```

bound the discarded series from `K=96` onward by

```
e_K / (2 c_K (1-5^-4)),
2 e_K / (L c_K^2 (1-5^-4)),
```

respectively, exactly the `es` and `ed` radii added by the builder.
They are outward balls, not midpoint corrections. The remaining pole
rational functions and all prime-power contributions are evaluated in Arb.
The strict prime cutoff is below 25. The full-length translation at 25 is
zero for these supported physical modes, consistently with the stipulated
strict-cutoff convention.

## Independent replay and alternate quadratic assembly

I imported the verifier, redirected only its `OUT` to a fresh temporary
directory containing a byte copy of the pinned witness, and ran `verify()`.
Every certificate field matched the original output in that replay.
Root's evidence files were not overwritten.

I also computed the signed quadratic by an independently written full
double sum, calling neither `block()` nor `signed_pairing()`:

```
q = 2^(-2p-1) sum_(n,m=17..128) z_n z_m
      sum_(s,t in {-1,+1}) e_s e_t W_(sn,tm),
```

where `p=60`, `e_s=1` in the even case and `e_s=s` in the odd case,
`W_(sn,tm)=d_n` when the two signed indices are equal, and otherwise
`(s b_n-t b_m)/(sn-tm)`. The metric was independently summed as
`2^(-2p) sum a_n z_n^2`. This alternate sum still shares the audited
analytic coefficient routine; it is an independent parity/index assembly,
not a second derivation of the analytic kernel.

At 448 bits it gave overlapping enclosures for:

| Parity | q | D | q/D |
|---|---:|---:|---:|
| even | 1.55884794745770125919e-17 | 2.42677982768940290249 | 6.42352441565298054355e-18 |
| odd | 2.73181237557136479370e-17 | 2.45491673166065540615 | 1.11279227533041427672e-17 |

Both strict shifted signs were verified again. I also checked that the
320- and 448-bit ratio balls overlap. The table is a shortened display of
the interval results, not a replacement for the archived ball strings.

## Complete-support interpretation

A finite supported coefficient vector has exactly zero coefficients in
every other mode. Its complete form value is therefore exactly the finite
quadratic using complete entries. No outside-vector cross term or remote
tail bound is needed for this falsification. The complete operator may
send the vector outside its support, but those output components do not
contribute to its quadratic form. The two positive numerators explicitly
exclude interpreting these witnesses as negative directions for the
complete Weil form. An even-source constraint is not part of the universal
literal-tail comparison being refuted.

No claim about complete lambda=5 positivity, another metric, the unarchived
v1.28 block witnesses, a cofinal floor, G2, or RH follows from this replay.

## Final pinned review state

The final verifier's metadata/parity checks are present. I validated every
source hash embedded in the certificate and repeated the complete verifier
with output redirected to a fresh temporary directory. No root evidence
file was overwritten.

The final hardening also refuses Python `-O` in both `main()` and imported
`verify()`, so optimization cannot silently disable the assertion gates.
I inspected both guards, tested the optimized CLI refusal, and repeated the
normal full 320/448-bit replay after this edit; it again matched every
certificate field exactly. My first wrapper test used the wrong expected
error-message words and failed after the valid refusal; a corrected check
matched the actual explicit error message. This was a review-wrapper issue,
not a certificate or verifier failure.

| File | Reviewed SHA256 |
|---|---|
| `evidence/ns44_metric_replay/replay.py` | `8d49106455b72127d8ff8c617cc12f4f0419580896e49e2b3117115892a89fa2` |
| `evidence/ns44_metric_replay/certificate.json` | `a32b8d9dac79037392f6dfc124152bf04dcac826864af16dafeb88dcc468781b` |
| `evidence/ns44_metric_replay/witnesses.json` | `3ec8f56770f2b8afacc12b1d4e9b6ad78ae7dfbe5b71ae32b8a1532a22776767` |
| `evidence/v124/g2_schur_cancellation/assembly_general.py` | `4da2e6805e92a2850fe28bd51cd2450d1f2ef0566e9f4f5b5b5fb50db2825b58` |
