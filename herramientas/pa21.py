# Placas web 1600x1067 · Paraguay · Paraguay · impuesto al diésel · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-21-cuanto-le-cuesta-al-estado-la-baja-del-diesel'; R='/home/claude/larevista-notas/img/'
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





# ---------- PLACA 1
fig,ax=hdr('MERCADO Y PRECIOS · PARAGUAY','EL ESTADO DEJA DE COBRAR US$ 9,5 MILLONES','Impuesto selectivo al diésel: cuánto cae por litro con la rebaja de G. 300 en el surtidor')
for i,(n,v,col,txt) in enumerate([('ANTES',680,NV,'G. 680 por litro'),('DESPUÉS',340,GR,'G. 340 por litro')]):
    y=290+i*150
    ax.text(80,y+30,n,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.add_patch(Rectangle((380,y+6),1000,84,color='#E8EDF2'))
    w=1000*v/680; ax.add_patch(Rectangle((380,y+6),w,84,color=col))
    ax.text(400,y+48,txt,fontfamily=BB,fontsize=50,color='white',va='center')
ax.text(80,640,'Base imponible del diésel tipo III: de G. 3.777,78 a G. 1.888,89 por litro. La tasa sigue en 18 %.',fontfamily=B,fontweight='semibold',fontsize=22,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'US$ 9,5 MILLONES, UNOS G. 59.500 MILLONES AL CAMBIO DE G. 6.260',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Decreto 7.229 y declaraciones del director de la DNIT. Monto de renuncia fiscal confirmado por la DNIT.','-1.jpg',ysrc=878)

# ---------- PLACA 2
fig,ax=hdr('EL SURTIDOR','LOS G. 300 LLEGAN AL CARTEL','Diésel común, precio por litro en guaraníes, con IVA incluido')
rows=[('ANTES · SHELL',9285,'G. 9.285',NV),('AHORA · SHELL Y PETROPAR',8985,'G. 8.985',GR)]
for j,(lab,v,txt,col) in enumerate(rows):
    y=290+j*120
    ax.text(80,y+20,lab,fontfamily=B,fontweight='bold',fontsize=24,color=MU,va='center')
    ax.add_patch(Rectangle((80,y+40),1440,72,color='#E8EDF2'))
    ax.add_patch(Rectangle((80,y+40),1440*v/9285,72,color=col))
    ax.text(100,y+76,txt,fontfamily=BB,fontsize=50,color='white',va='center')
ax.text(80,560,'Rango del diésel común en el mercado: entre G. 8.940 y G. 8.990 por litro.',fontfamily=B,fontweight='semibold',fontsize=24,color=NV,va='center')
ax.text(80,612,'Las naftas no entran en la rebaja del impuesto; algunos emblemas bajaron también precios de nafta.',fontfamily=B,fontsize=22,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'DE LOS G. 340 DE IMPUESTO, AL SURTIDOR LLEGAN G. 300',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Precios de cartel del 16/11 al 20/11. La diferencia de G. 40 la atribuyen las empresas a gastos operativos y administrativos.','-2.jpg',ysrc=878)
print('ok')
