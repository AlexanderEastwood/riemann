# NS-54 Selberg-to-QG assessment — independent analytic review

Classification: analytic review of exact identities and proved conditional
implications. No numerical run, arithmetic limit theorem, signed-floor
estimate, G2 or RH conclusion is supplied. Only this review file was written;
the frozen author files, manuscript, map and board were not edited.

## Pinned inputs

| File | SHA256 |
|---|---|
| `evidence/ns54_zero_picture/selberg/selberg_qg_assessment.tex` | `f9f4c43f07c768f32df09df7aa472149a1d4d1220ce6c3ea4dbc30ae99c87b3d` |
| `evidence/ns54_zero_picture/selberg/sources.md` | `422b6c1e6c33ce1c3b73416cb3eb40a283130026336a6f9b556279b8fb6356ac` |
| `evidence/v149/weighted_zero_input.tex` | `519624d6d0b2352098fffcf3c694d4f2213d91481e45aeb47581c3168c4f0e42` |
| `evidence/v147/level_distribution_zero_statement.tex` | `08318a91fb04cf2741f99a3464193f525b99107a7ea3b943bf187c50899dfa71` |
| `evidence/v146/beta_lattice_identity.tex` | `ac18164e177e1786692d40cf07ed911369fe30e6ddf4d147500365862ff7f459` |

Line references below are to the pinned assessment unless otherwise stated.

## Ranked findings

**MAJOR: none.**

**MINOR: none.**

**NOTE 1 — lines 180–225: the stronger normalized-cost conclusion stands.**
For the actual at-most-K downward quantizer, a full limiting probability
law with unbounded negative support forces `QC_K/b_a -> infinity`, not
merely a positive lower limit. The proof controls grids depending on `a`,
does not presume existence of an optimizer, and does not require first
moment convergence. No fix is needed; the justification is expanded below.

**NOTE 2 — lines 215–224: the ZLD conclusion is conditional and uses the
whole sampling family.** The contradiction applies to every fixed
`0 < theta <= 1` in the repository's ZLD definition. It is not confined
to theta=1, but it does require the full uncentered head law (or a centered
law with a finite normalized center). A law on a possibly vanishing
subinterval does not establish arithmetic ZLD failure. The text states
these restrictions correctly.

**NOTE 3 — lines 121–138 and 242–270: the arithmetic transfer remains
open.** The primary theorems are not being rejected because every zero
statistic CLT assumes RH: Maples–Rodgers is explicitly and correctly
unconditional. The fixed test, variance and scale mismatches, complete-field
error controls, prescribed observation interval and centering must still
be addressed. Growth of the unweighted cost also supplies no packet with
all-Borel domination and bounded energy. No fix is needed.

## Exact definition and stronger one-sided implication

The assessment retains exactly `eq:v149-qc`: a finite set of at most K
levels in `[-D_a,0]`, containing the global anchor `-D_a`; rounding is
downward. The measure is the pushforward of uniform `[0,X_a]` restricted
to negative values, with its original subprobability mass. It is not
renormalized by the negative fraction. The global depth remains valid
even if the observed head never attains it. The field is bounded below
by `-D_a` everywhere, so the anchored quantizer is always defined.

Write `Y_a=beta_a(U_a)/b_a`, `d_a=D_a/b_a`, and let the limiting probability
law have unbounded negative support. For any M, a bounded open interval
strictly below `-M` has positive limiting mass. Portmanteau gives positive
eventual mass there; therefore `d_a>M` eventually. This proves `d_a ->
infinity` without assuming convergence of extrema or a head minimum.

If the normalized quantization infima were bounded along a subsequence,
choose grids with normalized cost at most the normalized infimum plus 1.
This is possible because a finite-cost grid exists at each parameter;
no minimizer is required. Order each grid and pad by repeated levels to
K entries without changing its rounding map. The K-fold compactification
`[-infinity,0]^K` supplies a subsequence with coordinatewise limits. The
first coordinate is the global anchor and tends to minus infinity.

If any level has a finite limit, let ell be the smallest such limit and
choose a bounded negative open interval I whose closure lies strictly
below ell and whose limiting mass p is positive. If none has a finite
limit, choose any bounded negative open interval with positive mass.
All finite-limit levels eventually lie above I. The remaining levels
all tend to minus infinity, so their maximum tends to minus infinity.
Consequently the downward error tends uniformly to infinity on I.
Portmanteau ensures eventual I-mass at least p/2. Integrating on I alone
contradicts bounded normalized cost. All discarded costs are nonnegative.
This proves the stated limit for each fixed K even for atomic limiting
laws and without moment convergence.

Weak convergence of probability laws also gives tightness. For fixed
`0<r1<r2<=theta`, the event with values in `(-r2 D_a,-r1 D_a)` lies below
the moving normalized threshold `-r1 d_a -> -infinity`; its probability
therefore tends to zero. ZLD requires it to be at least the fixed positive
number `kappa (r2-r1)`. These cannot both hold on the same entire family.
The implication to unnormalized QG growth additionally uses `b_a ->
infinity`, as the statement explicitly requires.

## Gaussian transfer, centering and boundary cases

