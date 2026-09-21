"""Bind the complete complement and directional certificates to one Schur form."""
from simultaneous_trial import *
from fractions import Fraction

def dyad(p):
 n,e=p;return Fraction(int(n))*Fraction(2)**int(e)

def run():
 ctx.prec=768
 p=BASE/'simultaneous_odd_M4096_s16_normalized_witness.json.gz';oldraw=p.read_bytes();old=json.loads(gzip.decompress(oldraw));oldhash=hashlib.sha256(oldraw).hexdigest()
 p=BASE/'directional_odd_M8192_s24_witness.json.gz';raw=p.read_bytes();new=json.loads(gzip.decompress(raw));newhash=hashlib.sha256(raw).hexdigest()
 c=json.loads((BASE/'direction_complement_report_b768.json').read_text());assert c['status']=='PASS_COMPLETE_COMPLEMENT' and c['sigma']=='1/1000' and c['trial_witness_sha256']==oldhash
 vwraw=(BASE/'simultaneous_odd_M4096_s32_normalized_witness.json.gz').read_bytes();vw=json.loads(gzip.decompress(vwraw));assert c['direction_witness_sha256']==hashlib.sha256(vwraw).hexdigest()
 assert new['direction_dyadics']==vw['direction_dyadics'] and new['parent_witness_sha256']==oldhash
 v=list(map(dyad,new['direction_dyadics']));head=[sum((dyad(old['base_columns'][j][i])*v[j] for j in range(16)),Fraction(0)) for i in range(16)]
 assert head==list(map(dyad,new['dyadics'][:16]))
 inp=BASE/'simultaneous_odd_M4096_s16_normalized_ingredients_b768.json';data=json.loads(inp.read_text());assert c['ingredient_sha256']==hashlib.sha256(inp.read_bytes()).hexdigest()
 VH=arb_mat([[arb(t) for t in row] for row in data['matrices']['head']]);assert not VH.det().contains(0)
 paths=[];ss=[]
 for bits in [1024,1280]:
  p=BASE/f'directional_odd_M8192_s24_report_b{bits}_J65536.json';r=json.loads(p.read_text())
  assert r['status']=='PASS_DIRECTION_VS_SIGMA' and r['trial_witness_sha256']==newhash and r['parent_witness_sha256']==oldhash
  assert (r['M'],r['steps'],r['J'],r['rho_source_J'],r['bits'])==(8192,24,65536,65536,bits)
  K,V,E,H,rho,den=[arb(r[k]) for k in ['K','finite_far_upper','remote_outer_upper','finite_mixed_squared','rho_upper','old_direction_denominator']]
  assert min(K,V,E,H,rho,den)>0
  mu=arb(9999999999)/10000000000
  U=V+E+(H.sqrt()+(rho*E).sqrt())**2/mu;s=(K-U)/den
  assert s>arb(429)/1000
  assert s.overlaps(arb(r['s_lower_interval']))
  ss.append(s.str(80));paths.append({'path':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 assert arb(429)/1000-arb(1)/1000>0
 out={'status':'PASS_COMPLETE_ODD_AND_FULL_LAMBDA4','lambda':4,'certified_directional_s':'429/1000','complete_complement_sigma':'1/1000','certified_odd_S_over_K_lower':'107/250','full_window_negative_error':0,'old_trial_support':4096,'directional_trial_support':8192,'verified_rows_through':65536,'remote_moment_order':64,'same_physical_head_exact_fraction_check':True,'physical_head_mantissa_bits_max':max(int(n).bit_length() for n,e in new['dyadics'][:16]),'old_head_invertibility_gate':True,'direction_lower_recomputations':ss,'reports':paths,'old_witness_sha256':oldhash,'directional_witness_sha256':newhash,'complement_report_sha256':hashlib.sha256((BASE/'direction_complement_report_b768.json').read_bytes()).hexdigest(),'scope':'Complete fixed-window odd sign via PSD inverse-correction gluing; full lambda4 sign additionally uses existing complete even certificate. Relative107/250 is not an ordinary spectral-gap constant. No G2/RH or growing-window theorem.'}
 (BASE/'complete_lambda4_v126_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
