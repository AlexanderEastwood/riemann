# Independent fixed beta certificate — sealed 2026-09-30

**Wall check: Same open gap.** Closest result NS38 and manuscript proposition `prop:v132-global-index`. This is a replacement validation of its fixed numerical premise, not a new candidate, arithmetic estimate or RH route. Success supplies new evidence for the stated full-line multiplier argument only. RH, G2, the cofinal signed floor, and NB gain inputs stay open. Both missing historical-original evidence groups remain OPEN.

## Source review and independence

The coordinator refreshed public origin to `769359298fada57711b6895c4bde3fabe2cc5168`. I read the isolated worktree's AGENTS, conclusion register and continuation demands, README/checkpoint and NEXT_STEPS context, evidence/MISSING, and the source formula/proposition. This is a conclusions/dependency review and this single numerical replay, not a replay of historical proofs. I did not read `certificate/01-direct` before deriving, implementing and sealing this result. No manuscript, register, global configuration, or other worker's files were modified.

The source at `manuscript/fixed_space_prime_action_v1.tex`, equations `eq:v130-r-symbol`, `eq:v130-beta`, gives, at a=log(4), xi=1:

    beta = Re psi(5/4 + i/2) - log(pi)
           - 2 sum_{1<m<16} Lambda(m)/sqrt(m) cos(log(m))
           + 2 integral_0^log(16) exp(t/2) cos(t) dt.

The strict finite cutoff contributes exactly

    (m, prime base) = (2,2), (3,3), (4,2), (5,5), (7,7),
                      (8,2), (9,3), (11,11), (13,13).

Lambda(p^j)=log(p), not log(p^j). The integer 16 is excluded. The script independently enumerates these powers with exact integers and checks the list.

## Digamma enclosure without a digamma call

Use the convergent partial-fraction series in [NIST DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6). For a=5/4 and b=1/2 its real part is

    Re psi(a+ib) = -gamma + sum_{k=0}^infinity f(k),
    f(x) = 1/(x+1) - (x+a)/((x+a)^2+b^2)
         = (a-1)/((x+1)(x+a))
           + b^2/((x+a)((x+a)^2+b^2)).

Both terms in the last expression are positive and decreasing for x>=0. Therefore, after summing k=0,...,K-1,

    I_K <= sum_{k=K}^infinity f(k) <= I_K + f(K),
    I_K = integral_K^infinity f(x) dx
        = (1/2) log((K+a)^2+b^2) - log(K+1).

This is a proved outward tail bound, not agreement of two approximate truncations. We fix K=1024 before the replay. Arb `union` encloses the two endpoints and every intervening value; no midpoint is extracted for subsequent arithmetic.

Euler's constant is also independently enclosed without `const_euler` or another gamma-related function. Write h_M=H_M-log(M), with gamma=lim h_M. For N>M,

    h_M-h_N = sum_{k=M+1}^N [log(k/(k-1)) - 1/k].

Each summand is positive and less than 1/(k-1)-1/k, by integrating 1/x over [k-1,k]. Taking the limit yields

    h_M - 1/M < gamma < h_M.

The certificate fixes M=4096. This deliberately elementary bound supplies most of the final interval width. Increasing working precision does not remove that analytic remainder.

## Independent continuum integral

Let c=1/2+i, L=log(16), |c|=sqrt(5)/2. Termwise integration of the entire exponential series gives

    integral_0^L exp(t/2)cos(t) dt
       = sum_{k=0}^infinity Re(c^k) L^(k+1)/(k+1)!.

The first K=40 terms are evaluated with a real two-component recurrence for c^k. For the omitted terms, their absolute values are bounded by

    T_k = L (|c| L)^k/(k+1)!.

For k>=K, T_(k+1)/T_k <= q=|c|L/(K+2)<1. Hence the absolute remainder is at most

    E = T_K/(1-q).

The script verifies q<1 with balls and adds the whole interval [-E,E] outward. Both precision runs give E<4.04×10^-30. This method is independent of an antiderivative or numerical quadrature. The integral itself lies in the printed ball around −0.73810223273233490520623727614187.

## Result and replay

`certify_series.py` uses python-flint 0.9.0, fixed analytic cutoffs above and elementary Arb operations at **128 and 256 bits**. It uses no digamma, gamma, polygamma, zeta, or Euler-constant function. Logs, cosine, square roots and pi are the library's outward elementary operations; independence is in the mathematical evaluation path, not a second arithmetic backend.

Both complete replays enclose

    −0.640150 < beta_(log 4)(1) < −0.639904 < −3/5.

The full saved endpoint balls are in `certificate.json`. In particular, the entire computed ball is strictly above −0.64784909 and strictly below −0.6321938. Thus the proposition's reported historical coarse enclosure is confirmed by this fresh, independent calculation. No contradiction was found.

Replay from the repository root:

    .venv/bin/python audits/bounds-six-agent-2026-09-30-v1/certificate/02-independent/certify_series.py
    pyright --project audits/bounds-six-agent-2026-09-30-v1/certificate/02-independent/pyrightconfig.json

CLI pyright is the scoped fallback because no callable LSP tool is present in this session. Result: **0 errors, 0 warnings, 0 informations**. All touched Python functions are annotated. Source and script hashes, library version, per-term prime values, tail bounds, both precision records and all strict gates are saved. The owned pyright configuration points to the existing repository virtual environment and changes no global or primary config.

## What this changes and what it does not

Continuity of the real symbol gives a negative interval about xi=1. Even Fourier tests supported in disjoint symmetric subintervals there span negative subspaces of arbitrarily large dimension; finitely many linear constraints remove only finitely many dimensions. The numerical premise for that existing **full-line multiplier** implication is now supported by this fresh certificate.

Such tests are not compactly supported in the physical spatial interval (−log(4),log(4)). No physical-window negative direction follows; the already certified nonnegative lambda=4 form is consistent with this sign. No finite or cofinal RH positivity estimate is obtained. This certificate is newly generated replacement evidence: it does **not** recover `certify_beta4_negative.py` or any original output, and it does not close either missing-original group.

**Final classification: Same open gap; fixed existing-claim validation passed.**
