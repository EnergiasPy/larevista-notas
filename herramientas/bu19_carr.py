import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw, ImageFont
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/bu19/'
os.makedirs(O,exist_ok=True); os.makedirs(R,exist_ok=True)
C='/home/claude/fotos_mopc/crop/'
ID='2026-11-19-donde-cargan-buses-electricos-san-lorenzo'
N=7; PY=['#D52B1E','#FFFFFF','#0038A8']
F=lambda n,s: ImageFont.truetype('/home/claude/chart/'+n,s)
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
def base(n,kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1])
    ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(PY): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
    if kicker: ax.text(70,110,kicker,fontfamily=BC,fontweight='bold',fontsize=26,color=G,va='center')
    ax.text(1010,1295,'energiaslatam.com',fontfamily=BC,fontweight='bold',fontsize=28,color=W,va='center',ha='right')
    ax.text(70,1295,f'{n}/{N}',fontfamily=BC,fontweight='bold',fontsize=24,color=M,va='center')
    if n<N: ax.text(540,1295,'Deslizá  »',fontfamily=B,fontweight='semibold',fontsize=22,color=M,va='center',ha='center')
    return fig,ax
def title(ax,lines,y0=200,size=84,step=92,green_last=True):
    for i,l in enumerate(lines):
        ax.text(66,y0+i*step,l,fontfamily=BB,fontsize=size,color=G if (green_last and i==len(lines)-1) else W,va='center')
    return y0+len(lines)*step
def cards(ax,items,y0,h=150,gap=24):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.36,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.68,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def big3(ax,y,items,fs=62):
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
        if '|' in big:
            num,uni=big.split('|')
            ax.text(100,yy+60,num,fontfamily=BB,fontsize=fs,color=W,va='center')
            ax.text(100+len(num)*fs*0.46,yy+66,uni,fontfamily=B,fontweight='bold',fontsize=int(fs*0.52),color=W,va='center')
        else:
            ax.text(100,yy+60,big,fontfamily=BB,fontsize=fs,color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k):
    fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)

