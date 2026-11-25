# Carrusel 1080x1350 · Paraguay · Obra pública · US$ 300 millones · 26/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ob26/'; os.makedirs(O,exist_ok=True)
ID='2026-11-26-300-millones-obras-publicas-diciembre-estaciones'
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



fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2,sz) in enumerate([('US$ 300',W,150),('MILLONES PARA',W,112),('LA OBRA PÚBLICA',G,112)]):
    ax.text(66,300+i*150,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['El Gobierno los desembolsa','en diciembre.']):
    ax.text(70,820+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1000,'¿Qué gana una estación de servicio?',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL ANUNCIO')
y=title(ax,['DE DÓNDE','SALE LA PLATA'],y0=210,size=100,step=108)
cards(ax,[('US$ 150 millones del Tesoro','Pagos pendientes de noviembre y diciembre'),
          ('US$ 150 millones de un crédito','Todavía necesita aprobación del Congreso'),
          ('US$ 350 millones','La deuda con constructoras a principios de noviembre')],y+40,h=150,gap=26)
ax.text(70,1180,'Lo anunció el presidente Pedro Alliana,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'con los ministros de Obras Públicas y de Economía.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'LO QUE MUEVE')
y=title(ax,['300 CONTRATOS','Y 300.000 EMPLEOS'],y0=210,size=84,step=94)
big3(fig,ax,y,[('300|contratos','De obra pública alcanzados'),('300.000','Empleos directos, según los gremios'),('1|millón','De personas alcanzadas de forma indirecta')],fs=64)
save(fig,3)

fig,ax=base(4,'EL DATO DEL SURTIDOR')
y=title(ax,['EL GASOIL CAYÓ','15,1 % EN UN MES'],y0=210,size=88,step=98)
big3(fig,ax,y,[('133|millones de litros','De gasoil tipo III en octubre, contra 156,7 en septiembre'),('300,5|millones de litros','Vendidos en total: 8,2 % menos que un año atrás'),('−15,1 %','La caída del gasoil tipo III en el mes')],fs=56)
ax.text(70,1180,'Una obra parada es una flota que no carga.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
save(fig,4)

fig,ax=base(5,'2027')
y=title(ax,['US$ 931 MILLONES','PARA EL AÑO QUE VIENE'],y0=210,size=74,step=86)
cards(ax,[('US$ 361 millones más que en 2026','Este año el presupuesto de obras fue de 570'),
          ('El foco: reparación y mantenimiento','De rutas en todo el país'),
          ('Más control de peso y peajes','Es como piensan sostener el mantenimiento')],y+40,h=150,gap=26)
save(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['CUATRO COSAS','PARA MIRAR'],y0=205,size=100,step=108)
cards(ax,[('Mirá las obras paradas cerca tuyo','Pueden devolverte un cliente de alto volumen'),
          ('La venta a flotas se prepara','Cuenta corriente, descarga rápida y playa libre'),
          ('2027 es mantenimiento','El trabajo se reparte por todo el país'),
          ('Falta que el Congreso apruebe','La mitad del dinero depende de eso')],y+30,h=140,gap=20)
save(fig,6)

fig,ax=base(7,'LA ESTACIÓN DEL FUTURO')
y=title(ax,['LEÉ LA NOTA','COMPLETA'],y0=420,size=120,step=128)
ax.text(70,760,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=52,color=G,va='center')
ax.text(70,860,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=30,color=W,va='center')
ax.text(70,920,'¿Hay una obra parada cerca de tu estación?',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,7)
