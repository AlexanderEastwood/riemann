"""Independent high-precision constant-mode normalization check, not proof."""
from pathlib import Path
import json,mpmath as mp
mp.mp.dps=90
rows=[]
for value in ['1.2','2','3','10']:
 lam=mp.mpf(value);L=2*mp.log(lam)
 def rho(y):return mp.exp(y/2)/(2*mp.sinh(y))
 def k(y):
  if abs(y)<mp.mpf('1e-40'):return mp.mpf(1)/4-y/48-y*y/32
  return rho(y)-1/(2*y)
 def old_integrand(y):
  if y==0:return mp.mpf(1)/2-1/L
  return 2*rho(y)*(-y/L-mp.expm1(-y/2))
 old=-mp.quad(old_integrand,[0,L])-mp.log(4*mp.pi)-mp.euler-mp.log(mp.tanh(L/2))
 new=1-mp.log(L)-mp.euler-mp.log(2*mp.pi)-2/L*mp.quad(lambda y:(L-y)*k(y),[0,L])
 error=abs(old-new)
 assert error<mp.mpf('1e-65')
 rows.append(dict(lambda_exact=value,original_archimedean_diagonal=mp.nstr(old,75),log_laplacian_plus_remainder=mp.nstr(new,75),absolute_difference=mp.nstr(error,8)))
r=dict(status='PASS: high-precision diagnostic',scope='Independent constant-mode cross-check of the exact analytic physical decomposition; numerical agreement is not its proof.',decimal_precision=mp.mp.dps,rows=rows)
Path(__file__).with_name('log_kernel_normalization_checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