# ---- 1 PORTADA con foto ----
cw,ch=1080,1350
c=Image.new('RGB',(cw,ch),BG)
ph=Image.open(C+'c1.jpg').convert('RGB'); s=cw/ph.width
ph=ph.resize((cw,round(ph.height*s)),Image.LANCZOS)
c.paste(ph.crop((0,max(0,(ph.height-700)//2),cw,max(0,(ph.height-700)//2)+700)),(0,0))
d=ImageDraw.Draw(c)
for i,cc in enumerate(PY): d.rectangle((0,i*7,cw,i*7+7),fill=cc)
d.text((cw-24-d.textlength('Foto: MOPC',font=F('Barlow-SemiBold.ttf',22)),666),'Foto: MOPC',font=F('Barlow-SemiBold.ttf',22),fill='#E8EEF4')
BK=F('Barlow-Bold.ttf',24); k='LA ESTACIÓN DEL FUTURO · PARAGUAY'
d.rounded_rectangle((66,676,66+d.textlength(k,font=BK)+36,720),8,fill='#3A7D44'); d.text((84,683),k,font=BK,fill='white')
BG1=F('BebasNeue-Regular.ttf',98); y=752
for l,cc in [('DÓNDE CARGAN','white'),('LOS 30 BUSES','white'),('ELÉCTRICOS','#76C46E')]:
    d.text((62,y),l,font=BG1,fill=cc); y+=102
y+=18
for l in ['Seis cargadores rápidos de 180 kW y 1.500 kW','de infraestructura en una sola base.']:
    d.text((66,y),l,font=F('Barlow-SemiBold.ttf',36),fill='#C9D4DF'); y+=50
f=F('Barlow-SemiBold.ttf',26)
d.text((66,1280),'1/7',font=f,fill='#8FA3B8'); d.text((470,1280),'Deslizá »',font=f,fill='#8FA3B8')
t='energiaslatam.com'; d.text((cw-66-d.textlength(t,font=F('Barlow-Bold.ttf',28)),1278),t,font=F('Barlow-Bold.ttf',28),fill='white')
c.save(R+f'{ID}-c1.jpg',quality=92)

# ---- 2 EL NUMERO ----
fig,ax=base(2,'EL NÚMERO')
y=title(ax,['MIL QUINIENTOS','KILOVATIOS'],y0=210,size=80,step=90)
big3(ax,y,[('6 CARGADORES','Rápidos, de 180 kW cada uno, en San Lorenzo'),('1.500|kW','Infraestructura eléctrica de ese solo predio'),('30 BUSES','Toda la flota eléctrica del Estado')],fs=64)
ax.text(70,1180,'Es otro orden de magnitud frente a la',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'potencia contratada de una estación.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# ---- 3 LAS TRES ESTACIONES ----
fig,ax=base(3,'LAS TRES ESTACIONES')
y=title(ax,['DÓNDE SE','ENCHUFAN'],y0=210,size=86,step=96)
cards(ax,[('Oficinas de Gobierno · Asunción','2 cargadores de 180 kW · 1.000 kW instalados'),
          ('Predio del MOPC · San Lorenzo','6 cargadores de 180 kW · 1.500 kW instalados'),
          ('Comando de Ingeniería · provisorio','1 cargador de 180 kW, durante las revisiones')],y+40,h=150,gap=26)
ax.text(70,1120,'Nueve cargadores rápidos en total,',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center')
ax.text(70,1170,'todos de la misma potencia: 180 kW.',fontfamily=B,fontsize=29,color=M,va='center')
ax.text(70,1232,'Las obras las ejecuta el Parque Tecnológico Itaipú.',fontfamily=B,fontsize=25,color=M,va='center')
save(fig,3)

# ---- 4 FOTO CONECTOR ----
cw,ch=1080,1350
c=Image.new('RGB',(cw,ch),BG)
ph=Image.open(C+'c2.jpg').convert('RGB'); s=cw/ph.width
ph=ph.resize((cw,round(ph.height*s)),Image.LANCZOS)
c.paste(ph.crop((0,0,cw,min(ph.height,760))),(0,0))
d=ImageDraw.Draw(c)
for i,cc in enumerate(PY): d.rectangle((0,i*7,cw,i*7+7),fill=cc)
d.text((cw-24-d.textlength('Foto: MOPC',font=F('Barlow-SemiBold.ttf',22)),726),'Foto: MOPC',font=F('Barlow-SemiBold.ttf',22),fill='#E8EEF4')
d.text((66,110),'LA CARGA',font=F('BarlowCondensed-Bold.ttf',30),fill='#76C46E')
yy=820
d.text((62,yy),'15 MINUTOS',font=F('BebasNeue-Regular.ttf',104),fill='white'); yy+=112
d.text((62,yy),'DEL 20 % AL 80 %',font=F('BebasNeue-Regular.ttf',88),fill='#76C46E'); yy+=108
for l in ['Pasar del 80 % al 100 % lleva 40 minutos más:','el último quinto es el más caro en tiempo.']:
    d.text((66,yy),l,font=F('Barlow-SemiBold.ttf',34),fill='#C9D4DF'); yy+=48
f=F('Barlow-SemiBold.ttf',26)
d.text((66,1280),'4/7',font=f,fill='#8FA3B8'); d.text((470,1280),'Deslizá »',font=f,fill='#8FA3B8')
t='energiaslatam.com'; d.text((cw-66-d.textlength(t,font=F('Barlow-Bold.ttf',28)),1278),t,font=F('Barlow-Bold.ttf',28),fill='white')
c.save(R+f'{ID}-c4.jpg',quality=92)

# ---- 5 AUTONOMIA ----
fig,ax=base(5,'POR QUÉ CARGA DE DÍA')
y=title(ax,['SESENTA','KILÓMETROS'],y0=210,size=88,step=98)
big3(ax,y,[('60|km','Autonomía promedio de cada unidad'),('VARIAS VECES','Se enchufa durante la jornada, no solo de noche'),('EN CABECERA','Entre servicio y servicio, como una parada técnica')],fs=60)
ax.text(70,1180,'La carga deja de ser tarea de garaje',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'y pasa a ser parte de la operación.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# ---- 6 QUE SIGNIFICA ----
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['EL LÍMITE NO','ES LA ENERGÍA'],y0=205,size=76,step=86)
cards(ax,[('Es tu acometida','1.500 kW en un predio no se resuelve con obra civil'),
          ('El equipo no es lo caro','Un cargador rápido ronda los USD 50.000'),
          ('Primero la potencia','Después cuántos vehículos por hora, y recién el equipo')],y+40,h=150,gap=26)
save(fig,6)

# ---- 7 CIERRE ----
fig,ax=base(7,'LO QUE VIENE')
y=title(ax,['800 BUSES','AL 2040'],y0=210,size=92,step=100)
big3(ax,y,[('40 %','De la flota metropolitana, según el plan del Estado'),('EN RUTA','Un bus que rinde 60 km no carga en su base'),('YA ESTÁN','Las estaciones están sobre esas rutas')],fs=68)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
