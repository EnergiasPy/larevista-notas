# Portada con foto (-1.jpg) y foto del saludo (-3.jpg) · Milei en Paraguay · 27/11/2026
from PIL import Image, ImageDraw, ImageFont
NV='#0C1A29'; GR='#3A7D44'
ID='2026-11-27-gasoducto-bioceanico-vaca-muerta-chaco-paraguay-milei'
R='/home/claude/larevista-notas/img/'; C='/home/claude/fotos_milei/crop/'
PY_=('#D52B1E','#FFFFFF','#0038A8')
F=lambda n,s: ImageFont.truetype('/home/claude/chart/'+n,s)
CRED='Foto: Presidencia de la Nación Argentina'

# ---------- -1.jpg : portada con foto ----------
W,H=1600,1067
im=Image.new('RGB',(W,H),NV)
ph=Image.open(C+'c1.jpg').convert('RGB')
s=H/ph.height; ph=ph.resize((round(ph.width*s),H),Image.LANCZOS)
x=max(0,(ph.width-760)//2); im.paste(ph.crop((x,0,x+760,H)),(0,0))
d=ImageDraw.Draw(im)
for i,c in enumerate(PY_): d.rectangle((0,i*6,W,i*6+6),fill=c)
d.text((24,H-40),CRED,font=F('Barlow-SemiBold.ttf',22),fill='#E8EEF4')
X=830; BK=F('Barlow-Bold.ttf',24); k='PARAGUAY · ENERGÍA'
d.rounded_rectangle((X,110,X+d.textlength(k,font=BK)+36,154),8,fill=GR); d.text((X+18,117),k,font=BK,fill='white')
BG=F('BebasNeue-Regular.ttf',88); y=205
for l,c in [('MILEI EN PARAGUAY:','white'),('¿QUÉ SE GANA CON','white'),('EL GAS ARGENTINO?','#6DBB78')]:
    d.text((X-4,y),l,font=BG,fill=c); y+=94
d.rectangle((X,y+28,X+140,y+34),fill='#6DBB78'); y+=66
for l in ['Dos proyectos distintos: un gasoducto hacia Brasil','por el Chaco y una conexión para importar de Formosa.']:
    d.text((X,y),l,font=F('Barlow-SemiBold.ttf',28),fill='#C9D4DF'); y+=42
y+=48
fnum=F('BebasNeue-Regular.ttf',76); funi=F('Barlow-Bold.ttf',40)
d.text((X,y),'USD',font=funi,fill='white')
off=d.textlength('USD ',font=funi)
d.text((X+off,y-14),'2.000',font=fnum,fill='white')
d.text((X+off+d.textlength('2.000',font=fnum)+14,y),'millones',font=funi,fill='white')
d.text((X,y+78),'Inversión estimada del gasoducto bioceánico',font=F('Barlow-SemiBold.ttf',26),fill='#8FA3B8')
bs=F('BebasNeue-Regular.ttf',40)
d.text((X,985),'LA ESTACIÓN',font=bs,fill='white')
d.text((X+d.textlength('LA ESTACIÓN ',font=bs),985),'DEL FUTURO',font=bs,fill='#6DBB78')
t='energiaslatam.com'; f=F('Barlow-SemiBold.ttf',24)
d.text((W-40-d.textlength(t,font=f),995),t,font=f,fill='white')
im.save(R+ID+'-1.jpg',quality=88); print('ok -1 portada con foto')

# ---------- -3.jpg : foto del saludo, 3:2 ----------
p=Image.open(C+'c2.jpg').convert('RGB').resize((1500,1000),Image.LANCZOS)
im3=Image.new('RGB',(1500,1050),NV); im3.paste(p,(0,0))
d3=ImageDraw.Draw(im3)
d3.text((22,1012),CRED,font=F('Barlow-SemiBold.ttf',22),fill='#C9D4DF')
im3.save(R+ID+'-3.jpg',quality=88); print('ok -3 saludo')
