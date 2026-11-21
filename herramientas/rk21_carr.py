# Carrusel 1080x1350 · Paraguay · Paraguay · ranking de octubre · 20/11/2026
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
import os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/rk21/'; os.makedirs(O,exist_ok=True)
ID='2026-11-21-ranking-ventas-combustibles-octubre-2026'
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





fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · DATOS DEL SECTOR · PARAGUAY')
for i,(l,c2) in enumerate([('QUIÉN VENDIÓ',W),('MÁS COMBUSTIBLE',W),('EN OCTUBRE',G)]):
    ax.text(66,300+i*140,l,fontfamily=BB,fontsize=128,color=c2,va='center')
ax.add_patch(Rectangle((70,740),140,7,color=G))
for i,l in enumerate(['Petropar lidera con 21,6 % del mercado.','El gasoil cayó 15 % en un mes','y las naftas se sostuvieron.']):
    ax.text(70,820+i*52,l,fontfamily=B,fontweight='semibold',fontsize=38,color=W,va='center')
ax.text(70,1022,'El ranking por emblema, con los datos',fontfamily=B,fontsize=30,color=M,va='center')
ax.text(70,1064,'del Ministerio de Industria y Comercio.',fontfamily=B,fontsize=30,color=M,va='center')
save(fig,1)

fig,ax=base(2,'EL MES')
y=title(ax,['SE VENDIÓ MENOS','QUE EN SEPTIEMBRE'],y0=210,size=84,step=94)
big3(fig,ax,y,[('300,5|millones de litros','Naftas y gasoil vendidos en octubre'),('−6,8 %','Contra septiembre de 2026'),('−8,2 %','Contra octubre de 2025')],fs=68)
ax.text(70,1180,'En el año, las ventas siguen 3 % arriba',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'del mismo período de 2025.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,2)

fig,ax=base(3,'EL RANKING')
y=title(ax,['LAS CINCO','QUE MÁS VENDIERON'],y0=210,size=84,step=94)
R5=[('PETROPAR','64,9','21,6 %'),('SHELL','50,6','16,8 %'),('PETROBRAS','31,7','10,6 %'),('COPETROL','26,3','8,8 %'),('PUMA','18,9','6,3 %')]
for k,(n,v,sh) in enumerate(R5):
    yy=y+40+k*128; rb(ax,60,yy,960,108,CARD); ax.add_patch(Rectangle((60,yy),10,108,color=G))
    ax.text(100,yy+56,f'{k+1}. {n}',fontfamily=BB,fontsize=52,color=W,va='center')
    ax.text(760,yy+56,v,fontfamily=BB,fontsize=52,color=W,va='center',ha='right'); ax.text(772,yy+62,'M L',fontfamily=B,fontweight='bold',fontsize=22,color=M,va='center')
    ax.text(990,yy+56,sh,fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='right')
ax.text(70,y+40+5*128+24,'Millones de litros y participación de mercado.',fontfamily=B,fontweight='semibold',fontsize=26,color=M,va='center')
save(fig,3)

fig,ax=base(4,'UN AÑO DESPUÉS')
y=title(ax,['SOLO PETROPAR','CRECIÓ'],y0=210,size=88,step=98)
big3(fig,ax,y,[('+16,9 %','Petropar, contra octubre de 2025'),('−8,5 %','Shell, la segunda del ranking'),('−26,4 %','Puma, la mayor caída entre las cinco primeras')],fs=68)
ax.text(70,1180,'Petropar pasó de 17 % a 21,6 %',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'del mercado en doce meses.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,4)

fig,ax=base(5,'POR PRODUCTO')
y=title(ax,['EL GASOIL','EXPLICA LA CAÍDA'],y0=210,size=88,step=98)
big3(fig,ax,y,[('−15,1 %','Gasoil tipo III: de 156,7 a 133 millones de litros'),('+2,3 %','Nafta de 90 octanos: 110,6 millones de litros'),('+1 %','Todas las naftas juntas, contra septiembre')],fs=68)
ax.text(70,1180,'Octubre fue el mes de la última suba',fontfamily=B,fontweight='bold',fontsize=30,color=W,va='center')
ax.text(70,1226,'del gasoil, antes de la rebaja del impuesto.',fontfamily=B,fontsize=27,color=M,va='center')
save(fig,5)

fig,ax=base(6,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['COMPARÁ','TU OCTUBRE'],y0=205,size=88,step=98)
cards(ax,[('¿Tu gasoil cayó menos de 15 %?','Te fue mejor que al promedio del mercado'),
          ('La nafta sostuvo el mes','El cliente particular siguió cargando'),
          ('Noviembre es la prueba','Con el gasoil G. 300 más barato, ¿vuelve el volumen?')],y+40,h=150,gap=24)
ax.text(70,1150,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=32,color=G,va='center')
ax.text(70,1205,'Seguinos para la noticia del sector todos los días.',fontfamily=B,fontweight='semibold',fontsize=27,color=W,va='center')
save(fig,6)
print('ok')
