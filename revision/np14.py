import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-14-nuevos-precios-diesel-nafta-petropar-privados'; R='/home/claude/larevista-notas/img/'
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
fig,ax=hdr('PARAGUAY · PRECIOS','LOS NUEVOS PRECIOS DE PETROPAR','Por litro, desde el viernes 13 de noviembre. Todos bajaron G. 300')
rows=[('DIÉSEL PORÃ','9.285','8.985'),('NAFTA KAPE · 88','6.990','6.690'),('NAFTA OIKOITE · 93','7.490','7.190'),('NAFTA ARATIRI · 97','8.990','8.690')]
ax.text(760,288,'ANTES',fontfamily=B,fontweight='bold',fontsize=20,color=MU,va='center',ha='center'); ax.text(1080,288,'AHORA',fontfamily=B,fontweight='bold',fontsize=20,color=GR,va='center',ha='center'); ax.text(1380,288,'BAJA',fontfamily=B,fontweight='bold',fontsize=20,color=RD,va='center',ha='center')
for i,(p,a1,b1) in enumerate(rows):
    y=318+i*112; rb(ax,80,y,1440,96,SO,10); ax.add_patch(Rectangle((80,y),8,96,color=GR if i else NV))
    ax.text(120,y+48,p,fontfamily=BB,fontsize=44,color=NV,va='center')
    ax.text(760,y+48,'G. '+a1,fontfamily=B,fontweight='semibold',fontsize=30,color=MU,va='center',ha='center')
    ax.plot([680,840],[y+50,y+46],color=MU,lw=2)
    ax.text(1080,y+48,'G. '+b1,fontfamily=BB,fontsize=56,color=GR,va='center',ha='center')
    ax.text(1380,y+48,'−G. 300',fontfamily=BB,fontsize=44,color=RD,va='center',ha='center')
foot(fig,ax,'Datos: Petropar, 13 de noviembre de 2026. Precio anterior calculado con la baja de G. 300 anunciada. Diésel Mbarete: G. 11.395.','-1.jpg')
fig,ax=hdr('PARAGUAY · DIÉSEL','DE DÓNDE SALEN LOS G. 300','Cómo se traslada el recorte del impuesto selectivo al consumo (ISC) en los emblemas privados')
for i,(big,t,l,c) in enumerate([('G. 340','POR LITRO',['equivale el recorte del','50 % del ISC al diésel'],NV),('G. 300','AL SURTIDOR',['es la baja que trasladan','Petropar y los privados'],GR),('G. 40','PARA COSTOS',['quedan para costos','operativos y administrativos'],RD)]):
    x=80+i*490; rb(ax,x,300,460,330,SO,10); ax.add_patch(Rectangle((x,300),8,330,color=c))
    ax.text(x+40,350,t,fontfamily=B,fontweight='bold',fontsize=22,color=MU,va='center')
    ax.text(x+40,440,big,fontfamily=BB,fontsize=96,color=c,va='center')
    for j,ln in enumerate(l): ax.text(x+40,540+j*36,ln,fontfamily=B,fontweight='semibold',fontsize=22,color=NV,va='center')
rb(ax,80,670,1440,120,NV,10)
ax.text(120,710,'HASTA EL 31 DE DICIEMBRE',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,752,'Si el decreto no se prorroga, en enero el impuesto vuelve a su nivel normal y el diésel sube de nuevo.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
foot(fig,ax,'Datos: decreto del Poder Ejecutivo, Petropar y representantes de los emblemas privados, 13 de noviembre de 2026.','-2.jpg')
print('ok')
