# Independent review of the NS57 first-zero passage

Reviewed base: `b55d13ef6975e14a1f5b3cffe82381a68d64d943`.
Owned scope: small-window positivity, fixed-domain realization, compactness,
lowest-eigenvalue continuity, first-zero attainment and support saturation.
Perturbation: `delta_2 = -log(2)/100`, all other `delta_n = 0`.

**Disposition: no blocking defect found in these steps.** Strong continuity
of the compressed shifts is sufficient here because bounded reference-form
energy gives compactness in ordinary `L²`. It is not being treated as
operator-norm continuity. The argument below reconstructs that passage and
retains both pole signs and the entire form domain.

**Wall check: Same open gap**, KERNEL-API. This validates the relevant part
of an existing altered-weight control. It supplies no injectivity theorem
for the original arithmetic operator, cofinal lower floor, G2 or RH result.

## Dependencies and scope

The following are the exact archived dependencies used:

- `thm:ns57-first-zero-controls` in `evidence/v156/proof.tex` is the claim
  under review. The separate negative-test existence input is accepted:
  the perturbed global form has a negative compact smooth test in each
  parity. The detection and cutoff construction are not re-audited here.
- `prop:v118-log-dirichlet`, `eq:v118-bounded-physical-part`, and
  `eq:v118-K-bound` in the manuscript identify the actual canonical form
  with the restricted logarithmic Laplacian plus its bounded physical
  remainder. This identity, rather than an alternative boundary extension,
  is retained. Its kernel, shift and pole terms are inspected below.
- `prop:v114-weil-core` identifies the canonical realization, form core
  and compact resolvent. The compactness and core facts actually needed
  below are also reconstructed directly for the logarithmic form domain;
  finite Fourier compressions are not substituted for that domain.
- `prop:ns55fc-dilation` in `evidence/v155/proof.tex` gives the exact complete
  Fourier/pole/prime form and its digamma derivative bound. The scaling
  and norm-continuity consequences are reconstructed below.
- `prop:ns55fc-geometry` gives the earlier support argument. The full and
  parity arguments are reconstructed separately below, with no endpoint
  trace assumption.

V1.36's independent-review history remains intact. This note does not
replay that proof, NS46's quantitative cutoff estimates, any numerical
certificate, or NS57's sensitivity-rate or bounded-floor conclusions.

## 1. The complete form on one fixed domain

Use `I_a = (-a,a)`, `E_a` for zero extension, and the unitary Fourier
convention `hat f(ξ) = (2π)^(-1/2) ∫ f(x) exp(-iξx) dx`. Let
`D_a u(x) = a^(-1/2) u(x/a)` map `L²(-1,1)` to `L²(I_a)`.
The complete formula is

    q_delta,a[f] = ∫ alpha(ξ) |hat(E_a f)(ξ)|² dξ
                   + 2|∫ f(x) cosh(x/2) dx|²
                   - 2|∫ f(x) sinh(x/2) dx|²
                   - 2 Σ_n (w_n + delta_n) Re R_f(log n),

where `alpha(ξ) = Re psi(1/4+iξ/2) - log π`,
`w_n = Lambda(n)/sqrt(n)`, and `R_f(s) = <T_s E_a f,E_a f>`.
The sum is finite on any fixed support: correlations vanish for
`|s| >= 2a`, including equality. Both pole signs are essential.

The pullback domain is exactly

    V = {u in L²(-1,1): t[u] := ∫ log(2+|ξ|) |hat(E_1 u)(ξ)|² dξ < ∞}.

Indeed `hat(D_a u)(ξ) = sqrt(a) hat(E_1 u)(aξ)`, and
`log(2+|ξ|/a)` differs from `log(2+|ξ|)` by a bounded function for each
positive `a`, locally uniformly in `a`. The bounded prime and pole terms
do not change this domain. It is not `H¹_0`, and no boundary trace is
imposed by declaring the domain.

The form `t` is closed and positive. Its domain embeds compactly into
`L²(-1,1)`: a bounded `t`-ball has Fourier tail squared norm at most
`t[u]/log(2+R)` outside `[-R,R]`. Restricting the Fourier transform of a
function supported in `[-1,1]` to `[-R,R]` is a Hilbert–Schmidt operator,
because its kernel has finite square integral on this rectangle. Thus the
embedding is a uniform norm limit of compact maps. This proves the needed
compactness without substituting a stronger Sobolev norm.

