from pathlib import Path
import hashlib,json,re,zipfile,fitz
B=Path(__file__).resolve().parent
roots=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md','v1_validation.json']
s=(B/roots[0]).read_text();old=(B/'input'/roots[0]).read_text()
labels=re.findall(r'\\label\{([^}]+)\}',s);prior=set(re.findall(r'\\label\{([^}]+)\}',old))
assert prior<=set(labels) and len(labels)==len(set(labels))
ledger=s.split('\\section{Integration ledger for the complete previous manuscript}')[1].split('\\end{longtable}')[0]
assert len(re.findall(r'^\s*\d+\.\d+\s*&',ledger,re.M))==72
log=(B/'fixed_space_prime_action_v1.log').read_text()
warnings=[x for x in log.splitlines() if re.search('Warning|Overfull|Underfull|undefined|multiply defined',x)]
assert not warnings,warnings
pdf=fitz.open(B/roots[1]);assert len(pdf)==156
for page in pdf:assert page.get_text().strip()
newmap={}
for p in B.iterdir():
 if p.is_file() and p.name not in roots and p.suffix in ['.py','.md','.json','.tex']:
  newmap['g2_inverse_refinement/'+p.name]=p
for n in ['fixed_space_prime_action_v1.tex','RH_G1_G2_research_log.md','v1_revision_notes.md','v1_validation.json']:
 newmap['g2_inverse_refinement/input/'+n]=B/'input'/n
for p in (B/'renders').glob('contact*.jpg'):newmap['g2_inverse_refinement/renders/'+p.name]=p
v=json.loads((B/'input/v1_validation.json').read_text())
v.update({'manuscript_version':'1.22','date':'2026-09-21','pdf_pages':156,'main_sections':32,'appendices':2,'historical_claims_accounted_for':72,'unique_labels':len(labels),'prior_labels_preserved':len(prior),'undefined_references':[],'duplicate_labels':[],'latex_warning_lines':warnings,'visual_review':{'status':'passed','complete_pdf_pages':156,'all_pages_reviewed_in_contact_sheets':True,'new_proofs_and_tables_reviewed_at_full_size':[1,98,99,100,101,148,149],'layout_corrections':'Wrapped long witness filenames and updated ledger version headers; no remaining box warning or clipped content.'},'limitations':'No G2 sign gap closed. One complete far-energy direction passes; the refined mixed term, full head matrix and growing-window uniformity remain open.'})
v['v122_inverse_refinement']={'proved':['Parity sandwich constants20even/90odd for the complete shifted lambda4 far operators.','Finite-prefix scalar, matrix Young, and relative matrix bounds including infinite residual rows.','A complete far-energy bound below the trial budget on one archived exact dyadic even direction.','Consistent Q_* substitution in both structured inverse terms with closed form domains.'],'constants_precision_bits':[320,384],'directional_gate_precision_bits':[768,896],'directional_cutoff':65536,'moment_order':64,'directional_far_upper':'5.758e-20','directional_trial_lower':'6.469e-20','mixed_term_certified':False,'full_schur_sign_certified':False,'no_G2_sign_gap_closed':True,'adversarial_review':'Passed; explicit nu>=0 added. Shift, pole factors, original kappa_N, matrix positive-part warning, polynomial indexing and Q_* form domains checked.'}
v['sha256']={}
for n in roots[:-1]:v['sha256'][n]=hashlib.sha256((B/n).read_bytes()).hexdigest()
for n,p in newmap.items():v['sha256'][n]=hashlib.sha256(p.read_bytes()).hexdigest()
v['source_bundle_sha256']=hashlib.sha256((B/'input/fixed_space_prime_action_v1_bundle.zip').read_bytes()).hexdigest()
with zipfile.ZipFile(B/'input/fixed_space_prime_action_v1_bundle.zip') as z:v['cumulative_bundle_previous_members']=len(z.namelist())
(B/'v1_validation.json').write_text(json.dumps(v,indent=2)+'\n')
out=B/'fixed_space_prime_action_v1_bundle.zip'
with zipfile.ZipFile(B/'input/fixed_space_prime_action_v1_bundle.zip') as src,zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as dest:
 for info in src.infolist():
  if info.filename not in roots and info.filename not in newmap:dest.writestr(info,src.read(info.filename))
 for n in roots:dest.write(B/n,n)
 for n,p in sorted(newmap.items()):dest.write(p,n)
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(set(z.namelist()))
 for n in roots:assert z.read(n)==(B/n).read_bytes()
 count=len(z.namelist())
print(json.dumps({'pages':156,'prior_labels':len(prior),'labels':len(labels),'historical_claims':72,'bundle_members':count,'bundle_bytes':out.stat().st_size,'warnings':warnings},indent=2))
