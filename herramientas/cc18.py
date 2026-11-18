import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-16-ande-licita-640-mw-chaco-solar-baterias'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
ID='2026-11-18-cuida-tu-combustible-tapas-agua-lluvias'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
    ax.text(80,72,k,fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
    ax.text(76,148,t,fontfamily=BB,fontsize=60,color=NV,va='center')
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
def card(x,y,w,h,k,big,lines,col,fs=64):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')

fig,ax=hdr('PARAGUAY · ANTES DE LAS LLUVIAS','EL AGUA ENTRA POR LA TAPA DEL TANQUE','Tres verificaciones que llevan menos de media hora')
card(80,290,460,300,'UNO','TAPAS',['Que cierren herméticas,','no apoyadas. Revisá la junta:','flexible y entera.'],NV,fs=104)
card(570,290,460,300,'DOS','CÁMARA',['Seca antes de abrir.','Si tiene agua, al abrir','se va adentro del tanque.'],RD,fs=96)
card(1060,290,460,300,'TRES','PASTA',['Medí el agua de fondo','antes y después de la lluvia.','Si subió, entró por arriba.'],GR,fs=104)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'Y DESDE ENERO EL GASOIL LLEVA 8 % DE BIODIÉSEL',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
ax.text(120,730,'El biodiésel absorbe humedad con más facilidad. Con más biodiésel, el agua en el tanque perdona menos.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
foot(fig,ax,'Guía de verificación para estaciones de servicio. Fotos de instalaciones: Energías LATAM.','-1.jpg')

fig,ax=hdr('SI ENCONTRÁS AGUA','QUÉ HACER, EN ESTE ORDEN','Lo que conviene resolver antes de la próxima descarga')
for i,(t,d2) in enumerate([('SACARLA, NO ESPERAR','Recibir producto nuevo sobre un fondo con agua mezcla el problema con el stock'),('BUSCAR POR DÓNDE ENTRÓ','La junta de la tapa, la cámara que junta agua o el nivel del piso alrededor'),('DEJARLO ANOTADO','Fecha, tanque, cuánta agua y qué se hizo: muestra si el problema se repite'),('REVISAR ANTES, NO DESPUÉS','Cuesta una fracción de lo que cuesta un tanque contaminado')]):
    y=296+i*118; rb(ax,80,y,1440,100,SO,10); ax.add_patch(Rectangle((80,y),8,100,color=GR))
    ax.text(120,y+34,t,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.text(122,y+72,d2,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
ax.text(80,800,'El agua favorece la corrosión, alimenta la contaminación microbiana y termina tapando filtros.',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
foot(fig,ax,'Guía de verificación para estaciones de servicio. Energías LATAM.','-2.jpg')
print('ok')
