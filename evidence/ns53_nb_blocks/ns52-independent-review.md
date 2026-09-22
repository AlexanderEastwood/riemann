# Independent review of NS-52 paired heat transport

Reviewer: NS-53 approximation subagent, 22 September 2026 (UTC).
Reviewed `evidence/ns52_heat_pairs/proof.tex` in this worktree before parent integration. This review changes no NS-52 files.

## Disposition

**0 MAJOR mathematical findings. 1 MINOR typesetting finding comprising two mechanical edits, sent to the author.** The propositions are exact identities and conditional implications with the arithmetic bridge explicitly open. No unconditional closure of the heat route is justified or claimed.

## Checks

1. **Normalization:** Polymath15 equations (1)–(4) give `H_0(z)=xi(1/2+iz/2)/8` and `∂_t H=-∂_z² H`. Therefore `Z_t(w)=8H_t(2w)` has `Z_0=Xi` and heat coefficient `kappa=1/4`. Checked against the primary full text: <https://arxiv.org/html/1904.12438>. The nonunitary transform matches the manuscript's equations `v1:eq:transform` and `v1:eq:zeros`; the off-real second factor is correctly `conj(F_g(conj(w)))`.
2. **Core zero sum:** the fixed strip for nonnegative times, a uniform quadratic zero count from Jensen, and arbitrary smooth-test transform decay suffice for absolute convergence and continuity on the smooth core. The manuscript does not use this to justify differentiating the infinite sum.
3. **Finite-cluster transport:** differentiating the argument-principle integral gives the positive sign `kappa ∮ Psi' Zww/Z /(2pi i)`. Factoring the simple cluster gives velocities `2kappa sum_(k≠j)1/(wj-wk)+2kappa A'/A(wj)`. Pairing yields the stated divided difference. At an order-m zero the double-pole residue is `kappa m(m-1)Psi''+2kappa m(A'/A)Psi'`. The exterior factor cannot be omitted and is retained.
4. **Support cost:** the derivative bound `2a(2a)^n exp(2a|Im w|)` follows by Cauchy–Schwarz and Leibniz. At a double zero it gives `16kappa(a³+B a²)exp(2aY)`. The odd-profile witness has `Psi'=0` and `Psi''=2a³ M1²`; its cluster derivative is `4kappa a³ M1²`. This is conditional on that cluster's occurrence and is correctly not a bound on the complete derivative.
5. **Translated-radical comparison:** for each fixed M, first pass to the cofinal cutoff limit. The L1 limit controls one real Fourier evaluation. The translated packet has uniformly bounded L2 norm from the absolutely summable Schwartz autocorrelation and has evaluation `sqrt(M)F_phi(c)`. Letting M grow only after the cutoff limit contradicts the same-test comparison if an unmatched real deformed zero exists. No estimate uniform in M, global closed form, or lower semicontinuity is smuggled in. The cutoff-radical and unmatched-zero hypotheses are explicit. The manuscript's source transform at its CCM selection subsection is a nonzero multiple of Xi, consistent with the interpretation.

## MINOR M1 — typesetting

The residue display had a form-feed control character in place of the backslash of `\frac{m(m-1)}`. The exhaustion-time integral had a comma before `dt`, rather than `\,dt`. These are mechanical corrections; the intended formulas and proof are unambiguous. They were sent to the NS-52 author before integration. A clean full build remains the integrating author's responsibility.

## NOTE

The existence of an unmatched real zero at the chosen positive time is not established in this checkpoint. The conclusion must remain conditional on it. Pair cancellation alone is not a support-uniform estimate, and the possible contribution of all remaining clusters is not controlled by the single-cluster witness. The current text explicitly observes both limitations.
