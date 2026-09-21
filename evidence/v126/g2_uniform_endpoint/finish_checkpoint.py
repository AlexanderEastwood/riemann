from pathlib import Path
import hashlib
import json
import os
import re
import zipfile
import fitz

b = Path(__file__).resolve().parent
old = b.parent / 'g2_ground_order'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def write(path, content):
    with open(path, 'w') as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())

t = (b / 'fixed_space_prime_action_v1.tex').read_text()
s = (old / 'fixed_space_prime_action_v1.tex').read_text()
labels = re.findall(r'\\label\{([^}]+)\}', t)
assert len(labels) == len(set(labels)) == 423
assert set(re.findall(r'\\label\{([^}]+)\}', s)) <= set(labels)
assert set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', t)) <= set(labels)
assert len(fitz.open(b / 'fixed_space_prime_action_v1.pdf')) == 137
assert t.count('\\section{') == 34
ledger = lambda x: re.findall(r'^\d+\.\d+ &.*$', x, re.M)
assert ledger(t) == ledger(s) and len(ledger(t)) == 72
assert not re.search(r'Warning|Overfull|Underfull', (b / 'fixed_space_prime_action_v1.log').read_text())

entry = (b / 'checkpoint_entry.md').read_text()
entry += '\n**Completed validation:** 137 pages, 423 unique labels, all 32 main sections, two appendices and all 72 historical dispositions retained. The complete PDF was rendered and visually reviewed; new proof pages 75–78 and 87–88, the title, research goals and reproduction summary were also reviewed at larger scale. A short front-matter spill page was removed by condensing duplicated status prose. The final build has no warnings, unresolved references or overflow. One truncated intermediate page render was regenerated; the PDF was intact.\n'
oldlog = (old / 'RH_G1_G2_research_log.md').read_text().removeprefix('# RH manuscript research log\n\n').replace('## Current research checkpoint:', '## Previous research checkpoint:', 1)
write(b / 'RH_G1_G2_research_log.md', '# RH manuscript research log\n\n' + entry + '\n' + oldlog)

notes = '''# Complete manuscript v1.18 — September 21, 2026

The complete paper is 137 pages, with 32 main sections, two appendices, 423 unique labels and all 72 historical claim dispositions retained.

**Continuum endpoint resolved, with a correction to the proposed target:** Proposition 20.29 identifies the complete canonical Weil operator as one half of the restricted logarithmic Laplacian plus an explicitly bounded operator. Theorem 20.30 proves that every eigenfunction has a bounded representative with continuous zero physical boundary trace and inverse-square-root logarithmic boundary decay. This applies to every fixed window and every spectral level, without assuming RH or positivity.

The proof retains the exact scalar -log(2pi), both prime-shift orientations and both pole signs. A common-core argument establishes the closed realization before a simultaneous L2/L-infinity resolvent argument proves eigenfunction boundedness. Only then is the bounded-solution boundary theorem applied. Two independent internal reviews checked these gates.

Corollary 20.31 gives fixed-window Fejer endpoint decay and exact relative endpoint mismatch one between a complete eigenfunction and the repaired source's nonzero endpoint. Thus the proposed nonzero continuum ground-to-source endpoint comparison is false. It must not be pursued as a missing estimate. This is consistent with the retained ordinary overlap results and finite-compression endpoint calculations. It does not establish sharp Fourier endpoint convergence or joint finite-cut/window control.

Proposition 20.32 gives an explicit real even polynomial shell with physical endpoint one and Weil graph norm tending to zero. The physical trace is therefore not closable on that polynomial core in the operator graph norm. Eigenfunction boundary regularity is a separate property, not a consequence of graph convergence.

Proposition 20.41 proves the sharp complement estimate |q(f)-q((I-P)f)| <= (2/sqrt(3))||AP|| ||f||^2. A complementary lower bound -eta therefore gives a complete lower bound -eta-(2/sqrt(3))||AP||, without a positive complementary gap. The already proved rank-one source residual tends to zero; the arithmetic nonnegativity estimate on its entire complement remains unproved. A fixed negative compact test persists after source removal, so the desired cofinal sign remains RH-strength.

The abstract, status, Section 20, Section 32 goals, reproduction appendix and bibliography are integrated. The complete PDF was rendered and visually reviewed, with detailed checks of new proof pages 75–78 and 87–88. The final build has no warnings, unresolved references or overflow. All old labels and ledger rows are preserved. The evidence bundle adds the analytic derivations, primary-source audit, independent adverse reviews and a 90-decimal normalization diagnostic, which is explicitly not a proof certificate.

**Remaining:** growing-window G2 still needs an independent signed lower bound tending to zero, or a sufficient independent quantitative ground-space argument. Finite-compression endpoint control, uniform source-block residuals, the corrected sampler graph defect and full-strip obligations remain separate. No G2 sign gap was closed and no RH proof is claimed. No publication or outside contact occurred.

'''
oldnotes = (old / 'v1_revision_notes.md').read_text().replace('# Complete manuscript v1.17 — September 21, 2026', '## Previous release: complete manuscript v1.17 — September 21, 2026', 1)
write(b / 'v1_revision_notes.md', notes + oldnotes)

