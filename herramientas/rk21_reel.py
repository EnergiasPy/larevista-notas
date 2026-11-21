# Reel vertical 1080x1920 · ranking de ventas de octubre (MIC) · placas animadas + voz Nico + subtitulos quemados
import sys, os, subprocess
sys.path.insert(0,'/home/claude/chart')
from reel_lib import *
from PIL import Image, ImageDraw
FR=((213,43,30),(255,255,255),(0,56,168))
OUT='/home/claude/reel21b/'
def dur(p,est):
    try: return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout.strip())
    except Exception: return est
A1=OUT+'audio/t1.mp3'; A2=OUT+'audio/t2.mp3'; GAP=0.35; TAIL=0.8
REAL=os.path.exists(A1) and os.path.exists(A2)
D1=dur(A1,15.5); D2=dur(A2,16.5); O=D1+GAP; T=O+D2+TAIL
# inicios de escena: fracciones de cada tanda (se reemplazan por las pausas reales en CUT1/CUT2 si se definen)
CUT1=None; CUT2=None
c1=CUT1 or [0, D1*0.22, D1*0.55, D1*0.76, D1*0.88]
c2=CUT2 or [0, D2*0.24, D2*0.50, D2*0.64, D2*0.84]
SCN=[(c1[0],'q'),(c1[1],'r1'),(c1[2],'r2'),(c1[3],'r3'),(c1[4],'r5'),(O+c2[0],'y'),(O+c2[1],'g'),(O+c2[2],'n'),(O+c2[3],'p'),(O+c2[4],'m')]
def seg(t):
    for n in range(len(SCN)-1,-1,-1):
        if t>=SCN[n][0]:
            e=SCN[n+1][0] if n+1<len(SCN) else T
            return n,t-SCN[n][0],e-SCN[n][0]
class PF(Frame):
    def sub(s,txt):
        f=BBo(52); lines=txt.split('|'); h=len(lines)*70+34; y0=1690-h
        wmax=max(s.d.textlength(l,font=f) for l in lines)
        s.rb(540-wmax/2-34,y0,wmax+68,h,(8,18,34),18)
        for i,l in enumerate(lines): s.t(540,y0+26+i*70,l,f,W,'ma')
def kick(f,t): f.t(60,150,t,BC(34),G)
R=[('PETROPAR',64.9,'21,6 %'),('SHELL',50.6,'16,8 %'),('PETROBRAS',31.7,'10,6 %'),('COPETROL',26.3,'8,8 %'),('PUMA',18.9,'6,3 %')]
def ranking(f,nvis,k):
    kick(f,'RANKING DE OCTUBRE · DATOS DEL MIC')
    f.t(60,230,'QUIÉN VENDIÓ MÁS',BB(104),W); f.t(60,340,'COMBUSTIBLE',BB(104),G)
    for j,(n,v,sh) in enumerate(R[:nvis]):
        y=520+j*200; new=(j>=nvis-(2 if nvis==5 else 1)); p=ease(min(1,k/0.6)) if new else 1.0
        f.rb(60,y,960,170,CARD,18)
        f.t(90,y+18,f'{j+1}',BB(64),M); f.t(150,y+18,n,BB(64),W)
        f.t(990,y+24,sh,BBo(40),G,'ra')
        w=int(780*v/64.9*p); f.d.rectangle([90,y+104,90+max(w,4),y+146],fill=G if j==0 else (118,150,196))
        f.t(90+max(w,4)+16,y+100,nf(v*p,1),BB(48),W)
        tw=f.d.textlength(nf(v*p,1),font=BB(48)); f.t(90+max(w,4)+24+tw,y+116,'M L',BBo(24),M)
