import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-08-bolivia-diesel-precio-internacional-paz'; R='/home/claude/larevista-notas/img/'
BOF=('#D52B1E','#F9E300','#007934')
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
ID='2026-11-10-brasil-prorroga-impuesto-cero-gasolina'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#009C3B','#FFDF00','#002776')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'REGIÓN · BRASIL',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'BRASIL PRORROGA EL IMPUESTO CERO A LA GASOLINA',fontfamily=BB,fontsize=62,color=NV,va='center')
ax.text(80,214,'Decreto 13.159: la exención que vencía el 9 de noviembre sigue hasta el 9 de diciembre',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
def card(x,y,w,h,k,big,t1,t2,col):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+50,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+125,big,fontfamily=BB,fontsize=78,color=col,va='center')
    ax.text(x+40,y+200,t1,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
    ax.text(x+40,y+232,t2,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,290,450,270,'NUEVO VENCIMIENTO','9 DE DIC',['exención de PIS/Cofins y Cide','a la gasolina y al etanol'][0],'a la gasolina y al etanol',GR)
card(570,290,450,270,'GASOLINA','R$ 0,89',['por litro sin impuestos federales'][0],'(R$ 0,79 PIS/Cofins + R$ 0,10 Cide)',GR)
card(1060,290,460,270,'COSTO FISCAL','R$ 3.570 M',['estimado para los próximos'][0],'30 días, según el Gobierno',NV)
rb(ax,80,600,1440,160,NV,10)
ax.text(120,645,'EL DIÉSEL, EN SUSPENSO',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,692,'Subvención de R$ 2,12 por litro y refuerzo de R$ 1,40 a los importadores, que vence esta semana.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
ax.text(120,728,'Etanol hidratado: impuestos en cero (R$ 0,19 por litro) y subvención de R$ 0,428 a los productores.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
ax.text(80,815,'R$ 6,48',fontfamily=BB,fontsize=54,color=RD,va='center')
ax.text(270,815,'precio medio de la gasolina común en Brasil, según la ANP (25 al 31 de octubre).',fontfamily=B,fontweight='semibold',fontsize=21,color=NV,va='center')
ax.add_patch(Rectangle((80,862),1440,1,color='#DCE3EA'))
ax.text(80,900,'Datos: Gobierno de Brasil (Decreto 13.159, DOU 9/11/2026), Ministerio de Hacienda y ANP.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('br10-web.png',facecolor='white'); Image.open('br10-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88); plt.close(fig)
print('ok')
