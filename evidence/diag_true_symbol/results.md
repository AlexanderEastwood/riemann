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

## 7. The level pencil: is the cancellation one direction or a block? (`pencil.py` → `pencil_output.txt`, `pencil_N96_output.txt`)

Question left by §3–6: the ground state cancels ∓0.09 (λ=3) / ∓0.23 (λ=4)
of negative- and positive-level energy to 1e-38 / 1e-75. Is that a single
critical direction, with the rest of the head comfortably positive, or is the
whole deep block a cancellation? The weighted criterion
(`eq:v131-weighted-concentration`) quantifies over every admissible `f`, so
the answer decides whether G2 at a window is a one-dimensional problem.

Method. `W = block()` (Arb, exact), `W⁻ = ∫ β_a⁻ |Fe|²` (negative level,
float quadrature over the bounded negative set; the part beyond the grid is
≤ 3e-4 relative, `wminus_tail.py`), `W⁺ = W + W⁻`. The pencil
`W v = ν W⁺ v` gives `ν_k = q[v_k]/q⁺[v_k]`, the fraction of positive-level
energy that survives in direction `k`; `ν ≥ 0` in every direction is
positivity, and `1−ν_k = μ_k` is the negative-to-positive ratio. The
numerator is exact and the denominator is accurate to ~1e-6 (the full-symbol
quadrature reproduces `block()` to 7e-5 on every head entry with `|W| > 1e-2`,
2e-6 on the low block), so each
`ν_k` carries about six *relative* digits however small it is. Solved in
mpmath at 120 digits.

Even head N=48 (`e_k` = eigenvalues of `W` itself, for comparison):

| λ | ν_0 | ν_1 | ν_2 | ν_3 | … | first ν > 1e-2 at k | e_k/ν_k over the deep block | #ν < 1e-8 | #ν < 1e-16 | #ν < 1e-30 |
|--:|--:|--:|--:|--:|:-:|--:|--:|--:|--:|--:|
| 3 | 4.7e-37 | 3.5e-30 | 4.7e-24 | 6.2e-19 | … | 7 (0.011) | 0.09 – 0.50 | 6 | 4 | 1 |
| 4 | 2.9e-65 | 2.7e-58 | 5.2e-52 | 5.3e-46 | … | 14 | 0.23 – 0.69 | 12 | 10 | 7 |
| 6 | 6.3e-92 | 5.5e-85 | 1.3e-78 | 9.7e-73 | … | >14 | 0.17 – 0.53 | 21 | 18 | 13 |
| 8 | 1.5e-105 | 1.0e-98 | 1.6e-92 | 9.8e-87 | … | >14 | 0.04 – 0.41 | 26 | 22 | 17 |

Cutoff dependence of the counts (`#ν < 1e-8 / 1e-16 / 1e-30`):

| λ | N=24 | N=48 | N=96 |
|--:|--:|--:|--:|
| 3 | 6 / 4 / 1 | 6 / 4 / 1 | — |
| 4 | 9 / 7 / 3 | 12 / 10 / 7 | 13 / 10 / 7 |
| 6 | — | 21 / 18 / 13 | 30 / 26 / 22 |
| 8 | — | 26 / 22 / 17 | 41 / 37 / 31 |

So the block is converged in N at λ=3 and λ=4 (a head of ~2λ² modes
suffices) and still growing with the cutoff at λ=6 and 8: there the count is
a finite-section quantity and the numbers above are lower bounds on the deep
block of the complete operator. At N=96 and λ ≥ 6 the smallest `ν_k` sit
below the 120-digit working precision (values of order ±1e-116 are
numerical zero, not negative eigenvalues; the complete operator is certified
nonnegative in `evidence/v138/`), which does not affect the counts at the
1e-30 threshold. The `e_k` are the compression's eigenvalues, not the
certified complete values (`v138/`, `v140/`), and are quoted only for the
ratio; at λ=4, N=96, `e_0 = 5.2e-75` sits above the certified complete
`μ0 < 2.454e-75` as it must. The validation line in `pencil_N96_output.txt`
predates the tail-factor fix in `pencil.py` and reads a few percent; the
pencil itself never uses that quadrature (`W` is exact from Arb), so the
`ν_k` are unaffected; `pencil_output.txt` carries the corrected line (≤ 7e-5).

**Reading.**

1. **It is a block, not a direction.** Every deep direction has `ν_k ≈ e_k / q⁺`
   with `q⁺` between 0.05 and 0.7: in each of them a positive-level energy of
   order 0.1–0.5 is cancelled by an equal negative-level energy down to `e_k`.
   The ground is only the tightest of these. The number of directions cancelled
   below 1e-8 grows with the window (6, 13, ≥30, ≥41 at λ = 3, 4, 6, 8),
   of the order of the deep-block size `N ~ λ²` (AGENTS.md §8),
   and the pencil spectrum decays super-exponentially with a step that shrinks
   as `k` grows (λ=8: 7, 7, 6, 6, 5, 5, 4 decades per step).
2. **What this rules out.** Any argument that treats the ground state as
   the single delicate direction and bounds the rest of the head by a
   comfortable margin is wrong in its premise: at λ=8 the thirty-first
   direction is still cancelled to 1e-30. This is the finite-dimensional
   face of `cor:v137-scalar-no-go` and of the meta-obstructions of v1.39:
   arithmetic-blind bounds fail on the whole deep block, not at one vector.
