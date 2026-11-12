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
ID='2026-11-12-mic-cambio-emblema-60-dias-resolucion-857'
Y='/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/yam/g_07.jpg'
def save2(fig,k): save(fig,f'{ID}-c{k}')
def qa(n,kick,tit,preg,resp):
    fig,ax=base(n,kick); y=title(ax,tit)
    ax.text(70,y+50,preg,fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center')
    h=110+len(resp)*56; rb(ax,60,y+100,960,h,CARD); ax.add_patch(Rectangle((60,y+100),10,h,color=G))
    for j,t in enumerate(resp): ax.text(100,y+160+j*56,t,fontfamily=B,fontweight='semibold',fontsize=35,color=W,va='center')
    ax.text(70,y+100+h+50,'Víctor Yambay, presidente de APESA',fontfamily=B,fontweight='semibold',fontsize=26,color=M,va='center')
    save2(fig,n)
fig,ax=base(1,'ENTREVISTA · VÍCTOR YAMBAY, PRESIDENTE DE APESA')
ph=Image.open(Y).convert('RGB'); hh=640; cr=ph.crop((0,0,740,640)); ax.imshow(cr,extent=(170,910,150+hh,150),zorder=1)
rb(ax,186,150+hh-56,370,40,BG,8); ax.text(200,150+hh-36,'Foto: Energías Paraguay 2026',fontfamily=B,fontweight='semibold',fontsize=19,color=W,va='center',zorder=3)
yy=150+hh+70
for j,(t,c2) in enumerate([('"ES UN PASO IMPORTANTÍSIMO',W),('PARA EL OPERADOR"',G)]):
    ax.text(66,yy+j*84,t,fontfamily=BB,fontsize=74,color=c2,va='center')
ax.text(70,yy+185,'El MIC bajó de 90 a 60 días el aviso',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center')
ax.text(70,yy+231,'para cambiar de emblema.',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center')
save2(fig,1)
fig,ax=base(2,'LA NOVEDAD · RESOLUCIÓN N.º 857 DEL MIC')
y=title(ax,['CAMBIO DE EMBLEMA:','DE 90 A 60 DÍAS'])
cards(ax,[('El aviso al emblema saliente','60 días antes de firmar con la nueva distribuidora'),('Se puede notificar por correo','A las direcciones declaradas en la plataforma VUE'),('La distribuidora entrante','Informa al MIC la primera factura en 48 horas hábiles')],y+60,h=140)
save2(fig,2)
qa(3,'ENTREVISTA','¿CÓMO LA RECIBE APESA?',['¿Era un pedido del sector?'],['"Si bien existen muchas más necesidades','que se tienen que atender, este es un','paso importantísimo para obtener','condiciones más justas y equilibradas','para el operador."'])
qa(4,'ENTREVISTA','¿QUÉ CAMBIA EN LA PRÁCTICA?',['Para el operador que quiere cambiar de emblema'],['"Le permite al operador no cesar sus','movimientos y no depender','excesivamente del solo criterio','de la distribuidora."'])
qa(5,'ENTREVISTA','¿ALCANZAN 60 DÍAS?',['¿O el plazo debería ser menor?'],['"El cambio de emblema ya no depende','del MIC, que solamente debe registrarlo.','Consideramos que con 30 días ya era','suficiente. De igual forma, estamos','conformes con el resultado."'])
qa(6,'ENTREVISTA','¿VIENEN MÁS CAMBIOS?',['Con las ventas y los márgenes como están'],['"Se esperan muchos cambios de','emblema, buscando mejores y más','equitativas condiciones de trabajo."'])
qa(7,'ENTREVISTA','LO QUE QUEDA PENDIENTE',['¿Qué le va a plantear APESA al MIC?'],['"Estamos abocados a buscar reglas de','juego para un sector más ordenado,','equitativo, sin distorsiones y, por','sobre todas las cosas, rentable."'])
fig,ax=base(8,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['MÁS PODER','PARA NEGOCIAR'])
cards(ax,[('Cambiar es más real','Un mes menos de espera'),('El aviso sigue siendo obligatorio','Con constancia de la fecha de recepción'),('Ojo con el contrato vigente','Revisar plazos, exclusividad y penalidades')],y+60,h=140)
ax.text(540,1180,'Leé la entrevista completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,8)
print('ok')
