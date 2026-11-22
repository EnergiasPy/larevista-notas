# Carrusel 1080x1350 · Paraguay · Chile · margen de comercialización · 22/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/cl22/'; os.makedirs(O,exist_ok=True)
ID='2026-11-22-cuanto-gana-estacion-de-servicio-chile-margen'
N=7; BR=['#0039A6','#FFFFFF','#D52B1E']
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


fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · CHILE')
for i,(l,c2,sz) in enumerate([('CUÁNTO GANA',W,128),('UNA ESTACIÓN',W,128),('EN CHILE',G,128)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['75 pesos por litro de gasolina,','para repartir entre la distribuidora','y la estación.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'Son unos G. 460 por litro. Y el dato oficial',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'no se actualiza desde agosto de 2024.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL NÚMERO')
y=title(ax,['LO QUE QUEDA','POR LITRO'],y0=210,size=88,step=98)
big3(fig,ax,y,[('$ 75','Gasolina 93 en Santiago: unos 7 centavos de dólar'),('$ 94','Diésel en Santiago: unos 9 centavos de dólar'),('G. 460','La gasolina, en guaraníes por litro')],fs=68)
ax.text(70,1180,'Es el margen de toda la cadena después',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'de la refinería: distribuidora y estación.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'POR REGIÓN · GASOLINA 93')
y=title(ax,['FUERA DE SANTIAGO,','CASI EL DOBLE'],y0=210,size=80,step=90)
rows=[('METROPOLITANA','$ 75'),('VALPARAÍSO','$ 98'),('MAULE','$ 110'),('MAGALLANES','$ 127'),('BIOBÍO','$ 139'),("O'HIGGINS",'$ 141')]
for k,(n,v) in enumerate(rows):
    yy=y+50+k*112; rb(ax,60,yy,960,96,CARD); ax.add_patch(Rectangle((60,yy),10,96,color=G))
    ax.text(100,yy+50,n,fontfamily=BB,fontsize=46,color=W,va='center')
    ax.text(985,yy+50,v,fontfamily=BB,fontsize=50,color=G,va='center',ha='right')
ax.text(70,1226,'Pesos chilenos por litro. Datos de la CNE.',fontfamily=B,fontsize=25,color=M,va='center')
save(fig,3)

fig,ax=base(4,'EL DATO OFICIAL')
y=title(ax,['FRENADO','EN 2024'],y0=210,size=100,step=108)
cards(ax,[('Último mes publicado: agosto de 2024','En el reporte de la CNE de septiembre de 2026'),
          ('Dos años sin actualizar el margen','Los precios al público sí están al día'),
          ('Aun así, es más de lo que hay acá','En Paraguay no se publica el margen por eslabón')],y+50,h=150,gap=26)
save(fig,4)

fig,ax=base(5,'QUIÉNES SON')
y=title(ax,['UN NEGOCIO','DE TRES MARCAS'],y0=210,size=84,step=94)
big3(fig,ax,y,[('95 %','De las ventas: Copec, Enex (Shell) y Aramco'),('691','Puntos de venta de Copec al cierre de 2024'),('454 Y 300','Los de Enex y Aramco')],fs=66)
ax.text(70,1180,'En Copec, casi todas las estaciones son de',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'la compañía: el concesionario las administra.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

fig,ax=base(6,'LA COMPARACIÓN')
y=title(ax,['POR LITRO,','EN GUARANÍES'],y0=210,size=88,step=98)
big3(fig,ax,y,[('G. 460','Chile: distribuidora y estación juntas'),('G. 580','Colombia: margen regulado de la estación'),('G. 740','Argentina: lo que estima el gremio')],fs=66)
ax.text(70,1180,'Las estaciones chilenas hablan de un 5 %',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'de las ventas.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,6)

fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['EL MARGEN','ES LOCAL'],y0=205,size=88,step=98)
cards(ax,[('El margen depende de dónde estás','En Chile, el mercado más grande es el de menor margen'),
          ('Paraguay: 2.880 bocas, mercado chico','La competencia de tu zona pesa como tu contrato'),
          ('Falta un dato oficial de margen','Ordenaría la discusión entre operadores y emblemas')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
