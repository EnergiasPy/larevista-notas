import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-27-cuanto-cuesta-el-diesel-en-brasil-subsidio-prorroga'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#009C3B','#FFDF00','#002776')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'REGIÓN · BRASIL',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'DIÉSEL EN BRASIL: EL S10 PROMEDIA R$ 7,26',fontfamily=BB,fontsize=62,color=NV,va='center')
ax.text(80,214,'Hacienda anunció 30 días más de subsidio de R$ 2,12 por litro de diésel A',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))

# dos columnas: con y sin subsidio
def precio(x,w,k,big,sub,col,bg):
    rb(ax,x,290,w,250,bg,10); ax.add_patch(Rectangle((x,290),8,250,color=col))
    ax.text(x+40,340,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU if bg==SO else '#C9D4DF',va='center')
    ax.text(x+40,428,big,fontfamily=BB,fontsize=96,color=col,va='center')
    ax.text(x+40,502,sub,fontfamily=B,fontweight='semibold',fontsize=21,color=NV if bg==SO else 'white',va='center')
precio(80,700,'PRECIO MEDIO DEL S10 (15 AL 21/11)','R$ 7,26','por litro, con la subvención vigente',GR,SO)
precio(820,700,'SIMULACIÓN, NO UN PRECIO MEDIDO','R$ 9,06','si el subsidio se trasladara por completo',RD,SO)
ax.text(80,578,'+19,8 %',fontfamily=BB,fontsize=46,color=RD,va='center')
ax.text(258,578,'subió el precio medio del diésel S10 frente al mismo período del año pasado.',fontfamily=B,fontweight='semibold',fontsize=21,color=NV,va='center')

# franja comparativa regional
rb(ax,80,624,1440,196,NV,10)
ax.text(120,672,'EL LITRO DE DIÉSEL EN LA REGIÓN, EN DÓLARES',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
for i,(pais,val,det) in enumerate([('BRASIL','USD 1,27','con subvención; sin ella, unos USD 1,58'),
                                   ('PARAGUAY','USD 1,40','diésel común, G. 8.940 a G. 8.990'),
                                   ('BOLIVIA','USD 1,75','Bs 20,57 desde el 24 de noviembre')]):
    x=120+i*470
    ax.text(x,726,pais,fontfamily=B,fontweight='bold',fontsize=19,color='#9FB3C8',va='center')
    ax.text(x,766,val,fontfamily=BB,fontsize=44,color='white',va='center')
    ax.text(x,800,det,fontfamily=B,fontweight='semibold',fontsize=16,color='#C9D4DF',va='center')

ax.text(80,872,'R$ 85.000 M',fontfamily=BB,fontsize=54,color=NV,va='center')
ax.text(420,872,'costarían en 2026 las políticas de contención de precios, con esta prórroga incluida.',fontfamily=B,fontweight='semibold',fontsize=21,color=NV,va='center')
ax.add_patch(Rectangle((80,904),1440,1,color='#DCE3EA'))
ax.text(80,936,'Datos: Ministerio de Hacienda y Ministerio de Planificación de Brasil, ANP y precios de referencia de Paraguay y Bolivia.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('br27-web.png',facecolor='white'); Image.open('br27-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88); plt.close(fig)
import os; print('ok',round(os.path.getsize(R+ID+'-1.jpg')/1024),'KB')
