# Carrusel 1080x1350 · Paraguay · Petropar cancela la consultoría de exploración · 19/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/pt19/'; os.makedirs(O,exist_ok=True)
ID='2026-11-19-hay-petroleo-en-paraguay-petropar-cancela-consultoria-chaco'
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
for i,(l,c2,s) in enumerate([('¿HAY PETRÓLEO',W,124),('EN PARAGUAY?',W,124),('EL ESTUDIO SE CANCELÓ',G,88)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=s,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['Petropar dejó sin efecto la consultoría','de USD 837.566 que debía destrabar','la búsqueda en el Chaco.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'Tiene 5,6 millones de hectáreas asignadas',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'y ningún pozo perforado.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL HECHO
fig,ax=base(2,'EL HECHO')
y=title(ax,['UNA LICITACIÓN','QUE SE CAYÓ'],y0=210,size=84,step=94)
big3(fig,ax,y,[('USD 837.566','Presupuesto de la consultoría internacional'),('2 DE NOVIEMBRE','Fecha de la resolución que la canceló'),('SIN EXPLICACIÓN','El motivo: "extinción de la necesidad"')],fs=66)
ax.text(70,1180,'Se había autorizado el 3 de septiembre.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'Duró dos meses.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 QUE IBA A HACER
fig,ax=base(3,'QUÉ IBA A HACER')
y=title(ax,['REHACER','LA RONDA ABIERTA'],y0=210,size=84,step=94)
cards(ax,[('Revisar la Ronda Abierta Petropar','Lanzada en 2022, sin contratos firmados'),
          ('Reformular el contrato con privados','El Acuerdo de Producción Compartida'),
          ('Comparar con otros países','Y proponer un relanzamiento en 14 a 18 semanas')],y+50,h=150,gap=26)
ax.text(70,1150,'El propio llamado reconocía el problema:',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1196,'pocos datos técnicos y condiciones poco competitivas.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

# 4 LO QUE TIENE
fig,ax=base(4,'LO QUE TIENE PETROPAR')
y=title(ax,['MUCHA TIERRA,','NINGÚN POZO'],y0=210,size=88,step=98)
big3(fig,ax,y,[('6 BLOQUES','En el Chaco, otorgados entre 2016 y 2020'),('5,6 MILLONES','De hectáreas, según el catastro oficial'),('3 ÁREAS MÁS','En trámite: otros 2,7 millones de hectáreas')],fs=68)
ax.text(70,1180,'Solo Palo Santo figura en exploración.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'Ninguno llegó a perforar.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 EL SOCIO
fig,ax=base(5,'LO QUE FALTA')
y=title(ax,['UN SOCIO','QUE PONGA LA PLATA'],y0=210,size=76,step=86)
cards(ax,[('USD 30 millones','Costo estimado de la prospección inicial'),
          ('Lo tiene que aportar un privado','Ese es el modelo de la Ronda Abierta'),
          ('Hay un memorando con Scorpion','La firma de EE.UU. evalúa los datos de los bloques')],y+50,h=150,gap=26)
ax.text(70,1150,'El memorando no implica',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1196,'trabajos en el terreno.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 CIERRE
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['EN EL SURTIDOR,','NADA CAMBIA'],y0=205,size=84,step=94)
cards(ax,[('Paraguay importa todo su combustible','Un hallazgo tardaría años en llegar al surtidor'),
          ('El precio depende de lo de siempre','Valor internacional, dólar e impuestos'),
          ('Anotá el 31 de diciembre','Vence la rebaja del impuesto al diésel')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,6)
print('ok')
