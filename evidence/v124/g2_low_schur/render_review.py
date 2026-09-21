from pathlib import Path
import fitz,json
from PIL import Image,ImageOps,ImageDraw
B=Path(__file__).parent;R=B/'renders';R.mkdir(exist_ok=True)
doc=fitz.open(B/'fixed_space_prime_action_v1.pdf');pages=[];details=[]
for i,p in enumerate(doc):
 pix=p.get_pixmap(matrix=fitz.Matrix(1.0,1.0),alpha=False);path=R/f'page-{i+1:03}.png';pix.save(path);pages.append(path)
 text=p.get_text()
 if any(x in text for x in ['Reusing the signed tail','structured inverse bound','ordinary-error target','structured low-mode','Structured low-mode','Current research']):details.append(i+1)
for start in range(0,len(pages),25):
 out=Image.new('RGB',(5*250,5*350),'#ddd');draw=ImageDraw.Draw(out)
 for k,path in enumerate(pages[start:start+25]):
  im=Image.open(path);im.thumbnail((240,320));x=(k%5)*250+(250-im.width)//2;y=(k//5)*350+20;out.paste(im,(x,y));draw.text(((k%5)*250+10,(k//5)*350+3),str(start+k+1),fill='black')
 out.save(R/f'contact-{start+1:03}.jpg',quality=90)
for n in sorted(set([1]+details)):
 p=doc[n-1];p.get_pixmap(matrix=fitz.Matrix(1.7,1.7),alpha=False).save(R/f'detail-{n:03}.png')
print(json.dumps({'pages':len(doc),'detail_pages':sorted(set([1]+details)),'contacts':[str(p) for p in sorted(R.glob('contact*'))]},indent=2))
