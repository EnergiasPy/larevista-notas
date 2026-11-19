# Placas web 1600x1067 · Paraguay · Petropar cancela la consultoría de exploración · 19/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-19-hay-petroleo-en-paraguay-petropar-cancela-consultoria-chaco'; R='/home/claude/larevista-notas/img/'
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


# ---------- PLACA 1: los seis bloques ----------
fig,ax=hdr('PARAGUAY · HIDROCARBUROS','SEIS BLOQUES EN EL CHACO Y NINGÚN POZO PERFORADO','Áreas asignadas a Petropar para buscar petróleo y gas, en hectáreas')
bl=[('PALO SANTO',799368,'2016 · en exploración',GR),('PETROPAR II',635066,'2019',NV),('PETROPAR III',1542996,'2020',NV),('PETROPAR IV',800620,'2019',NV),('PETROPAR V',795348,'2019',NV),('PETROPAR VI',1040485,'2020',NV)]
BX=420; BW=820; VMAX=1542996
for i,(n,v,a,col) in enumerate(bl):
    y=282+i*74
    ax.text(80,y+30,n,fontfamily=BB,fontsize=40,color=NV,va='center')
    ax.add_patch(Rectangle((BX,y+6),BW,48,color='#E8EDF2'))
    w=BW*v/VMAX; ax.add_patch(Rectangle((BX,y+6),w,48,color=col))
    ax.text(BX+w+18,y+30,f'{v:,}'.replace(',','.'),fontfamily=BB,fontsize=36,color=col,va='center')
    ax.text(1520,y+30,a,fontfamily=B,fontweight='semibold',fontsize=19,color=MU,va='center',ha='right')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'EN TOTAL: 5,6 MILLONES DE HECTÁREAS · LA RONDA ABIERTA NO FIRMÓ NINGÚN CONTRATO',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: catastro de hidrocarburos del Viceministerio de Minas y Energía (MOPC) y Petropar.','-1.jpg',ysrc=878)

# ---------- PLACA 2: cronologia ----------
fig,ax=hdr('QUÉ PASÓ','DE LA AUTORIZACIÓN A LA CANCELACIÓN, DOS MESES','La consultoría internacional de USD 837.566 para rehacer la Ronda Abierta Petropar')
for i,(t,d2) in enumerate([
  ('2022','Petropar lanza la Ronda Abierta para recibir ofertas de petroleras privadas. No firmó ningún contrato'),
  ('3 DE SEPTIEMBRE DE 2026','Se autoriza la licitación internacional para contratar el estudio: cinco etapas, de 14 a 18 semanas'),
  ('26 DE OCTUBRE DE 2026','La Dirección de Gabinete de la empresa pide dejar sin efecto el llamado'),
  ('2 DE NOVIEMBRE DE 2026','Resolución PR/WW N° 961/26: se cancela por "extinción de la necesidad de la contratación"')]):
    y=296+i*118; rb(ax,80,y,1440,100,SO,10); ax.add_patch(Rectangle((80,y),8,100,color=GR))
    ax.text(120,y+36,t,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.text(122,y+76,d2,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,768,1440,54,NV,10)
ax.text(120,795,'LA RESOLUCIÓN NO EXPLICA QUÉ CAMBIÓ ENTRE UNA FECHA Y LA OTRA',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Petropar, licitación pública internacional ID 485.831.','-2.jpg')
print('ok')
