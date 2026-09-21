from pathlib import Path
import hashlib,json,os,re,zipfile
import fitz
b=Path(__file__).resolve().parent
old=b/'current'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):
    with open(p,'w') as f:f.write(s);f.flush();os.fsync(f.fileno())
t=(b/'fixed_space_prime_action_v1.tex').read_text()
s=(old/'fixed_space_prime_action_v1.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==len(set(labels))==431
assert set(re.findall(r'\\label\{([^}]+)\}',s))<=set(labels)
assert set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',t))<=set(labels)
assert t.count('\\section{')==34
ledger=lambda x:re.findall(r'^\d+\.\d+ &.*$',x,re.M)
assert ledger(s)==ledger(t) and len(ledger(t))==72
assert not re.search('Warning|Overfull|Underfull',(b/'fixed_space_prime_action_v1.log').read_text())
with fitz.open(b/'fixed_space_prime_action_v1.pdf') as d:
    assert len(d)==139
    assert all(p.get_text().strip() for p in d)
entry=(b/'checkpoint_entry.md').read_text()
entry+='\n**Completed validation:** complete v1.19 is 139 pages, with 431 unique labels, all 32 main sections, two appendices and the 72 historical ledger rows retained. Every PDF page was rendered and visually reviewed, with the new proof on pages 89–90, title, goals and reproduction summary checked at higher resolution. The final build has no warnings, unresolved references or overflow. An incomplete intermediate build was discarded and rebuilt in a fresh directory; only the complete, closed, parseable PDF was installed. Truncated intermediate image renders were regenerated. The cumulative archive retains all prior evidence and is independently checked for CRC and current artifact hashes.\n'
oldlog=(old/'RH_G1_G2_research_log.md').read_text().removeprefix('# RH manuscript research log\n\n').replace('## Current research checkpoint:','## Previous research checkpoint:',1)
write(b/'RH_G1_G2_research_log.md','# RH manuscript research log\n\n'+entry+'\n'+oldlog)
notes='''# Complete manuscript v1.19 — September 21, 2026

The complete paper has 139 pages, 32 main sections, two appendices, 431 unique labels and all 72 historical claim dispositions.

**New analytic obstruction:** Proposition 20.42 proves that the unsigned prime-shift norm is exactly unchanged by every finite-rank orthogonal source or Fourier-head removal. Its essential norm equals its ordinary norm; subtracting a compact operator, including the rank-two pole operator, cannot make the complementary norm smaller. The proof uses simultaneous phase recurrence and weakly null Fourier modulations, with no rational independence or operator-domain assumption.

**Sharp growth:** Proposition 20.43 proves ||T_pr||=(1+o(1))lambda, with the actual weights Lambda(m)/sqrt(m) and L=2log(lambda). A positive exponential-cosh weight gives an exact ratio; the unconditional prime number theorem and Chebyshev estimate sandwich its norm. The result remains true after any family of finite-rank orthogonal removals, however fast their ranks grow.

The consequence is limited to the paper's scalar place-by-place tail bound: subtracting the exact unsigned prime norm from the minimum logarithmic archimedean diagonal still requires an exponential cutoff in lambda. This is not a necessary cutoff for actual signed positivity. Frequency-weighted estimates and directional inverse-action bounds remain viable because the recurrence vectors may occur far above the cutoff, where their logarithmic energy is much larger. The paper's earlier broad wording about every scalable complement method was narrowed accordingly.

The abstract, status, Section 20, Section 32 research goals, reproduction appendix and bibliography are updated. The independent adverse review checks the compact-correction extension and scope. A non-certified numerical script checks the exact positive-trial autocorrelation and illustrates recurrence away from the first 64 Fourier modes. No numerical observation is used as a proof of a sign or asymptotic statement.

The full PDF was compiled without warnings and visually reviewed throughout, including detailed checks of new proof pages 89–90. All prior labels, ledger rows, physical endpoint and Fourier conventions, separate logarithmic diagonal and the corrected sampler graph defect are preserved. The cumulative evidence archive includes the new proofs, review, diagnostic, result, reproduction guide and persistent log.

**No G2 sign gap was closed.** The small unweighted complementary-norm shortcut is now ruled out. The next target is a frequency-weighted prime comparison retaining the increasing diagonal, or an independent signed arithmetic estimate along growing windows. Weak G1, fixed-window positivity and ground ordering, and the zero continuum endpoint remain unchanged. G2 and RH remain open. No publication or outside contact occurred.

'''
write(b/'v1_revision_notes.md',notes+(old/'v1_revision_notes.md').read_text().replace('# Complete manuscript v1.18 — September 21, 2026','## Previous release: complete manuscript v1.18 — September 21, 2026',1))
v=json.loads((old/'v1_validation.json').read_text())
for f in ['new_results','proof_checks','certificates']:v['retained_v1_18_'+f]=v.get(f)
v.update(manuscript_version='1.19',date='2026-09-21',pdf_pages=139,unique_labels=431,
 visual_review='All139 pages rendered and visually reviewed; new proof89–90, front matter, research goals and reproduction summary checked at higher scale. Final PDF has no warnings, unresolved references or overflow.',
 new_results=['Proposition20.42: every finite-codimension orthogonal compression retains the complete unsigned prime norm; arbitrary compact corrections cannot reduce that norm.',
 'Proposition20.43: the actual prime norm is asymptotic to lambda as lambda grows, uniformly over arbitrary families of finite-rank removals by the exact compression identity.',
 'Precisely scoped scalar-tail-budget obstruction: even the exact compressed prime norm requires an exponential-in-lambda cutoff in that sufficient bound.'],
 proof_checks=['Finite simultaneous recurrence includes rationally dependent prime phases and exact periodic returns.',
 'Conjugation converges in operator norm for the finite active shift sum; modulations are weakly null on every fixed L2 input.',
 'Finite-rank projections and arbitrary compact operators vanish strongly on the weakly null sequence.',
 'Exact weights and forward/backward strict cuts checked in Tphi/phi.',
 'Uniform PNT envelope includes small arguments; S(X) bound follows by partial summation.',
 'Positive weight is bounded away from zero at every fixed window; no uniform lower bound on that weight is required.',
 'Only orthogonal finite-rank projections are claimed.',
 'Scope excludes frequency-weighted, directional and actual signed-positivity conclusions.',
 'All423 prior labels and72 ledger rows retained; corrected sampler defect unchanged.'],
 certificates=[],
 numerical_illustrations='Non-certified positive-trial Rayleigh and recurrence diagnostics; physical/autocorrelation agreement below1e-50 at60digits for lambda2,3. No norm or sign certificate inferred.',
 limitations='G2 and RH remain open. The scalar-norm shortcut is falsified; frequency-weighted unsigned and signed approaches are not ruled out. No uniform recurrence frequency estimate is claimed.',
 primary_sources=v.get('primary_sources',[])+[{'url':'https://dlmf.nist.gov/27.12','use':'Classical unconditional prime number theorem; actual operator norm proof is written explicitly.'}],
 internal_adversarial_review='Independent agent checked recurrence, compact perturbation, normalization, PNT sandwich and scalar-bound scope. Orthogonal projection qualifier added after review.')
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md']
newfiles=['prime_norm_insert.tex','adversarial_prime_norm_review.md','check_prime_norm.py','prime_norm_checks.json','checkpoint_entry.md','REPRODUCE_v119.md','integrate_v119.py','build_complete_pdf.py','finish_checkpoint.py']
for n in roots:v['sha256'][n]=sha(b/n)
for n in newfiles:v['sha256']['g2_growing_sign/'+n]=sha(b/n)
write(b/'v1_validation.json',json.dumps(v,indent=2)+'\n')
roots+=['v1_validation.json']
base=old/'fixed_space_prime_action_v1_bundle.zip'
assert base.stat().st_size==42348454
assert sha(base)=='689476b8c111ff49102f3a1c9a3238e98eab354ee2e54a1d5b9b852338072af0'
with zipfile.ZipFile(base) as z:assert z.testzip() is None and len(z.namelist())==151
output=b/'fixed_space_prime_action_v1_bundle.zip';tmp=b/'bundle_complete.tmp'
with open(tmp,'wb') as f:
    with zipfile.ZipFile(base) as z,zipfile.ZipFile(f,'w',zipfile.ZIP_DEFLATED) as out:
        for info in z.infolist():
            if info.filename not in roots:out.writestr(info,z.read(info.filename))
        for n in roots:out.write(b/n,n)
        for n in newfiles:out.write(b/n,'g2_growing_sign/'+n)
    f.flush();os.fsync(f.fileno())
os.replace(tmp,output)
fd=os.open(b,os.O_RDONLY);os.fsync(fd);os.close(fd)
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))==160
    for n in roots:assert hashlib.sha256(z.read(n)).hexdigest()==sha(b/n)
    for n in newfiles:assert hashlib.sha256(z.read('g2_growing_sign/'+n)).hexdigest()==sha(b/n)
