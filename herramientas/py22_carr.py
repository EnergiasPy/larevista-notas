# Carrusel 1080x1350 · Paraguay · litros por estación · 22/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/py22/'; os.makedirs(O,exist_ok=True)
ID='2026-11-22-cuantos-litros-vende-estacion-de-servicio-paraguay'
N=8; BR=['#D52B1E','#FFFFFF','#0038A8']
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
        num,_,uni=big.partition('|')
        tx=ax.text(100,yy+60,num,fontfamily=BB,fontsize=fs,color=W,va='center')
        if uni:
            fig.canvas.draw(); bb=tx.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
            ax.text(x2+14,yy+66,uni,fontfamily=B,fontweight='bold',fontsize=int(fs*0.52),color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k):
    fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)


fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2,sz) in enumerate([('CUÁNTOS LITROS',W,118),('VENDE UNA',W,118),('ESTACIÓN',G,118)]):
    ax.text(66,300+i*132,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,720),140,7,color=G))
for i,l in enumerate(['En promedio, 104.000 litros por mes.','Una de Petropar, el doble.']):
    ax.text(70,800+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1000,'Compará con tu estación: ¿vendés más',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1042,'o menos que el promedio de tu emblema?',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL NÚMERO')
y=title(ax,['EL PROMEDIO','DEL PAÍS'],y0=210,size=88,step=98)
big3(fig,ax,y,[('104.000|litros','Por estación y por mes, entre naftas y gasoil'),('3.400|litros','Por día, en promedio'),('2.880','Estaciones para 300,5 millones de litros')],fs=68)
ax.text(70,1180,'Cuenta propia con datos del MIC:',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'ventas de octubre y estaciones habilitadas.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'POR EMBLEMA')
y=title(ax,['PETROPAR VENDE','EL DOBLE'],y0=210,size=84,step=94)
big3(fig,ax,y,[('215.000|litros','Petropar: 302 estaciones'),('156.000|litros','San Isidro (Energy): 109 estaciones'),('139.000|litros','Shell: 363 estaciones')],fs=66)
ax.text(70,1180,'Litros por estación en octubre.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
save(fig,3)

fig,ax=base(4,'POR EMBLEMA')
y=title(ax,['EL RESTO','DE LA TABLA'],y0=210,size=88,step=98)
rows=[('PETROBRAS','129.000'),('PUMA','105.000'),('PETROMAX','95.000'),('PETROSUR','94.000'),('PETROCHACO','86.000'),('COPETROL','68.000')]
for k,(n,v) in enumerate(rows):
    yy=y+50+k*112; rb(ax,60,yy,960,96,CARD); ax.add_patch(Rectangle((60,yy),10,96,color=G))
    ax.text(100,yy+50,n,fontfamily=BB,fontsize=46,color=W,va='center')
    ax.text(985,yy+50,v,fontfamily=BB,fontsize=50,color=G,va='center',ha='right')
ax.text(70,1226,'Litros por estación y por mes. Valores aproximados.',fontfamily=B,fontsize=25,color=M,va='center')
save(fig,4)

fig,ax=base(5,'CÓMO LEERLO')
y=title(ax,['SON PROMEDIOS,','NO AUDITORÍAS'],y0=210,size=84,step=94)
cards(ax,[('El MIC informa ventas por empresa','Si hay venta mayorista, el promedio real es menor'),
          ('Ventas de octubre, red de noviembre','Sirve para comparar órdenes de magnitud'),
          ('Una ruta no es un barrio','El mismo cartel puede vender diez veces distinto')],y+50,h=150,gap=26)
save(fig,5)

fig,ax=base(6,'CON QUÉ SE COMPARA')
y=title(ax,['UNA RED DENSA','PARA EL MERCADO'],y0=210,size=84,step=94)
big3(fig,ax,y,[('104.000|litros','Paraguay: promedio por estación'),('212.000|litros','Colombia: despacho promedio que informa el gremio'),('350.000|litros','Argentina: lo que hace falta para cubrir costos')],fs=66)
ax.text(70,1180,'Por eso una caída de 15 % en el gasoil',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'se siente tanto.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,6)

fig,ax=base(7,'EL NEGOCIO NO ES SOLO EL COMBUSTIBLE')
y=title(ax,['MEJORÁ','LA TIENDA'],y0=205,size=100,step=108)
cards(ax,[('Punto de retiro de encomiendas','Abrís muchas horas y estás sobre el camino'),
          ('Pago de servicios, giros y recargas','El que paga una factura vuelve todos los meses'),
          ('Café y comida lista','Una parada de dos minutos pasa a ser de diez'),
          ('Baños limpios, wifi y dónde sentarse','Para el que viaja pesan tanto como el precio')],y+30,h=140,gap=20)
ax.text(70,1200,'Más motivos para entrar: más clientes y más litros.',fontfamily=B,fontweight='bold',fontsize=29,color=G,va='center')
save(fig,7)

fig,ax=base(8,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['MEDÍ TUS','LITROS'],y0=205,size=96,step=104)
cards(ax,[('Comparate con tu emblema','Si vendés más que el promedio, negociá con ese dato'),
          ('Litros por día, no solo facturación','El volumen es lo que paga los costos fijos'),
          ('Sumá un servicio y medilo','Empezá por uno y mirá cuánta gente trae')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,8)
print('ok')
