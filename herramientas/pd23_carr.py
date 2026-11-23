# Carrusel 1080x1350 · Paraguay · petróleo y dólar · 23/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/pd23/'; os.makedirs(O,exist_ok=True)
ID='2026-11-23-va-a-bajar-combustible-diciembre-petroleo-dolar'
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
for i,(l,c2,sz) in enumerate([('¿VA A BAJAR',W,128),('EL COMBUSTIBLE',W,118),('EN DICIEMBRE?',G,128)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=sz,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['El petróleo bajó 21 %,','pero el dólar volvió a subir.']):
    ax.text(70,820+i*54,l,fontfamily=B,fontweight='semibold',fontsize=40,color=W,va='center')
ax.text(70,1000,'Al costo en guaraníes llegó poco más',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1042,'de la mitad de esa baja.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'LOS DOS NÚMEROS')
y=title(ax,['UNO BAJA,','EL OTRO SUBE'],y0=210,size=88,step=98)
big3(fig,ax,y,[('USD 92,57','El Brent del viernes 20: 21 % menos que a fin de octubre'),('G. 6.390','El dólar del viernes 20, según el Banco Central'),('G. 6.200','Lo que valía el dólar diez días antes')],fs=68)
ax.text(70,1180,'El petróleo casi no se movió en diez días.',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'El dólar subió alrededor de 3 %.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'LA CUENTA EN GUARANÍES')
y=title(ax,['CUÁNTO CUESTA','UN BARRIL'],y0=210,size=88,step=98)
big3(fig,ax,y,[('G. 670.000','A fin de octubre'),('G. 575.000','El 11 de noviembre'),('G. 592.000','El 20 de noviembre: 3 % más que diez días antes')],fs=68)
ax.text(70,1180,'Cálculo propio y aproximado: Brent',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'por dólar del Banco Central.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,3)

fig,ax=base(4,'EL DATO')
y=title(ax,['EL DÓLAR SE COMIÓ','CASI LA MITAD'],y0=210,size=84,step=94)
big3(fig,ax,y,[('−21 %','Lo que bajó el petróleo desde fin de octubre'),('−12 %','Lo que bajó el barril medido en guaraníes'),('+3 %','Lo que subió ese barril en los últimos diez días')],fs=68)
save(fig,4)

fig,ax=base(5,'DICIEMBRE')
y=title(ax,['HAY ESPACIO,','PERO POCO'],y0=210,size=92,step=100)
cards(ax,[('A favor: tres semanas de petróleo en baja','Y el stock caro de octubre ya debería haberse renovado'),
          ('En contra: el dólar','Encarece cada compra de combustible importado'),
          ('El diésel ya bajó G. 300','Por la rebaja del impuesto, que vence el 31 de diciembre'),
          ('Petropar revisa precios para diciembre','Mantiene los actuales hasta el 30 de noviembre')],y+30,h=140,gap=20)
save(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['MIRÁ EL DÓLAR,','NO SOLO EL BARRIL'],y0=205,size=84,step=94)
cards(ax,[('No cuentes con una baja fuerte','Al costo en guaraníes llegó poco más de la mitad'),
          ('Fin de noviembre: comprá lo justo','Si hay ajuste, llegás sin sobrestock'),
          ('Anotá el 31 de diciembre','Sin prórroga, el diésel sube G. 340 en enero')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,6)
print('ok')
