import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/gl17/'; os.makedirs(O,exist_ok=True)
N=6
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#D52B1E','#FFFFFF','#0038A8']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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

ID='2026-11-17-autogas-cae-estaciones-industria-glp'
def save2(fig,k): save(fig,f'{ID}-c{k}')

# 1 · portada
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2) in enumerate([('EL AUTOGAS',W),('CAE 11 % EN',W),('LAS ESTACIONES',G)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=112,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
ax.text(70,820,'Y el gas que pierde el surtidor',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,872,'lo está ganando la industria.',fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,960,'Datos del registro del MIC,',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1004,'enero a septiembre.',fontfamily=B,fontsize=30,color=M,va='center')
save2(fig,1)

# 2 · el reparto
fig,ax=base(2,'ADÓNDE FUE EL GAS')
y=title(ax,['QUIÉN COMPRA','EL GLP'],y0=210)
big3(ax,y,[('−11,3 %','Estaciones de servicio: 18.823 t'),('+14,7 %','Industrias: 11.222 t'),('−1,9 %','Garrafas: 30.275 t')],fs=76)
ax.text(70,1180,'El mercado total cayó sólo 2,5 %.',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center')
ax.text(70,1226,'No cambió cuánto gas se vende: cambió quién lo compra.',fontfamily=B,fontsize=26,color=M,va='center')
save2(fig,2)

# 3 · participacion
fig,ax=base(3,'EL SURTIDOR PIERDE PESO')
y=title(ax,['TRES PUNTOS','DE MERCADO'],y0=210)
big3(ax,y,[('34,3 % A 31,2 %','Lo que pesa el surtidor en el GLP del país'),('15,8 % A 18,6 %','Lo que pesa la industria'),('66 %','Del autogas se lo reparten tres empresas')],fs=62)
ax.text(70,1180,'Los tres puntos que perdió la estación',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'no se volatilizaron: se los llevó la industria.',fontfamily=B,fontsize=26,color=M,va='center')
save2(fig,3)

# 4 · quien vende autogas
fig,ax=base(4,'AUTOGAS · ENERO A SEPTIEMBRE')
y=title(ax,['QUIÉN VENDE','EN LA PLAYA'],y0=210)
D=[('PETROPAR','5.411 t','−11,6 %',RD),('COPETROL','3.601 t','−10,0 %',RD),('COPESA','3.396 t','−17,6 %',RD),('SAN ISIDRO','1.638 t','de cero',G),('LIMA GAS','927 t','−15,7 %',RD),('PUMA','553 t','−18,1 %',RD)]
for k,(n,v,d2,c) in enumerate(D):
    yy=y+40+k*104; rb(ax,60,yy,960,88,CARD); ax.add_patch(Rectangle((60,yy),10,88,color=c))
    ax.text(100,yy+46,n,fontfamily=BB,fontsize=50,color=W,va='center')
    ax.text(700,yy+46,v,fontfamily=BB,fontsize=50,color=W,va='center',ha='right')
    ax.text(985,yy+46,d2,fontfamily=B,fontweight='bold',fontsize=27,color=c,va='center',ha='right')
save2(fig,4)

# 5 · de donde viene
fig,ax=base(5,'DE DÓNDE VIENE')
y=title(ax,['EL 99 % DEL GAS','ES ARGENTINO'],y0=210,size=76,step=86)
big3(ax,y,[('61.665 t','De las 62.166 que entraron en nueve meses'),('501 t','Todo el resto de los orígenes, juntos'),('0','Lo que produce Paraguay: se importa todo')],fs=72)
ax.text(70,1180,'Cualquier cambio de precio o de cupo del otro lado',fontfamily=B,fontweight='bold',fontsize=28,color=W,va='center')
ax.text(70,1222,'llega al surtidor sin escalas.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,5)

# 6 · que revisar
fig,ax=base(6,'QUÉ TIENE QUE REVISAR LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA HOY'],y0=210)
cards(ax,[('Compará tu venta contra el año pasado','El segmento cayó 11 %, pero no cayó parejo'),('Mirá la brecha con la nafta','Si la nafta baja, conviene menos convertir'),('La industria es la que está creciendo','La venta a granel en tu zona es el segmento en alza')],y+60,h=150,gap=26)
ax.text(70,1118,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1176,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save2(fig,6)
print('ok')
