#!/usr/bin/env python3
# reel_it18.py · reel de Itaipú para @energiaslatam · placas animadas + voz de Diego + logo
import sys, os, subprocess; sys.path.insert(0,'/home/claude/chart')
from reel_lib import *
from PIL import Image, ImageDraw

LOGO='/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png'
VOZ='/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/voz_itaipu.mp3'
FR=((213,43,30),(255,255,255),(0,56,168))      # franja Paraguay
# escenas alineadas con las pausas de la locución
SC=[6.96, 3.83, 4.31, 3.51, 5.81, 1.26, 2.90, 4.72, 3.92, 4.16, 3.11]
T=sum(SC)

def logo_redondo(px):
    lg=Image.open(LOGO).convert('RGBA')
    mk=Image.new('L',lg.size,0); ImageDraw.Draw(mk).ellipse((6,6,lg.size[0]-6,lg.size[1]-6),fill=255)
    lg.putalpha(mk); return lg.resize((px,px),Image.LANCZOS)
LG_CHICO=logo_redondo(96); LG_GRANDE=logo_redondo(330)

def seg(t):
    a=0
    for i,d in enumerate(SC):
        if t<a+d or i==len(SC)-1: return i,(t-a),d
        a+=d

def marca(f, kicker=None):
    f.im.paste(LG_CHICO,(56,70),LG_CHICO); f.d=ImageDraw.Draw(f.im)
    f.t(170,128,'ENERGÍAS',BB(48),W,'ls'); f.t(170,174,'LATAM',BB(48),G,'ls')
    if kicker: f.t(1020,150,kicker,BC(34),G,'rs')

