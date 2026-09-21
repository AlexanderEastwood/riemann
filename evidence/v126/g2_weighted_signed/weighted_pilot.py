"""Exploratory signed energy-normalized Fourier-tail matrices. Not a certificate."""
import numpy as np, json, os
from scipy.special import digamma
from scipy.linalg import eigh
from pathlib import Path

def seq(lam,M):
 L=2*np.log(lam);n=np.arange(M+1);t=2*np.pi*n/L;z=.25-.5j*t
 sieve=np.ones(int(lam*lam)+1,dtype=bool);sieve[:2]=False
 for p in range(2,int(lam)+1):
  if sieve[p]:sieve[p*p::p]=False
 ys=[];ws=[]
 for p in np.flatnonzero(sieve):
  m=int(p)
  while m<lam*lam:
   ys.append(np.log(m));ws.append(np.log(p)/np.sqrt(m));m*=int(p)
 y=np.array(ys);w=np.array(ws);phase=t[:,None]*y
 # trigamma recurrence plus Bernoulli asymptotic, checked against mpmath later.
 zz=z+32;tri=1/zz+1/(2*zz**2)
 for k,B in [(1,1/6),(2,-1/30),(3,1/42),(4,-1/30),(5,5/66),(6,-691/2730)]:tri+=B/zz**(2*k+1)
 for k in range(32):tri+=1/(z+k)**2
 ps=digamma(z);s=-ps.imag/2;a=-np.log(np.pi)+ps.real+tri.real/(2*L)
 for k in range(30):
  c=2*k+.5;e=np.exp(-c*L);den=c*c+t*t
  s-=e*t/den;a-=2/L*e*(c*c-t*t)/(den*den)
 h=np.sinh(L/4)**2;den=L*L+16*np.pi**2*n*n
 bp=32*L*h*n/den;dp=32*L*h*(L*L-16*np.pi**2*n*n)/den**2
 b=bp+(s+np.sin(phase)@w)/np.pi
 d=a+dp-2*np.cos(phase)@((1-y/L)*w)
 return L,b,d,a

def run(lam,N,M):
 L,b,d,a=seq(lam,M);ns=np.arange(N+1,M+1);bn=b[ns];dd=ns[:,None]-ns
 same=np.divide(bn[:,None]-bn,dd,out=np.zeros(dd.shape),where=dd!=0);np.fill_diagonal(same,d[ns]);opp=(bn[:,None]+bn)/(ns[:,None]+ns)
 out={'lambda':lam,'N':N,'M':M,'arch_min':float(a[N+1]),'sectors':{}}
 for parity,sign in [('even',1),('odd',-1)]:
  W=same+sign*opp;A=np.sqrt(a[ns]);E=W/A[:,None]/A[None,:];lo=float(eigh(E,subset_by_index=[0,0],eigvals_only=True)[0]);hi=float(eigh(E,subset_by_index=[len(ns)-1,len(ns)-1],eigvals_only=True)[0]);out['sectors'][parity]={'normalized_min':lo,'normalized_max':hi,'remainder_norm':max(abs(hi-1),abs(lo-1))}
 return out
if __name__=='__main__':
 from threadpoolctl import threadpool_limits
 rows=[]
 with threadpool_limits(2):
  for lam,N in [(3,4),(3,8),(3,16),(4,16),(5,25),(8,64),(10,100),(16,256),(24,576)]:
   M=max(256,3*N);r=run(lam,N,M);rows.append(r);print(json.dumps(r),flush=True)
 Path(__file__).with_name('weighted_pilot.json').write_text(json.dumps(rows,indent=2)+'\n')
