import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/it11/'; os.makedirs(O,exist_ok=True)
N=8
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
ID='2026-11-11-itaipu-paraguay-supera-2025-solar-flotante'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
ph=Image.open('/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/d16d967c-image.jpg').convert('RGB')
pw=1080; phh=640; ch=int(ph.width*phh/pw); ph=ph.crop((0,(ph.height-ch)//2,ph.width,(ph.height-ch)//2+ch))
ax.imshow(ph.resize((pw,phh)),extent=(0,1080,140+phh,140),zorder=1)
rb(ax,20,140+phh-56,330,40,BG,8); ax.text(34,140+phh-36,'Foto: Itaipú Binacional',fontfamily=B,fontweight='semibold',fontsize=19,color=W,va='center',zorder=3)
yy=140+phh+80
for i,(l,c) in enumerate([('PARAGUAY, POR SUPERAR',W),('TODA LA ENERGÍA DE ITAIPÚ',G),('QUE USÓ EN 2025',G)]):
    ax.text(66,yy+i*84,l,fontfamily=BB,fontsize=70,color=c,va='center')
ax.text(70,yy+250,'Faltan 1.647 GWh. Y en el embalse, el sol.',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center')
save2(fig,1)
fig,ax=base(2,'LOS NÚMEROS')
y=title(ax,['ENERO A','OCTUBRE'])
big3(ax,y,[('24.121 GWh','entregó Itaipú al Paraguay'),('25.768 GWh','fue todo 2025, un récord'),('1.647 GWh','es lo que falta')])
save2(fig,2)
fig,ax=base(3,'CUÁNDO')
y=title(ax,['ALREDEDOR DEL','20 DE NOVIEMBRE'])
cards(ax,[('Octubre: 2.503 GWh','Unos 81 GWh por día'),('A ese ritmo','La marca de 2025 cae en unos 20 días'),('Es un cálculo propio','Depende del calor de noviembre')],y+60,h=140)
save2(fig,3)
fig,ax=base(4,'CADA AÑO, MÁS')
y=title(ax,['UN CONSUMO','QUE NO PARA'])
cards(ax,[('2024','Unos 20.400 GWh'),('2025','25.768 GWh: +26,4 %'),('2026 (proyección)','Cerca de 29.000 GWh: +13 %')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'LA CONTRACARA')
y=title(ax,['MENOS PARA','VENDER'])
cards(ax,[('66.071 GWh','generó Itaipú entre enero y octubre'),('Cerca del 36 %','fue para el Paraguay'),('Más consumo propio','Menos excedente para ceder a Brasil')],y+60,h=140)
save2(fig,5)
fig,ax=base(6,'Y EN EL EMBALSE, EL SOL')
y=title(ax,['SOLAR','FLOTANTE'])
big3(ax,y,[('1,1 MWp','1.584 paneles en Hernandarias'),('10 MW','la proyección, con baterías'),('2027','resultados del estudio binacional')])
save2(fig,6)
fig,ax=base(7,'ASÍ FUNCIONA')
y=title(ax,['PANELES','SOBRE EL AGUA'])
ph=Image.open('/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/92d0fe36-image.jpg').convert('RGB')
phh=int(ph.height*960/ph.width); ax.imshow(ph.resize((960,phh)),extent=(60,1020,y+40+phh,y+40),zorder=1)
rb(ax,76,y+40+phh-52,250,38,BG,8); ax.text(90,y+40+phh-33,'Imagen ilustrativa',fontfamily=B,fontweight='semibold',fontsize=19,color=W,va='center',zorder=3)
for j,t in enumerate(['No ocupan tierra cultivable ni monte.','Itaipú estudia sumar baterías para','usar la energía en las horas pico.']):
    ax.text(70,y+120+phh+j*50,t,fontfamily=B,fontweight='semibold',fontsize=30,color=W if j==0 else M,va='center')
save2(fig,7)
fig,ax=base(8,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['ENERGÍA BARATA','NO INFINITA'])
cards(ax,[('Tarifas en discusión','ANDE e Itaipú 2027, sin definir'),('La solar ya cuenta','El canopy también puede generar'),('Antes del verano','Revisar equipos de frío y tablero')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,8)
print('ok')
