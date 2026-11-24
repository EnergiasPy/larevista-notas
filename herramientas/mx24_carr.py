# Carrusel 1080x1350 · Paraguay · México · margen de la gasolinera · 24/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/mx24/'; os.makedirs(O,exist_ok=True)
ID='2026-11-24-cuanto-gana-una-gasolinera-en-mexico-margen'
N=7; BR=['#006847','#FFFFFF','#CE1126']
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



fig,ax=base(1,'REGIÓN · MÉXICO')
for i,(l,c2,sz) in enumerate([('CUÁNTO GANA',W,150),('UNA GASOLINERA',W,128),('EN MÉXICO',G,150)]):
    ax.text(66,300+i*150,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['1,50 pesos brutos por litro de diésel.','Y un precio de venta con techo.']):
    ax.text(70,820+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1000,'El punto de equilibrio se estima en',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1042,'390.000 litros por mes.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL MARGEN')
y=title(ax,['OCHO CENTAVOS','DE DÓLAR POR LITRO'],y0=210,size=84,step=94)
big3(fig,ax,y,[('1,50|pesos','Margen bruto por litro de diésel'),('2|pesos','Lo que superaba a comienzos de año'),('1,55|pesos','Costo de operación estimado en Hermosillo')],fs=68)
ax.text(70,1180,'Con eso se pagan flete, sueldos,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'almacenamiento y financiamiento. Datos de Onexpo.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'EL PRECIO')
y=title(ax,['UN SURTIDOR','CON TECHO'],y0=210,size=100,step=108)
cards(ax,[('Magna: menos de 24 pesos el litro','Acuerdo voluntario con el gobierno, renovado en agosto'),
          ('Diésel: tope de 27 pesos','Vigente desde abril'),
          ('Promedios: 23,69 y 26,97 pesos','Unos USD 1,25 y USD 1,42 por litro, según Profeco')],y+40,h=150,gap=26)
ax.text(70,1180,'Si el costo sube y el precio no se mueve,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'la diferencia sale del margen de la estación.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

fig,ax=base(4,'EL VOLUMEN')
y=title(ax,['EL NÚMERO QUE DECIDE:','LOS LITROS'],y0=210,size=78,step=90)
big3(fig,ax,y,[('200.000|litros','Por mes o menos: la mayoría pierde'),('300.000|litros','Desde ahí el equilibrio es alcanzable'),('390.000|litros','Punto de equilibrio promedio estimado')],fs=68)
ax.text(70,1180,'Lo dijo un expresidente de Onexpo,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'el gremio de las estaciones mexicanas.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

fig,ax=base(5,'EL MERCADO')
y=title(ax,['14.325 ESTACIONES,','62 % CON MARCA PEMEX'],y0=210,size=78,step=90)
cards(ax,[('Pemex: 8.925 estaciones','Casi dos de cada tres'),
          ('392 marcas privadas','Se reparten las otras 5.400'),
          ('Mobil 713 · G500 491 · Valero 337','Las tres privadas con más estaciones')],y+40,h=150,gap=26)
ax.text(70,1180,'Conteo de PetroIntelligence a mayo de 2026.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA MIRAR'],y0=205,size=100,step=108)
cards(ax,[('El margen dice poco sin los litros','México: equilibrio en 390.000. Paraguay vende 104.000'),
          ('Un precio con techo se paga con margen','Miralo cuando se discuta un acuerdo de precios'),
          ('Lo que no es combustible gana peso','Tienda, servicios y pagos sostienen la cuenta')],y+40,h=150,gap=24)
save(fig,6)

fig,ax=base(7,'LA ESTACIÓN DEL FUTURO')
y=title(ax,['LEÉ LA NOTA','COMPLETA'],y0=420,size=120,step=128)
ax.text(70,760,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=52,color=G,va='center')
ax.text(70,860,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=30,color=W,va='center')
ax.text(70,920,'¿Cuántos litros necesita tu estación para empatar?',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,7)
