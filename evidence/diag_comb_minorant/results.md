# Comb-following step minorants for the weighted concentration criterion -- DIAGNOSTIC, NOT A CERTIFICATE

> **Correction notice (2026-09-22, after the adversarial audit `audits/circle-symbol-lane-2026-09-22-v2.html` (NS-31, PR #16); originals retained below).**
> Withdrawn: the "charged tail" as a valid global minorant — the charge is the largest sampled depth on a finite scan, and `β_8(130060.425) = −8.812 < −8.050`, `β_6(152359.725) = −6.436 < −5.808` (50-digit values, independently confirmed), so the with-tail η values are outputs of a tail-substituted model, not bounds; (D2) the centered comb was implemented with a nondecreasing (suffix-minimum) profile where a nonincreasing (prefix-minimum) one was required — the corrected λ=4 profile gives η = 3.157 rather than 3.332; (D3) the matrix quantizes a lower-edge rounding of `β` while the pointwise check uses `β` itself; D1 has J+1 values; and the verdict's "every bounded-complexity step minorant loses a fixed fraction of D_a" and "bounded η_a requires the level count to grow linearly with D_a" as conclusions — the optimized losses are upper bounds on the best loss within restricted grid families and cannot bound all minorants or a necessary complexity.
> What stands: the measured losses of the specific families on the head at ξ ≤ 800, as finite-head numbers; the observation that the binding direction is a packet at a deep trough, not the ground.

**Status: diagnostic, not a certificate.** Board row NS-22 (2026-09-21, Claude).
Float quadrature, midpoint eigenvalues, one head size; nothing here is a bound,
and nothing here bears on G2 or RH. Companion to
`evidence/diag_true_symbol/results.md` section 8 (`layercake.py`).

Script: `comb_minorant.py` (run from the repo root with the project venv);
output: `comb_minorant_output.txt`; tables: `comb_minorant_l3_4_6_8.json`.
Helpers `beta_grid`, `Fe_grid` are imported from `evidence/diag_true_symbol/pencil.py`.

## 0. The quantity computed

The live mechanism is `prop:v131-concentration`. With beta_a the validated
symbol (`eq:v130-beta`) and D_a = sup beta_a^-, a step minorant

    -D_a + sum_j w_j 1_{G_j}(xi)  <=  beta_a(xi)   for all xi        (eq:v131-step-minorant)

with symmetric sets G_j and positive weights w_j gives the criterion

    -D_a P_a + sum_j w_j C_a(G_j)  >=  -eta_a P_a,                  (eq:v131-weighted-concentration)

C_a(G) = P_a F* 1_G F P_a.  Writing m := -D_a + sum_j w_j 1_{G_j}, the
left side IS the operator P_a Op(m) P_a with Op(m) = F* m F, so on the even
head (N = 256 modes, matrix entries int m Fe_n Fe_m, unitary F) the loss is

    eta_a(m) := max(0, -lambda_min( P_N Op(m) P_N )).

Everything below is eta_a(m) for explicit step minorants m, on the head
N = 256, grid xi in [0, 800] (step 0.002 below 40, 0.005 above; two-sided by
symmetry), exactly the setting of `layercake.py`.  The pointwise inequality
m <= beta_a was checked on every grid point for every minorant reported;
the maximum violation is 0.0 in all cases (the constructions use bin lower
edges / lobe minima, so this holds by construction).

**Tail treatment (a head artefact, sized in every table).**  The head sees
|xi| > 800 only through the tail matrix T = I - C([0,800]) (Plancherel:
int_R Fe_n Fe_m = delta_nm).  Its norm is NOT small -- ||T|| = 0.26, 0.17,
0.12, 0.10 at lambda = 3, 4, 6, 8 -- because head directions near the cut
(combinations of modes centred just below 2 pi N/L) carry up to a quarter of
their Fourier mass beyond 800, although every single mode carries < 0.3%
there.  A valid minorant must say something on the tail; we charge it at
the worst value found on [800, 40000], m_tail = -D_tail, i.e. we add
-D_tail T.  Every eta is reported twice: "with tail" (a valid global
minorant) and "grid-only" (m := 0 beyond 800, NOT a valid minorant, but the
number `layercake.py` computed).  The difference is the artefact.  Since
beta_a is large and positive near xi = 800 on the grid, the charge matters
only when the minorant is already fine (eta small), and only at lambda = 8
where D_tail = 8.05.

## 1. Setup per window

| lambda | a | L | head reaches xi < 2 pi N/L | D_a (grid, at xi) | D_tail on [800, 40000] (at xi) | neg. set ends | ||T|| | head floor -lambda_min(Op(beta)) grid / with tail | lobes on grid |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | 1.099 | 2.197 | 732 | 2.378 (35.5) | 1.096 (898) | 2448 | 0.258 | 2.3e-5 / 5.4e-5 | 42 |
| 4 | 1.386 | 2.773 | 580 | 3.419 (526.5) | 3.073 (2448) | > 39400 | 0.172 | 6.4e-4 / 1.8e-3 | 91 |
| 6 | 1.792 | 3.584 | 449 | 5.537 (296.7) | 5.808 (2819) | > 39900 | 0.124 | 4e-12 / 6.7e-3 | 183 |
| 8 | 2.079 | 4.159 | 387 | 6.221 (362.3) | 8.050 (35615) | > 39980 | 0.104 | 7e-10 / 7.8e-2 | 269 |

Read: D_a here is the grid value (depth of the deepest lobe below xi = 800),
as in `layercake.py`.  At lambda >= 4 the negative set of beta_a extends past
xi = 40000 and at lambda = 8 the deepest value found is beyond the scan
(8.05 at xi = 35615 on a scan to 40000; the true D_a is at least that).  The
head can only resolve lobes below 2 pi N/L (387 at lambda = 8): the deepest
in-window lobes at lambda = 4 (526, 652, 789), 6 (681, 566) and 8 (635,
752) sit at or beyond the head's reach.  The "head floor" is
-lambda_min(P_N Op(beta_a) P_N): losses below it are not resolved by this
computation; with the tail charge the floor at lambda = 8 is 0.078.

Deepest lobes, depth @ xi (u = xi L / 2 pi is the cell index):

    lambda 3: 2.38@35.5 (u=12.4)   2.14@90.4 (u=31.6)   2.12@280.9 (u=98.2)   2.04@109.3 (u=38.2)   1.84@45.5 (u=15.9)
    lambda 4: 3.42@526.5 (u=232)   3.37@39.2 (u=17.3)   3.30@222.8 (u=98.3)   3.21@81.0 (u=35.8)    3.14@652.1 (u=288)
    lambda 6: 5.54@296.7 (u=169)   4.91@86.0 (u=49.0)   4.79@164.3 (u=93.7)   4.36@680.9 (u=388)    4.29@565.6 (u=323)
    lambda 8: 6.22@362.3 (u=240)   5.66@290.7 (u=192)   5.54@177.4 (u=117)    5.52@634.6 (u=420)    5.51@751.9 (u=498)

None of the deep troughs is in the low cells where the ground lives
(section 5 of `diag_true_symbol`: the ground's mass is in cells 0-4); the
low-cell train has amplitude 0.13-0.71.  The depth D_a is set by lobes at
cell index 12-500, and the lobe depths are densely packed just below D_a
(lambda = 8: eight lobes deeper than 0.84 D_a).

## 2. The constructions

**(A) J deepest troughs.**  Let l_1, l_2, ... be the negative lobes
(connected components of {beta_a < 0} on the grid, each taken with its
mirror image) ordered by depth d_1 >= d_2 >= ..., d_1 = D_a.  The J sets are
the nested complements G_j = complement of (l_1 u ... u l_j), with weights
w_j = d_j - d_{j+1} >= 0 (d_{J+1} := depth of the next-deepest lobe, 0 when
all lobes are used).  This is "the largest constant step on the lobe's
complement that keeps the minorant below beta_a", applied lobe by lobe:
the resulting minorant is

    m_A^J = -d_j on lobe l_j (j <= J),   -d_{J+1} everywhere else.

(The literal non-nested reading -- G_j = complement of l_j alone -- is
degenerate: inside l_1 all the other steps would have to vanish, so it
collapses to J = 1.)  The J -> all limit is the lobe-floor minorant,
-d_j on every lobe and 0 on the positive set.

**(B) One level set.**  G(t) = {beta_a >= -t}, weight D_a - t, i.e.
m = -D_a on {beta_a < -t} and -t elsewhere, for t on the 80-level grid
t = k D_a / 80; the best t is reported.

**(C) Layer-cake reference.**  eta^op = int_0^{D_a} ||C(E(t))|| dt over the
same 80 levels as `layercake.py` (the tail bounded by adding T to C(E(t))
whenever the tail dips below -t).  Also the J -> infinity limit of the
negative level-set family, ||Op(beta_a^-)|| = -lambda_min(Op(-beta_a^-)),
which is the exact loss from dropping the positive part without the
triangle inequality across levels.

**(D1) J-level quantization of beta_a (the comb-following family).**  For
levels s_1 < ... < s_J (s_0 = -D_a) take G_j = {beta_a >= s_j}, w_j = s_j -
s_{j-1}; then m = max{ s_j : s_j <= beta_a }, the step function under
beta_a with J+1 values.  For s > 0 the set {beta_a >= s} is exactly a union
of the positive crest cores around the lattice points 2 pi n / L, for s < 0
the complement of a union of trough cores, so this family follows the comb
by construction; levels may be positive.  Levels are restricted to the 240
bin edges (160 uniform on [-D_a, 0), 80 on [0, max beta_a]); they are
chosen greedily (insert the level that most reduces eta) and refined by
coordinate descent (up to 3 sweeps) at J = 1, 2, 3, 4, 6, 8, 12, 16; the
J = 24..64 entries continue the greedy from the refined J = 16 set.  The
reported eta(J) is therefore an UPPER bound on the best J-level loss; at
J = 1 it reproduces (B) to 4 digits, which is the consistency check.

**(D2) Lattice-periodic comb.**  G(rho) = {xi : dist(xi L / 2 pi, Z) <= rho},
40 nested rings, uniform across all cells, with the largest admissible
profile g(rho) = min of beta_a over the ring and all rings beyond it (so
that the weights are positive).  This is the minorant defined by the
lattice geometry alone, with no cell adaptivity.

**(D3) Binary-coded quantization.**  J sets G_j = {xi : bit j of
floor((beta_a + D_a)/h) is 1} with weights w_j = 2^j h,
h = (D_a + cap)/2^J, cap in {1,...,8} chosen best.  Then m is the uniform
2^J-level quantization of min(beta_a, cap) -- J SETS encode 2^J LEVELS.
This separates the number of sets in `eq:v131-step-minorant` from the
number of distinct values of the minorant.

## 3. Results: references (B), (C), (D2)

All entries are eta / D_a (with tail charge; grid-only in brackets where different).

| lambda | (C) layer-cake eta^op | (C') ||Op(beta^-)|| | (B) best t / D_a | (B) eta | (D2) uniform comb, 40 rings |
|--:|--:|--:|--:|--:|--:|
| 3 | 0.363 | 0.344 | 0.19 | 0.598 | 0.997 |
| 4 | 0.354 [0.353] | 0.320 [0.319] | 0.17 | 0.581 | 0.975 [0.962] |
| 6 | 0.350 [0.341] | 0.309 [0.308] | 0.20 | 0.568 | 0.932 [0.906] |
| 8 | 0.375 [0.342] | 0.296 [0.295] | 0.20 | 0.577 [0.573] | 0.995 [0.957] |

- (C) grid-only reproduces `layercake.py` (0.862, 1.206, 1.886, 2.128) to
  the printed digits; the tail charge adds 0.005-0.2.
- The exact negative-part operator norm (C') is 0.30-0.34 D_a: the
  triangle inequality across levels costs only ~0.02-0.08 D_a, so the
  layer-cake's ~0.35 D_a is essentially the loss of dropping beta_a^+, not
  of the level integral.
- One level set (B) is worse than the layer-cake: best at t = 0.2 D_a with
  eta = 0.57-0.60 D_a, a lambda-independent fraction.  The profile over t
  is flat near the optimum (eta/D_a within 0.02 for t/D_a in [0.1, 0.3]).
- The lattice-periodic comb (D2) is pinned at ~D_a: its profile must sit
  below the deepest cell (g(0) = -D_a), so it is a constant -D_a on the
  head to within 0.5-7%.  A cell-blind comb cannot use the comb.

## 4. Results: (A) the J deepest troughs, eta / D_a

| lambda | J=1 | 2 | 4 | 8 | 16 | 32 | 64 | all lobes (J) |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | 0.950 | 0.945 | 0.885 | 0.830 | 0.737 | 0.570 | -- | 0.515 (42) |
| 4 | 0.991 | 0.980 | 0.953 | 0.858 | 0.792 | 0.704 | 0.575 | 0.479 (91) |
| 6 | 0.939 | 0.927 | 0.878 | 0.854 | 0.813 | 0.748 | 0.688 | 0.463 (183) |
| 8 | 0.950 | 0.938 | 0.936 | 0.908 | 0.852 | 0.817 | 0.737 | 0.444 (269) |

(Grid-only values differ by <= 0.003 D_a.)  The floor d_{J+1} outside the
J chosen lobes stays near D_a for a long time because the lobe depths are
densely packed just below D_a: at lambda = 8, d_9 = 5.2 = 0.84 D_a and
d_65 = 3.3 = 0.54 D_a.  Even with every lobe used the flat lobe floors lose
0.44-0.52 D_a, MORE than the layer-cake (0.35 D_a), because a flat floor
-d_j on a lobe discards the lobe's shape as well as beta_a^+.  At fixed J
the fraction eta / D_a rises with lambda (J = 16: 0.74, 0.79, 0.81, 0.85),
so this family needs J growing faster than the lobe count.  Trough-by-trough
patching is the wrong currency: what a direction sees is not "which lobe"
but "how far below beta_a the step sits", and that gap is ~D_a on every
unpatched lobe.

## 5. Results: (D1) J-level quantization, eta(J)

eta(J) with tail charge [grid-only], and the ratio J eta(J) / D_a:

| J | lambda=3 | 4 | 6 | 8 | J eta/D_a at 3 / 4 / 6 / 8 (grid-only) |
|--:|--:|--:|--:|--:|--:|
| 1 | 1.423 | 1.988 | 3.141 [3.137] | 3.585 [3.565] | 0.60 / 0.58 / 0.57 / 0.57 |
| 2 | 0.982 | 1.399 | 2.178 | 2.479 | 0.83 / 0.82 / 0.79 / 0.80 |
| 3 | 0.727 | 1.058 | 1.624 | 1.862 | 0.92 / 0.93 / 0.88 / 0.90 |
| 4 | 0.603 | 0.875 | 1.394 | 1.547 | 1.01 / 1.02 / 1.01 / 0.99 |
| 6 | 0.428 | 0.631 | 0.912 | 1.105 | 1.08 / 1.11 / 0.99 / 1.07 |
| 8 | 0.334 | 0.491 | 0.718 | 0.876 [0.847] | 1.12 / 1.15 / 1.04 / 1.09 |
| 12 | 0.235 | 0.332 | 0.511 [0.505] | 0.627 [0.591] | 1.18 / 1.16 / 1.10 / 1.14 |
| 16 | 0.180 | 0.258 | 0.380 [0.374] | 0.504 [0.472] | 1.21 / 1.20 / 1.08 / 1.21 |
| 24 | 0.130 | 0.188 | 0.267 | 0.375 [0.329] | 1.30 / 1.31 / 1.15 / 1.27 |
| 32 | 0.098 | 0.139 | 0.198 | 0.296 [0.244] | 1.31 / 1.28 / 1.14 / 1.26 |
| 48 | 0.067 | 0.096 | 0.138 [0.135] | 0.226 [0.159] | 1.34 / 1.34 / 1.17 / 1.22 |
| 64 | 0.050 | 0.071 | 0.102 [0.098] | 0.188 [0.118] | 1.34 / 1.31 / 1.13 / 1.21 |

As a fraction of D_a the whole table is lambda-independent to ~10%:
eta(J)/D_a = 0.58, 0.40, 0.25, 0.14, 0.076, 0.041, 0.021 at J = 1, 2, 4, 8,
16, 32, 64 (grid-only), i.e.

    eta_a(J)  ~  (1.0 - 1.35) D_a / J      for  4 <= J <= 64,  all four windows,

with the constant creeping up slowly with J (uniform-in-level placement
would give exactly (D_a + cap)/J; the optimized levels do a little better
at small J).  The levels chosen at J = 8 are roughly equispaced from
-0.7 D_a to +cap with cap ~ 1.0-1.3 D_a (lambda 3: -1.71, -1.14, -0.61,
-0.03, +0.60, +1.31, +2.15, +3.10), with about half of them negative.

First listed J with eta(J) <= threshold (with tail / grid-only), and J / D_a:

| lambda | D_a | eta <= 1.0 | eta <= 0.5 | eta <= 0.25 | J(0.5)/D_a | J(0.25)/D_a |
|--:|--:|--:|--:|--:|--:|--:|
| 3 | 2.378 | 2 | 6 | 12 | 2.5 | 5.0 |
| 4 | 3.419 | 4 | 8 | 24 | 2.3 | 7.0 |
| 6 | 5.537 | 6 | 16 | 32 | 2.9 | 5.8 |
| 8 | 6.221 | 8 | 24 / 16 | 48 / 32 | 3.9 / 2.6 | 7.7 / 5.1 |

(The J list is coarse -- 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64 -- so
these are upper bounds rounded up to the next listed J.)  The number of
levels needed for a fixed loss grows linearly with D_a: J(eta) ~ 1.2 D_a / eta.

**Where the loss sits.**  The eigen-direction attaining lambda_min has
Fourier centroid xi ~ 35 (lambda 3), 42-68 (4), 86-126 (6), 92-220 (8)
and mass below xi = 20 of 0.00-0.14 (typically 0.01): the binding
direction is a packet at one of the deep troughs (35.5 at lambda 3; 39/81
at lambda 4; 86/117/164 at lambda 6; 177/291 at lambda 8), never the
ground.  The loss is the quantization gap at the deep troughs -- a packet of
width ~2 pi / L cannot sit inside a half-cell trough, so it averages the
gap beta_a - m over the trough and its neighbouring crests, and the
optimizer places levels to equalize this gap across the deep troughs, which
is why eta scales like (level spacing) ~ (D_a + cap)/J.

**Tail artefact.**  At lambda = 8 the tail charge (-8.05 T, ||T|| = 0.10)
separates the two columns from J = 8 on and floors eta at ~0.08 (the head
floor with tail charge is 0.078): eta(64) = 0.188 with tail vs 0.118
grid-only, J eta/D_a = 1.93 vs 1.21.  The grid-only column is the
head-resolved trend; the with-tail column is what a valid minorant costs
on this head.  At lambda <= 6 the two agree to <= 0.006.

## 6. Results: (D3) binary-coded sets -- J sets, 2^J levels, eta / D_a

| J sets (levels) | lambda=3 | 4 | 6 | 8 | 2^J eta / D_a (lambda 3) |
|--:|--:|--:|--:|--:|--:|
| 1 (2) | 0.613 | 0.585 | 0.570 | 0.579 | 1.23 |
| 2 (4) | 0.337 | 0.335 | 0.315 | 0.316 | 1.35 |
| 3 (8) | 0.185 | 0.177 | 0.171 | 0.171 | 1.48 |
| 4 (16) | 0.105 | 0.095 | 0.092 | 0.107 | 1.68 |
| 5 (32) | 0.060 | 0.058 | 0.056 | 0.071 | 1.92 |
| 6 (64) | 0.036 | 0.035 | 0.031 | 0.047 | 2.33 |
| 7 (128) | 0.026 | 0.024 | 0.021 | 0.036 | 3.34 |
| 8 (256) | 0.021 | 0.019 | 0.017 | 0.030 | 5.36 |

Four sets (16 uniform levels) already give eta ~ 0.1 D_a at every window,
matching (D1) at J = 12-16 levels; beyond 6 bits the uniform spacing stops
paying (the loss saturates near the (D1) J = 64 value and, at lambda = 8,
at the tail-charge floor).  So the SET count J in `eq:v131-step-minorant`
is not the relevant complexity: with binary weights, J sets carry 2^J
levels and J ~ log2(1.3 D_a / eta) sets suffice for a loss eta on this
head.  The level count (the sup-norm resolution at which m tracks beta_a
on the deep troughs) is what grows like D_a / eta.

## 7. Head artefacts, stated

1. Modes reach only xi < 2 pi N / L = 732, 580, 449, 387.  Lobes at or
   beyond that (lambda 4: 526, 652, 789; lambda 6: 566, 681; lambda 8: 635,
   752; and the whole tail with D_tail = 8.05 at lambda 8) are seen only
   through the edge of the head or through T.  D_a on the head is the depth
   of the deepest lobe the head resolves; the true D_a is larger (unbounded
   in a by `cor:v137-scalar-no-go`), so at fixed J the true loss of the
   same construction is larger than tabulated.  The D_a-fraction tables are
   the head-resolved statement.
2. The tail charge -D_tail T is a valid but crude treatment of |xi| > 800
   (worst value on [800, 40000]; the negative set continues beyond the scan
   at lambda >= 4).  It sets the resolution floor 5e-5, 2e-3, 7e-3, 0.08
   at lambda = 3, 4, 6, 8; etas below it are not resolved.  Both columns
   are given everywhere.
3. Float quadrature and midpoint eigenvalues throughout; the grid-only
   head floor is 2e-5 (lambda 3) and 6e-4 (lambda 4), so the small-eta
   end of the (D1)/(D3) tables at lambda <= 4 is good to ~1e-3 only.
4. (D1) levels are optimized greedily with coordinate refinement on a 240-
   edge grid: eta(J) is an upper bound on the best J-level loss, and the
   J >= 24 entries are greedy continuations.  The J-scaling could be
   somewhat better than 1.2 D_a / J with a global optimizer, but not below
   the uniform-quantization floor set by the gap at the deep troughs.
5. Only the even head; the source-compressed C_{a,u} is replaced by the
   full-head concentration matrix (an upper bound for the complement, as in
   `layercake.py`).

## 8. Verdict

On the even head (N = 256, xi < 800) at lambda = 3, 4, 6, 8, every
bounded-complexity step minorant loses a fixed fraction of D_a: one level
set 0.57-0.60 D_a (best at t = 0.2 D_a), the layer-cake 0.35 D_a (of which
0.30-0.34 D_a is the exact cost of dropping beta_a^+), the J deepest
troughs 0.74-0.85 D_a at J = 16 and still 0.44-0.52 D_a with every lobe
used, and a cell-blind lattice comb ~1.0 D_a.  The comb-following family
that works is the J-level quantization of beta_a (level sets = unions of
crest cores, positive levels included): its loss is lambda-independent as
a fraction of D_a, eta_a(J) ~ (1.0-1.35) D_a / J, so a bounded eta_a
requires the number of LEVELS to grow linearly with D_a -- J(eta) ~ 1.2
D_a / eta on these windows (6, 8, 16, 16-24 levels for eta <= 0.5 at
lambda = 3, 4, 6, 8) -- and since D_a -> infinity the level count is
unbounded in a.  The number of SETS in `eq:v131-step-minorant` is not the
right measure: binary weights let J sets carry 2^J levels, so
J ~ log2(1.3 D_a/eta) sets suffice, but only because the minorant then
tracks beta_a to within ~eta on the deep troughs, i.e. the criterion
reproduces q_a itself rather than closing anything.  The binding direction
is never the ground but a packet at a deep trough at cell index 12-500, so
the obstruction is the density of near-D_a troughs at moderate frequency,
not the low-cell train.  All of this is head-resolved and float; the true
D_a is larger than the grid value at lambda >= 4 and the tail charge
floors eta at 0.08 at lambda = 8.  Nothing here is a bound, and nothing
here bears on G2 or RH.