3. **What this leaves — with a qualification (2026-09-21, after Astra's
   translation of the criterion into these coordinates).** The pencil
   vectors `v_k` order the head by `q/q⁺`, and for a source-admissible
   direction the minorant of `eq:v131-step-minorant` may lose at most
   `ν_k q⁺[v_k] + η_a ‖v_k‖²` there. At *zero* allowed error that is a
   relative loss of at most `ν_k`, i.e. down to 1e-100 at λ=8 in ~40
   directions at once — the exact-positivity reading. But the target is the
   uniform finite floor of `prop:v136-bounded-floor`, which allows a finite
   `η_a` uniformly bounded in `a`; a finite `η_a` swamps every `ν_k` above,
   so the tiny values do **not** by themselves obstruct the weaker goal. Two
   further qualifications: this pencil is on the uncompressed even head,
   whereas the criterion acts on the source complement; and directional
   checks do not control mixtures (the cross-term rule of
   `prop:v126-direction-complement`). The directional test is a
   finite-window statement; using it for the live criterion still needs the
   full complement and uniform control along a cofinal family. Nothing here
   is a bound.

## 8. The layer-cake constant η_a^op on the even head (`layercake.py` → `layercake_output.txt`, `layercake_N256_output.txt`)

Follow-up to §7's qualification: under the bounded-floor target
(`prop:v136-bounded-floor`) the question is not the tiny `ν_k` but whether
the concentration mechanism's loss `η_a` can be kept bounded in `a`. The
first form of the mechanism is the layer-cake bound `eq:v131-layercake`,

    q[f] ≥ −η_a^op ‖f‖²,   η_a^op = ∫_0^{D_a} ‖C_a(E_a(t))‖ dt,   E_a(t) = {β_a < −t},

with `D_a = ‖β_a⁻‖_∞`. Here `‖C_a(E)‖` is the top eigenvalue of the
concentration matrix `∫_E Fe_n Fe_m` on the even head (source term omitted,
so this is the norm on the full head: an upper bound for the complement and a
lower bound for the complete operator; 80 levels of `t`; grid to ξ=800, so
the deepest lobes beyond 800 at λ=6, 8 are missed and `D_a` there is the
grid value, 5.54 / 6.22 against 5.81 / 7.82 on [0, 4000]).

| λ | a | D_a (grid) | η_a^op, head 48 | η_a^op, head 256 | η/D_a | trace bound | ‖C(E(0))‖ | \|E(0)\| |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | 1.099 | 2.378 | 0.862 | 0.862 | 0.36 | 1.99 | 0.63 | 81 |
| 4 | 1.386 | 3.419 | 1.200 | 1.206 | 0.35 | 3.11 | 0.81 | 146 |
| 6 | 1.792 | 5.537 | 1.30 (cut off) | 1.886 | 0.34 | 4.58 | 0.72 | 251 |
| 8 | 2.079 | 6.221 | 1.37 (cut off) | 2.128 | 0.34 | 5.45 | 0.80 | 331 |

Head 48 only reaches ξ < 2πN/L (84 at λ=6), below the deep lobes, which is
why its λ=6, 8 values are too small; head 256 covers ξ < 449 / 387 and is
converged at λ=3, 4 (identical to head 48 there). The norm profile is close
to linear in the level: `‖C(E(t))‖ ≈ 0.6–0.8 · (1 − t/D_a)`.

**Reading.**

1. **The layer-cake loss is a fixed fraction of the depth, ~0.35 D_a.**
   Since `D_a → ∞` unconditionally (`cor:v137-scalar-no-go`,
   `inf β_a → −∞`), `η_a^op → ∞` along with it: the unweighted layer-cake
   form of the mechanism does not give a uniform finite floor either. This
   is a statement about the bound, on the head; the true form is ≥ 0.
2. **The concentration norm never approaches 1**, even for the whole
   negative set (0.63–0.81 at `t = 0`, with `|E(0)|` in the hundreds). The
   negative set is a comb at the window's own resolution (§5), and a comb of
   half-cells has concentration eigenvalues bounded away from 1 no matter
   how many teeth it has. That is the same fact as the pencil's 50/50 level
   split, seen from the operator side. The trace bound
   `eq:v131-trace-bound` (min{1, tr}) is far weaker than the norm
   (1.99 vs 0.86 at λ=3) and is not the right tool here.
3. **What a bounded floor would need.** A step minorant with finitely many
   weighted sets recovers at most the layer-cake profile unless the sets
   `G_{a,j}` follow the comb, i.e. unless the minorant tracks `β_a` at the
   cell scale. As `J → ∞` the weighted form reproduces `q` exactly, so it
   is not a closure; but any bounded-complexity minorant that ignores the
   cell-scale structure loses `~0.35 D_a → ∞`. The remaining question for
   the mechanism is therefore purely about that fine structure: whether a
   minorant with `J` growing with `a` can hold the loss bounded, which is
   the arithmetic-blind obstruction of v1.39 in operator form. Nothing here
   is a bound.