For completeness, `C_c^∞(-1,1)` is a form core of this realization.
First shrink a zero-extended `u` by dilation with ratio `r<1`, then mollify
with radius less than `1-r`. Dilation tends strongly to the identity in
the logarithmically weighted Fourier norm: its norms are uniformly bounded
near `r=1`, and the assertion follows first on Schwartz functions and then
by density in that weighted space. Mollification converges by dominated
convergence in the same norm. These approximants lie in the open interval;
even mollifiers preserve parity. This argument imposes no unproved trace
or `H¹` condition on the original vector.

The digamma asymptotic makes `alpha(ξ)-log(2+|ξ|)` bounded. The precise
external fact used is `psi(z)=log z+O(1/|z|)` in a closed sector away from
the negative real axis; the line `z=1/4+iξ/2` lies in such a sector.
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2).
Consequently the rescaled complete form is

    q_delta,a[D_a u] = t[u] + <K(a)u,u>

with `K(a)` bounded and self-adjoint. It has compact resolvent and an
attained lowest eigenvalue, by closedness, semiboundedness and the compact
embedding just proved. The same statements hold in each closed parity
subspace. These are the canonical forms because they agree on the actual
smooth core with the v1.18 physical decomposition.

## 2. Continuity through prime-entry points

Fix a compact parameter interval `0<a_-<=a<=a_+`. Use a single finite prime
list with `log n <= 2a_+`; do not differentiate a changing cutoff.
Write `S_s = P_1 T_s E_1` on `L²(-1,1)`. Then `||S_s||<=1`,
`S_s*=S_-s`, and

    ||(S_s-S_t)u|| <= ||(T_s-T_t)E_1u|| -> 0 as s -> t.

The prime terms are finite sums of `S_(log n/a)+S_(-log n/a)` with fixed
coefficients. At entry, `|log n/a|=2`, the compressed shift is zero
almost everywhere. Strong continuity still holds there, while its norm
need not tend to zero. No norm-continuity claim is needed.

The rescaled pole term is

    2a (|<u,c_a>|² - |<u,s_a>|²),
    c_a(y)=cosh(ay/2),  s_a(y)=sinh(ay/2).

Both `c_a` and `s_a` vary continuously in `L²(-1,1)`, so this signed
finite-rank operator is norm-continuous and locally bounded. The negative
odd pole is retained.

The principal multiplier difference is norm-continuous as well. The
digamma series used in NS55 gives, with `s_k=k+1/4` and `v=|ξ|/2`,

    ξ alpha'(ξ) = Σ_(k>=0) 2v²s_k / (s_k²+v²)²,  0 <= ξ alpha'(ξ) <= 5.

The bound follows by comparing the nonnegative unimodal function
`2v²s/(s²+v²)²` with its integral plus twice its supremum on `s>=1/4`;
these are at most `1` and `4`, respectively. Hence

    sup_ξ |alpha(ξ/a)-alpha(ξ/b)| <= 5|log(a/b)|.

Compressing this bounded multiplier does not increase its norm. In sum,
`K(a)` is strongly continuous and locally uniformly bounded on the fixed
Hilbert space, while the form domain and reference form `t` stay fixed.

Here is the missing compactness argument in full. If `a_j -> a`, let
`mu_j` be the bottom and choose normalized minimizing eigenvectors `u_j`.
A fixed unit trial in `V` bounds `mu_j` above; `t>=log(2)||.||²` and the
local bound on `||K(a_j)||` bound it below. Therefore `t[u_j]` is uniformly
bounded. Along a subsequence realizing the lower limit, compact embedding
gives `u_j -> u` in ordinary norm, with `||u||=1`; weak convergence in the
form Hilbert space and lower semicontinuity give
`t[u] <= liminf t[u_j]`. If `M` bounds the perturbation norms, then

    |<K(a_j)u_j,u_j>-<K(a)u,u>|
      <= 2M||u_j-u|| + ||(K(a_j)-K(a))u|| -> 0.

Thus `mu(a) <= q_delta,a[D_a u] <= liminf mu_j`. A fixed minimizing vector
at `a` gives `limsup mu_j <= mu(a)`. The bottom is continuous. The proof
is unchanged within either closed parity subspace. Strong continuity alone
would not control arbitrary moving unit vectors; the form-energy compactness
is exactly the additional property used here.

