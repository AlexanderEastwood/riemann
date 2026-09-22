# NS-43 CCM selection note — independent bounded mathematical review

Review scope: the final versioned
`evidence/ns43_route_selection/ccm/selection_note-v2.tex`, compared with
the preserved original `selection_note.tex`.
No numerical computation, certificate, or verification of an arithmetic
cofinal selection hypothesis was requested or performed.

## Ranked findings

- **MAJOR: none.** The selection estimates and abstract countermodels do
  not establish their missing cofinal arithmetic hypotheses, and the note
  expressly distinguishes that scope.
- **MINOR M1, resolved in v2:** the opening notation uses
  the even-sector operator, while the coarse-profile proposition (S5)
  uses the full space `L²(R)` and the dense span of all translated
  radicals. The final v2 now explicitly resets this subsection to the full
  both-parity Weil form and full zero-extension space. Its final assertion
  defines the complete ground as the minimum of the even and odd ground
  energies and scopes the equivalence to both parities. This was a
  notation/domain scope issue, not a failure of the density proof once
  its form is correctly specified. No outstanding MAJOR, MINOR, or
  actionable NOTE remains in this bounded mathematical review.

## Checks and mathematical conclusions

**Fixed cutoff and actual near-radical.** The specified single smooth
profile is constant near the origin after composition with `|x|-a`,
has support at distance at least one half from the physical boundary,
and has uniformly bounded derivatives. Thus the v1.35 residual proof
applies to this exact cutoff, and normalization changes only its fixed
constant eventually. This repairs the invalid possibility of asserting
the same rate for arbitrary cutoffs with growing derivatives. It is
correctly distinguished from the repaired prolate source. Its weighted
L¹ convergence follows from the stated double-exponential tail.

**Rayleigh-excess selection.** Decomposition against the complete ground
spectral projection preserves the form domain. The mixed term vanishes
because the selected vector is an eigenvector, rather than because two
unrelated blocks have separate sign estimates. The bound
`||p-v||² <= 2 E/g` is correct. The stated `C_R(a)` equals the exact
Cauchy–Schwarz factor for the exponential evaluator on `(-a,a)`.
Consequently (S1) is a sufficient quantitative topology upgrade; mere
ordinary L² convergence is not used as entire-transform convergence.

**Residual and evaluator versions.** A complete lower bound for the
second eigenvalue strictly above the trial energy forces a unique simple
ground below that threshold. Spectral expansion proves the residual
angle estimate with denominator `beta-alpha`. The complement evaluator
estimate (S3), including its shift by the actual ground eigenvalue, gives
the displayed transform bound. Both variants still require their stated
complete-space and cofinal inputs. No finite matrix gap is substituted.

**Complete source-complement condition.** In (S4), projection along an
operator-domain source preserves the form domain and the restricted
form is closed. Min–max proves the complete second-eigenvalue lower
bound. The proof explicitly retains `2 Re(t <Ap,y>)`; completing the
square gives the stated `alpha-||r||²/delta` lower edge. The compressed
resolvent argument and phase alignment give the stated angle bound.

Even without the relative selection rate, (S4) plus a vanishing complete
source residual gives the simpler sector floor

```
q[f] >= (alpha - ||r||) ||f||²,
```

by `2 |t| ||y|| <= |t|² + ||y||²`. Thus the prose floor implication is
valid even if the Schur bound `||r||²/delta` is large. Relative smallness
of `r/delta` is an additional requirement for selecting the source,
not for this elementary sector floor. A full floor still requires the
odd obligation if (S4) was imposed only in the even sector.

**Actual near-radical separator ceiling.** The even reflected v1.35
block has eventual dimension greater than one, so it contains a unit
vector perpendicular to the named cutoff source. Its complete residual
is bounded by the block estimate. Testing (S4) on this vector gives
`delta <= epsilon-alpha <= epsilon+|alpha| = O(epsilon)`.
That excludes a fixed positive or polynomial lower scale for this
particular source-relative separator. It does not exclude a much finer
hierarchy in which the actual source error is smaller still. The note
does not assert that such a hierarchy has been proved.

**Identification and conditional zero transfer.** The coefficient
`2/(sqrt(6 pi) ||h||)` follows from the archived Mellin identity and
the unitary Fourier normalization. Positivity of the explicit kernel
makes its transform at zero nonzero. Uniform convergence after division
by the value at zero fixes phase and scale. Conditional on the complete
real-zero theorem applying cofinally as well, the disk/argument-principle
argument is valid. The single certified fixed window does not supply
that cofinal hypothesis.

**Abstract nonselection.** The fourth convolution of the indicated
interval indicator is nonnegative, even, compactly supported and in
H². Dilation preserves unit norm and produces the stated distinct
sinc-power transforms, whose zeros are all real. The Householder vector
lies in the Dirichlet operator domain. Its unitary involution preserves
that domain and parity and maps the Laplacian ground to the chosen
compact spline. The eigenvalues, simple even ground, global spectral
gap, residual estimates, and strong-resolvent collapse follow as stated.
Uniformly bounded support gives weighted tightness. Positive scalar
rescaling can make the absolute residual arbitrarily fast without
altering the alternating ground profiles.

This model has no support-consistent arithmetic Weil form, no claimed
prime identity or CvS representation, and no positivity-improving
semigroup. Its ground is nonnegative, not positive throughout every
increasing interval. Those exclusions are material and explicitly
stated. The construction therefore refutes only selection inferred
from the listed abstract premises, not arithmetic CCM selection.

**Topology and coarse profile.** The small positive far-end bump has
vanishing L² norm but an exponentially increasing evaluator at `iR`,
as claimed. It is correctly separated from the real-zero countermodel.
For (S5), once the full-parity form scope is specified, each fixed
translated-radical combination supplies a strongly convergent cutoff
sequence with rescaled energy tending to zero. Nonnegativity and lower
semicontinuity then extend the zero value from the dense span to all
of H. This only closes the explicitly coarse scale and liminf proposal;
it does not preclude finer profiles or stronger arithmetic selection.

## Final pinned state

Final reviewed file:
`evidence/ns43_route_selection/ccm/selection_note-v2.tex`, SHA256
`3c4135cdea011f07184a68afd54c45e389cb53f982ebb11cd33b0de08ebd9286`.

I inspected the complete original and the full subsequent diff. The v2
diff contains the explicit both-parity scope reset, the qualified final
ground-energy statement, and the valid elementary S4 floor calculation.
All requested corrections are resolved. The preserved original has SHA256
`003c493a4a8a674456875c1a5d31d1c841a1163042554f70589e770884840ede`.
The parent owns manuscript integration and build verification; this review
does not assert that an integrated manuscript was built.