For a Gaussian target with finite center c, each specified negative band
`J_j=(-3j-1,-3j)` has mass at least `m_K>0`. A CDF error Delta changes
an interval probability by at most `2 Delta`. The actual field is
nonconstant real analytic, so its pushforward has no endpoint atoms;
this follows from the existing v1.47 level-set argument. Alternatively,
taking left limits in the CDF estimate gives the same open-interval
lower bound against a continuous target. Thus the lower band mass
`m_K/2` is justified when `Delta<=m_K/4`.

For any grid, the points with downward error less than `b_a` are contained
in at most K intervals `[level,level+b_a)`. A length-`b_a` interval cannot
meet two of the bands `b_a J_j`, whose pairwise distances are at least
`2b_a`. At least one of K+1 bands is missed. Its loss is at least `b_a`
everywhere; multiplication by its unconditioned mass proves
`QC_K >= b_a m_K/2`. Intersecting a band with actual support does not
reduce its probability or the separation estimate.

For the surrogate, put `X=(F_a-mu_a)/b_a` and `s=mu_a/b_a`. Outside the
exceptional event, `|Y_a-(X+s)|<=r_a`. Hence its CDF is sandwiched between
the CDFs of X at `z-s-r_a` and `z-s+r_a`, up to epsilon. The Gaussian
density bound gives exactly

```
Delta <= delta_a + epsilon_a
         + (r_a + |mu_a/b_a-c|)/sqrt(2*pi).
```

To apply the proposition that displayed expression must tend to zero,
consistent with the proposition's Delta hypothesis and final error-scope
paragraph. A centered CLT alone does not imply this centering condition.
The truncated-Gaussian countermodel at lines 228–234 has mean
`2n b_n`, minimum `n b_n>0`, and zero negative cost despite Gaussian
centered fluctuations. It is correctly identified as a measure-theoretic
example, not an arithmetic construction. Conditional negative laws must
restore their mass fraction before estimating this cost.

## Fixed-window calibration and exact terms

Differentiating the finite sine polynomial yields
`2 pi V_x'=-2 sum_(n<x) Lambda(n)/sqrt(n) cos(xi log n)`. Thus the sign
and extra logarithmic factor relative to the logarithmic polynomial are
correct, with both A and `2 I_x` retained. For fixed a the sum is finite,
and `I_x=O_a(1/T)` uniformly on `[T,2T]`. Distinct cosine frequencies
have cross averages `O_a(1/T)` and diagonal averages `1/2+O_a(1/T)`.
The leading second moment is therefore exactly
`2 sum_(n<x) Lambda(n)^2/n`; subtracting the squared mean changes the
remainder by only `O_a(1/T^2)`. Cross terms with `I_x` are `O_a(1/T)`.
The stated variance follows. Close frequencies may make the constants
large as a grows; no simultaneous-limit uniformity is asserted.

The digamma asymptotic gives `A(xi)=log(xi/(2 pi))+o(1)`, while the finite
prime sum is bounded. Therefore `beta_a(xi)=log xi+O_a(1)` at fixed a.
This supplies no cofinal variance law. The RH-conditional sinc formula,
finite-interval Stieltjes integration by parts with boundary terms, and
the distinction between the small endpoint/trivial correction and an
uncontrolled finite-height Perron remainder agree with v1.46/v1.47.

## Primary-source restrictions independently checked

- [Radziwill–Soundararajan, Theorem 1](https://arxiv.org/pdf/1509.06827),
  printed p.1, concerns the real logarithm at uniform height `[T,2T]`,
  normalized by `sqrt((1/2) log log T)`. It supplies no derivative-law
  transfer to the present field.
- [Bourgade, Theorem 1.1](https://arxiv.org/pdf/0902.1757v1), printed p.2,
  concerns a fixed finite set of shifted logarithms with separation
  limits. The normalization changes with distance from the line. This
  does not justify a growing differential or convolution operator.
- [Maples–Rodgers, Theorem 1.2](https://arxiv.org/pdf/1404.3080v2), printed
  pp.1–2, is unconditional and counts the ordinates of all zeros with
  multiplicity. It requires a fixed real compactly supported BV test,
  `n(T)->infinity`, `n(T)=o(log T)`, and divergent Fourier variance.
  Sinc has noncompact support and infinite total variation: its derivative
  has a leading `cos(u)/u` term. Its Fourier transform is a bounded
  interval indicator, giving finite half-derivative Fourier energy.
  These are actual mismatches with the stated theorem. Matching the
  argument scale requires `n(T)=log T/(2 pi L)`; when `log T` is comparable
  to L, this does not diverge. Unconditionality is not the obstruction.
- [Bourgade–Kuan, Theorem 1 and conditions (3)–(5)](https://arxiv.org/pdf/1203.5328),
  printed p.3, assume RH and mesoscopic scaling. The specified decay of
  the test and its first two derivatives excludes bare sinc. This does
  not establish that every extension or smoothed variant is unavailable.

The paper statements and the assessment's source notes agree within the
reviewed scope. A dyadic-height interval occupies fraction `T/X_a` of
the prescribed full head, so its band mass must carry that factor. An
arbitrary new head rule or a finite-zero error that is merely named
cannot supply the missing arithmetic transfer.

## Verdict

The frozen conditional propositions and fixed-window calibration stand.
No actionable correction is required. The arithmetic full-head law,
centering and complete-field approximation remain open; a separate
admissible weighted packet is still needed for full QG. No arithmetic ZLD
failure or closure of a positivity route follows from the cited CLTs
alone. No manuscript build was requested or performed in this review.
