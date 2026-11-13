import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-13-diesel-isc-50-decreto-petropar-baja'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
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
fig,ax=hdr('PARAGUAY · COMBUSTIBLES','DIÉSEL: LA MITAD DE IMPUESTO HASTA FIN DE AÑO','Lo que anunció el Gobierno el viernes 13 de noviembre')
card(80,290,450,300,'IMPUESTO SELECTIVO (ISC)','−50 %',['al diésel, por decreto del','presidente Pedro Alliana'],GR)
card(570,290,450,300,'VIGENCIA','13/11 AL 31/12',['desde este viernes hasta','fin de año'],NV,fs=56)
card(1060,290,460,300,'PRECIO','BAJA',['Petropar anuncia nuevos','valores y los privados','acompañan la medida'],RD)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'ANTES DEL ANUNCIO',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'Diésel común: G. 9.285 por litro en Petropar y alrededor de G. 9.490 en la mayoría de los emblemas privados.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(120,754,'Los nuevos precios por emblema se conocerán a medida que cada distribuidora los comunique.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
foot(fig,ax,'Datos: conferencia de prensa en Palacio de Gobierno (MIC y Petropar), 13 de noviembre de 2026; precios previos de Petropar y emblemas.','-2.jpg')
print('ok')
