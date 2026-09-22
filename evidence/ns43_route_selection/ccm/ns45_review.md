# NS-45 bounded independent review

Disposition: **no MAJOR or MINOR finding within the assigned scope**. The fresh witness gates support failure of the specified lambda=5, N=25 signed-block norm-comparison criterion in both parities. They do not prove full block positive definiteness or a negative Weil direction.

Reviewed exact source hash for `evidence/ns45_block_replay/replay.py`:
`77aa0b462347380193594473504e0c299fe036ab813a7e4c1690f4300527435e`.

Frozen witnesses SHA256:
`2a8725849e1cb8b363bd0d79bdb07b1d0b17b22a856f0fdd01fb72145a1e1a64`.

Certificate SHA256:
`ee9b6a526ec79a6501f426957e847940d7052f0da39bb8c86690b7237aa19114`.

## Checked arguments

- **Dyadic proposal convention passes** (`replay.py:61-68`). With Tjj=Lj Lj^T and Tkk=Lk Lk^T, the proposed normalized cross matrix is Lj^-1 Tjk Lk^-T. Its singular vectors are returned to physical coordinates using Lj^-T and Lk^-T. Euclidean renormalization leaves the quotient invariant. Rounding to integer/2^60 produces exact dyadics; no proposal accuracy or optimality is a proof dependency.
- **Exact energy and cross gates pass** (`replay.py:120-142`). The verifier constructs the saved dyadics exactly as Arb balls. It strictly proves Ex>0, Ey>0, and cross^2-H^2 Ex Ey>0, with H>=0. These imply |cross|/sqrt(Ex Ey)>H; the square-root quotient gate is separately checked. No midpoint solve, Cholesky factor, or approximate eigenvalue occurs on this verification path.
- **Both signed-index parity embeddings pass** (`replay.py:85-102`). Coefficients x_n/√2 on +n and ±x_n/√2 on −n recover the even/odd parity block. The full signed matrix has diagonal d_|n| and off-diagonal (b_n-b_m)/(n-m), with b_-n=-b_n. Combining ± indices gives the same diagonal/off-diagonal terms and the correct ±(b_n+b_m)/(n+m) contribution. The odd real embedding differs from physical sine coefficients by a common unit complex phase, which cancels in the Hermitian pairing. The separate energy and squared-gap gates pass and all three pairings overlap. This independently checks the parity/index assembly, not the analytic coefficient derivation; the README states that limit correctly.
- **Metric dichotomy is sufficient** (`README.md`, “Why no full block inertia certificate is needed”; `replay.py:167`). If 0<Mj<=Tjj exists, then finite Tjj is positive definite and each verified positive-energy pair quotient is at most beta_jk(T). The analytic variational lemma gives beta_jk(M)>=beta_jk(T). If such metrics do not exist, the criterion's prerequisite fails. No unconditional full Tjj inertia assertion is needed or made.
- **The strict rational comparison obstruction passes** (`replay.py:156-161`). The zero-diagonal symmetric nonnegative H has entries (997,568,481)/1000 in the even sector and (997,484,612)/1000 in the odd sector. The exact quotient on (1,1,1) is 341/250 and 2093/1500, respectively, both greater than one. A hypothetical positive row weight with all weighted row sums below one would force H's spectral radius below one by diagonal similarity and the row-sum norm, a contradiction. Pair witnesses need not share a single physical direction. A fourth block is unnecessary; further norm terms cannot reduce these finite row sums.
- **Two fresh precisions pass** (`replay.py:31-41,111-112`). Each 320/448-bit run redirects the coefficient assembler to a newly created empty temporary cache, retaining its analytic K=96 remainder enclosure. No preexisting coefficient cache can satisfy this path. The exact witness set and rational H stay fixed across precision runs.

## Independent verifier replay

I imported the original script with bytecode writing disabled, copied only the frozen witnesses to a temporary output directory, redirected `OUT`, and called `verify()` without running `propose()`. The source files and author's output files were not overwritten. Both parity runs passed all gates at 320 and 448 bits; the resulting certificate was byte-for-byte identical to the archived certificate. All four reviewed author-file hashes were unchanged afterwards.

The replay transcript is [ns45_reviewer_replay.txt](ns45_reviewer_replay.txt). Its short displayed balls are rounded summaries; the byte-identical JSON contains the full outward interval strings. The smallest squared gap remains the even 02 pair, approximately 6.7932046559e-10, strictly positive at both precisions.

## Scope retained

This is new replacement evidence for the existing partition, not recovery of the original v1.28 witness files or certification of their historical six-entry tables. It concerns one norm-comparison criterion at the existing window and cutoff. It does not establish complete lambda=5 positivity/negativity, a global spectral gap, a new tail metric, another partition's failure, or any cofinal/G2/RH claim. No author file, manuscript, map, or board was edited by this review.
