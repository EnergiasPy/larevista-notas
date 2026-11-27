# Carrusel 1080x1350 · Paraguay · restricciones Ruta 2 por Caacupé · 27/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ca27/'; os.makedirs(O,exist_ok=True); os.makedirs(R,exist_ok=True)
ID='2026-11-27-restricciones-ruta-2-caacupe-camiones-combustible'
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
fig,ax=base(1,'PARAGUAY · RUTA PY02')
for i,(l,c2,sz) in enumerate([('70 HORAS SIN',W,124),('CAMIONES DE',W,124),('COMBUSTIBLE',G,124)]):
    ax.text(66,310+i*134,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,742),140,7,color=G))
for i,l in enumerate(['Caacupé saca los pesados','de la Ruta 2 del 5 al 8.']):
    ax.text(70,822+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1000,'Justo en el fin de semana de mayor',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1042,'demanda del año.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 · qué dice la resolución
fig,ax=base(2,'LA RESOLUCIÓN 1756 DEL MOPC')
y=title(ax,['QUÉ CAMIONES','NO PUEDEN PASAR'],y0=210,size=80,step=92)
cards(ax,[('Combustibles, inflamables y explosivos','Están nombrados expresamente en la resolución'),
          ('Carga de 16,5 toneladas o más','Y todo vehículo con acoplado'),
          ('Ganado en pie y cargas indivisibles','También los rodados sin condiciones técnicas')],y+40,h=150,gap=26)
ax.text(70,1180,'La firmó el ministro Juan Carlos Baruja',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'el 24 de noviembre.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 · cuándo y dónde
fig,ax=base(3,'CUÁNDO Y DÓNDE')
y=title(ax,['DEL SÁBADO 5','AL MARTES 8'],y0=210,size=96,step=104)
big3(fig,ax,y,[('12:00|sábado 5','Hora en que arranca la restricción'),('10:00|martes 8','Hora en que se levanta'),('70|horas','El total, sin reposición posible')],fs=64)
ax.text(70,1180,'El tramo va del km 15, en San Lorenzo,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'al km 86,5, en Itacurubí de la Cordillera.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

# 4 · lo que cambia el acceso
fig,ax=base(4,'LO QUE CAMBIA EL ACCESO A LA PLAYA')
y=title(ax,['BICICLETAS,','MOTOS Y PEREGRINOS'],y0=210,size=72,step=84)
cards(ax,[('Bicicletas: San Lorenzo a Eusebio Ayala','Del mediodía del domingo 6 al martes 8 a las 10:00'),
          ('Motos: fuera del casco de Caacupé','Desde las 12:00 del lunes 7'),
          ('Carril de peregrinos: km 38 al 52,5','Lunes 7 de 16:00 a martes 8 de 06:00')],y+40,h=150,gap=26)
ax.text(70,1180,'Con el carril invertido, la entrada y la salida',fontfamily=B,fontweight='bold',fontsize=29,color=W,va='center')
ax.text(70,1226,'de la estación no son las de siempre.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 · la magnitud
fig,ax=base(5,'LA MAGNITUD')
y=title(ax,['TRES MILLONES','DE PEREGRINOS'],y0=210,size=84,step=96)
cards(ax,[('El novenario empieza el sábado 28','Y la fiesta es el martes 8 de diciembre'),
          ('Más de 3 millones de personas','Es la previsión del operativo oficial'),
          ('Para la Ruta 2 es el pico del año','Y los cuatro días más cargados son sin reposición')],y+40,h=150,gap=26)
save(fig,5)

# 6 · qué hacer
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['CUATRO COSAS','PARA HACER YA'],y0=205,size=92,step=100)
cards(ax,[('Pedí la última carga para el viernes 4','Todas las bocas del tramo van a pedir lo mismo'),
          ('Calculá sobre el pico, no sobre el promedio','Mirá el mismo fin de semana del año pasado'),
          ('La tienda también se queda sin reposición','Hielo, bebidas y comida siguen el mismo calendario'),
          ('Reforzá los turnos del domingo al martes','No se cubren con la plantilla de siempre')],y+30,h=138,gap=20)
save(fig,6)

# 7 · cierre
fig,ax=base(7,'LA ESTACIÓN DEL FUTURO')
y=title(ax,['LEÉ LA NOTA','COMPLETA'],y0=420,size=120,step=128)
ax.text(70,760,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=52,color=G,va='center')
ax.text(70,860,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=30,color=W,va='center')
ax.text(70,920,'¿Tu estación está sobre la Ruta 2? Compartilo.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,7)
print('ok carrusel 7')
