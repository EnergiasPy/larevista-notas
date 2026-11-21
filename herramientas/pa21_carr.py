# Carrusel 1080x1350 · Paraguay · Paraguay · impuesto al diésel · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/pa21/'; os.makedirs(O,exist_ok=True)
ID='2026-11-21-cuanto-le-cuesta-al-estado-la-baja-del-diesel'
N=7; BR=['#D52B1E','#FFFFFF','#0038A8']
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
        num,_,uni=big.partition('|'); x0=100
        if num.startswith('BS '):
            p=ax.text(100,yy+66,'Bs',fontfamily=B,fontweight='bold',fontsize=int(fs*0.62),color=W,va='center')
            fig.canvas.draw(); bb=p.get_window_extent(); x0=ax.transData.inverted().transform((bb.x1,0))[0]+10; num=num[3:]
        tx=ax.text(x0,yy+60,num,fontfamily=BB,fontsize=fs,color=W,va='center')
        if uni:
            fig.canvas.draw(); bb=tx.get_window_extent(); x2=ax.transData.inverted().transform((bb.x1,0))[0]
            ax.text(x2+14,yy+66,uni,fontfamily=B,fontweight='bold',fontsize=int(fs*0.52),color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
def save(fig,k):
    fig.savefig(O+f'c{k}.png',facecolor=BG); Image.open(O+f'c{k}.png').convert('RGB').save(R+f'{ID}-c{k}.jpg',quality=92); plt.close(fig)



# 1 PORTADA
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · MERCADO Y PRECIOS · PARAGUAY')
for i,(l,c2,s) in enumerate([('CUÁNTO LE CUESTA',W,128),('AL ESTADO LA BAJA',W,128),('DEL DIÉSEL',G,128)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=s,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['US$ 9,5 millones en impuestos para','bajar G. 300 el litro de diésel.','La rebaja rige hasta el 31 de diciembre.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'La cuenta que conviene hacer en tu estación:',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'qué pasa el 1 de enero.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL MONTO
fig,ax=base(2,'EL MONTO')
y=title(ax,['LO QUE DEJA','DE COBRAR EL ESTADO'],y0=210,size=84,step=94)
big3(fig,ax,y,[('US$ 9,5|millones','Lo que el Estado renuncia a recaudar, según la DNIT'),('G. 59.500|millones','Al cambio de G. 6.260 por dólar: cifra aproximada'),('G. 340|por litro','Impuesto que queda; antes era G. 680')],fs=68)
ax.text(70,1180,'La medida alcanza solo al diésel tipo III.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'Las naftas quedan afuera del beneficio fiscal.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 COMO FUNCIONA
fig,ax=base(3,'CÓMO FUNCIONA')
y=title(ax,['NO SUBE NI BAJA','LA TASA, SOLO LA BASE'],y0=210,size=80,step=92)
cards(ax,[('La tasa del impuesto sigue en 18 %','Lo que cambia es la base sobre la que se aplica'),
          ('Base: de G. 3.777 a G. 1.888','Por litro de diésel tipo III, según el decreto'),
          ('Decreto 7.229, publicado el 13/11','Rebaja vigente en Petropar y en la mayoría de los emblemas')],y+50,h=150,gap=26)
save(fig,3)

# 4 EL PRECIO
fig,ax=base(4,'EL PRECIO')
y=title(ax,['EL DIÉSEL COMÚN','CAYÓ G. 300'],y0=210,size=88,step=98)
big3(fig,ax,y,[('G. 8.985|por litro','Diésel común en Shell y Petropar, con IVA incluido'),('G. 9.285|antes','Lo que costaba el diésel común en Shell'),('G. 8.940–8.990','Rango del diésel común en el mercado')],fs=66)
ax.text(70,1180,'Las empresas dicen que la diferencia',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'de G. 40 por litro son gastos operativos.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 HASTA CUANDO
fig,ax=base(5,'¿HASTA CUÁNDO?')
y=title(ax,['EL 1 DE ENERO','SE ACABA LA BAJA'],y0=210,size=88,step=98)
cards(ax,[('Vigente hasta el 31/12/2026','Decreto 7.229: la base vuelve a la anterior el 1/1/2027'),
          ('Salvo que el Ejecutivo prorrogue','Si no hay nuevo decreto, el impuesto sube G. 340 por litro'),
          ('Petropar garantiza sus precios','Al menos hasta mediados o fines de enero')],y+50,h=150,gap=26)
save(fig,5)

# 6 QUIEN CONTROLA
fig,ax=base(6,'QUIÉN CONTROLA')
y=title(ax,['LA DNIT COBRA,','EL MIC CONTROLA'],y0=210,size=88,step=98)
cards(ax,[('La DNIT recauda el impuesto','No controla los precios en el surtidor'),
          ('El control de precios es del MIC','Ministerio de Industria y Comercio'),
          ('"Se busca bajar un bien básico"','Dijo el director de la DNIT al justificar la renuncia')],y+50,h=150,gap=26)
save(fig,6)

# 7 CIERRE
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['TRES COSAS','PARA REVISAR'],y0=205,size=88,step=98)
cards(ax,[('Pedí la lista nueva por escrito','Cambiá cartel y surtidores el mismo día'),
          ('El stock vendido hasta el viernes','Se compró con impuesto completo: hablalo con la distribuidora'),
          ('Anotá el 1 de enero','Si no hay prórroga, el impuesto sube G. 340 por litro')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,7)
print('ok')
