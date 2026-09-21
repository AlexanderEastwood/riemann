# Reusing the exact finite trial in the full canonical Weil operator

The old upper bound **5.32e-38 is an actual Rayleigh quotient bound for an explicitly specified vector**, not merely an upper enclosure of a finite eigenvalue. It therefore supplies an exact full-operator trial bound, with no projection-error adjustment.

## Exact physical vector and normalization

Let L=2 log(3). Read the 65 decimal strings c_0,...,c_64 in `g2_finite_candidate.json` as exact rational numbers, and put c_-n=c_n and

    s=c_0^2+2 sum_{n=1}^{64} c_n^2.

The physical unit vector is

    v(u)=[c_0+2 sum_{n=1}^{64}c_n cos(2 pi n log(3u)/L)]/sqrt(Ls),
          1/3 <= u <= 3,

and is extended by zero outside this interval. The Hilbert measure is du/u. Thus v is real, invariant under u -> 1/u, and has norm exactly one. In the orthonormal even Fourier basis its coordinates are

    (c_0, sqrt(2)c_1, ..., sqrt(2)c_64)/sqrt(s).

There is no extra factor of two in a parity Gram matrix, and no factor of lambda in this unitary logarithmic coordinate change. The manuscript's first-slot-linear convention is retained.

The unnormalized norm is enclosed by

    sqrt(s)=0.651725550833717052741540427832888609509660988458...,

and the candidate file's SHA-256 is

    6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e.

The numerical routine that originally generated these strings is not a proof assumption. The rational strings themselves define the vector. A byte-for-byte copy is retained in this directory.

## Audit and fresh verification of the Rayleigh quotient

`g2_certificate/certify_g2_finite.py` first computes the exact norm of these rational coefficients, forms the normalized even coordinate vector, and then computes alpha=v^T W_even v. Its JSON explicitly records the strict comparison alpha<5.32e-38. The independent `certify_g2_series.py` forms the full signed-index vector and computes c^T W c/(c^T c), with the same result. The old upper eigenvalue claim was derived from this quotient by the variational principle.

The fresh verifier `certify_trial_reuse.py` uses the current exact assembly at 768 bits and verifies overlap with both independent old quotient enclosures. It certifies

    alpha=QW_3(v,v)
         =5.3123817005863590028616680254783549108663620501086...e-38
         <5.32e-38.

The finite polynomial v belongs to the proved canonical operator core. Since P_64 v=v,

    <Wv,v>=<P_64 W P_64 v,v>

exactly. Although Wv generally has infinitely many nonzero Fourier coefficients, those outside the support of v do not contribute to this quadratic pairing. No assumption that v is an exact prolate source, an eigenvector, or endpoint-corrected is needed.

The old certificate's lower eigenvalue bound 3.64e-38 and angle 0.000216 concern its finite matrix only. They are **not** reused as continuum lower bounds or continuum angles.

## Complete residual: certified, but unsuitable for a raw gap estimate

The verifier computes every even residual row through J=4096 and bounds every omitted row by the proved exact moment expansion, with M=64 and 48 terms. This is the residual of the full canonical operator,

    r=(W-alpha I)v.

The resulting rigorous enclosure implies

    3.33684e-19 < ||r|| < 3.88714e-19.

At a spectral threshold a=1e-34, the crude residual estimate ||r||/(a-alpha) is approximately 3.8892e15 and gives no useful angle information. This failure is consistent with v having a tiny high-energy component. It does not invalidate the much sharper energy argument below. `full_trial_certificate.json` retains the finite residual, remote majorant, and all scalar enclosures.

## Even-ground overlap after the shifted spectral certificate

Assume the independently proved full positivity of W and the new shifted certificate showing that exactly one eigenvalue of the **complete even sector** lies below a>alpha. Write u_0 for its unit even ground eigenvector and P_0 for its orthogonal projection. Both the trial and corrected trial below are exactly even. Therefore only the even-sector threshold is needed in the energy bound; a smaller odd-sector threshold does not weaken this bound. The spectral theorem gives

    alpha=<Wv,v> >= a ||(I-P_0)v||^2.

Consequently

    sin(theta_v) <= sqrt(alpha/a),
    |<v,u_0>| >= sqrt(1-alpha/a).

For a=1e-34 the certified numbers are

    sin(theta_v) < 0.023048605,
    |<v,u_0>| > 0.9997343456.

The phase-aligned ordinary vector distance is below 0.023050136. These bounds use positivity and the complete even spectral threshold, not the ineffective residual/gap estimate. The JSON labels these overlap quantities conditional on that separately checked threshold. If the odd sector is separately certified above a smaller threshold still exceeding the even trial energy, u_0 is also the unique global ground. A failed lower-bound test at odd threshold 1e-34 does not refute this even-sector argument.

