# Reproduce the v1.38 finite-floor certificates

Dependencies: Python 3, python-flint 0.9.0, NumPy, SciPy, threadpoolctl. Install them in an isolated environment. No zeta zero list, RH assumption, old tail witness or missing cumulative archive is needed for this update's certificates.

From this directory:

```sh
OPENBLAS_NUM_THREADS=2 python3 pack_and_replay.py --bits 256
python3 cutoff_cost.py
```

The first command replays the supplied exact IEEE754 dyadic witnesses; it does not regenerate them. It freshly evaluates all coefficients and analytic remainder enclosures if no matching coefficient cache exists. The cache header must record the correct lambda, J, bits and K = 64. To force fresh evaluation, move aside only matching `sequences_v2_l*_J = 4096_b256.json` cache files before the run.

`dyadic_witnesses.npz` contains the six congruence matrices and six finite trial vectors, using `allow_pickle=False`. The report records its SHA256. All proof gates are outward Arb inequalities. Floating eigensolvers and Cholesky are used only by the optional proposal script, not as evidence of positivity. The replay also verifies the lower bounds for the generalized certificate margin.

To regenerate proposals for one sector, for example:

```sh
OPENBLAS_NUM_THREADS=2 python3 shifted_floor.py --lam 8 --parity odd --N 256 --J 4096 --r 16 --bits 160 --shifts 8
```

Do not overwrite the frozen NPZ when replaying the published witnesses. The optional `--pack` operation is for producing a new snapshot after all six initial JSON outputs exist. The published initial certificate summaries omit the bulky duplicated dyadic arrays; the NPZ is their complete witness representation.

`assembly_general.py` is copied unchanged from the audited archived source, Git blob `794fdd1a236798586b9c7e0366552887eb753712`. The complete parity wrapper in `shifted_floor.py` additionally handles the even zero index with its exact normalization. Prime powers at the full interval length are omitted because that translation is zero in L2.

Scope: complete fixed-window lower floors, not positivity, not a cofinal G2 theorem. The current source and all new evidence are supplied; the historical cumulative reproduction archive is a separate, still unavailable artifact.
