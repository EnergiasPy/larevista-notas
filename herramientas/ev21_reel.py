# Reel vertical 1080x1920 · cliente electrico · video de apoyo generado con IA + voz Nico + subtitulos quemados
import sys, os, subprocess
sys.path.insert(0,'/home/claude/chart')
from reel_lib import *
from PIL import Image, ImageDraw
FR=((213,43,30),(255,255,255),(0,56,168))
OUT='/home/claude/reel21/'; 
def dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout.strip())
A1=OUT+'audio/t1.mp3'; A2=OUT+'audio/t2.mp3'; GAP=0.35; TAIL=0.7
O=dur(A1)+GAP; T=O+dur(A2)+TAIL
# escenas cronometradas con las pausas reales de la voz: (inicio, clip, tramo del clip en s, dibujo)
SCN=[(0.0,1,(0.0,3.0),'a'),(2.6,1,(3.0,6.5),'b'),(4.9,2,(0.5,5.5),'c'),(10.5,4,(4.0,6.0),'d'),(12.9,4,(6.0,8.0),'e'),
     (O+0.0,1,(3.0,8.0),'f'),(O+5.85,2,(5.0,8.0),'g'),(O+9.1,4,(0.0,4.0),'h'),(O+13.1,3,(0.0,4.5),'i'),
     (O+16.7,3,(4.5,8.0),'j'),(O+19.2,4,(4.0,6.0),'k'),(O+20.75,5,(0.5,4.0),'l'),(O+22.3,5,(4.0,8.0),'m')]
def seg(t):
    for n in range(len(SCN)-1,-1,-1):
        if t>=SCN[n][0]:
            e=SCN[n+1][0] if n+1<len(SCN) else T
            return n,t-SCN[n][0],e-SCN[n][0]
_c={}
def fondo(n,k,d):
    _,c,(a,b),_k=SCN[n]; fr=min(192,max(1,int((a+(b-a)*min(1,k/d))*24)+1)); key=(c,fr)
    if key not in _c:
        if len(_c)>12: _c.clear()
        im=Image.open(f'{OUT}src{c}/v{fr:04d}.jpg').convert('RGB').resize((1080,1920),Image.BICUBIC)
        _c[key]=velo(im)
    return _c[key]
_ov=None
def velo(im):
    global _ov
    if _ov is None:
        _ov=Image.new('L',(1080,1920),0); dd=ImageDraw.Draw(_ov)
        for y in range(1920):
            f=y/1920.0; a=70
            if f>0.30: a=max(a,int(232*min(1.0,(f-0.30)/0.42)**1.3))
            if f<0.12: a=max(a,int(170*(1-f/0.12)))
            dd.line([(0,y),(1080,y)],fill=min(236,a))
    return Image.composite(Image.new('RGB',(1080,1920),(8,18,34)),im,_ov)
class PF(Frame):
    def __init__(s,bg):
        s.im=bg.copy(); s.d=ImageDraw.Draw(s.im)
        for i,c in enumerate(FR): s.d.rectangle([0,i*9,1080,i*9+9],fill=c)
    def sub(s,txt):
        f=BBo(52); lines=txt.split('|'); h=len(lines)*70+34; y0=1690-h
        wmax=max(s.d.textlength(l,font=f) for l in lines)
        s.rb(540-wmax/2-34,y0,wmax+68,h,(8,18,34),18)
        for i,l in enumerate(lines): s.t(540,y0+26+i*70,l,f,W,'ma')
def kick(f,t): f.t(60,150,t,BC(34),G)
def nu(f,x,y,num,uni,fs,col=W,ucol=G,us=0.42):
    f.t(x,y,num,BB(fs),col); w=f.d.textlength(num,font=BB(fs)); f.t(x+w+18,y+int(fs*0.42),uni,BBo(int(fs*us)),ucol); 
def pick(k,d,subs):
    return subs[min(len(subs)-1,int(len(subs)*k/d))]
