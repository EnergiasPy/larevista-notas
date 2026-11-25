# Carrusel 1080x1350 · Paraguay · Gulf en Paraguay · el lanzamiento · 25/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/gu25/'; os.makedirs(O,exist_ok=True)
ID='2026-11-25-gulf-paraguay-lanzamiento-modelo-licencia-operadores'
N=6; BR=['#D52B1E','#FFFFFF','#0038A8']
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
for i,(l,c2,sz) in enumerate([('GULF PONE',W,138),('EL CARTEL,',W,138),('NO LA OPERACIÓN',G,112)]):
    ax.text(66,280+i*160,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['Qué les ofrecieron la marca y ANJOR','a los dueños de estaciones.']):
    ax.text(70,820+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1000,'El lanzamiento fue el martes en Asunción.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL MODELO')
y=title(ax,['UNA LICENCIA','DE MARCA'],y0=210,size=100,step=108)
cards(ax,[('Gulf no opera estaciones','Licencia la marca y la mantiene vigente'),
          ('No se mete en los precios','Lo dijo su vicepresidente para América Latina'),
          ('La operación es local','ANJOR tiene la licencia en Paraguay')],y+40,h=150,gap=26)
save(fig,2)

fig,ax=base(3,'LA PROMESA')
y=title(ax,['CAMBIAR EL CARTEL','SUBE LAS VENTAS'],y0=210,size=88,step=98)
cards(ax,[('Lo midieron en Brasil y en la Argentina','Según la marca'),
          ('Más ventas y más productos premium','Es lo que dicen haber visto'),
          ('No dieron cifras','El dato que falta para decidir')],y+40,h=150,gap=26)
save(fig,3)

fig,ax=base(4,'LA RED')
y=title(ax,['LOS NÚMEROS','QUE MOSTRÓ GULF'],y0=210,size=92,step=102)
cards(ax,[('Argentina: 126 bocas','Licencia renovada por otras 200'),
          ('Chile: 105 en plan','Brasil: más de 350 en plan'),
          ('México: 200 bocas','Estados Unidos: estaciones en 22 estados'),
          ('Paraguay: 30 en la primera etapa','Cambios de emblema previstos')],y+30,h=140,gap=20)
save(fig,4)

fig,ax=base(5,'EL PEDIDO DE ANJOR')
y=title(ax,['SUMAR LITROS','PARA NEGOCIAR'],y0=210,size=100,step=108)
ax.text(70,y+90,'«Ser independiente no significa',fontfamily=B,fontweight='bold',fontsize=46,color=W,va='center')
ax.text(70,y+150,'tener que estar solos.»',fontfamily=B,fontweight='bold',fontsize=46,color=W,va='center')
ax.text(70,y+220,'Lucas Velasco, presidente de ANJOR',fontfamily=B,fontsize=30,color=G,va='center')
cards(ax,[('La fuerza está fragmentada','Propuso sumar litros, estaciones y presencia'),
          ('Pensar el negocio a diez años','Fue su cierre ante los operadores')],y+300,h=150,gap=24)
save(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA MIRAR'],y0=205,size=100,step=108)
cards(ax,[('Tu contrato es con ANJOR','Abastecimiento, logística y condiciones'),
          ('Pedí el número','Cuánto suben las ventas y en qué plazo'),
          ('Sumar volumen tiene un precio','Exclusividad y plazos: leelos antes de firmar')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,6)
