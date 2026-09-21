#!/usr/bin/env python3
"""Freeze a rational candidate. This generator is not a true-PSWF certificate.

The output decimal strings DEFINE the exact rational candidate subsequently
certified, regardless of the accuracy of this non-certified source calculation.
"""
import json,sys
from pathlib import Path
base=Path(__file__).resolve().parent
pilot=Path(sys.argv[1]) if len(sys.argv)>1 else base.parent/'g2_spectral_pilot'
if not pilot.exists(): pilot=base.parent/'g2_spectral'
sys.path.insert(0,str(pilot))
import mpmath as mp
from check_g2_spectral import repaired_source
from check_g2_spectral_mp import coefficients

_,h,metadata=repaired_source('3',70,105,return_mp=True)
nodes,weights=mp.gauss_quadrature(320,'legendre')
co=coefficients(mp.mpf(3),64,h,nodes,weights)
data=dict(definition='The strings are exact decimal rationals c_n for n=0,...,64; set c_-n=c_n and normalize in Euclidean norm. They define the certificate candidate, not exact PSWF coefficients.',
    lambda_exact='3',N=64,source_metadata=metadata,
    positive_coefficients=[mp.nstr(co[64+n],90) for n in range(65)])
(base/'g2_finite_candidate.json').write_text(json.dumps(data,indent=2)+'\n')
print('Frozen 65 exact decimal rationals; no accuracy assumption needed to define candidate.',flush=True)
