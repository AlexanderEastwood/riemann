# NS-18 same-agent proof and provenance review

This is a reasoning and second-implementation review by the authoring agent,
not an external review or an independent-agent audit.

1. **Object and parity.** The new separator bounds the spectrum of the
   complete even restriction above its ground. The odd sector does not enter
   the error of an exactly even trial. The global ordering and ground parity
   remain the v1.40 theorem. The new 1e-67 threshold is not the global gap.
2. **Inertia.** The shifted lower form has 16 positive and one negative
   direction. A lower bound alone would not supply a negative direction for
   the exact form. The exact trial Rayleigh quotient below the shift does.
   This excludes a zero shifted eigenvalue as well: one negative direction
   plus a zero would contradict the at-most-one nonpositive index. The
   complete tail remains positive after the shift.
3. **Infinite tail.** The shift comparison is precisely v1.40's resolvent
   lemma. The inherited 768/896-bit residual Grams enclose every row after
   J=65536 and their small gates pass again. Neither a finite compression
   nor a finite residual replaces the complete operator. Original full
   assemblies are not rerun; dependency paths and byte hashes are recorded.
4. **Projection, not normalized-vector error.** Write f=h+e with
   h=P_ground f. Nonnegativity and the even separator give ||e||²<=rho/b.
   Since rho<b, h is nonzero and a scalar multiple of the ground. Comparing
   f to an arbitrarily normalized ground with this same bound would be
   invalid; no such comparison is used. Signs refer to h, whose orientation
   is fixed by f. Zeros are independent of its scalar and Fourier convention.
5. **Functionals and derivatives.** On a length-L centered interval, the
   evaluation norms are sqrt(L) and sqrt(L³/12). All trial coefficients
   through 4096 enter the exact formula. No small coefficient is set to zero.
   The partial-fraction evaluations avoid every removable pole. A separate
   direct sinc formula retains the (-1)^n centered coefficient phase.
6. **Unique local zero.** Strict opposite signs prove existence. Eight
   covering interval derivative gates prove strict monotonicity and a
   nonzero derivative, hence uniqueness and simplicity. The direct formula
   repeats the derivative argument on 32 covering intervals. No claim is
   made about zeros outside this local interval, including earlier ones.
7. **Precision and serialization.** All new gates pass at 1024/1280 bits
   with the same trial and thresholds. Leading principal determinants
   independently reproduce the signed LDL negative count. Saved intervals
   are reparsed and preserve their sign gates; all key scalar enclosures
   overlap across precisions. The inherited residual data use their original
   two precision evaluations. No new cutoff or cutoff-limit claim is made.
8. **Bound versus object.** The old global separator yields transform error
   about 0.260823 and fails this endpoint sign test. This does not disprove a
   local zero or the underlying approximation. The even separator improves
   the error by 1000 and passes. The resulting width 0.2 still cannot decide
   the discrepancy's sign or certify the minute finite-compression values.
9. **Claims left open.** No uniform/cofinal estimate, G2, RH, publication
   readiness, complete zero enumeration, or tiny-discrepancy transfer is
   claimed. NS-1's two original missing-evidence groups remain OPEN.
