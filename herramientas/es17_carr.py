import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/es17/'; os.makedirs(O,exist_ok=True)
N=6
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#D52B1E','#FFFFFF','#0038A8']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
    if kicker: ax.text(70,110,kicker,fontfamily=BC,fontweight='bold',fontsize=26,color=G,va='center')
    ax.text(1010,1295,'energiaslatam.com',fontfamily=BC,fontweight='bold',fontsize=28,color=W,va='center',ha='right')
    ax.text(70,1295,f'{n}/{N}',fontfamily=BC,fontweight='bold',fontsize=24,color=M,va='center')
    if n<N: ax.text(540,1295,'Deslizá  »',fontfamily=B,fontweight='semibold',fontsize=22,color=M,va='center',ha='center')
    return fig,ax
def title(ax,lines,y0=200,size=84,step=92,green_last=True):
    for i,l in enumerate(lines): ax.text(66,y0+i*step,l,fontfamily=BB,fontsize=size,color=G if (green_last and i==len(lines)-1) else W,va='center')
    return y0+len(lines)*step
def cards(ax,items,y0,h=130,gap=22,big=False):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.38,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.72,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def save(fig,name): fig.savefig(O+name+'.png',facecolor=BG); Image.open(O+name+'.png').convert('RGB').save(R+name+'.jpg',quality=92); plt.close(fig)
def big3(ax,y,items,fs=62):
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
        ax.text(100,yy+60,big,fontfamily=BB,fontsize=fs,color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
ID='2026-11-17-cuantas-estaciones-hay-paraguay-red-emblemas'
def save2(fig,k): save(fig,f'{ID}-c{k}')

fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2) in enumerate([('2.880',G),('ESTACIONES',W),('Y NINGUNA',W),('SIN BANDERA',G)]):
    ax.text(66,290+i*128,l,fontfamily=BB,fontsize=118,color=c2,va='center')
ax.add_patch(Rectangle((70,810),140,7,color=G))
ax.text(70,886,'Cuántas hay, de quién son',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,938,'y dónde están.',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1020,'Registro del MIC al 17 de noviembre.',fontfamily=B,fontsize=29,color=M,va='center')
save2(fig,1)

fig,ax=base(2,'EL RANKING')
y=title(ax,['QUIÉN TIENE','MÁS BOCAS'],y0=210)
D=[('COPETROL','387','13,4 %'),('SHELL','363','12,6 %'),('PETROPAR','302','10,5 %'),('PETROBRAS','245','8,5 %'),('PUMA','180','6,3 %'),('PETROSUR','160','5,6 %')]
for k,(n,v,p) in enumerate(D):
    yy=y+40+k*104; rb(ax,60,yy,960,88,CARD); ax.add_patch(Rectangle((60,yy),10,88,color=G))
    ax.text(100,yy+46,n,fontfamily=BB,fontsize=48,color=W,va='center')
    ax.text(730,yy+46,v,fontfamily=BB,fontsize=48,color=W,va='center',ha='right')
    ax.text(985,yy+46,p,fontfamily=B,fontweight='bold',fontsize=27,color=G,va='center',ha='right')
save2(fig,2)

fig,ax=base(3,'CONCENTRACIÓN')
y=title(ax,['CINCO MARCAS,','MEDIA RED'],y0=210,size=78,step=88)
big3(ax,y,[('51,3 %','Lo que concentran las cinco primeras marcas'),('23','Las marcas que operan en el país'),('0','Estaciones sin bandera en el registro')],fs=86)
ax.text(70,1180,'En otros países la estación blanca pesa.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'Acá, según el registro oficial, no existe.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,3)

fig,ax=base(4,'LAS QUE NO FIGURAN CON EMBLEMA')
y=title(ax,['322 ESTACIONES','DE CUATRO DUEÑOS'],y0=210,size=66,step=78)
cards(ax,[('Energy · Inversiones San Isidro','109 estaciones'),('TEGA','99 estaciones'),('Enercon · San Luis','63 estaciones'),('Yguazú Combustibles','51 estaciones')],y+40,h=128,gap=22)
ax.text(70,1200,'Juntas serían la tercera red del país.',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center')
save2(fig,4)

fig,ax=base(5,'DÓNDE ESTÁN')
y=title(ax,['UN TERCIO EN','EL ÁREA METRO'],y0=210,size=76,step=86)
big3(ax,y,[('928','Central y Asunción: el 32,2 % del país'),('90','Todo el Chaco: el 3,1 %'),('13','Alto Paraguay, el departamento con menos')],fs=92)
ax.text(70,1180,'Central 739 · Alto Paraná 364 · Caaguazú 252',fontfamily=B,fontweight='bold',fontsize=28,color=W,va='center')
ax.text(70,1226,'Itapúa 240 · San Pedro 225 · Asunción 189',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,5)

fig,ax=base(6,'QUÉ TIENE QUE REVISAR LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA HOY'],y0=210)
cards(ax,[('Mirá tu distrito, no el país','En Central competís con 739; en Ñeembucú, con 43'),('Abanderarse es la norma','La pregunta no es si tener bandera: es cuál y con qué contrato'),('El Chaco sigue abierto','90 estaciones para más de la mitad del territorio')],y+60,h=150,gap=26)
ax.text(70,1118,'Mirá el mapa en energiaslatam.com/estaciones',fontfamily=B,fontweight='bold',fontsize=31,color=G,va='center')
ax.text(70,1176,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save2(fig,6)
print('ok')
