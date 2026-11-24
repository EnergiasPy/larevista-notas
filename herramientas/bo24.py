# Placas web 1600x1067 · Paraguay · Gulf llega a Paraguay · 24/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-24-cuanto-cuesta-el-diesel-en-bolivia-sube-a-bs-20-57'; R='/home/claude/larevista-notas/img/'
BR=('#D52B1E','#F9E300','#007934')
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










fig,ax=hdr('REGIÓN · BOLIVIA','EL DIÉSEL EN BOLIVIA SUBE A BS 20,57 POR LITRO','Precio del litro de diésel, en bolivianos, y desde cuándo rige cada valor')
vals=[(3.72,'3,72','Hasta dic. 2025',MU),(9.80,'9,80','Desde dic. 2025',NV),(17.95,'17,95','Desde el 18 de sep. 2026',NV),(20.57,'20,57','Desde el 24 de nov. 2026',RD)]
base=760; mx=430
for i,(v,t,l,col) in enumerate(vals):
    x=150+i*345; hgt=v/20.57*mx
    rb(ax,x,base-hgt,250,hgt,col,8)
    ax.text(x+125,base-hgt-34,'Bs '+t,fontfamily=B,fontweight='bold',fontsize=40,color=col,ha='center',va='center')
    ax.text(x+125,base+34,l,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,ha='center',va='center')
ax.add_patch(Rectangle((80,base),1440,2,color='#DCE3EA'))
foot(fig,ax,'Datos: Agencia Nacional de Hidrocarburos (ANH) y decretos supremos 5503 y 5716. Bs 20,57 equivale a unos USD 1,75.','-1.jpg',ysrc=878)
