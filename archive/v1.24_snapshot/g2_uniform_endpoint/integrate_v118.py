from pathlib import Path
import re
b=Path(__file__).resolve().parent;old=b.parent/'g2_ground_order'
s=(old/'fixed_space_prime_action_v1.tex').read_text();t=s.replace('v1.17','v1.18').replace('version 1.17','version 1.18')
a=t.index('A bounded discrete-Hilbert commutator identifies');z=t.index('\\end{abstract}',a)
t=t[:a]+r'''A bounded discrete-Hilbert commutator identifies the canonical
semilocal Weil operator and Fourier core. Arithmetic tail estimates and
interval Schur certificates prove complete positivity, a simple even
ground state and projected-source overlap at $\lambda=3$.
An exact restricted logarithmic-Laplacian decomposition now proves that
every complete eigenfunction has continuous zero physical endpoint,
with inverse-square-root logarithmic boundary decay. Thus the source's
nonzero endpoint cannot be transferred to a continuum ground vector.
A complementary-form reduction avoids division by a small spectral gap,
but its growing-window arithmetic sign remains unproved.
G2 remains open; no RH proof is claimed.
'''+t[z:]
a=t.index('Version 1.17 proves');z=t.index('\\paragraph{Reading conventions.}',a)
t=t[:a]+r'''Version 1.18 proves the zero continuum endpoint and a fixed-window
filtered decay rate. Finite-compression endpoints remain separate.
The complement estimate leaves G2's growing-window sign open.
Weak G1, the certified $\lambda=3$ ordinary overlap, all 72 historical
dispositions and the sampler graph defect are retained.

'''+t[z:]
needle='Let\n\\[\n \\mathcal V_\\lambda:=\\operatorname{Var}(p_\\lambda)'
assert needle in t
endpoint=(b/'eigen_endpoint_insert.tex').read_text().replace('as in $V_n(x)=','as in $U_n(x)=')
graph=(b/'graph_trace_insert.tex').read_text()
t=t.replace(needle,endpoint+'\n'+graph+'\n'+needle,1)
oldscope='''or source overlap estimates along unbounded windows. Endpoint stability,
the existing sampler graph defect and full-strip transfer requirements
remain separate; G2 and RH are not closed by this result.'''
newscope='''or source overlap estimates along unbounded windows. The physical
endpoint is resolved below by a separate regularity argument; it does
not follow from this ordinary overlap bound. The sampler graph defect
and full-strip requirements remain separate; G2 and RH are not closed
by the fixed-window spectral result.'''
assert oldscope in t;t=t.replace(oldscope,newscope,1)
needle='The time--frequency geometry suggests a canonical family of candidate projections'
assert needle in t;t=t.replace(needle,(b/'gap_free_block_insert.tex').read_text()+'\n'+needle,1)
t=t.replace('''A valid G2 proof still needs a coercivity estimate''','''One sufficient G2 route seeks a coercivity estimate''',1)
t=t.replace('''(or a block estimate of equivalent strength) together with control of the couplings to the deep and plunge blocks.''','''together with control of the couplings to the deep and plunge blocks.
Proposition~\\ref{prop:v118-gap-free} gives an alternative: a uniform
operator residual on the removed block and asymptotic nonnegativity of
its whole complement suffice, without a strictly positive gap.''',1)
a=t.index('The remaining G2 spectral task is a lower bound tending to zero along');z=t.index('\\paragraph{What is established by the sampler correction.}',a)
t=t[:a]+r'''The remaining G2 spectral task is a complete lower bound tending to
zero along unbounded windows, or sufficient quantitative source-to-ground
overlap on such a family. This is RH-strength: by nested support domains,
even a cofinal sequence of complete lower bounds $-o(1)$ implies
nonnegativity of every compact test. A finite list of certified windows
cannot replace that estimate.
Proposition~\ref{prop:v118-gap-free} removes an unnecessary positive-gap
requirement from one route. The already proved rank-one source residual
reduces the target to asymptotic nonnegativity of its entire orthogonal
complement. A negative compact test would persist in that complement;
the required arithmetic sign is still unproved. Growing source blocks
also need an independent uniform operator-residual bound.

The continuum endpoint is now settled by
Theorem~\ref{thm:v118-eigen-endpoint-zero}: every complete eigenfunction
has continuous zero physical trace. Hence a nonzero endpoint comparison
to the repaired source is false, with exact relative mismatch one.
Corollary~\ref{cor:v118-ground-fejer} supplies a fixed-window filtered
endpoint-decay rate. It gives no sharp-cut or joint growing-window rate
for finite-compression ground vectors. Those finite endpoint estimates,
the sampler graph defect and full-strip normalization remain separate.
The next spectral work should retain these distinctions while seeking
an independent signed complementary lower bound, rather than imposing
a nonzero continuum ground trace. G2 and RH remain open.


'''+t[z:]
t=t.replace('''Neither result supplies an exact source-to-ground endpoint comparison
or a bound for unbounded windows.''','''Neither certificate alone supplies an endpoint comparison or a bound
for unbounded windows. The separate boundary theorem now determines
the continuum eigenfunction trace to be zero.''',1)
needle='\\section{Integration ledger for the complete previous manuscript}'
extra=r'''\subsection*{Analytic endpoint and complement checks}
The proof of Theorem~\ref{thm:v118-eigen-endpoint-zero} is analytic.
It does not use a numerical endpoint extrapolation. Its three gates are
the exact physical kernel identity with scalar $-\log(2\pi)$, a common
closed-form core, and the simultaneous $L^2/L^\infty$ resolvent argument
that makes the boundary theorem applicable. The archived independent
reviews check each gate, the retained pole signs and the distinction
between a restricted logarithmic Laplacian and a spectral logarithm.
The script \texttt{check\_log\_kernel\_normalization.py} independently
compares the original and decomposed constant-mode archimedean diagonal
at $\lambda=1.2,2,3,10$, with 90-decimal working precision. Agreement is
a diagnostic only; the scalar integral in the proof establishes the
normalization exactly.

The Fej\'er bound retains the physical $L^{-1/2}$ Fourier factor and
uses a positive kernel of total mass one. It does not replace the
paper's literal Fourier cutoff in any earlier formula.
Proposition~\ref{prop:v118-graph-trace} explicitly shows why graph
convergence does not transfer the physical trace.
The complement estimate in Proposition~\ref{prop:v118-gap-free}
is an exact Hilbert-space inequality with a sharp two-dimensional
example. Its use of the rank-one source invokes the proved ordinary
operator residual; its arithmetic complementary-sign hypothesis remains
open. These checks close the continuum endpoint question and improve
the formulation of the growing-window target, without closing G2.

'''
t=t.replace(needle,extra+needle,1)
t=t.replace('\\end{thebibliography}',(b/'endpoint_bibitems.tex').read_text()+'\n\\end{thebibliography}')
oldlabels=set(re.findall(r'\\label\{([^}]+)\}',s));labels=re.findall(r'\\label\{([^}]+)\}',t)
assert oldlabels<=set(labels) and len(labels)==len(set(labels))
ledger=lambda x:re.findall(r'^\d+\.\d+ &.*$',x,re.M)
assert ledger(s)==ledger(t) and len(ledger(t))==72
(b/'fixed_space_prime_action_v1.tex').write_text(t)
print({'labels':len(labels),'oldlabels':len(oldlabels),'ledger':len(ledger(t))})
