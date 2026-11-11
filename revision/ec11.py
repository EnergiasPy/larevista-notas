import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-11-ecuador-baja-gasolina-diesel-bandas'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#FFD100','#0072CE','#EF3340')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'REGIÓN · ECUADOR',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'ECUADOR: LA GASOLINA Y EL DIÉSEL BAJAN OTRA VEZ',fontfamily=BB,fontsize=64,color=NV,va='center')
ax.text(80,214,'Desde el jueves 12 de noviembre, 5 centavos menos por galón: el quinto recorte mensual seguido',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
def card(x,y,w,h,k,big,lines,col,fs=64):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,290,450,300,'EXTRA Y ECOPAÍS','USD 3,12',['por galón (antes, unos 3,17).','Unos USD 0,83 por litro'],GR,fs=64)
card(570,290,450,300,'DIÉSEL','USD 3,06',['por galón (antes, unos 3,11).','Unos USD 0,81 por litro'],GR,fs=64)
card(1060,290,460,300,'DESDE JULIO','−19 CENTAVOS',['por galón acumulados en','cinco meses seguidos de bajas'],RD,fs=58)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'CÓMO SE FIJA EL PRECIO',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'Sistema de bandas: cada mes se recalcula según el petróleo, con suba máxima de 5 % y baja máxima de 10 %.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
ax.text(120,754,'La gasolina Súper queda afuera: su precio está liberado. Los nuevos precios rigen hasta el 11 de diciembre.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
ax.add_patch(Rectangle((80,830),1440,1,color='#DCE3EA'))
ax.text(80,872,'Datos: Gobierno del Ecuador. Precios por galón (3,785 litros), en dólares. Conversión a litros: cálculo propio.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('/tmp/ec11.png',facecolor='white'); Image.open('/tmp/ec11.png').convert('RGB').save(R+ID+'-1.jpg',quality=88); plt.close(fig)
print('ok')
