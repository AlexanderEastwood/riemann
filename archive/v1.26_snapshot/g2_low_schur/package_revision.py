from pathlib import Path
import hashlib,json,re,zipfile,fitz
B=Path(__file__).parent;rootnames=['fixed_space_prime_action_v1.tex','fixed_space_prime_action_v1.pdf','RH_G1_G2_research_log.md','v1_revision_notes.md','v1_validation.json']
s=(B/rootnames[0]).read_text();old=(B/'current'/rootnames[0]).read_text();labels=re.findall(r'\\label\{([^}]+)\}',s);oldlabels=set(re.findall(r'\\label\{([^}]+)\}',old));assert oldlabels<=set(labels) and len(labels)==len(set(labels))
ledger=s.split('\\section{Integration ledger for the complete previous manuscript}')[1].split('\\end{longtable}')[0]
rows=re.findall(r'^\s*\d+\.\d+\s*&',ledger,re.M);assert len(rows)==72,len(rows)
logs=(B/'fixed_space_prime_action_v1.log').read_text();warnings=[x for x in logs.splitlines() if re.search('Warning|Overfull|Underfull|undefined|multiply defined',x)];assert not warnings,warnings
pdf=fitz.open(B/rootnames[1]);assert len(pdf)==148
v=json.loads((B/'current/v1_validation.json').read_text());v.update({'manuscript_version':'1.20','revision':'structured inverse and low-mode Schur investigation','date':'2026-09-21','pdf_pages':len(pdf),'historical_claims_accounted_for':72,'unique_labels':len(labels),'prior_labels_preserved':len(oldlabels),'main_sections':32,'appendices':2,'undefined_references':[],'duplicate_labels':[],'latex_warning_lines':warnings,'visual_review':'All148 final pages rendered and visually reviewed in contact sheets; title and new proof94–96 reviewed individually. No warning, overflow or blank content page.','limitations':'No low-head Schur sign or growing-window G2 sign was proved. Actual complete far-inverse sandwich atlambda4 certified, with monotone inverse approximation; signed polynomial evaluations remain open.'})
v['schur_revision']={'proved':['Structured closed-form inverse bound, with both signed mixed terms retained.','Finite-row version enclosing every remote Gram and its mixed term.','Two-sided complete archimedean diagonal estimate.','Monotone arithmetic inverse polynomials with full-operator error bound.','Actual lambda4 shifted far sandwich constants67even/335odd, verified at320and384bits.','Sufficient ordinary-error criterion with operator norm, growing dimension and congruence scales explicit.'],'failed_candidates':{'even_outer_cutoffs':[256,512,1024],'certified_obstruction':'K_X−V_J has a strictly negative dyadic witness for every candidate; this is not a negative Weil vector.','replay_bits':896},'no_G2_sign_gap_closed':True,'adversarial_review':'Full structured implementation and inverse polynomial/form-domain argument reviewed; corrected global pole scale32h/L before final integration.'}
new=[]
for p in B.iterdir():
 if not p.is_file() or p.name in rootnames or p.name=='far_inverse_contraction.json':continue
 if p.suffix in ['.py','.json','.md','.tex'] or p.name.endswith('.json.gz'):new.append(p)
# Baseline source makes the integration reproducible without an older scratch tree.
newmap={'g2_low_schur/'+p.name:p for p in new};newmap['g2_low_schur/current/fixed_space_prime_action_v1.tex']=B/'current/fixed_space_prime_action_v1.tex'
for name in rootnames[:-1]:v['sha256'][name]=hashlib.sha256((B/name).read_bytes()).hexdigest()
for name,p in newmap.items():v['sha256'][name]=hashlib.sha256(p.read_bytes()).hexdigest()
v['source_bundle_sha256']=hashlib.sha256((B/'current/fixed_space_prime_action_v1_bundle.zip').read_bytes()).hexdigest()
v['cumulative_bundle_previous_members']=181
(B/'v1_validation.json').write_text(json.dumps(v,indent=2)+'\n')
out=B/'fixed_space_prime_action_v1_bundle.zip'
with zipfile.ZipFile(B/'current/fixed_space_prime_action_v1_bundle.zip') as oldz,zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 assert len(oldz.namelist())==181
 for info in oldz.infolist():
  if info.filename not in rootnames and info.filename not in newmap:z.writestr(info,oldz.read(info.filename))
 for n in rootnames:z.write(B/n,n)
 for n,p in sorted(newmap.items()):z.write(p,n)
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(set(z.namelist()))
 for n in rootnames:assert z.read(n)==(B/n).read_bytes()
 count=len(z.namelist())
print(json.dumps({'pages':len(pdf),'unique_labels':len(labels),'ledger_rows':len(rows),'bundle_members':count,'bundle_size':out.stat().st_size,'bundle_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'warnings':warnings},indent=2))
