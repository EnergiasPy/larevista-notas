# Placas web 1600x1067 · Brasil · estaciones de biometano para camiones (Ultragaz) · 19/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-19-brasil-estaciones-biometano-camiones-ultragaz'; R='/home/claude/larevista-notas/img/'
BR=('#009C3B','#FFDF00','#002776')
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

# ---------- PLACA 1: la estacion en numeros ----------
fig,ax=hdr('REGIÓN · BRASIL','UNA ESTACIÓN DE BIOMETANO PARA CAMIONES, EN NÚMEROS','Cada una de las dos unidades que Ultragaz abrió sobre la Rodovia dos Bandeirantes, en São Paulo')
tiles=[('R$ 4 MILLONES','','Inversión por estación: cerca de USD 690.000',GR),
       ('24.000','m³ por día','Biometano que puede despachar cada unidad',NV),
       ('+200','camiones por día','Capacidad de atención de cada estación',NV),
       ('8 A 12','minutos','Lo que lleva llenar un camión pesado',RD)]
for i,(big,uni,sub,col) in enumerate(tiles):
    x=80+(i%2)*735; y=290+(i//2)*222
    rb(ax,x,y,705,200,SO,10); ax.add_patch(Rectangle((x,y),8,200,color=col))
    t=ax.text(x+40,y+82,big,fontfamily=BB,fontsize=86,color=col,va='center')
    if uni:
        fig.canvas.draw(); bb=t.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
        ax.text(x2+16,y+92,uni,fontfamily=B,fontweight='bold',fontsize=34,color=col,va='center')
    ax.text(x+42,y+158,sub,fontfamily=B,fontweight='semibold',fontsize=23,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'EN BRASIL HAY 2.500 CAMIONES A GAS Y MÁS DE DOS MILLONES A DIÉSEL',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Ultragaz. Conversión a dólares al tipo de cambio de la semana.','-1.jpg',ysrc=878)

# ---------- PLACA 2: el orden del negocio ----------
fig,ax=hdr('CÓMO SE ARMÓ EL NEGOCIO','PRIMERO EL CLIENTE, DESPUÉS LA RUTA','Los pasos de Ultragaz antes de abrir una estación de biometano al público')
for i,(t,d2) in enumerate([
  ('1 · SURTIDORES DENTRO DE LAS EMPRESAS','Unos 20 clientes con biometano, seis con estación propia: más de 300 camiones abastecidos por día'),
  ('2 · UNA FLOTA CON CONTRATO','Acuerdo con la transportista Transjordano para 100 vehículos en la ruta Santos–Ribeirão Preto'),
  ('3 · LAS DOS PRIMERAS ESTACIONES EN RUTA','Kilómetros 58 y 62 de la Rodovia dos Bandeirantes; hasta fin de año, solo para clientes con contrato'),
  ('4 · ABIERTAS A TODOS, EN 2027','Venta a cualquier transportista desde comienzos de año; la próxima estación iría sobre la BR-101')]):
    y=296+i*118; rb(ax,80,y,1440,100,SO,10); ax.add_patch(Rectangle((80,y),8,100,color=GR))
    ax.text(120,y+36,t,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.text(122,y+76,d2,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,768,1440,54,NV,10)
ax.text(120,795,'LA META: UNAS 20 ESTACIONES SOBRE LOS CORREDORES DE CARGA, SIN CRONOGRAMA DEFINIDO',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Ultragaz.','-2.jpg')
print('ok')
