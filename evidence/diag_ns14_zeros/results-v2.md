Diagnostic correction, not a certificate; see the finite-compression certificate in `../v141/`.

# NS-14 correction — September 21, 2026, version 2

The original `results.md` and `zeros.py` are preserved as the historical run.
Their sinc-lattice conclusion is withdrawn because the script reconstructs
a different function from the matrix eigenvector.

The actual matrix uses unshifted Fourier modes on `[0,L]`, as stated in
`prop:v116-window-positive`. Moving their even combinations to `[-L/2,L/2]`
changes cosine coefficients from `v_n` to `(-1)^n v_n`. The old `xhat()`
uses `v_n` without that phase. It also rounds L to a float, stops at a small
coefficient, changes precision during evaluation, and replaces failed root
solves by scan-cell midpoints. These cannot certify zero positions.

For unshifted coefficients, the correct exact formula is

    ghat(z) = 2 sin(zL/2)/sqrt(L) [v_0/z + sqrt(2) sum_{n=1}^N v_n z/(z^2-omega_n^2)].

At a retained lattice point, its removable-pole value is

    ghat(omega_k) = sqrt(L/2) (-1)^k v_k.

A small nonzero coefficient does not make this value zero. Concentration of
90% of the coefficient mass in low modes does not control relative error
near transform zeros or imply that off-lattice zeros are absent.

NS-2 now reproduces CCM section 6 Figure 1 at the existing lambda=3, N=120
benchmark. All first eight published discrepancies match their rounding;
the first is approximately 1.582329697193127e-34. The new verifier uses Arb
assembly and isolated eigenpairs at 768/1024 bits, then interval signs and
a nonzero derivative to certify each proposed local root bracket. These
are finite-compression statements; see `prop:v141-ccm-lock` and its artifacts.

This run uses CCM's N=120, not the historical NS-14 N=256. It does not
silently substitute one cutoff for the other: the exact phase correction
applies to both, while the numerical certificate is only for N=120.
No certified claim about the complete-ground zero locations at lambda=3
or 4 follows. The old negative diagnostic conclusion supplies no evidence
against CCM step (b). Complete-ground transfer and cofinal convergence
remain open, as do G2 and RH. No new window was computed.
