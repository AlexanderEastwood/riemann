# G1/G2 audit - boundary quotient and sharp boundary-trace scale

Date: 2026-09-19

## Status

This manuscript is **not a proof of the Riemann Hypothesis**. This run does not claim the missing zero-independent upper bound. It sharpens the exact compatibility gate and proves two no-go/reduction results that prevent further work from being spent on endpoint-preserving interior reshaping of the G1 candidate or on a second boundary-annihilation of the reflected G2 test.

## G1 status

The previously audited G1 chain is unchanged:

- the fixed-order prolate/co-Poisson cross-tail estimate is zero-independent;
- the Sobolev continuum estimate gives a residual of size `|B_lambda| r(lambda)` against the full smoothed Hardy family;
- de la Vallee-Poussin finite transfer and the exact-boundary shell give explicit finite candidates;
- on a common G1/G2 diagonal the literal term `(b/a)<D_log W k, v>` is `o(1)` for the boundary-annihilated adjoint-resolvent tests at every fixed Jordan multiplicity.

The new result below shows that, once this G1 pairing condition is imposed, the G2 mismatch is invariant under every even endpoint-preserving change of candidate that also satisfies G1.

## G2 audit correction: sesquilinear cross pairing

The reflected-partner cross-Weil constant remains nonzero at arbitrary multiplicity, but the exact first-slot-linear zero-side formula is sesquilinear. The unique nonzero summand is

`conj(kappa(rho) zeta^(m)(rho)/m!) * kappa(rho#) zeta^(m)(rho#)/m!`

up to the positive multiplicity factor and the fixed global phase convention. The previous non-conjugated display was a normalization inaccuracy. It did **not** affect the nonvanishing argument, because both factors are nonzero, but the manuscript now records the correct conjugation.

## New G2 theorem 1: rank-two boundary traces exhaust the reflected signal

For the top Jordan sample `x_m`, radical predecessor `u_m`, and

`A_rho = i D_log - mu_rho`,

let `y=A_rho^* v`, `b_m=eta_N(x_m)`, and `c_m=<x_m,beta_log>`. The finite CCM commutator gives the exact identity

`<W x_m,y> = <W u_m,v> + i b_m <beta_log,v> - i c_m <eta_N,v>`.

Because `u_m` is a global Weil-radical test, the first term tends to zero on the already audited Hardy-resolvent families. Therefore every surviving reflected-partner lower signal factors through the two boundary traces

`v -> <eta_N,v>` and `v -> <beta_log,v>`.

The constructed reflected test already has `eta_N(vtilde_m)=0` exactly. If one also forced `<beta_log,vtilde_m>=0`, the reflected cross pairing would tend to zero and the G2 lower signal would disappear. Hence a second boundary-annihilation cannot produce a contradiction while retaining the reflected-partner lower bound. The beta channel is not an artifact of one choice of test; after the radical bulk is removed it is the unique surviving CCM boundary channel.

## New G2 theorem 2: the surviving beta trace has the exact critical scale

The previous block theorem gave

`i b_m <beta_log,vtilde_m> -> C_{rho,m} != 0`.

For the same fixed-sigma Hardy sampler,

`b_m/sqrt(L) -> sigma F_{rho,m}(sigma) != 0`.

Therefore

`sqrt(L) <beta_log,vtilde_m> -> C_{rho,m}/(i sigma F_{rho,m}(sigma)) != 0`.

This is a materially sharper coercivity statement. Under a hypothetical off-line block the physical boundary trace is forced to be exactly of order `L^(-1/2)`. Consequently a closing upper theorem must prove

`<beta_log,vtilde_m> = o(L^(-1/2))`.

An `O(L^(-1/2))` estimate is not enough; it sits exactly at the obstruction scale.

## New G1/G2 theorem: boundary-quotient invariance

Let `k1` and `k2` be any two even finite candidates with the same nonzero boundary amplitude

`eta_N(k1)=eta_N(k2)=a`,

