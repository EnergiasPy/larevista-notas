import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-18-ecuador-margen-estacion-congelado'; R='/home/claude/larevista-notas/img/'
EC=('#FFDD00','#0B4EA2','#ED1C24')
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(EC): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
    ax.text(80,72,k,fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
    ax.text(76,148,t,fontfamily=BB,fontsize=58,color=NV,va='center')
    ax.text(80,214,b,fontfamily=B,fontsize=23,color=MU,va='center')
    ax.add_patch(Rectangle((80,240),80,5,color=RD))
    return fig,ax
def foot(fig,ax,src,name):
    ax.add_patch(Rectangle((80,830),1440,1,color='#DCE3EA'))
    ax.text(80,872,src,fontfamily=B,fontsize=18,color=MU,va='center')
    ax.add_patch(Rectangle((0,967),1600,100,color=NV))
    ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
    ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
    fig.savefig('/tmp/w.png',facecolor='white'); Image.open('/tmp/w.png').convert('RGB').save(R+ID+name,quality=88); plt.close(fig)

# ---------- PLACA 1: comparacion de margenes ----------
fig,ax=hdr('REGIÓN · ECUADOR','DOCE CENTAVOS POR GALÓN, CONGELADOS 23 AÑOS','Margen de comercialización del diésel: lo que le queda a toda la cadena que lo vende')
BX=430; BW=940; VMAX=0.36
for i,(pais,val,col) in enumerate([('ECUADOR',0.12,RD),('PERÚ',0.28,NV),('COLOMBIA',0.33,GR)]):
    y=330+i*150
    ax.text(80,y+40,pais,fontfamily=BB,fontsize=52,color=NV,va='center')
    ax.add_patch(Rectangle((BX,y+6),BW,68,color='#E8EDF2'))
    w=BW*val/VMAX
    ax.add_patch(Rectangle((BX,y+6),w,68,color=col))
    ax.text(BX+w+24,y+40,f'USD {val:.2f}'.replace('.',','),fontfamily=BB,fontsize=50,color=col,va='center')
ax.text(80,762,'El margen ecuatoriano no es la ganancia de la estación:',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
ax.text(80,798,'se reparte entre comercializadoras, estaciones y transportistas.',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
foot(fig,ax,'Datos: Cámara Nacional de Distribuidores de Derivados del Petróleo del Ecuador (Camddepe).','-1.jpg')

# ---------- PLACA 2: cronologia y pedido ----------
fig,ax=hdr('QUÉ PASÓ Y QUÉ PIDEN','UNA MARCA SE VA Y EL GREMIO PIDE 22 CENTAVOS','La secuencia del margen ecuatoriano en los últimos doce meses')
for i,(t,d2) in enumerate([
  ('NOVIEMBRE DE 2025','El Decreto 209 sube el margen de la Extra y la Ecopaís de USD 0,16 a USD 0,19 por galón. El diésel queda afuera'),
  ('JULIO DE 2026','Terpel informa la desinversión de su red de 110 estaciones y tiendas; opera en Ecuador desde 2006'),
  ('SEPTIEMBRE DE 2026','El gremio pide llevar el diésel a USD 0,19 y después los dos combustibles a USD 0,22 por galón'),
  ('6 DE OCTUBRE DE 2026','Plantón en la Plaza Grande de Quito y suspensión de la venta de diésel a crédito al transporte pesado')]):
    y=296+i*118; rb(ax,80,y,1440,100,SO,10); ax.add_patch(Rectangle((80,y),8,100,color=GR))
    ax.text(120,y+36,t,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.text(122,y+76,d2,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,768,1440,54,NV,10)
ax.text(120,795,'700 DE LAS 1.200 ESTACIONES DEL PAÍS TRABAJAN APENAS EN EL PUNTO DE EQUILIBRIO',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.add_patch(Rectangle((80,852),1440,1,color='#DCE3EA'))
ax.text(80,894,'Datos: Camddepe, Decreto Ejecutivo 209 e información de la Organización Terpel a la Superintendencia Financiera de Colombia.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('/tmp/w.png',facecolor='white'); Image.open('/tmp/w.png').convert('RGB').save(R+ID+'-2.jpg',quality=88); plt.close(fig)
print('ok')
