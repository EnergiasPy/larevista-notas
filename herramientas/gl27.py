import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-27-baja-el-gas-de-garrafa-paraguay-petropar-nande-gas'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.add_patch(Rectangle((0,0),1600,18,fill=False,ec='#DCE3EA',lw=1))
ax.text(80,72,'PARAGUAY · MERCADO Y PRECIOS',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'BAJA EL GAS DE GARRAFA EN PARAGUAY',fontfamily=BB,fontsize=62,color=NV,va='center')
ax.text(80,214,'Desde el viernes 27, el Ñande Gas de Petropar cuesta G. 600 menos por kilo',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))

def card(x,w,k,big,t1,t2,col,fs=86):
    rb(ax,x,290,w,262,SO,10); ax.add_patch(Rectangle((x,290),8,262,color=col))
    ax.text(x+40,340,k,fontfamily=B,fontweight='bold',fontsize=20,color=MU,va='center')
    ax.text(x+40,424,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    ax.text(x+40,498,t1,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
    ax.text(x+40,530,t2,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,450,'POR KILO','G. 600','menos en el gas de uso','doméstico de Petropar',GR)
card(570,450,'POR GARRAFA DE 10 KG','G. 6.000','lo que deja de pagar','una familia por recarga',GR)
card(1060,460,'NAFTAS Y DIÉSEL','SIN CAMBIOS','el anuncio no los alcanza:','habría novedades el lunes o martes',MU,fs=70)

# franja: donde pega
rb(ax,80,590,1440,212,NV,10)
ax.text(120,640,'CÓMO SE REPARTE EL GLP EN PARAGUAY (ENERO A SEPTIEMBRE)',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
for i,(seg,val,off,det) in enumerate([('GARRAFAS','30.275',172,'el canal que baja de precio'),
                                      ('ESTACIONES DE SERVICIO','18.823',168,'autogas: cayó 11,3 % en un año'),
                                      ('INDUSTRIAS','11.222',158,'el único segmento que crece')]):
    x=120+i*470
    ax.text(x,694,seg,fontfamily=B,fontweight='bold',fontsize=18,color='#9FB3C8',va='center')
    ax.text(x,742,val,fontfamily=BB,fontsize=50,color='white',va='center')
    ax.text(x+off,748,'toneladas',fontfamily=B,fontweight='semibold',fontsize=20,color='#C9D4DF',va='center')
    ax.text(x,780,det,fontfamily=B,fontweight='semibold',fontsize=17,color='#C9D4DF',va='center')

ax.text(80,856,'99,2 %',fontfamily=BB,fontsize=54,color=RD,va='center')
ax.text(290,856,'del gas licuado que entra a Paraguay viene de la Argentina: el país no produce GLP.',fontfamily=B,fontweight='semibold',fontsize=21,color=NV,va='center')
ax.add_patch(Rectangle((80,890),1440,1,color='#DCE3EA'))
ax.text(80,926,'Datos: anuncio de la Presidencia de la República y registro de ventas de GLP del Ministerio de Industria y Comercio.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('gl27-web.png',facecolor='white'); Image.open('gl27-web.png').convert('RGB').save(R+ID+'-2.jpg',quality=88); plt.close(fig)
import os; print('ok',round(os.path.getsize(R+ID+'-2.jpg')/1024),'KB')
