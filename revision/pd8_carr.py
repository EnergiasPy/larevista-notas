import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/pd8/'; os.makedirs(O,exist_ok=True)
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






ID='2026-11-08-petropar-denuncia-ueno-reintegros'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · CASO UENO')
for i,(l,c) in enumerate([('PETROPAR',W),('DENUNCIÓ A LOS',W),('RESPONSABLES',G),('DE UENO',G)]):
    ax.text(66,280+i*130,l,fontfamily=BB,fontsize=118,color=c,va='center')
ax.add_patch(Rectangle((70,800),140,7,color=G))
for i,l in enumerate(['Y se terminó el reintegro que','llevaba clientes a sus estaciones']):
    ax.text(70,880+i*62,l,fontfamily=B,fontweight='bold',fontsize=44,color=W,va='center')
ax.text(70,1080,'Según el comunicado de Petropar del 6 de noviembre',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'QUÉ HIZO PETROPAR')
y=title(ax,['DENUNCIA PENAL','Y PEDIDO AL BCP'])
cards(ax,[('4 de noviembre','Pidió a la Superintendencia certificar sus saldos'),('6 de noviembre','Denuncia por presunta estafa y lesión de confianza'),('Medidas cautelares','Para proteger el patrimonio de la empresa')],y+60,h=140)
save2(fig,2)
fig,ax=base(3,'EL MOTIVO')
y=title(ax,['FONDOS QUE NO','PUEDE USAR'])
cards(ax,[('Depósitos a la vista en ueno','Bloqueados por la resolución del banco'),('El monto no fue informado','Petropar no publicó la cifra'),('No es la única entidad pública','También denunciaron el MEF y el Senave')],y+60,h=140)
save2(fig,3)
fig,ax=base(4,'DIÉSEL PORÃ · 50 LITROS')
y=title(ax,['ADIÓS AL','40 % DE VUELTA'])
for k,(big,t) in enumerate([('G. 5.571','por litro con el reintegro de ueno en octubre'),('G. 9.285','por litro desde el 3 de noviembre, sin reintegro'),('G. 205','de diferencia con la mayoría de los privados')]):
    yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
    ax.text(100,yy+60,big,fontfamily=BB,fontsize=66,color=W,va='center')
    ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
save2(fig,4)
fig,ax=base(5,'QUÉ CAMBIA EN LA PLAYA')
y=title(ax,['EL CLIENTE VUELVE','A MIRAR EL PRECIO'],size=80,step=88)
cards(ax,[('Estación Petropar','Mirá el volumen contra octubre'),('Otros emblemas','Oportunidad de recuperar clientes'),('Promos bancarias','El calendario diario vuelve a pesar')],y+60,h=140)
save2(fig,5)
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['PREPARÁ','A TU EQUIPO'])
cards(ax,[('Reintegros pendientes','No hay información oficial todavía'),('Derivá al BCP','Solo canales oficiales'),('Cuidado con estafas','Nadie puede "recuperar" tu dinero por link')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,6)
print('ok')
