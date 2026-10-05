# Four-coordinate explanation of the missing theta bound

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR76.**
Reviewed remote commit: 18d324703969b5bcc9aa94043cfd90a6e8211f34.

Open [the self-contained interactive HTML](theta-gap-4d-2026-10-05-v1.html)
locally in a browser. It displays the zero set of

```text
p = r^2+1/4
J(r,y,v,w) = p^2*(v^2-y*w)+2*(r^2-1/4)*y^2.
```

For the specific original trajectory, J=16*(X'^2-X*X'').
The missing requirement is J>=0 for every real height. First-Laguerre
positivity alone is not RH. The visualization adds no arithmetic input.

The four coordinates are independently adjustable illustrative local states.
No actual theta values or trajectory are evaluated. Motion rotates the
four-coordinate projection only. The displayed finite box, wire mesh, sign
examples and scale choices are not arithmetic evidence. The y=0 boundary
line is explicitly retained, and negative y reverses the allowed curvature
direction. Complete cross terms and the polynomial correction are unchanged.

Validation: `node audits/theta-gap-4d-2026-10-05-v1/validate-display.cjs`;
JavaScript syntax check; browser preset/slider/projection controls; readable
390px and 1280px layouts without overflow; no captured browser errors.
[Preview](model-preview.jpg). The unchanged manuscript builds: 358 pages,
zero undefined/duplicate references. No new version or manifest.

[Review record](review-record.json) describes the conclusion/dependency
refresh; no historical proof or numerical replay is claimed. Both original
evidence-recovery groups remain OPEN.

The user's follow-up asks for twelve reviews specifically of **next steps**.
Those are recorded separately in
[the method feasibility audit](../theta-next-steps-team-2026-10-05-v1/README.md).
