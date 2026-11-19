# Reel vertical 1080x1920 · buses electricos San Lorenzo · fotos del MOPC + subtitulos quemados
import sys, os, subprocess, math
sys.path.insert(0,'/home/claude/chart')
from reel_lib import *
from PIL import Image, ImageDraw, ImageFilter

FR=((213,43,30),(255,255,255),(0,56,168))   # franja Paraguay
C='/home/claude/fotos_mopc/crop/'
OUT='/home/claude/reel19/'
os.makedirs(OUT+'frames',exist_ok=True)

# duraciones reales del audio si estan; si no, estimadas
def dur(p):
    try:
        r=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True)
        return float(r.stdout.strip())
    except Exception: return None
A1=OUT+'audio/t1.mp3'; A2=OUT+'audio/t2.mp3'
d1=dur(A1) if os.path.exists(A1) else None
d2=dur(A2) if os.path.exists(A2) else None
EST1, EST2 = 14.0, 22.0
GAP = 0.35   # pausa entre tandas, igual que en voz.mp3
D1 = d1 or EST1; D2 = (d2 or EST2) + GAP
# reparto dentro de cada tanda, proporcional al texto de cada escena
w1=[0.34,0.33,0.33]; w2=[0.26,0.24,0.26,0.24]
SC=[D1*x for x in w1]+[D2*x for x in w2]
T=sum(SC)

def seg(t):
    a=0.0
    for i,d in enumerate(SC):
        if t<a+d or i==len(SC)-1: return i,(t-a),d
        a+=d

_cache={}
def foto(name, zoom=1.0, dx=0.5, dy=0.42):
    """foto escalada para cubrir 1080x1920, recorte centrado en (dx,dy)"""
    key=(name,round(zoom,3),dx,dy)
    if key in _cache: return _cache[key]
    im=Image.open(C+name).convert('RGB')
    s=max(1080/im.width, 1920/im.height)*zoom
    im=im.resize((max(1080,int(im.width*s)),max(1920,int(im.height*s))),Image.LANCZOS)
    x=int((im.width-1080)*dx); y=int((im.height-1920)*dy)
    im=im.crop((x,y,x+1080,y+1920))
    _cache[key]=im; return im

def velo(im, top=0.0, bottom=0.78):
    """oscurece para que el texto se lea"""
    ov=Image.new('L',(1080,1920),0); d=ImageDraw.Draw(ov)
    for y in range(1920):
        f=y/1920.0
        a=int(235*max(0.0,min(1.0,(f-top)/0.55))**1.5) if f>top else 0
        a=max(a, int(215*max(0.0,min(1.0,(f-bottom)/0.22))))
        a=max(a, 70)
        d.line([(0,y),(1080,y)],fill=min(238,a))
    base=Image.new('RGB',(1080,1920),(8,18,34))
    return Image.composite(base, im, ov)

class PFrame(Frame):
    def __init__(s, franja, bg=None):
        if bg is None:
            Frame.__init__(s,franja); return
        s.im=bg.copy(); s.d=ImageDraw.Draw(s.im)
        for i,c in enumerate(franja): s.d.rectangle([0,i*9,1080,i*9+9],fill=c)
    def sub(s,txt):
        # subtitulos mas grandes que los de reel_lib: se leen en el celular sin sonido
        if not txt: return
        f=BBo(52); lines=txt.split('|')
        h=len(lines)*70+34; y0=1690-h
        wmax=max(s.d.textlength(l,font=f) for l in lines)
        s.rb(540-wmax/2-34,y0,wmax+68,h,(8,18,34),18)
        for i,l in enumerate(lines): s.t(540,y0+26+i*70,l,f,W,'ma')

def kicker(f,txt): f.t(60,150,txt,BC(34),G)

