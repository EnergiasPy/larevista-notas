import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'; GL='#8CC889'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-08-petropar-denuncia-ueno-reintegros'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(['#D52B1E','#FFFFFF','#0038A8']): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'COMBUSTIBLES Y EESS · CASO UENO BANK',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'PETROPAR DENUNCIÓ A LOS RESPONSABLES DE UENO',fontfamily=BB,fontsize=64,color=NV,va='center')
ax.text(80,214,'Y se terminó el reintegro que llevaba clientes a sus estaciones',fontfamily=B,fontsize=24,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
# izquierda: qué hizo Petropar
ax.text(80,295,'QUÉ HIZO PETROPAR',fontfamily=BB,fontsize=34,color=NV,va='center')
items=[('4 DE NOV','Pidió a la Superintendencia de Bancos','certificar sus saldos y recuperar los fondos'),('6 DE NOV','Denuncia penal ante el Ministerio Público','por presunta estafa y lesión de confianza'),('MOTIVO','No puede acceder a sus fondos a la vista','en ueno. El monto no fue informado')]
for k,(d,a,b) in enumerate(items):
    y=330+k*112; rb(ax,80,y,760,98,SO,8); ax.add_patch(Rectangle((80,y),10,98,color=RD if k==1 else GR))
    ax.text(108,y+49,d,fontfamily=BB,fontsize=30,color=RD if k==1 else GR,va='center')
    ax.text(270,y+32,a,fontfamily=B,fontweight='bold',fontsize=21,color=NV,va='center')
    ax.text(270,y+66,b,fontfamily=B,fontweight='semibold',fontsize=19,color=MU,va='center')
# derecha: reintegro
rb(ax,880,280,650,436,NV,10)
ax.text(910,325,'DIÉSEL PORÃ EN PETROPAR',fontfamily=BB,fontsize=32,color='#AFC0D0',va='center')
ax.text(910,362,'Precio por litro, 50 litros',fontfamily=B,fontsize=19,color='#AFC0D0',va='center')
ax.text(910,420,'Con el 40 % de ueno (octubre)',fontfamily=B,fontweight='bold',fontsize=21,color='white',va='center')
ax.add_patch(Rectangle((910,445),430*5571/9285,46,color='#6DBB78')); ax.text(910+430*5571/9285+12,468,'G. 5.571',fontfamily=BB,fontsize=38,color='#6DBB78',va='center')
ax.text(910,530,'Desde el 3 de noviembre, sin reintegro',fontfamily=B,fontweight='bold',fontsize=21,color='white',va='center')
ax.add_patch(Rectangle((910,555),430,46,color='#E8EEF3')); ax.text(1352,578,'G. 9.285',fontfamily=BB,fontsize=38,color='white',va='center')
ax.text(910,640,'Privados, diésel común: G. 9.490',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(910,676,'Diferencia con Petropar: G. 205 por litro',fontfamily=B,fontweight='bold',fontsize=20,color='#F2A0A4',va='center')
ax.add_patch(Rectangle((80,760),1450,1,color='#DCE3EA'))
ax.text(80,800,'También denunciaron a directivos de ueno el Ministerio de Economía y el Senave (G. 40.000 millones depositados).',fontfamily=B,fontweight='semibold',fontsize=19,color=NV,va='center')
ax.text(80,838,'Reintegro de octubre: 40 % todos los días con tarjetas de crédito ueno por la red Upay, tope de compra G. 600.000.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.text(80,872,'Datos: comunicado de Petropar (6/11/2026), bases del beneficio en la app de ueno (octubre) y precios vigentes al 8/11/2026.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('pd8-web.png',facecolor='white'); Image.open('pd8-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88)
print('ok')
