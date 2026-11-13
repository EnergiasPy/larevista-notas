import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-13-region-barril-baja-surtidor'; R='/home/claude/larevista-notas/img/'
def hdr(k,t,b):
    fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
    for i,c in enumerate(('#3A7D44','#FFFFFF','#0C1A29')): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
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
fig,ax=hdr('REGIÓN · COMBUSTIBLES','EL BARRIL BAJÓ. ¿Y EL SURTIDOR?','Qué pasó con los precios en la región tras la caída del petróleo, al 13 de noviembre')
rows=[('PERÚ','BAJÓ',GR,'Petroperú y Repsol: diésel hasta S/ 1,43 menos por galón (10/11)'),
('ECUADOR','BAJÓ',GR,'Extra, Ecopaís y diésel: 5 centavos menos por galón desde el 12/11'),
('CHILE','SUBIÓ',RD,'+$41,9 el diésel y +$38,7 las bencinas por litro (12/11); el Gobierno promete revertirlo'),
('ARGENTINA','SUBIÓ',RD,'La nafta súper de YPF pasó de $2.090 a $2.103 mientras caía el crudo'),
('URUGUAY','QUIETO',MU,'Precios congelados en noviembre: gasoil a $62,79, unos $20 bajo el precio técnico'),
('BRASIL','QUIETO',MU,'Petrobras no descarta ajustes puntuales, pero no anunció cambios'),
('BOLIVIA','QUIETO',MU,'El diésel se mantiene en Bs 17,95 por litro, según la ANH')]
for i,(p,st,c,t) in enumerate(rows):
    y=278+i*76; rb(ax,80,y,1440,64,SO,8); ax.add_patch(Rectangle((80,y),8,64,color=c))
    ax.text(112,y+33,p,fontfamily=BB,fontsize=34,color=NV,va='center')
    rb(ax,330,y+13,120,38,c,6); ax.text(390,y+33,st,fontfamily=BB,fontsize=26,color='white',va='center',ha='center')
    ax.text(475,y+33,t,fontfamily=B,fontweight='semibold',fontsize=19,color=NV,va='center')
foot(fig,ax,'Datos: Opecu (Perú), Gobierno de Ecuador, ENAP (Chile), surtidores de YPF, MIEM-URSEA (Uruguay), Petrobras y ANH (Bolivia), al 13/11/2026.','-1.jpg')
fig,ax=hdr('REGIÓN · PETRÓLEO','EL BRENT CAYÓ 24 % EN 11 DÍAS','Precio del barril de petróleo Brent, en dólares')
vals=[('30 DE OCTUBRE',117.58,RD),('10 DE NOVIEMBRE',89.34,GR),('11 DE NOVIEMBRE',93.83,NV)]
for i,(l,v,c) in enumerate(vals):
    x=200+i*440; h=v*3.7; y0=790
    rb(ax,x,y0-h,260,h,c,6); ax.text(x+130,y0-h-40,'USD '+f'{v:.2f}'.replace('.',','),fontfamily=BB,fontsize=48,color=c,va='center',ha='center')
    ax.text(x+130,y0+24,l,fontfamily=B,fontweight='bold',fontsize=20,color=MU,va='center',ha='center')
foot(fig,ax,'Datos: cotización del Brent en el mercado internacional. Los precios en surtidor se ajustan con rezago y según las reglas de cada país.','-2.jpg')
print('ok')