## A stronger bound from an exact finite correction

The fresh verifier also recomputes the old even complement construction. Decompose the N=64 even space as span(v) plus v-perp, and write its exact matrix as [[alpha,r^*],[r,C]]. Put

    z=(C-alpha I)^(-1)r,
    q^2=||z||^2,
    E=<z,r>.

The independent old complement certificate proves invertibility; a fresh Arb LU solve encloses this exact z. This is an exactly defined vector using the actual matrix, not an approximate eigenvector silently treated as exact. With z identified as a vector perpendicular to v, define

    w=(v-z)/sqrt(1+q^2).

The vector w is exactly even, remains in E_64, and has full-form Rayleigh quotient

    beta=alpha-E/(1+q^2)
        =3.643399656992330629578219734731385...e-38
        <3.644e-38.

Indeed z^*(C-alpha I)z=E, which proves this identity after expanding the numerator. Also

    sin(angle(v,w))=q/sqrt(1+q^2)
                  <0.000215892090.

For the complete even threshold a=1e-34, positivity gives sin(angle(w,u_0))<=sqrt(beta/a). The triangle inequality for rank-one orthogonal projectors then yields

    sin(angle(v,u_0))
      <=q/sqrt(1+q^2)+sqrt(beta/a)
      <0.019303583561 <0.01931.

This does not import the old finite ground eigenvector as the continuum ground. It uses a new exact trial w and the newly certified complete even threshold. It also supplies the sharper full even ground eigenvalue upper bound beta<3.644e-38. A separate odd-sector ordering certificate promotes this to the global ground upper bound.

## Transfer to the exact projected repaired source

The v1.13 certificate `g2_source_certificate/pswf_source_certificate.json` proves

    ||P_64 p_3-c|| < epsilon=2.60e-36,

where c denotes the unnormalized rational polynomial above. Its recorded sharper upper enclosure is 2.5940161025...e-36. The new script checks the old PASS gates, input candidate hash, and bound before importing this statement. In particular,

    ||P_64 p_3|| >= ||c||-epsilon >0.

Put rho=epsilon/||c||. The elementary geometry of a ball of radius epsilon centered at c shows that the normalized vectors have positive real inner product and

    ||P_64 p_3/||P_64 p_3|| - v||
       <= sqrt(2 rho^2/[1+sqrt(1-rho^2)])
       <3.989410e-36 <4e-36.

For completeness, if z=P_64 p_3 and t=Re<z/||z||,c/||c||>, then closeness gives t>0, while minimizing ||r z/||z||-c|| over positive r gives epsilon^2>=||c||^2(1-t^2). Hence t>=sqrt(1-rho^2), which yields the displayed distance without cancellation-prone subtraction of nearly equal numbers.

The orthogonal projection I-P_0 is contractive, so the triangle inequality gives

    ||(I-P_0)P_64 p_3/||P_64 p_3||||
       <= sqrt(alpha/a)+3.989410e-36.

At a=1e-34 this first estimate is less than 0.02305. Replacing the trial-angle bound by the stronger finite-correction argument gives

    ||(I-P_0)P_64 p_3/||P_64 p_3||||
       <0.019303583561+4e-36 <0.01931.

No crude Rayleigh perturbation by the source coefficient error is used; such a perturbation would be far too large relative to the 1e-38 trial energy.

This conclusion is about the exact **projected** source P_64 p_3 at one fixed window. It says nothing by itself about the angle of the unprojected source, the physical endpoint, a graph-normalized residual, or a uniform growing-window family. The established relative endpoint error near 1.3745 at this cutoff is unchanged.

## Reproducibility and retained inputs

Run `certify_trial_reuse.py` with Python-FLINT 0.9.0 and the adjacent `g2_schur_directional` assembly and remote-Gram modules. It takes no numerical source generator as input.

The prior complete v1.15 archive contains the exact candidate, both independent finite certifier programs, both finite result JSON files, their matrix intervals, and the exact-source certificate. Every ZIP member in that archive passed its CRC check. The scratch v1.16 ZIP was found truncated; the parent task is rebuilding the cumulative archive atomically from the valid prior archive and the intact current files. No archive was mutated by this trial audit.

Relevant immutable dependency hashes:

```text
g2_finite_certificate.json
f35600e45b2e2af1234c6611983e241580eee8817669ac7c468b2783472e87ed

g2_finite_series_certificate.json
a207516292d6afcc8198da1af463b6e10dd59b2ba77bf31d91034aedfad8d811

pswf_source_certificate.json
06ed429775be546fabcefa7f300615fd37ff8c00a879229e7fdbc654ad9fcc19
```

The full threshold certificate and any resulting ground-order theorem are separate files supplied by the parent task. No uniform G2 or RH claim is made here.
