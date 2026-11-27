# Portada con foto (-1.jpg) y foto 3:2 (-3.jpg) · Baja el gas de garrafa · 27/11/2026
from PIL import Image, ImageDraw, ImageFont
NV=(12,26,41); GR='#3A7D44'
ID='2026-11-27-baja-el-gas-de-garrafa-paraguay-petropar-nande-gas'
R='/home/claude/larevista-notas/img/'; SRC='/home/claude/fotos_gas/g1.jpg'
PY_=('#D52B1E','#FFFFFF','#0038A8')
F=lambda n,s: ImageFont.truetype('/home/claude/chart/'+n,s)
CRED='Foto: Petropar'

# ---------- -1.jpg : portada, foto a sangre con velo ----------
W,H=1600,1067; PH=967
ph=Image.open(SRC).convert('RGB')
s=max(W/ph.width,PH/ph.height); ph=ph.resize((round(ph.width*s),round(ph.height*s)),Image.LANCZOS)
x=(ph.width-W)//2; y=(ph.height-PH)//2
im=Image.new('RGB',(W,H),NV); im.paste(ph.crop((x,y,x+W,y+PH)),(0,0))

# velo: transparente arriba, azul marino abajo
velo=Image.new('RGBA',(W,PH),NV+(0,)); px=velo.load()
for yy in range(PH):
    if yy<210: a=0
    elif yy<600: a=int(234*((yy-210)/390)**1.15)
    else: a=234
    for xx in range(W): px[xx,yy]=NV+(a,)
base=im.convert('RGBA'); base.alpha_composite(velo,(0,0)); im=base.convert('RGB')

d=ImageDraw.Draw(im)
for i,c in enumerate(PY_): d.rectangle((0,i*6,W,i*6+6),fill=c)
d.text((W-40-d.textlength(CRED,font=F('Barlow-SemiBold.ttf',22)),PH-38),CRED,font=F('Barlow-SemiBold.ttf',22),fill='#C9D4DF')

X=80; BK=F('Barlow-Bold.ttf',24); k='PARAGUAY · MERCADO Y PRECIOS'
d.rounded_rectangle((X,500,X+d.textlength(k,font=BK)+36,544),8,fill=GR); d.text((X+18,507),k,font=BK,fill='white')
BG=F('BebasNeue-Regular.ttf',92); yy=592
for l,c in [('BAJA EL GAS DE GARRAFA','white'),('EN PARAGUAY','#6DBB78')]:
    d.text((X-4,yy),l,font=BG,fill=c); yy+=98
d.rectangle((X,yy+26,X+140,yy+32),fill='#6DBB78'); yy+=64
for l in ['Desde hoy, el Ñande Gas de Petropar cuesta G. 600 menos por kilo:','G. 6.000 menos por cada garrafa de 10 kilos. Naftas y diésel, sin cambios.']:
    d.text((X,yy),l,font=F('Barlow-SemiBold.ttf',28),fill='#D7E0E9'); yy+=42

bs=F('BebasNeue-Regular.ttf',40)
d.text((X,985),'LA ESTACIÓN',font=bs,fill='white')
d.text((X+d.textlength('LA ESTACIÓN ',font=bs),985),'DEL FUTURO',font=bs,fill='#6DBB78')
t='energiaslatam.com'; f=F('Barlow-SemiBold.ttf',24)
d.text((W-80-d.textlength(t,font=f),995),t,font=f,fill='white')
im.save(R+ID+'-1.jpg',quality=88); print('ok -1 portada con foto')

# ---------- -3.jpg : la foto, 3:2, con crédito ----------
p=Image.open(SRC).convert('RGB')
s=1500/p.width; p=p.resize((1500,round(p.height*s)),Image.LANCZOS)
yy=max(0,(p.height-1000)//2); p=p.crop((0,yy,1500,yy+min(1000,p.height)))
im3=Image.new('RGB',(1500,p.height+50),NV); im3.paste(p,(0,0))
ImageDraw.Draw(im3).text((22,p.height+12),CRED,font=F('Barlow-SemiBold.ttf',22),fill='#C9D4DF')
im3.save(R+ID+'-3.jpg',quality=90); print('ok -3 foto', im3.size)
