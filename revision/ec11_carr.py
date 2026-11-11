import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ec11/'; os.makedirs(O,exist_ok=True)
N=7
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#FFD100','#0072CE','#EF3340']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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
ID='2026-11-11-ecuador-baja-gasolina-diesel-bandas'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · ECUADOR')
for i,(l,c) in enumerate([('ECUADOR:',W),('LA GASOLINA',W),('Y EL DIÉSEL',G),('BAJAN OTRA VEZ',G)]):
    ax.text(66,280+i*142,l,fontfamily=BB,fontsize=104,color=c,va='center')
ax.add_patch(Rectangle((70,830),140,7,color=G))
for i,l in enumerate(['5 centavos menos por galón desde','el jueves 12: quinto mes seguido']):
    ax.text(70,905+i*62,l,fontfamily=B,fontweight='bold',fontsize=38,color=W,va='center')
ax.text(70,1095,'Miércoles 11 de noviembre',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'LOS NUEVOS PRECIOS')
y=title(ax,['POR GALÓN,','EN DÓLARES'])
big3(ax,y,[('USD 3,12','Extra y Ecopaís (antes, unos 3,17)'),('USD 3,06','diésel (antes, unos 3,11)'),('11 DE DICIEMBRE','hasta cuándo rigen')])
save2(fig,2)
fig,ax=base(3,'CINCO MESES DE BAJAS')
y=title(ax,['DESDE EL','PICO DE JUNIO'])
cards(ax,[('Junio','USD 3,31 las gasolinas y 3,25 el diésel'),('Noviembre','USD 3,12 y 3,06'),('Acumulado','Unos 19 centavos menos por galón')],y+60,h=140)
save2(fig,3)
fig,ax=base(4,'CÓMO SE FIJA')
y=title(ax,['EL SISTEMA','DE BANDAS'])
cards(ax,[('Cada mes','Se recalcula según el petróleo'),('Con límites','Sube hasta 5 % y baja hasta 10 %'),('Súper, afuera','Precio liberado: cada estación cobra distinto')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'EL COSTO PARA EL ESTADO')
y=title(ax,['AMORTIGUAR','CUESTA'])
big3(ax,y,[('USD 757 M','pérdida por importar derivados, enero a mayo'),('+60,7 %','frente al mismo período de 2025'),('USD 1,04','por galón de diésel cubría el Estado en julio')],fs=58)
save2(fig,5)
fig,ax=base(6,'COMPARADO CON PARAGUAY')
y=title(ax,['EL DIÉSEL,','POR LITRO'])
big3(ax,y,[('USD 0,81','en Ecuador desde el jueves'),('USD 1,49 a 1,52','en Paraguay, Petropar y privados'),('CASI EL DOBLE','lo que cuesta en Paraguay')],fs=58)
save2(fig,6)
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['EL ALIVIO','LLEGA DE A POCO'])
cards(ax,[('Operador ecuatoriano','Planificar compras con el ajuste del día 12'),('Paraguay','Próxima referencia: Petropar en diciembre'),('La región','Ecuador baja mientras Chile sigue subiendo')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,7)
print('ok')
