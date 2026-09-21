from pathlib import Path
import re
b=Path(__file__).resolve().parent
old=b.parent/'g2_schur_directional'
s=(old/'fixed_space_prime_action_v1.tex').read_text()
t=s.replace('v1.16','v1.17').replace('version 1.16','version 1.17')
t=t.replace('This does not identify\nthe lowest eigenspace or control a growing source block.', 'These asymptotic estimates do not by themselves identify\nthe lowest eigenspace or control a growing source block.')
a=t.index('A bounded discrete-Hilbert commutator identifies')
z=t.index('\\end{abstract}',a)
t=t[:a]+r'''A bounded discrete-Hilbert commutator identifies the canonical
semilocal Weil operator and Fourier core. Arithmetic tail estimates,
exact dyadic witnesses and interval Schur certificates prove complete
positivity at $\lambda=3$. Shifted certificates now prove a simple even
ground state, a spectral gap and an ordinary overlap bound for the exact
projected source at that window. The proof includes both parity sectors
and the entire Fourier complement. It supplies no growing-window lower
estimate or ground-state endpoint comparison.
G2 remains open; no RH proof is claimed.
'''+t[z:]
a=t.index('Version 1.16 closes')
z=t.index('\\paragraph{Reading conventions.}',a)
t=t[:a]+r'''Version 1.17 proves a simple even ground state of the complete
operator at $\lambda=3$, with $0<\mu_0<3.644\cdot10^{-38}$ and
$\mu_1>10^{-36}$. The sine of the ordinary angle between that ground
state and the exact normalized $P_{64}p_3$ is less than $0.01931$.
Both shifted certificates pass independent higher-precision replays.
These fixed-window results do not supply the growing-window estimate
needed for G2. The physical endpoint, corrected sampler graph defect
and all 72 historical dispositions are preserved.

'''+t[z:]
a=t.index('This closes the signed head/complement obligation at this one window.')
z=t.index('Let\n\\[\n \\mathcal V_\\lambda',a)
insert=(b/'ground_order_proof_draft.tex').read_text()
insert=insert.replace('The fixed-window positivity certificate can be shifted to count its low','The fixed-window computer-assisted positivity certificate can be shifted to count its low')
insert=insert.replace('$G=I-Z$ is unchanged.',r'$G=\binom{I_{\rm head}}{-Z}$ is unchanged.')
insert=insert.replace('witnesses, every pivot enclosure and all shifted residual rows are\nrecorded by \\texttt{certify\\_shifted\\_inertia.py}.',r'''witnesses and every pivot enclosure are retained in the bundle;
\texttt{certify\_shifted\_inertia.py} recomputes all shifted residual rows.
The exact parameters are those of Proposition~\ref{prop:v116-window-positive}:
$(N,M,J,r)=(256,512,4096,80)$ for the even sector and
$(512,1024,4096,100)$ for the odd sector. Both certificates pass
at 768 bits and again at 896 bits using identical dyadic witnesses.''')
insert=insert.replace('finite-supported candidate.  More precisely, in the $N=64$ certificate\nwrite',r'''finite-supported candidate of
Proposition~\ref{prop:v112-finite-certificate}. More precisely, in that
$N=64$ certificate let $u$ be its normalized even vector, let $Q$ project
onto its even orthogonal complement. Set
$W_{64}=P_{64}\mathsf W_3P_{64}$, $\alpha=\ip{W_{64}u}{u}$,
$C=QW_{64}Q$ on that complement, and $r=QW_{64}u$. Write''')
insert=insert.replace('By finite-dimensional min--max,',r'By finite-dimensional min--max (see also \cite[Section~4.3]{Teschl2009}),')
insert=insert.replace('The normalized exact projected source differs by less than\n$4\\,10^{-36}$, which fits within the final margin.',r'''For the unnormalized rational candidate $c$,
Proposition~\ref{prop:v113-source-certificate} gives
$\|P_{64}p_3-c\|<\varepsilon:=2.60\cdot10^{-36}$, while the
exact rational norm calculation gives $\|c\|>0.65172555$.
Writing $\rho=\varepsilon/\|c\|$, elementary ball geometry yields
\[
 \left\|\frac{P_{64}p_3}{\|P_{64}p_3\|}-\frac c{\|c\|}\right\|^2
 \le\frac{2\rho^2}{1+\sqrt{1-\rho^2}}<(4\cdot10^{-36})^2.
\]
Indeed the real inner product of these two unit vectors is positive
and at least $\sqrt{1-\rho^2}$, by minimizing the squared distance
from $c$ along the positive ray through $P_{64}p_3$.
This normalization error fits within the final margin.''')
insert=insert[:insert.index('This proves parity, simplicity and quantitative ordinary overlap at one')]+r'''This proves parity, simplicity and quantitative ordinary overlap at one
fixed window. It does not identify the unprojected source with the
ground vector. There is still no uniform family of spectral thresholds
or source overlap estimates along unbounded windows. Endpoint stability,
the existing sampler graph defect and full-strip transfer requirements
remain separate; G2 and RH are not closed by this result.

'''
insert=insert.replace(r'\,10',r'\cdot10')
(b/'ground_order_insert.tex').write_text(insert)
t=t[:a]+insert+t[z:]
a=t.index('The remaining G2 spectral task is a lower bound tending to zero along')
z=t.index('\\paragraph{What is established by the sampler correction.}',a)
t=t[:a]+r'''Proposition~\ref{prop:v117-ground-order} now proves that the complete
operator at this window has a simple even ground, with
$0<\mu_0<3.644\cdot10^{-38}$ and $\mu_1>10^{-36}$.
Corollary~\ref{cor:v117-ground-overlap} bounds the ordinary sine angle
of the exact normalized $P_{64}p_3$ by $0.01931$. The stronger
$10^{-34}$ threshold for all other even states is essential here.
The earlier $N=64$ finite-matrix angle bound and this complete-operator
bound are different statements.

The remaining G2 spectral task is a lower bound tending to zero along
unbounded windows, or sufficient quantitative source-to-ground overlap
on such a family. One fixed-window certificate does not establish either.
The next test should transport the complete inverse-action certificate
to a larger physical window, track the arithmetic constants and remote
moments, and determine whether a bounded block of low modes admits a
uniform error budget. An ordinary small residual is still insufficient
when the competing levels collapse. Endpoint stability for a
source-to-ground comparison, the sampler graph defect and full-strip
normalization remain separate obligations. The fixed-window ground
ordering is now proved; G2 and RH remain open.


'''+t[z:]
t=t.replace('''The successful result certifies complete fixed-window positivity.
It does not report a numerical lower eigenvalue, a simple ground state,
an exact source-to-ground endpoint comparison, or a bound for unbounded
windows.''', '''The unshifted result certifies complete fixed-window positivity.
The shifted extension below also establishes ground-state ordering.
Neither result supplies an exact source-to-ground endpoint comparison
or a bound for unbounded windows.''')
needle='\\section{Integration ledger for the complete previous manuscript}'
extra=r'''\subsection*{Shifted inertia and complete ground-overlap reproduction}
Proposition~\ref{prop:v117-ground-order} uses
\texttt{g2\_ground\_order/certify\_shifted\_inertia.py} with
$\texttt{shift}=10^{-34}$ in the even sector and $10^{-36}$ in the
odd sector. The bundle retains the signed pivot reports at 768 and
896 bits. It reuses the unchanged exact witnesses from
\texttt{g2\_schur\_directional}; their identity is checked by hash.
The script shifts both the actual logarithmic diagonal and all inverse
comparison weights, recomputes the middle residual and retains the
full remote moment bound. A negative lower-matrix pivot is not itself
a negative direction of the complete operator: the proved trial quotient
supplies that direction for the shifted even operator.

The separate \texttt{certify\_trial\_reuse.py} checks the exact rational
trial's full-form Rayleigh quotient, constructs the finite-supported
correction and imports the proved exact-source error from
Proposition~\ref{prop:v113-source-certificate}. Its corrected Rayleigh
enclosure is contained in
\[
 (3.64339965699233062,3.64339965699233064)\cdot10^{-38}.
\]
The separate scalar script also verifies the conservative constants
displayed in the theorem.
The complete ground-overlap conclusion uses the independently proved
even-sector spectral threshold. It does not reuse the finite matrix's
gap as if it were a gap for the complete operator.
All reproducibility commands and unsuccessful exploratory tests are
recorded separately in the guide and research log.

'''
assert needle in t
t=t.replace(needle,extra+needle,1)
if '\\bibitem{Teschl2009}' not in t:
    t=t.replace('\\end{thebibliography}',r'''\bibitem{Teschl2009}
G. Teschl, \emph{Mathematical Methods in Quantum Mechanics},
Graduate Studies in Mathematics 99, American Mathematical Society, 2009,
Section~4.3.
\url{https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf}.
\end{thebibliography}''')
oldlabels=set(re.findall(r'\\label\{([^}]+)\}',s))
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert oldlabels <= set(labels)
assert len(labels)==len(set(labels))
ledger=lambda x: re.findall(r'^\d+\.\d+ &.*$',x,re.M)
assert ledger(s)==ledger(t) and len(ledger(t))==72
(b/'fixed_space_prime_action_v1.tex').write_text(t)
print({'labels':len(labels),'retained_labels':len(oldlabels),'ledger_rows':len(ledger(t))})
