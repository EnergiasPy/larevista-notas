# Carrusel 1080x1350 · Paraguay · Bolivia · diésel a Bs 20,57 · 25/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/bo24/'; os.makedirs(O,exist_ok=True)
ID='2026-11-24-cuanto-cuesta-el-diesel-en-bolivia-sube-a-bs-20-57'
N=6; BR=['#D52B1E','#F9E300','#007934']
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




fig,ax=base(1,'REGIÓN · BOLIVIA')
for i,(l,c2,sz) in enumerate([('BOLIVIA SUBE',W,138),('EL DIÉSEL',W,138),('A BS 20,57',G,138)]):
    ax.text(66,275+i*168,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['14,6 % más desde el martes 24.','Unos USD 1,75 por litro.']):
    ax.text(70,820+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1000,'El transporte evalúa un paro.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL AJUSTE')
y=title(ax,['BS 2,62 MÁS','POR LITRO'],y0=210,size=100,step=108)
big3(fig,ax,y,[('20,57|bolivianos','Precio desde el 24 de noviembre'),('17,95|bolivianos','Lo que costaba desde el 18 de septiembre'),('+14,6 %','La suba, de un día para el otro')],fs=68)
ax.text(70,1180,'La gasolina especial no cambió:',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'sigue en Bs 6,96, con subsidio.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'POR QUÉ SUBE')
y=title(ax,['UNA REGLA','CON BANDA DE 5 %'],y0=210,size=88,step=98)
cards(ax,[('El precio sigue al costo de importación','Decreto Supremo 5716, del 18 de septiembre'),
          ('Si la referencia varía menos de 5 %, queda igual','Para arriba o para abajo'),
          ('Si supera el 5 %, se traslada al surtidor','Es lo que pasó ahora, según el ministro')],y+40,h=150,gap=26)
ax.text(70,1180,'El Gobierno dice que también puede bajar.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
save(fig,3)

fig,ax=base(4,'EL RECORRIDO')
y=title(ax,['DE BS 3,72 A BS 20,57','EN UN AÑO'],y0=210,size=84,step=94)
cards(ax,[('Bs 3,72','Hasta diciembre de 2025, congelado dos décadas'),
          ('Bs 9,80','Desde diciembre de 2025'),
          ('Bs 17,95','Desde el 18 de septiembre de 2026'),
          ('Bs 20,57','Desde el 24 de noviembre de 2026')],y+30,h=140,gap=20)
save(fig,4)

fig,ax=base(5,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['MÁS CARO QUE','EN PARAGUAY'],y0=205,size=100,step=108)
cards(ax,[('Bolivia: unos USD 1,75 por litro','Paraguay: diésel común a unos USD 1,40'),
          ('La frontera del Chaco se da vuelta','Antes el combustible barato era el boliviano'),
          ('El transporte evalúa un paro','Los choferes definen medidas el jueves 26')],y+40,h=150,gap=24)
save(fig,5)

fig,ax=base(6,'LA ESTACIÓN DEL FUTURO')
y=title(ax,['LEÉ LA NOTA','COMPLETA'],y0=420,size=120,step=128)
ax.text(70,760,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=52,color=G,va='center')
ax.text(70,860,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=30,color=W,va='center')
ax.text(70,920,'¿Pasa lo mismo en tu país?',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,6)