def draw(t):
    i,k,d=seg(t)
    # --- 1 GANCHO: foto estacion + numero grande desde el primer cuadro
    if i==0:
        z=1.0+0.045*(k/d)
        f=PFrame(FR,velo(foto('c1.jpg',zoom=z),top=0.30))
        kicker(f,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
        f.t(60,980,'SEIS CARGADORES',BB(104),W)
        p=max(0.0,min(1.0,k/0.45)); e=ease(p)
        f.t(60,int(1110+(1-e)*40),'DE 180',BB(150),W)
        f.t(474,1178,'kW',BBo(76),G)
        if k>0.55:
            f.d.rectangle([62,1300,62+int(170*ease(min(1,(k-0.55)/0.5))),1310],fill=G)
        f.sub('Seis cargadores de 180 kilovatios.')
    # --- 2 EL 1.500
    elif i==1:
        f=PFrame(FR,velo(foto('c1.jpg',zoom=1.10,dx=0.62),top=0.26))
        kicker(f,'LA BASE DE SAN LORENZO')
        p=max(0.0,min(1.0,k/0.5)); e=ease(p)
        f.t(60,int(900+(1-e)*50),'1.500',BB(230),W)
        f.t(640,968,'kW',BBo(96),G)
        if k>0.5:
            f.t(60,1190,'DE INFRAESTRUCTURA',BBo(56),W)
            f.t(60,1262,'ELÉCTRICA, EN UN SOLO PREDIO',BBo(56),W)
        f.sub('Y 1.500 kW de infraestructura,|en una sola base, para 30 colectivos.')
    # --- 3 DONDE
    elif i==2:
        f=PFrame(FR,velo(foto('c3.jpg',zoom=1.04+0.04*(k/d),dy=0.5),top=0.34))
        kicker(f,'DÓNDE')
        f.t(60,1080,'PREDIO DEL MOPC',BB(118),W)
        f.t(60,1200,'SAN LORENZO',BB(118),G)
        f.sub('Es el predio del MOPC en San Lorenzo.')
    # --- 4 EL GIRO: 60 km
    elif i==3:
        f=PFrame(FR,velo(foto('c2.jpg',zoom=1.02+0.05*(k/d),dx=0.42,dy=0.35),top=0.30))
        kicker(f,'PERO')
        p=max(0.0,min(1.0,k/0.45)); e=ease(p)
        f.t(60,int(980+(1-e)*44),'60',BB(290),RD)
        f.t(330,1070,'km',BBo(110),W)
        if k>0.5:
            f.t(60,1290,'DE AUTONOMÍA',BBo(58),W)
        f.sub('Pero el número que importa es otro:|60 kilómetros de autonomía.')
    # --- 5 POR ESO CARGA DE DIA
    elif i==4:
        f=PFrame(FR,velo(foto('c2.jpg',zoom=1.14,dx=0.55,dy=0.3),top=0.24))
        kicker(f,'POR ESO')
        f.t(60,900,'NO CARGA',BB(132),W)
        f.t(60,1030,'DE NOCHE',BB(132),W)
        f.t(60,1170,'CARGA EN RUTA',BB(132),G)
        f.sub('Con eso no alcanza para cargar de noche.|Se enchufa varias veces por día.')
    # --- 6 EL LIMITE
    elif i==5:
        f=PFrame(FR,velo(foto('c4.jpg',zoom=1.03+0.04*(k/d),dx=0.45),top=0.28))
        kicker(f,'LO QUE TE TOCA')
        f.t(60,980,'EL LÍMITE NO ES',BBo(64),W)
        f.t(60,1060,'LA ENERGÍA DEL PAÍS',BB(126),W)
        f.sub('El límite para poner un cargador|no es la energía del país.')
    # --- 7 CIERRE
    else:
        f=PFrame(FR,velo(foto('c4.jpg',zoom=1.12,dx=0.45),top=0.20))
        p=max(0.0,min(1.0,k/0.5)); e=ease(p)
        f.t(60,int(880+(1-e)*40),'ES EL',BB(118),W)
        f.t(60,1000,'ALIMENTADOR',BB(150),G)
        f.t(60,1150,'DE TU ESQUINA',BB(150),G)
        if k>0.9:
            f.rb(60,1330,960,150,(10,22,42),18)
            f.t(100,1360,'Nota completa en energiaslatam.com',BBo(44),W)
        f.sub('Es el alimentador de tu esquina.')
    f.foot()
    return f.im

if __name__=='__main__':
    fps=30; n=int(T*fps)
    print(f'duracion {T:.2f}s  ({"audio real" if d1 else "estimada"}) · {n} cuadros')
    for j in range(n):
        draw(j/fps).save(f'{OUT}frames/f{j:05d}.jpg',quality=90)
        if j%60==0: print(' ',j,end='',flush=True)
    print()
    encode(OUT+'frames',OUT+'reel_mudo.mp4',fps=fps)
    print('video mudo listo')
