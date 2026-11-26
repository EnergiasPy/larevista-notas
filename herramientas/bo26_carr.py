# Carrusel 1080x1350 · Región · Bolivia · paro de transporte · 26/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/bo26/'; os.makedirs(O,exist_ok=True); os.makedirs(R,exist_ok=True)
ID='2026-11-26-paro-nacional-transporte-bolivia-lunes-diesel'
N=7; BR=['#D52B1E','#F9E300','#007934']
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

# 1 · portada
fig,ax=base(1,'REGIÓN · BOLIVIA')
for i,(l,c2,sz) in enumerate([('PARO NACIONAL',W,118),('DE TRANSPORTE',W,118),('DESDE EL LUNES',G,118)]):
    ax.text(66,310+i*132,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,736),140,7,color=G))
for i,l in enumerate(['Los choferes bolivianos paran','por tiempo indefinido.']):
    ax.text(70,816+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,996,'El motivo: el diésel pasó de Bs 17,95',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1038,'a Bs 20,57 el litro el martes.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 · qué resolvieron
fig,ax=base(2,'QUÉ RESOLVIERON')
y=title(ax,['ARRANCA A LAS 00:00','DEL LUNES 30'],y0=210,size=80,step=92)
cards(ax,[('Lo decidió un ampliado en La Paz','Confederación Sindical de Choferes de Bolivia'),
          ('Se suma Transporte Libre','El paro es general y por tiempo indefinido'),
          ('Cabildo nacional el 7 de diciembre','Ahí definirían nuevas medidas')],y+40,h=150,gap=26)
ax.text(70,1180,'"No es una lucha política partidaria, es una lucha',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'social": Lucio Gómez, secretario ejecutivo.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 · qué piden
fig,ax=base(3,'QUÉ PIDEN')
y=title(ax,['ABROGAR','EL DECRETO 5716'],y0=210,size=92,step=100)
cards(ax,[('Anular el comunicado de la ANH','El que fijó el nuevo precio del diésel'),
          ('Abrogar el DS 5716','Ató el precio interno al costo de importación'),
          ('Sin diálogo hasta entonces','No se sientan a ninguna mesa antes de eso')],y+40,h=150,gap=26)
ax.text(70,1180,'La regla tiene una banda: el precio se mueve',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'cuando la referencia internacional varía más de 5 %.',fontfamily=B,fontsize=26,color=M,va='center')
save(fig,3)

# 4 · la serie
fig,ax=base(4,'EL PRECIO, AÑO A AÑO')
y=title(ax,['DE BS 3,72','A BS 20,57'],y0=210,size=100,step=108)
big3(fig,ax,y,[('3,72|Bs','Hace un año, congelado desde hacía dos décadas'),('9,80|Bs','Diciembre de 2025'),('20,57|Bs','Hoy: cinco veces y media el precio de 2025')],fs=66)
ax.text(70,1180,'En septiembre había saltado a Bs 17,95.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'El martes subió 14,6 % de una sola vez.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 · lo que NO se anunció
fig,ax=base(5,'LO QUE TODAVÍA NO SE ANUNCIÓ')
y=title(ax,['NI BLOQUEOS','NI FRONTERAS'],y0=210,size=96,step=104)
cards(ax,[('No hay bloqueo de rutas anunciado','El gremio habló de unidades guardadas'),
          ('No hay cierre de pasos fronterizos','Tampoco se mencionó en la resolución'),
          ('Son cosas distintas','Un paro no es lo mismo que un bloqueo')],y+40,h=150,gap=26)
ax.text(70,1180,'Lo decimos porque cambia todo para la carga:',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'hasta ahora solo está confirmado el paro.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 · qué significa
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA MIRAR'],y0=205,size=100,step=108)
cards(ax,[('El lunes, los despachos','Primero se siente en las que cargan flotas en el Chaco'),
          ('La brecha se dio vuelta','Diésel: USD 1,75 en Bolivia y cerca de USD 1,40 acá'),
          ('Paraguay le vende combustible','Por Infante Rivarola pasan diésel y gasolina')],y+40,h=150,gap=24)
save(fig,6)

# 7 · cierre
fig,ax=base(7,'LA ESTACIÓN DEL FUTURO')
y=title(ax,['LEÉ LA NOTA','COMPLETA'],y0=420,size=120,step=128)
ax.text(70,760,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=52,color=G,va='center')
ax.text(70,860,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=30,color=W,va='center')
ax.text(70,920,'¿Cargás flotas que cruzan a Bolivia? Contanos.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,7)
print('ok carrusel 7')
