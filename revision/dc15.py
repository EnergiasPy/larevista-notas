import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-15-decreto-7229-isc-diesel-privados-lunes'; R='/home/claude/larevista-notas/img/'
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
fig,ax=hdr('PARAGUAY · IMPUESTOS','DECRETO 7.229: EL IMPUESTO AL DIÉSEL, A LA MITAD','Impuesto selectivo al consumo (ISC) por litro de diésel tipo III')
card(80,290,450,300,'ANTES','G. 680',['por litro: 18 % sobre una','base de G. 3.777,78'],RD)
card(570,290,450,300,'AHORA','G. 340',['por litro: 18 % sobre una','base de G. 1.888,89'],GR)
card(1060,290,460,300,'AL SURTIDOR','−G. 300',['la baja que trasladan','Petropar y los emblemas','privados'],NV)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'HASTA EL 31 DE DICIEMBRE DE 2026',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'Alcanza solo al diésel tipo III. Las naftas no están incluidas en el decreto.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(120,754,'Desde el 1 de enero de 2027 vuelve la base anterior, si no hay prórroga.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
foot(fig,ax,'Datos: Decreto N° 7.229 del Poder Ejecutivo, 13 de noviembre de 2026.','-1.jpg')
fig,ax=hdr('PARAGUAY · PRECIOS','PETROPAR Y SHELL, DESPUÉS DE LA BAJA','Precios de cartel por litro, al 14 de noviembre de 2026. Shell bajó sus naftas el 8/11')
ax.text(900,288,'PETROPAR',fontfamily=B,fontweight='bold',fontsize=20,color=MU,va='center',ha='center'); ax.text(1300,288,'SHELL',fontfamily=B,fontweight='bold',fontsize=20,color=MU,va='center',ha='center')
for i,(p,a1,b1,eq) in enumerate([('DIÉSEL COMÚN','8.985','8.985',1),('NAFTA 93 OCTANOS','7.190','7.190',1),('NAFTA 97 OCTANOS','8.690','8.890',0)]):
    y=320+i*140; rb(ax,80,y,1440,118,SO,10); ax.add_patch(Rectangle((80,y),8,118,color=GR if eq else RD))
    ax.text(120,y+59,p,fontfamily=BB,fontsize=46,color=NV,va='center')
    ax.text(900,y+59,'G. '+a1,fontfamily=BB,fontsize=54,color=NV,va='center',ha='center'); ax.text(1300,y+59,'G. '+b1,fontfamily=BB,fontsize=54,color=GR if eq else RD,va='center',ha='center')
ax.text(80,780,'Mismo precio en el diésel común y en la nafta 93. En la 97, Shell queda G. 200 por encima.',fontfamily=B,fontweight='bold',fontsize=21,color=NV,va='center')
foot(fig,ax,'Datos: precios de cartel de Petropar y de estaciones Shell, 13 y 14 de noviembre de 2026.','-2.jpg')
print('ok')
