# Carrusel 1080x1350 · Región · Uruguay · autodespacho · 26/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/uy26/'; os.makedirs(O,exist_ok=True); os.makedirs(R,exist_ok=True)
ID='2026-11-26-autodespacho-uruguay-estaciones-cargar-uno-mismo'
N=7; BR=['#0038A8','#FFFFFF','#0038A8']
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
fig,ax=base(1,'REGIÓN · URUGUAY')
for i,(l,c2,sz) in enumerate([('¿Y SI EL CLIENTE',W,112),('CARGA SOLO?',W,112),('URUGUAY LO ESTUDIA',G,112)]):
    ax.text(66,310+i*130,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,730),140,7,color=G))
for i,l in enumerate(['El gremio de las estaciones','encargó analizar el autodespacho.']):
    ax.text(70,810+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,990,'No está prohibido: ya hay dos estaciones',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1032,'uruguayas funcionando así.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 · qué pasó
fig,ax=base(2,'QUÉ PASÓ')
y=title(ax,['EL GREMIO PIDIÓ','ESTUDIAR SI CONVIENE'],y0=210,size=78,step=90)
cards(ax,[('Lo resolvió la asamblea de UNVENU','La Unión de Vendedores de Nafta del Uruguay'),
          ('El Consejo Directivo tiene que analizarlo','Viabilidad técnica, legal y de costos'),
          ('Todavía no hay una propuesta formal','Es un estudio, no un pedido al Gobierno')],y+40,h=150,gap=26)
ax.text(70,1180,'"Generar las condiciones para avanzar en esa',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'línea en caso de que sea necesario": F. de Castro, UNVENU.',fontfamily=B,fontsize=26,color=M,va='center')
save(fig,2)

# 3 · ya hay dos casos
fig,ax=base(3,'LO QUE YA EXISTE')
y=title(ax,['DOS ESTACIONES','YA FUNCIONAN ASÍ'],y0=210,size=84,step=96)
cards(ax,[('Termas del Arapey, Salto','Con bandera ANCAP, operada por particulares'),
          ('Pueblo Isidoro Noblía, Cerro Largo','El segundo caso del país'),
          ('La autorización se tramita en la URSEA','El autoservicio no está prohibido por ley')],y+40,h=150,gap=26)
ax.text(70,1180,'Son pueblos chicos: el autodespacho apareció',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'donde no cierra tener playa atendida todo el día.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

# 4 · por qué ahora
fig,ax=base(4,'POR QUÉ AHORA')
y=title(ax,['EL MARGEN','SE ACHICA'],y0=210,size=100,step=108)
big3(fig,ax,y,[('3,7|% del parque','Autos eléctricos e híbridos en Uruguay'),('20|% menos','Caída de nafta en algunas estaciones'),('0|de IMESI','Lo que paga un auto eléctrico')],fs=66)
ax.text(70,1180,'Los dos primeros datos son de la CLAEC;',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'la carga impositiva, del planteo de UNVENU.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 · Argentina
fig,ax=base(5,'EL ANTECEDENTE')
y=title(ax,['LA ARGENTINA','YA LO HABILITÓ'],y0=210,size=92,step=100)
cards(ax,[('Decreto 46/2025','Dejó sin efecto la prohibición de 1983'),
          ('Resolución 147/2025 de Energía','Fijó el trámite para pedir la autorización'),
          ('Es optativo, total o parcial','Lo decide cada estación, con auditoría de seguridad')],y+40,h=150,gap=26)
ax.text(70,1180,'Un año y medio después, Uruguay mira ese camino',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'con una ventaja: allá hizo falta un decreto, acá no.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 · qué significa
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA MIRAR'],y0=205,size=100,step=108)
cards(ax,[('No es una moda: es una cuenta','Aparece cuando el litro deja menos y el turno cuesta igual'),
          ('La playa atendida es un servicio','Si se cobra con atención, hay que saber cuánto vale'),
          ('El surtidor ya no es todo el negocio','Tienda, carga eléctrica y servicios pesan cada vez más')],y+40,h=150,gap=24)
save(fig,6)

# 7 · cierre
fig,ax=base(7,'LA ESTACIÓN DEL FUTURO')
y=title(ax,['LEÉ LA NOTA','COMPLETA'],y0=420,size=120,step=128)
ax.text(70,760,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=52,color=G,va='center')
ax.text(70,860,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=30,color=W,va='center')
ax.text(70,920,'¿Dejarías que el cliente cargue solo en tu estación?',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,7)
print('ok carrusel 7')
