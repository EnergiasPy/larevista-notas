import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/b100/'; os.makedirs(O,exist_ok=True)
N=7
ID='2026-11-27-b100-biodiesel-puro-barcazas-paraguay-resolucion-908'
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
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
def cards(ax,items,y0,h=140,gap=22):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.36,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.68,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def big3(ax,y,items,fs=62,col=None):
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=(col[k] if col else G)))
        ax.text(100,yy+60,big,fontfamily=BB,fontsize=fs,color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k): fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)

fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c) in enumerate([('BIODIÉSEL PURO',W),('B100 PARA',W),('LAS BARCAZAS',G)]):
    ax.text(66,300+i*142,l,fontfamily=BB,fontsize=100,color=c,va='center')
ax.add_patch(Rectangle((70,700),140,7,color=G))
for i,l in enumerate(['El MIC habilitó un mercado','para el biodiésel que no','pasa por el surtidor']):
    ax.text(70,775+i*62,l,fontfamily=B,fontweight='bold',fontsize=40,color=W,va='center')
ax.text(70,1030,'Resolución N° 908/2026',fontfamily=B,fontweight='semibold',fontsize=30,color=G,va='center')
ax.text(70,1130,'Qué cambia para la estación',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save(fig,1)

fig,ax=base(2,'LA RESOLUCIÓN')
y=title(ax,['QUÉ','SE HABILITA'])
cards(ax,[('B100: biodiésel puro','Sin mezcla, para abastecer embarcaciones'),('Régimen diferenciado','Modalidades de abastecimiento y requisitos de calidad'),('Puestos en muelles','Y atracaderos, con reglas de seguridad y almacenaje')],y+60)
save(fig,2)

fig,ax=base(3,'EL CLIENTE')
y=title(ax,['POR QUÉ','LA FLOTA'])
big3(ax,y,[('3.000','barcazas y unos 400 remolcadores (CAFYM)'),('3ª','flota fluvial del mundo, tras EE. UU. y China'),('25 millones','de toneladas movió la flota en 2025')],fs=60,col=[G,G,W])
save(fig,3)

fig,ax=base(4,'LO QUE ESTÁ EN JUEGO')
y=title(ax,['GASOIL','IMPORTADO'],size=80,step=90)
cards(ax,[('80 % del comercio exterior','Pasa por la hidrovía, hoy movido con gasoil'),('El biodiésel es nacional','Hecho sobre todo con aceite de soja paraguaya'),('Menos factura afuera','Y una etapa industrial más dentro del país')],y+60)
save(fig,4)

fig,ax=base(5,'OJO CON ESTO')
y=title(ax,['LA MEZCLA','NO CAMBIA'])
big3(ax,y,[('B7','mínimo en el gasoil común hasta el 31/12'),('B8','desde el 1 de enero de 2027'),('Aún sin cargar','la primera operación todavía no se hizo')],fs=62,col=[W,W,RD])
save(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA MIRAR'])
cards(ax,[('Un canal nuevo','Muelles y atracaderos: bocas que no son de ruta'),('El B100 no es gasoil','Sensible al agua y al frío; tapa filtros'),('La misma materia prima','Si crece el río, seguí el abastecimiento del corte')],y+60)
save(fig,6)

fig,ax=base(7,'')
ax.text(540,430,'LEÉ LA NOTA',fontfamily=BB,fontsize=104,color=W,va='center',ha='center')
ax.text(540,540,'COMPLETA EN',fontfamily=BB,fontsize=104,color=W,va='center',ha='center')
ax.text(540,660,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=58,color=G,va='center',ha='center')
ax.add_patch(Rectangle((430,730),220,6,color=G))
ax.text(540,820,'Seguinos para la noticia del sector',fontfamily=B,fontweight='semibold',fontsize=34,color=M,va='center',ha='center')
ax.text(540,870,'todos los días',fontfamily=B,fontweight='semibold',fontsize=34,color=M,va='center',ha='center')
ax.text(540,990,'Link en la bio',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center',ha='center')
save(fig,7)
print('ok')
