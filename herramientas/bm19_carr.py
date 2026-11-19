# Carrusel 1080x1350 · Brasil · estaciones de biometano para camiones (Ultragaz) · 19/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/bm19/'; os.makedirs(O,exist_ok=True)
ID='2026-11-19-brasil-estaciones-biometano-camiones-ultragaz'
N=7; BR=['#009C3B','#FFDF00','#002776']
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

# 1 PORTADA (con la comparacion con Paraguay, decision de la auditoria del 18/11)
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · BRASIL')
for i,(l,c2,s) in enumerate([('BIOMETANO',W,128),('PARA CAMIONES:',W,112),('20 ESTACIONES EN RUTA',G,88)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=s,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['Una empresa de garrafas abrió las dos','primeras en São Paulo, sin gasoducto','y con carga en 8 a 12 minutos.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'En Paraguay el autogas cayó 11,3 %:',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'qué deja este modelo para la estación.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL NUMERO
fig,ax=base(2,'EL NÚMERO')
y=title(ax,['UNA ESTACIÓN,','EN TRES CIFRAS'],y0=210,size=80,step=90)
big3(fig,ax,y,[('R$ 4 MILLONES','Inversión por estación: cerca de USD 690.000'),('24.000|m³ por día','Biometano que despacha cada unidad'),('+200 CAMIONES','Por día, con carga en 8 a 12 minutos')],fs=68)
ax.text(70,1180,'Son dos, sobre la Rodovia dos Bandeirantes:',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'una en cada sentido de la autopista.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 COMO FUNCIONA
fig,ax=base(3,'CÓMO FUNCIONA')
y=title(ax,['GAS VEHICULAR','SIN GASODUCTO'],y0=210,size=84,step=94)
cards(ax,[('El gas sale de un relleno sanitario','El de Caieiras, a unos cinco kilómetros'),
          ('Se comprime en el lugar','No depende de una red de gas por cañería'),
          ('Sirve el mismo camión','Biometano y gas natural usan el mismo motor')],y+50,h=150,gap=26)
ax.text(70,1150,'El precio no está atado al del petróleo:',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1196,'el transportista puede prever sus costos.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

# 4 EL PROBLEMA
fig,ax=base(4,'EL PROBLEMA')
y=title(ax,['2.500 CONTRA','DOS MILLONES'],y0=210,size=88,step=98)
big3(fig,ax,y,[('2.500','Camiones a gas natural en todo Brasil'),('+2 MILLONES','Camiones pesados a diésel'),('1 CADA 1.000','Poco más: esa es la flota a gas')],fs=68)
ax.text(70,1180,'Sin estaciones no hay camiones,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'y sin camiones nadie pone una estación.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 COMO LO DESTRABO
fig,ax=base(5,'CÓMO LO DESTRABÓ')
y=title(ax,['PRIMERO','EL CLIENTE'],y0=210,size=92,step=100)
cards(ax,[('Surtidores dentro de las empresas','Unos 20 clientes, seis con estación propia'),
          ('Una flota con contrato','100 camiones entre Santos y Ribeirão Preto'),
          ('Recién después, la ruta','Abierta a todos desde comienzos de 2027')],y+50,h=150,gap=26)
ax.text(70,1150,'Hoy abastece más de 300 camiones por día',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1196,'sin haber vendido todavía al público.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 LO QUE VIENE
fig,ax=base(6,'LO QUE VIENE')
y=title(ax,['UNAS VEINTE','ESTACIONES'],y0=210,size=92,step=100)
cards(ax,[('La próxima, sobre la BR-101','Con negociaciones avanzadas'),
          ('Sur, Belo Horizonte y Río de Janeiro','Los corredores que evalúa la empresa'),
          ('Sin cronograma definido','Depende de la demanda y de socios locales')],y+50,h=150,gap=26)
ax.text(70,1150,'Gas no le falta: tiene contratados 700.000 m³',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1196,'por día y hoy vende unos 150.000.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,6)

# 7 CIERRE
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['EL GAS BUSCA','OTRO NEGOCIO'],y0=205,size=84,step=94)
cards(ax,[('Acá el autogas cayó 11,3 %','En estaciones, entre enero y septiembre'),
          ('No hace falta gasoducto','Paraguay no tiene red de gas natural'),
          ('Primero la flota, después el surtidor','Buscá quién tiene volumen y recorrido fijo')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
