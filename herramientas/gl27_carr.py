import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw, ImageFont
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
NVt=(15,33,61)
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/gl27/'; os.makedirs(O,exist_ok=True)
SRC='/home/claude/fotos_gas/g1.jpg'
F=lambda n,s: ImageFont.truetype('/home/claude/chart/'+n,s)
N=7
ID='2026-11-27-baja-el-gas-de-garrafa-paraguay-petropar-nande-gas'
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
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
def cards(ax,items,y0,h=140,gap=22):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.36,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.68,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def big3(ax,y,items,fs=62,col=None):
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=(col[k] if col else G)))
        ax.text(100,yy+60,big,fontfamily=BB,fontsize=fs,color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k): fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)

# ---- 1 portada con foto (PIL) ----
CW,CH=1080,1350; PH=760
ph=Image.open(SRC).convert('RGB')
s=max(CW/ph.width,PH/ph.height); ph=ph.resize((round(ph.width*s),round(ph.height*s)),Image.LANCZOS)
x=(ph.width-CW)//2; y=max(0,(ph.height-PH)//2)
im=Image.new('RGB',(CW,CH),NVt); im.paste(ph.crop((x,y,x+CW,y+PH)),(0,0))
velo=Image.new('RGBA',(CW,PH),NVt+(0,)); px=velo.load()
for yy in range(PH):
    a=0 if yy<430 else int(238*((yy-430)/330)**1.1)
    for xx in range(CW): px[xx,yy]=NVt+(a,)
b=im.convert('RGBA'); b.alpha_composite(velo,(0,0)); im=b.convert('RGB')
d=ImageDraw.Draw(im)
for i,c in enumerate(['#D52B1E','#FFFFFF','#0038A8']): d.rectangle((0,i*7,CW,i*7+7),fill=c)
d.text((CW-70-d.textlength('Foto: Petropar',font=F('Barlow-SemiBold.ttf',22)),PH-38),'Foto: Petropar',font=F('Barlow-SemiBold.ttf',22),fill='#C9D4DF')
kk='LA ESTACIÓN DEL FUTURO · PARAGUAY'; kf=F('Barlow-Bold.ttf',26)
d.rounded_rectangle((70,520,70+d.textlength(kk,font=kf)+40,568),9,fill='#3A7D44'); d.text((90,528),kk,font=kf,fill='white')
yy=620
for l,c in [('BAJA EL GAS',W),('DE GARRAFA',W),('EN PARAGUAY','#76C46E')]:
    d.text((66,yy),l,font=F('BebasNeue-Regular.ttf',108),fill=c); yy+=118
d.rectangle((70,yy+30,70+140,yy+37),fill='#76C46E'); yy+=80
for l in ['G. 600 menos por kilo en el','Ñande Gas de Petropar, desde hoy']:
    d.text((70,yy),l,font=F('Barlow-Bold.ttf',40),fill=W); yy+=58
d.text((70,1180),'Qué cambia para la estación',font=F('Barlow-SemiBold.ttf',28),fill='#9FB3C8')
d.text((70,1282),f'1/{N}',font=F('BarlowCondensed-Bold.ttf',24),fill='#9FB3C8')
d.text((470,1282),'Deslizá  »',font=F('Barlow-SemiBold.ttf',22),fill='#9FB3C8')
t='energiaslatam.com'; f=F('BarlowCondensed-Bold.ttf',28)
d.text((CW-70-d.textlength(t,font=f),1280),t,font=f,fill=W)
im.save(R+f'{ID}-c1.jpg',quality=92)

# ---- 2 el anuncio ----
fig,ax=base(2,'EL ANUNCIO')
y=title(ax,['CUÁNTO','BAJA'])
big3(ax,y,[('G. 600','menos por kilo de Ñande Gas'),('G. 6.000','menos por garrafa de 10 kilos'),('Desde hoy','viernes 27 de noviembre')],fs=66,col=[G,G,W])
save(fig,2)

# ---- 3 que no bajo ----
fig,ax=base(3,'LO QUE NO CAMBIÓ')
y=title(ax,['NAFTAS','Y DIÉSEL'])
cards(ax,[('No entraron en el anuncio','La rebaja es solo del gas de uso doméstico'),('"No va a ser la última"','Dijo el presidente Pedro Alliana'),('Lunes o martes','Cuándo prometió los próximos anuncios')],y+60)
save(fig,3)

# ---- 4 donde pega ----
fig,ax=base(4,'EL MERCADO DEL GLP')
y=title(ax,['DÓNDE PEGA','Y DÓNDE NO'])
big3(ax,y,[('30.275','toneladas en garrafas: el canal que baja de precio'),('18.823','toneladas en estaciones: el autogas cayó 11,3 %'),('11.222','toneladas en industrias: el único que crece')],fs=62,col=[G,RD,W])
save(fig,4)

# ---- 5 el dato estructural ----
fig,ax=base(5,'DE DÓNDE VIENE EL GAS')
y=title(ax,['PARAGUAY','NO PRODUCE GLP'],size=76,step=88)
cards(ax,[('99,2 % viene de la Argentina','De 62.166 toneladas importadas, 61.665'),('Sin alternativa inmediata','Un cambio del otro lado llega sin escalas'),('Petropar marca el piso','Lidera el autogas con el 28,7 % del volumen')],y+60)
save(fig,5)

# ---- 6 que significa ----
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA REVISAR'])
cards(ax,[('Si vendés garrafas','Se movió el precio de referencia del mercado'),('Si despachás autogas','Tu surtidor no cambió: mirá si baja el granel'),('El fin de semana del 5','Feriado el 7 y Ruta 2 cerrada a los cisternas')],y+60)
save(fig,6)

# ---- 7 cierre ----
fig,ax=base(7,'')
ax.text(540,430,'LEÉ LA NOTA',fontfamily=BB,fontsize=104,color=W,va='center',ha='center')
ax.text(540,540,'COMPLETA EN',fontfamily=BB,fontsize=104,color=W,va='center',ha='center')
ax.text(540,660,'energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=58,color=G,va='center',ha='center')
ax.add_patch(Rectangle((430,730),220,6,color=G))
ax.text(540,820,'Seguinos para la noticia del sector',fontfamily=B,fontweight='semibold',fontsize=34,color=M,va='center',ha='center')
ax.text(540,870,'todos los días',fontfamily=B,fontweight='semibold',fontsize=34,color=M,va='center',ha='center')
ax.text(540,990,'Link en la bio',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center',ha='center')
save(fig,7)
print('ok')
