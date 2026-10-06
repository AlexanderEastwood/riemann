# Six-agent fixed-stencil quotient-PD screen

Baseline main0da30a5c92203e45c452df87b68a93d86b7e5fd7 (PR80).
Wall check: Distinct test. Closest PR78–80, NS100/101. Same original all-height signed estimate remains open.

User approved proposed test with six agents. EXACT stencil t_j=j/4,j=0,...,5; B_ij=k((i-j)/4), k=C/M with original complete theta M,C from PR78–80. No larger stencil, spacing variation, scan, pole search or adjacent test. Goal: one negative rational quadratic form would directly refute PD of k without requiring complex poles. This rejects that sufficient certificate only, not original L1[X], RH or G2. A finite PSD result is inconclusive for PD and ends this screening round.

Before ORIGINAL computations: filled PROPOSAL_TEMPLATE in draft PR body, matched controls, protocol review. Controls use same six-point matrix/pipeline: g(t)=exp(-t²) (positive); f(t)=exp(-t²)(1+t²) (entire and non-PD, per PR79). Original value computations wait for parent's go. Synthetic controls permitted now.

Budget: one hour diagnostic incl controls; one fixed rational witness, if convincingly negative, may receive at most two hours complete Arb validation (two precisions, all tails/quadrature/roundoff, no midpoint solves). Diagnostic eigendecomposition merely SELECTS a vector, never certifies it. No candidate => no certification. No row, thaw or manuscript version for screening/audit.

Original diagnostic: reuse archived theta_eval at t=0,1/4,...,5/4 using128/256bits,N24/32,GL48/96,R4/4.5; B=C/M after SAME normalization so it cancels. Check realness/M>0 samples and preserve all full-tail metadata. Matrix built from SIX unique k values. Independent replay same six arguments only. Numerical quadrature errors NOT certificates. Freeze rational-witness rule and threshold before original run.

Six roles in two waves: (1) matrix pipeline+controls, (2) original evaluation wrapper, (3) mathematical protocol, (4) independent direct-term quadrature, (5) code/result review, (6) adversarial final admission/certificate review. No child agents. Exclusive ownership. Workers are not alone: do not revert or modify others' files. No git/PR operations by agents. Parent owns integration and publication.
