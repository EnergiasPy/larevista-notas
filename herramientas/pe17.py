import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-16-ande-licita-640-mw-chaco-solar-baterias'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
ID='2026-11-17-peru-grifos-inventario-diario-osinergmin-sunat'; R='/home/claude/larevista-notas/img/'
PE=('#D91023','#FFFFFF','#D91023')
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(PE): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
    ax.text(80,72,k,fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
    ax.text(76,148,t,fontfamily=BB,fontsize=58,color=NV,va='center')
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

fig,ax=hdr('REGIÓN · PERÚ','EL GRIFO QUE NO DECLARA NO PUEDE COMPRAR','Lo que ya rige en Perú y lo que empieza en febrero de 2027')
card(80,290,700,300,'DESDE MAYO · OSINERGMIN','DIARIO',['La estación carga su inventario','todos los días en la plataforma'],RD,fs=84)
card(820,290,700,300,'DESDE FEBRERO · SUNAT','CADA MOVIMIENTO',['Registro diario de operaciones','y de pérdidas y derrames'],NV,fs=60)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'SIN DECLARACIÓN NO HAY COMPRA',fontfamily=BB,fontsize=38,color='#6DBB78',va='center')
ax.text(120,730,'El grifo que no reporta queda inhabilitado para adquirir combustible en las plantas de venta.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
foot(fig,ax,'Datos: Resolución de Consejo Directivo N° 60-2026-OS/CD de Osinergmin y Resolución de Superintendencia N° 000170-2026 de la SUNAT.','-1.jpg')

fig,ax=hdr('CÓMO SE LLEGÓ ACÁ','DE LA EMERGENCIA DEL GAS AL CONTROL DIARIO','La secuencia regulatoria peruana de este año')
for i,(t,d2) in enumerate([('5 DE MARZO','Decreto Supremo N° 002-2026-EM: emergencia del suministro de gas natural por catorce días'),('MAYO','Osinergmin obliga a declarar el inventario todos los días en su plataforma virtual'),('AGOSTO','La SUNAT posterga su régimen para hidrocarburos y da plazo hasta febrero'),('1 DE FEBRERO DE 2027','Arranca el registro diario de operaciones; el primer período a declarar es febrero')]):
    y=296+i*118; rb(ax,80,y,1440,100,SO,10); ax.add_patch(Rectangle((80,y),8,100,color=GR))
    ax.text(120,y+36,t,fontfamily=BB,fontsize=40,color=NV,va='center')
    ax.text(122,y+76,d2,fontfamily=B,fontweight='semibold',fontsize=22,color=MU,va='center')
ax.text(80,800,'El inventario inicial de cada operador se calcula con las compras e importaciones hasta el 31 de enero.',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
foot(fig,ax,'Datos: normas publicadas por el Gobierno del Perú, Osinergmin y la SUNAT durante 2026.','-2.jpg')
print('ok')
