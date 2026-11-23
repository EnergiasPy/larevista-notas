# Placas web 1600x1067 · Paraguay · petróleo y dólar · 23/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-23-va-a-bajar-combustible-diciembre-petroleo-dolar'; R='/home/claude/larevista-notas/img/'
BR=('#D52B1E','#FFFFFF','#0038A8')
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








fig,ax=hdr('MERCADO Y PRECIOS · PARAGUAY','EL PETRÓLEO BAJÓ, PERO EL DÓLAR VOLVIÓ A SUBIR','Costo de un barril de Brent medido en guaraníes, en tres momentos')
D=[('FIN DE OCTUBRE',670,'Brent a USD 117,64 · dólar a G. 5.700',NV),('11 DE NOVIEMBRE',575,'Brent a USD 92,76 · dólar a G. 6.200',GR),('20 DE NOVIEMBRE',592,'Brent a USD 92,57 · dólar a G. 6.390',RD)]
X0=440; BW=1000; VM=670
for i,(n,v,sub,col) in enumerate(D):
    y=290+i*150
    ax.text(80,y+34,n,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.add_patch(Rectangle((X0,y),BW,70,color='#E8EDF2')); ax.add_patch(Rectangle((X0,y),BW*v/VM,70,color=col))
    num(fig,ax,X0+24,y+36,f'G. {v}.000','por barril',50,'white',ufs=26)
    ax.text(X0,y+98,sub,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,752,1440,62,NV,10)
ax.text(120,783,'EL PETRÓLEO BAJÓ 21 %; EL BARRIL EN GUARANÍES, CERCA DE 12 %',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Cálculo propio y aproximado con el precio del Brent y la cotización del dólar del Banco Central del Paraguay.','-1.jpg',ysrc=888)
print('ok')