and put `q=i b/a`. Their difference `f=k1-k2` is even and has zero boundary. Since `beta_log` is odd,

`eta_N(f)=0` and `<f,beta_log>=0`.

The rank-two CCM commutator therefore vanishes on `f` exactly:

`[D_log,W] f = 0`, hence `W D_log f = D_log W f`.

It follows that

`<W(u-q D_log k1),v> - <W(u-q D_log k2),v>`

`= -q <D_log W(k1-k2),v>`.

Thus if both candidates satisfy the audited G1 pairing condition, their G2 mismatch pairings differ by `o(1)`.

This proves that after G1 is imposed, the reflected G2 obstruction depends only on the endpoint class of the even candidate, not on its interior prolate/co-Poisson/moment-repair/filter shape.

## Shell universality consequence

Scale the explicit high-frequency shell to the same physical endpoint `B_lambda` as the exact-boundary prolate/co-Poisson candidate. The existing shell estimates let its normalized `D_log W` pairing be made arbitrarily small while preserving the endpoint exactly. Boundary-quotient invariance therefore gives the same nonzero reflected mismatch limit for the pure shell as for the full prolate/co-Poisson candidate.

This is a useful negative result: **interior prolate geometry is no longer the active compatibility variable once G1 has been enforced**. Endpoint-preserving reshaping, extra moment repairs, different VP filters, or moving the candidate mass into a remote shell cannot remove the G2 lower obstruction.

## What remains

The active RH-strength target is now sharper than in r6:

1. derive a **zero-independent arithmetic upper bound** for the CCM boundary trace on the boundary-annihilated Hardy-resolvent family;
2. the bound must be little-o at the exact critical scale, `o(L^(-1/2))`;
3. equivalently, derive an upper bound that kills the finite family of reflected top-Jordan mismatch pairings without replacing `W D_log k` by the already-controlled `D_log W k`;
4. any replacement transport must escape the endpoint-quotient equivalence above rather than merely reshaping the same even candidate.

No such upper bound is proved in this run.

## Routes now explicitly closed for the active G1/G2 program

Do not reopen these without genuinely new arithmetic input:

- scalar shifts or other corrections commuting with `D_log`;
- treating `W D_log k` as another copy of the G1-controlled `D_log W k`;
- endpoint-preserving interior retuning of the prolate/co-Poisson candidate;
- pure boundary-shell substitution as a closure mechanism;
- adding more reflected test vectors solely to annihilate both CCM boundary traces;
- relying on global zeta divisibility alone;
- endpoint matching alone without bulk/form transfer.

## Bottom line

G1 remains an audited zero-independent vanishing mechanism for the explicit finite residual. G2 is now more rigid: at arbitrary multiplicity the reflected lower signal is completely boundary-supported after radical transfer, and its surviving physical trace is nonzero at the exact `L^(-1/2)` scale. The new boundary-quotient theorem proves that all even same-endpoint G1-admissible candidates have the same asymptotic G2 mismatch. The remaining problem is therefore not to improve the interior prolate/co-Poisson shape, but to obtain a genuinely arithmetic little-o estimate for the finite CCM boundary channel itself. This remains an RH-strength open step, not an RH proof.

---

# Run 8 addendum - exact arithmetic realization of the beta channel

## Status

Still **not an RH proof**. This run does not prove the required `o(L^(-1/2))` upper bound. It does, however, remove a conceptual compatibility ambiguity: the surviving G2 boundary vector is now written exactly in terms of the *same centered pole-prime discrepancy* already used in the audited G1 proof.

## Exact CCM coefficient identity

Write `L=2 log lambda`, `t_n=2 pi n/L`, and

`V(y)=2(e^(y/2)-1)-sum_{2<=k<=e^y} Lambda(k)/sqrt(k)`.

If `b_lambda(n)` is the odd CCM coefficient before physical scaling, so

`beta_log=(2 pi/L) sum b_lambda(n) V_n`,

then the finite Weil matrix gives exactly

