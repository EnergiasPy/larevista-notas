# Placas web 1600x1067 · Paraguay · Paraguay · cliente eléctrico · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-21-media-hora-para-cargar-estaciones-cliente-electrico'; R='/home/claude/larevista-notas/img/'
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






# ---------- PLACA 1: tiempos
fig,ax=hdr('ELECTROMOVILIDAD · PARAGUAY','CUÁNTO TIEMPO TIENE LA TIENDA','Tiempo mínimo para sumar 30 kWh (de 30 % a 80 % en una batería de 60 kWh), según el cargador')
T=[('150','kW · carga rápida',12,'12','minutos',GR),('60','kW · carga rápida',30,'30','minutos',NV),('22','kW · corriente alterna',82,'1 H 22','minutos',RD)]
for i,(p,u,m,txt,un,col) in enumerate(T):
    y=285+i*148
    num(fig,ax,80,y+48,p,u,66,NV,ufs=24,dy=10)
    ax.add_patch(Rectangle((560,y+6),960,84,color='#E8EDF2'))
    w=960*m/82; ax.add_patch(Rectangle((560,y+6),w,84,color=col))
    if i==2:
        t1=ax.text(584,y+48,'1',fontfamily=BB,fontsize=56,color='white',va='center'); ax.text(622,y+54,'h',fontfamily=B,fontweight='bold',fontsize=32,color='white',va='center')
        ax.text(664,y+48,'22',fontfamily=BB,fontsize=56,color='white',va='center'); ax.text(734,y+54,'min',fontfamily=B,fontweight='bold',fontsize=32,color='white',va='center')
    elif w>300: num(fig,ax,584,y+48,txt,'min',56,'white',ufs=32)
    else: num(fig,ax,560+w+20,y+48,txt,'min',56,NV,ufs=32)
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'EN LA PRÁCTICA TARDA MÁS: LA POTENCIA BAJA A MEDIDA QUE SE LLENA LA BATERÍA',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Cálculo propio: energía dividida por potencia. Es un mínimo teórico; depende de la potencia que admite cada vehículo.','-1.jpg',ysrc=878)

# ---------- PLACA 2: la cuenta
fig,ax=hdr('LA CUENTA','¿EL CAFÉ AYUDA A PAGAR EL CARGADOR?','Un ejercicio simple para un punto de carga rápida de 150 kW')
tiles=[('G. 265','millones','Presupuesto del punto de carga, con transformador',NV),
       ('G. 30.000','por recarga','30 kWh, con un margen supuesto de G. 1.000',GR),
       ('5','recargas por día','Para recuperar la inversión en cinco años',RD),
       ('+ TIENDA','','El gasto del cliente en la tienda mejora la cuenta',NV)]
for i,(big,uni,sub,col) in enumerate(tiles):
    x=80+(i%2)*735; y=290+(i//2)*222
    rb(ax,x,y,705,200,SO,10); ax.add_patch(Rectangle((x,y),8,200,color=col))
    if uni: num(fig,ax,x+40,y+82,big,uni,86,col,ufs=34,dy=10)
    else: ax.text(x+40,y+82,big,fontfamily=BB,fontsize=86,color=col,va='center')
    ax.text(x+42,y+158,sub,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'ANTES DE CARGOS FIJOS, MANTENIMIENTO, IMPUESTOS Y FINANCIACIÓN',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Presupuesto: proyecto de la Universidad Nacional de Caaguazú. El margen por kWh es un supuesto, no un dato de mercado.','-2.jpg',ysrc=878)
print('ok')
