import sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch
from PIL import Image
for f in ['BebasNeue-Regular.ttf','Barlow-Regular.ttf','Barlow-SemiBold.ttf','Barlow-Bold.ttf','BarlowCondensed-Bold.ttf']: fm.fontManager.addfont(f)
BB='Bebas Neue'; B='Barlow'; BC='Barlow Condensed'; BG='#0F213D'; W='#F4F6F9'; M='#9FB3C8'; G='#76C46E'
def story(img_path,cat,titulo_lines,url_slug,out,franja=('#D52B1E','#FFFFFF','#0038A8')):
    fig=plt.figure(figsize=(10.8,19.2),dpi=100,facecolor=BG); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1080); ax.set_ylim(1920,0); ax.axis('off')
    for i,c in enumerate(franja): ax.add_patch(Rectangle((0,i*8),1080,8,color=c))
    im=Image.open(img_path).convert('RGB'); w,h=im.size; nh=int(920*h/w)
    total=(260+nh+90+len(titulo_lines)*82+40+400)-100   # alto del bloque desde el encabezado hasta el botón
    off=max(150,int((1920-(total+60))/2))-100           # centrado vertical, dejando ~240 px abajo para el sticker
    ax.text(80,140+off,'LA ESTACIÓN',fontfamily=BB,fontsize=58,color=W,va='center'); ax.text(388,140+off,'DEL FUTURO',fontfamily=BB,fontsize=58,color=G,va='center')
    ax.text(82,200+off,'NOTA NUEVA · '+cat.upper(),fontfamily=BC,fontweight='bold',fontsize=26,color=M,va='center')
    ax.imshow(im,extent=(80,1000,260+off+nh,260+off),zorder=2)
    y=260+off+nh+90
    for ln in titulo_lines:
        ax.text(80,y,ln,fontfamily=BB,fontsize=72,color=W,va='center'); y+=82
    y+=40
    # recuadro sin link escrito: título, manito centrada y espacio adentro para el sticker (pedido de Diego 6/11)
    ax.add_patch(FancyBboxPatch((80,y),920,400,boxstyle='round,pad=0,rounding_size=48',color=G,lw=0))
    ax.text(540,y+72,'LEÉ LA NOTA COMPLETA',fontfamily=BB,fontsize=62,color=BG,va='center',ha='center')
    mano=Image.open('/home/claude/chart/mano.png'); mh=80; mw=int(mano.width*mh/mano.height)
    ax.imshow(mano,extent=(540-mw/2,540+mw/2,y+125+mh,y+125),zorder=4)
    # y+215 a y+390: espacio libre dentro del recuadro para el sticker de link
    fig.savefig(out+'.png',facecolor=BG); Image.open(out+'.png').convert('RGB').save(out,quality=90)
if __name__=='__main__':
    story('/home/claude/larevista-notas/img/2026-10-26-cocinas-electricas-glp-1.jpg','Energía',['COCINAS ELÉCTRICAS:','¿MENOS GARRAFAS','EN LA ESTACIÓN?'],'2026-10-26-cocinas-electricas-glp','/home/claude/larevista-notas/img/2026-10-26-cocinas-electricas-glp-story.jpg')
