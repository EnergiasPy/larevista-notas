# Placas web 1600x1067 · Paraguay · Bolivia · subsidio a los combustibles y precios · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-20-cuanto-cuesta-gasolina-bolivia-subsidio-9000-millones'; R='/home/claude/larevista-notas/img/'
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




# ---------- PLACA 1: la escalera de decretos ----------
fig,ax=hdr('REGIÓN · BOLIVIA','EL TECHO DEL SUBSIDIO SE MULTIPLICÓ POR NUEVE','Dinero público que el Tesoro puede transferir a YPFB en 2026, en millones de bolivianos')
D=[('9 DE JULIO','Decreto 5652',1000),('27 DE AGOSTO','Decreto 5683',2000),('SEPTIEMBRE','Decreto 5705',6000),('19 DE NOVIEMBRE','Decreto 5778',9000)]
BX=380; BW=1000
for i,(f,d,v) in enumerate(D):
    y=282+i*112
    ax.text(80,y+30,f,fontfamily=BB,fontsize=34,color=NV,va='center')
    ax.text(80,y+68,d,fontfamily=B,fontweight='semibold',fontsize=20,color=MU,va='center')
    ax.add_patch(Rectangle((BX,y+6),BW,84,color='#E8EDF2'))
    w=BW*v/9000; col=RD if i==3 else NV
    ax.add_patch(Rectangle((BX,y+6),w,84,color=col))
    lab='Bs '+f'{v:,}'.replace(',','.')
    if w>330: num(fig,ax,BX+24,y+48,lab,'millones',54,'white',ufs=28)
    else: num(fig,ax,BX+w+20,y+48,lab,'millones',54,NV,ufs=28)
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'EL NUEVO TECHO EQUIVALE A UNOS USD 766 MILLONES AL TIPO DE CAMBIO OFICIAL',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: decretos supremos 5652, 5683, 5705 y 5778 de Bolivia. Son autorizaciones "de hasta" ese monto. Dólar oficial: Bs 11,75.','-1.jpg',ysrc=878)

# ---------- PLACA 2: precios Bolivia vs Paraguay ----------
fig,ax=hdr('LA FRONTERA DEL CHACO','DOS BRECHAS QUE VAN EN SENTIDO CONTRARIO','Precio por litro en Bolivia y en Paraguay, llevado a guaraníes')
G2=[('GASOLINA / NAFTA',[('Bolivia · gasolina especial (Bs 6,96)',3708,'G. 3.700',GR),('Paraguay · nafta más económica',6690,'G. 6.690',NV)]),
    ('DIÉSEL',[('Bolivia · diésel (Bs 17,95)',9563,'G. 9.560',RD),('Paraguay · diésel común',8985,'G. 8.985',NV)])]
BX=80; BW=1440; VM=10400
for i,(t,rows) in enumerate(G2):
    y0=276+i*236
    ax.text(80,y0+18,t,fontfamily=BB,fontsize=38,color=NV,va='center')
    for j,(lab,v,txt,col) in enumerate(rows):
        y=y0+46+j*88
        ax.add_patch(Rectangle((BX,y),BW,72,color='#E8EDF2'))
        w=BW*v/VM; ax.add_patch(Rectangle((BX,y),w,72,color=col))
        ax.text(BX+22,y+37,txt,fontfamily=BB,fontsize=50,color='white',va='center')
        if w>760: ax.text(BX+250,y+38,lab,fontfamily=B,fontweight='semibold',fontsize=23,color='white',va='center')
        else: ax.text(BX+w+22,y+38,lab,fontfamily=B,fontweight='semibold',fontsize=23,color=NV,va='center')
rb(ax,80,752,1440,62,NV,10)
ax.text(120,783,'LA GASOLINA BOLIVIANA CUESTA CASI LA MITAD; EL DIÉSEL, MÁS QUE EN PARAGUAY',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Precios con impuestos. Bolivia: precios vigentes al 20/11, al dólar oficial (Bs 11,75) y G. 6.260 por dólar. Paraguay: precios de cartel.','-2.jpg',ysrc=886)
print('ok')