summary=dict(bytes=output.stat().st_size,sha256=sha(output),members=160,crc='PASS',current_hashes='PASS')
write(b/'bundle_integrity.json',json.dumps(summary,indent=2)+'\n')
ids=[('fixed_space_prime_action_v1.tex','libfile_917c02e02af48191904626b60b218aeb',18),('fixed_space_prime_action_v1.pdf','libfile_efb5d0e5c444819185f4ed729b225882',18),('v1_revision_notes.md','libfile_d5d8a33f6b8c819198e0be7602c5f6e8',18),('RH_G1_G2_research_log.md','libfile_947acdc341748191ab57ed202c5bb37e',19),('v1_validation.json','libfile_b1cb4075cb548191b44d42cdf44a49a6',18),('fixed_space_prime_action_v1_bundle.zip','libfile_386d5bdf90848191b485e716d0205c09',19)]
uploads=[dict(local_path=str(b/n),purpose='replace_library_file',library_file_id=i,expected_current_version=ver,version_reason='Complete v1.19: finite-rank removal preserves unsigned prime norm; exact leading growth lambda and compact-pole obstruction proved. Full signed G2 and RH remain open.') for n,i,ver in ids]
write(b/'upload_requests.json',json.dumps(dict(uploads=uploads),indent=2)+'\n')
print(json.dumps(summary));print('139pages;431labels;72ledgerrows;validated complete PDF.')
