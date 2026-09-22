# NS-44: fresh witnesses against the stipulated 10^-8 D comparison

Classification: **certified computation**, replayed with strict Arb interval gates at 320 and 448 bits. These are fresh replacement witnesses; they are not recovered v1.27 originals. Historical artifact recovery remains **OPEN**.

## Exact object and conclusion

The window is lambda=5. Each frozen vector has exact integer-over-2^60 coordinates supported on modes 17 through 128, hence belongs to the literal Q16 tail. Both even and odd parities are checked. The denominator is D[v]=sum a_n v_n^2, where a_n=-A_n is the complete archimedean diagonal from the audited coefficient routine; it is not the full arithmetic/pole diagonal d_n and not the ordinary L2 norm.

At both precisions, the verifier proves ordinary norm > 0, D[v] > 0, **q[v] > 0**, and **q[v] - D[v]/100000000 < 0**. Thus q[v]/D[v] < 10^-8 in both parities. This refutes only the stipulated universal lower comparison T >= 10^-8 D on Q16. The witnesses have positive complete Weil energy. They are not negative Weil directions, and they do not settle complete lambda=5 positivity or negativity, another metric, a cofinal floor, G2 or RH.

| Parity | q[v] (short display) | D[v] (short display) | q[v]/D[v] (short display) |
|---|---:|---:|---:|
| Even | 1.55884794745770125919e-17 | 2.42677982768940290249 | 6.42352441565298054355e-18 |
| Odd | 2.73181237557136479370e-17 | 2.45491673166065540615 | 1.11279227533041427672e-17 |

The corresponding shifted values are approximately -2.42677982613055495503e-8 and -2.45491672892884303058e-8. These shortened decimals are displays of enclosures, not exact scalar values. The 448-bit ratio balls below are copied verbatim from `certificate.json`:

Even:

```text
[6.4235244156529805435524569703242929577471031414566951511421938983280411697654828869896900689753055118885839140524e-18 +/- 8.40e-131]
```

Odd:

```text
[1.11279227533041427671889054235119593489450463585403682397972153106386274380693016313286838599893918701248166739881e-17 +/- 6.17e-131]
```

## What is independently replayed

`replay.py --verify` rebuilds every coefficient in Arb at each precision using a newly created empty temporary cache and the audited `assembly_general.sequences(5,128,bits,K=96)`. Its analytic infinite-series remainder is retained. Existing rounded sequence caches are not loaded. The same frozen dyadics are used at both precisions; no float renormalization, midpoint solve or midpoint eigenvalue enters a sign gate. The vectors' ordinary norms are close to one but are not asserted equal to one; every conclusion is homogeneous.

The verifier separately expands the quadratic on signed Fourier indices +n and -n, checks its positive q and negative shifted q, and checks overlap with the parity-block result. The odd signed embedding differs from the real sine basis only by a common complex phase, which does not alter the Hermitian quadratic. This is an independent parity/index assembly using the same analytic coefficient enclosures, not an independent derivation of the analytic kernel.

The bounded independent review in `evidence/ns43_route_selection/concentration/ns44_review.md` additionally reran verification in a fresh output directory and used a separately written full signed-index double sum. It records no outstanding MAJOR, MINOR or actionable NOTE after metadata checks were added. The review does not assert that missing historical files were recovered.

Finite support makes these complete-form counterwitnesses to the stated comparison: all other input coefficients vanish, so remote output components contribute nothing to the quadratic. No remote-tail enclosure is needed. An even-source constraint is not part of this universal literal-tail comparison.

## Reproduction and provenance

From the repository root, using the existing virtual environment and ordinary Python assertion mode:

```sh
.venv/bin/python evidence/ns44_metric_replay/replay.py --verify
pyright evidence/ns44_metric_replay/replay.py
```

Do not use Python `-O`, which disables the asserted proof gates. `--propose` is the float-only proposal stage and refuses to overwrite existing frozen witnesses.

- `evidence/ns44_metric_replay/witnesses.json`: exact integer coordinates, support and denominator.
- `evidence/ns44_metric_replay/certificate.json`: both precision records, complete ball strings, gate results, source hashes and witness SHA256.
- `evidence/ns44_metric_replay/replay.py`: proposal and strict interval replay.
- `evidence/ns44_metric_replay/replay-output.txt`: recorded 320/448-bit output.
- `evidence/ns44_metric_replay/pyright.txt`: narrow Python diagnostics.
- `evidence/ns43_route_selection/concentration/ns44_review.md`: independent scoped review and pinned hashes.
- `evidence/ns44_metric_replay/metric-replay-2026-09-22-v1.html`: styled reading copy.

The new certificate supports this newly replayed comparison failure. It does not authenticate the old recorded hashes or reconstruct the original transfer protocol, old witness coordinates, outputs or other absent artifacts. Their archival recovery status remains OPEN. No manuscript build, version change, new window or new tail metric is claimed by this documentation.
