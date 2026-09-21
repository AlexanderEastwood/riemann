"""Rebuild the complete revision from the recovered authoritative v1.21."""
from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'input/fixed_space_prime_action_v1.tex').read_text()
s=s.replace('-- v1.21','-- v1.22').replace('manuscript, version 1.21','manuscript, version 1.22')
s=s.replace('Disposition in v1.21','Disposition in v1.22')
s=s.replace('residual correction open. Strong cancellation persists in the exact', 'residual correction open. Parity signs sharpen the complete inverse\niteration, with finite-prefix bounds retaining all remote rows.\nStrong cancellation persists in the exact')
start=s.index('Version 1.21 certifies');end=s.index('\\paragraph{Reading conventions.}',start)
s=s[:start]+r'''Version 1.22 sharpens the complete far-inverse bounds at $\lambda=4$
and proves finite-prefix estimates with all remote residuals included.
A certified far-energy comparison succeeds on one head direction;
the refined inverse must also enter the still-uncontrolled mixed term.
Local trial positivity remains certified, while the low Schur sign
$S_\infty=K_X-r^*T^{-1}r\succeq0$ is unresolved. Weak G1, all
72 historical dispositions, the physical endpoint and sampler graph
defect are retained. No G2 sign gap is closed; no RH proof is claimed.

'''+s[end:]
insert=(B/'inverse_refinement_insert.tex').read_text()
needle='\\begin{proposition}[Refining both terms of the structured inverse]'
assert insert.count(needle)==1
insert=insert.replace(needle,(B/'directional_gate_insert.tex').read_text()+needle)
needle='\\begin{proposition}[An ordinary-error target for growing windows]'
assert s.count(needle)==1;s=s.replace(needle,insert+'\n'+needle)
needle='Evaluating the signed powers and their complete remote\ncontributions, and proving the remaining low-head sign, are separate\nobligations.'
assert needle in s
s=s.replace(needle,'Proposition~\\ref{prop:v122-parity-inverse} below improves these\nconstants to $20$ and $90$ using the actual parity signs. Evaluating\nthe signed powers and their complete remote contributions, and\nproving the remaining low-head sign, remain separate obligations.')
needle='constants at $\\lambda=4$. Its signed polynomial evaluations are the\nnext concrete refinement of the low-mode correction.'
assert needle in s
s=s.replace(needle,r'''constants at $\lambda=4$, sharpened to $20$ and $90$ by
Proposition~\ref{prop:v122-parity-inverse}. The complete far energy
now fits below the trial budget on one certified head direction,
by Proposition~\ref{prop:v122-directional-far}. This is not the full
inverse correction. The next concrete target is to evaluate the
refined mixed term in \eqref{eq:v122-refined-structured}, enclosing
its remote correlations jointly, and then control the simultaneous
Gram on the entire head. Scalar direction bounds alone do not
establish that matrix comparison.''')
needle='\\subsection*{Finite trial positivity and exact-source cancellation audit}'
assert s.count(needle)==1
s=s.replace(needle,r'''\subsection*{Parity inverse refinement and its directional gate}
\label{app:v122-inverse}
The cumulative bundle's \texttt{g2\_inverse\_refinement} directory
contains \texttt{refine\_inverse.py}, both parity-constant interval
reports, both final directional-gate reports and the internal adverse
review. The constants replay at $320$ and $384$ bits; the directional
gate replays at $768$ and $896$ bits. The mathematical arguments of
Propositions~\ref{prop:v122-prefix-refinement} and
\ref{prop:v122-refined-structured} are independent of a numerical
positivity gate.

The exact direction uses the $17$ numerators and denominator $2^{160}$
from the archived \texttt{g2\_low\_schur} directory:
\begin{itemize}[nosep]
\item \nolinkurl{structured_ceiling_counterwitness.json} defines $v$;
\item \nolinkurl{low_witness_even_M256_b768.json.gz} defines the dyadic $X$.
\end{itemize}
These archived files define the inputs, not a new rounded eigenvector.
The actual matrix assembly retains its analytic archimedean-series
remainder and correct logarithmic diagonal.

For consecutive positive indices, four Arb polynomial products
evaluate the Toeplitz divided difference and the Hankel matrix action.
The first uses the convolution kernel $1/j$ for $j\ne0$, with zero
central coefficient, applied to $z_n$ and $b_nz_n$. The second
uses reversed input coefficients and the kernel $1/(n+m)$.
Thus the output is exactly
\[
 ((U_Jz)_n)=(d_n-ca_n)z_n+
 \sum_{m\ne n}\frac{b_n-b_m}{n-m}z_m+
 \sum_m\frac{b_n+b_m}{n+m}z_m
\]
in the even sector, including the opposite-sign contribution on its
parity diagonal. The polynomial products retain outward ball errors;
a dense $25$-row evaluation independently checks their indexing.
Only the computational method changes. The tail beyond $J=65536$
is still included by the complete moment bound and
\eqref{eq:v122-remote-H}. Earlier inconclusive cutoffs are retained
in the research log. No full mixed-term, matrix-head or G2 sign
certificate is asserted by this directional test.

'''+needle)
(B/'fixed_space_prime_action_v1.tex').write_text(s)
print('Complete v1.22 source integrated.')
