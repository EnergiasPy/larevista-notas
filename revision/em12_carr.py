import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/em12/'; os.makedirs(O,exist_ok=True)
N=7
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
ID='2026-11-12-mic-cambio-emblema-60-dias-resolucion-857'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c) in enumerate([('CAMBIAR DE',W),('EMBLEMA AHORA',W),('LLEVA MENOS',G),('TIEMPO',G)]):
    ax.text(66,280+i*142,l,fontfamily=BB,fontsize=104,color=c,va='center')
ax.add_patch(Rectangle((70,830),140,7,color=G))
for i,l in enumerate(['El MIC bajó de 90 a 60 días el aviso','previo. Resolución N.º 857']):
    ax.text(70,905+i*62,l,fontfamily=B,fontweight='bold',fontsize=38,color=W,va='center')
ax.text(70,1095,'Jueves 12 de noviembre',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'EL PLAZO')
y=title(ax,['DE 90','A 60 DÍAS'])
cards(ax,[('A quién se avisa','Al emblema saliente'),('Cuándo','60 días antes de firmar con la nueva distribuidora'),('Antes','Eran 90 días, y el proceso podía llegar a 120')],y+60,h=140)
save2(fig,2)
fig,ax=base(3,'CÓMO SE NOTIFICA')
y=title(ax,['TAMBIÉN','POR CORREO'])
cards(ax,[('Correo electrónico','A las direcciones declaradas en la plataforma VUE'),('Otros medios','Nota, telegrama u otro medio fehaciente'),('Si hay acuerdo','Vale la rescisión o la nota de conformidad')],y+60,h=140)
save2(fig,3)
fig,ax=base(4,'LA DISTRIBUIDORA ENTRANTE')
y=title(ax,['UNA OBLIGACIÓN','NUEVA'])
cards(ax,[('Informar la primera factura','A la Dirección General de Combustibles'),('48 horas hábiles','Desde la emisión de la factura'),('Qué informar','Fecha, número, productos y volumen')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'LAS MULTAS')
y=title(ax,['EN JORNALES','MÍNIMOS'])
big3(ax,y,[('100','por no registrar el cambio a tiempo'),('HASTA 200','para la distribuidora entrante y el operador'),('100','por no informar la primera factura')])
save2(fig,5)
fig,ax=base(6,'POR QUÉ LO CAMBIAN')
y=title(ax,['MÁS','COMPETENCIA'])
cards(ax,[('Menos espera','60 días alcanzan para coordinar la transición'),('Sin cortes','Evitar interrupciones de la actividad'),('El argumento del MIC','Libertad de actividad económica y de competencia')],y+60,h=140)
save2(fig,6)
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['MÁS PODER','PARA NEGOCIAR'])
cards(ax,[('Cambiar es más real','Un mes menos de espera'),('El aviso sigue siendo obligatorio','Con constancia de la fecha de recepción'),('Ojo con el contrato vigente','Revisar plazos, exclusividad y penalidades')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,7)
print('ok')
