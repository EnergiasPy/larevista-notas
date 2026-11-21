# Carrusel 1080x1350 · Paraguay · Argentina · cuánto gana una estación · 21/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ar21/'; os.makedirs(O,exist_ok=True)
ID='2026-11-21-cuanto-gana-estacion-de-servicio-argentina-margen'
N=7; BR=['#74ACDF','#FFFFFF','#74ACDF']
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


# 1 PORTADA
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · REGIÓN · ARGENTINA')
for i,(l,c2,sz) in enumerate([('CUÁNTO GANA',W,128),('UNA ESTACIÓN',W,128),('EN ARGENTINA',G,128)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['Cerca del 8 % de lo que marca','el surtidor. Y hacen falta 350.000','litros para cubrir los costos.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'Son unos G. 740 por litro: hacé la misma',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'cuenta con el margen de tu estación.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL NUMERO
fig,ax=base(2,'EL NÚMERO')
y=title(ax,['LO QUE QUEDA','POR LITRO'],y0=210,size=88,step=98)
big3(fig,ax,y,[('8 % A 8,5 %','Del precio del surtidor, según el gremio del nordeste'),('$ 182 A $ 193','Por litro de nafta súper a $ 2.275'),('12 CENTAVOS','De dólar por litro: unos G. 740')],fs=68)
ax.text(70,1180,'Con eso se pagan los sueldos, la energía,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'el mantenimiento y las tarjetas.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 VOLUMEN
fig,ax=base(3,'UN NEGOCIO DE VOLUMEN')
y=title(ax,['EL PISO','SE CORRIÓ'],y0=210,size=100,step=108)
cards(ax,[('Antes: 100.000 a 120.000 litros','Con eso había estaciones que se sostenían'),
          ('Hoy: unos 350.000 litros','Y apenas alcanza, según el gremio del nordeste'),
          ('366.000 litros por mes','El punto de equilibrio que calculó Cecha en 2022')],y+50,h=150,gap=26)
save(fig,3)

# 4 CADA LITRO RINDE MENOS
fig,ax=base(4,'CADA LITRO RINDE MENOS')
y=title(ax,['MÁS LITROS','PARA LO MISMO'],y0=210,size=84,step=94)
big3(fig,ax,y,[('−21,1 %','Valor real de la nafta súper contra diciembre de 2018'),('+26,7 %','Litros de más para igualar el ingreso de entonces'),('2 % A 3 %','Todo el descuento que puede dar sin perder')],fs=66)
ax.text(70,1180,'El margen es un porcentaje: si el precio',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'pierde contra la inflación, la estación también.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 EL VOLUMEN NO ACOMPAÑA
fig,ax=base(5,'LAS VENTAS')
y=title(ax,['Y EL VOLUMEN','NO ACOMPAÑA'],y0=210,size=88,step=98)
cards(ax,[('Septiembre: +1,96 % interanual','La primera suba después de siete meses de caídas'),
          ('La nafta súper volvió a caer: −2,17 %','La mejora vino del gasoil, que creció 6,29 %'),
          ('YPF vende cerca del 55 %','El margen se negocia con quien fija el precio')],y+50,h=150,gap=26)
ax.text(70,1226,'Datos: Secretaría de Energía de la Nación.',fontfamily=B,fontsize=24,color=M,va='center')
save(fig,5)

# 6 COMPARACION
fig,ax=base(6,'LA COMPARACIÓN')
y=title(ax,['POR LITRO,','EN GUARANÍES'],y0=210,size=88,step=98)
big3(fig,ax,y,[('G. 740','Argentina: un porcentaje del precio, sin regular'),('G. 580','Colombia: un margen fijo por galón, regulado'),('15 % A 17 %','Brasil, según la estimación del gremio argentino')],fs=66)
ax.text(70,1180,'¿Cuánto te deja tu emblema por litro?',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
save(fig,6)

# 7 CIERRE
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['HACÉ LA MISMA','CUENTA ACÁ'],y0=205,size=88,step=98)
cards(ax,[('Tu margen, en guaraníes por litro','Allá son unos G. 740'),
          ('Tu punto de equilibrio en litros','Cuánto necesitás vender antes de ganar'),
          ('En la frontera, el vecino no puede bajar','Tiene 2 % o 3 % de aire para descuentos')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
