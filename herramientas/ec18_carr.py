import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ec18/'; os.makedirs(O,exist_ok=True); os.makedirs(R,exist_ok=True)
N=7
EC=['#FFDD00','#0B4EA2','#ED1C24']
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(EC): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
    if kicker: ax.text(70,110,kicker,fontfamily=BC,fontweight='bold',fontsize=26,color=G,va='center')
    ax.text(1010,1295,'energiaslatam.com',fontfamily=BC,fontweight='bold',fontsize=28,color=W,va='center',ha='right')
    ax.text(70,1295,f'{n}/{N}',fontfamily=BC,fontweight='bold',fontsize=24,color=M,va='center')
    if n<N: ax.text(540,1295,'Deslizá  »',fontfamily=B,fontweight='semibold',fontsize=22,color=M,va='center',ha='center')
    return fig,ax
def title(ax,lines,y0=200,size=84,step=92,green_last=True):
    for i,l in enumerate(lines): ax.text(66,y0+i*step,l,fontfamily=BB,fontsize=size,color=G if (green_last and i==len(lines)-1) else W,va='center')
    return y0+len(lines)*step
def cards(ax,items,y0,h=150,gap=24):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.36,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.68,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def big3(ax,y,items,fs=62):
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
        ax.text(100,yy+60,big,fontfamily=BB,fontsize=fs,color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
ID='2026-11-18-ecuador-margen-estacion-congelado'
def save(fig,k):
    fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)

# 1 PORTADA
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · ECUADOR')
for i,(l,c2) in enumerate([('DOCE CENTAVOS',W),('POR GALÓN,',W),('CONGELADOS 23 AÑOS',G)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=92 if i==2 else 116,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
ax.text(70,820,'Es el margen con el que se vende',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,872,'el diésel en Ecuador. Una petrolera',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,924,'con 20 años en el país ya se va.',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1010,'Qué deja para el operador paraguayo.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL NUMERO
fig,ax=base(2,'EL NÚMERO')
y=title(ax,['DOCE CENTAVOS','PARA TRES'],y0=210,size=78,step=88)
big3(ax,y,[('USD 0,12','Margen del diésel premium, por galón'),('SE REPARTE','Entre comercializadoras, estaciones y transportistas'),('23 AÑOS','Sin una actualización integral')],fs=70)
ax.text(70,1180,'No es lo que gana la estación:',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'es lo que queda para toda la cadena.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 LA COMPARACION
fig,ax=base(3,'LA COMPARACIÓN')
y=title(ax,['LOS VECINOS','PAGAN EL TRIPLE'],y0=210,size=76,step=86)
BX=330; BW=620; VMAX=0.36
for i,(pais,val,col) in enumerate([('ECUADOR',0.12,RD),('PERÚ',0.28,W),('COLOMBIA',0.33,G)]):
    yy=y+70+i*150
    ax.text(66,yy+34,pais,fontfamily=BB,fontsize=54,color=W,va='center')
    ax.add_patch(Rectangle((BX,yy+4),BW,60,color=CARD))
    ax.add_patch(Rectangle((BX,yy+4),BW*val/VMAX,60,color=col))
    ax.text(66,yy+92,f'USD {val:.2f}'.replace('.',','),fontfamily=B,fontweight='semibold',fontsize=26,color=M,va='center')
rb(ax,60,900,960,160,CARD); ax.add_patch(Rectangle((60,900),10,160,color=RD))
ax.text(100,958,'CASI EL TRIPLE DE DIFERENCIA',fontfamily=BB,fontsize=54,color=W,va='center')
ax.text(102,1014,'Con el mismo galón de diésel y la misma estación.',fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
ax.text(70,1250,'Margen del diésel por galón.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

# 4 EL BALANCE
fig,ax=base(4,'CÓMO SE VE EN EL BALANCE')
y=title(ax,['TRES CENTAVOS','CADA CIEN DÓLARES'],y0=210,size=68,step=80)
big3(ax,y,[('USD 3.050 M','Vendieron las tres principales cadenas privadas en 2025'),('USD 7,5 M','Lo que les quedó de utilidad neta'),('0,3 %','El margen neto que da esa cuenta')],fs=66)
ax.text(70,1180,'Cerca de 700 de las 1.200 estaciones',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'trabajan apenas en el punto de equilibrio.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 LA MARCA QUE SE VA
fig,ax=base(5,'LA SEÑAL MÁS FUERTE')
y=title(ax,['UNA MARCA','QUE SE VA'],y0=210,size=82,step=92)
big3(ax,y,[('110 ESTACIONES','Las que Terpel puso en venta en Ecuador'),('DESDE 2006','Veinte años en el mercado ecuatoriano'),('HASTA 2030','Plazo de salida de la red afiliada')],fs=58)
ax.text(70,1180,'Se queda con los lubricantes Mobil.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'El negocio de vender combustible, no.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 QUE PIDEN
fig,ax=base(6,'QUÉ PIDE EL GREMIO')
y=title(ax,['DE DOCE','A VEINTIDÓS'],y0=210,size=82,step=92)
cards(ax,[('Primero, igualar a las gasolinas','Llevar el diésel de USD 0,12 a USD 0,19 por galón'),('Después, los dos a USD 0,22','Con subas de un centavo por mes y estudio técnico'),('El Banco Mundial ya lo dijo','En 2023 recomendó subir al menos seis centavos')],y+50,h=150,gap=26)
save(fig,6)

# 7 CIERRE
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['ACÁ EL PRECIO','NO LO FIJA UN DECRETO'],y0=205,size=62,step=76)
cards(ax,[('En Paraguay el margen se mueve','Petropar fija el suyo y los privados el propio'),('El riesgo no es el número','Es que nadie lo vuelva a mirar en 23 años'),('Mirá quién revisa y cada cuánto','Es la letra chica de cualquier precio administrado')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
