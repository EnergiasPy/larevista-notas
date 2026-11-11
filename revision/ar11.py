import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-11-argentina-shell-edenor-manzano-mercuria'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#74ACDF','#FFFFFF','#74ACDF')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'REGIÓN · ARGENTINA',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'ARGENTINA: LOS NUEVOS DUEÑOS DE SHELL',fontfamily=BB,fontsize=64,color=NV,va='center')
ax.text(80,214,'Edenor y el grupo de José Luis Manzano entran como socios de Mercuria en la red de 892 estaciones',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
def card(x,y,w,h,k,big,lines,col,fs=64):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,290,450,300,'CONTROL','MERCURIA 60 %',['Trader suizo de energía:','compró en junio el negocio','argentino de Raízen'],NV,fs=58)
card(570,290,450,300,'SOCIO','EDENOR 20 %',['La mayor distribuidora','eléctrica del país, a través','de Edenor Inversiones'],GR,fs=58)
card(1060,290,460,300,'SOCIO','SOUTHERN CONE 20 %',['Southern Cone Investments,','del grupo Integra Capital','de José Luis Manzano'],GR,fs=40)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'QUÉ CONTROLAN',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'892 estaciones Shell, la refinería de Dock Sud (101.000 barriles por día) y la planta de Barracas.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
ax.text(120,754,'La marca Shell sigue en los surtidores, bajo licencia, a cargo de Signar Energy.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
ax.add_patch(Rectangle((80,830),1440,1,color='#DCE3EA'))
ax.text(80,872,'Datos de las empresas involucradas, al 11 de noviembre de 2026.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('/tmp/ar11.png',facecolor='white'); Image.open('/tmp/ar11.png').convert('RGB').save(R+ID+'-2.jpg',quality=88); plt.close(fig)
print('ok')
