# NS-46 finite-arc Gram lemma — independent analytic review

Reviewed source: `evidence/ns46_radical_block/coordinator/finite_arc_gram.tex`.

Reviewed SHA256:
`ed8d0093fb1a21e8f81857b4c3f053762a9d22a2a50d38313aec2237df1e701b`.

## Ranked findings

- **MAJOR: none.**
- **MINOR: none.**
- **NOTE:** this is an analytic finite-dimensional Gram lower bound. It
  does not certify a numerical value of `r`, `c0`, or an effective window
  threshold, and it is not a lower bound on a Weil eigenvalue. Those
  limits are stated correctly in the reviewed source.

## Finite-polynomial and sampling argument

Under the unitary Fourier transform, a common translation contributes
only a unit-modulus factor. The other translation phases give
`P(exp(-i delta xi))` for the coefficient polynomial. After using the
lower bound on `|phi_hat|²` and changing variable, integration over the
symmetric interval changes the minus sign without changing the integral.
Thus the physical squared norm is at least `(c0/delta) I_P`, with no
additional `2 pi` factor. This holds for arbitrary complex coefficients;
no real-coefficient symmetry was used.

The `m` sampling bins have length `ell=theta0/m` and lie inside the arc.
For `j>k`, the minimum difference between points in their bins is

```
(2(j-k)-1) ell >= (j-k) ell.
```

The maximum difference is at most `2 theta0 <= pi`. Hence all selected
nodes are distinct, and the chord estimate

```
|exp(i theta_j)-exp(i theta_k)| >= (2 ell/pi) |j-k|
```

is valid. Continuity and averaging on each bin supply a node with
`|P| <= sqrt(I_P/ell)`. The nodes may depend on `P`; that causes no gap
because the interpolation estimate is uniform over every such node
choice. The proof does not claim one fixed sample set simultaneously
works by averaging for all polynomials.

For the kth Lagrange basis polynomial, the denominator is bounded below
by

```
(2 ell/pi)^(m-1) k! (m-1-k)!,
```

while every numerator factor on the unit circle has modulus at most two.
The identity

```
sum_(k=0)^(m-1) 1/[k! (m-1-k)!] = 2^(m-1)/(m-1)!
```

therefore gives exactly the displayed supremum factor
`(2 pi/ell)^(m-1)/(m-1)!`. Normalized circle Parseval is
`sum |c_j|² = (1/(2 pi)) integral |P|²`, and is bounded by the squared
supremum. Thus there is no missing or extra circle-normalization factor.
Finally `(m-1)! >= ((m-1)/e)^(m-1)` and `(m-1)/m >= 1/2` for `m>=2`
yield the claimed `4 pi e` denominator. Multiplication by `c0/delta`
leaves the prefactor `c0 r/m`.

This proves the lower bound for every complex coefficient vector and
hence the stated matrix inequality. It needs no infinite-lattice Gram
estimate or lower bound for a periodized transform.

## Identity of the actual source

The v1.35 definition is `k(x)=f_infty(exp(x))`, `phi=k/||k||_2`.
The v1.50 definition explicitly identifies its positive weight
`h(x)=f_infty(exp(x))`. Therefore these are the same underlying function,
with only the stated L² normalization distinguishing `phi` from `h`.
They are not being identified with the different repaired prolate source.

The v1.35 Gaussian tail makes `phi` integrable, and v1.50 establishes
strict positivity, evenness and nonzero mass. Therefore
`phi_hat(0)=(2 pi)^(-1/2) integral phi > 0`, and ordinary Fourier
continuity supplies fixed positive `r,c0`. This inference uses no
zero-distribution or RH hypothesis. It asserts existence, not a computed
interval enclosure for either constant.

## Growing-rank asymptotic

Writing `x_a=lambda²/(40000a)`, one has `x_a -> infinity`,
`J_a=floor(x_a)`, and

```
m_a = 2J_a+1 ~ lambda²/(20000a).
```

The weaker displayed upper bound `m_a <= lambda²/(10000a)` holds
eventually. The centers `j/J_a` are exactly in `[-1,1]`. Reindexing
them as `-1+k/J_a` gives the lemma's finite progression with a common
shift. Its hypothesis `0<r/J_a<=pi/2` holds for all sufficiently large
`a`.

Also

```
log(4 pi e J_a/r)
 <= 2a - log(a) + log(4 pi e/(40000r))
 <= 3a
```

eventually. Since the lemma's logarithmic exponent is
`2(m_a-1) log(4 pi e J_a/r)`, these conservative bounds give at most
`6 lambda²/10000`. Exponentiating with the correct inequality direction
proves

```
gamma_a >= (c0 r/m_a) exp(-6 lambda²/10000).
```

The conditioning cost is therefore retained explicitly, rather than
replaced by a uniform Gram constant. The separate cutoff-tail Gram loss,
complete operator residual, normalization by the inverse Gram, and parity
dimensions are outside this lemma review and remain obligations of the
separate NS-46 author proof.

## Review limits

No numerical computation or certificate was used or asserted. No author
file, manuscript, map, or task claim was edited. This review establishes
no complementary signed lower bound, G2 statement, or RH conclusion.
