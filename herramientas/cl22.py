# Placas web 1600x1067 · Región · Chile · margen de comercialización · 22/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-22-cuanto-gana-estacion-de-servicio-chile-margen'; R='/home/claude/larevista-notas/img/'
BR=('#0039A6','#FFFFFF','#D52B1E')
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



def num(fig,ax,x,y,big,uni,fs,col,ufs=None,dy=8):
    if big.startswith('Bs '):
        p=ax.text(x,y+dy,'Bs',fontfamily=B,fontweight='bold',fontsize=int(fs*0.62),color=col,va='center')
        fig.canvas.draw(); bb=p.get_window_extent(); x=ax.transData.inverted().transform((bb.x1,0))[0]+10; big=big[3:]
    t=ax.text(x,y,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    fig.canvas.draw(); bb=t.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
    ax.text(x2+14,y+dy,uni,fontfamily=B,fontweight='bold',fontsize=ufs or int(fs*0.5),color=col,va='center')








D=[('METROPOLITANA',75,94),('VALPARAÍSO',98,118),('MAULE',110,95),('MAGALLANES',127,126),('BIOBÍO',139,124),("O'HIGGINS",141,137)]
fig,ax=hdr('REGIÓN · CHILE','CUÁNTO GANA UNA ESTACIÓN DE SERVICIO EN CHILE','Margen bruto de comercialización por región, en pesos chilenos por litro')
X0=400; BW=900; VM=141; y0=285; step=92
ax.add_patch(Rectangle((X0,258),26,16,color=NV)); ax.text(X0+36,266,'Gasolina 93',fontfamily=B,fontweight='semibold',fontsize=19,color=MU,va='center')
ax.add_patch(Rectangle((X0+190,258),26,16,color=GR)); ax.text(X0+226,266,'Diésel',fontfamily=B,fontweight='semibold',fontsize=19,color=MU,va='center')
for i,(n,g,d) in enumerate(D):
    y=y0+i*step
    ax.text(80,y+38,n,fontfamily=BB,fontsize=36,color=NV,va='center')
    for j,(v,col) in enumerate([(g,NV),(d,GR)]):
        yy=y+4+j*36
        ax.add_patch(Rectangle((X0,yy),BW,32,color='#E8EDF2')); ax.add_patch(Rectangle((X0,yy),BW*v/VM,32,color=col))
        ax.text(X0+14,yy+17,f'$ {v}',fontfamily=BB,fontsize=26,color='white',va='center')
rb(ax,80,848,1440,0,NV,0)
ax.text(80,858,'El margen incluye a la distribuidora y a la estación. Santiago, el mercado más grande, es el de menor margen.',fontfamily=B,fontweight='bold',fontsize=21,color=RD,va='center')
foot(fig,ax,'Datos: Comisión Nacional de Energía de Chile (CNE). Última información publicada: agosto de 2024.','-1.jpg',ysrc=920)
print('ok')
