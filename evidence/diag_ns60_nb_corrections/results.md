Numerical illustration only; no certified sign or convergence claim.

NS-60 tests explicit old-space corrections to the adjacent-difference
family. Downsampling a new piecewise constant function by an integer d
places it in the old support interval; averaging on old integer cells
produces a valid old-space correction. All cross terms are retained.

The fixed Euler products Q=2,6,30 and tapered Mobius lengths R=4,16,64
are compared with the complete optimal projection and the actual residual
direction. These tests address the proposed correction, not a larger
table of approximation distances.

## Finite outcome and analytic disposition

The explicit corrections modestly reduce the raw operator norm in the
reported blocks, while their selected-direction energies are substantially
smaller than the worst-direction norm. For example at N=512 the scaled
raw norm N^2||D|| is about 8.24; Euler Q=30 gives about 7.58 and the
optimal projected norm about 7.17. The scaled selected-direction Rayleigh
values are about 2.55, 1.82 and 1.58 respectively. These are floating
illustrations only.

The analytic NS-60 argument is independent of these numbers. It retains
the averaging-grid defect and shows that for any fixed alpha<1, any
choice of squarefree Q_N<=N^alpha still cannot produce a uniform raw
corrected norm O(N^(-2)(log N)^B) for fixed B. This does not give a
lower bound for the optimal projected Gram, and does not exclude a
selected-direction estimate. Tapered non-Euler mollifiers are outside
that proved exclusion.

Small negative eigenvalues of a computed comparison difference at float
roundoff are not sign certificates: the exact difference is a positive
Gram square. Every comparison is made against the same old space.
