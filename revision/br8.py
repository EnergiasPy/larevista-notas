import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import numpy as np
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-08-brasil-vencen-alivios-gasolina-diesel'; R='/home/claude/larevista-notas/img/'
BRF=['#009C3B','#FFDF00','#002776']
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(BRF): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'BRASIL · MERCADO Y PRECIOS',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'NOVIEMBRE DE VENCIMIENTOS EN EL SURTIDOR',fontfamily=BB,fontsize=64,color=NV,va='center')
ax.text(80,214,'Los alivios a la gasolina y al diésel tienen fecha. Sin prórroga, el precio puede subir',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
cal=[('LUN 9 NOV','Gasolina','Vence la exención de impuestos: R$ 0,89 por litro de gasolina A',RD),
     ('12 NOV','Diésel importado','Termina el refuerzo de R$ 1,40 por litro a los importadores',NV),
     ('26 NOV','Diésel','Vence la subvención de R$ 2,12 por litro a productores e importadores',NV),
     ('30 NOV','Paraguay','Petropar termina el congelamiento del diésel y revisa precios',GR)]
for k,(d,t,s,c) in enumerate(cal):
    y=290+k*120; rb(ax,80,y,1000,104,SO,8); ax.add_patch(Rectangle((80,y),10,104,color=c))
    ax.text(110,y+52,d,fontfamily=BB,fontsize=40,color=c,va='center')
    ax.text(330,y+34,t,fontfamily=B,fontweight='bold',fontsize=23,color=NV,va='center')
    ax.text(330,y+70,s,fontfamily=B,fontweight='semibold',fontsize=17,color=MU,va='center')
rb(ax,1110,290,420,464,NV,10)
ax.text(1140,340,'GASOLINA COMÚN',fontfamily=BB,fontsize=32,color='#AFC0D0',va='center')
ax.text(1140,410,'R$ 6,48',fontfamily=BB,fontsize=74,color='#6DBB78',va='center')
ax.text(1140,460,'precio medio por litro (ANP,',fontfamily=B,fontsize=19,color='white',va='center')
ax.text(1140,488,'25 al 31 de octubre)',fontfamily=B,fontsize=19,color='white',va='center')
ax.add_patch(Rectangle((1140,520),360,1,color='#3A4B5C'))
ax.text(1140,565,'AYUDA AL DIÉSEL IMPORTADO',fontfamily=BB,fontsize=28,color='#AFC0D0',va='center')
ax.text(1140,630,'R$ 3,52',fontfamily=BB,fontsize=74,color='white',va='center')
ax.text(1140,680,'por litro: R$ 2,12 + R$ 1,40',fontfamily=B,fontsize=19,color='white',va='center')
ax.text(1140,712,'Costo: R$ 5.200 M cada 30 días',fontfamily=B,fontsize=17,color='#AFC0D0',va='center')
ax.add_patch(Rectangle((80,800),1450,1,color='#DCE3EA'))
ax.text(80,840,'La gasolina común brasileña lleva 32 % de etanol anhidro. El Congreso amplió por 60 días la MP 1.391, base legal de la subvención al diésel.',fontfamily=B,fontweight='semibold',fontsize=18,color=NV,va='center')
ax.text(80,878,'Datos: Ministerio de Hacienda de Brasil, ANP y Decreto 13.134 (al 8/11/2026). Petropar: precio congelado hasta el 30/11.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('br8-web.png',facecolor='white'); Image.open('br8-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88)
plt.close(fig)
# placa IG
exec(open('rentab_carr.py').read().split('# 1 portada')[0].replace("O='/home/claude/out/carr/'","O='/home/claude/out/br8/'").replace('N=8','N=1'))
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · BRASIL')
for i,c in enumerate(BRF): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
for i,(l,c) in enumerate([('BRASIL:',W),('VENCEN LOS',W),('ALIVIOS AL',G),('SURTIDOR',G)]):
    ax.text(66,250+i*125,l,fontfamily=BB,fontsize=112,color=c,va='center')
cards(ax,[('Lunes 9: gasolina','Vence la exención de R$ 0,89 por litro'),('12 y 26 de noviembre: diésel','Vencen las ayudas de R$ 1,40 y R$ 2,12'),('Frontera con Paraguay','Si sube del otro lado, cambia la cuenta')],790,h=125,gap=18)
ax.add_patch(Rectangle((50,1275),80,40,color=BG,zorder=10))
save(fig,ID+'-ig')
print('ok')
