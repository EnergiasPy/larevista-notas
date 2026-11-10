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
ID='2026-11-10-mopc-registro-autogeneracion-renovable'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'PARAGUAY · ENERGÍAS RENOVABLES',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'AUTOGENERACIÓN: YA HAY REGISTRO HASTA 1 MW',fontfamily=BB,fontsize=62,color=NV,va='center')
ax.text(80,214,'El MOPC habilitó la inscripción para quienes generan electricidad con fuentes renovables',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
def card(x,y,w,h,k,big,lines,col):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=64,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,290,450,300,'QUIÉN SE REGISTRA','HASTA 1 MW',['Autogeneración y cogeneración','solar, eólica, biomasa o','geotérmica, conectada o aislada'],GR)
card(570,290,450,300,'QUÉ SE AHORRA','SIN LICENCIA',['Hasta 1 MW alcanza con el','registro. Más de 1 MW requiere','la autorización del MOPC'],NV)
card(1060,290,460,300,'QUÉ PERMITE','EXCEDENTES',['Vender a la ANDE lo que sobra,','con balance semestral','en guaraníes'],RD)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'CÓMO SE INSCRIBE',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'Formulario, instructivo y modelos para personas físicas y jurídicas en el portal del VMME (minasyenergia.mopc.gov.py).',fontfamily=B,fontweight='semibold',fontsize=18,color='white',va='center')
ax.text(120,754,'Consultas: MOPC, Oliva y Alberdi 411, Asunción · (021) 414-9000 · de 7:00 a 15:00.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.add_patch(Rectangle((80,830),1440,1,color='#DCE3EA'))
ax.text(80,872,'Base legal: Ley 7599/2025, Decreto 6034/2026 y Resolución MOPC 996/2026. Datos: MOPC, Viceministerio de Minas y Energía y ANDE.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('mo10-web.png',facecolor='white'); Image.open('mo10-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88); plt.close(fig)
print('ok')