`b_lambda(n)`
`= 32 L sinh^2(L/4)n/(L^2+16 pi^2 n^2)`
`  + (1/pi) int_0^L sin(t_n y) rho_infty(y) dy`
`  + (1/pi) sum_{1<k<=e^L} Lambda(k)k^(-1/2) sin(t_n log k)`

with `rho_infty(y)=e^(y/2)/(e^y-e^(-y))`.

After combining the point term with the prime sum and integrating the centered prime cumulative by parts,

`b_lambda(n)`
`= (t_n/pi) int_0^L V(y) cos(t_n y) dy`
`  + (1/pi) int_0^L (rho_infty(y)-e^(-y/2)) sin(t_n y) dy`.

This formula contains only primes up to `e^L=lambda^2`, the point term, and the archimedean kernel. No nontrivial zero locations enter the matrix/vector.

A direct numerical sign/normalization audit was also run independently at several nonintegral values of `L` and positive/negative Fourier indices. The direct point+prime+archimedean formula and the centered-discrepancy formula agreed to roughly `1e-17`--`1e-19` in the tested cases. This numerical check is only an audit of the algebra; the manuscript proof is exact.

## Exact same-object trace formula

For a finite vector

`v=L^(-1/2) sum h_n V_n`,

put

`H_v(y)=L^(-1) sum h_n exp(i t_n y)`,

`A_v(y)=conj(H_v(-y))-conj(H_v(y))`.

Then, in the manuscript's first-slot-linear convention,

`i sqrt(L) <beta_log,v>`
`= int_0^L V(y) A_v'(y) dy`
`  + int_0^L (rho_infty(y)-e^(-y/2)) A_v(y) dy`.

Because `A_v(L-y)=-A_v(y)` and `A_v'(L-y)=A_v'(y)`, this folds exactly to `[0,L/2]` with the terminal prime discrepancy appearing as `V(L-y)`. This identifies the periodic endpoint aliasing that is absent from the special G1 co-Poisson cross-tail kernel.

## Strengthened G2 interpretation

For the already audited boundary-annihilated reflected top-Jordan test `vtilde_m`, the critical-scale theorem becomes the explicit finite arithmetic forcing statement

`i sqrt(L)<beta_log,vtilde_m>`
`-> C_{rho,m}/(sigma F_{rho,m}(sigma)) != 0`.

Thus, under a hypothetical off-line block, a finite prime/pole/archimedean observable built from the same CCM matrix is forced to have a nonzero limit. The hypothetical zero enters only through the test vector, not through the finite arithmetic operator.

This is the strongest same-object compatibility statement obtained so far: G1 and G2 are now literally driven by the same centered arithmetic discrepancy `V`; what differs is the kernel against which `V` is tested.

## Why the existing PNT estimate does not transfer

The unconditional bound already used in G1,

`|V(y)| <= C e^(y/2) e^(-c sqrt(y))`,

inserted *absolutely* in the new beta formula yields on every fixed physical band

`sup_{|t_n|<=T} |b_lambda(n)| <= C_T(1+lambda e^(-c_T sqrt(L)))`.

This does not tend to zero. In G1 the special co-Poisson cross-tail supplies an additional `e^(-L/2)=lambda^(-1)` factor, which cancels the `e^(L/2)` size of the terminal PNT remainder. The periodic Hardy trace has no corresponding factor at the level of the present absolute estimate.

Therefore the remaining compatibility theorem cannot be obtained merely by reusing the same unsigned PNT envelope more carefully. It must prove **signed arithmetic cancellation** for `V` against the exact Hardy boundary kernel, or an equivalent transport identity that turns that kernel into the G1 kernel without violating the already proved boundary-quotient obstruction.

## Updated active target

The active G1/G2 target is now:

- preserve the audited G1 co-Poisson vanishing theorem;
- use the exact beta arithmetic identity above to prove, uniformly on the relevant fixed reflected Riesz/Jordan test family,

  `sqrt(L)<beta_log,vtilde_m> -> 0`,

  equivalently `<beta_log,vtilde_m>=o(L^(-1/2))`;
