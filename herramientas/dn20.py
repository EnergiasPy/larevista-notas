# Placas web 1600x1067 · Paraguay · licitación de cargadores de Petropar (Res. DNCP 3278/26) · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-20-petropar-cargadores-electricos-estaciones-licitacion-dncp'; R='/home/claude/larevista-notas/img/'
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
    t=ax.text(x,y,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    fig.canvas.draw(); bb=t.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
    ax.text(x2+14,y+dy,uni,fontfamily=B,fontweight='bold',fontsize=ufs or int(fs*0.5),color=col,va='center')


# ---------- PLACA 1: que pide por punto de carga ----------
fig,ax=hdr('PARAGUAY · ELECTROMOVILIDAD','QUÉ PIDE PETROPAR PARA CADA PUNTO DE CARGA','Licitación de cargadores para vehículos eléctricos en estaciones de servicio')
tiles=[('90','kW','Cargador rápido, con tres salidas de carga',GR),
       ('150','kVA','Transformador propio y puesto de media tensión',NV),
       ('45','días hábiles','Plazo de entrega, según la corrección anunciada',NV),
       ('G. 13.994','millones','Monto estimado: unos USD 2,2 millones',RD)]
for i,(big,uni,sub,col) in enumerate(tiles):
    x=80+(i%2)*735; y=290+(i//2)*222
    rb(ax,x,y,705,200,SO,10); ax.add_patch(Rectangle((x,y),8,200,color=col))
    num(fig,ax,x+40,y+82,big,uni,86,col,ufs=36,dy=10)
    ax.text(x+42,y+158,sub,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'LA LICITACIÓN ESTÁ SUSPENDIDA HASTA QUE PETROPAR PUBLIQUE LA ADENDA',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Resolución DNCP N° 3278/26 y pliego de la licitación ID 490.579.','-1.jpg',ysrc=878)

# ---------- PLACA 2: que cambia y que no ----------
fig,ax=hdr('QUÉ RESOLVIÓ LA DNCP','QUÉ CAMBIA Y QUÉ NO EN LA LICITACIÓN','Resultado de la protesta contra el pliego de los cargadores de Petropar')
for i,(t,d2,col) in enumerate([
  ('CAMBIA · LA POTENCIA','Se admitirán equipos de 90 kW o más, no solo de 90 kW exactos',GR),
  ('CAMBIA · MUESTRAS Y VISITA A FÁBRICA','Petropar debe revisar ese requisito y fijar reglas claras',GR),
  ('SE MANTIENE · TRES SALIDAS EN UN MISMO EQUIPO','Se rechazó el pedido de admitir la salida de corriente alterna en un equipo separado',NV),
  ('RECHAZADO · EL PLANTEO DE BARRERA DE MERCADO','La DNCP consideró que ese punto no estaba suficientemente fundamentado',RD)]):
    y=296+i*118; rb(ax,80,y,1440,100,SO,10); ax.add_patch(Rectangle((80,y),8,100,color=col))
    ax.text(120,y+36,t,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.text(122,y+76,d2,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,768,1440,54,NV,10)
ax.text(120,795,'PETROPAR NEGÓ HABER ARMADO EL PLIEGO PARA FAVORECER A UN FABRICANTE',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Resolución DNCP N° 3278/26, del 13 de noviembre de 2026.','-2.jpg')
print('ok')
