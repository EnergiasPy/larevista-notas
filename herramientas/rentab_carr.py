import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/carr/'; os.makedirs(O,exist_ok=True)
N=8
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
logo=Image.open('/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png').convert('RGBA')
mk=Image.new('L',logo.size,0); ImageDraw.Draw(mk).ellipse((6,6,506,506),fill=255); logo.putalpha(mk)
def base(n, kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(['#D52B1E','#FFFFFF','#0038A8']): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
    if kicker: ax.text(70,110,kicker,fontfamily=BC,fontweight='bold',fontsize=26,color=G,va='center')
    ax.text(1010,1295,'energiaslatam.com',fontfamily=BC,fontweight='bold',fontsize=28,color=W,va='center',ha='right')
    ax.text(70,1295,f'{n}/{N}',fontfamily=BC,fontweight='bold',fontsize=24,color=M,va='center')
    if n<N: ax.text(540,1295,'Deslizá  »',fontfamily=B,fontweight='semibold',fontsize=22,color=M,va='center',ha='center')
    return fig,ax
def title(ax,lines,y0=200,size=84,step=92,green_last=True):
    for i,l in enumerate(lines): ax.text(66,y0+i*step,l,fontfamily=BB,fontsize=size,color=G if (green_last and i==len(lines)-1) else W,va='center')
    return y0+len(lines)*step
def cards(ax,items,y0,h=130,gap=22,big=False):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.38,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.72,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def save(fig,name): fig.savefig(O+name+'.png',facecolor=BG); Image.open(O+name+'.png').convert('RGB').save(R+name+'.jpg',quality=92); plt.close(fig)

# 1 portada
fig,ax=base(1,None)
ax.imshow(np.array(logo),extent=(70,230,290,130),zorder=3)
ax.text(250,190,'LA ESTACIÓN',fontfamily=BB,fontsize=50,color=W,va='center'); ax.text(250,245,'DEL FUTURO',fontfamily=BB,fontsize=50,color=G,va='center')
for i,l in enumerate(['SI BAJAN','LAS VENTAS','DE COMBUSTIBLE…']):
    ax.text(66,420+i*148,l,fontfamily=BB,fontsize=120,color=W,va='center')
ax.add_patch(Rectangle((70,820),140,7,color=G))
for i,l in enumerate(['¿Qué podemos hacer para','mejorar la rentabilidad','de la estación?']):
    ax.text(70,900+i*66,l,fontfamily=B,fontweight='bold',fontsize=46,color=G,va='center')
ax.text(70,1145,'6 ideas para aprovechar cada visita',fontfamily=B,fontweight='semibold',fontsize=30,color=M,va='center')
save(fig,'rentabilidad-1')

# 2 cada cliente
fig,ax=base(2,'IDEA 1 · LA OPORTUNIDAD')
y=title(ax,['CADA CLIENTE','QUE ENTRA ES UNA','OPORTUNIDAD'])
ax.text(70,y+40,'Mientras se carga el vehículo, el vendedor de playa',fontfamily=B,fontweight='semibold',fontsize=28,color=M,va='center')
ax.text(70,y+82,'puede hacer una invitación simple:',fontfamily=B,fontweight='semibold',fontsize=28,color=M,va='center')
rb(ax,60,y+130,960,330,'#FFFFFF',22)
for i,l in enumerate(['“Mientras esperás,','¿por qué no aprovechás','las ofertas que tenemos','en la tienda?”']):
    ax.text(110,y+190+i*70,l,fontfamily=B,fontweight='bold',fontsize=44,color=BG,va='center')
ax.text(70,y+530,'Sin presionar al cliente ni descuidar la seguridad de la carga.',fontfamily=B,fontweight='semibold',fontsize=25,color=G,va='center')
save(fig,'rentabilidad-2')

# 3 playa y tienda
fig,ax=base(3,'IDEA 2 · TRABAJO EN EQUIPO')
y=title(ax,['LA PLAYA Y','LA TIENDA, JUNTAS'])
ax.text(70,y+30,'Para el cliente es una sola experiencia.',fontfamily=B,fontweight='semibold',fontsize=29,color=M,va='center')
cards(ax,[('Antes de cada turno','El encargado repasa las promociones vigentes'),('En la playa','El equipo conoce qué ofrecer y cuándo'),('En la tienda','El producto está, con precio y atención ágil'),('Si no está la oferta','Se pierde la venta y la confianza del cliente')],y+90)
save(fig,'rentabilidad-3')

# 4 excelencia
fig,ax=base(4,'IDEA 3 · ATENCIÓN')
y=title(ax,['UN PROGRAMA DE','EXCELENCIA EN PLAYA'],size=80,step=88)
pasos=[('Saludar','y confirmar combustible e importe'),('Seguridad','cumplir procedimientos y atender con orden'),('Conocer','las promociones y servicios de la estación'),('Invitar','con una frase breve y natural a la tienda'),('Cerrar','resolver consultas y agradecer la visita')]
for k,(t,s) in enumerate(pasos):
    yy=y+50+k*140; rb(ax,60,yy,960,120,CARD); ax.add_patch(Rectangle((60,yy),10,120,color=G))
    ax.text(105,yy+60,str(k+1),fontfamily=BB,fontsize=64,color=G,va='center')
    ax.text(170,yy+42,t.upper(),fontfamily=BB,fontsize=42,color=W,va='center')
    ax.text(172,yy+86,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
save(fig,'rentabilidad-4')

# 5 comunicar
fig,ax=base(5,'IDEA 4 · COMUNICACIÓN')
y=title(ax,['SI NADIE LO CUENTA,','EL CLIENTE','NO LO SABE'])
ax.text(70,y+30,'Promos, café, sanitarios limpios, lavado, medios de pago…',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
chips=['Playa','Tienda','Carteles','Redes','Google']
for k,c in enumerate(chips):
    x=70+(k%3)*320; yy=y+100+(k//3)*120
    rb(ax,x,yy,290,96,G if k==0 else CARD,48); ax.text(x+145,yy+48,c.upper(),fontfamily=BB,fontsize=46,color=BG if k==0 else W,va='center',ha='center')
ax.text(70,y+400,'El mensaje tiene que ser claro y la propuesta',fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
ax.text(70,y+446,'tiene que existir cuando el cliente llega.',fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
save(fig,'rentabilidad-5')

# 6 costos
fig,ax=base(6,'IDEA 5 · RENTABILIDAD')
y=title(ax,['VENDER MÁS','TAMBIÉN ES','MIRAR LOS COSTOS'])
ax.text(70,y+30,'No toda promoción deja más rentabilidad. Revisá:',fontfamily=B,fontweight='semibold',fontsize=28,color=M,va='center')
cards(ax,[('Mercadería','Costo, vencimientos, mermas y rotación'),('Operación','Heladeras, iluminación y servicios contratados'),('Equipo','Organización de los turnos y dotación adecuada')],y+90,h=140)
ax.text(70,y+640,'Optimizar no es recortar por recortar.',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center')
save(fig,'rentabilidad-6')

# 7 prueba
fig,ax=base(7,'IDEA 6 · EMPEZAR')
y=title(ax,['EMPEZÁ CON','UNA PRUEBA SIMPLE'])
for k,(n,t) in enumerate([('1','Elegí una oferta de la tienda'),('2','Explicásela al equipo de playa'),('3','Medí las ventas durante unas semanas'),('4','Si funciona, repetila. Si no, ajustala')]):
    yy=y+60+k*150; ax.add_patch(plt.Circle((120,yy+55),48,color=G)); ax.text(120,yy+57,n,fontfamily=BB,fontsize=60,color=BG,va='center',ha='center')
    ax.text(200,yy+55,t,fontfamily=B,fontweight='bold',fontsize=34,color=W,va='center')
ax.text(70,y+700,'No hace falta una gran inversión: hace falta constancia.',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save(fig,'rentabilidad-7')

# 8 cierre
fig,ax=base(8,None)
ax.imshow(np.array(logo),extent=(415,665,420,170),zorder=3)
for i,l in enumerate(['¿ESTAMOS APROVECHANDO','TODAS LAS OPORTUNIDADES','DE CADA VISITA?']):
    ax.text(540,530+i*95,l,fontfamily=BB,fontsize=78,color=G if i==2 else W,va='center',ha='center')
ax.text(540,860,'Leé la nota completa en La Estación del Futuro',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center',ha='center')
rb(ax,240,930,600,96,G,48); ax.text(540,978,'LINK EN LA BIO',fontfamily=BB,fontsize=56,color=BG,va='center',ha='center')
ax.text(540,1110,'Seguinos para más ideas para tu estación',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center',ha='center')
save(fig,'rentabilidad-8')
print('ok')
