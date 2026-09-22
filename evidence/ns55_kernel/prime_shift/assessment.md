# NS-55 — prime-shift and Fredholm assessment

Classification: exact identities; proved, scoped operator obstructions; named open arithmetic input. No numerical computation is offered as proof. RH and G2 remain open.

Assigned after claim `a3c4fb6`; only `evidence/ns55_kernel/prime_shift/` is owned by this subagent. Read full AGENTS.md, NS-51's `evidence/ns51_kernel/proof.tex`, v1.18's complete operator and domain decomposition, and the relevant source normalization. No manuscript/board/map edits, commits, pushes or branch switches.

## 1. An exact useful reformulation

Write `g=g0+sum w_n (|t|-log n)_+`, where g0 retains the archimedean and both pole terms. For the zero extension of f, let H be its clamped antiderivative and M its total integral. Then

`(g'*Ef)(x)=(g0'*Ef)(x)+sum w_n [H(x-log n)+H(x+log n)-M]`.

This is a continuous identity for every L2 f, with no H1 hypothesis on f. The primitive H does have a weak L2 derivative, but that is regularity of an antiderivative, not a gain for f. Differentiating returns the two-sided translated f terms and the nonlocal logarithmic operator.

The identity does not allow recursive propagation from one vanishing interval: the unshifted archimedean term still samples all of f. Analyticity of the kernel away from its diagonal does not prove that the convolution is analytic across the unknown support. Prime-free exterior gaps are a separate additional condition investigated by the domain agent.

## 2. An actual obstruction to positive transfer

For disjoint smooth tests avoiding prime-power separations, the full off-diagonal kernel is

`J(t)=2 cosh(t/2)-rho(t)`, with `rho(t)=e^(t/2)/(e^t-e^(-t))`.

For u=e^t it has the sign of `u³-u-1`. Let r>1 be the unique root of that polynomial. At every interval length L>log r, disjoint nonnegative smooth bumps can be placed at a separation above log r and away from every (finitely many) prime-power separation. The exact mixed energy q(f,g) is then positive.

Since these tests belong to the complete operator domain, the semigroup pairing has derivative `-q(f,g)<0` at time zero. Thus the complete full-space semigroup is **not positivity preserving** with respect to the ordinary nonnegative cone. This also excludes repairing that property by conjugation with a strictly positive bounded multiplier having bounded inverse.

This is an actual operator property, not a failure of a numerical estimate. It is **not** negative diagonal Weil energy, not failure of API, and not a claim about a parity-restricted order cone. A specialized uniqueness theorem or a different cone is not excluded. Positivity of a self-adjoint operator's quadratic form and positivity preservation by its semigroup are different statements.

## 3. Why raw analytic perturbation in window size is unavailable

On the fixed rescaled interval (0,1), a newly entering symmetric prime shift has norm exactly 1 for `ell<L<2ell`, but is zero for `L<=ell`. At each prime-power threshold the actual bounded K perturbation has an operator-norm jump at least its coefficient w. The proof isolates input and output in the two shrinking endpoint intervals; old prime shifts and scalar diagonal do not connect those intervals, while the bounded integral kernels give a vanishing contribution.

The screw-ramp operator, which is compact, instead has exact Hilbert–Schmidt norm `w(L-ell)_+²/sqrt(6)`. It becomes small, but its vanishing on one side and nonvanishing on the other preclude real analyticity through prime entry. These facts do not contradict form or norm-resolvent continuity and do not preclude a suitably justified alternative parameterization.

## 4. What Fredholm theory can legitimately deliver

At one fixed window choose `T=A_log+beta I>=I`, set `B=K-beta I`, and form the compact self-adjoint operator `C=T^(-1/2) B T^(-1/2)`. Nullvectors of the complete operator correspond exactly to eigenvalue -1 of C. The coupling family `T+zB` is invertible outside the discrete real set of reciprocals `-1/nu`, for nonzero eigenvalues nu of C. Its inverse is meromorphic with finite-rank principal parts.

This is proved directly with the compact spectral theorem; no window analyticity is assumed. The exceptional set can still contain the actual coupling z=1. Moreover the compact potential operator from NS-51 is not itself Fredholm on an infinite-dimensional space; standard analytic Fredholm theory applies to identity plus compact (or a proved Fredholm family), not to a compact first-kind equation alone.

**Missing input:** arithmetic exclusion of the eigenvalue -1 at every required window, or a genuinely stronger uniqueness mechanism for the two-sided primitive equation. No such exclusion is obtained here.

## Primary sources verified

- Huyuan Chen and Tobias Weth, *The Dirichlet Problem for the Logarithmic Laplacian*, [author preprint](https://arxiv.org/abs/1710.03416), accepted in Communications in Partial Differential Equations. This is the principal-operator framework already used in v1.18; its maximum-principle results for the logarithmic operator cannot simply be transferred to the full signed arithmetic perturbation.
- Michael Taylor, *Multidimensional Analytic Fredholm Theory*, [author paper](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fred.pdf), Introduction and Theorem 1.1. The theorem requires a holomorphic Fredholm family and one invertible point, and allows exceptional parameters. Our fixed-window coupling assertion is proved directly; this citation checks the scope of the proposed theorem application.
- The exact screw formula and complete-domain affine criterion are inherited from the archived NS-51 proof, which identifies the Suzuki source and sections. No new zero distribution theorem is used.

## Reporting

What changed: replace one-way prime propagation by the exact two-sided antiderivative equation; replace raw window analyticity by a legitimate fixed-window coupling family. What fails: ordinary positive-semigroup transfer and the raw analytic-window shortcut. What remains open: API. No negative diagonal direction, new window, tail metric, G2 or RH claim. The integrating author runs the full manuscript build and reports its page/reference counts; this assessment is not a substitute build.
