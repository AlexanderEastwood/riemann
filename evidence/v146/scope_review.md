# v1.46 scope and algebra review

- **Exact identity:** s=1/2-i xi gives n^(-s)=n^(-1/2)exp(i xi log n).
  Perron's half endpoint minus the strict sum contributes +Lambda(x)/sqrt(x)
  cos(xi L) in beta. The pole, zero, s and trivial residues have signs
  +,-,-,+. The finite remainder is retained with sign -2 Re R in beta.
- **No RH:** functional equation gives the real log-derivative cancellation
  on the critical line regardless of zeros off the line. Every nontrivial
  zero remains in the analytic sum. Replacing x^(Re rho-1/2) by 1 for all
  zeros, or replacing all zeros by real ordinates, would use RH. The finite
  computed zero lists are checked against N(T); unseen zeros are not
  assumed to lie on the line.
- **Real limits:** at a critical-line zero the combined real expression has
  a continuous limit. The separate complex denominator/envelopes may have
  poles; the statement does not assign them independent finite values.
- **Summation:** sharp sums use symmetric height/Perron (or Cesaro) limits.
  Numerical samples use a different, explicitly specified but exactly
  desmoothed Gaussian Perron representation. Gaussian trivial residues
  stop at the fixed left contour; summing them to infinity would diverge.
- **Numerical scope:** forty low samples plus ten archived grid troughs and
  four centroids. No optimization, new head or window. The old three-decimal
  file only supports rounding checks. Sufficient finite-prefix counts are
  empirical, with two precisions and cutoff stability; no interval tail
  certificate is asserted. Centroids need not be negative symbol points.
- **Packet signs:** eta is max(0,-inf T_m). A trough gives eta >=
  (b+B)c-B, not bc when positive levels are retained. A quantization gap
  gives eta >= c*delta-q[g], not c*delta alone. These follow directly from
  quadratic forms, with all positive spill and source cross terms retained.
- **Width:** lattice spacing pi/a; full-cell half-width pi/(2a), half-cell
  half-width pi/(4a). Mirrored-band even trace at half-cell width is <.509
  when a*omega>=10*pi. The 0.6-0.8 whole-negative-set diagnostic is not a
  single-half-cell estimate.
- **Projection:** norm on E of F(Pf) is at least sqrt(c0)-|<f,u>|;
  normalize by sqrt(1-r^2). The energy projection includes the source
  cross term (2r+r^2)||Wu||. A packet is never assumed source-orthogonal.
- **Level counting:** partition [-D,0] by the at most K distinct values,
  append 0, and integrate triangular gaps. Sum Delta_j^2 >= D^2/K. This
  lower-bounds eta only with the displayed arithmetic pushforward mass
  lower bound and a bounded original packet energy. Arbitrary J sets may
  have 2^J levels.
- **Cofinal gap:** v1.37 proves D_a->infinity unconditionally, not widths,
  number of near-deepest components, the needed level distribution or the
  packet-energy upper bound. Its RH probe is not a physical squared Fourier
  transform. No cofinal hypothesis is inferred from four windows.
- **Countermodel:** for c=||C_E||<1, B=dc/(1-c) and m=B-(B+d)1_E,
  T_m>=0 although depth is d and m has two values. This refutes an inference
  from depth/concentration alone, not the desired assertion for the actual
  arithmetic symbol. Hence the latter route remains blocked, not closed.
- **Odd sector:** use the established common symbol and normalized sine
  packet. The even source causes no odd rank-one loss. The same arithmetic
  gap remains.

No G2/RH claim, no positivity transfer, and no refinement of v1.43.
