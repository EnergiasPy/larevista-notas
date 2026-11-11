import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-11-itaipu-paraguay-supera-2025-solar-flotante'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#D52B1E','#FFFFFF','#0038A8')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
    ax.text(80,72,k,fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
    ax.text(76,148,t,fontfamily=BB,fontsize=62,color=NV,va='center')
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
fig,ax=hdr('PARAGUAY · ELECTRICIDAD','PARAGUAY, A UN PASO DE SUPERAR TODO 2025','Energía que Itaipú le entregó al país a través de la ANDE, en gigavatios hora (GWh)')
def card(x,y,w,h,k,big,lines,col):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=64,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,290,450,300,'ENERO A OCTUBRE 2026','24.121 GWh',['Solo en octubre fueron','2.503 GWh: unos 81 GWh','por día'],GR)
card(570,290,450,300,'TODO 2025','25.768 GWh',['Ya había sido un récord:','26,4 % más que en 2024'],NV)
card(1060,290,460,300,'LO QUE FALTA','1.647 GWh',['Al ritmo de octubre, se','alcanza alrededor del','20 de noviembre'],RD)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'Y EN EL EMBALSE, EL SOL',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'Itaipú opera una planta solar flotante de 1,1 MWp en Hernandarias y estudia llevarla a 10 MW, con almacenamiento.',fontfamily=B,fontweight='semibold',fontsize=19,color='white',va='center')
ax.text(120,754,'Los resultados del estudio binacional se esperan para el primer trimestre de 2027.',fontfamily=B,fontweight='semibold',fontsize=19,color='white',va='center')
foot(fig,ax,'Datos: Itaipú Binacional (informes de producción y suministro). La fecha estimada es un cálculo propio con el ritmo de octubre.','-1.jpg')
# placa 2: barras
fig,ax=hdr('PARAGUAY · ELECTRICIDAD','CADA AÑO, MÁS ENERGÍA DE ITAIPÚ','Suministro de Itaipú al Paraguay, en GWh')
rows=[('2024',20383,'20.383',MU),('2025',25768,'25.768',NV),('2026 · ENE-OCT',24121,'24.121',GR),('2026 · PROYECCIÓN',29000,'≈ 29.000',RD)]
for i,(l,v,t,c) in enumerate(rows):
    y=300+i*125; ax.text(80,y+40,l,fontfamily=BB,fontsize=34,color=NV,va='center')
    w=v/29000*900; rb(ax,420,y,w,80,c,8); ax.text(420+w+20,y+40,t,fontfamily=BB,fontsize=40,color=c,va='center')
ax.text(80,810,'Proyección: lo entregado hasta octubre más unos 2.450 GWh por mes en noviembre y diciembre. Sería cerca de 13 % más que en 2025.',fontfamily=B,fontweight='semibold',fontsize=16,color=MU,va='center')
foot(fig,ax,'Datos: Itaipú Binacional. 2024 calculado a partir del aumento de 26,4 % informado para 2025. La proyección es un cálculo propio.','-2.jpg')
print('ok')
