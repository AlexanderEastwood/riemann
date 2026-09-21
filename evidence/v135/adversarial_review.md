# Adversarial final review of the v1.35 proposed section

Reviewed `/workspace/scratch/c86bf52508ed/research_v135/new_section.tex` against the relevant identities and domains in the recovered v1.34 manuscript. No manuscript file was modified. This is an internal mathematical review, not an external referee report or a numerical certificate.

**Disposition: pass.** I found no blocking mathematical error, missing scale factor, or overstatement of the sign conclusion in this draft. The growing-rank operator-residual result is stronger than the previously recorded fixed-dimensional radical construction. It remains a continuation of that construction and does not prove the missing arithmetic lower bound.

## Full-parity symbol and concentration statement

The pole kernel is exactly `2 cosh((x-y)/2)`, including the negative odd rank-one term. Its difference from `exp(|x-y|/2)` is `exp(-|x-y|/2)`. Thus the beta-symbol identity extends from even functions to all complex functions in the unchanged logarithmic form domain. The bounded prime, pole, and continuum differences at each fixed window justify the form-core extension.

For symmetric frequency sets, reflection commutes with every concentration operator. Projection off the actual even source is the identity on the odd sector. The two parity trace densities, their sum `a/pi`, and subtraction of the source only from the even trace have the correct factors of two. Applying the gap-free theorem only to the even block gives precisely the displayed maximum of the odd error and the even error plus `2 epsilon/sqrt(3)`. As in the referenced criterion, these errors are nonnegative ordinary-norm lower-bound errors.

## Explicit spacing and uniform Gram estimate

Here `M2 = ||(1+|x|)^2 phi||_2` is an L2 norm, not a squared norm. Since `||phi||_2=1`, splitting the correlation integral into the two tails gives

`|<phi(.-s),phi>| <= 2 M2/(1+|s|/2)^2`.

There are two lattice directions, so the row sum is bounded by

`4 M2 sum_(n>=1)(1+nD/2)^(-2) <= 8 pi^2 M2/(3 D^2)`.

The definition `D=ceil(4 pi sqrt(M2))` therefore gives a row sum at most `1/6`, and every finite uncut Gram is at least `5I/6`. This normalization and the ceiling are correct.

The cutoff Gram loss is positive semidefinite because `0<=chi<=1`. Its trace uses `(1-chi^2)|phi_j|^2`, not `(1-chi)^2|phi_j|^2`. The draft correctly invokes the same estimate for the uncut tails, which controls this trace by `C m_a delta_a^2`. Since `m_a=O(a)`, eventual loss below `1/3` gives the claimed lower Gram bound `I/2`.

## Radicality, Gaussian tails, and the exponential scale

The existing Schwartz radical theorem is polarized against arbitrary compact logarithmic tests; it is not restricted to even logarithmic tests. Translation corresponds to the displayed even Schwartz source `h_t(u)=exp(-t/2)h_infinity(exp(-t)u)`, and preserves both zero moments. Thus all translates are legitimate global radicals without a positivity or RH assumption.

The Gaussian series and reflection give the stated derivative bound for every fixed derivative order. Only finitely many derivative orders are used in this argument, so no growing-order uniformity is being assumed.

For centers `|jD|<=a/2` and exterior points `|x|>=a-1`, write `X=exp(2|x-jD|)`. Then `X>=lambda/e^2` and

`exp(2|x|)<=lambda X<=e^2 X^2`.

Absorbing the polynomial `X^2` into half of the Gaussian exponent proves the supremum estimate with exponent `pi lambda/(4e^2)`. Derivatives of the cutoff are uniformly bounded, and the remaining Gaussian envelope is integrable, giving the H1 bound as well. The scale is correctly `exp(-c lambda)`: the translated centers have distance only approximately `a/2` from the cutoff, while `lambda=exp(a)`. There is no accidental replacement of this scale by `exp(-c lambda^2)`.

## Complete operator residual and domain

Each column is smooth and supported strictly inside the physical interval, hence belongs to the canonical operator domain. Radicality gives the distributional residual identity on that interval. The draft then supplies an L2 representative by bounding all three geometric contributions.

The archimedean multiplier has at most linear absolute growth, so its L2 action is controlled by the H1 norm. The prime estimate keeps every integer `n>=2`, including those beyond `lambda^2`; its bound follows from `|x +/- log n|>=log n-|x|` and the convergent series `sum Lambda(n)n^(-5/2)`. The pole kernels are controlled by the same weighted tail supremum. Restriction to the interval produces the factor `sqrt(a) lambda^2`, which is correctly absorbed into the weaker final exponential because `pi/(4e^2)>1/100`.

Writing `U=G_a Gamma_a^(-1/2)`, the map U is an isometry, and `||W P_G||=||W U||`. The Hilbert-Schmidt bound on the column residuals costs exactly `sqrt(m_a)`, while the Gram inverse costs at most `sqrt(2)`. Consequently `sqrt(m_a a)=O(a)` gives the complete operator bound `C a exp(-lambda/100)`. This is an operator-norm estimate on the entire growing span, not just separate small Rayleigh quotients.

## Odd block, removed constraints, and spectral count

Reflection exchanges the two columns with indices j and -j. Antisymmetric coefficient vectors embed isometrically into the full coefficient space, so the odd block has the asserted lower Gram bound and exactly `J_a` independent columns. The constant C can be fixed once to cover both displayed estimates.

For any removed subspace of dimension less than `m_a`, elementary dimension counting leaves a nonzero vector in its orthogonal complement inside the growing radical block. Normalizing it proves the residual and absolute Rayleigh bounds. Hence a positive coercivity constant there cannot exceed the residual scale. Since `m_a` is asymptotic to `a/D`, the conclusion for every `o(log lambda)` family of removed directions follows. A positive lower bound `c lambda^(-A)` with fixed `c>0` and finite A is incompatible with this ceiling for all sufficiently large lambda.

Every odd column is orthogonal to every even image, regardless of the number of even constraints. Fewer than `J_a` independent odd constraints still leave an odd vector. These claims concern the indicated physical complements and do not identify them with the source complement or with a different weighted space.

If the spectral projection on `[-2 epsilon_a,2 epsilon_a]` had rank below `m_a`, dimension counting would produce a unit vector in the constructed span orthogonal to that projection. The spectral theorem would force its residual norm to be at least `2 epsilon_a`, contradicting the bound `epsilon_a`. The same argument applies on the odd block. Compact resolvent, already established in the manuscript, converts these projection ranks into eigenvalue counts with multiplicity. No assertion about which side of zero contains these eigenvalues follows or is made.

## Scope and novelty

The prior log already records fixed-dimensional even-derivative radical blocks and the obstruction to a fixed positive complement gap after fixed-rank removal. The new contribution here is the uniform lattice Gram bound, the explicit growing dimension proportional to `log lambda`, its full ordinary operator residual, and the resulting near-zero spectral count. The text identifies this relationship accurately. Constants C and a0 are existence constants depending on the fixed source and cutoff; the section does not claim a numerically certified finite starting window. No positive arithmetic estimate, RH implication without its stated remaining hypothesis, or transfer to a finite Fourier section is silently inferred.
