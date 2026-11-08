import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/ue8/'; os.makedirs(O,exist_ok=True)
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






ID='2026-11-08-ueno-pagos-avance-deudas'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · SERVICIO')
for i,(l,c) in enumerate([('UENO:',W),('YA COBRARON',W),('CASI 1,2',G),('MILLONES',G)]):
    ax.text(66,280+i*130,l,fontfamily=BB,fontsize=118,color=c,va='center')
ax.add_patch(Rectangle((70,800),140,7,color=G))
for i,l in enumerate(['Qué pasa desde el lunes con','quienes tienen deudas']):
    ax.text(70,880+i*62,l,fontfamily=B,fontweight='bold',fontsize=46,color=W,va='center')
ax.text(70,1080,'Según los datos del Banco Central del Paraguay',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'EL AVANCE')
y=title(ax,['64 % DE LAS CUENTAS','YA COBRÓ'],size=80,step=88)
for k,(big,t) in enumerate([('1.197.000','cuentas pagadas en dos lotes (722.000 y 475.000)'),('670.000','cuentas que faltan, de 1.867.000 con saldo'),('G. 996.000 M','desembolsados: unos USD 168 millones')]):
    yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
    ax.text(100,yy+60,big,fontfamily=BB,fontsize=66,color=W,va='center')
    ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
save2(fig,2)
fig,ax=base(3,'DESDE EL LUNES 9')
y=title(ax,['COBRAN QUIENES','TIENEN DEUDAS'])
cards(ax,[('Se descuentan las deudas vencidas','Préstamos, sobregiros y tarjetas'),('Se paga el resto','Hasta 40 salarios mínimos: G. 121.760.000'),('Varias cuentas, un solo cálculo','La garantía es por persona, no por cuenta')],y+60,h=140)
save2(fig,3)
fig,ax=base(4,'LOS QUE FALTAN')
y=title(ax,['CUENTAS BLOQUEADAS','Y SIN OTRO BANCO'],size=80,step=88)
cards(ax,[('Cuentas bloqueadas','En revisión: lotes previstos lunes y martes'),('262.000 sin cuenta en otra entidad','Se les abre una en 15 entidades'),('Saldos sobre el anticipo','El resto depende de la liquidación del banco')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'CONSULTAS')
y=title(ax,['SOLO POR CANALES','OFICIALES'])
cards(ax,[('pagosacreditadosfgd@bcp.gov.py','Montos, cálculos o problemas con el pago'),('No hay que registrarse','Lo aclaró la Asociación de Bancos'),('Nadie puede "acelerar" el pago','No compartas claves ni entres a links')],y+60,h=140)
save2(fig,5)
fig,ax=base(6,None)
ax.imshow(np.array(logo),extent=(415,665,420,170),zorder=3)
for i,l in enumerate(['COMPARTILO CON','QUIEN TODAVÍA','NO COBRÓ']):
    ax.text(540,530+i*95,l,fontfamily=BB,fontsize=84,color=G if i==2 else W,va='center',ha='center')
ax.text(540,860,'Leé la nota completa en La Estación del Futuro',fontfamily=B,fontweight='bold',fontsize=32,color=W,va='center',ha='center')
rb(ax,240,930,600,96,G,48); ax.text(540,978,'LINK EN LA BIO',fontfamily=BB,fontsize=56,color=BG,va='center',ha='center')
ax.text(540,1110,'Información basada en datos oficiales del BCP',fontfamily=B,fontweight='semibold',fontsize=25,color=M,va='center',ha='center')
save2(fig,6)
print('ok')
