from PIL import Image, ImageDraw, ImageFont
P='/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/v13/f2.jpg'
R='/home/claude/larevista-notas/img/'; I='2026-11-13-diesel-isc-50-decreto-petropar-baja'
F=lambda n,s: ImageFont.truetype(n,s)
W,H=1600,1067; im=Image.new('RGB',(W,H),'#0C1A29'); ph=Image.open(P).convert('RGB')
ph=ph.crop((0,0,ph.width,int(ph.height*0.80)))
s=H/ph.height; ph=ph.resize((round(ph.width*s),H),Image.LANCZOS); x=int(ph.width*0.37); im.paste(ph.crop((x,0,x+760,H)),(0,0)); d=ImageDraw.Draw(im)
for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): d.rectangle((0,i*6,W,i*6+6),fill=c)
X=830; BK=F('Barlow-Bold.ttf',24); k='ÚLTIMO MOMENTO · PARAGUAY'
d.rounded_rectangle((X,110,X+d.textlength(k,font=BK)+36,154),8,fill='#C0392B'); d.text((X+18,117),k,font=BK,fill='white')
B=F('BebasNeue-Regular.ttf',96); y=196
for l,c in [('EL DIÉSEL PAGA','white'),('LA MITAD DE','white'),('IMPUESTO HASTA','#6DBB78'),('FIN DE AÑO','#6DBB78')]:
    d.text((X-4,y),l,font=B,fill=c); y+=98
d.rectangle((X,y+28,X+140,y+34),fill='#6DBB78'); y+=66
for l in ['Decreto del presidente Alliana: −50 % de ISC','desde hoy y baja de precio de Petropar']:
    d.text((X,y),l,font=F('Barlow-SemiBold.ttf',31),fill='#C9D4DF'); y+=44
y+=44; d.text((X,y),'MARCO RIQUELME',font=F('BebasNeue-Regular.ttf',48),fill='white'); d.text((X,y+54),'Ministro de Industria y Comercio',font=F('Barlow-SemiBold.ttf',27),fill='#8FA3B8')
cr='Imagen: Paraguay TV'; f=F('Barlow-SemiBold.ttf',20); tw=d.textlength(cr,font=f); d.rounded_rectangle((16,H-56,16+tw+24,H-18),8,fill='#0C1A29'); d.text((28,H-51),cr,font=f,fill='white')
bs=F('BebasNeue-Regular.ttf',40); d.text((X,985),'LA ESTACIÓN',font=bs,fill='white'); d.text((X+d.textlength('LA ESTACIÓN ',font=bs),985),'DEL FUTURO',font=bs,fill='#6DBB78')
t='energiaslatam.com'; f=F('Barlow-SemiBold.ttf',24); d.text((W-60-d.textlength(t,font=f),995),t,font=f,fill='white')
im.save(R+I+'-1.jpg',quality=88)
# portada carrusel
W,H=1080,1350; c=Image.new('RGB',(W,H),'#0C1A29'); ph=Image.open(P).convert('RGB'); ph=ph.crop((0,0,ph.width,int(ph.height*0.80))); s=700/ph.height; ph=ph.resize((round(ph.width*s),700),Image.LANCZOS); x=(ph.width-W)//2-60; c.paste(ph.crop((x,0,x+W,700)),(0,0)); d=ImageDraw.Draw(c)
for i,cc in enumerate(('#D52B1E','#FFFFFF','#0038A8')): d.rectangle((0,i*6,W,i*6+6),fill=cc)
k='ÚLTIMO MOMENTO · PARAGUAY'; d.rounded_rectangle((66,676,66+d.textlength(k,font=BK)+36,720),8,fill='#C0392B'); d.text((84,683),k,font=BK,fill='white')
B=F('BebasNeue-Regular.ttf',104); y=750
for l,cc in [('EL DIÉSEL PAGA LA MITAD','white'),('DE IMPUESTO HASTA','#6DBB78'),('FIN DE AÑO','#6DBB78')]:
    d.text((62,y),l,font=B,fill=cc); y+=106
y+=24
for l in ['Decreto del presidente Alliana: −50 % del ISC desde','hoy al 31/12, y baja de precio de Petropar']:
    d.text((66,y),l,font=F('Barlow-SemiBold.ttf',36),fill='#C9D4DF'); y+=50
f=F('Barlow-SemiBold.ttf',26); d.text((66,1280),'1/6',font=f,fill='#8FA3B8'); d.text((480,1280),'Deslizá »',font=f,fill='#8FA3B8'); t='energiaslatam.com'; d.text((W-66-d.textlength(t,font=F('Barlow-Bold.ttf',28)),1278),t,font=F('Barlow-Bold.ttf',28),fill='white')
d.text((W-66-d.textlength('Imagen: Paraguay TV',font=F('Barlow-SemiBold.ttf',20)),640),'Imagen: Paraguay TV',font=F('Barlow-SemiBold.ttf',20),fill='white')
c.save(R+'social/'+I+'-c1.jpg',quality=88)
