# Carrusel 1080x1350 · Paraguay · Colombia · margen de la estación · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/co20/'; os.makedirs(O,exist_ok=True)
ID='2026-11-20-cuanto-gana-estacion-de-servicio-colombia-margen-minimo'
N=7; BR=['#FCD116','#003893','#CE1126']
def rb(ax,x,y,w,h,c,r=14): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
def base(n,kicker):
    fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1350,0); ax.axis('off')
    for i,c in enumerate(BR): ax.add_patch(Rectangle((0,i*7),1080,7,color=c))
    if kicker: ax.text(70,110,kicker,fontfamily=BC,fontweight='bold',fontsize=26,color=G,va='center')
    ax.text(1010,1295,'energiaslatam.com',fontfamily=BC,fontweight='bold',fontsize=28,color=W,va='center',ha='right')
    ax.text(70,1295,f'{n}/{N}',fontfamily=BC,fontweight='bold',fontsize=24,color=M,va='center')
    if n<N: ax.text(540,1295,'Deslizá  »',fontfamily=B,fontweight='semibold',fontsize=22,color=M,va='center',ha='center')
    return fig,ax
def title(ax,lines,y0=200,size=84,step=92,green_last=True):
    for i,l in enumerate(lines): ax.text(66,y0+i*step,l,fontfamily=BB,fontsize=size,color=G if (green_last and i==len(lines)-1) else W,va='center')
    return y0+len(lines)*step
def cards(ax,items,y0,h=150,gap=24):
    for k,(t,s) in enumerate(items):
        y=y0+k*(h+gap); rb(ax,60,y,960,h,CARD); ax.add_patch(Rectangle((60,y),10,h,color=G))
        ax.text(100,y+h*0.36,t,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
        ax.text(100,y+h*0.68,s,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
def big3(fig,ax,y,items,fs=62):
    # numero en Bebas; si trae "|unidad", la unidad va en Barlow (Bebas es solo mayusculas)
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
        num,_,uni=big.partition('|')
        tx=ax.text(100,yy+60,num,fontfamily=BB,fontsize=fs,color=W,va='center')
        if uni:
            fig.canvas.draw(); bb=tx.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
            ax.text(x2+14,yy+66,uni,fontfamily=B,fontweight='bold',fontsize=int(fs*0.52),color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k):
    fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)

# 1 PORTADA (con la comparación con Paraguay)
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · COLOMBIA')
for i,(l,c2,s) in enumerate([('CUÁNTO GANA',W,128),('UNA ESTACIÓN',W,128),('EN COLOMBIA',G,128)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=s,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['35 centavos de dólar por galón.','El gremio pide que le garanticen','al menos el 90 %.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'Son unos G. 580 por litro: hacé la misma',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'cuenta con el margen de tu estación.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL NUMERO
fig,ax=base(2,'EL NÚMERO')
y=title(ax,['LO QUE QUEDA','POR GALÓN'],y0=210,size=88,step=98)
big3(fig,ax,y,[('$ 1.155,09','Margen por galón de gasolina y de diésel'),('USD 0,35','Lo mismo en dólares, por galón'),('9 CENTAVOS','De dólar por litro: unos G. 580')],fs=68)
ax.text(70,1180,'Con eso se paga la nómina, la operación,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'el capital de trabajo y la inversión.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 QUE PIDEN
fig,ax=base(3,'QUÉ PIDEN')
y=title(ax,['UN PISO','DEL 90 %'],y0=210,size=100,step=108)
cards(ax,[('Precio base mínimo transitorio','Garantiza el 90 % del margen: unos $ 1.040 por galón'),
          ('Que el margen no se pierda','En el mercado abierto ni con intermediarios'),
          ('Todavía no es una norma','Los estudios están en el regulador, la CREG')],y+50,h=150,gap=26)
save(fig,3)

# 4 LA RED
fig,ax=base(4,'QUIÉNES SON')
y=title(ax,['UNA RED DE','DUEÑOS CHICOS'],y0=210,size=84,step=94)
big3(fig,ax,y,[('6.400 ESTACIONES','De 4.300 propietarios'),('86 %','De los dueños tiene una sola estación'),('68.035 EMPLEOS','En 980 municipios')],fs=66)
ax.text(70,1180,'Una estación promedio despacha',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'unos 212.000 litros por mes.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 LOS COSTOS
fig,ax=base(5,'LO QUE SE LLEVA EL COSTO')
y=title(ax,['UN TERCIO','ES PERSONAL'],y0=210,size=88,step=98)
cards(ax,[('35 % del margen es costo laboral','La estación abre las 24 horas'),
          ('El salario mínimo subió más de 23 %','Uno de cuatro cambios en cuatro años'),
          ('Jornada de 42 horas y más recargos','En domingos, feriados y de noche')],y+50,h=150,gap=26)
save(fig,5)

# 6 COMO LO PIDEN
fig,ax=base(6,'CÓMO LO PIDEN')
y=title(ax,['UNIDOS Y','CON NÚMEROS'],y0=210,size=88,step=98)
cards(ax,[('Una sola entidad: Somos Uno','La formaron Comce y Fendipetróleo Nacional'),
          ('Estudios técnicos ante el regulador','No pidieron "más margen": pidieron un piso'),
          ('Un proyecto de ley','De política pública para el minorista')],y+50,h=150,gap=26)
save(fig,6)

# 7 CIERRE
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['HACÉ LA MISMA','CUENTA ACÁ'],y0=205,size=88,step=98)
cards(ax,[('En Paraguay el margen no es regulado','Lo define cada emblema, y Petropar el suyo'),
          ('Cuánto te queda por litro','Allá son unos G. 580'),
          ('Y qué parte se va en sueldos','Allá, más de un tercio')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