v = json.loads((old / 'v1_validation.json').read_text())
for field in ['new_results', 'proof_checks', 'certificates']:
    v['retained_v1_17_' + field] = v.get(field)
v.update(
    manuscript_version='1.18', date='2026-09-21', pdf_pages=137, unique_labels=423,
    visual_review='All 137 final pages rendered; all page layouts reviewed, with new proofs on 75–78 and 87–88, title, goals and reproduction appendix checked at larger scale. Final build has no warnings, unresolved references or overflow.',
    new_results=[
        'Proposition 20.29: exact restricted logarithmic-Laplacian decomposition of the complete operator, with common form core and equal operator domain.',
        'Theorem 20.30: every complete fixed-window eigenfunction is bounded and has continuous zero physical trace, with inverse-square-root logarithmic boundary decay.',
        'Corollary 20.31: fixed-window Fejer endpoint rate and exact relative mismatch one against the repaired source nonzero endpoint.',
        'Proposition 20.32: physical trace on the polynomial core is not closable in the complete Weil operator graph norm.',
        'Proposition 20.41: sharp complement form comparison with constant 2/sqrt(3), no positive complementary gap required.'
    ],
    proof_checks=[
        'Exact scalar -log(2pi), Fourier factors, physical cutoff, prime weights and signed pole kernel retained.',
        'Restricted logarithmic Laplacian distinguished from the spectral logarithm of the Dirichlet Laplacian.',
        'Common compact smooth form core established by endpoint cutoffs and fractional Sobolev interpolation.',
        'Eigenfunction boundedness proved by consistent L2/L-infinity killed-jump resolvents before applying boundary regularity.',
        'Boundary theorem hypotheses checked for complex eigenfunctions by real and imaginary parts; no positivity assumed.',
        'Fejer kernel normalized to physical mass one; far mass bounded by 1/(2sqrt(N)); no sharp-cut claim substituted.',
        'Explicit shell has exactly 2N modes, endpoint one and graph norm O(log(N)/sqrt(N)).',
        'Complement form expansion uses first-slot-linear convention; sharp two-dimensional witness checked.',
        'Growing-window complementary sign explicitly remains unproved and RH-strength.',
        'All 410 prior labels and 72 historical ledger rows preserved; sampler graph defect unchanged.'
    ],
    certificates=[],
    numerical_illustrations='90-decimal constant-mode normalization diagnostic at lambda=1.2,2,3,10; maximum discrepancy below 5e-91. This is not interval certification or the proof of the identity.',
    limitations='No growing-window arithmetic sign or G2 proof. Boundary constants are fixed-window. Fejer estimates do not imply sharp Fourier endpoint convergence or joint finite-compression endpoint control. Nonzero continuum source-to-ground endpoint matching is false.',
    primary_sources=[
        {'url': 'https://arxiv.org/pdf/1710.03416', 'use': 'Chen–Weth Theorems 1.1 and 3.1: exact normalization and form core'},
        {'url': 'https://arxiv.org/pdf/2401.18033', 'use': 'Hernandez-Santamaria–Lopez Rios–Saldana Theorem 1.1: bounded weak solution boundary regularity'}
    ],
    internal_adversarial_review='Endpoint decomposition, domain and boundedness bootstrap independently checked; complement estimate and graph-trace counterexample separately checked. Internal review only.'
)
roots = ['fixed_space_prime_action_v1.tex', 'fixed_space_prime_action_v1.pdf', 'RH_G1_G2_research_log.md', 'v1_revision_notes.md']
newfiles = [
    'actual_ground_endpoint_derivation.md', 'adversarial_endpoint_review.md',
    'adversarial_uniform_bound.md', 'primary_source_and_endpoint_audit.md',
    'eigen_endpoint_insert.tex', 'endpoint_bibitems.tex', 'graph_trace_insert.tex',
    'gap_free_block_insert.tex', 'check_log_kernel_normalization.py',
    'log_kernel_normalization_checks.json', 'checkpoint_entry.md',
    'REPRODUCE_v118.md', 'integrate_v118.py', 'finish_checkpoint.py'
]
for n in roots:
    v['sha256'][n] = sha(b / n)
