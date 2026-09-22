# NS-28: the two inputs of `prop:v146-level-complexity`, measured — DIAGNOSTIC, NOT A CERTIFICATE

Even head, N=256 window modes (reach `ξ < 2πN/L` = 732 / 580 / 449 / 387 at
λ = 3 / 4 / 6 / 8), grid `ξ ∈ [0, 800]`, `W = block()` Arb midpoints in float64
(energies below 1e-16 read as 0), `β_a` from `evidence/diag_true_symbol/pencil.py`.
`D = D_a` is the grid value (5.54 / 6.22 at λ = 6 / 8 against 5.81 / 7.82 on
[0, 4000]: the true depth is larger there, which only makes the conclusions below
stronger). Scripts: `level_dist.py`, `min_energy_lp.py` (needs scipy, added to
the venv 2026-09-21). Nothing here is a bound; nothing bears on G2 or RH.

## 1. The question

`prop:v146-level-complexity` (v1.46) gives, for a unit source-admissible `g`
with `q_a[g] ≤ Q` whose Fourier mass is spread over the levels of `β_a` with
density at least `c/D` on `[−D, 0]` (`eq:v146-level-density`), the bound

    η(m) ≥ c D / (2K) − Q                      (eq:v146-level-lower)

for every step minorant with `K` distinct values. Its content depends on two
numbers nobody had measured: the achievable level constant `c`, and the energy
`Q` a state must pay to achieve it. Because the proposition is linear in
`|F g|²`, it holds verbatim for a density matrix `X`, so the right quantity is

    Q_min(c) = min { tr(W X) : X ⪰ 0, tr X = 1, tr(M_b X) ≥ c/D for all 20 level bins b }

with `M_b` the level-density matrix of bin `b`. Its SDP dual gives a lower
bound valid for **every** state in the head; the dual's minimizing eigenvector
gives a pure state whose energy is an upper bound. The two coincide to all
printed digits in almost every cell below (the optimum is rank one), so
`Q_min(c)` is determined on the head.

## 2. Level-set measure of the symbol (`level_dist.py`)

Fraction of `[0, 800]` on which `β_a < −t`, and the number of lobes reaching below `−t`:

| t/D | 0 | 0.3 | 0.5 | 0.7 | 0.8 | 0.9 |
|--:|--:|--:|--:|--:|--:|--:|
| λ=3 measure | 0.050 | 0.021 | 0.010 | 0.0038 | 0.0021 | 0.0006 |
| λ=3 lobes | 42 | 22 | 14 | 6 | 4 | 2 |
| λ=4 measure | 0.091 | 0.035 | 0.017 | 0.0054 | 0.0032 | 0.0015 |
| λ=4 lobes | 91 | 46 | 29 | 12 | 8 | 5 |
| λ=6 measure | 0.157 | 0.055 | 0.017 | 0.0034 | 0.0010 | 0.0003 |
| λ=6 lobes | 183 | 100 | 39 | 13 | 3 | 1 |
| λ=8 measure | 0.207 | 0.080 | 0.028 | 0.0066 | 0.0022 | 0.0004 |
| λ=8 lobes | 269 | 170 | 73 | 27 | 9 | 2 |

The negative set grows with the window, but the deep levels stay rare: below
`−0.9D` the symbol occupies 0.03–0.15 % of the range, in one to five lobes.
Uniform density on `[−D, 0]` is therefore an expensive shape for a state to
have: its deepest bins can only be fed from one or two troughs.

## 3. Level distributions of the natural states (`level_dist.py`)

`c` = best constant on 20 bins; `Q = q_a[g]`.

| state | λ=3 | λ=4 | λ=6 | λ=8 |
|---|--:|--:|--:|--:|
| deep pencil directions k = 0..3: empty bins / 20 | 6, 0, 0, 0 | 9, 8, 6, 0 | 10, 10, 10, 10 | 13, 12, 12, 11 |
| their `c` | 0 | 0 | 0 | 0 |
| their `Q` | ≤ 1e-13 | ≤ 1e-12 | ≤ 1e-16 | ≤ 1e-16 |
| packet at the deepest trough: `c` | 0.285 | 0.296 | 0.210 | 0.251 |
| packet at the deepest trough: `Q` | 0.332 | 0.620 | 1.352 | 1.806 |
| packets at the other four deepest troughs: `c` | ≤ 0.004 | ≤ 0.25 | 0 | 0 |
| sum of 5 packets: `c`, `Q` | 0.233, 1.04 | 0.270, 1.26 | 0.168, 1.52 | 0.277, 1.86 |

