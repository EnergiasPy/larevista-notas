import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-08-bolivia-diesel-precio-internacional-paz'; R='/home/claude/larevista-notas/img/'
BOF=('#D52B1E','#F9E300','#007934')
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(BOF): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'BOLIVIA · MERCADO Y PRECIOS',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'UN AÑO DE PAZ: EL DIÉSEL YA VA A PRECIO INTERNACIONAL',fontfamily=BB,fontsize=60,color=NV,va='center')
ax.text(80,214,'La gasolina sigue subsidiada. Precio por litro en dólares, Bolivia frente a Paraguay',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
mx=1.7; x0=300; W=470
def bar(y,lab,v,c,txt):
    ax.text(x0-20,y+22,lab,fontfamily=B,fontweight='bold',fontsize=21,color=NV,va='center',ha='right')
    ax.add_patch(Rectangle((x0,y),W*v/mx,44,color=c)); ax.text(x0+W*v/mx+14,y+22,txt,fontfamily=BB,fontsize=34,color=c,va='center')
ax.text(80,300,'DIÉSEL',fontfamily=BB,fontsize=36,color=NV,va='center')
bar(330,'Bolivia',1.53,RD,'USD 1,53  (Bs 17,95)'); bar(390,'Paraguay',1.44,GR,'USD 1,44  (G. 9.285)')
ax.text(80,490,'GASOLINA / NAFTA',fontfamily=BB,fontsize=36,color=NV,va='center')
bar(520,'Bolivia',0.59,RD,'USD 0,59  (Bs 6,96)'); bar(580,'Paraguay',1.08,GR,'USD 1,08  (G. 6.990)')
ax.text(80,672,'Paraguay: Diésel Porã y Kape 88 de Petropar.',fontfamily=B,fontsize=18,color=MU,va='center')
rb(ax,1150,290,380,420,NV,10)
ax.text(1180,335,'LA RUTA DEL DIÉSEL',fontfamily=BB,fontsize=30,color='#AFC0D0',va='center')
st=[('DIC 2025','De Bs 3,72 a Bs 9,80'),('AGO 2026','Grandes consumidores: Bs 18'),('SEP 2026','Paridad de importación:'),('','Bs 17,95 y ajuste por banda')]
yy=390
for d,t in st:
    if d: ax.text(1180,yy,d,fontfamily=BB,fontsize=28,color='#6DBB78',va='center')
    ax.text(1180,yy+34 if d else yy-6,t,fontfamily=B,fontweight='semibold',fontsize=19,color='white',va='center'); yy+=80 if d else 40
ax.add_patch(Rectangle((80,760),1450,1,color='#DCE3EA'))
ax.text(80,800,'Rodrigo Paz cumple un año en la presidencia el 8 de noviembre de 2026. La subvención costaba USD 55 a 60 millones por semana.',fontfamily=B,fontweight='semibold',fontsize=18,color=NV,va='center')
ax.text(80,838,'Datos: Gobierno de Bolivia (DS 5503 y 5716), YPFB, BCB, Petropar y BCP. Cambio aprox.: Bs 11,7 y G. 6.450 por dólar.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('bo8-web.png',facecolor='white'); Image.open('bo8-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88); plt.close(fig)
print('ok')
