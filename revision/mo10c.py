import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; BC='Barlow Condensed'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-08-bolivia-diesel-precio-internacional-paz'; R='/home/claude/larevista-notas/img/'
BOF=('#D52B1E','#F9E300','#007934')
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
ID='2026-11-10-mopc-registro-autogeneracion-renovable'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'LA CUENTA · EJEMPLO',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'¿SE RECUPERA? UN SISTEMA SOLAR EN EL CANOPY',fontfamily=BB,fontsize=64,color=NV,va='center')
ax.text(80,214,'Estimación simple, solo con la energía que la estación consume (sin contar venta de excedentes)',fontfamily=B,fontsize=22,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
rows=[('Potencia instalada','30 kWp','unos 65 paneles de 460 W'),('Inversión (USD 700 por kW)','≈ G. 135 M','USD 21.000; el rango va de USD 350 a 1.000 por kW'),('Energía generada','≈ 43.800 kWh/año','5 horas de sol pico y 80 % de rendimiento'),('Ahorro en la factura','≈ G. 17,8 M/año','G. 406/kWh: tarifa comercial ANDE, baja tensión')]
y=290
for k,(a,b,c) in enumerate(rows):
    rb(ax,80,y,1000,110,SO,10); ax.add_patch(Rectangle((80,y),8,110,color=GR))
    ax.text(115,y+38,a,fontfamily=B,fontweight='bold',fontsize=22,color=MU,va='center')
    ax.text(115,y+80,c,fontfamily=B,fontweight='semibold',fontsize=18,color=NV,va='center')
    ax.text(1060,y+55,b,fontfamily=BC,fontweight='bold',fontsize=40,color=NV,va='center',ha='right'); y+=125
rb(ax,1120,290,400,485,NV,10)
ax.text(1150,340,'RECUPERO',fontfamily=BB,fontsize=32,color='#AFC0D0',va='center')
ax.text(1150,430,'≈ 7,6',fontfamily=BB,fontsize=110,color='#6DBB78',va='center')
ax.text(1150,505,'años',fontfamily=B,fontweight='bold',fontsize=30,color='white',va='center')
ax.text(1150,580,'Con USD 350/kW: ≈ 3,8 años',fontfamily=B,fontweight='semibold',fontsize=19,color='white',va='center')
ax.text(1150,615,'Con USD 1.000/kW: ≈ 10,9 años',fontfamily=B,fontweight='semibold',fontsize=19,color='white',va='center')
ax.text(1150,670,'Vida útil de los paneles:',fontfamily=B,fontweight='semibold',fontsize=19,color='#AFC0D0',va='center')
ax.text(1150,702,'hasta 25 años',fontfamily=B,fontweight='bold',fontsize=19,color='white',va='center')
ax.add_patch(Rectangle((80,800),1440,1,color='#DCE3EA'))
ax.text(80,838,'No incluye mantenimiento, baterías, degradación ni la venta de excedentes, cuyo precio para baja potencia todavía no se publicó.',fontfamily=B,fontweight='semibold',fontsize=18,color=NV,va='center')
ax.text(80,872,'Datos: ANDE (Pliego de Tarifas N.º 21), instaladores y técnicos del sector. Cambio: G. 6.450 por dólar. Ejemplo, no presupuesto.',fontfamily=B,fontsize=17,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('mo10c.png',facecolor='white'); Image.open('mo10c.png').convert('RGB').save(R+ID+'-3.jpg',quality=88); plt.close(fig)
print('ok')