def draw(t):
    n,k,d=seg(t); i=SCN[n][3]; f=PF(fondo(n,k,d)); e=ease(max(0.0,min(1.0,k/0.4)))
    if i in 'ab':
        kick(f,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
        f.t(60,960 if i=='b' else int(960+(1-e)*40),'MEDIA HORA',BB(170),W); f.t(60,1120,'PARA CARGAR',BB(170),W)
        if i=='b': f.t(60,int(1300+(1-e)*30),'¿ESTÁ LISTA TU ESTACIÓN?',BB(92),G)
        f.sub('Media hora para cargar|un auto eléctrico.' if i=='a' else '¿Tu estación está lista|para ese cliente?')
    elif i=='c':
        kick(f,'CUÁNTO ESPERA EL CLIENTE')
        f.t(60,930,'CARGADOR RÁPIDO DE 150 kW',BBo(54),W)
        nu(f,60,int(1010+(1-e)*40),'12','minutos',300,W,G,0.30)
        f.sub('Con un cargador rápido de 150 kilovatios,|la espera es de unos doce minutos.')
    elif i in 'de':
        kick(f,'CUÁNTO ESPERA EL CLIENTE')
        f.t(60,900,'CON 60 kW',BBo(54),M); nu(f,60,960 if i=='e' else int(960+(1-e)*40),'30','minutos',190,W,G,0.36)
        if i=='e':
            f.t(60,1190,'CON 22 kW',BBo(54),M); f.t(60,int(1250+(1-e)*30),'MÁS DE UNA HORA',BB(120),RD)
        f.sub('Con uno de sesenta, media hora.' if i=='d' else 'Y con uno de veintidós,|más de una hora.')
    elif i in 'fg':
        kick(f,'CUÁNTO CUESTA')
        f.t(60,900,'UN PUNTO DE CARGA RÁPIDA',BBo(54),W)
        nu(f,60,970 if i=='g' else int(970+(1-e)*40),'G. 265','millones',230,W,G,0.34)
        if i=='g':
            f.t(60,1250,'Según un proyecto de la',BBo(44),M); f.t(60,1306,'Universidad Nacional de Caaguazú',BBo(44),M)
        f.sub('Instalar un punto de carga rápida|cuesta unos G. 265 millones,' if i=='f' else 'según un proyecto de la|Universidad Nacional de Caaguazú.')
    elif i=='h':
        kick(f,'LA CUENTA')
        nu(f,60,int(900+(1-e)*40),'5','recargas por día',260,W,G,0.26)
        if k>d*0.5: f.t(60,1200,'SE PAGA EN 5 AÑOS',BB(120),G)
        f.sub('Con cinco recargas por día,|se paga en cinco años.')
    elif i=='i':
        kick(f,'LA TIENDA SUMA')
        f.t(60,int(940+(1-e)*40),'LO QUE GASTA',BB(150),W); f.t(60,1085,'MIENTRAS ESPERA',BB(150),W); f.t(60,1240,'MEJORA LA CUENTA',BB(120),G)
        f.sub('Y lo que el cliente gasta|mientras espera mejora la cuenta.')
    elif i in 'jkl':
        kick(f,'ENTONCES')
        q={'j':('¿TENÉS','BUEN CAFÉ?'),'k':('¿QUÉ TAL ESTÁ','TU TIENDA?'),'l':('¿CÓMO ESTÁN','TUS BAÑOS?')}[i]
        f.t(60,int(1000+(1-e)*40),q[0],BB(160),W); f.t(60,1150,q[1],BB(160),G)
        f.sub({'j':'Entonces: ¿tenés buen café?','k':'¿Qué tal está tu tienda?','l':'¿Cómo están tus baños?'}[i])
    else:
        f.t(60,int(960+(1-e)*40),'LEÉ LA NOTA',BB(150),W); f.t(60,1110,'COMPLETA',BB(150),W)
        f.rb(60,1300,960,130,(10,22,42),18); f.t(100,1336,'energiaslatam.com',BBo(56),G)
        f.sub('La nota completa, en energiaslatam.com')
    f.t(1020,1770,'Video y voz generados con IA',BBo(24),M,'ra')
    f.foot(); return f.im
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='test':
        ims=[]
        for n,sc in enumerate(SCN):
            e=SCN[n+1][0] if n+1<len(SCN) else T
            ims.append(draw(sc[0]+(e-sc[0])*0.85).resize((270,480)))
        sh=Image.new('RGB',(270*7,960)); [sh.paste(x,((j%7)*270,(j//7)*480)) for j,x in enumerate(ims)]; sh.save(OUT+'test.jpg'); print('test',round(T,2))
    else:
        fps=30; n=int(T*fps); print(f'duracion {T:.2f}s')
        os.makedirs(OUT+'frames',exist_ok=True)
        for j in range(n): draw(j/fps).save(f'{OUT}frames/f{j:05d}.jpg',quality=90)
        encode(OUT+'frames',OUT+'reel_mudo.mp4',fps=fps)
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',A1,'-i',A2,'-filter_complex',f'[0:a]apad=pad_dur={GAP}[a];[1:a]apad=pad_dur={TAIL}[b];[a][b]concat=n=2:v=0:a=1[o]','-map','[o]','-c:a','aac','-b:a','160k',OUT+'voz.m4a'],check=True)
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',OUT+'reel_mudo.mp4','-i',OUT+'voz.m4a','-map','0:v','-map','1:a','-c:v','copy','-c:a','copy','-shortest','-movflags','+faststart',OUT+'reel.tmp.mp4'],check=True)
        os.replace(OUT+'reel.tmp.mp4',OUT+'reel_cliente_electrico.mp4'); print('reel listo')