- the proof must exploit signed prime correlation/kernel structure, because the current absolute PNT estimate is quantitatively too weak;
- do not reopen endpoint-preserving candidate retuning, scalar shifts, second boundary annihilation, or the `W D_log k` = `D_log W k` substitution routes already ruled out.

This remains the RH-strength gap.

---

# Run 9 addendum - projective candidate invariance and moving Hardy phase stress test

## Status

Still **not an RH proof**. This run proves three structural statements and isolates one new quantitative transfer gate. It does **not** promote the moving-phase contradiction to a theorem because the existing off-line semilocal form-transfer result was proved for a fixed Hardy multiplier, whereas the new phase depends exponentially on the growing interval length.

## 1. Boundary-quotient invariance is actually projective and does not need parity

The previous theorem assumed two even candidates with the same endpoint. Both assumptions can be removed on the already boundary-annihilated reflected test.

For arbitrary finite candidates `k1,k2` with nonzero endpoints `a1=eta(k1)`, `a2=eta(k2)`, set

`f = k1/a1 - k2/a2`.

Then `eta(f)=0`. The CCM commutator gives

`[D_log,W]f = - eta <f,beta_log>`

in the first-slot-linear convention. Since the reflected test `vtilde_m` also has `eta(vtilde_m)=0`, the commutator term vanishes **after pairing**:

`<W D_log f,vtilde_m> = <D_log W f,vtilde_m>`.

Therefore the two normalized mismatch pairings differ exactly by the difference of their normalized G1 pairings. Hence every nonzero-endpoint candidate satisfying the same projectively normalized G1 estimate represents the same asymptotic G2 mismatch class. Parity, identical endpoint amplitude, scalar rescaling, and interior candidate shape are no longer active compatibility variables.

This strengthens the earlier endpoint-preserving/no-go theorem.

## 2. A Hardy phase shift preserves the hypothetical reflected G2 signal but damps the physical endpoint

For fixed `sigma>1`, define

`Phi_tau(s)=exp(-tau(s-1/2))`, `kappa_tau=Phi_tau kappa`.

`Phi_tau` is bounded analytic in the Hardy half-plane and has unit modulus on the critical line. On the finite Fourier lattice it is therefore a unitary diagonal phase and commutes with `D_log`, so the sampled graph identity keeps exactly the same form.

The Hardy Cauchy formula gives the exact shifted endpoint factor

`endpoint_tau(F) = exp(-(sigma-1/2) tau) sigma F(sigma)`.

The same factor multiplies the adjoint-resolvent endpoints, so the *continuum* boundary-annihilation ratio is independent of `tau`.

For a hypothetical off-line pair `rho`, `rho#=1-conj(rho)`, the reflected global cross-Weil constant is exactly invariant because

`conj(Phi_tau(rho)) Phi_tau(rho#)=1`.

Thus one can exponentially damp the Hardy endpoint without damping the global reflected zero-side signal.

## 3. At the continuum-kernel level, the phase shift restores an absolute PNT gain

Let `rho=1/2+d+i gamma`, `d>0`, and let the shifted boundary-annihilated adjoint-resolvent test be formed with the same phase. The continuum logarithmic representative has two-sided exponential localization: on the endpoint-facing side any rate below `sigma-1/2` is available, while the reflected resolvent pole supplies a positive rate below `d` on the opposite side.

For `tau=theta L` with

`1/(2 sigma) < theta < 1/2`, 

the folded Hardy kernel obeys weighted estimates of the form

`int exp(-y/2)|A'_tau(y)| dy <= C exp(-tau/2)`

and

`int exp(y/2)|A'_tau(y)| dy <= C[exp(tau/2)+exp(L/4-d0(L/2-tau))]`.

Combining these with the same unconditional PNT remainder already used in G1 yields

`exp(-(sigma-1/2)tau) * | explicit folded beta arithmetic observable | <= C exp(-c L)`.

The critical terminal exponent is

