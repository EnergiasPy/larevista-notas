# Carrusel 1080x1350 · Paraguay · Gulf llega a Paraguay · 24/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/gu24/'; os.makedirs(O,exist_ok=True)
ID='2026-11-24-gulf-paraguay-30-estaciones-anjor-lanzamiento'
N=6; BR=['#D52B1E','#FFFFFF','#0038A8']
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


fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2,sz) in enumerate([('GULF LLEGA',W,150),('A PARAGUAY',W,150),('CON 30 ESTACIONES',G,104)]):
    ax.text(66,300+i*150,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['Van a cambiar de emblema.','Es cerca del 1 % de la red del país.']):
    ax.text(70,820+i*54,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1000,'La presentación es hoy, martes 24,',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1042,'a las 18:00 en Asunción.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL ARRANQUE')
y=title(ax,['TREINTA BOCAS','EN LA PRIMERA ETAPA'],y0=210,size=88,step=98)
big3(fig,ax,y,[('30|estaciones','Cambios de emblema previstos, primera etapa'),('1 %','De una red de 2.880 estaciones habilitadas'),('0','Estaciones sin bandera hay en Paraguay')],fs=68)
ax.text(70,1180,'Cada estación que suma un emblema nuevo',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'sale de otro.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'QUIÉN ESTÁ DETRÁS')
y=title(ax,['GULF PONE LA MARCA,','ANJOR LA OPERACIÓN'],y0=210,size=74,step=86)
cards(ax,[('ANJOR PY SA tiene la licencia','Exclusiva para Paraguay, Uruguay y Bolivia'),
          ('Más de cinco décadas en combustibles','Transporte, venta mayorista y estaciones'),
          ('Una flota de más de 300 camiones','Se ocupa de la logística y el abastecimiento')],y+50,h=150,gap=26)
save(fig,3)

fig,ax=base(4,'EL PLAN')
y=title(ax,['PRIMERO,','LOS QUE YA ESTÁN'],y0=210,size=88,step=98)
cards(ax,[('Sumar operadores con estación propia','Es la prioridad, según su gerente general'),
          ('Construir estaciones nuevas','Queda como alternativa, caso por caso'),
          ('Sin meta de cantidad ni monto','Hablan de rentabilidad y de inversión progresiva'),
          ('1.000 estaciones en la región a 2030','El objetivo de Gulf Oil International')],y+30,h=140,gap=20)
save(fig,4)

fig,ax=base(5,'LO QUE FALTA SABER')
y=title(ax,['CUATRO','PREGUNTAS'],y0=210,size=100,step=108)
cards(ax,[('¿Dónde van a estar las primeras 30?','Zonas y ciudades'),
          ('¿En cuánto tiempo cambian la imagen?','El cronograma'),
          ('¿De dónde viene el combustible?','Origen y logística'),
          ('¿Qué le ofrecen al operador?','Contrato y condiciones')],y+30,h=140,gap=20)
save(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['UNA OPCIÓN MÁS','SOBRE LA MESA'],y0=205,size=88,step=98)
cards(ax,[('Mejora tu posición para negociar','Con ellos o con tu bandera actual'),
          ('Pedí la propuesta por escrito','Plazo, exclusividad, imagen y volumen'),
          ('Mirá quién te abastece','La logística pesa tanto como el cartel')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,6)
print('ok')
