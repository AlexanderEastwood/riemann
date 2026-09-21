# The validated symbol β_a and the ground-state level split — DIAGNOSTIC

**Status: diagnostic, not a certificate.** This is the correct version of the
experiment retracted in `evidence/diag_circle_split/results.md`. The object is
now the manuscript's own symbol (`eq:v130-r-symbol`, `eq:v130-beta`):

    β_a(ξ) = Re ψ(5/4 + iξ/2) − log π − r_a(ξ),
    r_a(ξ) = 2 Σ_{1<m<e^{2a}} Λ(m)/√m · cos(ξ log m) − 2 ∫_0^{2a} e^{t/2} cos(ξt) dt,
    q_a[f] = ∫_ℝ β_a(ξ) |F f̃(ξ)|² dξ     (unitary F of the zero extension; prop:v130-remainder / prop:v135-both-parities)

## 1. Validation against the assembled matrix (`beta_check2.py`, λ=3)

Quadrature of `β_a · Fe_n · Fe_m` over ℝ (step 0.01 to ξ=3000 plus an averaged
analytic tail) against `assembly_general.block()`:

| entry | block() | (−1)^{n+m} × quadrature | rel. err |
|---|--:|--:|--:|
| W[0,0] | +0.04085520 | +0.04085521 | 2.5e-7 |
| W[1,1] | +0.08283138 | +0.08283140 | 2.4e-7 |
| W[0,1] | +0.05817114 | +0.05817115 | 2.5e-7 |
| W[1,2] | +0.08464430 | +0.08464432 | 2.2e-7 |
| W[0,2] | +0.05943220 | +0.05943222 | 2.3e-7 |
| W[1,3] | +0.08816769 | +0.08816771 | 1.9e-7 |

So `β_a` is the exact symbol of the assembled operator, and `block()`'s basis
carries a `(−1)^n` relative to the centered cosine transform (window `[0,L]`
vs `[−L/2, L/2]`). Both facts must be used when moving a vector between the
matrix and the transform; the earlier diagnostics used neither.

## 2. The negative set of the true symbol (`true_scan.py`, ξ ∈ [0, 400])

| λ | L | min β_a | at ξ | negative measure (2-sided) | lobes | naive (L/2π)·\|neg\| |
|--:|--:|--:|--:|--:|--:|--:|
| 3 | 2.197 | −2.38 | 35.5 | 70.5 | 33 | 24.6 |
| 4 | 2.773 | −3.37 | 39.3 | 115.9 | 67 | 51.1 |
| 6 | 3.584 | −5.54 | 296.7 | 173.0 | 118 | 98.6 |
| 8 | 4.159 | −6.22 | 362.3 | 212.4 | 161 | 140.6 |

The negative set is large and its deep part is at **high** frequency; the lobes
recur at the window's own resolution period `2π/L`. The last column is what a
Kac–Murdock–Szegő count would give against a certified 0 negative eigenvalues;
it is reported for the record only — KMS's hypotheses (a fixed symbol as
`L → ∞`) do not hold, because the symbol's oscillation scale is tied to `L`.

## 3. Level split of the λ=3 ground state (`ground_true.py`, `levels_true.py`)

Ground vector of the N=120 even compression by a full eigensolve (1024-bit
assembly, 220 digits; `ε_N = 2.954e-38`, tail components ~1e-20 by n=60).

| quantity | value |
|---|--:|
| Plancherel `∫\|Ff\|²` | 1.000000 |
| `q_neg = ∫_{β<0} β\|Ff\|²` | −0.089782 |
| `q_pos = ∫_{β>0} β\|Ff\|²` | +0.089782 |
| `q_neg + q_pos` | +1.4e-16 (true `ε_N` = 2.95e-38; quadrature-limited) |
| mass of `\|Ff\|²` on `{β_a<0}` | 0.4991 |

By frequency band (negative / positive level energy): `[0,5)`: −0.0828 / +0.0729;
`[5,10)`: −0.0069 / +0.0167; `[10,20)`: −0.0001 / +0.0002; nothing beyond.

**Reading.** The identity `q = ∫β_a|Ff|²` is verified on the ground state to
16 digits. The ground state is a low-frequency object (`ξ ≲ 10`) sitting half
on the first few negative lobes of `β_a` and half on the positive crests
between them, with energies `∓0.0898` cancelling to `10^-38`. It puts no mass
where `β_a` is deeply negative (`ξ ≈ 35`, `−2.4`). Hence any bound that sees
only `inf β_a` (the pointwise criterion `eq:v130-pointwise`) is pessimistic by
`−2.4` against a truth of `0`; the weighted concentration criterion
(`eq:v131-weighted-concentration`) must certify that the positive-level mass of
every admissible `f ⊥ u_a` covers its negative-level mass — at the ground state
that is an equality at scale `0.09`. This is the number the live mechanism has
to control, on the right object. Nothing here is a bound.

## 4. The same split at the certified window λ=4 (`levels_l4.py`)

Ground of the N=120 even compression (`ε_N = 3.743e-75`; certified complete
`μ0 < 2.454e-75`, `prop:v140-ground4`).

| quantity | λ=3 | λ=4 |
|---|--:|--:|
| Plancherel | 1.000000 | 1.000000 |
| `q_neg` | −0.089782 | −0.225661 |
| `q_pos` | +0.089782 | +0.225661 |
| `q_neg + q_pos` (true) | +1.4e-16 (2.95e-38) | −8.3e-17 (3.74e-75) |
| mass on `{β_a<0}` | 0.4991 | 0.5011 |
| energy in `[0,5)` neg / pos | −0.083 / +0.073 | −0.185 / +0.204 |
| energy in `[5,10)` | −0.007 / +0.017 | −0.039 / +0.021 |
| energy in `[10,20)` | −0.0001 / +0.0002 | −0.0008 / +0.0003 |
| beyond 20 | 0 | 0 |

The cancellation scale grows with the window (0.090 → 0.226) while the
structure is unchanged: half the Fourier mass on the negative set, everything
below `ξ ≈ 10–20`, nothing at the deep high-frequency negativity. The next
step in this lane (NS-16) is the same split over the source-orthogonal
complement `f ⊥ u_a` — the class the weighted criterion actually quantifies
over — rather than the ground alone.
