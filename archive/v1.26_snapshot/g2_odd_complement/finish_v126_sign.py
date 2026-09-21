from pathlib import Path
B=Path(__file__).resolve().parent;s=(B/'fixed_space_prime_action_v1.tex').read_text()
s=s.replace('A complete odd-complement certificate reduces a\nsufficient sign test to one direction, and the full form has the\nordinary lower bound $-10^{-43}I$ at this window. The odd sign\nremains open.', 'A complete odd-complement certificate and a repaired\nsingle direction now prove positivity of the entire form at\n$\\lambda=4$, with exact fixed-window error $\\varepsilon_4=0$.')
a=s.index('Version 1.26 proves');b=s.index('\\paragraph{Reading conventions.}',a)
s=s[:a]+r'''Version 1.26 proves positivity of the complete Weil form at $\lambda=4$.
A complete $15$-dimensional complement certificate, a repaired odd
trial supported through $8192$, and a sharp matrix inequality close
the remaining odd-sector sign. The frozen directional witness is
verified at $1024$ and $1280$ bits with every omitted Fourier row
bounded. Together with the previous even certificate this gives the
exact fixed-window error $\varepsilon_4=0$, not a cofinal estimate.
Weak G1, all 72 historical dispositions, the physical endpoint and
the explicit sampler graph defect are retained. The independent
arithmetic estimate as $\lambda\to\infty$ remains open;
G2 and RH are not proved.

'''+s[b:]
s=s.replace('even sector; the odd sector remains open. It is not the raw finite', 'even sector; Proposition~\\ref{prop:v126-full-window} completes the\nodd sector. It is not the raw finite')
s=s.replace('The later simultaneous certificate proves the even-sector sign\nat $\\lambda=4$; the odd-sector sign remains open.', 'The later simultaneous and directional-complement certificates\nprove both parity signs at $\\lambda=4$.')
s=s.replace('The odd sign and the corresponding growing-window\nhead/inverse estimates remain unproved;', 'The complete odd sign is established below, while the corresponding\ngrowing-window head/inverse estimates remain unproved;')
s=s.replace('The analogous odd-head bounds tested here are inconclusive.  The\nexact statement established so far is positivity of the complete\neven sector at $\\lambda=4$; it is not yet\n$\\mathsf W_4\\succeq0$ on both sectors.  No finite list of such\nfixed-window statements implies the cofinal estimate needed for RH.', 'The analogous initial odd-head bounds are inconclusive. The next\nsubsection completes the odd sector by combining a complete\ncomplement certificate with a larger-support directional trial.\nNo finite list of such fixed-window statements implies the cofinal\nestimate needed for RH.')
s=s.replace('\\subsection*{A complete complement bound and a reduced odd-sector target}', '\\subsection*{A complete complement bound and the full sign at $\\lambda=4$}')
s=s.replace('\\begin{proposition}[Complete odd complement and ordinary lower error]', '\\begin{proposition}[Complete odd complement]')
a=s.index('Independently, in the original ordinary Hilbert norm,',s.index('\\label{prop:v126-odd-complement}'));b=s.index('\\end{proposition}',a)
s=s[:a]+'''This is a complete inverse-correction estimate on the indicated
subspace, with every omitted Fourier row retained.
'''+s[b:]
a=s.index('A separate interval $LDL^*$ test, now with',s.index('\\label{prop:v126-odd-complement}'));b=s.index('\\end{proof}',a)
s=s[:a]+s[b:]
a=s.index('For this $v$, one may now seek a different finite trial');b=s.index('\\subsection*{What the present diagonal majorant costs',a)
s=s[:a]+r'''\begin{proposition}[Complete positivity at $\lambda=4$]
\label{prop:v126-full-window}
The canonical complete Weil form $\mathsf W_4$ is strictly positive
on every nonzero vector in its form domain and is bounded below
by a positive constant at this fixed window. In particular its
nonnegative-error formulation has $\varepsilon_4=0$ exactly.
\end{proposition}
\begin{proof}[A larger-support directional certificate]
Keep $G_0,K,V,v$ and the complete odd tail $T$ from
Proposition~\ref{prop:v126-odd-complement}; put $a=v^*Kv$.
The archived exact dyadic odd trial $f$ has support through $8192$
and physical head exactly $Vv$. Thus, with $r_f=Q_{16}\mathsf W_4f$,
\[
 S(v,v)=QW_4(f,f)-\ip{T^{-1}r_f}{r_f},\qquad S=K-\mathcal C.
\]
This identity uses the same complete Schur form and the old
normalization $a$, although the finite trial has changed.

The same physical diagonal, inner certificate, $J=65536$ and
order-$64$ remote moment give the following conservative outward
intervals, reproduced at $1024$ and $1280$ bits on the same frozen
witness:
\begin{center}
\begin{tabular}{ll}
\toprule
quantity & enclosing interval\\
\midrule
$a$ & $(1,\ 1.000000000000002)$\\
$QW_4(f,f)$ & $(0.9016760830,\ 0.9016760831)$\\
finite far energy upper $V_f$ & $(0.3125027254,\ 0.3125027255)$\\
remote source majorant $E_f$ & $(0.0608540372,\ 0.0608540373)$\\
finite mixed squared norm $H_f$ & $(0.0701478147,\ 0.0701478148)$\\
complete correction upper $U_f$ & $(0.4725352935,\ 0.4725352936)$\\
$(QW_4(f,f)-U_f)/a$ & $(0.4291407894,\ 0.4291407895)$\\
\bottomrule
\end{tabular}
\end{center}
Here $\mu=0.9999999999$ and
$0.0412001510<\rho<0.0412001511$ are the certified odd inner
constants. Proposition~\ref{prop:v125-simultaneous}, or its scalar
Cauchy--Schwarz form, gives
\[
 \ip{T^{-1}r_f}{r_f}\le U_f
 :=V_f+E_f+\mu^{-1}
          \bigl(\sqrt{H_f}+\sqrt{\rho E_f}\bigr)^2.
\]
The bound includes every row past $J$, not only the finite residual.
The verifier checks exact equality of all physical head coefficients,
provenance of the frozen inner factors, and eight independently
assembled rows of the unshifted physical operator. The physical
head equality is also checked with independent exact rational
arithmetic; its largest dyadic mantissa has $912$ bits. The finite
proposal method supplies no hypothesis about its convergence.

The outward directional inequality proves
$S(v,v)\ge(429/1000)a$. Combining it with
\eqref{eq:v126-complement} in
Proposition~\ref{prop:v126-direction-complement} yields the
simultaneous odd-head estimate
\begin{equation}\label{eq:v126-odd-relative-margin}
 S\succeq\frac{428}{1000}K\succ0.
\end{equation}
Since $V$ is invertible and the complete tail is coercive,
square completion proves positivity of the entire odd form.
The triangular change is bounded with bounded inverse, so the
finite positive head and coercive tail also give a positive
ordinary lower constant at this fixed window. The orthogonal
parity decomposition and Proposition~\ref{prop:v125-even-complete}
prove the full claim. The relative constant $428/1000$ is not
an ordinary spectral-gap estimate, and no congruence factor is
needed to pass the exact sign $\varepsilon_4=0$.
\end{proof}

The reduced directional argument closes this fixed-window obligation.
It gives no bound for the heads, inverse factors or residuals at
unbounded $\lambda$. In particular, the constants above are tied
to $L=2\log4$ and are not transferred to other windows.

'''+s[b:]
s=s.replace('The $16$-dimensional odd sector is still a fixed-window target.\nProposition~\\ref{prop:v126-odd-complement} bounds its complete\ncorrection on a $15$-dimensional complement and proves the full\nordinary lower error $10^{-43}$ at this window. The sufficient\nremaining directional test is given by\nProposition~\\ref{prop:v126-direction-complement}.', 'Proposition~\\ref{prop:v126-full-window} now completes the\n$16$-dimensional odd sector and proves $\\varepsilon_4=0$.\nThe remaining target is complete ordinary-error control along an\nunbounded window family, not another finite compression at this\nalready certified window.')
s=s.replace('complete Gram bound. The odd complete-complement certificate\nand ordinary bound $\\mathsf W_4\\succeq-10^{-43}I$ sharpen the\nremaining fixed-window target. The attempted odd sign bounds remain\ninconclusive; they do not give a negative Weil vector.', 'complete Gram bound. Proposition~\\ref{prop:v126-full-window}\ncompletes the odd sector by a different finite trial in one\ncertified direction and the whole complementary bound. Thus\n$\\mathsf W_4\\succeq0$ exactly at this window.')
s=s.replace('The complete\neven sign at one window closes a local obligation, not G2 or RH.', 'The complete\nsign at one window closes a local obligation, not G2 or RH.')
s=s.replace('\\subsection*{Odd complement and ordinary-error certificates}', '\\subsection*{Odd complement and complete fixed-window sign}')
a=s.index('The proposed extra finite repairs are recorded',s.index('\\label{app:v126-complement}'));b=s.index('\\subsection*{Simultaneous even certificate',a)
s=s[:a]+r'''The script \texttt{directional\_tail\_repair.py} reconstructs the
same frozen $8192$-support directional trial at $1024$ and $1280$
bits and bounds its complete inverse correction. The success
certificate combines the exact rational thresholds $429/1000$
and $1/1000$ to give the relative matrix margin $428/1000$.
The physical head is checked both by outward dyadic arithmetic
and by a separate exact rational calculation. The additional
complement calculation at $896$ bits reuses the previously
certified $768$-bit ingredient enclosures; it is not represented
as a fresh evaluation of those ingredients.

The proof and implementations have been checked adversarially.
Earlier unsuccessful repairs, the intermediate ordinary error
$10^{-43}$, and the limits of these tests are retained in the
research log. No accuracy assumption for a suggested eigenvector
or convergence theorem for conjugate gradients is used. This
internal computer-assisted certificate does not constitute
independent external verification or a growing-window theorem.

'''+s[b:]
(B/'fixed_space_prime_action_v1.tex').write_text(s)
print('Integrated complete lambda4 sign into full v1.26')
