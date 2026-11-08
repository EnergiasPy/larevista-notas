import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; NV='#0C1A29'; RD='#C0252D'; GR='#3A7D44'; MU='#4A5B6C'; SO='#F0F4F8'; GL='#8CC889'
def rb(ax,x,y,w,h,c,r=10): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',color=c,lw=0))
ID='2026-11-08-ueno-pagos-avance-deudas'; R='/home/claude/larevista-notas/img/'
fig=plt.figure(figsize=(16,10.67),dpi=100,facecolor='white'); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1600); ax.set_ylim(1067,0); ax.axis('off')
for i,c in enumerate(['#D52B1E','#FFFFFF','#0038A8']): ax.add_patch(Rectangle((0,i*6),1600,6,color=c))
ax.text(80,72,'SERVICIO · DEVOLUCIÓN DE DEPÓSITOS DE UENO BANK',fontfamily=B,fontweight='semibold',fontsize=20,color=GR,va='center')
ax.text(76,148,'YA COBRARON CASI 1,2 MILLONES DE CUENTAS',fontfamily=BB,fontsize=66,color=NV,va='center')
ax.text(80,214,'Cuentas con saldo para devolver: 1.867.000. Avance al 8 de noviembre de 2026',fontfamily=B,fontsize=23,color=MU,va='center')
ax.add_patch(Rectangle((80,240),80,5,color=RD))
x0,W,y0,H=80,1450,300,110; tot=1867000
segs=[('1.er lote',722000,GR),('2.º lote',475000,GL),('Faltan',670000,'#DCE3EA')]
x=x0
for lab,v,c in segs:
    w=W*v/tot; ax.add_patch(Rectangle((x,y0),w,H,color=c))
    ax.text(x+w/2,y0+H/2,f'{v:,}'.replace(',','.'),fontfamily=BB,fontsize=44,color='white' if c!='#DCE3EA' else NV,va='center',ha='center')
    ax.text(x+w/2,y0+H+30,lab,fontfamily=B,fontweight='bold',fontsize=22,color=NV,va='center',ha='center'); x+=w
ax.text(x0,y0-22,'64 % pagado',fontfamily=BB,fontsize=30,color=GR,va='center')
cal=[('LUNES 9',['Con deudas: se descuentan las vencidas','y se paga el resto hasta el tope']),('LUN 9 Y MAR 10',['Cuentas bloqueadas en revisión','y saldos consolidados por persona']),('AL FINAL',['262.000 sin cuenta en otra entidad:','se les abre una en 15 entidades'])]
for k,(d,t) in enumerate(cal):
    y=490+k*92; rb(ax,80,y,950,82,SO,8); ax.add_patch(Rectangle((80,y),10,82,color=GR))
    ax.text(108,y+41,d,fontfamily=BB,fontsize=30,color=GR,va='center')
    for j,ln in enumerate(t): ax.text(370,y+24+j*32,ln,fontfamily=B,fontweight='semibold',fontsize=20,color=NV,va='center')
rb(ax,1060,490,470,268,NV,8)
ax.text(1090,545,'DESEMBOLSADO',fontfamily=BB,fontsize=32,color='#AFC0D0',va='center')
ax.text(1090,605,'G. 996.000 M',fontfamily=BB,fontsize=56,color='#6DBB78',va='center')
ax.text(1090,650,'unos USD 168 millones',fontfamily=B,fontweight='semibold',fontsize=20,color='white',va='center')
ax.text(1090,700,'Consultas:',fontfamily=B,fontsize=18,color='#AFC0D0',va='center')
ax.text(1090,732,'pagosacreditadosfgd@bcp.gov.py',fontfamily=B,fontweight='bold',fontsize=19,color='white',va='center')
ax.add_patch(Rectangle((80,800),1450,1,color='#DCE3EA'))
ax.text(80,840,'Anticipo: hasta 40 salarios mínimos (G. 121.760.000). Cobertura total: 75 salarios mínimos por depositante y entidad.',fontfamily=B,fontweight='semibold',fontsize=19,color=NV,va='center')
ax.text(80,878,'Datos: Banco Central del Paraguay (8/11/2026). Nadie puede "acelerar" la devolución: no compartas claves ni entres a links.',fontfamily=B,fontsize=18,color=MU,va='center')
ax.add_patch(Rectangle((0,967),1600,100,color=NV))
ax.text(80,1017,'LA ESTACIÓN',fontfamily=BB,fontsize=40,color='white',va='center'); ax.text(294,1017,'DEL FUTURO',fontfamily=BB,fontsize=40,color='#6DBB78',va='center')
ax.text(1520,1017,'energiaslatam.com',fontfamily=B,fontweight='semibold',fontsize=24,color='white',va='center',ha='right')
fig.savefig('ue8-web.png',facecolor='white'); Image.open('ue8-web.png').convert('RGB').save(R+ID+'-1.jpg',quality=88)
from story import story
story(R+ID+'-1.jpg','Servicio',['UENO: YA COBRARON','CASI 1,2 MILLONES','¿Y LOS QUE TIENEN DEUDAS?'],ID,R+ID+'-story.jpg')
print('ok')
