"""Certified ordinary-head lower errors, never positivity from an inconclusive bound."""
from simultaneous_trial import *

def run(path):
 data=json.loads(Path(path).read_text());ctx.prec=max(768,data['bits']);mats={n:arb_mat([[arb(t) for t in row] for row in v]) for n,v in data['matrices'].items()};K=mats['K'];dh=K.nrows();mu=arb(data['mu']);rho=arb(data['rho']);V=mats.get('head',arb_mat([[int(i==j) for j in range(dh)] for i in range(dh)]));norm=V.transpose()*V
 best=None;checks=[]
 for ep in range(-5,6):
  tau=arb(10)**ep;low=sym(K-mats['V']-mats['E']-((1+tau)*mats['HGram']+(1+1/tau)*rho*mats['E'])/mu)
  if ldl(low)[0]['status']=='PASS':checks.append({'tau_exp':ep,'positive':True});best={'positive':True,'tau_exp':ep};break
  def test(q):return ldl(sym(low+arb(10)**(-q)*norm))[0]
  if test(-6)['status']!='PASS':checks.append({'tau_exp':ep,'error_bound':'greater than tested range'});continue
  lo=-6;hi=150
  while hi-lo>1:
   q=(hi+lo)//2
   if test(q)['status']=='PASS':lo=q
   else:hi=q
  got={'tau_exp':ep,'epsilon_exponent':lo,'epsilon':f'1e{-lo:+d}','gate':test(lo)};checks.append(got)
  if best is None or lo>best.get('epsilon_exponent',-100):best=got
 result={'status':'CERTIFIED_HEAD_LOWER_ERROR' if best else 'NO_CERTIFICATE','source':Path(path).name,'bits':data['bits'],'parity':data['parity'],'M':data['M'],'J':data['J'],'steps':data['steps'],'best':best,'checks':checks,'scope':'S_infinity >= -epsilon I on the ordinary outer head; not a positivity result or growing-window estimate. A shifted complete form square gives the same lower error for the full parity operator.'}
 out=Path(path).with_name(Path(path).name.replace('_ingredients_','_ordinary_error_'));out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run(sys.argv[1])
