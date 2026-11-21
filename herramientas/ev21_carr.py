# Carrusel 1080x1350 · Paraguay · Paraguay · cliente eléctrico · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ev21/'; os.makedirs(O,exist_ok=True)
ID='2026-11-21-media-hora-para-cargar-estaciones-cliente-electrico'
N=7; BR=['#D52B1E','#FFFFFF','#0038A8']
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
def base(n,kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(BR): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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
def big3(fig,ax,y,items,fs=62):
    # numero en Bebas; si trae "|unidad", la unidad va en Barlow (Bebas es solo mayusculas)
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
        num,_,uni=big.partition('|'); x0=100
        if num.startswith('BS '):
            p=ax.text(100,yy+66,'Bs',fontfamily=B,fontweight='bold',fontsize=int(fs*0.62),color=W,va='center')
            fig.canvas.draw(); bb=p.get_window_extent(); x0=ax.transData.inverted().transform((bb.x1,0))[0]+10; num=num[3:]
        tx=ax.text(x0,yy+60,num,fontfamily=BB,fontsize=fs,color=W,va='center')
        if uni:
            fig.canvas.draw(); bb=tx.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
            ax.text(x2+14,yy+66,uni,fontfamily=B,fontweight='bold',fontsize=int(fs*0.52),color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k):
    fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)




# 1 PORTADA
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · ELECTROMOVILIDAD · PARAGUAY')
for i,(l,c2) in enumerate([('MEDIA HORA',W),('PARA CARGAR.',W),('¿ESTÁ LISTA',G),('TU ESTACIÓN?',G)]):
    ax.text(66,290+i*132,l,fontfamily=BB,fontsize=124,color=c2,va='center')
ax.add_patch(Rectangle((70,800),140,7,color=G))
for i,l in enumerate(['El cliente eléctrico espera entre','20 minutos y una hora. Ese tiempo','vale plata, si tenés qué ofrecerle.']):
    ax.text(70,880+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1090,'Cuánto cuesta el cargador y cuántas',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1132,'recargas por día hacen falta para pagarlo.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 TIEMPOS
fig,ax=base(2,'CUÁNTO ESPERA EL CLIENTE')
y=title(ax,['EL TIEMPO LO','PONE EL CARGADOR'],y0=210,size=84,step=94)
big3(fig,ax,y,[('12|minutos','Con un cargador rápido de 150 kW'),('30|minutos','Con un cargador rápido de 60 kW'),('1|hora y 22 minutos','Con un equipo de 22 kW en corriente alterna')],fs=68)
ax.text(70,1180,'Para sumar 30 kWh: de 30 % a 80 %',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'en una batería de 60 kWh. Mínimo teórico.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 QUE OFRECER
fig,ax=base(3,'QUÉ OFRECER')
y=title(ax,['CADA ESPERA','PIDE OTRA COSA'],y0=210,size=88,step=98)
cards(ax,[('Parada corta','Café con chipa o un pedido por QR listo para retirar'),
          ('Media hora','Almuerzo rápido, mesa con wifi y enchufes'),
          ('Estación de ruta','Baño limpio, cambiador y un lugar climatizado')],y+50,h=150,gap=26)
save(fig,3)

# 4 INVERSION
fig,ax=base(4,'CUÁNTO CUESTA')
y=title(ax,['EL PRIMER PASO:','G. 265 MILLONES'],y0=210,size=84,step=94)
big3(fig,ax,y,[('G. 265|millones','Un punto de carga rápida de 150 kW'),('G. 175|millones','De ese total, el equipo'),('G. 36|millones','El transformador de 200 kVA')],fs=68)
ax.text(70,1180,'Presupuesto de un proyecto de la',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'Universidad Nacional de Caaguazú.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 LA CUENTA
fig,ax=base(5,'LA CUENTA')
y=title(ax,['CINCO RECARGAS','POR DÍA'],y0=210,size=88,step=98)
big3(fig,ax,y,[('G. 30.000|por recarga','30 kWh con un margen supuesto de G. 1.000 por kWh'),('5|recargas por día','Para recuperar G. 265 millones'),('5|años','Antes de cargos fijos, impuestos y financiación')],fs=68)
ax.text(70,1180,'Lo que el cliente gasta en la tienda',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'mientras espera mejora esa cuenta.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 ANTES DE COMPRAR
fig,ax=base(6,'ANTES DE COMPRAR')
y=title(ax,['TRES COSAS','PARA AVERIGUAR'],y0=210,size=88,step=98)
cards(ax,[('Consulta previa a la ANDE','Cuánta potencia tiene disponible tu predio'),
          ('Qué tarifa eléctrica te corresponde','Y qué cargos fijos tendría el cargador'),
          ('La ley ya lo permite','La Ley 6925 habilita a las estaciones a vender recarga')],y+50,h=150,gap=26)
save(fig,6)

# 7 CIERRE
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['CUATRO','PREGUNTAS'],y0=205,size=88,step=98)
cards(ax,[('¿Hiciste la cuenta?','Cargador, recargas por día y gasto en la tienda'),
          ('¿Tenés buen café?','Media hora alcanza para consumir'),
          ('¿Qué tal está tu tienda?','Mesas, wifi, enchufes y aire acondicionado'),
          ('¿Cómo están tus baños?','En la ruta deciden dónde para una familia')],y+30,h=128,gap=18)
ax.text(70,1160,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1210,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
