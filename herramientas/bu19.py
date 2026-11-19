import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw, ImageFont
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
ID='2026-11-19-donde-cargan-buses-electricos-san-lorenzo'; R='/home/claude/larevista-notas/img/'
C='/home/claude/fotos_mopc/crop/'
PY=('#D52B1E','#FFFFFF','#0038A8')
F=lambda n,s: ImageFont.truetype('/home/claude/chart/'+n,s)

# ---------- -1.jpg : placa con foto (portada) ----------
W,H=1600,1067
im=Image.new('RGB',(W,H),NV)
ph=Image.open(C+'c1.jpg').convert('RGB')
s=H/ph.height; ph=ph.resize((round(ph.width*s),H),Image.LANCZOS)
x=max(0,(ph.width-760)//2); im.paste(ph.crop((x,0,x+760,H)),(0,0))
d=ImageDraw.Draw(im)
for i,c in enumerate(PY): d.rectangle((0,i*6,W,i*6+6),fill=c)
d.text((24,H-40),'Foto: MOPC',font=F('Barlow-SemiBold.ttf',22),fill='#E8EEF4')
X=830; BK=F('Barlow-Bold.ttf',24); k='PARAGUAY · ELECTROMOVILIDAD'
d.rounded_rectangle((X,110,X+d.textlength(k,font=BK)+36,154),8,fill=GR); d.text((X+18,117),k,font=BK,fill='white')
BG=F('BebasNeue-Regular.ttf',88); y=205
for l,c in [('SEIS CARGADORES','white'),('RÁPIDOS PARA','white'),('TREINTA BUSES','#6DBB78')]:
    d.text((X-4,y),l,font=BG,fill=c); y+=94
d.rectangle((X,y+28,X+140,y+34),fill='#6DBB78'); y+=66
for l in ['Son de 180 kW cada uno y la base de San Lorenzo','tiene 1.500 kW. Cada bus rinde 60 kilómetros.']:
    d.text((X,y),l,font=F('Barlow-SemiBold.ttf',30),fill='#C9D4DF'); y+=44
y+=46
# "1.500" en Bebas y "kW" en Barlow, para no romper el simbolo
fnum=F('BebasNeue-Regular.ttf',76); funi=F('Barlow-Bold.ttf',46)
d.text((X,y),'1.500',font=fnum,fill='white')
d.text((X+d.textlength('1.500',font=fnum)+14,y+26),'kW',font=funi,fill='white')
d.text((X,y+86),'Potencia instalada del predio del MOPC',font=F('Barlow-SemiBold.ttf',26),fill='#8FA3B8')
bs=F('BebasNeue-Regular.ttf',40)
d.text((X,985),'LA ESTACIÓN',font=bs,fill='white')
d.text((X+d.textlength('LA ESTACIÓN ',font=bs),985),'DEL FUTURO',font=bs,fill='#6DBB78')
t='energiaslatam.com'; f=F('Barlow-SemiBold.ttf',24)
d.text((W-60-d.textlength(t,font=f),995),t,font=f,fill='white')
im.save(R+ID+'-1.jpg',quality=88)

# ---------- -2.jpg : placa de datos ----------
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1])
ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(PY): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'PARAGUAY · ELECTROMOVILIDAD',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'DÓNDE CARGAN, Y CON CUÁNTA POTENCIA',fontfamily=BB,fontsize=58,color=NV,va='center')
ax.text(80,214,'Las tres estaciones de carga de los 30 buses eléctricos del Estado',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
est=[('OFICINAS DE GOBIERNO · ASUNCIÓN','2 cargadores de 180 kW','1.000',NV,'Terminada'),
     ('PREDIO DEL MOPC · SAN LORENZO','6 cargadores de 180 kW','1.500',GR,'Base de recarga y mantenimiento'),
     ('COMANDO DE INGENIERÍA · PROVISORIO','1 cargador de 180 kW','180',RD,'Durante las revisiones técnicas')]
for i,(t1,t2,big,col,pie) in enumerate(est):
    y=300+i*150; rb(ax,80,y,1440,130,SO,10); ax.add_patch(Rectangle((80,y),8,130,color=col))
    ax.text(120,y+38,t1,fontfamily=B,fontweight='bold',fontsize=23,color=MU,va='center')
    ax.text(120,y+84,t2,fontfamily=B,fontweight='semibold',fontsize=27,color=NV,va='center')
    ax.text(1480,y+54,'kW',fontfamily=B,fontweight='bold',fontsize=30,color=col,va='center',ha='right')
    ax.text(1430,y+54,big,fontfamily=BB,fontsize=62,color=col,va='center',ha='right')
    ax.text(1480,y+100,pie,fontfamily=B,fontsize=20,color=MU,va='center',ha='right')
rb(ax,80,762,1440,66,NV,10)
ax.text(120,795,'60 KM DE AUTONOMÍA · DEL 20 % AL 80 % DE BATERÍA EN 15 MINUTOS',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
ax.add_patch(Rectangle((80,862),1440,1,color='#DCE3EA'))
ax.text(80,900,'Datos: documento técnico del Viceministerio de Transporte del MOPC, Acciones para la electrificación del transporte público del AMA.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center')
ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('/tmp/w.png',facecolor='white'); Image.open('/tmp/w.png').convert('RGB').save(R+ID+'-2.jpg',quality=88); plt.close(fig)

# ---------- -3/-4/-5 : fotos limpias 1600x1067 ----------
for n,src in [('-3','c2.jpg'),('-4','c3.jpg'),('-5','c4.jpg')]:
    p=Image.open(C+src).convert('RGB').resize((1600,1067),Image.LANCZOS)
    dd=ImageDraw.Draw(p)
    dd.rectangle((0,1067-46,1600,1067),fill=(12,26,41))
    dd.text((24,1067-36),'Foto: MOPC',font=F('Barlow-SemiBold.ttf',24),fill='#E8EEF4')
    p.save(R+ID+n+'.jpg',quality=88)
print('ok')
