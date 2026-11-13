from PIL import Image, ImageDraw, ImageFont
P='/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/19f50268-image.jpg'
R='/home/claude/larevista-notas/img/'; I='2026-11-13-ande-congela-tarifa-suspende-cortes-ueno'
F=lambda n,s: ImageFont.truetype(n,s)
W,H=1600,1067; im=Image.new('RGB',(W,H),'#0C1A29'); ph=Image.open(P).convert('RGB')
s=H/ph.height; ph=ph.resize((round(ph.width*s),H),Image.LANCZOS); x=(ph.width-760)//2+20; im.paste(ph.crop((x,0,x+760,H)),(0,0)); d=ImageDraw.Draw(im)
for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): d.rectangle((0,i*6,W,i*6+6),fill=c)
X=830; BK=F('Barlow-Bold.ttf',24); k='PARAGUAY · ELECTRICIDAD'
d.rounded_rectangle((X,110,X+d.textlength(k,font=BK)+36,154),8,fill='#3A7D44'); d.text((X+18,117),k,font=BK,fill='white')
B=F('BebasNeue-Regular.ttf',92); y=200
for l,c in [('LA ANDE CONGELA','white'),('LA TARIFA POR','white'),('UN AÑO Y SUSPENDE','#6DBB78'),('LOS CORTES','#6DBB78')]:
    d.text((X-4,y),l,font=B,fill=c); y+=96
d.rectangle((X,y+30,X+140,y+36),fill='#6DBB78'); y+=70
for l in ['Sin cortes por falta de pago hasta el 31 de','diciembre y deudas en 24 cuotas sin intereses']:
    d.text((X,y),l,font=F('Barlow-SemiBold.ttf',31),fill='#C9D4DF'); y+=44
y+=50; d.text((X,y),'FÉLIX SOSA',font=F('BebasNeue-Regular.ttf',50),fill='white'); d.text((X,y+56),'Presidente de la ANDE',font=F('Barlow-SemiBold.ttf',28),fill='#8FA3B8')
bs=F('BebasNeue-Regular.ttf',40); d.text((X,985),'LA ESTACIÓN',font=bs,fill='white'); d.text((X+d.textlength('LA ESTACIÓN ',font=bs),985),'DEL FUTURO',font=bs,fill='#6DBB78')
t='energiaslatam.com'; f=F('Barlow-SemiBold.ttf',24); d.text((W-60-d.textlength(t,font=f),995),t,font=f,fill='white')
im.save(R+I+'-3.jpg',quality=88)
# portada carrusel 1080x1350
W,H=1080,1350; c=Image.new('RGB',(W,H),'#0C1A29'); ph=Image.open(P).convert('RGB'); s=W/ph.width; ph=ph.resize((W,round(ph.height*s)),Image.LANCZOS); c.paste(ph.crop((0,60,W,760)),(0,0)); d=ImageDraw.Draw(c)
for i,cc in enumerate(('#D52B1E','#FFFFFF','#0038A8')): d.rectangle((0,i*6,W,i*6+6),fill=cc)
k='LA ESTACIÓN DEL FUTURO · PARAGUAY'; d.rounded_rectangle((66,676,66+d.textlength(k,font=BK)+36,720),8,fill='#3A7D44'); d.text((84,683),k,font=BK,fill='white')
B=F('BebasNeue-Regular.ttf',104); y=750
for l,cc in [('LA ANDE CONGELA LA TARIFA','white'),('POR UN AÑO Y SUSPENDE','#6DBB78'),('LOS CORTES','#6DBB78')]:
    d.text((62,y),l,font=B,fill=cc); y+=106
y+=24
for l in ['Lo anunció su presidente, Félix Sosa: sin cortes por','falta de pago hasta el 31 de diciembre']:
    d.text((66,y),l,font=F('Barlow-SemiBold.ttf',36),fill='#C9D4DF'); y+=50
f=F('Barlow-SemiBold.ttf',26); d.text((66,1280),'1/7',font=f,fill='#8FA3B8'); d.text((480,1280),'Deslizá »',font=f,fill='#8FA3B8'); t='energiaslatam.com'; d.text((W-66-d.textlength(t,font=F('Barlow-Bold.ttf',28)),1278),t,font=F('Barlow-Bold.ttf',28),fill='white')
c.save(R+'social/'+I+'-c1.jpg',quality=88)
a=im.resize((900,600)); b=c.resize((480,600)); s=Image.new('RGB',(1380,600)); s.paste(a,(0,0)); s.paste(b,(900,0)); s.save('/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/ph13.jpg')
