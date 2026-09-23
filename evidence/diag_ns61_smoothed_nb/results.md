Numerical illustration only — these truncated series are not certificates.

This exploratory scan used Ehm's q=2 Gram formula with the S2 series stopped
after 512 or 1024 terms. It retained the complete old/new projection but did
not enclose the remaining series. The finite problem through index 32 was
computed at 60 digits/cutoff 512; the overlapping problem through index 64
was computed at 80 digits/cutoff 1024. Both precision and cutoff changed, so
agreement here alone is not a two-precision certificate.

The scan suggested that smoothing sharply improves the raw difference trace,
while the actual corrected numerator can still make the trace gain estimate
small. The complete interval replacement is in `../v159/ns61/`: it uses a
proved Bernoulli/Hurwitz tail, the same matrix at 256/384 bits, a separate
cutoff replay, and independent physical cell integrals. Only those interval
outputs support the manuscript's finite numerical statements.

The initial truncated values differ from the certified values in later
digits. No truncation result is represented as a bound or an asymptotic
observation. The small absolute q=2 errors are in a different fixed norm
from the original q=1 problem and are not evidence of RH convergence.