`(1/2 - sigma theta)L`,

so the sharp threshold is `theta>1/(2 sigma)`. The slower reflected tail does not spoil the estimate: at the threshold its remaining exponent simplifies to

`((1-sigma)(1+2 d0))/(4 sigma) < 0`.

This continuum-kernel estimate uses only absolute values and the ordinary zero-independent PNT envelope; it does not need the signed cancellation sought in Run 8.

## 4. New active gate: moving-shift semilocal/endpoint transfer

If the previously proved fixed-multiplier G2 transfer could be substituted unchanged into the moving phase `tau=theta L`, the invariant global G2 lower signal and the preceding arithmetic upper estimate would contradict one another, which would close RH.

That substitution is **not audited** and is therefore not made.

The fixed-multiplier strip estimate and endpoint Riemann-sum convergence were proved with `kappa` fixed as `L -> infinity`. Here `Phi_{theta L}`:

- is unit modulus on the critical line but grows exponentially on the left side of the critical strip;
- makes the physical endpoint itself exponentially small, so absolute `o(1)` endpoint convergence is insufficient;
- requires relative endpoint control at scale `exp(-(sigma-1/2)theta L)`;
- requires a moving-family periodization/zero-side form-transfer estimate strong enough to survive the phase growth off the critical line.

The next G2 task is therefore concrete: prove or refute a quantitative moving-shift transfer theorem on a common finite diagonal. If it fails, identify the exact rate obstruction. If it succeeds at the required threshold, the phase-shift mechanism would materially change the status of the project and would require independent expert verification before any RH claim.

## Routes still closed

All previously rejected routes remain closed: scalar shifts, treating `W Dk` as `D Wk`, endpoint-preserving candidate reshaping, shell substitution as a closure, second boundary annihilation, and unsigned PNT on the unshifted Hardy kernel.

The new phase shift is not one of those routes: it changes the Hardy test family itself while preserving the global reflected cross pairing.

---

# Run 10 addendum - pole-aware G2 transfer and reflected endpoint alias

## Status

Still **not an RH proof**. This run closes the moving-Hardy-phase route identified in Run 9 and repairs an imprecision in the fixed-sampler G2 radical transfer. The unshifted G1/G2 boundary obstruction remains active.

## 1. Fixed-sampler radical transfer is valid, but the proof must be pole-aware

The earlier proof said that the Hardy zeta radical pairs to zero with the boundary-annihilated adjoint-resolvent test by the ordinary admissible-test zero-side transfer. That wording was too quick: the reflected component of the adjoint-resolvent top vector has multiplier

`- kappa(s) zeta(s) / (s-rho#)^(m+1)`.

If `rho#` has exact multiplicity `m`, this has a **simple pole** at `rho#`, with nonzero residue

`-kappa(rho#) zeta^(m)(rho#)/m!`.

Thus the reflected test itself is not an ordinary global Weil test at that point.

The fixed-sampler conclusion nevertheless survives. The fundamental-window transform of the pole term grows only linearly in `L` at the exceptional point, while the radical predecessor retains a zeta zero at the paired point and its truncation error is exponentially small by the same fixed strip margins as the standard periodization estimate. The exceptional zero therefore contributes `O(L exp(-cL))`; all other zeros are handled by the usual high-order vertical decay and zero counting. A Galerkin diagonal then gives

`<W u_m, vtilde_m> -> 0`.

This has now been stated as a separate pole-aware lemma. It strengthens the G2 audit without changing the fixed-sampler beta-channel lower theorem.

## 2. The moving phase has an unavoidable reflected-pole endpoint alias

Run 9 observed that the common Hardy phase

`Phi_tau(s)=exp(-tau(s-1/2))`

preserves the global reflected cross-Weil signal and, at the continuum-kernel level, restores an absolute PNT gain if

`tau = theta L`, `theta > 1/(2 sigma)`.

The missing question was whether the exact finite boundary quotient can follow that moving continuum sampler. The answer is **no for this construction**.

