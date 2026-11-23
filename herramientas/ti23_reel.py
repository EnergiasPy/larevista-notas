# Reel vertical 1080x1920 · la tienda de la estacion · video de apoyo generado con IA (Google Flow) + voz Nico + subtitulos quemados
import sys, os, subprocess
sys.path.insert(0,'/home/claude/chart')
from reel_lib import *
from PIL import Image, ImageDraw
FR=((213,43,30),(255,255,255),(0,56,168))
OUT='/home/claude/reel23/'
def dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout.strip())
A=OUT+'audio/t.mp3'; TAIL=0.7
T=dur(A)+TAIL
# escenas cronometradas con las pausas reales de la voz: (inicio, clip, tramo del clip en s, dibujo)
# clips: 1 encomiendas · 2 pago de servicios · 3 cafe
SCN=[(0.0,2,(0.0,2.0),'q'),(4.45,1,(0.0,3.3),'a1'),(7.4,1,(3.3,8.0),'a2'),(10.1,2,(2.0,4.5),'b1'),(12.6,2,(4.5,8.0),'b2'),
     (15.8,3,(0.0,3.5),'c1'),(18.35,3,(3.5,8.0),'c2'),(20.65,0,(0,0),'m'),(23.2,0,(0,0),'z')]
def seg(t):
    for n in range(len(SCN)-1,-1,-1):
        if t>=SCN[n][0]:
            e=SCN[n+1][0] if n+1<len(SCN) else T
            return n,t-SCN[n][0],e-SCN[n][0]
_c={}
def fondo(n,k,d):
    _,c,(a,b),_k=SCN[n]
    if c==0: return Image.new('RGB',(1080,1920),BG)
    fr=min(192,max(1,int((a+(b-a)*min(1,k/d))*24)+1)); key=(c,fr)
    if key not in _c:
        if len(_c)>12: _c.clear()
        im=Image.open(f'{OUT}src{c}/v{fr:04d}.jpg').convert('RGB').resize((1080,1920),Image.BICUBIC)
        if c==3:
            sh=Image.new('RGB',(1080,1920),(8,18,34)); sh.paste(im.crop((0,430,1080,1920)),(0,0)); im=sh
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
def idea(f,num,l1,l2,e):
    f.t(60,int(900+(1-e)*40),num,BB(300),G)
    f.t(60,1210,l1,BB(124),W)
    if l2: f.t(60,1330,l2,BB(124),W)
def draw(t):
    n,k,d=seg(t); i=SCN[n][3]; f=PF(fondo(n,k,d)); e=ease(max(0.0,min(1.0,k/0.4)))
    if i=='q':
        kick(f,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
        f.t(60,int(960+(1-e)*40),'MÁS CLIENTES',BB(190),W); f.t(60,1140,'SIN TOCAR',BB(190),W); f.t(60,1320,'EL PRECIO',BB(190),G)
        f.sub('¿Cómo traer más clientes a tu estación|sin tocar el precio del surtidor?')
    elif i[0]=='a':
        kick(f,'EL NEGOCIO NO ES SOLO EL COMBUSTIBLE')
        idea(f,'1','PUNTO DE RETIRO','DE ENCOMIENDAS',e if i=='a1' else 1)
        f.sub('Uno: punto de retiro|de encomiendas.' if i=='a1' else 'Abrís muchas horas|y estás sobre el camino.')
    elif i[0]=='b':
        kick(f,'EL NEGOCIO NO ES SOLO EL COMBUSTIBLE')
        idea(f,'2','PAGO DE','SERVICIOS',e if i=='b1' else 1)
        f.sub('Dos: pago de servicios.' if i=='b1' else 'El que paga una factura|vuelve todos los meses.')
    elif i[0]=='c':
        kick(f,'EL NEGOCIO NO ES SOLO EL COMBUSTIBLE')
        idea(f,'3','CAFÉ Y','COMIDA LISTA',e if i=='c1' else 1)
        f.sub('Tres: café y comida lista.' if i=='c1' else 'Dos minutos|pasan a ser diez.')
    elif i=='m':
        kick(f,'LA CUENTA')
        f.t(60,int(700+(1-e)*40),'MÁS MOTIVOS',BB(190),W); f.t(60,880,'PARA ENTRAR,',BB(190),W); f.t(60,1060,'MÁS LITROS',BB(190),G)
        f.sub('Más motivos para entrar|son más litros.')
    else:
        f.t(60,int(740+(1-e)*40),'COMPARTILO',BB(190),W); f.t(60,920,'CON OTRO',BB(190),W); f.t(60,1100,'OPERADOR',BB(190),G)
        f.rb(60,1340,960,130,(10,22,42),18); f.t(100,1376,'energiaslatam.com',BBo(56),G)
        f.sub('Compartilo con otro operador.')
    f.t(1020,1770,'Video y voz generados con IA',BBo(24),M,'ra')
    f.foot(); return f.im
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='test':
        ims=[]
        for n,sc in enumerate(SCN):
            e=SCN[n+1][0] if n+1<len(SCN) else T
            ims.append(draw(sc[0]+(e-sc[0])*0.85).resize((270,480)))
        sh=Image.new('RGB',(270*9,480)); [sh.paste(x,(j*270,0)) for j,x in enumerate(ims)]; sh.save(OUT+'test.jpg'); print('test',round(T,2))
    else:
        fps=30; n=int(T*fps); print(f'duracion {T:.2f}s')
        os.makedirs(OUT+'frames',exist_ok=True)
        for j in range(n): draw(j/fps).save(f'{OUT}frames/f{j:05d}.jpg',quality=90)
        encode(OUT+'frames',OUT+'reel_mudo.mp4',fps=fps)
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',A,'-af',f'apad=pad_dur={TAIL}','-c:a','aac','-b:a','160k',OUT+'voz.m4a'],check=True)
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',OUT+'reel_mudo.mp4','-i',OUT+'voz.m4a','-map','0:v','-map','1:a','-c:v','copy','-c:a','copy','-shortest','-movflags','+faststart',OUT+'reel.tmp.mp4'],check=True)
        os.replace(OUT+'reel.tmp.mp4',OUT+'reel_tienda.mp4'); print('reel listo',round(T,2))
