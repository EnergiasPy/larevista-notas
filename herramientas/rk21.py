# Placas web 1600x1067 · Paraguay · Paraguay · ranking de ventas de octubre · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-21-ranking-ventas-combustibles-octubre-2026'; R='/home/claude/larevista-notas/img/'
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







E=[('PETROPAR',64.9,'21,6 %','+16,9 %'),('SHELL',50.6,'16,8 %','−8,5 %'),('PETROBRAS',31.7,'10,6 %','−13,7 %'),('COPETROL',26.3,'8,8 %','−15,5 %'),('PUMA',18.9,'6,3 %','−26,4 %'),
   ('SAN ISIDRO',17.0,'5,6 %','−2,2 %'),('PETROSUR',15.1,'5,0 %','−6,6 %'),('ECOP',13.0,'4,3 %','−17,0 %'),('PETROCHACO',12.7,'4,2 %','+4,6 %'),('PETROMAX',10.4,'3,5 %','−27,5 %')]
fig,ax=hdr('DATOS DEL SECTOR · PARAGUAY','QUIÉN VENDIÓ MÁS COMBUSTIBLE EN OCTUBRE','Ventas de naftas y gasoil por emblema, en millones de litros, y variación contra octubre de 2025')
for i,(n,v,sh,yo) in enumerate(E):
    y=268+i*59
    ax.text(80,y+24,f'{i+1}',fontfamily=BB,fontsize=30,color=MU,va='center')
    ax.text(124,y+24,n,fontfamily=BB,fontsize=32,color=NV,va='center')
    ax.add_patch(Rectangle((360,y+2),820,44,color='#E8EDF2'))
    ax.add_patch(Rectangle((360,y+2),820*v/64.9,44,color=GR if i==0 else NV))
    lab=f'{v:.1f}'.replace('.',',')
    if v>20: ax.text(374,y+25,lab,fontfamily=BB,fontsize=32,color='white',va='center')
    else: ax.text(360+820*v/64.9+12,y+25,lab,fontfamily=BB,fontsize=32,color=NV,va='center')
    ax.text(1290,y+25,sh,fontfamily=B,fontweight='bold',fontsize=23,color=NV,va='center',ha='right')
    ax.text(1520,y+25,yo,fontfamily=B,fontweight='bold',fontsize=23,color=GR if yo[0]=='+' else RD,va='center',ha='right')
ax.text(1290,254,'PARTICIPACIÓN',fontfamily=B,fontweight='bold',fontsize=15,color=MU,va='center',ha='right')
ax.text(1520,254,'VS. OCTUBRE 2025',fontfamily=B,fontweight='bold',fontsize=15,color=MU,va='center',ha='right')
foot(fig,ax,'Datos: Ministerio de Industria y Comercio (MIC). Nombres de los emblemas según el registro del MIC. Total del mes: 300,5 millones de litros.','-1.jpg',ysrc=905)

fig,ax=hdr('POR PRODUCTO','EL GASOIL CAYÓ 15 % EN UN MES','Ventas en millones de litros: septiembre y octubre de 2026')
P=[('GASOIL TIPO III',156.7,133.0,'−15,1 %'),('NAFTA DE 90 OCTANOS',108.1,110.6,'+2,3 %'),('NAFTA DE 95 OCTANOS',25.0,24.6,'−1,6 %'),('GASOIL TIPO I',23.9,24.2,'+1,0 %'),('NAFTA DE 85 OCTANOS',8.5,7.7,'−9,1 %')]
for i,(n,a,b,v) in enumerate(P):
    y=272+i*92
    ax.text(80,y+40,n,fontfamily=BB,fontsize=32,color=NV,va='center')
    for j,(val,col) in enumerate([(a,'#9FB3C8'),(b,NV)]):
        yy=y+6+j*36; w=820*val/156.7
        ax.add_patch(Rectangle((420,yy),w,30,color=col))
        ax.text(420+w+12,yy+16,f'{val:.1f}'.replace('.',','),fontfamily=B,fontweight='bold',fontsize=21,color=NV,va='center')
    ax.text(1520,y+40,v,fontfamily=BB,fontsize=44,color=GR if v[0]=='+' else RD,va='center',ha='right')
ax.add_patch(Rectangle((420,742),30,22,color='#9FB3C8')); ax.text(460,754,'Septiembre',fontfamily=B,fontweight='semibold',fontsize=20,color=MU,va='center')
ax.add_patch(Rectangle((620,742),30,22,color=NV)); ax.text(660,754,'Octubre',fontfamily=B,fontweight='semibold',fontsize=20,color=MU,va='center')
rb(ax,80,790,1440,62,NV,10)
ax.text(120,821,'TODO EL GASOIL: −12,9 % EN EL MES · TODAS LAS NAFTAS: +1 %',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Ministerio de Industria y Comercio (MIC). Variación de octubre contra septiembre de 2026.','-2.jpg',ysrc=905)
print('ok')
