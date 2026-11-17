import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/pe17/'; os.makedirs(O,exist_ok=True)
N=6
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#D91023','#FFFFFF','#D91023']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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
ID='2026-11-17-peru-grifos-inventario-diario-osinergmin-sunat'
def save2(fig,k): save(fig,f'{ID}-c{k}')

fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · PERÚ')
for i,(l,c2) in enumerate([('EL GRIFO QUE',W),('NO DECLARA',W),('NO PUEDE COMPRAR',G)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=104 if i==2 else 116,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
ax.text(70,820,'En Perú la estación carga su stock',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,872,'todos los días. El que no reporta,',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,924,'queda sin poder cargar combustible.',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1010,'Lo que viene para el sector.',fontfamily=B,fontsize=30,color=M,va='center')
save2(fig,1)

fig,ax=base(2,'LO QUE YA RIGE')
y=title(ax,['DECLARAR','TODOS LOS DÍAS'],y0=210,size=76,step=86)
big3(ax,y,[('DIARIO','La estación carga su inventario en la plataforma del regulador'),('SIN DECLARAR','No puede comprar en las plantas de venta'),('DESDE MAYO','Rige para todos los locales de expendio')],fs=70)
ax.text(70,1180,'El registro también condiciona los pedidos',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'con los que la estación se abastece.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,2)

fig,ax=base(3,'DE DÓNDE SALIÓ')
y=title(ax,['EMPEZÓ CON','UNA EMERGENCIA'],y0=210,size=72,step=84)
cards(ax,[('5 de marzo: emergencia del gas','Catorce días de emergencia en el suministro de gas natural'),('Los grifos de Lima sin GNV','Colas, reventa y denuncias por especulación'),('El punto ciego','El Estado no sabía cuánto producto había en cada tanque')],y+50,h=150,gap=26)
save2(fig,3)

fig,ax=base(4,'LO QUE VIENE')
y=title(ax,['DESDE FEBRERO,','CADA MOVIMIENTO'],y0=210,size=68,step=80)
big3(ax,y,[('1 DE FEBRERO DE 2027','Arranca el registro diario de operaciones'),('PÉRDIDAS Y DERRAMES','También hay que informar excedentes y desmedros'),('31 DE ENERO','Hasta ahí se calcula el inventario inicial')],fs=58)
ax.text(70,1180,'La declaración se presenta consolidada',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'una vez por mes, pero el registro es diario.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,4)

fig,ax=base(5,'LA COMPARACIÓN')
y=title(ax,['PARAGUAY','DECLARA AL MES'],y0=210,size=76,step=86)
big3(ax,y,[('MENSUAL','Lo que se declara acá al Ministerio de Industria y Comercio'),('SEPTIEMBRE','El último mes de ventas publicado, a mediados de noviembre'),('EL DÍA ANTERIOR','Lo que va a tener el regulador peruano')],fs=64)
ax.text(70,1180,'La distancia con Perú es de tiempo,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'no de concepto.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,5)

fig,ax=base(6,'QUÉ TIENE QUE REVISAR LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA HOY'],y0=210)
cards(ax,[('¿Medís el tanque todos los días?','Con varilla y planilla no se sostiene un reporte diario'),('¿El dato sale solo de tu sistema?','Si alguien lo transcribe a mano, se va a romper'),('Conciliá stock contra ventas','Una merma rara aparece en el día, no a fin de mes')],y+60,h=150,gap=26)
ax.text(70,1118,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1176,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save2(fig,6)
print('ok')
