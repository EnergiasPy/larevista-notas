import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-14-chile-congela-combustibles-marzo-acuerdo-camioneros'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#0039A6','#FFFFFF','#D52B1E')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
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
fig,ax=hdr('REGIÓN · CHILE','EL ACUERDO QUE LEVANTÓ EL PARO','Lo que pactó el Gobierno chileno con los camioneros, 12 de noviembre de 2026')
card(80,290,450,300,'DIÉSEL','−$141,9',['por litro: reversión del alza','de $41,9 más una baja de $100'],GR,fs=60)
card(570,290,450,300,'CONGELAMIENTO','31/3/2027',['precios fijos de bencinas','y diésel hasta esa fecha'],NV,fs=60)
card(1060,290,460,300,'COSTO FISCAL','US$ 900 M',['paquete completo, con medidas','hasta diciembre de 2027'],RD,fs=60)
rb(ax,80,630,1440,150,NV,10)
ax.text(120,675,'FALTA LA LEY',fontfamily=BB,fontsize=32,color='#6DBB78',va='center')
ax.text(120,720,'El proyecto ingresó a la Cámara de Diputados el 12 de noviembre. La reversión rige cuando se apruebe.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(120,754,'Transportistas: recuperan hasta el 90 % del impuesto específico al diésel hasta diciembre de 2027.',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
foot(fig,ax,'Datos: Ministerio del Interior, Ministerio de Hacienda y ENAP (Chile), 12 y 13 de noviembre de 2026.','-1.jpg')
fig,ax=hdr('REGIÓN · DIÉSEL','CÓMO BAJAN EL DIÉSEL LOS GOBIERNOS','Tres países, tres herramientas para contener el precio en noviembre de 2026')
rows=[('PARAGUAY','−50 % DEL ISC','unos G. 340 por litro, hasta el 31 de diciembre. Petropar y privados bajan G. 300',RD),
('CHILE','CONGELA Y BAJA','−$100 por litro más la reversión del alza; precios fijos hasta el 31 de marzo',NV),
('BRASIL','SUBSIDIO','R$ 2,12 por litro de diésel, extendido hasta fin de noviembre',GR)]
for i,(p,h,t,c) in enumerate(rows):
    y=290+i*165; rb(ax,80,y,1440,145,SO,10); ax.add_patch(Rectangle((80,y),8,145,color=c))
    ax.text(120,y+50,p,fontfamily=BB,fontsize=40,color=NV,va='center'); ax.text(440,y+50,h,fontfamily=BB,fontsize=40,color=c,va='center')
    ax.text(120,y+105,t,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
foot(fig,ax,'Datos: Poder Ejecutivo y Petropar (Paraguay), Gobierno de Chile, Ministerio de Hacienda de Brasil, noviembre de 2026.','-2.jpg')
print('ok')
