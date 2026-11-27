# Placa web 1600x1067 · Paraguay · restricciones Ruta 2 por Caacupe · 27/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-27-restricciones-ruta-2-caacupe-camiones-combustible'; R='/home/claude/larevista-notas/img/'
BR=('#D52B1E','#FFFFFF','#0038A8')   # bandera de Paraguay
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(BR): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
    ax.text(80,72,k,fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
    ax.text(76,148,t,fontfamily=BB,fontsize=58,color=NV,va='center')
    ax.text(80,214,b,fontfamily=B,fontsize=23,color=MU,va='center')
    ax.add_patch(Rectangle((80,240),80,5,color=RD))
    return fig,ax
def foot(fig,ax,src,name,ysrc=894):
    ax.add_patch(Rectangle((80,ysrc-42),1440,1,color='#DCE3EA'))
    ax.text(80,ysrc,src,fontfamily=B,fontsize=18,color=MU,va='center')
    ax.add_patch(Rectangle((0,967),1600,100,color=NV))
    ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
    ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
    fig.savefig('/tmp/w.png',facecolor='white'); Image.open('/tmp/w.png').convert('RGB').save(R+ID+name,quality=88); plt.close(fig)

def num(fig,ax,x,y,big,uni,fs,col,ufs=None,dy=8,pre=None):
    if pre:
        p=ax.text(x,y+dy,pre,fontfamily=B,fontweight='bold',fontsize=int(fs*0.62),color=col,va='center')
        fig.canvas.draw(); bb=p.get_window_extent(); x=ax.transData.inverted().transform((bb.x1,0))[0]+10
    t=ax.text(x,y,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    fig.canvas.draw(); bb=t.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
    ax.text(x2+14,y+dy,uni,fontfamily=B,fontweight='bold',fontsize=ufs or int(fs*0.5),color=col,va='center')

fig,ax=hdr('PARAGUAY · RUTA PY02','CAACUPÉ: 70 HORAS SIN CAMIONES DE COMBUSTIBLE','La Resolución 1756 del MOPC saca los pesados de la Ruta 2 en el fin de semana de mayor demanda')
tiles=[('70','horas','Del sábado 5 a las 12:00 al martes 8 a las 10:00',RD,None),
       ('16,5','toneladas','Desde ese peso, el camión no circula por el tramo',NV,None),
       ('15','al km 86,5','De San Lorenzo a Itacurubí de la Cordillera',NV,'km'),
       ('3','millones','Peregrinos previstos para Caacupé 2026',GR,None)]
for i,(big,uni,sub,col,pre) in enumerate(tiles):
    x=80+(i%2)*735; y=290+(i//2)*222
    rb(ax,x,y,705,200,SO,10); ax.add_patch(Rectangle((x,y),8,200,color=col))
    num(fig,ax,x+40,y+82,big,uni,86,col,ufs=36,dy=10,pre=pre)
    ax.text(x+42,y+158,sub,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'LA CARGA DEL FIN DE SEMANA TIENE QUE ESTAR EN EL TANQUE ANTES DEL SÁBADO',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Resolución N° 1756 del MOPC, del 24 de noviembre de 2026, y Operativo Caacupé 2026.','-1.jpg',ysrc=878)
print('ok placa web')
