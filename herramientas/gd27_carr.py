# Carrusel 1080x1350 · Paraguay · gasoducto bioceánico · 27/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/gd27/'; os.makedirs(O,exist_ok=True); os.makedirs(R,exist_ok=True)
ID='2026-11-27-gasoducto-bioceanico-vaca-muerta-chaco-paraguay-milei'
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
fig,ax=base(1,'PARAGUAY · ENERGÍA')
for (l,c2,sz,yy) in [('MILEI EN',W,124,290),('PARAGUAY:',W,124,420),('¿QUÉ SE GANA',G,92,548),('CON EL GAS?',G,92,648)]:
    ax.text(66,yy,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,730),140,7,color=G))
for i,l in enumerate(['El jueves 26, en el Palacio','de López, con Pedro Alliana.']):
    ax.text(70,810+i*54,l,fontfamily=B,fontweight='semibold',fontsize=37,color=W,va='center')
ax.text(70,990,'Sin documento firmado, pero con dos',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1032,'proyectos de gas sobre la mesa.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 · dos proyectos
fig,ax=base(2,'LO PRIMERO: NO MEZCLARLOS')
y=title(ax,['SON DOS','PROYECTOS'],y0=210,size=104,step=112)
cards(ax,[('Gasoducto bioceánico a Brasil','Paraguay es el territorio por donde pasa el caño'),
          ('Conexión desde Formosa','Acá sí Paraguay sería comprador de gas'),
          ('De ninguno se anunció el inicio de obras','Tienen escalas y lógicas distintas')],y+40,h=150,gap=26)
ax.text(70,1180,'El primero sale USD 2.000 millones.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'Del segundo no se dieron montos ni plazos.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 · el gasoducto
fig,ax=base(3,'EL GASODUCTO BIOCEÁNICO')
y=title(ax,['DE LA PATAGONIA','A SÃO PAULO'],y0=210,size=88,step=96)
big3(fig,ax,y,[('2.000|millones de USD','Inversión estimada'),('1.050|km','De ductos, atravesando el Chaco paraguayo'),('2032|el plazo','Año en que Paraguay busca tenerlo viabilizado')],fs=62)
ax.text(70,1180,'Lo planteó el canciller Rubén Ramírez Lezcano',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'durante la visita.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

# 4 · lo que NO pasó
fig,ax=base(4,'LO QUE NO PASÓ')
y=title(ax,['NO HUBO','NADA FIRMADO'],y0=210,size=100,step=108)
cards(ax,[('Sin documento ni conferencia','Hablaron los cancilleres, no los presidentes'),
          ('Sin financiamiento ni cronograma','Es una agenda de prioridades, no un contrato'),
          ('Falta la decisión de tres países','Argentina, Paraguay y Brasil')],y+40,h=150,gap=26)
ax.text(70,1180,'Lo decimos porque un gasoducto de esta escala',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'se mide en años, no en anuncios.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 · por qué ahora
fig,ax=base(5,'POR QUÉ APARECE AHORA')
y=title(ax,['EL TECHO','ELÉCTRICO'],y0=210,size=108,step=116)
cards(ax,[('Itaipú: 2029 y 2030','Paraguay consumiría toda su parte en varios meses'),
          ('Aña Cuá: primera turbina en 2028','Sumaría 10 % de generación y USD 90 M al año'),
          ('El gas entra como alternativa','Para no quedarse sin margen antes de 2032')],y+40,h=150,gap=26)
ax.text(70,1180,'Hace una semana contamos que el excedente',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'de Itaipú se termina antes de lo previsto.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 · las obras
fig,ax=base(6,'LAS OBRAS EN LA LISTA')
y=title(ax,['TRES PASOS','CON LA ARGENTINA'],y0=210,size=80,step=92)
cards(ax,[('Puente Pozo Hondo–Misión La Paz','Conectaría Boquerón con Salta'),
          ('Clorinda–Puerto Falcón','Centro de frontera y accesos a Asunción'),
          ('Puente Pilar–Colonia Cano','Se acompañará el proyecto, sin fechas')],y+40,h=150,gap=26)
ax.text(70,1180,'Los dos gobiernos ratificaron el Corredor',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'Bioceánico, sin plazos ni montos nuevos.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,6)

# 7 · qué significa
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['LO QUE CAMBIA','SI HAY GAS'],y0=205,size=100,step=108)
cards(ax,[('Hoy no hay gas natural de red','Todo el GLP llega envasado o por camión'),
          ('Con ducto aparece el GNV','Isla y compresión que hoy nadie invierte'),
          ('Y los tres pasos mueven la carga','El tránsito pesado del Chaco cambia de mapa')],y+40,h=150,gap=24)
save(fig,7)

# 8 · cierre
fig,ax=base(8,'LA ESTACIÓN DEL FUTURO')
y=title(ax,['LEÉ LA NOTA','COMPLETA'],y0=420,size=120,step=128)
ax.text(70,760,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=52,color=G,va='center')
ax.text(70,860,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=30,color=W,va='center')
ax.text(70,920,'¿Pondrías GNV en tu estación si hubiera red?',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,8)
print('ok carrusel 8')
