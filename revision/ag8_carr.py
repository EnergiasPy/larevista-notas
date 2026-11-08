import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ag8/'; os.makedirs(O,exist_ok=True)
N=6
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






ID='2026-11-08-alliana-agenda-combustibles'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGULACIÓN')
for i,(l,c) in enumerate([('COMBUSTIBLES:',W),('LA AGENDA',W),('QUE HEREDA',G),('ALLIANA',G)]):
    ax.text(66,280+i*130,l,fontfamily=BB,fontsize=118,color=c,va='center')
ax.add_patch(Rectangle((70,800),140,7,color=G))
for i,l in enumerate(['Las decisiones que tocan al','surtidor y cuándo vencen']):
    ax.text(70,880+i*62,l,fontfamily=B,fontweight='bold',fontsize=46,color=W,va='center')
ax.text(70,1080,'Diésel, petróleo, dólar y biodiésel',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'EL NUEVO GABINETE')
y=title(ax,['LOS PRIMEROS','NOMBRES'])
cards(ax,[('Interior: Ariel Martínez','Obras Públicas: Juan Carlos Baruja'),('Jefe de Gabinete: Rolando de Barros','Designado por Alliana el sábado 7'),('Economía: sigue Óscar Lovera','MIC: sin confirmación oficial todavía')],y+60,h=140)
save2(fig,2)
fig,ax=base(3,'DIÉSEL · PRECIO POR LITRO')
y=title(ax,['PETROPAR VS.','PRIVADOS'])
for k,(nm,a,b,d) in enumerate([('Diésel común (tipo III)','G. 9.285','G. 9.490','G. 205'),('Diésel especial (tipo I)','G. 11.395','G. 11.490','G. 95')]):
    yy=y+60+k*300; rb(ax,60,yy,960,270,CARD); ax.add_patch(Rectangle((60,yy),10,270,color=G))
    ax.text(100,yy+50,nm,fontfamily=B,fontweight='bold',fontsize=31,color=W,va='center')
    ax.text(100,yy+120,'Petropar',fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center'); ax.text(100,yy+175,a,fontfamily=BB,fontsize=64,color=G,va='center')
    ax.text(520,yy+120,'Mayoría de los privados',fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center'); ax.text(520,yy+175,b,fontfamily=BB,fontsize=64,color=W,va='center')
    ax.text(100,yy+238,f'Diferencia: {d} por litro',fontfamily=B,fontweight='bold',fontsize=24,color=RD,va='center')
ax.text(70,y+680,'Petropar mantiene sus precios hasta el 30 de noviembre',fontfamily=B,fontweight='semibold',fontsize=25,color=M,va='center')
save2(fig,3)
fig,ax=base(4,'LA CUENTA DE DICIEMBRE')
y=title(ax,['EL PETRÓLEO AYUDA,','EL DÓLAR NO'],size=80,step=88)
for k,(big,t) in enumerate([('USD 98,32','Brent al cierre del viernes 6: mayor caída semanal desde 2020'),('G. 6.450','dólar mayorista al cierre de la semana, tras subir cerca de 9 %'),('¿Baja o suba?','el resultado de esa cuenta define el precio de diciembre')]):
    yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
    ax.text(100,yy+60,big,fontfamily=BB,fontsize=66,color=W,va='center')
    ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=23,color=M,va='center')
save2(fig,4)
fig,ax=base(5,'EL CALENDARIO')
y=title(ax,['TRES FECHAS','PARA AGENDAR'])
cards(ax,[('30 de noviembre','Termina el congelamiento de Petropar'),('31 de diciembre','Vence la mezcla de biodiésel al 7 %'),('1 de enero de 2027','El cronograma del MIC la lleva al 8 %')],y+60,h=140)
save2(fig,5)
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['NOVIEMBRE CLARO,','DICIEMBRE ABIERTO'],size=80,step=88)
cards(ax,[('Noviembre: precio conocido','Planificá compras y caja sin sorpresas'),('Diciembre: sin apuestas','Evitá compras especulativas de stock'),('Enero: tanques en orden','Más biodiésel pide control de agua y filtros')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,6)
print('ok')
