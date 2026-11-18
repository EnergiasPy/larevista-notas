import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/it18/'; os.makedirs(O,exist_ok=True)
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
ID='2026-11-18-itaipu-tarifa-vence-31-diciembre-anexo-c'
def save2(fig,k): save(fig,f'{ID}-c{k}')

fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2) in enumerate([('LA TARIFA',W),('DE ITAIPÚ VENCE',W),('EL 31 DE',G),('DICIEMBRE',G)]):
    ax.text(66,300+i*128,l,fontfamily=BB,fontsize=104,color=c2,va='center')
ax.add_patch(Rectangle((70,830),140,7,color=G))
ax.text(70,906,'Seis semanas, sin propuesta',fontfamily=B,fontweight='semibold',fontsize=40,color=W,va='center')
ax.text(70,960,'pública paraguaya, y 1.250',fontfamily=B,fontweight='semibold',fontsize=40,color=W,va='center')
ax.text(70,1014,'millones de dólares en juego.',fontfamily=B,fontweight='semibold',fontsize=40,color=W,va='center')
save2(fig,1)

fig,ax=base(2,'LO QUE ESTÁ VENCIENDO')
y=title(ax,['UN ACUERDO','DE TRES AÑOS'],y0=210,size=80,step=92)
big3(ax,y,[('US$ 19,28','Por kilovatio-mes, acordado en mayo de 2024'),('2024, 2025 Y 2026','Los tres años que cubre'),('31 DE DICIEMBRE','Cuando deja de regir')],fs=72)
ax.text(70,1180,'Desde 2027 la tarifa la define',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'la negociación del Anexo C del Tratado.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,2)

fig,ax=base(3,'LO QUE DEJA HOY')
y=title(ax,['1.250 MILLONES','POR AÑO'],y0=210,size=78,step=90)
cards(ax,[('US$ 650 millones','para inversión social'),('US$ 280 millones','en concepto de royalties'),('US$ 265 millones','por compensación de energía'),('US$ 53 millones','en utilidades de capital')],y+40,h=128,gap=22)
ax.text(70,1200,'Datos del Ministerio de Industria y Comercio.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,3)

fig,ax=base(4,'QUÉ QUIERE BRASIL')
y=title(ax,['UNA TARIFA','MUCHO MENOR'],y0=210,size=78,step=90)
big3(ax,y,[('US$ 8 A 10','Lo que quedaría si refleja sólo costos de operación'),('LA MITAD','De lo que se cobra hoy'),('DESDE 2027','Cuando arranca el esquema nuevo')],fs=76)
ax.text(70,1180,'Si la tarifa cae a la mitad, los recursos',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'se achican en la misma proporción.',fontfamily=B,fontsize=27,color=M,va='center')
save2(fig,4)

fig,ax=base(5,'QUÉ PIDE PARAGUAY')
y=title(ax,['VENDER AL','MERCADO LIBRE'],y0=210,size=76,step=88)
cards(ax,[('Colocar el excedente a precio de mercado','En lugar de cederlo a precio de costo'),('Participación técnica de la ANDE','En la mesa de negociación'),('Cerrar la revisión del Anexo C','Lo que define las próximas décadas')],y+50,h=150,gap=26)
save2(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA ENTENDER'],y0=210,size=76,step=88)
cards(ax,[('Tu factura no cambia mañana','La ANDE congeló su tarifa por un año'),('Más barato no es automáticamente mejor','El Estado recibiría bastante menos'),('Mirá la venta al mercado brasileño','Es lo que más puede mover el resultado')],y+50,h=150,gap=26)
ax.text(70,1118,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1176,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save2(fig,6)
print('ok')
