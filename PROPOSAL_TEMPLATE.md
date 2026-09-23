# Proposal gate (fill in before claiming a task row)

Copy this block into the PR body or the task's `evidence/nsNNN/README.md`
**before** the row in `NEXT_STEPS.md` is claimed. A proposal that cannot
fill every field is not started. See `AGENTS.md` section "Proposal gate".

```
Proposal: <one sentence: what estimate, identity or construction>

Shared-input group: <one of the 14 ids in RESEARCH_MAP.md "Shared
  continuation inputs", e.g. WEIL-FLOOR, NB-GAIN, ZERO-GEOMETRY>
  or DISTINCT with the closest recorded node named.
Status of that group: <frozen / open; attempts so far: NS-..>

Arithmetic input beyond the functional equation:
  <what the argument uses that Davenport-Heilbronn does not have:
   Euler product, multiplicativity of coefficients, nonnegativity of
   Lambda(n), a specific prime-sum estimate, ... or NONE>
  If NONE: stop. The proposal is arithmetic-blind (AGENTS.md 3.5).

Control screen (run before any proof or certificate):
  Davenport-Heilbronn   controls/davenport_heilbronn.py   holds / fails / n.a.
  Log-concave order-2   evidence/ns100_reassessment       holds / fails / n.a.
  Reciprocal dilation   evidence/ns101_theta_factorization holds / fails / n.a.
  A candidate that HOLDS on a known-false analogue cannot imply RH as
  stated. Say what hypothesis it would need to add, or stop.

Wall check: <Known wall / Same open gap / Distinct test>
  Closest result: <NS/PR>
  What changes: <specific input or hypothesis, or explicitly nothing>

What success changes: <which group closes, or which prediction is tested>
What failure changes: <what gets recorded; frozen? closed?>

Budget: <hours / one PR>   Version bump expected: <no / yes because ...>
```