## 3. Small windows start strictly positive

This conclusion can be checked directly from v1.18, without invoking a
small-window eigenvalue computation or simplicity theorem. Write `l_a`
for the quadratic form of `(1/2)L_Delta^Dir`, the restricted logarithmic
Laplacian with full-line symbol `log|ξ|`. Its exact dilation formula is

    l_a[D_a u] = l_1[u] + log(1/a)||u||².

The negative low-frequency part on the reference interval is bounded:
`|hat(E_1u)(ξ)|² <= ||u||²/π`, and
`∫_(|ξ|<1) |log|ξ|| dξ = 2`. Consequently
`l_1[u] >= -(2/π)||u||²`. This bound holds on the complete form domain;
no operator-domain membership is being assumed for an arbitrary trial.

For `2a<log 2`, every original prime shift and the altered `n=2` shift
vanish exactly. The v1.18 remainder bound, with physical length `L=2a`, is

    ||K_physical,a|| <= log(2π) + 2∫_0^(2a)|k(y)|dy + 4sinh(a),
    k(y)=exp(-y/2)/(1-exp(-2y)) - 1/(2y),  k(0)=1/4.

It retains both poles through their full signed kernel. Therefore

    q_delta,a[f] >= [log(1/a)-2/π-log(2π)
                    -2∫_0^(2a)|k(y)|dy-4sinh(a)] ||f||².

The bracket tends to positive infinity as `a` decreases to zero. This
establishes strict positivity on sufficiently small windows, in the full
space and both parities. No effective first-zero location, simplicity or
ordering is inferred from this lower bound.

## 4. Finite first zero and support saturation

Accept the separately reviewed negative compact test in each parity. Put
each test in a finite interval to obtain a negative lowest eigenvalue
there. Together with small-window positivity and continuity, this yields

    a_* = inf {a>0: mu_delta(a)<=0},
    0<a_*<∞,  mu_delta(a_*)=0,  mu_delta(b)>0 for 0<b<a_*.

The zero is attained by a nonzero operator-domain vector: the operator of
the closed form has compact resolvent, and a form minimizer satisfies its weak eigenvalue
equation; the representation theorem puts it in the operator domain. The
**full** form is nonnegative at its full first zero. Apply the same argument
to the even and odd restrictions. At a parity sector's own first zero,
only that sector is asserted nonnegative; the other sector may already be
negative. The full first-zero parameter is the smaller of the two parity
parameters.

For support, the compact-support global form is translation invariant.
The multiplier and prime-correlation terms make this immediate. The pole
pair must first be kept together as the kernel `2cosh((x-y)/2)`; the
individual positive and negative pole squares are not separately invariant.
Support consistency extends from the core to the complete form domain.
Translation preserves the logarithmic Fourier norm because it changes the
transform only by a unimodular phase.

If a nonzero full first-zero nullvector had essential support diameter
strictly less than `2a_*`, choose a slightly larger interval of diameter
still less than `2a_*` containing that support and translate it into
`(-b,b)` with `b<a_*`. It belongs to `V_b`, has the same norm and zero
form value, contradicting strict positivity there. Since its essential
support already lies in `[-a_*,a_*]`, its extreme support points are exactly
the two endpoints.

For a parity first zero, essential support is symmetric. If its support
radius were less than its window radius, place it in a smaller **centered**
interval, preserving parity, and obtain the same contradiction. No
translation out of the parity subspace is used. Support reaching the
endpoints does not assert a nonzero endpoint trace or create an open
exterior-of-support cell inside the window.

## Final assessment

The first-zero passage survives this independent reconstruction under the
explicit negative-test and canonical-form inputs. No omitted pole, prime
entry jump, norm-continuity assumption, unproved `H¹` upgrade, or support
translation error was found. In particular the topology concern is resolved
by compactness of bounded logarithmic-form energy, not by a new operator
estimate.

This assessment does not validate the separately delegated near-radical
detection step by assertion. It does not locate a first-zero window, compute
a nullvector, replay the v1.36 proof, or rule out the original API or a
bounded-floor method. It is independent agent validation of these stated
links, not external expert review or a new mathematical research node.
