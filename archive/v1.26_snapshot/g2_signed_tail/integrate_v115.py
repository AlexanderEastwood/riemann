from pathlib import Path
import re

b=Path(__file__).resolve().parent
old=b.parent/'g2_deep_next'
original=(old/'fixed_space_prime_action_v1.tex').read_text()
t=original.replace('v1.14','v1.15').replace('version 1.14','version 1.15')
t=t.replace('\\date{September 20, 2026}','\\date{September 21, 2026}')
start=t.index('\\begin{abstract}')
end=t.index('\\end{abstract}',start)
t=t[:start]+r'''\begin{abstract}
We study fixed-space prime actions on Burnol's Sonine quotients and
finite Weil forms. Source covariance, compact Mellin division and
Fredholm reduction identify arithmetic boundary and range defects.
For the repaired fixed-order prolate source, tail, endpoint, correlation
and domain estimates establish weak G1. Its ordinary polynomial
Fourier projection also recovers the physical endpoint and has an
exponentially small full operator residual. This does not identify
the lowest eigenspace or control a growing source block.

The corrected Hardy sampler combines centered periodization with an
endpoint shell. It preserves ordinary Gram and Weil-form limits and
the physical endpoint while retaining an explicit graph defect.
Reflected resolvent tests and sharp frequency cuts expose separate
endpoint and complex-strip obstructions. A finite-core metric criterion
bypasses the global arithmetic operator realization; a full-space
projection preserves strip-product bounds and Weil transfer, but its
remaining signed commutator is uncontrolled. An exact arithmetic
adjoint describes source orthogonality without supplying the missing
evaluator-shell sign.

A bounded discrete-Hilbert commutator identifies the canonical
semilocal Weil operator and Fourier core. Sharper prime, pole and
archimedean estimates give a positive omitted Fourier tail at
$\lambda=3$, $N=256$. The low-frequency Schur correction still
requires signed arithmetic control. Earlier finite matrix and
exact-source certificates are retained. G2 remains open;
no RH proof is claimed.
'''+t[end:]
start=t.index('Version 1.14 proves')
end=t.index('\\paragraph{Reading conventions.}',start)
t=t[:start]+r'''Version 1.15 proves an exponentially small ordinary operator residual
for the actual repaired source and its polynomial Fourier projection,
closing the separate Rayleigh and residual prerequisites. It sharpens
the positive omitted-tail bound to $N=256$ at $\lambda=3$.
The signed Schur estimate, quantitative ground-state overlap and
growing-window G2 remain open. The physical endpoint, corrected sampler
graph defect and all 72 historical dispositions are retained.

'''+t[end:]
needle='This is a quantitative omitted-tail theorem, not full Weil positivity.'
assert needle in t
t=t.replace(needle,(b/'sharp_tail_insert.tex').read_text()+'\n'+needle,1)
t=t.replace('With $Q_N=I-P_N$ and $\\Gamma_{\\lambda,N}>0$, write',
'''The sharper estimate may be used in its place. With $Q_N=I-P_N$
and $\\Gamma_{\\lambda,N}>0$ denoting either proved lower bound, write''',1)
start=t.index('bounding $B$ alone. For any $Z:E_N')
end=t.index('If the final finite lower bound is',start)
t=t[:start]+r'''bounding $B$ alone. For any $Z:E_N\to\mathcal D(T)$ put
$R=B-TZ$ and $K_Z=F-B^*Z-Z^*B+Z^*TZ$. Then
\begin{equation}\label{eq:v114-schur-residual}
 K=K_Z-R^*T^{-1}R
 \succeq K_Z-\Gamma_{\lambda,N}^{-1}R^*R
 \succeq K_Z-\frac{\|R\|^2}{\Gamma_{\lambda,N}}I.
\end{equation}
Expansion proves the identity and $T^{-1}\preceq\Gamma_{\lambda,N}^{-1}I$
proves both bounds. Retaining the residual Gram matrix $R^*R$ preserves
directional cancellation lost by its scalar-norm majorant.
'''+t[end:]
needle='\\subsection*{G2 calibration from the screw-function realization}'
assert needle in t
t=t.replace(needle,(b/'residual_insert.tex').read_text()+'\n'+needle,1)
start=t.index('The fixed-band G1 estimate does not test the form on the changing')
end=t.index('A quantitative spectral-overlap formulation',start)
t=t[:start]+r'''Weak fixed-band G1 alone does not test the form on the changing
proxy itself. The stronger operator estimate in
Proposition~\ref{prop:v115-absolute-residual} now supplies that missing
Rayleigh prerequisite for the actual normalized source and its literal
polynomial projection: $q_a(u_a,u_a)\to0$. Hence monotonicity gives
\[
 \lambda_a\to0\quad\Longleftrightarrow\quad
 \lambda_a\ge0\text{ for every finite }a.
\]
The forward implication uses only monotonicity; the reverse combines
positivity with the proved Rayleigh upper bound. The right side is the
compact-support Weil positivity criterion. The new source estimate
proves the upper bound, not positivity or the asserted limit of the
bottom level.

'''+t[end:]
start=t.index('Consequently, if separate operator-domain estimates supply')
end=t.index('This calibration is deliberately restrictive:',start)
t=t[:start]+r'''Proposition~\ref{prop:v115-absolute-residual} now proves both
$\alpha_a\to0$ and $\|r_a\|\to0$ for the normalized actual source,
with $\lambda=e^a$ and an upper envelope
\[
 \varepsilon_\lambda=C\lambda^6e^{-2\pi\lambda^2/3}.
\]
Therefore an independently proved overlap bound
$\kappa_a\ge\kappa_0>0$ would imply $\lambda_a\to0$ and close G2.
More generally it suffices that
$\varepsilon_\lambda/\kappa_a\to0$ along an unbounded sequence;
for example, $\kappa_a\ge e^{-\theta c}$ with fixed
$\theta<1/3$ and $c=2\pi\lambda^2$ would suffice.
No such lower bound is proved. If instead
$\lambda_a\le-\delta<0$, spectral projection of
$A_au_a$ gives $\delta\kappa_a\le\|A_au_a\|$.
Thus a negative ground state can coexist with the new residual estimate
by having exponentially small overlap with this source.

At small support Suzuki's positivity-improving analysis gives a simple
positive ground state, but it does not furnish a uniform large-support
overlap bound. Even positivity of both vectors would imply only a
nonzero overlap, without its required quantitative size. The model
$\operatorname{diag}(-1,\epsilon)$ with source $(0,1)$ shows directly
why a vanishing source residual does not determine the bottom sign.

'''+t[end:]
oldgoal='''Proposition~\\ref{prop:v114-weil-tail} supplies a positive
omitted Fourier tail at an explicit, but expensive, cutoff. The remaining
spectral task is the signed finite-core correction'''
newgoal=r'''Proposition~\ref{prop:v115-sharp-tail} sharpens the omitted-tail
estimate to $N=256$ at $\lambda=3$. Proposition~\ref{prop:v115-absolute-residual}
additionally proves a small full ordinary residual and Rayleigh value
for the actual source and its polynomial projection. It gives no
endpoint-normalized operator estimate and no lowest-state overlap.
The remaining spectral task is the signed finite-core correction'''
assert oldgoal in t
t=t.replace(oldgoal,newgoal,1)
t=t.replace('''a sufficiently strong source-to-ground approximation.
Several near-zero modes''','''a sufficiently strong source-to-ground overlap estimate. A concrete
fixed-window next step is an inverse-action certificate for the entire
$|n|\\le256$ head and its omitted complement; the earlier $N=64$
positive matrix alone is insufficient. A proof of G2 further needs a
lower error tending to zero along unbounded windows.
Several near-zero modes''',1)
needle='\\section{Integration ledger for the complete previous manuscript}'
extra=r'''\subsection*{Sharper tail certificate and ordinary residual scope}
The script \texttt{g2\_signed\_tail/check\_sharp\_tail\_constants.py}
evaluates the exact elementary constants of
Proposition~\ref{prop:v115-sharp-tail} with 256-bit Arb intervals.
Its output gives
\[
 \Gamma^{\rm all}_{3,256}>0.0148329,\qquad
 \Gamma^{\rm all}_{3,512}>0.7085077,\qquad
 \Gamma^{\rm even}_{3,256}>1.5867887.
\]
The interval arithmetic certifies these scalar evaluations of analytic
bounds. No new head matrix, inverse-action correction or full-window
positivity was certified. The ordinary residual theorem is an analytic
asymptotic estimate with no claimed effective threshold at $\lambda=3$.
It concerns the same exact source and literal Fourier projection as
the endpoint theorem. An independent internal adverse review checked
the norm normalization, low-output duality, high-output matrix bound,
graph tail, all scale factors and the remaining lack of ground overlap.

'''
t=t.replace(needle,extra+needle,1)
needle='\\end{thebibliography}'
t=t.replace(needle,r'''\bibitem{NISTDigamma}
NIST Digital Library of Mathematical Functions, Chapter 5,
equations 5.9.15 and 5.15.1 (Binet's digamma formula and trigamma series),
\url{https://dlmf.nist.gov/5.9.E15},
\url{https://dlmf.nist.gov/5.15.E1}.

'''+needle,1)
t=t.replace('\\begin{thebibliography}{99}\n\\small','\\begin{thebibliography}{99}\n\\small\n\\setlength{\\itemsep}{2pt}')
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))
assert t.count('\\section{')==34
def ledger(s):
    p=s.index('\\section{Integration ledger')
    return s[s.index('\\begin{longtable}',p):s.index('\\end{longtable}',p)]
assert ledger(t).replace('v1.15','v1.14')==ledger(original)
(b/'fixed_space_prime_action_v1.tex').write_text(t)
print('Integrated v1.15:',len(labels),'unique labels; 34 sections including appendices; historical ledger preserved.')
