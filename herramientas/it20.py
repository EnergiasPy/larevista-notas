# Placas web 1600x1067 · Paraguay · excedente de Itaipú · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-20-cuando-se-acaba-excedente-itaipu-paraguay-2029'; R='/home/claude/larevista-notas/img/'
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

# ---------- PLACA 1: suministro a la ANDE ----------
fig,ax=hdr('PARAGUAY · ITAIPÚ','PARAGUAY USA CADA VEZ MÁS DE SU MITAD DE ITAIPÚ','Energía que la central le entregó a la ANDE entre enero y octubre de cada año')
BX=330; BW=900; VMAX=24121
for i,(an,v,col) in enumerate([('2025',20753,NV),('2026',24121,GR)]):
    y=300+i*150
    ax.text(80,y+52,an,fontfamily=BB,fontsize=84,color=NV,va='center')
    ax.add_patch(Rectangle((BX,y+6),BW,92,color='#E8EDF2'))
    w=BW*v/VMAX; ax.add_patch(Rectangle((BX,y+6),w,92,color=col))
    num(fig,ax,BX+28,y+52,f'{v:,}'.replace(',','.'),'GWh',64,'white',ufs=34)
ax.text(1260,300+150+52,'+16,23 %',fontfamily=BB,fontsize=70,color=GR,va='center')
ax.text(80,650,'Con ese ritmo, la central calcula que Paraguay usará toda su parte en varios meses de 2029 y 2030.',fontfamily=B,fontweight='bold',fontsize=24,color=NV,va='center')
ax.text(80,690,'Hasta ahora, la fecha que se manejaba era 2034.',fontfamily=B,fontweight='semibold',fontsize=24,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'LA TARIFA DE ITAIPÚ VENCE EL 31 DE DICIEMBRE: FALTAN 38 DÍAS',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Itaipú Binacional, informe de producción y suministro de la Dirección Técnica de la margen derecha.','-1.jpg',ysrc=878)

# ---------- PLACA 2: los dos techos ----------
fig,ax=hdr('LA DISCUSIÓN EN BRASIL','DOS TECHOS PARA EL CONSUMO PARAGUAYO','Cuánta energía de Itaipú se proyecta para la ANDE desde enero de 2027, en megavatios medios')
BX=80; BW=1180; VMAX=7750.8
for i,(n,v,col,sub) in enumerate([('PROPUESTA DE ENBPAR E ITAIPÚ',7000,GR,'Con un método nuevo, que mira once años de historia'),('PEDIDO DE LOS INDUSTRIALES BRASILEÑOS',3875,RD,'La mitad de la garantía física de la central')]):
    y=290+i*215
    ax.text(80,y+22,n,fontfamily=BB,fontsize=40,color=NV,va='center')
    ax.add_patch(Rectangle((BX,y+52),BW,84,color='#E8EDF2'))
    w=BW*v/VMAX; ax.add_patch(Rectangle((BX,y+52),w,84,color=col))
    num(fig,ax,BX+28,y+94,f'{v:,}'.replace(',','.'),'MW medios',60,'white',ufs=32)
    ax.text(80,y+166,sub,fontfamily=B,fontweight='semibold',fontsize=22,color=MU,va='center')
ax.text(1290,290+52+42,'Garantía física',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
ax.text(1290,290+52+72,'de toda la central:',fontfamily=B,fontsize=20,color=MU,va='center')
ax.text(1290,290+52+104,'7.750,8 MW medios',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'EN BRASIL ESTIMAN QUE EL PRECIO DE LA ENERGÍA SUBIRÍA CERCA DE 21 % EN 2027',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: ENBPar, Itaipú Binacional y presentación de Abrace Energia ante la Aneel.','-2.jpg',ysrc=878)
print('ok')
