# Directional Schur pilots at the exact window lambda = 3

These calculations retain the complete Weil matrix, its physical logarithmic diagonal, the actual Fourier basis, and both reflection sectors. The initial pilots below omit residual rows beyond J. A subsequent complete certificate, documented in the final section, includes those rows and succeeds in both reflection sectors at the fixed window lambda=3. No uniform growing-window G2 or RH conclusion follows.

## Reproducible assembly

`assembly.py` provides `assemble_sequences(nmax,bits,K)`, `parity_entry`, and `parity_block`. It implements the independently certified digamma/trigamma expansion from `g2_certificate/certify_g2_series.py`, including explicit geometric tail radii. Computations below use 768-bit Arb arithmetic and K=128. The prime-power shift at m=9 is identically zero at lambda=3 and is omitted exactly. The remaining prime powers are 2, 3, 4, 5, 7, 8. The pole contribution uses the exact identity sinh(log(3)/2)^2=1/3.

The new assembly's even and odd entries through Fourier cutoff 64 overlap all 8,321 corresponding interval entries from the independent integration certificate. See `assembly_independent_overlap.json`. The larger sequence caches preserve Arb radii and can be reused without repeating special-function evaluation.

## Exact finite calculation and its scope

Partition each reflection sector into head indices through N, intermediate indices N+1 through M, and output rows M+1 through J. Let F, B, T be the actual head, intermediate/head, and intermediate blocks. A verified interval solve encloses the exact Z=T^{-1}B. Define

    K_Z = F - B^* Z,
    R_J = W_{M+1:J,0:N} - W_{M+1:J,N+1:M} Z,
    S_J = K_Z - Gamma^{-1} R_J^* R_J.

For the odd sector, all index ranges start at 1. Arb LU encloses the exact inverse solve, so the intermediate residual is exactly zero mathematically. Interval LDL uses the exact symmetric matrix enclosed by these expressions. Strictly positive interval pivots certify positivity of this finite S_J. A negative interval pivot certifies failure of that chosen finite Gamma-only residual budget. Neither result alone determines the sign of W.

The full Schur certificate still requires subtracting Gamma^{-1} times a PSD enclosure of the omitted residual Gram for output rows n>J. Such a subtraction can destroy finite S_J positivity. Conversely, a negative S_J already prevents this particular lower-bound architecture from certifying positivity, regardless of how the omitted Gram is bounded.

## Results

| Sector | N | M | J | Gamma used | K_Z interval LDL | S_J interval LDL |
|---|---:|---:|---:|---:|---|---|
| Even | 256 | 512 | 1024 | 1.5867 | All 257 pivots positive | All 257 pivots positive |
| Odd | 256 | 512 | 1024 | 0.0148 | All 256 pivots positive | Negative pivot at index 1 |
| Odd | 256 | 512 | 1024 | 0.4970 | All 256 pivots positive | Negative pivot at index 18 |
| Odd | 512 | 1024 | 2048 | 1.1900 | All 512 pivots positive | All 512 pivots positive |

The old unweighted theorem gives Gamma>1.5867 in the first row and Gamma>0.0148 in the second. The independently proved cosh-weighted prime bound gives Gamma>0.4970758664 at N=256 and Gamma>1.1907506685 at N=512, so the last two rounded constants are conservative.

The even corrected LDL minimum pivot is approximately 9.3222311e-9. The successful odd corrected minimum pivot is approximately 9.7029019e-8. **A minimum LDL pivot is not a lower eigenvalue bound**: these matrices have extremely small eigenvalues and ill-conditioned triangular factors. No spectral-gap claim is inferred from these pivot magnitudes.

The N=256 odd budget with Gamma=.4970 has a float64 smallest eigenvalue near -1.9644e-12, consistent with the rigorous negative interval pivot. By contrast, successful finite matrices produce spurious float64 negative eigenvalues around 1e-15; these signs are contradicted by interval LDL and must not be interpreted as spectral evidence. The exact interval computations, not the double-precision diagonalization, decide the displayed signs.

A sensitivity check at odd N=256 found finite S_J positive when Gamma=1. This does **not** supply a certificate, because no such coercivity constant has been proved at that cutoff. It merely explains why the stronger N=512 tail estimate is useful. Results are in `pilot_gamma_sensitivity_odd.json`.

## Completion of the infinite residual step

The parent certifier `certify_infinite_schur.py` uses the proved moment-preserving enclosure from `directional_tail_derivation.md` on the lifted columns G=[I;-Z]. It freezes Z to exact dyadic midpoints, restores the full expression F-B^*Z-Z^*B+Z^*TZ, and explicitly charges the finite intermediate residual. It also uses the stronger diagonal lower bound T>=diag(g(n)) rather than replacing every g(n) by its minimum Gamma_N. Inverse order bounds the near residual contribution by the rowwise weights 1/g(n), and the remote Gram by 1/g(J+1).

Complete interval certificates then passed:

| Sector | N | M | J | Expansion order r | Positive LDL pivots |
|---|---:|---:|---:|---:|---:|
| Even | 256 | 512 | 4096 | 80 | 257 |
| Odd | 512 | 1024 | 4096 | 100 | 512 |

The odd calculation includes the whole infinite remote tail with geometric-remainder coefficient bounded near 3.2874201e-124. Its smallest interval LDL pivot is approximately 9.6802634e-8, again not a lower eigenvalue bound. Its frozen lift witness has uncompressed SHA-256 `4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea`. The scalar-Gamma odd N512/M1024/J2048 run and the diagonal odd N256/M512/J4096 run failed; these failures are retained in separate JSON outputs.

Under the proved canonical operator/core, exact assembly, weighted-prime, archimedean/pole tail, and residual-moment identities, the two successful certificates establish strict positivity of the complete fixed-window Weil operator at lambda=3. No omitted Fourier modes remain in this particular sign calculation. The ground-state parity, simplicity, and quantitative spectral ordering are separate refinements unless independently certified.

This fixed-window result does not establish the uniform growing-window estimates or G2/RH. A concrete further refinement is to run shifted certificates for W-aI: positivity in the odd sector and a one-negative-direction lower bound in the even sector, combined with an existing even trial quotient below a, would certify the actual fixed-window ground-state ordering.

## Files

- `pilot_schur.py`: reproducible finite-output computation.
- `pilot_N256_M512_J1024_even.json`: positive even pilot.
- `pilot_N256_M512_J1024_odd.json`: failed odd pilot with old Gamma.
- `pilot_improved_gamma_odd.json`: failed odd pilot with weighted Gamma=.4970.
- `pilot_N512_M1024_J2048_odd.json`: positive odd larger pilot.
- `weil_sequences_n1024_b768_k128.json` and `weil_sequences_n2048_b768_k128.json`: reusable rigorous sequence enclosures.
- `assembly_independent_overlap.json`: independent entry comparison.

All failed bounds are retained as research evidence; none are claims that the actual Weil operator has a negative direction.