for n in newfiles:
    v['sha256']['g2_uniform_endpoint/' + n] = sha(b / n)
write(b / 'v1_validation.json', json.dumps(v, indent=2) + '\n')
roots += ['v1_validation.json']

base = old / 'fixed_space_prime_action_v1_bundle.zip'
assert base.stat().st_size == 42272375
with zipfile.ZipFile(base) as z:
    assert z.testzip() is None and len(z.namelist()) == 137
output = b / 'fixed_space_prime_action_v1_bundle.zip'
temp = b / 'bundle_complete.tmp'
with open(temp, 'wb') as f:
    with zipfile.ZipFile(base) as z, zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED) as out:
        for info in z.infolist():
            if info.filename not in roots:
                out.writestr(info, z.read(info.filename))
        for n in roots:
            out.write(b / n, n)
        for n in newfiles:
            out.write(b / n, 'g2_uniform_endpoint/' + n)
    f.flush()
    os.fsync(f.fileno())
os.replace(temp, output)
fd = os.open(b, os.O_RDONLY)
os.fsync(fd)
os.close(fd)
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    members = z.namelist()
    assert len(members) == len(set(members)) == 151
    for n in roots:
        assert hashlib.sha256(z.read(n)).hexdigest() == sha(b / n)
    for n in newfiles:
        assert hashlib.sha256(z.read('g2_uniform_endpoint/' + n)).hexdigest() == sha(b / n)
summary = dict(bytes=output.stat().st_size, sha256=sha(output), members=len(members), crc='PASS', current_artifact_hashes='PASS')
write(b / 'bundle_integrity.json', json.dumps(summary, indent=2) + '\n')
requests = json.loads((old / 'upload_requests.json').read_text())
for item in requests['uploads']:
    item['local_path'] = str(b / Path(item['local_path']).name)
    item['expected_current_version'] += 1
    item['version_reason'] = 'Complete manuscript v1.18: analytic zero physical trace for every complete eigenfunction, fixed-window filtered endpoint decay, graph-trace obstruction and sharp complement reduction. Nonzero continuum endpoint matching falsified; growing-window G2 and RH remain open.'
write(b / 'upload_requests.json', json.dumps(requests, indent=2) + '\n')
print(json.dumps(summary))
print('137 pages; 423 labels; 72 ledger rows; no LaTeX warnings.')
