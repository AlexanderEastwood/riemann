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

## 5. The ground in lattice units across λ (`selfsim.py` → `selfsim_output.txt`; N=120 even, midpoint eigensolve)

Question: does the ground state have a limiting shape in the window's own
frequency units `u = ξL/2π` (one unit = one resolution cell = one lattice
mode)? Answer: **no.** Both the ground and the symbol change with λ in those
units, in opposite directions.

Ground-state Fourier mass per lattice cell (`2∫|Ff|²` over the cell; rows sum to 1):

| λ | [0,½) | [½,1½) | [1½,2½) | [2½,3½) | [3½,4½) | [4½,6½) | [6½,10½) |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | 0.326 | 0.471 | 0.173 | 0.029 | 0.002 | 0.000 | 0.000 |
| 4 | 0.267 | 0.429 | 0.221 | 0.070 | 0.013 | 0.001 | 0.000 |
| 6 | 0.212 | 0.369 | 0.244 | 0.120 | 0.043 | 0.012 | 0.000 |
| 8 | 0.186 | 0.335 | 0.243 | 0.141 | 0.065 | 0.029 | 0.001 |

Lattice-mode coefficients `|v_0..v_5|` tell the same story (λ=3: 0.58, 0.69,
0.41, 0.16, 0.03, 0.00; λ=8: 0.43, 0.58, 0.49, 0.37, 0.25, 0.15). The ground
**delocalizes outward in lattice units** as the window grows, even though it
contracts in physical frequency (§3–4: everything below ξ ≈ 10–20).

The validated symbol at fixed `u`:

| λ | u=¼ | u=½ | u=¾ | u=1 | u=1¼ | u=1½ | u=2 | u=2½ | u=3 | u=4 |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | −0.001 | −0.285 | +0.005 | +0.284 | −0.012 | −0.279 | +0.272 | −0.259 | +0.238 | +0.119 |
| 4 | −0.000 | −0.687 | +0.001 | +0.695 | −0.001 | −0.708 | +0.728 | −0.757 | +0.797 | +0.935 |
| 6 | −0.010 | −0.509 | +0.029 | +0.512 | −0.049 | −0.515 | +0.520 | −0.527 | +0.536 | +0.562 |
| 8 | +0.000 | −0.131 | −0.001 | +0.132 | +0.002 | −0.134 | +0.138 | −0.142 | +0.148 | +0.166 |

So at low frequency `β_a` is a clean alternating train in the window's own
units: zeros at the quarter points, troughs at half-integers, crests of equal
magnitude at the integers — i.e. exactly on the lattice modes the window
samples. Its amplitude is **not monotone in λ** (0.28, 0.70, 0.51, 0.13). The
train comes from the `−r_a` term, whose low-frequency size is the *weighted*
Chebyshev remainder

    r_a(0) = 2 [ Σ_{1<m<λ²} Λ(m)/√m − 2(λ−1) ]  =  −1.66, −2.06, −1.88, −1.50   (λ = 3, 4, 6, 8),

which orders the four windows the same way as the crest amplitude (4 > 6 > 3 > 8).
The remainder is the whole explanation of the *ordering*, not a formula for the
amplitude (the constant `Re ψ(5/4) − log π = −2.11` and the ξ-dependence of
the continuum term also enter). Earlier wording that attributed this to
`ψ(λ²) − λ²` was loose; the relevant object is the `1/√m`-weighted sum.

**Reading.** In lattice units the ground state's energy budget is a
window-by-window arithmetic quantity: the ground samples a ± train whose
amplitude is set by the prime-power remainder at the cutoff `λ²`, spreading
over more cells as the window grows. There is no λ-independent limiting
picture in these units, so a self-similar (renormalization-style) argument
for the ground alone has nothing to act on. Nothing here is a bound.

## 6. The negative lobe nearest the first zeta ordinate (`nearzero.py` → `nearzero_output.txt`)

`γ₁ = 14.1347`. For each λ, the *negative interval of `β_a` nearest `γ₁`*
(not a lobe centred on `γ₁`: at λ=3 it lies below, at λ ≥ 4 above), its
depth and width, and the ground's mass and negative-level energy there.

| λ | L | ε_N | lobe centre | depth | width | width·L/2π | mass in `\|ξ−γ₁\|<1` | mass in lobe | E_neg in lobe | mass ξ>10 |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | 2.197 | 3.0e-38 | 12.289 | −0.668 | 1.258 | 0.440 | 3.9e-6 | 1.5e-4 | −5.6e-5 | 1.7e-3 |
| 4 | 2.773 | 3.7e-75 | 15.613 | −0.550 | 0.988 | 0.436 | 2.7e-6 | 1.1e-6 | −3.7e-7 | 1.4e-3 |
| 6 | 3.584 | 3.1e-150 | 15.293 | −1.442 | 0.804 | 0.459 | 2.0e-6 | 5.5e-7 | −5.1e-7 | 1.1e-3 |
| 8 | 4.159 | 7.5e-190 | 15.241 | −2.130 | 0.764 | 0.506 | 1.4e-6 | 3.5e-7 | −4.8e-7 | 9.4e-4 |

(ε_N at λ=6, 8 is the N=120 midpoint value at 2048 bits, cutoff-limited;
the certified values are in `evidence/v138/`.)

Three things are happening at once near `γ₁`:

1. the nearest lobe **deepens** (−0.55 → −2.13 from λ=4 to 8), consistent
   with the unconditional `inf β_a → −∞` of `cor:v137-scalar-no-go`;
2. it **narrows** in physical frequency but stays about **half a resolution
   cell** wide (0.44–0.51 of `2π/L`), so the window cannot resolve it;
3. the ground's mass in it **shrinks** (1.5e-4 → 3.5e-7 from λ=3 to 8) and
   its negative-level energy there stays at the 1e-7 scale — five to six
   orders below the ∓0.09 / ∓0.23 cancellation budget of §3–4.

In lattice units `γ₁` sits at `u = γ₁L/2π = 4.9, 6.2, 8.1, 9.4`, at the outer
edge of the ground's support (§5: 1e-3 of the mass in `[6.5,10.5)` at λ=8).
Both the ground's spread and `u(γ₁)` grow with `L`; whether the ground's mass
at `u(γ₁)` stays negligible as `a → ∞` is the local, quantitative form of the
open question, and two more windows would not settle it
(`prop:v121-cofinal-rh`). The frontier this lane leaves is therefore: the
ground's energy near the first zeta ordinate is a race between a lobe that
deepens like `a` (`cor:v137-scalar-no-go`) and half a cell wide, and a ground
whose mass there is currently 1e-6 and falling. Nothing here is a bound.
