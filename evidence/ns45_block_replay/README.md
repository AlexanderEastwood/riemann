# NS-45: fresh replay of the existing signed-block comparison failure

Classification: **certified computation**, with exact dyadic witnesses, fresh Arb interval gates at 320 and 448 bits, and exact rational Rayleigh arithmetic. The float proposal is not proof evidence.

This is a new witness certificate for the existing lambda=5, N=25 partition. It does **not** recover the absent v1.28 files, certify the historical displayed lower numbers, or assert full block positive definiteness. The original missing evidence record must remain distinguished from this replacement evidence.

## Exact finite object

Both parity sectors use the same first three literal blocks of the existing partition:

- I0 = 26 through 50.
- I1 = 51 through 100.
- I2 = 101 through 200.

The fourth block 201 through 400 is not needed. Every vector coordinate is an integer divided by 2^60. Each pair has its own vectors; no common physical vector across the three pair tests is required for operator-norm lower bounds.

The exact rational comparison matrices have zero diagonals and symmetric entries:

| Parity | H01 | H02 | H12 | Exact Rayleigh quotient on (1,1,1) |
|---|---:|---:|---:|---:|
| Even | 997/1000 | 568/1000 | 481/1000 | 341/250 = 1.364 > 1 |
| Odd | 997/1000 | 484/1000 | 612/1000 | 2093/1500 > 1 |

These are deliberately coarse fresh lower bounds, not the original v1.28 integers.

## Gates replayed at both precisions

For each of three block pairs in each parity, the verifier checks:

1. Ex = xᵀTjj x > 0 and Ey = yᵀTkk y > 0 using Arb intervals.
2. (xᵀTjk y)^2 − Hjk² Ex Ey > 0 using Arb intervals. Together with positive energies and Hjk≥0, this proves the normalized absolute coupling exceeds Hjk. A direct interval square-root quotient gate is checked as well.
3. A separate signed-index expansion over +n and −n verifies both positive energies and the squared coupling gate. Its three pairings overlap the parity-block assembly.
4. Exact Fraction arithmetic checks 2(H01+H02+H12)/3 > 1, with no midpoint eigenvalue in this gate.

The signed-index expansion uses ±x_n/√2 in the two parity embeddings; the odd embedding differs from the physical sine convention by one harmless common complex phase. It is an independent parity/sign/index assembly check using the **same** analytic coefficient enclosures, not an independent analytic derivation of those coefficients.

Every coefficient is recomputed by the audited `assembly_general.sequences(5,200,bits,K=96)` with its analytic infinite-series remainder. A newly created temporary cache directory is installed for each precision and removed afterwards; preexisting cache files cannot supply the coefficients. The verification path has no midpoint solve, Cholesky factor or eigenvalue. The proposal path alone uses midpoint matrices, float Cholesky factors and singular vectors.

The smallest recorded x-energy among these pairs is the even 02 value, approximately 1.2991502856e−7; it is strictly positive as an interval at both precisions. The smallest squared gate gap is the even 02 value, approximately 6.7932046559e−10; its interval is strictly positive. The JSON retains the full ball strings rather than these display approximations.

## Why no full block inertia certificate is needed

Assume the proposed criterion has metrics 0 < Mj <= Tjj. Then each Tjj must be positive definite. Under this hypothesis, the verified pair quotients are lower bounds for beta_jk(T), and the analytic `lem:v128-comparison-obstruction` shows beta_jk(M) >= beta_jk(T). The rational H has largest eigenvalue strictly above one because of its exact Rayleigh quotient. Therefore no positive row-weight vector can make the weighted coupling row sums strictly below one, even after adding any infinite continuation of the same partition.

If such positive metrics do not exist, the criterion's prerequisite already fails. This dichotomy proves the stated comparison obstruction without asserting or proving unused full-block inertia.

The result is failure of this fixed partition's norm-comparison criterion for every admissible smaller metric and every positive scalar row reweighting. It is **not** a negative Weil direction, a complete lambda=5 sign result, a spectral-gap claim, a new tail metric, or a cofinal/G2/RH conclusion. It does not exclude other cutoffs or partitions.

## Reproduction and files

From the repository root with the existing virtual environment:

```sh
.venv/bin/python evidence/ns45_block_replay/replay.py --verify
pyright evidence/ns45_block_replay/replay.py
```

`--propose` is solely the original proposal stage and refuses to overwrite existing frozen witnesses. Do not run with Python `-O`; the script rejects disabled assertions.

- `witnesses.json`: exact integer coordinates, denominators, and rational H entries.
- `certificate.json`: all 320/448-bit gates, pairings, rational quotients, source hashes and frozen-witness hash.
- `replay-output.txt`: first proposal and successful two-precision run.
- `verification-output.txt`: successful final-script replay of the same frozen witnesses.
- `pyright-output.txt`: zero errors and zero warnings.
- `block-comparison-replay-2026-09-22-v1.html`: user-facing report.

No manuscript or research map was edited. The assigned scope did not include a manuscript build or new version. Independent code review should check the inverse-Cholesky proposal convention, signed-index diagonal/off-diagonal formula, strict interval squared-quotient gates, rational H arithmetic, and the positive-metric/positive-block dichotomy. Proposal optimality and full block inertia are intentionally not proof dependencies.
