NUMERICAL ILLUSTRATION ONLY — not a certificate, window computation, or Weil-tail estimate.

# NS-26: exact symbol identity and the finite zero-sum comparison

The exact proposition and proof are `prop:v146-beta-explicit` and
`eq:v146-lattice` in the manuscript; their incremental source is
`evidence/v146/beta_lattice_identity.tex`. RH and G2 remain open.

## What had to change

1. The archived cutoffs x = lambda² are 9, 16, 36, 64, all integers.
   The defining sum is strict. Perron inversion supplies a half-weight
   at a prime-power endpoint, which must be removed. In beta the resulting
   term is +Lambda(x)/sqrt(x) cos(xi log x). It vanishes at 36, but not
   at 9, 16, or 64. The separate noninteger identity has zero endpoint term.
2. The diagnostic's equal crests and exact quarter-point zeros are not
   exact properties. The identity has a frequency-dependent cosine
   envelope and an additional sine envelope. The table already shows this.
3. `selfsim_output.txt` has only three decimal places. A literal 1e-6
   comparison to its rounded numbers is impossible. We reproduced all
   forty underlying sample locations with the unchanged `make_beta_true`
   and compared an independently assembled zero-side formula; all saved
   three-decimal roundings also agree. No ground or head was recomputed.
4. `4 sum sin(gamma L)/gamma` is a zero-frequency amplitude contribution,
   not a crest-minus-trough. Applying it to every zero would use RH.
   We use only a finite located zero list in the illustration, count all
   zeros up to 680, and retain the omitted sum in the exact identity.

## Exact formula used for the numerical illustration

Set s=1/2-i xi and K_e(w)=exp(Lw+e²w²/2)/w. Gaussian Perron inversion gives

    S_e(s) = sum_n Lambda(n)n^(-s) Phi(log(x/n)/e)
           = x^(1-s) exp(e²(1-s)²/2)/(1-s) - zeta'/zeta(s)
             - sum_rho K_e(rho-s) - sum_{n=1}^9 K_e(-2n-s) + I_e(s),