Write

`rho = 1/2 + d + i gamma`, `0<d<1/2`, and `q=sigma-1/2`.

For the reflected adjoint-resolvent top vector, the direct continuum Cauchy endpoint has size

`C_sigma exp(-q tau)`.

But the simple pole at `rho#` produces an opposite one-sided physical tail of rate `d`. After periodization, its nearest image wraps around the logarithmic circle and reaches the same endpoint with size

`R_rho exp(-d(L-tau)) exp(i gamma (L-tau))`, `R_rho != 0`.

Further images are smaller by another `exp(-dL)` factor. Therefore the periodized endpoint differs from the continuum endpoint by an asymptotically nonzero alias of precisely this size.

Relative endpoint convergence requires

`exp(-d(L-tau)) / exp(-q tau) -> 0`,

hence

`theta < d/(d+q)`.

## 3. The endpoint threshold and the PNT threshold are exactly disjoint

The Run-9 continuum PNT gain requires

`theta > 1/(2 sigma) = 1/(2q+1)`.

For every nontrivial off-line zero, `0<d<1/2`, and

`d/(d+q) < 1/(2 sigma)`

is equivalent to

`d < 1/2`.

So there is **no** phase speed `theta` that both:

1. moves the Hardy kernel far enough for the absolute PNT gain, and
2. keeps the exact finite periodized endpoint relatively close to the exponentially small continuum Cauchy endpoint.

In the PNT-admissible range the alias/target ratio grows exponentially like

`exp( ((d+q) theta - d) L )`.

This is not a Galerkin-resolution problem. For fixed `L`, increasing the Fourier cutoff converges more accurately to the periodized endpoint, including the alias. Thus the moving continuum boundary-annihilation ratio does not transfer to the exact finite boundary-annihilation ratio.

## 4. Consequence for the project

The moving-phase stress test is now a **rejected route**, not an open subgate. It cannot be used to combine the Run-9 continuum PNT upper bound with the finite G2 reflected lower bound on the same object.

The active target returns to the unshifted exact boundary channel, or to a genuinely different transport that preserves the finite endpoint quotient while gaining cancellation. The following previously rejected routes remain rejected as well: scalar shifts, commuting regularizers, treating `W Dk` as `D Wk`, endpoint-preserving candidate reshaping, pure shell substitution as closure, and a second exact boundary annihilation.

The manuscript remains explicitly **not an RH proof**.

# Run 11 - Exact G2 normal form and bounded-filter no-go

This run stayed exclusively on the remaining G1/G2 compatibility channel. It did **not** produce an RH proof. It sharpened the same-object obstruction in two ways.

## 1. Exact continuum normal form of the boundary-annihilated G2 test

For an off-line zero `rho` of multiplicity `m`, with reflected partner `rho#=1-conj(rho)`, the continuum adjoint-resolvent vectors satisfy

`v+^(hat)(s) = -kappa(s) zeta(s) / ((s-rho)^m (s-rho#))`,

`v-^(hat)(s) = -kappa(s) zeta(s) / (s-rho#)^(m+1)`.

Their Hardy endpoints are

`delta(v+) = - sigma zeta(sigma) / ((sigma-rho)^m (sigma-rho#))`,

`delta(v-) = - sigma zeta(sigma) / (sigma-rho#)^(m+1)`.

Hence the continuum boundary-annihilation coefficient is exactly

`alpha_infinity = ((sigma-rho)/(sigma-rho#))^m`.

Therefore

`vtilde_m^(hat)(s) = kappa(s) zeta(s)/(s-rho#) * [ alpha_infinity/(s-rho)^m - 1/(s-rho#)^m ]`.

The bracket vanishes at `s=sigma`, so it cancels the fixed Cauchy pole `(sigma-s)^(-1)` in `kappa` exactly. At `s=rho` the order-`m` zero of `zeta` cancels the apparent pole. At `s=rho#` one power remains uncancelled, giving the exact nonzero residue

