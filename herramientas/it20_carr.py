# Carrusel 1080x1350 · Paraguay · excedente de Itaipú · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/it20/'; os.makedirs(O,exist_ok=True)
ID='2026-11-20-cuando-se-acaba-excedente-itaipu-paraguay-2029'
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

# 1 PORTADA
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c2,s) in enumerate([('¿CUÁNDO SE ACABA',W,112),('EL EXCEDENTE',W,128),('DE ITAIPÚ?',G,128)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=s,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['La central calcula que Paraguay usará','toda su parte en meses de 2029 y 2030.','Antes, la fecha era 2034.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'Y la tarifa vence en 41 días,',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'con director nuevo.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

# 2 EL NUMERO
fig,ax=base(2,'EL NÚMERO')
y=title(ax,['PARAGUAY','CONSUME MÁS'],y0=210,size=88,step=98)
big3(fig,ax,y,[('24.121|GWh','Entregó Itaipú a la ANDE de enero a octubre'),('20.753|GWh','En el mismo período de 2025'),('+16,23 %','El salto en un año')],fs=68)
ax.text(70,1180,'Son 3.368 GWh más',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'que el año pasado.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

# 3 EL CAMBIO
fig,ax=base(3,'EL CÁLCULO NUEVO')
y=title(ax,['DE 2034','A 2029'],y0=210,size=100,step=108)
cards(ax,[('Antes: 5 % de crecimiento por año','Así se proyectaba el consumo paraguayo'),
          ('Ahora: once años de historia','El método que proponen Itaipú y ENBPar'),
          ('Resultado: toda la parte paraguaya','Usada en varios meses de 2029 y 2030')],y+50,h=150,gap=26)
save(fig,3)

# 4 LA PELEA
fig,ax=base(4,'LA DISCUSIÓN EN BRASIL')
y=title(ax,['DOS TECHOS','PARA PARAGUAY'],y0=210,size=84,step=94)
big3(fig,ax,y,[('7.000|MW medios','Propuesta de ENBPar e Itaipú'),('3.875|MW medios','Lo que piden los industriales brasileños'),('+21 %','Suba de precio que estiman allá para 2027')],fs=68)
ax.text(70,1180,'Si Paraguay usa más,',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'a Brasil le queda menos energía de Itaipú.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

# 5 CAMBIO DE MANDO
fig,ax=base(5,'MIENTRAS TANTO, EN LA CENTRAL')
y=title(ax,['DIRECTOR NUEVO,','TARIFA POR VENCER'],y0=210,size=76,step=86)
cards(ax,[('Hugo Zárate, director interino','Ingeniero, 37 años en Itaipú; falta el acuerdo del Senado'),
          ('El ministro Riquelme entra al Consejo','Coordina el trabajo técnico de la tarifa'),
          ('La tarifa vence el 31 de diciembre','Hoy es de USD 19,28 por kilovatio-mes')],y+50,h=150,gap=26)
save(fig,5)

# 6 CIERRE
fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['YA NO SOBRA','ENERGÍA'],y0=205,size=92,step=100)
cards(ax,[('Tu factura no cambia','La ANDE congeló su tarifa por un año'),
          ('La pregunta es la potencia','Si va a haber disponible en tu zona, y cuándo'),
          ('Por eso se licitan 640 MW','La generación nueva que salió a buscar la ANDE')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,6)
print('ok')
