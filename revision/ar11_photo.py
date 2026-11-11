from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
P='/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/33e2a9d1-image.png'; P2='/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/814ce186-image.png'
R='/home/claude/larevista-notas/img/'; I='2026-11-11-argentina-shell-edenor-manzano-mercuria'
BB=ImageFont.truetype('BebasNeue-Regular.ttf',96); BBs=ImageFont.truetype('BebasNeue-Regular.ttf',40)
BS=ImageFont.truetype('Barlow-SemiBold.ttf',30); BC=ImageFont.truetype('Barlow-SemiBold.ttf',20); BK=ImageFont.truetype('Barlow-Bold.ttf',24)
def cover(im,W,H,cy=0.5):
    s=max(W/im.width,H/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-W)//2; y=int((im.height-H)*cy); return im.crop((x,y,x+W,y+H))
def grad(W,H,start,alpha=235):
    g=np.zeros((H,W,4),dtype=np.uint8); g[...,0]=12;g[...,1]=26;g[...,2]=41
    a=np.clip((np.arange(H)-start)/(H-start),0,1)**1.3*alpha; g[...,3]=a[:,None]; return Image.fromarray(g,'RGBA')
ph=Image.open(P).convert('RGB')
# HERO web 1600x1067
W,H=1600,1067; im=Image.new('RGBA',(W,H),'#0C1A29'); pim=cover(ph,W,640,0.55); im.paste(pim,(0,0)); d=ImageDraw.Draw(im)
for i,c in enumerate(('#74ACDF','#FFFFFF','#74ACDF')): d.rectangle((0,i*6,W,i*6+6),fill=c)
cr='Foto de archivo'; tw=d.textlength(cr,font=BC); d.rounded_rectangle((W-70-tw-24,640-52,W-70,640-16),8,fill='#0C1A29'); d.text((W-70-tw-12,640-48),cr,font=BC,fill='white')
d.rounded_rectangle((70,600,70+d.textlength('REGIÓN · ARGENTINA',font=BK)+36,644),8,fill='#3A7D44'); d.text((88,607),'REGIÓN · ARGENTINA',font=BK,fill='white')
B2=ImageFont.truetype('BebasNeue-Regular.ttf',86)
d.text((66,668),'LAS ESTACIONES SHELL',font=B2,fill='white'); d.text((66,752),'SUMAN SOCIOS LOCALES',font=B2,fill='#6DBB78')
d.text((70,862),'Edenor y el grupo Manzano entran con Mercuria en la red de 892 estaciones',font=BS,fill='#C9D4DF')
d.rectangle((70,925,1530,926),fill='#24384F')
d.rectangle((0,967,W,H),fill='#0C1A29'); d.text((70,995),'LA ESTACIÓN',font=BBs,fill='white'); d.text((70+d.textlength('LA ESTACIÓN ',font=BBs),995),'DEL FUTURO',font=BBs,fill='#6DBB78')
t='energiaslatam.com'; f=ImageFont.truetype('Barlow-SemiBold.ttf',24); d.text((W-70-d.textlength(t,font=f),1003),t,font=f,fill='white')
im.convert('RGB').save(R+I+'-1.jpg',quality=86)
# photo for body 3:2 whole
cr='Imagen ilustrativa'; b=Image.open(P2).convert('RGB'); b=b.resize((1600,round(1600*b.height/b.width)),Image.LANCZOS); c=Image.new('RGB',(1600,1067),'#0F213D'); c.paste(b,(0,(1067-b.height)//2))
d=ImageDraw.Draw(c); tw=d.textlength(cr,font=BC); d.rounded_rectangle((16,1067-56,16+tw+24,1067-18),8,fill='#0F213D'); d.text((28,1067-51),cr,font=BC,fill='white')
c.save(R+I+'-3.jpg',quality=86)
print('ok',b.size)
