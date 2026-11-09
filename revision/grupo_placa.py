from PIL import Image, ImageDraw, ImageFont
F='/home/claude/chart/'; f=lambda n,s: ImageFont.truetype(F+n,s)
W,H=1080,1350; NV=(15,33,61); CARD=(23,48,90); W1=(244,246,249); MU=(159,179,200); GL=(118,196,110); GR=(58,150,62)
im=Image.new('RGB',(W,H),NV); d=ImageDraw.Draw(im)
for i,c in enumerate([(213,43,30),(255,255,255),(0,56,168)]): d.rectangle([0,i*7,W,i*7+7],fill=c)
d.text((70,70),'NUEVO GRUPO DE FACEBOOK',font=f('BarlowCondensed-Bold.ttf',30),fill=GL)
y=118
d.text((66,y),'SUMATE AL GRUPO',font=f('BebasNeue-Regular.ttf',104),fill=W1)
y=200
cov=Image.open('/home/claude/larevista-notas/site/brand/fb-grupo-portada-1640x856.jpg').convert('RGB')
cw=940; ch=int(cw*cov.height/cov.width); cov=cov.resize((cw,ch),Image.LANCZOS)
m=Image.new('L',(cw,ch),0); ImageDraw.Draw(m).rounded_rectangle([0,0,cw-1,ch-1],18,fill=255)
cy=y+40; im.paste(cov,(70,cy),m)
y=cy+ch+40
for t,s in [('Precios y novedades del sector','Petropar, emblemas, MIC y la región'),('Consultas entre colegas','Proveedores, equipos, personal y trámites'),('Sin spam ni ventas','Un espacio para operadores, con reglas claras')]:
    d.rounded_rectangle([60,y,1020,y+104],14,fill=CARD); d.rectangle([60,y,70,y+104],fill=GL)
    d.text((100,y+18),t,font=f('Barlow-Bold.ttf',32),fill=W1); d.text((100,y+58),s,font=f('Barlow-SemiBold.ttf',24),fill=MU); y+=118
d.rounded_rectangle([170,y+18,910,y+108],24,fill=GR)
s='Sumate gratis · link en el posteo'; tw=d.textlength(s,font=f('Barlow-Bold.ttf',36)); d.text(((W-tw)/2,y+38),s,font=f('Barlow-Bold.ttf',36),fill=(255,255,255))
d.text((1010,1300),'energiaslatam.com',font=f('BarlowCondensed-Bold.ttf',28),fill=W1,anchor='rm')
d.text((70,1300),'Energías LATAM',font=f('BarlowCondensed-Bold.ttf',28),fill=MU,anchor='lm')
print(y+108); im.save('/home/claude/larevista-notas/img/social/grupo-fb-invitacion.jpg',quality=92)
