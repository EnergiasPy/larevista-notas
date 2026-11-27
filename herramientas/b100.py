import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-27-b100-biodiesel-puro-barcazas-paraguay-resolucion-908'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.add_patch(Rectangle((0,0),1600,18,fill=False,ec='#DCE3EA',lw=1))
ax.text(80,72,'PARAGUAY · BIOCOMBUSTIBLES',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'BIODIÉSEL PURO B100 PARA LAS BARCAZAS',fontfamily=BB,fontsize=62,color=NV,va='center')
ax.text(80,214,'Resolución N° 908/2026 del MIC: un régimen propio, fuera del surtidor',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))

def card(x,w,k,big,t1,t2,col,fs=80):
    rb(ax,x,290,w,254,SO,10); ax.add_patch(Rectangle((x,290),8,254,color=col))
    ax.text(x+40,338,k,fontfamily=B,fontweight='bold',fontsize=20,color=MU,va='center')
    ax.text(x+40,418,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    ax.text(x+40,492,t1,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
    ax.text(x+40,522,t2,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,450,'LO QUE SE HABILITA','B100','biodiésel puro, sin mezcla,','para abastecer embarcaciones',GR)
card(570,450,'DÓNDE SE CARGA','MUELLES','puestos de suministro en muelles','y atracaderos habilitados',NV,fs=64)
card(1060,460,'LA MEZCLA DEL SURTIDOR','NO CAMBIA','B7 hasta el 31 de diciembre','y B8 desde enero de 2027',MU,fs=64)

rb(ax,80,582,1440,214,NV,10)
ax.text(120,632,'POR QUÉ LA FLOTA: EL CLIENTE QUE YA ESTÁ',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
for i,(seg,val,uni,off,det) in enumerate([('BARCAZAS','3.000','y 400 remolcadores',150,'la tercera flota fluvial del mundo'),
                                          ('CARGA MOVIDA EN 2025','25','millones de toneladas',78,'según el CAFYM'),
                                          ('COMERCIO EXTERIOR','80','% pasa por la hidrovía',78,'hoy, todo con gasoil importado')]):
    x=120+i*470
    ax.text(x,686,seg,fontfamily=B,fontweight='bold',fontsize=18,color='#9FB3C8',va='center')
    ax.text(x,734,val,fontfamily=BB,fontsize=50,color='white',va='center')
    ax.text(x+off,740,uni,fontfamily=B,fontweight='semibold',fontsize=19,color='#C9D4DF',va='center')
    ax.text(x,774,det,fontfamily=B,fontweight='semibold',fontsize=17,color='#C9D4DF',va='center')

ax.text(80,850,'AÚN SIN CARGAR',fontfamily=BB,fontsize=46,color=RD,va='center')
ax.text(410,850,'la primera operación se hará al terminar las coordinaciones técnicas y operativas.',fontfamily=B,fontweight='semibold',fontsize=21,color=NV,va='center')
ax.add_patch(Rectangle((80,884),1440,1,color='#DCE3EA'))
ax.text(80,920,'Datos: Ministerio de Industria y Comercio (Resolución 908/2026) y comunicado conjunto de CAFYM, CAPPRO y BIOCAP.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('b100-web.png',facecolor='white'); Image.open('b100-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88); plt.close(fig)
import os; print('ok',round(os.path.getsize(R+ID+'-1.jpg')/1024),'KB')
