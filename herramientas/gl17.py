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
ID='2026-11-17-autogas-cae-estaciones-industria-glp'; R='/home/claude/larevista-notas/img/'
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
def card(x,y,w,h,k,big,lines,col,fs=64):
    rb(ax,x,y,w,h,SO,10); ax.add_patch(Rectangle((x,y),8,h,color=col))
    ax.text(x+40,y+48,k,fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
    ax.text(x+40,y+118,big,fontfamily=BB,fontsize=fs,color=col,va='center')
    for j,t in enumerate(lines): ax.text(x+40,y+188+j*32,t,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')

# -1 · el reparto del GLP
fig,ax=hdr('PARAGUAY · GAS LICUADO','EL GAS SE VA DEL SURTIDOR A LA FÁBRICA','Ventas de GLP por destino, enero a septiembre, en toneladas')
card(80,290,460,300,'ESTACIONES DE SERVICIO','−11,3 %',['18.823 t contra 21.232 t','del año pasado'],RD,fs=96)
card(570,290,460,300,'INDUSTRIAS','+14,7 %',['11.222 t contra 9.783 t','del año pasado'],GR,fs=96)
card(1060,290,460,300,'GARRAFAS','−1,9 %',['30.275 t contra 30.870 t:','casi sin cambio'],MU,fs=96)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'EL MERCADO TOTAL APENAS SE MOVIÓ: −2,5 %',fontfamily=BB,fontsize=38,color='#6DBB78',va='center')
ax.text(120,730,'60.321 toneladas contra 61.885. Lo que cambió no es cuánto gas se vende, sino quién lo compra.',fontfamily=B,fontweight='semibold',fontsize=21,color='white',va='center')
foot(fig,ax,'Datos: registro del Ministerio de Industria y Comercio, ventas declaradas de enero a septiembre de 2026 y 2025.','-1.jpg')

# -2 · quien manda en el autogas
fig,ax=hdr('AUTOGAS','QUIÉN VENDE EL GLP EN LAS ESTACIONES','Toneladas despachadas en estaciones de servicio, enero a septiembre')
D=[('PETROPAR','5.411 t','−11,6 %',RD),('COPETROL','3.601 t','−10,0 %',RD),('COPESA','3.396 t','−17,6 %',RD),('SAN ISIDRO','1.638 t','entró de cero',GR),('LIMA GAS','927 t','−15,7 %',RD),('PUMA','553 t','−18,1 %',RD)]
for i,(n,v,d2,c) in enumerate(D):
    y=296+i*82; rb(ax,80,y,1440,70,SO,10); ax.add_patch(Rectangle((80,y),8,70,color=c))
    ax.text(124,y+36,n,fontfamily=BB,fontsize=38,color=NV,va='center')
    ax.text(900,y+36,v,fontfamily=BB,fontsize=38,color=NV,va='center',ha='right')
    ax.text(1480,y+36,d2,fontfamily=B,fontweight='bold',fontsize=23,color=c,va='center',ha='right')
ax.text(80,806,'Entre las tres primeras se reparte el 66 % del autogas del país.',fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center')
foot(fig,ax,'Datos: registro del Ministerio de Industria y Comercio. Variación contra el mismo período de 2025.','-2.jpg')

# -3 · de donde viene y a que precio
fig,ax=hdr('ORIGEN Y PRECIOS','TODO EL GAS ENTRA POR UN SOLO VECINO','De dónde viene el GLP que consume Paraguay y a cuánto se vende')
card(80,290,700,300,'IMPORTACIÓN ENERO A SEPTIEMBRE','99,2 %',['61.665 de las 62.166 toneladas','que entraron vinieron de Argentina'],NV,fs=104)
card(820,290,700,300,'EL RESTO','501 t',['repartidas entre todos','los demás orígenes'],MU,fs=104)
rb(ax,80,630,700,150,SO,10); ax.add_patch(Rectangle((80,630),8,150,color=GR))
ax.text(120,678,'GARRAFA DE 10 KG',fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
ax.text(120,735,'de 100.000 a 120.000 Gs',fontfamily=BB,fontsize=44,color=NV,va='center')
rb(ax,820,630,700,150,SO,10); ax.add_patch(Rectangle((820,630),8,150,color=GR))
ax.text(860,678,'EN EL SURTIDOR',fontfamily=B,fontweight='bold',fontsize=21,color=MU,va='center')
ax.text(860,735,'de 4.700 a 5.500 Gs/L',fontfamily=BB,fontsize=44,color=NV,va='center')
foot(fig,ax,'Datos: registro del Ministerio de Industria y Comercio. Precios declarados por cada empresa, IVA incluido.','-3.jpg')
print('ok')
