from pathlib import Path
import fitz
from PIL import Image,ImageDraw
B=Path(__file__).resolve().parent;r=B/'renders_v124';r.mkdir(exist_ok=True)
doc=fitz.open(B/'fixed_space_prime_action_v1.pdf');thumbs=[]
for i,page in enumerate(doc):
 pix=page.get_pixmap(matrix=fitz.Matrix(.45,.45),alpha=False)
 im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 canvas=Image.new('RGB',(290,390),'#eee');canvas.paste(im,((290-im.width)//2,15));ImageDraw.Draw(canvas).text((10,373),str(i+1),fill='black');thumbs.append(canvas)
 if i+1 in [1,105,106,107,154,155] or 'simultaneous Gram bound' in page.get_text():page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(str(r/f'page_{i+1:03d}.png'))
for c,start in enumerate(range(0,len(thumbs),40)):
 group=thumbs[start:start+40];sheet=Image.new('RGB',(1450,390*((len(group)+4)//5)),'#ccc')
 for j,im in enumerate(group):sheet.paste(im,((j%5)*290,(j//5)*390))
 sheet.save(r/f'contact_{c+1}.jpg',quality=85)
print('Rendered',len(doc),'pages.')
