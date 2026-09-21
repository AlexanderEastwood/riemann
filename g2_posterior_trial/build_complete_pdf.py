"""Compile in a fresh directory; install only a closed, parseable full PDF."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import fitz

b=Path(__file__).resolve().parent
stem='fixed_space_prime_action_v1'
with tempfile.TemporaryDirectory(prefix='complete_build_',dir=b) as temp:
    d=Path(temp)
    shutil.copy2(b/(stem+'.tex'),d/(stem+'.tex'))
    p=subprocess.run(['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error',stem+'.tex'],cwd=d,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    with open(b/'build_transcript.txt','wb') as f:
        f.write(p.stdout);f.flush();os.fsync(f.fileno())
    if p.returncode:
        raise RuntimeError(p.stdout.decode()[-5000:])
    with fitz.open(d/(stem+'.pdf')) as pdf:
        pages=len(pdf)
        assert pages>130
        for page in pdf:
            assert page.get_text().strip()
    for suffix in ['.pdf','.aux','.log','.toc','.out']:
        source=d/(stem+suffix)
        with open(source,'rb') as f:os.fsync(f.fileno())
        os.replace(source,b/(stem+suffix))
    fd=os.open(b,os.O_RDONLY);os.fsync(fd);os.close(fd)
    print('Complete PDF installed:',pages,'pages,',(b/(stem+'.pdf')).stat().st_size,'bytes')
