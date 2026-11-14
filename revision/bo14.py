import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-14-bolivia-importadores-privados-diesel-ypfb'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#D52B1E','#F9E300','#007934')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
    ax.text(80,72,k,fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
    ax.text(76,148,t,fontfamily=BB,fontsize=62,color=NV,va='center')
    ax.text(80,214,b,fontfamily=B,fontsize=23,color=MU,va='center')
    ax.add_patch(Rectangle((80,240),80,5,color=RD))
    return fig,ax
def foot(fig,ax,src,name):
    ax.add_patch(Rectangle((80,830),1440,1,color='#DCE3EA'))
    ax.text(80,872,src,fontfamily=B,fontsize=18,color=MU,va='center')
    ax.add_patch(Rectangle((0,967),1600,100,color=NV))
    ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
    ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
    fig.savefig('/tmp/w.png',facecolor='white'); Image.open('/tmp/w.png').convert('RGB').save(R+ID+name,quality=88); plt.close(fig)
def card(x,y,w,h,k,big,lines,col,fs=64):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
fig,ax=hdr('REGIÓN · BOLIVIA','DIÉSEL: YPFB VS. LOS IMPORTADORES PRIVADOS','Precio y costo por litro, en bolivianos (Bs), noviembre de 2026')
vals=[('PRECIO REGULADO DE YPFB',17.95,GR,'Bs 17,95'),('COSTO PRIVADO (MÍNIMO)',20.50,RD,'Bs 20,50'),('COSTO PRIVADO (MÁXIMO)',21.50,RD,'Bs 21,50')]
for i,(l,v,c,t) in enumerate(vals):
    y=300+i*150; w=v*55
    ax.text(80,y+20,l,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    rb(ax,80,y+45,w,70,c,8); ax.text(80+w+24,y+80,t,fontfamily=B,fontweight='bold',fontsize=40,color=c,va='center')
ax.text(80,770,'De los Bs 21,50 de costo de importación, unos Bs 3,50 son impuestos.',fontfamily=B,fontweight='semibold',fontsize=21,color=NV,va='center')
foot(fig,ax,'Datos: ANH (precio regulado) y el importador privado Stevo Ostoic (costos de importación), 14 de noviembre de 2026.','-1.jpg')
fig,ax=hdr('REGIÓN · BOLIVIA','QUÉ PIDEN LOS IMPORTADORES PRIVADOS','Los reclamos al Gobierno tras el fin de la subvención al diésel')
items=[('1','REGLAS IGUALES','para YPFB y los importadores privados'),('2','UN ROL CLARO','para la estatal y para los privados'),('3','PRECIOS ESTABLES','una metodología que se aplique siempre igual'),('4','SEGURIDAD PARA INVERTIR','en infraestructura, estaciones y fidelización')]
for i,(n,t,d) in enumerate(items):
    x=80+(i%2)*730; y=290+(i//2)*230; rb(ax,x,y,710,200,SO,10); ax.add_patch(Rectangle((x,y),8,200,color=GR))
    ax.text(x+50,y+100,n,fontfamily=BB,fontsize=90,color=GR,va='center',ha='center')
    ax.text(x+110,y+70,t,fontfamily=BB,fontsize=44,color=NV,va='center')
    ax.text(x+110,y+130,d,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
ax.text(80,790,'Demanda de diésel: entre 30 % y 40 % menos tras la suba de precios, según los importadores.',fontfamily=B,fontweight='bold',fontsize=21,color=RD,va='center')
foot(fig,ax,'Datos: declaraciones del importador privado Stevo Ostoic y Ministerio de Hidrocarburos y Energías de Bolivia, noviembre de 2026.','-2.jpg')
print('ok')
