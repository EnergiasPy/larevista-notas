# Placas web 1600x1067 · Paraguay · Colombia · margen de la estación y pedido de piso · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-20-cuanto-gana-estacion-de-servicio-colombia-margen-minimo'; R='/home/claude/larevista-notas/img/'
BR=('#FCD116','#003893','#CE1126')
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
    t=ax.text(x,y,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    fig.canvas.draw(); bb=t.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
    ax.text(x2+14,y+dy,uni,fontfamily=B,fontweight='bold',fontsize=ufs or int(fs*0.5),color=col,va='center')



# ---------- PLACA 1: el margen y el piso ----------
fig,ax=hdr('REGIÓN · COLOMBIA','CUÁNTO LE QUEDA A UNA ESTACIÓN EN COLOMBIA','Margen por galón de gasolina corriente y de diésel, y el piso que pide el gremio')
BX=80; BW=1100; VMAX=1155.09
for i,(n,v,col,sub) in enumerate([('MARGEN ACTUAL',1155.09,NV,'Unos 35 centavos de dólar por galón: nueve centavos por litro'),('PISO QUE PIDE EL GREMIO: 90 %',1039.58,GR,'Un precio base mínimo, para que el margen no se pierda en el mercado')]):
    y=290+i*215
    ax.text(80,y+22,n,fontfamily=BB,fontsize=40,color=NV,va='center')
    ax.add_patch(Rectangle((BX,y+52),BW,84,color='#E8EDF2'))
    w=BW*v/VMAX; ax.add_patch(Rectangle((BX,y+52),w,84,color=col))
    num(fig,ax,BX+28,y+94,'$ '+(f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.') if i==0 else '1.040'),'por galón',60,'white',ufs=32)
    ax.text(80,y+166,sub,fontfamily=B,fontweight='semibold',fontsize=22,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'EL COSTO LABORAL SE LLEVA CERCA DEL 35 % DE ESE MARGEN',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Somos Uno (Comce y Fendipetróleo Nacional). Valores en pesos colombianos; conversión al tipo de cambio de la semana.','-1.jpg',ysrc=878)

# ---------- PLACA 2: la red ----------
fig,ax=hdr('EL SECTOR EN NÚMEROS','UNA RED DE DUEÑOS CHICOS','Las estaciones de servicio de Colombia, según los datos del gremio')
tiles=[('6.400','estaciones','En manos de 4.300 propietarios',NV),
       ('86 %','','De los dueños tiene una sola estación',GR),
       ('68.035','empleos','En 980 municipios del país',NV),
       ('55.948','galones por mes','Despacho promedio: unos 212.000 litros',RD)]
for i,(big,uni,sub,col) in enumerate(tiles):
    x=80+(i%2)*735; y=290+(i//2)*222
    rb(ax,x,y,705,200,SO,10); ax.add_patch(Rectangle((x,y),8,200,color=col))
    if uni: num(fig,ax,x+40,y+82,big,uni,86,col,ufs=36,dy=10)
    else: ax.text(x+40,y+82,big,fontfamily=BB,fontsize=86,color=col,va='center')
    ax.text(x+42,y+158,sub,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'EL 57 % DE LAS ESTACIONES SON MICRO, PEQUEÑAS O MEDIANAS EMPRESAS',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Somos Uno, Congreso Nacional de Estaciones de Servicio 2026.','-2.jpg',ysrc=878)
print('ok')
