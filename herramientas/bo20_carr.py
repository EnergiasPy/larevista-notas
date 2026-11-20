# Carrusel 1080x1350 · Paraguay · Bolivia · subsidio y precios · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/bo20/'; os.makedirs(O,exist_ok=True)
ID='2026-11-20-cuanto-cuesta-gasolina-bolivia-subsidio-9000-millones'
N=7; BR=['#D52B1E','#F9E300','#007934']
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
        num,_,uni=big.partition('|'); x0=100
        if num.startswith('BS '):
            p=ax.text(100,yy+66,'Bs',fontfamily=B,fontweight='bold',fontsize=int(fs*0.62),color=W,va='center')
            fig.canvas.draw(); bb=p.get_window_extent(); x0=ax.transData.inverted().transform((bb.x1,0))[0]+10; num=num[3:]
        tx=ax.text(x0,yy+60,num,fontfamily=BB,fontsize=fs,color=W,va='center')
        if uni:
            fig.canvas.draw(); bb=tx.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
            ax.text(x2+14,yy+66,uni,fontfamily=B,fontweight='bold',fontsize=int(fs*0.52),color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k):
    fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)


# 1 PORTADA
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · BOLIVIA')
for i,(l,c2,s) in enumerate([('CUÁNTO CUESTA',W,128),('LA GASOLINA',W,128),('EN BOLIVIA',G,128)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=s,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['Bs 6,96 por litro: casi la mitad','que en Paraguay. Y un subsidio','que ya llega a Bs 9.000 millones.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'El diésel, en cambio, ya es más caro',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'del lado boliviano de la frontera.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL PRECIO
fig,ax=base(2,'EL PRECIO')
y=title(ax,['LA GASOLINA','SIGUE CONGELADA'],y0=210,size=84,step=94)
big3(fig,ax,y,[('BS 6,96|por litro','Gasolina especial, el mismo precio desde principios de año'),('USD 0,59|por litro','Al tipo de cambio oficial de Bs 11,75'),('G. 3.700|por litro','En Paraguay, la nafta más económica cuesta G. 6.690')],fs=68)
ax.text(70,1180,'El diésel, en cambio, perdió',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'el subsidio el 18 de septiembre.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 EL TECHO
fig,ax=base(3,'LO QUE CUESTA SOSTENERLO')
y=title(ax,['EL TECHO SE','MULTIPLICÓ POR 9'],y0=210,size=84,step=94)
D=[('JULIO',1000),('AGOSTO',2000),('SEPTIEMBRE',6000),('NOVIEMBRE',9000)]
for k,(m,v) in enumerate(D):
    yy=y+50+k*150; rb(ax,60,yy,960,126,CARD)
    w=940*v/9000; ax.add_patch(Rectangle((60,yy),max(w,10),126,color=RD if k==3 else '#2A4A80'))
    ax.text(96,yy+30,m,fontfamily=BC,fontweight='bold',fontsize=24,color=W,va='center')
    p=ax.text(96,yy+86,'Bs',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center')
    fig.canvas.draw(); bb=p.get_window_extent(); x0=ax.transData.inverted().transform((bb.x1,0))[0]+10
    ax.text(x0,yy+82,f'{v:,}'.replace(',','.')+' MILLONES',fontfamily=BB,fontsize=50,color=W,va='center')
ax.text(70,y+50+4*150+24,'Dinero público autorizado para YPFB en 2026.',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save(fig,3)

# 4 POR QUE
fig,ax=base(4,'POR QUÉ')
y=title(ax,['BOLIVIA IMPORTA','LO QUE CONSUME'],y0=210,size=84,step=94)
big3(fig,ax,y,[('86 %','Del diésel que consume es importado'),('56 %','De la gasolina es importada'),('USD 766|millones','El nuevo techo de transferencias, en dólares')],fs=68)
ax.text(70,1180,'El Estado cubre la diferencia entre',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'el costo de importar y el precio interno.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 EL DIESEL
fig,ax=base(5,'EL DIÉSEL YA NO')
y=title(ax,['EL DIÉSEL SE PAGA','A PRECIO LLENO'],y0=210,size=84,step=94)
big3(fig,ax,y,[('BS 9,80|antes','El litro de diésel con subsidio'),('BS 17,95|desde el 18/9','Sin subsidio: unos USD 1,53 por litro'),('G. 9.560|por litro','Más que el diésel común paraguayo: G. 8.985')],fs=68)
ax.text(70,1180,'En el diésel, hoy es más barato',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'cargar del lado paraguayo.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

# 6 HASTA CUANDO
fig,ax=base(6,'¿HASTA CUÁNDO?')
y=title(ax,['LA FECHA ES','EL 12 DE ENERO'],y0=210,size=88,step=98)
cards(ax,[('El decreto mantiene el subsidio hasta ahí','Decreto 5652: hasta el 12 de enero de 2027'),
          ('YPFB habló de esa fecha como el final','Lo dijo su presidente, Sebastián Daroca'),
          ('El ministerio dice que no hay fecha','Pero confirma que la medida se va a aplicar')],y+50,h=150,gap=26)
save(fig,6)

# 7 CIERRE
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['DOS FECHAS','DE ENERO'],y0=205,size=88,step=98)
cards(ax,[('1 de enero, Paraguay','Vence la rebaja del impuesto al diésel'),
          ('12 de enero, Bolivia','Vence el plazo del subsidio a la gasolina'),
          ('Las dos mueven la frontera','Hoy la gasolina boliviana cuesta casi la mitad')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
