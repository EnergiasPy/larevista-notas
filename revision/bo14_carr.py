import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/bo14/'; os.makedirs(O,exist_ok=True)
N=6
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#D52B1E','#F9E300','#007934']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
    if kicker: ax.text(70,110,kicker,fontfamily=BC,fontweight='bold',fontsize=26,color=G,va='center')
    ax.text(1010,1295,'energiaslatam.com',fontfamily=BC,fontweight='bold',fontsize=28,color=W,va='center',ha='right')
    ax.text(70,1295,f'{n}/{N}',fontfamily=BC,fontweight='bold',fontsize=24,color=M,va='center')
    if n<N: ax.text(540,1295,'Deslizá  »',fontfamily=B,fontweight='semibold',fontsize=22,color=M,va='center',ha='center')
    return fig,ax
def title(ax,lines,y0=200,size=84,step=92,green_last=True):
    for i,l in enumerate(lines): ax.text(66,y0+i*step,l,fontfamily=BB,fontsize=size,color=G if (green_last and i==len(lines)-1) else W,va='center')
    return y0+len(lines)*step
def cards(ax,items,y0,h=130,gap=22,big=False):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.38,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.72,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def save(fig,name): fig.savefig(O+name+'.png',facecolor=BG); Image.open(O+name+'.png').convert('RGB').save(R+name+'.jpg',quality=92); plt.close(fig)
def big3(ax,y,items,fs=62):
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
        ax.text(100,yy+60,big,fontfamily=BB,fontsize=fs,color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
ID='2026-11-14-bolivia-importadores-privados-diesel-ypfb'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · BOLIVIA')
for i,(l,c2) in enumerate([('BOLIVIA:',W),('EL DIÉSEL SIN',W),('SUBSIDIO Y LOS',G),('PRIVADOS SIN',G),('MARGEN',G)]):
    ax.text(66,250+i*128,l,fontfamily=BB,fontsize=112,color=c2,va='center')
ax.add_patch(Rectangle((70,880),140,7,color=G))
for i,l in enumerate(['YPFB vende a Bs 17,95 y a los importadores','privados les cuesta hasta Bs 21,50']):
    ax.text(70,950+i*58,l,fontfamily=B,fontweight='bold',fontsize=36,color=W,va='center')
ax.text(70,1110,'Sábado 14 de noviembre',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'LOS NÚMEROS')
y=title(ax,['PRECIO VS.','COSTO'])
big3(ax,y,[('Bs 17,95','el litro de diésel de YPFB, precio regulado'),('Bs 20,50 a 21,50','lo que cuesta importarlo a un privado'),('Bs 3,50','de ese costo son impuestos')],fs=56)
save2(fig,2)
fig,ax=base(3,'EL MERCADO')
y=title(ax,['MENOS','DEMANDA'])
cards(ax,[('−30 a −40 %','La caída estimada de la demanda de diésel'),('El motivo','La suba de precios y el fin del subsidio'),('La salida de los privados','Competir por calidad, no por precio')],y+60,h=140)
save2(fig,3)
fig,ax=base(4,'LO QUE PIDEN')
y=title(ax,['REGLAS','IGUALES'])
cards(ax,[('Mismas reglas','Para YPFB y los importadores'),('Precios estables','Una metodología que no cambie'),('Seguridad para invertir','En estaciones y fidelización')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'EL GOBIERNO')
y=title(ax,['UN AÑO DE','CAMBIOS'])
cards(ax,[('Fin de la subvención al diésel','Para frenar el contrabando'),('Importación privada habilitada','Y compra directa de crudo'),('YPFB y la ANH intervenidas','Por 180 días')],y+60,h=140)
save2(fig,5)
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['MIRÁ LA','FRONTERA'])
cards(ax,[('En Bolivia','Calidad y servicio como diferencia'),('En el Chaco','Menos incentivo al contrabando'),('En la región','Sin reglas claras, no hay inversión')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,6)
print('ok')
