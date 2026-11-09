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
ID='2026-11-09-uruguay-gasoil-debajo-referencia-ancap'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(('#0038A8','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'REGIÓN · URUGUAY',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'URUGUAY CONGELA EL SURTIDOR EN NOVIEMBRE',fontfamily=BB,fontsize=62,color=NV,va='center')
ax.text(80,214,'Precio máximo frente a la referencia de la URSEA, en pesos uruguayos por litro',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
mx=100; x0=330; W=560
def bar(y,lab,v,c,txt):
    ax.text(x0-20,y+22,lab,fontfamily=B,fontweight='bold',fontsize=21,color=NV,va='center',ha='right')
    ax.add_patch(Rectangle((x0,y),W*v/mx,44,color=c)); ax.text(x0+W*v/mx+14,y+22,txt,fontfamily=BB,fontsize=34,color=c,va='center')
ax.text(80,300,'GASOIL 50S',fontfamily=BB,fontsize=36,color=NV,va='center')
bar(330,'Precio fijado',62.79,GR,'$ 62,79'); bar(390,'Referencia URSEA',82.4,RD,'≈ $ 82,4  (+31,3 %)')
ax.text(80,490,'NAFTA SÚPER 95',fontfamily=BB,fontsize=36,color=NV,va='center')
bar(520,'Precio fijado',90.45,GR,'$ 90,45'); bar(580,'Referencia URSEA',93.4,RD,'≈ $ 93,4  (+3,3 %)')
ax.text(80,672,'Referencia: precio de noviembre más la suba que implicaba el informe de la URSEA.',fontfamily=B,fontsize=18,color=MU,va='center')
rb(ax,1150,290,380,420,NV,10)
ax.text(1180,335,'QUIÉN PAGA',fontfamily=BB,fontsize=30,color='#AFC0D0',va='center')
ax.text(1180,410,'USD 80 M',fontfamily=BB,fontsize=64,color='#6DBB78',va='center')
for k,t in enumerate(['dejó de recaudar ANCAP','frente a la paridad de','importación en el','primer semestre de 2026']):
    ax.text(1180,470+k*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(1180,630,'Desde abril:',fontfamily=B,fontweight='bold',fontsize=19,color='#AFC0D0',va='center')
ax.text(1180,662,'revisión mensual de precios',fontfamily=B,fontweight='semibold',fontsize=19,color='white',va='center')
ax.add_patch(Rectangle((80,760),1450,1,color='#DCE3EA'))
ax.text(80,800,'En dólares (≈ $ 40,3 por USD): gasoil 50S, USD 1,56 por litro; nafta súper, USD 2,24. Paraguay: Diésel Porã, USD 1,44.',fontfamily=B,fontweight='semibold',fontsize=18,color=NV,va='center')
ax.text(80,838,'Datos: Presidencia de Uruguay, URSEA, ANCAP, Petropar y BCP. Conversiones aproximadas.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('uy9-web.png',facecolor='white'); Image.open('uy9-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88); plt.close(fig)
print('ok')