def draw(t):
    i,k,d=seg(t); f=Frame(FR); marca(f, None if i==10 else ('ITAIPÚ' if i<6 else 'QUÉ SIGNIFICA PARA TU ESTACIÓN'))
    if i==0:
        f.t(60,430,'LA TARIFA',BB(118),W,'ls')
        f.t(60,560,'DE ITAIPÚ VENCE',BB(118),W,'ls')
        p=max(0.0,min(1.0,k/0.5)); e=ease(p)
        f.t(60,int(700+(1-e)*40),'EL 31 DE DICIEMBRE',BB(104),RD,'ls')
        if k>1.0:
            f.d.rectangle([62,770,62+int(150*ease(min(1,(k-1.0)/0.5))),778],fill=G)
        if k>3.4:
            f.rb(90,880,900,240,CARD); f.d.rectangle([90,880,101,1120],fill=G)
            f.t(136,938,'Y PARAGUAY TODAVÍA',BBo(50),W)
            f.t(136,1006,'NO PUSO SU NÚMERO',BBo(50),W)
            f.t(138,1078,'sobre la mesa',BS(36),M)
        f.sub('La tarifa de Itaipú vence|el 31 de diciembre')
    elif i==1:
        f.t(60,340,'LA TARIFA',BB(96),W,'ls'); f.t(60,450,'DE HOY',BB(96),G,'ls')
        p=max(0.0,min(1.0,(k-0.2)/1.6)); v=19.28*ease(p)
        f.t(540,790,'US$ '+nf(v,2),BB(200),W if p<1 else G,'ms')
        f.t(540,900,'por kilovatio-mes',BS(46),M,'ms')
        if k>2.2:
            f.rb(90,1020,900,140,CARD); f.d.rectangle([90,1020,101,1160],fill=M)
            f.t(136,1058,'Acordada en 2024',BBo(44),W)
            f.t(138,1118,'para 2024, 2025 y 2026',BS(34),M)
        f.sub('Hoy se cobran US$ 19,28|por kilovatio-mes')
    elif i==2:
        f.t(60,340,'LO QUE LE DEJA',BB(88),W,'ls'); f.t(60,445,'AL PAÍS',BB(88),G,'ls')
        p=max(0.0,min(1.0,(k-0.2)/1.8)); v=1250*ease(p)
        f.t(540,740,'US$ '+nf(v,0),BB(170),G,'ms')
        f.t(540,850,'millones por año',BS(48),W,'ms')
        for j,(a1,b1) in enumerate([('650 M','inversión social'),('280 M','royalties'),('265 M','compensación')]):
            if k>1.6+j*0.25:
                x=70+j*320; f.rb(x,980,300,180,CARD); f.d.rectangle([x,980,x+10,1160],fill=G)
                f.t(x+28,1040,'US$ '+a1,BB(58),W,'ls'); f.t(x+30,1098,b1,BS(28),M,'ls')
        f.sub('Le deja al país US$ 1.250|millones por año')
    elif i==3:
        f.t(60,400,'BRASIL QUIERE',BB(104),W,'ls')
        p=max(0.0,min(1.0,k/0.5)); e=ease(p)
        f.t(60,int(520+(1-e)*40),'PAGAR MENOS',BB(104),RD,'ls')
        if k>0.9:
            f.d.rectangle([62,590,212,598],fill=G)
            f.rb(90,680,900,280,CARD); f.d.rectangle([90,680,101,960],fill=RD)
            f.t(136,748,'"CONSIDERABLEMENTE',BBo(46),W)
            f.t(136,812,'MENOR"',BBo(46),W)
            f.t(138,900,'dijo el director brasileño de la binacional',BS(32),M)
        f.sub('Brasil ya dijo que quiere|pagar considerablemente menos')
    elif i==4:
        f.t(60,320,'SI REFLEJA SÓLO',BB(80),W,'ls'); f.t(60,415,'LOS COSTOS',BB(80),G,'ls')
        p=max(0.0,min(1.0,(k-0.6)/2.4)); v=19.28-(19.28-9.0)*ease(p)
        col = W if p<1 else RD
        f.t(540,730,'US$ '+nf(v,2),BB(200),col,'ms')
        f.t(540,840,'por kilovatio-mes',BS(46),M,'ms')
        if k>3.4:
            f.rb(90,980,900,180,CARD); f.d.rectangle([90,980,101,1160],fill=RD)
            f.t(136,1040,'ENTRE US$ 8 Y US$ 10',BBo(48),W)
            f.t(138,1108,'es la estimación para 2027',BS(34),M)
        f.sub('La tarifa caería a|ocho o diez dólares')
    elif i==5:
        f.t(540,780,'LA MITAD',BB(200),RD,'ms')
        f.d.rectangle([430,860,650,872],fill=G)
        f.t(540,980,'de lo que se cobra hoy',BS(50),W,'ms')
        f.sub('La mitad')
    elif i==6:
        f.t(60,470,'¿Y ESO ES BUENO',BB(100),W,'ls')
        p=max(0.0,min(1.0,k/0.5)); e=ease(p)
        f.t(60,int(590+(1-e)*40),'O MALO PARA',BB(100),W,'ls')
        f.t(60,710,'TU ESTACIÓN?',BB(100),G,'ls')
        if k>1.2: f.d.rectangle([62,780,62+int(150*ease(min(1,(k-1.2)/0.5))),788],fill=G)
        f.sub('¿Y eso es bueno o malo|para tu estación?')
    elif i==7:
        f.t(60,340,'TU FACTURA',BB(96),W,'ls'); f.t(60,450,'NO CAMBIA MAÑANA',BB(88),G,'ls')
        if k>0.6:
            f.rb(90,600,900,260,CARD); f.d.rectangle([90,600,101,860],fill=G)
            f.t(136,668,'LA ANDE CONGELÓ',BBo(50),W)
            f.t(136,736,'SU TARIFA POR UN AÑO',BBo(50),W)
            f.t(138,812,'Lo anunció este mes',BS(34),M)
        if k>2.8:
            f.t(60,980,'Lo que se define ahora es el costo',BBo(42),W,'ls')
            f.t(60,1040,'de la energía del país desde 2027.',BBo(42),W,'ls')
        f.sub('Tu factura no cambia mañana:|la ANDE congeló su tarifa')
    elif i==8:
        f.t(60,340,'PERO SI ITAIPÚ',BB(92),W,'ls'); f.t(60,445,'COBRA MENOS...',BB(92),RD,'ls')
        p=max(0.0,min(1.0,(k-0.3)/0.8)); e=ease(p)
        if p>0:
            off=int((1-e)*80)
            f.rb(90+off,620,900,280,CARD); f.d.rectangle([90+off,620,101+off,900],fill=RD)
            f.t(136+off,694,'EL ESTADO RECIBE',BBo(50),W)
            f.t(136+off,762,'MENOS PARA OBRAS',BBo(50),W)
            f.t(138+off,844,'De esos US$ 1.250 millones al año',BS(34),M)
        f.sub('Si Itaipú cobra menos, el Estado|recibe menos para obras')
    elif i==9:
        f.t(60,320,'Y PARTE DE',BB(92),W,'ls'); f.t(60,425,'ESAS OBRAS ES...',BB(92),W,'ls')
        p=max(0.0,min(1.0,(k-0.4)/0.9)); e=ease(p)
        if p>0:
            f.t(540,int(700+(1-e)*40),'LA RED',BB(150),G,'ms')
            f.t(540,850,'ELÉCTRICA',BB(150),G,'ms')
        if k>2.2:
            f.rb(90,980,900,180,CARD); f.d.rectangle([90,980,101,1160],fill=G)
            f.t(136,1040,'LA QUE NECESITÁS',BBo(48),W)
            f.t(138,1108,'para ampliar tu estación',BS(34),M)
        f.sub('Y parte de esas obras es la red|eléctrica que necesitás')
    else:
        p=max(0.0,min(1.0,k/0.6)); e=ease(p)
        f.im.paste(LG_GRANDE,(375,int(380+(1-e)*30)),LG_GRANDE); f.d=ImageDraw.Draw(f.im)
        f.t(540,880,'SEIS SEMANAS',BB(130),W,'ms')
        f.t(540,1010,'PARA CERRAR',BB(130),G,'ms')
        if k>0.9:
            f.d.rectangle([430,1070,650,1080],fill=G)
            f.t(540,1190,'Nota completa en energiaslatam.com',BBo(44),W,'ms')
            f.t(540,1260,'Seguinos para la noticia del sector',BS(36),M,'ms')
        f.sub(None)
    f.foot(); return f.im

if __name__=='__main__':
    O='/home/claude/chart/reel/it18'; os.makedirs(O,exist_ok=True)
    if sys.argv[1:] and sys.argv[1]=='check':
        for n,t in enumerate([1.0,8.5,12.5,16.5,22.5,25.0,27.5,31.0,35.0,39.5,42.5]): draw(t).save(f'{O}/chk{n}.jpg',quality=90)
        print('check ok · duración', round(T,2))
    else:
        N=int(T*30)
        for n in range(N): draw(n/30).save(f'{O}/f{n+1:05d}.jpg',quality=92)
        encode(O,'/home/claude/out/reel-it18-mudo.mp4')
        subprocess.run(['ffmpeg','-y','-v','error','-i','/home/claude/out/reel-it18-mudo.mp4','-i',VOZ,'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart','/home/claude/out/reel-itaipu.mp4'],check=True)
        print('video', N, round(T,2))
