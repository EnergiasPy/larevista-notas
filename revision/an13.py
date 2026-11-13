import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-13-ande-congela-tarifa-suspende-cortes-ueno'; R='/home/claude/larevista-notas/img/'
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
fig,ax=hdr('PARAGUAY · ELECTRICIDAD','ANDE: TARIFA QUIETA POR UN AÑO Y SIN CORTES','Las medidas anunciadas el 12 de noviembre por la crisis de ueno bank')
card(80,290,450,300,'LA TARIFA','1 AÑO',['sin reajustes, como mínimo,','según anunció la ANDE'],GR)
card(570,290,450,300,'CORTES POR FALTA DE PAGO','31 DE DIC',['Suspendidos hasta esa fecha','para casi todos los clientes'],NV,fs=60)
card(1060,290,460,300,'DEUDAS','24 CUOTAS',['sin intereses ni recargos.','Solo para clientes de','baja tensión'],RD)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'SI PAGASTE Y NO FIGURA',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'Pagos por Wepa o ueno del 2 y 3 de noviembre: reclamá en la web o en la app Mi ANDE, con el comprobante.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(120,754,'Según la ANDE, el costo no lo asume el cliente y un pago comprobado no se vuelve a cobrar.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
foot(fig,ax,'Datos: ANDE y Presidencia de la República, al 12 de noviembre de 2026.','-1.jpg')
fig,ax=hdr('PARAGUAY · ELECTRICIDAD','CÓMO RECLAMAR UN PAGO NO REGISTRADO','Para pagos hechos por Wepa o por ueno bank el 2 y el 3 de noviembre')
steps=[('1','Entrá a la web de la ANDE o a la app Mi ANDE'),('2','Elegí "Reclamos comerciales"'),('3','Marcá la opción "pago no registrado"'),('4','Adjuntá el comprobante de pago')]
for i,(n,t) in enumerate(steps):
    y=285+i*125; rb(ax,80,y,1440,105,SO,10); ax.add_patch(Rectangle((80,y),8,105,color=GR))
    ax.text(140,y+54,n,fontfamily=BB,fontsize=70,color=GR,va='center',ha='center'); ax.text(210,y+54,t,fontfamily=B,fontweight='bold',fontsize=32,color=NV,va='center')
ax.text(80,805,'Mientras se verifica, la factura queda como "reclamada". También se puede reclamar en las oficinas de la ANDE.',fontfamily=B,fontweight='semibold',fontsize=19,color=MU,va='center')
foot(fig,ax,'Datos: ANDE, al 12 de noviembre de 2026.','-2.jpg')
print('ok')
