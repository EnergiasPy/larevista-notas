import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/cl9/'; os.makedirs(O,exist_ok=True)
N=6
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#0039A6','#FFFFFF','#D52B1E']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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
ID='2026-11-09-chile-alza-diesel-tope-camioneros'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · CHILE')
for i,(l,c) in enumerate([('CHILE:',W),('OTRA ALZA,',W),('UN TOPE Y',G),('CAMIONEROS',G)]):
    ax.text(66,280+i*142,l,fontfamily=BB,fontsize=108,color=c,va='center')
ax.add_patch(Rectangle((70,830),140,7,color=G))
for i,l in enumerate(['Lo que anunció el Gobierno de Kast','y qué anticipa para la región']):
    ax.text(70,905+i*62,l,fontfamily=B,fontweight='bold',fontsize=38,color=W,va='center')
ax.text(70,1095,'Lunes 9 de noviembre',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'DESDE EL JUEVES 12')
y=title(ax,['OTRA ALZA','EN EL SURTIDOR'])
big3(ax,y,[('+$ 40','por litro en bencinas y diésel'),('6.ª semana','seguida de alzas, según las proyecciones'),('MEPCO','el mecanismo que fija el ajuste semanal')])
save2(fig,2)
fig,ax=base(3,'EL PROYECTO DEL GOBIERNO')
y=title(ax,['TOPE A LAS','PRÓXIMAS ALZAS'])
big3(ax,y,[('$ 20','por litro como máximo en cada alza'),('90 días','de vigencia, con discusión inmediata'),('Esta semana','espera tratarlo el ministro de Hacienda')])
save2(fig,3)
fig,ax=base(4,'EL COSTO')
y=title(ax,['CONTENER PRECIOS','NO ES GRATIS'],size=80,step=88)
big3(ax,y,[('$ 1,1 billones','gastó el Estado entre agosto y octubre'),('$ 860.000 M','fueron para contener el diésel'),('$ 170','por litro subsidia hoy en el gasoil')],fs=58)
save2(fig,4)
fig,ax=base(5,'LOS CAMIONEROS')
y=title(ax,['CORTES EN','LA RUTA 5'])
cards(ax,[('Dónde','Los Ángeles, Victoria, Osorno y Curicó'),('Qué piden','Congelar el precio unos cuatro meses'),('Paro nacional','Convocado por una confederación desde el martes 10')],y+60,h=140)
save2(fig,5)
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TODOS POSTERGAN','LA CUENTA'],size=80,step=88)
cards(ax,[('Operador chileno','Precio nuevo el jueves y posibles cortes de ruta'),('Paraguay','Cuando el diésel sube, el conflicto aparece en el flete'),('La región','Chile topa, Uruguay congela, Brasil subsidia')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,6)
print('ok')
