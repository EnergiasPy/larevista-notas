# Carrusel 1080x1350 · Paraguay · licitación de cargadores de Petropar · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/dn20/'; os.makedirs(O,exist_ok=True)
ID='2026-11-20-petropar-cargadores-electricos-estaciones-licitacion-dncp'
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

# 1 PORTADA
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2,s) in enumerate([('CARGADORES',W,128),('EN PETROPAR:',W,128),('LICITACIÓN FRENADA',G,96)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=s,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['La DNCP ordenó cambiar el pliego','de una compra de G. 13.994 millones','para estaciones de servicio.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'Y deja a la vista qué equipo pide el Estado',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'para cada punto de carga.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL HECHO
fig,ax=base(2,'EL HECHO')
y=title(ax,['UNA COMPRA','EN PAUSA'],y0=210,size=92,step=100)
big3(fig,ax,y,[('G. 13.994|millones','Monto estimado: unos USD 2,2 millones'),('SUSPENDIDA','Hasta que Petropar publique la adenda'),('13 DE NOVIEMBRE','Fecha de la resolución de la DNCP')],fs=66)
ax.text(70,1180,'El llamado es para cargadores en',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'"estaciones de servicios y otros".',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 QUE PIDE
fig,ax=base(3,'QUÉ PIDE POR CADA PUNTO')
y=title(ax,['EL CARGADOR','Y LO DE ALREDEDOR'],y0=210,size=76,step=86)
big3(fig,ax,y,[('90|kW','Cargador rápido con tres salidas'),('150|kVA','Transformador propio, con media tensión'),('45|días hábiles','Plazo de entrega')],fs=70)
ax.text(70,1180,'Más bases de hormigón, canalizaciones,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'puesta a tierra y gestiones ante la ANDE.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

# 4 QUE SE OBJETO
fig,ax=base(4,'QUÉ SE OBJETÓ')
y=title(ax,['UN PLIEGO','DEMASIADO EXACTO'],y0=210,size=78,step=88)
cards(ax,[('Valores exactos en vez de mínimos','90 kW justos y precisión de corriente de ±0,1 %'),
          ('Muestras físicas y visita a fábrica','Del cargador y del transformador, durante la evaluación'),
          ('Tres salidas en un solo equipo','La empresa pedía admitir la de corriente alterna aparte')],y+50,h=150,gap=26)
ax.text(70,1150,'Petropar negó haber armado el pliego',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1196,'para favorecer a un fabricante.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 QUE RESOLVIO
fig,ax=base(5,'QUÉ RESOLVIÓ LA DNCP')
y=title(ax,['LE DIO LA RAZÓN','EN PARTE'],y0=210,size=84,step=94)
cards(ax,[('Cambia: potencia y muestras','Se admiten 90 kW o más; se revisan las muestras'),
          ('Se mantiene: tres salidas juntas','Ese pedido fue rechazado'),
          ('Rechazado: la barrera de mercado','Lo consideró sin fundamento suficiente')],y+50,h=150,gap=26)
save(fig,5)

# 6 CIERRE
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TU COMPETIDOR','YA ESTÁ COMPRANDO'],y0=205,size=76,step=86)
cards(ax,[('El pliego es una lista de compras','Para 90 kW: 150 kVA, media tensión y trámite en la ANDE'),
          ('Pedí mínimos, no valores exactos','Y normas internacionales de producto'),
          ('Exigí un protocolo abierto','Para poder cambiar de proveedor de software')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,6)
print('ok')
