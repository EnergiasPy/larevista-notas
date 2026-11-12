import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-12-petroleo-dolar-barril-guaranies-diciembre'; R='/home/claude/larevista-notas/img/'
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
fig,ax=hdr('PARAGUAY · MERCADO Y PRECIOS','EL BARRIL EN GUARANÍES CUESTA 14 % MENOS','El petróleo cayó más de lo que subió el dólar. La cuenta, al miércoles 11 de noviembre')
def card(x,y,w,h,k,big,lines,col,fs=64):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
card(80,290,450,300,'PETRÓLEO BRENT','USD 92,76',['Cerraba octubre en USD 117,64:','cerca de 21 % menos'],GR)
card(570,290,450,300,'DÓLAR DE REFERENCIA','G. 6.200',['Llegó a rondar los G. 6.600.','A fin de octubre: unos G. 5.700'],NV)
card(1060,290,460,300,'UN BARRIL, EN GUARANÍES','G. 575.000',['A fin de octubre costaba','unos G. 670.000'],RD)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'POR QUÉ TODAVÍA NO BAJA EL SURTIDOR',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'Petropar mantiene sus precios hasta el 30 de noviembre y las distribuidoras tienen stock comprado más caro.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(120,754,'Si el petróleo y el dólar siguen así, el alivio debería sentirse hacia diciembre.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
foot(fig,ax,'Cálculo propio y aproximado: precio del Brent por dólar de referencia. Datos del mercado internacional y del BCP.','-1.jpg')
fig,ax=hdr('PARAGUAY · MERCADO Y PRECIOS','CUÁNTO CUESTA UN BARRIL EN GUARANÍES','Precio del Brent multiplicado por el dólar de referencia, valores aproximados')
rows=[('FIN DE OCTUBRE',670000,'G. 670.000','USD 117,64 × G. 5.700',MU),('PRIMERA SEMANA DE NOV.',649000,'G. 649.000','USD 98 × G. 6.600',NV),('MIÉRCOLES 11 DE NOV.',575000,'G. 575.000','USD 92,76 × G. 6.200',GR)]
for i,(l,v,t,sub,c) in enumerate(rows):
    y=300+i*160; ax.text(80,y+28,l,fontfamily=BB,fontsize=34,color=NV,va='center'); ax.text(80,y+66,sub,fontfamily=B,fontweight='semibold',fontsize=19,color=MU,va='center')
    w=v/670000*780; rb(ax,480,y,w,90,c,8); ax.text(480+w+20,y+45,t,fontfamily=BB,fontsize=44,color=c,va='center')
ax.text(80,800,'El dólar se comió casi toda la baja de la primera semana. Con el dólar otra vez en G. 6.200, la baja del petróleo se nota.',fontfamily=B,fontweight='semibold',fontsize=18,color=MU,va='center')
foot(fig,ax,'Cálculo propio. No incluye el precio de los refinados, el flete ni los impuestos.','-2.jpg')
print('ok')
