Numerical illustration only; no convergence or certified sign claim.

NS-59 tests how much of the true projected block gain is retained by the
NS-53 raw-trace bound, the projected trace, and explicit block directions.
All old/new cross terms are retained. The starting questions concern this
specific sufficient estimate, not an extension of the table of distances.

The floating scan is a proposal diagnostic. Any finite bound entering the
research conclusion will be replayed separately in Arb at two precisions.

## Recorded outcome

The raw trace retained under 1/400 of the true gain at N=128 and N=256.
These two finite comparisons were separately certified in evidence/v158.
Changing to adjacent differences reduces the trace but also transforms the
correlations; its trace bound is worse at N=256. The v2 float scan records
that full change and agrees with the finite Arb replay where they overlap.

The raw difference spectral norm appeared roughly log(N)/N^2 in a small
exploratory scan. This visual scaling is not an asymptotic theorem: the
analytic argument in v1.58 excludes EVERY fixed logarithmic raw norm bound
at N^(-2), using known zeta large values. The projected norm and the
particular residual direction are outside that obstruction.

Files float-blocks-512-v1.json and float-blocks-2048-v1.json record the
initial raw/projected comparisons. The current generator adds adjacent
differences, as recorded in float-blocks-2048-v2.json. All three are
numerical illustrations. No finite failure disproves cofinal RBC.
