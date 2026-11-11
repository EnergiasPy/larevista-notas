import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ar11/'; os.makedirs(O,exist_ok=True)
N=7
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#74ACDF','#FFFFFF','#74ACDF']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
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
ID='2026-11-11-argentina-shell-edenor-manzano-mercuria'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · ARGENTINA')
ph=Image.open('/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/33e2a9d1-image.png').convert('RGB')
phh=700; cw=int(ph.height*1080/phh); x0=(ph.width-cw)//2+40; ph=ph.crop((x0,0,x0+cw,ph.height))
ax.imshow(ph.resize((1080,phh)),extent=(0,1080,140+phh,140),zorder=1)
rb(ax,20,140+phh-56,240,40,BG,8); ax.text(34,140+phh-36,'Foto de archivo',fontfamily=B,fontweight='semibold',fontsize=19,color=W,va='center',zorder=3)
yy=140+phh+75
for i,(l,c) in enumerate([('LAS ESTACIONES SHELL',W),('SUMAN SOCIOS LOCALES',G)]):
    ax.text(66,yy+i*88,l,fontfamily=BB,fontsize=80,color=c,va='center')
ax.text(70,yy+190,'Edenor y el grupo Manzano entran con Mercuria.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
save2(fig,1)
fig,ax=base(2,'QUIÉN TIENE QUÉ')
y=title(ax,['LOS NUEVOS','DUEÑOS'])
big3(ax,y,[('MERCURIA 60 %','trader suizo de energía, tiene el control'),('EDENOR 20 %','la mayor distribuidora eléctrica del país'),('SOUTHERN CONE 20 %','del grupo Integra Capital, de Manzano')],fs=56)
save2(fig,2)
fig,ax=base(3,'QUÉ HAY ADENTRO')
y=title(ax,['EL PAQUETE'])
big3(ax,y,[('892','estaciones de servicio Shell'),('101.000','barriles por día en la refinería de Dock Sud'),('BARRACAS','planta de lubricantes, terminales y aeroplantas')])
save2(fig,3)
fig,ax=base(4,'CÓMO SE LLEGÓ ACÁ')
y=title(ax,['DE RAÍZEN','A MERCURIA'])
cards(ax,[('Junio','Mercuria acuerda comprar el negocio de Raízen'),('Unos USD 1.420 millones','más la deuda de la compañía'),('Noviembre','Edenor y Southern Cone entran con 20 % cada uno')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'LA MARCA')
y=title(ax,['SHELL SIGUE','EN EL SURTIDOR'])
ph=Image.open('/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/814ce186-image.png').convert('RGB')
phh=int(ph.height*960/ph.width); ax.imshow(ph.resize((960,phh)),extent=(60,1020,y+40+phh,y+40),zorder=1)
rb(ax,76,y+40+phh-52,250,38,BG,8); ax.text(90,y+40+phh-33,'Imagen ilustrativa',fontfamily=B,fontweight='semibold',fontsize=19,color=W,va='center',zorder=3)
for j,t in enumerate(['La marca sigue, bajo licencia, a cargo de Signar Energy.','Para el cliente no cambia nada a la vista.','Lo que cambia es quién decide detrás de 892 estaciones.']):
    ax.text(70,y+115+phh+j*52,t,fontfamily=B,fontweight='semibold',fontsize=29,color=W if j==0 else M,va='center')
save2(fig,5)
fig,ax=base(6,'UN GRUPO QUE CRECE')
y=title(ax,['LUZ, GAS Y','COMBUSTIBLES'])
cards(ax,[('Edenor','Electricidad en el norte del AMBA'),('Metrogas','Compra del 70 % a YPF por USD 780 M'),('Shell','20 % de la red de estaciones')],y+60,h=140)
save2(fig,6)
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['QUIÉN NEGOCIA','CON VOS'])
cards(ax,[('Operador Shell en Argentina','Mirar condiciones, inversión y precios'),('Paraguay','La operación es solo del negocio argentino'),('La región','Marcas con licencia, dueños nuevos')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,7)
print('ok')