where Phi is the standard normal distribution function and

    I_e(s) = (1/(2 pi i)) integral_{Re w=-20}
             [-zeta'/zeta(s+w)] K_e(w) dw.

Only the first nine trivial zeros lie between this line and the initial
right line. Do NOT sum Gaussian-weighted trivial residues to infinity:
that would diverge along the negative real axis. The left contour stays
in the identity. The nontrivial-zero sum converges absolutely and includes
zeros anywhere in the critical strip, without RH.

Define the exact desmoothing correction

    D_e(s) = sum_n Lambda(n)n^(-s)
             [1_{n<x} - Phi(log(x/n)/e)].

This correction returns to the original sharp cutoff, not a new window.
At n=x its coefficient is -1/2. The functional equation and digamma
recurrence cancel the complete archimedean/log-derivative/lower-limit block.
Consequently the exact identity is

    beta = 2 Re sum_rho K_e(rho-s)
         + 2 Re sum_{n=1}^9 K_e(-2n-s)
         - 2 Re [x^(1-s) expm1(e²(1-s)²/2)/(1-s)]
         - 2 Re D_e(s) - 2 Re I_e(s).

The script evaluates the endpoint part of -2 Re D_e separately. This is
not a residual defined by subtracting the answer: every term is assembled
from zeros, trivial residues, the pole, and a convergent Gaussian Perron
correction. The original finite prime formula is used only for comparison.

The left contour is tiny on these inputs. For |xi|<=12, the functional
equation on z=-19.5+i(t-xi), the digamma series at 20.5, and the absolutely
convergent log-derivative series at Re(1-z)=20.5 give

    |zeta'/zeta(z)| <= 8 + 0.1 |t|.

For example |cot(pi z/2)|=1 on this line, psi(20.5)<log(20.5), and
|psi(20.5+iy)-psi(20.5)| <= |y| (1/20.5+1/20.5²).
It follows directly that

    2 |I_e| <= x^(-20) exp(200e²)/(20 pi)
               [8 sqrt(2 pi)/e + 0.2/e²] < 4e-18

for x>=9 and .025<=e<=.03. The script omits this bounded contour term.
It evaluates 400 positive zeros and their conjugates; Arb's finite zero
count N(680)=400 agrees with this list at both input precisions. No
assumption about the real parts of higher zeros is made. Gaussian damping
and the unconditional O(T log T) zero count ensure convergence; this run
is a floating-point illustration, not an interval certificate for its
omitted zero tail. The prime correction is summed through 256; the tail
is dominated by the Gaussian in log(n/64), using Lambda(n)<=log n.
The exact infinite tails remain part of the formula. Neither omitted tail
is replaced by an asserted RH estimate.

## Replay and observed agreement

From the repository root:

    .venv/bin/python evidence/diag_beta_lattice_identity/verify_identity.py

Environment: python-flint 0.9.0 and mpmath 1.4.1. The original beta function
and its prime-power assembly are imported unchanged. The zero-side prime
powers are generated independently. `check_b192.json` uses 192-bit zero
inputs, 45 decimal digits, epsilon=.025; `check_b256.json` uses 256-bit
zero inputs, 65 decimal digits, epsilon=.03. All results here are numerical
illustrations. The maximum observed absolute discrepancies are respectively
3.073e-21 and 3.257e-21, below 1e-6. Each JSON records every component,
the source hash, the saved rounding and the error from the legacy floating
sample abscissa. Pyright: 0 errors, 0 warnings.

The full zero contribution quoted below is reconstructed through the
Gaussian formula with exact desmoothing, rather than identified with a
400-zero raw or Cesaro sum. The residual in a truncated *sharp* zero sum
is then its difference from the reconstructed value; no bound on that
sharp-sum residual is claimed.

| lambda | 0.25 | 0.5 | 0.75 | 1 | 1.25 | 1.5 | 2 | 2.5 | 3 | 4 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | -0.001049620 | -0.285170440 | +0.004813623 | +0.283528080 | -0.011627613 | -0.279198149 | +0.271550179 | -0.259112589 | +0.238487065 | +0.119430410 |
| 4 | -0.000136061 | -0.686696623 | +0.000587379 | +0.694629609 | -0.001325758 | -0.708227383 | +0.728494661 | -0.757157288 | +0.797086684 | +0.935066074 |
| 6 | -0.009625892 | -0.509465665 | +0.029106199 | +0.511568482 | -0.049274218 | -0.515132406 | +0.520278251 | -0.527201212 | +0.536192519 | +0.562320938 |
| 8 | +0.000335780 | -0.130577913 | -0.001066304 | +0.131917033 | +0.001979857 | -0.134212830 | +0.137571506 | -0.142157995 | +0.148213318 | +0.166265590 |

## Which terms explain the naive mismatch

At lambda=3, C_x(0)=0.285219144687, decomposed as

    full zero amplitude       -0.077669995516
    trivial-zero amplitude    -0.003314956020
    strict endpoint           +0.366204096223

The 400-zero index-Cesaro candidate is -0.077720711653; height-Cesaro
(weight 1-gamma/680) gives -0.076414263832. Neither is a crest-minus-trough.
For the actual difference at u=1 minus u=1/2:

    full shifted zero term    -0.159765789563
    trivial-zero term         -0.003943883015
    strict endpoint           +0.732408192445
    TOTAL                     +0.568698519867

The height-Cesaro shifted zero term is -0.157163432709, with remaining
correction -0.002602356854. The raw 400-zero term is -0.164351811782,
with remaining correction +0.004586022219. The full shifted zero difference
is also not exactly twice its zero-frequency amplitude: the denominator
shifts contribute a further -0.004425798532 relative to that approximation.
Thus the sign reversal is mainly the endpoint term and the amplitude/difference
normalization, not a hidden archimedean constant (that block cancels exactly).

The exact amplitude at zero is the weighted arithmetic expression

    psi(5/4)-log(pi) - 2 sum_{n<x} Lambda(n)/sqrt(n) + 4(sqrt(x)-1).

Its four values are 0.285219144687, 0.684047784634, 0.508768457193,
0.130137500274. The archimedean constant is -1.372183419226, not the
-2.11 printed in the original diagnostic prose.

## Finding and scope

This is the classical explicit formula with the actual weighting, phase,
cutoff convention and remainder restored. It does not add a new arithmetic
lens, uniform positivity estimate, or energy budget determined by one scalar.
The energy still uses the full Fourier distribution of the state. The
failure here is of the constant-amplitude and truncated-zero surrogates,
not of the symbol or the concentration criterion. No new window, head,
Weil-tail metric or complete-ground enclosure was computed. G2 and RH remain open.

## Deep-trough follow-up and the summation convention (2026-09-21)

The analytic sharp zero sum is ordered by symmetric height |Im rho|<=T,
counting multiplicities and both conjugates. Its Perron limit (equivalently
its Cesaro limit here) is used; a finite prefix retains R_{x,T}. This is
not an absolutely convergent sum, and 400 zeros with or without Cesaro
weights do not give 1e-6 at the deep samples.

For a reproducible finite numerical evaluation we instead use the exact
Gaussian Perron identity above, epsilon=.025, including the pole,
trivial residues and exact desmoothing to the same strict cutoff. The
finite sum is ordered in increasing positive ordinate and includes each
conjugate. This convention has an absolutely convergent full zero sum.
The desmoothing correction is evaluated, not discarded. The number of
zeros below is specific to this convention and these sample frequencies;
it is not a required or sufficient count for an unsmoothed sharp sum.

Replay:

    .venv/bin/python evidence/diag_beta_lattice_identity/verify_deep.py

The script reads the top five archived grid troughs at each of lambda=4,8,
and the J=8 and J=16 binding centroids, directly from the NS-22 JSON. It
does not refine trough positions, rerun a head, or introduce a window.
It also repeats all forty low lattice samples. Both precisions use the
same epsilon: 192-bit zero inputs/45 decimal digits, and 256-bit/65 digits.
A reference prefix of 1200 positive zeros is checked against 1000; the
finite zero count at a separating height about 1648.69457 is 1200 at both
precisions. Counts below use the first prefix whose sum of absolute
omitted real paired contributions through 1200 is below 2e-7. Each
selected prefix is then compared to the recomputed original symbol and
passes 1e-6 at both precisions. This is an empirical sufficient count,
not a claim of a minimal count or an interval certificate on the infinite
tail. The 1000-to-1200 difference is below 1e-64 in the higher-precision run.

| lambda | sample group | locations | sufficient positive zeros (and conjugates) |
|---:|:---|---:|---:|
| 3 | low_lattice | 10 | 83 |
| 4 | low_lattice | 10 | 83 |
| 4 | deep_and_centroids | 7 | 530 |
| 6 | low_lattice | 10 | 80 |
| 8 | low_lattice | 10 | 80 |
| 8 | deep_and_centroids | 7 | 609 |

The following error is at the listed point-specific sufficient prefix,
against the recomputed original beta. The common window counts above
are the maxima of these sufficient prefixes. The reference-prefix
residuals at the deep points are below 6e-27 (lambda=4) and 4e-43 (lambda=8)
at both precisions. Archived grid depths agree to within 7e-13; unlike
the three-decimal low-sample text file, the NS-22 JSON stores full float
values. A centroid is not a trough location; two of the centroids have
positive beta.

| lambda | kind | xi | cell u | beta | positive zeros | absolute residual |
|---:|:---|---:|---:|---:|---:|---:|
| 4 | trough | 526.500000000 | 232.329287 | -3.419437295 | 431 | 1.456e-07 |
| 4 | trough | 39.247000000 | 17.318571 | -3.365250756 | 99 | 6.955e-09 |
| 4 | trough | 222.840000000 | 98.332874 | -3.300770464 | 215 | 4.577e-08 |
| 4 | trough | 81.020000000 | 35.751793 | -3.206301313 | 124 | 7.267e-09 |
| 4 | trough | 652.130000000 | 287.766188 | -3.136706249 | 530 | 1.843e-08 |
| 4 | centroid J=8 | 64.554323267 | 28.485964 | +4.608588674 | 115 | 4.637e-08 |
| 4 | centroid J=16 | 46.512756391 | 20.524740 | -0.481323287 | 103 | 3.212e-09 |
| 8 | trough | 362.255000000 | 239.779048 | -6.220830020 | 311 | 9.610e-09 |
| 8 | trough | 290.745000000 | 192.446093 | -5.658707866 | 261 | 9.610e-08 |
| 8 | trough | 177.390000000 | 117.415647 | -5.543126380 | 182 | 4.066e-08 |
| 8 | trough | 634.630000000 | 420.065913 | -5.515281321 | 517 | 7.121e-09 |
| 8 | trough | 751.895000000 | 497.684414 | -5.513353521 | 609 | 6.415e-08 |
| 8 | centroid J=8 | 220.024046355 | 145.635413 | -2.259398834 | 214 | 6.358e-08 |
| 8 | centroid J=16 | 213.278014653 | 141.170168 | +7.424038966 | 207 | 2.495e-08 |

For the deep checks |xi|<=800 and x>=16, the previous left-contour estimate
holds with 8 replaced by 50. The functional-equation/digamma-series estimate
then gives 2|I_e|<1e-20 for .025<=epsilon<=.03. The main formula retains
that contour exactly; its omission in this numerical illustration is
well below 1e-6. The finite zero count establishes the finite region only;
no RH extrapolation is made to zeros beyond the reference prefix.

At lambda=8, xi=751.895 (cell 497.684), the sharp 400-zero sum with endpoint
and trivial terms still has error about 5.567. The corresponding error at
lambda=4, xi=652.130 is about 0.233. The 400-zero prefix cannot resolve
these samples by simply dropping the Perron remainder.

The identity therefore extends to the deep troughs, not just the low-cell
train. Their depths are values of the full weighted, phased zero sum plus
specified corrections. This translates a trough-density question into a
level-set question for that whole sum; it does not turn it into a theorem
about nearest-neighbour zero spacings. Contributions from other zeros,
cutoff phases, the shifted denominators, and (without RH) the factors
x^(Re rho-1/2) remain. A handful of matching trough values establishes no
cofinal trough count, width, or density. G2 and RH remain open.
