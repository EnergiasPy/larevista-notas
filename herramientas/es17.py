import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-16-ande-licita-640-mw-chaco-solar-baterias'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
ID='2026-11-17-cuantas-estaciones-hay-paraguay-red-emblemas'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
    ax.text(80,72,k,fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
    ax.text(76,148,t,fontfamily=BB,fontsize=58,color=NV,va='center')
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

# -1 · ranking de marcas
fig,ax=hdr('PARAGUAY · RED DE ESTACIONES','2.880 ESTACIONES Y NINGUNA SIN BANDERA','Cuántas bocas de expendio hay y cómo se reparten entre las marcas')
D=[('COPETROL',387,'13,4 %'),('SHELL',363,'12,6 %'),('PETROPAR',302,'10,5 %'),('PETROBRAS',245,'8,5 %'),('PUMA',180,'6,3 %'),('PETROSUR',160,'5,6 %')]
for i,(n,v,p) in enumerate(D):
    y=296+i*82; rb(ax,80,y,1440,70,SO,10); ax.add_patch(Rectangle((80,y),8,70,color=GR))
    ax.text(124,y+36,n,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.text(1000,y+36,str(v),fontfamily=BB,fontsize=38,color=NV,va='center',ha='right')
    ax.text(1480,y+36,p,fontfamily=B,fontweight='bold',fontsize=23,color=GR,va='center',ha='right')
ax.text(80,806,'Las cinco primeras marcas concentran el 51,3 % de la red. Hay 23 marcas en total.',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
foot(fig,ax,'Datos: registro de estaciones de servicio del Ministerio de Industria y Comercio, consultado el 17 de noviembre de 2026.','-1.jpg')

# -2 · donde estan
fig,ax=hdr('DÓNDE ESTÁN','UN TERCIO DE LA RED ESTÁ EN EL ÁREA METROPOLITANA','Estaciones por departamento y el contraste con el Chaco')
card(80,290,460,300,'CENTRAL Y ASUNCIÓN','928',['el 32,2 % de todas las','estaciones del país'],NV,fs=92)
card(570,290,460,300,'TODO EL CHACO','90',['el 3,1 %, en más de la mitad','de la superficie nacional'],RD,fs=92)
card(1060,290,460,300,'ALTO PARAGUAY','13',['el departamento con','menos estaciones'],MU,fs=92)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'CENTRAL 739 · ALTO PARANÁ 364 · CAAGUAZÚ 252 · ITAPÚA 240',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
ax.text(120,730,'Por ciudad: Asunción 189, Ciudad del Este 129, San Lorenzo 113, Luque 97, Fernando de la Mora 80.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
foot(fig,ax,'Datos: registro de estaciones de servicio del MIC. Procesamiento y mapa interactivo: Energías LATAM.','-2.jpg')
print('ok')
