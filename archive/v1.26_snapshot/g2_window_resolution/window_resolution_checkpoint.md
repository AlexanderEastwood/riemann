# Post-v1.25 window-resolution checkpoint — September 21, 2026

The released full manuscript remains v1.25 (166 pages). This checkpoint continues its finite-window investigation; it does not add a complete lambda8 sign certificate or prove G2/RH.

## Concrete question and result

Does the very small lambda8 margin disappear upon modestly enlarging the cutoff or reducing the head? **No, in the tested finite configurations.** The loss persists both at the next cutoff and with only the physical constant Fourier mode retained. It cannot be attributed solely to conditioning of multi-dimensional head coordinates.

All quantities below belong to the same unshifted physical lambda8 Weil form, the fixed normalized even Fourier basis and first-slot-linear convention. No operator, window or boundary functional is changed. Each eliminated finite tail and finite Schur head passes its own interval positivity gate. The arithmetic assembly was independently rederived in the adverse audit; the new computation increases the archimedean series from192 to256 terms and uses4096bits.

| Retained/test cutoff | Head | Certified generalized margin range (conservatively rounded) |
|---|---|---|
|256/384|0..64|5.697e-101 < m < 5.755e-101|
|384/512|0..64|1.349e-44 < m < 1.363e-44|
|256/384|0..36|1.155e-93 < m < 1.168e-93|
|256/384|physical constant mode0 only|9.5263e-42 < m < 9.5264e-42|
|384/512|physical constant mode0 only|1.4535e-14 < m < 1.4536e-14|

The first line reproduces the previous192-term coefficient calculation. The matrix brackets use a high-precision eigenvector only as a proposal. A verified invertible triangular congruence followed by interval LDL proves S_test−delta S_ret>0; an outward frozen-vector Rayleigh quotient proves the upper bound. Matrix witnesses and reports are saved. All modes above512 are absent from these experiments.

The constant-head energies are 3.2907912176941e-278 atcut256, 3.1349152424855e-319 atcut384 and4.5566952718104e-333 atcut512. They are certified finite minima with the constant coefficient fixed to1, not ordinary unit-vector eigenvalues. The first two values independently agree when obtained by shorting either the37-dimensional or65-dimensional finite head. A scalar normalizing congruence has condition1; although its absolute scale is large, its generalized margin is unaffected by that rescaling. The remaining eliminated operator can still be badly conditioned.

## Exact finite accounting

Let W_M>0 be nested compressions of one fixed Hermitian form, H a fixed finite head, and S_M^H its Schur complement. The variational identity is

    x* S_M^H x = min_y [x;y]* W_M [x;y].

Thus S_M decreases with M. For a retained tail T and newly added rows, write the larger block as

    [ F  B* C* ]
    [ B  T  D* ]
    [ C  D  U  ].

After eliminating the retained tail,

    R = C − D T^(-1)B,       A = U − D T^(-1)D* > 0,
    S_new = S_old − R* A^(-1)R.

The effective A is essential: replacing it by raw U discards the coupling. The generalized margin m(M1,M2)=min_{x!=0}(x*S_M2 x)/(x*S_M1 x) measures relative improvement/loss of positive finite trial energy. It is neither an absolute negative Weil error nor the complete residual correction.

For nested heads Hsmall subset Hbig, Schur-complement associativity, homogeneity and order preservation imply m_small >= m_big. A recovered small-head margin alone can move the fragile direction into the eliminated tail: A=I2 and B=diag(1,epsilon) have full-head margin epsilon, whereas eliminating the second coordinate gives margin1 and leaves a tail scale epsilon.

For fixed head and cuts M1<M2<M3, multiplying the inequalities gives

    m12*m23 <= m13 <= min(m12,m23).

These comparisons require a common window and common form. They cannot be used to order the lambda3,4,5,6,8 data across changing operators. A finite list of positive margins supplies no estimate for all subsequent cuts or a cofinal window family.

The constant-head shortcut follows from Schur inversion:

    S_M^{mode0} = 1 / [(S_M^{larger head})^(-1)]_{00}.

The script checks the larger Schur sign and evaluates this inverse column outward. It avoids solving another large tail problem and makes the head comparison exact.

## Source and adversarial checks

Primary sources consulted: Connes–Consani, Spectral triples and zeta-cycles (2023), https://alainconnes.org/wp-content/uploads/Spectral-triples-and-zeta-cycles_2021.pdf, Section2.5–3; and Weil positivity and trace formula, the archimedean place (2020), https://arxiv.org/pdf/2006.13771. Their discussion of tiny semilocal eigenvalues and prolate near-radical constructions is relevant context. Neither paper supplies the omitted complete growing-window certificate used here. No numerical conclusion is imported from those papers, and their window parameter conventions are not silently identified with this manuscript's L=2log(lambda).

The adverse review confirms the finite shorting identities, warns that head reduction can relocate inverse difficulty, and notes that probes expressed in different normalizing congruences cannot be compared directly. Future direction tracking must save their actual physical head vectors Vz. The main complete even lambda4 certificate from v1.25 is unchanged.

## Next concrete step

The newly tested cuts have not reached a stable relative finite energy. Before building a huge complete inner witness atlambda8, either extend the nested cutoff study with physical-direction tracking or construct source-adapted finite trials and compare their complete residuals. Any positive finite limit or apparent stabilization still needs a beyond-cutoff enclosure. The current scalar far method also retains its exponential cutoff cost. No G2 sign gap was closed by this checkpoint.
