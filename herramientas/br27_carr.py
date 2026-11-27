import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/br27/'; os.makedirs(O,exist_ok=True)
N=8
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#009C3B','#FFDF00','#002776']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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
def save(fig,name): fig.savefig(O+name+'.png',facecolor=BG); Image.open(O+name+'.png').convert('RGB').save(R+name+'.jpg',quality=92); plt.close(fig)
ID='2026-11-27-cuanto-cuesta-el-diesel-en-brasil-subsidio-prorroga'
def save2(fig,k): save(fig,f'{ID}-c{k}')

# 1 portada
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · BRASIL')
for i,(l,c) in enumerate([('DIÉSEL EN BRASIL:',W),('EL S10 PROMEDIA',W),('R$ 7,26',G),('POR LITRO',G)]):
    ax.text(66,280+i*142,l,fontfamily=BB,fontsize=100,color=c,va='center')
ax.add_patch(Rectangle((70,830),140,7,color=G))
for i,l in enumerate(['Hacienda anunció 30 días más','del subsidio de R$ 2,12 por litro']):
    ax.text(70,905+i*62,l,fontfamily=B,fontweight='bold',fontsize=40,color=W,va='center')
ax.text(70,1095,'Qué cambia en la frontera',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)

# 2 cuanto cuesta
fig,ax=base(2,'EL PRECIO EN LA BOMBA')
y=title(ax,['CUÁNTO CUESTA','EL DIÉSEL'])
big3(ax,y,[('R$ 7,26','precio medio del S10, 15 al 21/11 (ANP)'),('R$ 9,06','simulación sin subsidio, no un precio medido'),('+19,8 %','subió el precio medio nacional en un año')],fs=66,col=[G,RD,RD])
save2(fig,2)

# 3 que se prorrogo
fig,ax=base(3,'LA MEDIDA')
y=title(ax,['QUÉ','SE PRORROGÓ'])
cards(ax,[('R$ 2,12 por litro','Subvención sobre el diésel A, el combustible puro'),('R$ 1,80 en el surtidor','Con el corte obligatorio de 15 % de biodiésel'),('30 días más','Anunciado por Hacienda; la portaria, sin verificar')],y+60)
save2(fig,3)

# 4 lo que cuesta
fig,ax=base(4,'LA FACTURA')
y=title(ax,['LO QUE','CUESTA'])
big3(ax,y,[('R$ 8.000 a 10.500 M','costo de estos 30 días, según Planificación'),('R$ 85.000 M','el total de 2026 en contención de precios'),('R$ 1,40','el beneficio al diésel importado que NO se renovó')],fs=52,col=[RD,RD,M])
save2(fig,4)

# 5 tres caminos
fig,ax=base(5,'LA REGIÓN')
y=title(ax,['TRES PAÍSES,','TRES CAMINOS'])
cards(ax,[('Bolivia sacó el subsidio','Bs 20,57 por litro y paro del transporte el lunes'),('Brasil lo sostiene','Un mes más, con costo fiscal creciente'),('Paraguay bajó el ISC','G. 300 menos en el diésel, hasta el 31 de diciembre')],y+60)
save2(fig,5)

# 6 el litro en dolares
fig,ax=base(6,'COMPARACIÓN')
y=title(ax,['EL LITRO,','EN DÓLARES'])
big3(ax,y,[('USD 1,27','Brasil, con la subvención vigente'),('USD 1,40','Paraguay, diésel común'),('USD 1,75','Bolivia, desde el 24 de noviembre')],fs=66,col=[G,W,RD])
ax.text(66,1035,'Sin los R$ 2,12, el litro brasileño rondaría',fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
ax.text(66,1080,'los USD 1,58: quedaría por encima',fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
ax.text(66,1125,'del paraguayo.',fontfamily=B,fontweight='bold',fontsize=31,color=G,va='center')
save2(fig,6)

# 7 que significa
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['LA BRECHA','SE DECIDE AFUERA'],size=74,step=86)
cards(ax,[('No es estructural','Se firma en Brasilia cada 30 días'),('El este, en desventaja','Salto del Guairá, Pedro Juan y Ciudad del Este'),('Si no se renueva','La brecha no se achica: se da vuelta')],y+60)
save2(fig,7)

# 8 cierre
fig,ax=base(8,'')
ax.text(540,430,'LEÉ LA NOTA',fontfamily=BB,fontsize=104,color=W,va='center',ha='center')
ax.text(540,540,'COMPLETA EN',fontfamily=BB,fontsize=104,color=W,va='center',ha='center')
ax.text(540,660,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=58,color=G,va='center',ha='center')
ax.add_patch(Rectangle((430,730),220,6,color=G))
ax.text(540,820,'Seguinos para la noticia del sector',fontfamily=B,fontweight='semibold',fontsize=34,color=M,va='center',ha='center')
ax.text(540,870,'todos los días',fontfamily=B,fontweight='semibold',fontsize=34,color=M,va='center',ha='center')
ax.text(540,990,'Link en la bio',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center',ha='center')
save2(fig,8)
print('ok', sorted(os.listdir(O)))