def draw(t):
    n,k,d=seg(t); i=SCN[n][1]; f=PF(FR); e=ease(max(0.0,min(1.0,k/0.4)))
    if i=='q':
        kick(f,'LA ESTACIÓN DEL FUTURO · PARAGUAY')
        f.t(60,int(700+(1-e)*40),'¿QUIÉN VENDIÓ',BB(150),W); f.t(60,850,'MÁS COMBUSTIBLE',BB(150),W); f.t(60,1000,'EN OCTUBRE?',BB(150),G)
        f.t(60,1200,'Datos del Ministerio de Industria y Comercio',BBo(40),M)
        f.sub('¿Quién vendió más combustible|en Paraguay en octubre?')
    elif i[0]=='r':
        ranking(f,int(i[1]),k)
        f.sub({'r1':'Primera, Petropar: 65 millones de litros,|casi 22 % del mercado.','r2':'Segunda, Shell,|con 50 millones y medio.','r3':'Tercera, Petrobras.','r5':'Después, Copetrol y Puma.'}[i])
    elif i=='y':
        kick(f,'UN AÑO DESPUÉS')
        f.t(60,560,'CONTRA OCTUBRE DE 2025',BBo(48),M)
        Y=[('PETROPAR','+16,9 %',G),('SHELL','−8,5 %',RD),('PETROBRAS','−13,7 %',RD),('COPETROL','−15,5 %',RD),('PUMA','−26,4 %',RD)]
        for j,(nm,v,col) in enumerate(Y):
            y=660+j*150; f.rb(60,y,960,126,CARD,18); f.t(100,y+26,nm,BB(72),W); f.t(980,y+26,v,BB(72),col,'ra')
        f.sub('De las cinco, solo Petropar|vendió más que hace un año.')
    elif i=='g':
        kick(f,'EL DATO DEL MES')
        f.t(60,640,'EL GASOIL CAYÓ',BB(150),W)
        f.t(60,int(800+(1-e)*50),'−15 %',BB(330),RD)
        f.t(60,1170,'EN UN SOLO MES',BB(110),W)
        f.t(60,1310,'Gasoil tipo III: de 156,7 a 133 millones de litros',BBo(38),M)
        f.sub('Y el dato del mes: el gasoil cayó|15 % en un solo mes.')
    elif i=='n':
        kick(f,'LAS NAFTAS')
        f.t(60,700,'LAS NAFTAS',BB(170),W); f.t(60,870,'SE SOSTUVIERON',BB(150),G)
        f.t(60,int(1060+(1-e)*40),'+1 %',BB(260),W)
        f.t(60,1350,'Contra septiembre',BBo(40),M)
        f.sub('Las naftas, en cambio, se sostuvieron.')
    elif i=='p':
        kick(f,'TU ESTACIÓN')
        f.t(60,int(740+(1-e)*40),'¿TE FUE MEJOR',BB(150),W); f.t(60,890,'O PEOR QUE',BB(150),W); f.t(60,1040,'AL MERCADO?',BB(150),G)
        f.sub('¿A tu estación le fue mejor|o peor que al mercado?')
    else:
        f.t(60,int(760+(1-e)*40),'EL RANKING',BB(170),W); f.t(60,930,'COMPLETO',BB(170),W)
        f.rb(60,1140,960,130,(10,22,42),18); f.t(100,1176,'energiaslatam.com',BBo(56),G)
        f.sub('El ranking completo, en energiaslatam.com')
    f.t(1020,1770,'Voz generada con IA · Datos: MIC',BBo(24),M,'ra')
    f.foot(); return f.im
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='test':
        ims=[]
        for n,sc in enumerate(SCN):
            e=SCN[n+1][0] if n+1<len(SCN) else T
            ims.append(draw(sc[0]+(e-sc[0])*0.9).resize((270,480)))
        sh=Image.new('RGB',(270*5,960)); [sh.paste(x,((j%5)*270,(j//5)*480)) for j,x in enumerate(ims)]; sh.save(OUT+'test.jpg'); print('test',round(T,2),'audio real' if REAL else 'estimado')
    else:
        assert REAL,'faltan los audios'
        fps=30; n=int(T*fps); os.makedirs(OUT+'frames',exist_ok=True)
        for j in range(n): draw(j/fps).save(f'{OUT}frames/f{j:05d}.jpg',quality=90)
        encode(OUT+'frames',OUT+'reel_mudo.mp4',fps=fps)
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',A1,'-i',A2,'-filter_complex',f'[0:a]apad=pad_dur={GAP}[a];[1:a]apad=pad_dur={TAIL}[b];[a][b]concat=n=2:v=0:a=1[o]','-map','[o]','-c:a','aac','-b:a','160k',OUT+'voz.m4a'],check=True)
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',OUT+'reel_mudo.mp4','-i',OUT+'voz.m4a','-map','0:v','-map','1:a','-c:v','copy','-c:a','copy','-shortest','-movflags','+faststart',OUT+'reel.tmp.mp4'],check=True)
        os.replace(OUT+'reel.tmp.mp4',OUT+'reel_ranking_octubre.mp4'); print('reel listo',round(T,2))
