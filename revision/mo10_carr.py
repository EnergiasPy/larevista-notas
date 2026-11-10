import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image, ImageDraw
import numpy as np, os
plt.rcParams['text.parse_math']=False
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'; CARD='#17305A'; RD='#E2484F'
R='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/mo10/'; os.makedirs(O,exist_ok=True)
N=7
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
ID='2026-11-09-itaipu-tarifa-2027-acuerdo-operativo'
def save2(fig,k): save(fig,f'{ID}-c{k}')
def big3(ax,y,items,fs=62):
    for k,(big,t) in enumerate(items):
        yy=y+60+k*175; rb(ax,60,yy,960,150,CARD); ax.add_patch(Rectangle((60,yy),10,150,color=G))
        ax.text(100,yy+60,big,fontfamily=BB,fontsize=fs,color=W,va='center')
        ax.text(102,yy+118,t,fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
ID='2026-11-10-mopc-registro-autogeneracion-renovable'
def save2(fig,k): save(fig,f'{ID}-c{k}')
fig,ax=base(1,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
for i,(l,c) in enumerate([('¿GENERÁS TU',W),('PROPIA ENERGÍA?',W),('YA HAY',G),('REGISTRO',G)]):
    ax.text(66,280+i*142,l,fontfamily=BB,fontsize=104,color=c,va='center')
ax.add_patch(Rectangle((70,830),140,7,color=G))
for i,l in enumerate(['El MOPC habilitó la inscripción para','autogeneradores renovables de hasta 1 MW']):
    ax.text(70,905+i*62,l,fontfamily=B,fontweight='bold',fontsize=38,color=W,va='center')
ax.text(70,1095,'Quiénes, cómo y qué permite',fontfamily=B,fontweight='semibold',fontsize=27,color=M,va='center')
save2(fig,1)
fig,ax=base(2,'QUIÉNES SE INSCRIBEN')
y=title(ax,['HASTA 1 MW','DE POTENCIA'])
cards(ax,[('Autogeneración','Para consumo propio'),('Cogeneración','Industrias que aprovechan su proceso'),('Conectadas o aisladas','Solar, eólica, biomasa o geotérmica')],y+60,h=140)
save2(fig,2)
fig,ax=base(3,'LA VENTAJA')
y=title(ax,['REGISTRO,','NO LICENCIA'])
big3(ax,y,[('≤ 1 MW','alcanza con inscribirse en el registro'),('> 1 MW','requiere la autorización del MOPC'),('Res. 996/2026','la resolución que regula el registro')])
save2(fig,3)
fig,ax=base(4,'CÓMO SE HACE')
y=title(ax,['FORMULARIO','E INSTRUCTIVO'])
cards(ax,[('Portal del VMME','minasyenergia.mopc.gov.py'),('Modelos','Para personas físicas y para empresas'),('Consultas','(021) 414-9000 · de 7:00 a 15:00')],y+60,h=140)
save2(fig,4)
fig,ax=base(5,'QUÉ PERMITE EL RÉGIMEN')
y=title(ax,['VENDER LO','QUE SOBRA'])
big3(ax,y,[('ANDE','debe absorber los excedentes de hasta 1 MW'),('Costo medio','de generación de la ANDE para la solar'),('6 meses','balance en guaraníes: se devuelve la diferencia')],fs=58)
save2(fig,5)
fig,ax=base(6,'LA CUENTA · EJEMPLO 30 kWp')
y=title(ax,['¿SE','RECUPERA?'])
big3(ax,y,[('≈ G. 135 M','inversión (USD 700 por kW instalado)'),('≈ G. 17,8 M','de ahorro por año, a G. 406 por kWh'),('≈ 7,6 años','de recupero; los paneles duran hasta 25')],fs=58)
ax.text(70,y+600,'Ejemplo sin venta de excedentes, cuyo precio aún no se publicó.',fontfamily=B,fontweight='semibold',fontsize=24,color=M,va='center')
save2(fig,6)
fig,ax=base(7,'QUÉ SIGNIFICA PARA LA ESTACIÓN')
y=title(ax,['EL CANOPY','TAMBIÉN GENERA'])
cards(ax,[('Techos que ya existen','Playa, tienda y depósitos'),('¿Ya tenés paneles?','Registralos para operar en regla'),('Itaipú 2027 sin precio','Generar es una forma de protegerse')],y+60,h=140)
ax.text(540,1180,'Leé la nota completa en energiaslatam.com',fontfamily=B,fontweight='bold',fontsize=30,color=G,va='center',ha='center')
save2(fig,7)
print('ok')
