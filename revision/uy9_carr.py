import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/uy9/'; os.makedirs(O,exist_ok=True)
N=6
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#0038A8','#FFFFFF','#0038A8']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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
ID='2026-11-09-uruguay-gasoil-debajo-referencia-ancap'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · URUGUAY')
for i,(l,c) in enumerate([('URUGUAY:',W),('EL GASOIL',W),('DEBERÍA',G),('SUBIR 31 %',G)]):
    ax.text(66,280+i*142,l,fontfamily=BB,fontsize=108 if i<3 else 96,color=c,va='center')
ax.add_patch(Rectangle((70,830),140,7,color=G))
for i,l in enumerate(['El Gobierno congeló los precios','de noviembre. Quién paga la diferencia']):
    ax.text(70,905+i*62,l,fontfamily=B,fontweight='bold',fontsize=42,color=W,va='center')
ax.text(70,1095,'y qué anticipa para la región',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'PRECIOS DE NOVIEMBRE')
y=title(ax,['SIN CAMBIOS','EN EL SURTIDOR'])
big3(ax,y,[('$ 90,45','por litro de nafta súper 95'),('$ 62,79','por litro de gasoil 50S'),('$ 93,56','por kilo de supergás')])
save2(fig,2)
fig,ax=base(3,'LO QUE PEDÍA LA REFERENCIA')
y=title(ax,['LA URSEA','INDICABA SUBAS'])
big3(ax,y,[('+31,3 %','en el gasoil 50S: unos $ 20 por litro'),('+3,3 %','en las naftas: unos $ 3 por litro'),('No se aplicaron','el Gobierno mantuvo los precios')])
save2(fig,3)
fig,ax=base(4,'LA ESTRATEGIA')
y=title(ax,['AMORTIGUAR','DESDE ABRIL'])
cards(ax,[('Revisión mensual','En lugar de cada dos meses'),('Decreto 130/025','Permite suspender el ajuste en casos excepcionales'),('Refinación de ANCAP','Según el Gobierno, ayuda a sostenerla')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'QUIÉN PAGA LA DIFERENCIA')
y=title(ax,['LA FACTURA','LA PAGA ANCAP'])
big3(ax,y,[('USD 80 M','menos que la paridad de importación (1.er semestre)'),('16 %','la brecha del gasoil en abril'),('USD 1,56','el litro de gasoil 50S (≈ $ 40,3 por dólar)')])
save2(fig,5)
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['PRECIOS QUE','ALGUIEN FINANCIA'])
cards(ax,[('Operador uruguayo','Si se corrige, el salto en el gasoil puede ser grande'),('Paraguay y Brasil','También congelan o subsidian: medidas temporales'),('Lección de Bolivia','Lo que se atrasa, se corrige de golpe')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,6)
print('ok')
