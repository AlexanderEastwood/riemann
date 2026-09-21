from pathlib import Path
import re
b=Path(__file__).resolve().parent
s=(b/'current/fixed_space_prime_action_v1.tex').read_text()
t=s.replace('v1.18','v1.19').replace('version 1.18','version 1.19')
a=t.index('A bounded discrete-Hilbert commutator identifies')
z=t.index('\\end{abstract}',a)
t=t[:a]+r'''A bounded discrete-Hilbert commutator identifies the canonical
semilocal Weil operator. Signed Schur certificates prove complete
positivity, simple ground ordering and projected-source overlap at
$\lambda=3$. Every complete eigenfunction has zero physical endpoint,
with logarithmic boundary decay. A complementary-form reduction avoids
a small-gap division. However, no finite-dimensional source removal
reduces the unsigned prime norm, whose leading scale is exactly
$\lambda$. The growing-window signed estimate remains open;
no RH proof is claimed.
'''+t[z:]
a=t.index('Version 1.18 proves')
z=t.index('\\paragraph{Reading conventions.}',a)
t=t[:a]+r'''Version 1.19 proves that the prime norm survives every finite source
or Fourier-head removal and has asymptotic size $\lambda$.
This rules out a small unweighted complementary prime norm, not signed
Weil positivity. Weak G1, the fixed-window certificates, all 72 historical
dispositions and the sampler graph defect are retained. G2 remains open.

'''+t[z:]
needle='The time--frequency geometry suggests a canonical family of candidate projections'
assert needle in t
t=t.replace(needle,(b/'prime_norm_insert.tex').read_text()+'\n'+needle,1)
old=r'''This is exactly where unsigned prime-shift bounds cease to scale: the absolute arithmetic mass up to the active threshold $n\le e^{2a}$ is $\asymp e^a$, whereas the archimedean symbol grows only logarithmically in frequency.  Any scalable complement theorem must therefore retain signed arithmetic correlation; replacing the prime part by its operator norm reproduces the previously rejected doubly-exponential frequency cutoff.'''
new=r'''Propositions~\ref{prop:v119-prime-essential}--\ref{prop:v119-prime-scale}
make one limitation exact: finite source removal leaves the unsigned
prime norm unchanged, and that norm is $(1+o(1))e^a$.
Subtracting this scalar from the minimum archimedean tail diagonal
forces the expensive cutoff \eqref{eq:v119-unsigned-cutoff}.
This does not exclude a frequency-weighted or directional estimate;
the recurrence vectors restoring the prime norm may have much larger
archimedean energy than that minimum.'''
assert old in t
t=t.replace(old,new,1)
needle='The continuum endpoint is now settled by'
extra=r'''The unsigned-prime shortcut is now excluded by
Propositions~\ref{prop:v119-prime-essential}--\ref{prop:v119-prime-scale}:
every finite-dimensional source or Fourier-head removal retains the
full prime norm, asymptotic to $\lambda$. The rank-two pole term cannot
make their combined ordinary operator norm smaller either. The next
estimate must therefore use the archimedean energy, directional inverse
weights or signed correlations; enlarging a finite source block alone
cannot make that unweighted arithmetic norm small. This is an
obstruction to a sufficient norm bound, not to full Weil positivity.

'''
assert needle in t
t=t.replace(needle,extra+needle,1)
needle='\\section{Integration ledger for the complete previous manuscript}'
extra=r'''\subsection*{Prime norm recurrence and growing-window scale}
Propositions~\ref{prop:v119-prime-essential}--\ref{prop:v119-prime-scale}
are analytic. The archived proof and adverse review distinguish a
finite-codimension norm obstruction from the still-open signed estimate.
The script \texttt{check\_prime\_norm.py} checks the positive trial
$\phi=e^{-x/2}+e^{-(L-x)/2}$ using
\[
 \|\phi\|_2^2=2(1-\lambda^{-2})+2L/\lambda,
 \qquad
 C_\phi(s)=2e^{-s/2}(1-e^{-(L-s)})
             +2(L-s)\lambda^{-1}\cosh(s/2).
\]
Thus its prime Rayleigh quotient is
$2\sum_m w_m C_\phi(\log m)/\|\phi\|_2^2$.
Independent piecewise physical quadrature at $\lambda=2,3$ agrees
with the autocorrelation formula to below $10^{-50}$ at 60-decimal
precision. At $\lambda=300$ the trial quotient divided by $\lambda$
is approximately $1.026889$; this is illustrative, not a norm certificate
or an asymptotic proof.

The same script tests phase recurrence at $\lambda=2$. Modulation by
Fourier index $381074$ has normalized $P_{64}$ head norm about
$9.52\cdot10^{-13}$, while its prime Rayleigh quotient differs from
the unmodulated value by about $4.7\cdot10^{-14}$.
These floating-point checks illustrate the analytic mechanism only.
They give no negative complete-Weil direction, because the
archimedean logarithmic energy grows with the modulation frequency.

'''
assert needle in t
t=t.replace(needle,extra+needle,1)
bib=r'''\bibitem{NISTPrimeAsymptotics}
NIST Digital Library of Mathematical Functions, Section~27.12,
Asymptotic Formulas: Primes, prime number theorem and classical error
estimates. \url{https://dlmf.nist.gov/27.12}.

'''
t=t.replace('\\end{thebibliography}',bib+'\\end{thebibliography}',1)
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))
assert set(re.findall(r'\\label\{([^}]+)\}',s))<=set(labels)
ledger=lambda x:re.findall(r'^\d+\.\d+ &.*$',x,re.M)
assert ledger(t)==ledger(s) and len(ledger(t))==72
(b/'fixed_space_prime_action_v1.tex').write_text(t)
print('labels',len(labels),'ledger',len(ledger(t)))
