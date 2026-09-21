# NS-5 completed: complete W4 has a simple even ground

**Category: certified computation and proved implication.** This run
executes the requested complete-operator spectral-ordering task. It does
not substitute finite eigenvalue diagnostics.

At the exact ordinary spectral threshold sigma=10^-73, outward Arb LDL
certifies the following counts at both1024 and1280bits:

| Sector | Head dimension | Negative pivots | Positive pivots |
|---|---:|---:|---:|
| even |17|1|16|
| odd |16|0|16|

The exact saved even finite trial has complete Rayleigh quotient

    2.45361754930e-75 < q(f)/||f||^2 < 2.45361754931e-75.

Together with prior complete strict positivity, this proves

    0 < mu0 < 2.454e-75,    mu1 > 1e-73,
    mu1 - mu0 > 9.7546e-74.

Eigenvalues here belong to the complete ordinary Hilbert-space operator
and are counted with multiplicity. Thus the ground is simple and even.

## What changed

The v1.17 inertia logic transfers; its hard-coded lambda3 tail constants
do not. Instead of rebuilding every shifted residual, we bound the entire
inverse change using the already certified complete lambda4 Schur forms.
For the old exact trial G=(V;Z), set K=G*WG, Hh=V*V, Ht=Z*Z. The existing
complete bounds are S^V>=kappa K, with kappa=.62629 even and .428 odd,
and T>=delta I, delta=1.7940e-8. Then for 0<sigma<delta:

    S_sigma^V >= L_sigma
      = kappa K - sigma [Hh + 2/(1-sigma/delta)(Ht + K/delta)].

Proof: write r=BV+TZ, C=r*T^-1r, Y=T^-1BV. The exact identities are
S^V=K-C and

    S_sigma^V = S^V - sigma Hh
                    - sigma Y*(I-sigma T^-1)^-1Y.

Since 0<=C<=K and Y=-Z+T^-1r,

    Y*Y <= 2Ht + 2C/delta <= 2Ht + 2K/delta.

This gives the displayed lower bound by spectral calculus. It retains the
ordinary Gram and the full inverse-shift term. A negative eigenvalue of
the lower form alone would not prove a negative shifted Weil direction;
the separate exact Rayleigh witness supplies that indispensable direction.
Square completion and compact resolvent then give the complete ordering.

## Precision and evidence scope

Both new runs reconstruct the same exact dyadic trials through4096 and
recompute their ordinary Grams. The old complete residual gates are
replayed on their saved enclosures: even768/896bits, odd complement768bits,
odd repaired direction1024/1280bits. The latter trial has support8192 but
exactly the same relevant physical head. The old infinite-tail assemblies
are not represented as newly recomputed. They remain inherited inputs
from v1.25/v1.26, with hashes recorded by the new verifier.

The earlier eight-order diagnostic concerns the even-sector finite
compression and is not a global complete spectral gap. The smaller
complete trial values differ from the N64 diagnostic, as expected when
the support grows. The log records the initially rejected threshold.

## External theorem and its exact scope

[Connes–van Suijlekom, Theorem6.1](https://arxiv.org/html/2511.23257v1#S6.Thmtheorem1)
requires a real distribution on[0,L] whose form on trigonometric
polynomials defines a lower-bounded essentially selfadjoint operator,
with simple isolated lowest eigenvalue and reflection-even eigenfunction.
It does not require a positive lowest eigenvalue or a nonzero endpoint.

The complete proof supplies the actual one-sided distribution, including
the origin counterterm and correct logarithmic diagonal; merely saying
"an even kernel" would not address the caveat in their Remark4.3.
The manuscript's prop:v114-weil-core supplies the essential selfadjointness
and compact resolvent. Taking L=2log4, the centered unitary Fourier
transform differs from their transform by a nonzero scalar and
exp(-izL/2), so its zeros are unchanged. Therefore xi-hat_4, the entire
Fourier transform of the complete ground eigenfunction, has only real
zeros. Simplicity of those zeros is not asserted.

This is a new certified fixed-window application within the project,
continuing v1.17's spectral mechanism and applying the cited existing
theorem. Worldwide novelty or publication readiness has not been established.
No convergence to Riemann Xi is proved. **No G2 gap was closed; RH remains
unproved.**
