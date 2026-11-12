import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-12-uruguay-transportistas-combustible-contratos'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#0038A8','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
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
fig,ax=hdr('REGIÓN · URUGUAY','URUGUAY: LOS FLETEROS PIDEN CAMBIAR LOS CONTRATOS','Transporte de combustibles entre las plantas de ANCAP y las estaciones de servicio')
def card(x,y,w,h,k,big,lines,col,fs=64):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,290,450,300,'EL CONTRATO','2 AÑOS',['Con renovación automática.','El gremio lo considera corto'],RD)
card(570,290,450,300,'EL CAMIÓN','USD 250.000',['Tractor y cisterna: entre','USD 220.000 y 250.000.','Se renueva cada 10 años'],NV,fs=58)
card(1060,290,460,300,'LA TARIFA','7 AÑOS',['es el plazo de amortización','que supone la fórmula','de la URSEA'],GR)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'EL ANTECEDENTE',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'En noviembre de 2023, un paro de 72 horas de los transportistas dejó estaciones sin combustible.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(120,754,'Hoy el reclamo va por el Senado: piden previsibilidad y un ámbito de diálogo. No hay amenaza de paro.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
foot(fig,ax,'Datos: Asociación de Transportistas de Combustibles (ATC), ANCAP y URSEA, al 11 de noviembre de 2026.','-1.jpg')
print('ok')