The deep pencil directions live entirely at shallow levels: at λ=3 the ground
has all its negative-level mass in `β ∈ [−0.15D, 0]` and nothing below
`−0.3D`; at λ=6, 8 nothing below `−0.5D`. They are the states with `Q ≈ 0`,
and they satisfy the level hypothesis with `c = 0`. The states that reach the
deepest level are packets at the single deepest trough, with `c ≈ 0.2–0.3`
(stable in λ) but `Q` growing with the window (0.33 → 1.81). For these, the
bound `cD/(2K) − Q` is negative for every `K ≥ 1` at λ ≥ 4.

## 4. The minimum energy for a given level constant (`min_energy_lp.py`)

`Q_min(c)`: dual lower bound = pure-state upper bound unless stated. `K_max` is
the largest `K` for which `cD/(2K) > Q_min(c)`, i.e. for which
`eq:v146-level-lower` says anything.

| c | λ=3 `Q_min` | `K_max` | λ=4 `Q_min` | `K_max` | λ=6 `Q_min` | `K_max` | λ=8 `Q_min` | `K_max` |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 0.01 | 1.3e-10 | 9e7 | ≤ 1e-15 | ∞ | 4e-4 – 1.6e-2 | 1–69 | 3.4e-4 | 92 |
| 0.03 | 5.7e-8 | 6e5 | ≤ 1e-15 | ∞ | 2.8e-2 | 2 | 2.0e-3 | 46 |
| 0.05 | 2.3e-7 | 2.6e5 | ≤ 1e-15 | ∞ | 4.7e-2 | 2 | 5.2e-3 | 30 |
| 0.10 | ≤ 1.6e-6 | ≥ 7e4 | ≤ 1.5e-4 | ≥ 1111 | 9.5e-2 | 2 | 1.9e-2 | 16 |
| 0.20 | 6.1e-5 | 3908 | 4.3e-8 | 8e6 | 0.190 | 2 | 6.4e-2 | 9 |
| 0.30 | 5.4e-4 | 666 | 4.7e-4 – 2.5e-3 | 100–1095 | 0.288 | 2 | 0.125 | 7 |
| 0.50 | infeasible on 20 bins at every window | | | | | | | |

(Where the dual and pure-state values differ, the range is shown; at λ=4,
`c ≤ 0.1`, the near-null space itself carries enough deep-level mass, so the
cost is at the float floor.)

## 5. Reading

1. **`c` is not the problem.** States with level constant 0.2–0.3 exist at all
   four windows (0.5 does not, on 20 bins). The constant is stable in λ.
2. **`Q_min(c)` is the problem, and it grows with the window.** At c = 0.3 it
   is 5e-4 (λ=3), ~1e-3 (λ=4), 0.29 (λ=6), 0.13 (λ=8): three orders of
   magnitude between λ=4 and λ=6. The reason is §2: the deepest levels are
   attained in one or two lobes, so a state that must put mass at level
   `−0.95D` has to pay for a packet at that trough, whose energy is of order 1.
   Hypothesis (b) of v1.46, `Q ≤ Q_*` uniformly, holds trivially (Q_min ≤ 0.3),
   but that is not the regime in which the bound has content.
3. **What the theorem can reach.** `eq:v146-level-lower` is informative only
   for `K ≤ K_max(c)`: hundreds to thousands of levels at λ=3, 4, but **2** at
   λ=6 and **7–16** at λ=8 (with the grid `D`; the true deeper `D_a` pushes the
   deepest bins further out and lowers these). NS-22 measured that the
   quantization minorants need `J ≈ 1.2 D_a/η` levels, i.e. 13–15 levels for
   `η ≤ 0.5` at λ = 6, 8. So at the windows where the loss is large, the
   conditional theorem with its best possible constants on the head does not
   reach the level counts the actual minorants use; at λ=8, K=8, the best it
   can say is `η ≥ 0.02`, against a measured loss near 3.
4. **The shape of the hypothesis is wrong, not just unproved.** Requiring
   uniform density on `[−D, 0]` forces mass onto the rarest levels, which is
   exactly where energy is expensive. A hypothesis weighted by the symbol's own
   level-set measure (density relative to `|{β_a ∈ B}|`, not to `|B|`) is what
   cheap states actually satisfy, and the proof of `prop:v146-level-complexity`
   goes through with the gap lengths `Δ_j` replaced by the level-set measures
   of the gaps. Whether that weighted version still forces the level count to
   grow with `a` is the question to hand back; the numbers here say the
   uniform version does not.
5. Caveats: even head, N=256, float; `c` on 20 bins (a finer partition can only
   lower `c`); grid `D` at λ ≥ 6; the source constraint is not imposed (the
   states here are not projected off `u_a`, which can only raise `Q_min`).
