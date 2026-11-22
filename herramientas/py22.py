# Placas web 1600x1067 · Paraguay · Paraguay · litros por estación · 22/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-22-cuantos-litros-vende-estacion-de-servicio-paraguay'; R='/home/claude/larevista-notas/img/'
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








D=[('PETROPAR',215,302),('SAN ISIDRO (ENERGY)',156,109),('SHELL',139,363),('PETROBRAS',129,245),('PUMA',105,180),('PETROMAX',95,109),('PETROSUR',94,160),('PETROCHACO',86,147),('COPETROL',68,387)]
fig,ax=hdr('DATOS DEL SECTOR · PARAGUAY','CUÁNTOS LITROS VENDE UNA ESTACIÓN EN PARAGUAY','Miles de litros de naftas y gasoil por estación en octubre de 2026, por emblema')
X0=430; BW=820; VM=215; y0=278; step=62
for i,(n,v,e) in enumerate(D):
    y=y0+i*step
    ax.text(80,y+22,n,fontfamily=BB,fontsize=31,color=NV,va='center')
    col=GR if i==0 else NV
    ax.add_patch(Rectangle((X0,y),BW,44,color='#E8EDF2')); ax.add_patch(Rectangle((X0,y),BW*v/VM,44,color=col))
    ax.text(X0+16,y+23,f'{v}.000',fontfamily=BB,fontsize=31,color='white',va='center',ha='left',zorder=5)
    ax.text(X0+BW+24,y+22,f'{e} estaciones',fontfamily=B,fontweight='semibold',fontsize=20,color=MU,va='center')
xa=X0+BW*104/VM
ax.plot([xa,xa],[y0-12,y0+len(D)*step-12],color=RD,lw=3,ls=(0,(4,3)))
rb(ax,80,838,1440,0,NV,0)
ax.text(80,858,'Promedio del país: 104.000 litros por estación (línea roja)',fontfamily=B,fontweight='bold',fontsize=23,color=RD,va='center')
foot(fig,ax,'Cuenta propia con datos del MIC: ventas de octubre por empresa y estaciones habilitadas al 17 de noviembre. Valores aproximados.','-1.jpg',ysrc=920)
print('ok')