`Res_{s=rho#} vtilde_m^(hat)(s) = -kappa(rho#) zeta^(m)(rho#)/m!`.

Thus after boundary annihilation the fixed Hardy Cauchy pole is gone and the **only strip singularity is the simple reflected-zero pole**. This isolates the G2 obstruction more sharply than the previous generic pole-aware argument.

## 2. Uniformly bounded Hardy filters cannot damp that pole while retaining G2

Let a common analytic Hardy filter `Phi_L` modify the sampler by `kappa -> Phi_L kappa`, and write

`M_L = ||Phi_L||_{H^infty(Re s > 1/2)}`.

The reflected cross-Weil signal is multiplied by

`conj(Phi_L(rho)) Phi_L(rho#)`,

while the simple reflected-pole residue is multiplied by

`Phi_L(rho#)`.

If the modified G2 cross signal retains a fixed fraction `c0>0` of the original signal, then

`|conj(Phi_L(rho)) Phi_L(rho#)| >= c0`.

Since `rho` lies in the Hardy half-plane,

`|Phi_L(rho)| <= M_L`,

and therefore

`|Phi_L(rho#)| >= c0/M_L`.

Consequences:

- if `M_L` stays uniformly bounded, the reflected-pole residue cannot be `o(1)`;
- if one wants residue damping `|Phi_L(rho#)| <= exp(-epsilon L)`, then necessarily `M_L >= c0 exp(epsilon L)`.

This is a maximum-modulus tradeoff, independent of the special moving-phase ansatz.

## 3. Absolute-PNT rescue by pole damping costs exponential Hardy norm

For `rho=1/2+d+i gamma`, `0<d<1/2`, the nearest periodic image of the reflected pole has exponential scale

`|Phi_L(rho#)| exp(-dL)`.

The terminal prime-discrepancy envelope available from the unconditional PNT is

`|V(L-y)| <= exp((L-y)/2 - c sqrt(L-y))`.

Therefore an **absolute-value** attempt to make the terminal folded term vanish solely by damping the reflected-pole amplitude needs, at exponential scale,

`|Phi_L(rho#)| <= exp(-(1/2-d)L + O(sqrt L))`.

Keeping a nondegenerate G2 cross signal then forces

`M_L >= exp((1/2-d)L - O(sqrt L))`.

But the audited G1 saving is only

`r(lambda) = poly(L) exp(-c1 sqrt L) + poly(L) exp(-L/2)`.

So the currently proved Sobolev/Hardy G1 transfer cannot absorb the exponential norm growth required by pole damping. This closes a broad class of bounded-filter rescue attempts: the remaining route must use **signed arithmetic cancellation in the unshifted exact boundary observable**, or a genuinely different transport.

## 4. Active G1/G2 target after Run 11

The open RH-strength statement is still a zero-independent estimate forcing

`sqrt(L) <beta^log_{lambda,N}, vtilde_m> -> 0`

on the same finite object for which G2 forces a nonzero limit under an off-line zero. The new normal form shows that the difficulty is concentrated in the simple reflected-zero pole; the filter no-go shows that uniformly bounded analytic Hardy filtering cannot remove that pole without also destroying the G2 signal.

The manuscript remains explicitly **not an RH proof**.

### Additional Run-11 structural corollary

The reflected pole is not peculiar to the specific endpoint subtraction. If `w` is any correction whose Mellin transform is holomorphic at `rho#`, then

`Res_{rho#}(c v- + w) = -c kappa(rho#) zeta^(m)(rho#)/m!`.

If the correction is zero-side invisible to the target top Jordan vector, so that

`QW(g_{rho,m}, A_rho^* w)=0`,

then its reflected cross signal is exactly `c C_{rho,m}`. Hence retaining a nonzero reflected G2 cross signal forces `c != 0`, and therefore forces the simple pole at `rho#` to remain. The usual boundary-annihilating correction `w=-alpha_infinity v+` is in this class: it cancels the Hardy endpoint and the `s=sigma` Cauchy pole, but not the reflected pole.
