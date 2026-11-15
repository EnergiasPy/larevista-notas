import sys, os, math; sys.path.insert(0,'/home/claude/chart')
from reel_lib import *
FR=((117,170,219),(255,255,255),(117,170,219))   # franja Argentina
SC=[4.0,5.0,5.0,5.5,4.0]; T=sum(SC)
def seg(t):
    a=0
    for i,d in enumerate(SC):
        if t<a+d or i==len(SC)-1: return i,(t-a),d
        a+=d
def slide(f,i,k,n,x,y,w,h,big,sub,col=G,fs=112,delay=0.18):
    p=max(0.0,min(1.0,(k-delay*i)/0.55)); e=ease(p)
    if p<=0: return
    off=int((1-e)*90)
    f.rb(x+off,y,w,h,CARD); f.d.rectangle([x+off,y,x+off+11,y+h],fill=col)
    f.t(x+off+46,y+28,big,BB(fs),W); f.t(x+off+48,y+28+fs*0.92,sub,BS(34),M)
def draw(t):
    i,k,d=seg(t); f=Frame(FR)
    if i==0:
        f.t(60,170,'LA ESTACIÓN DEL FUTURO · ARGENTINA',BC(34),G)
        for j,(l,c) in enumerate([('EL BARRIL CAYÓ',W),('US$ 20',G),('EN DOS SEMANAS',W)]):
            p=max(0.0,min(1.0,(k-0.12*j)/0.5)); e=ease(p)
            if p<=0: continue
            f.d.text((60,int(420+j*185+(1-e)*60)),l,font=BB(150 if j==1 else 118),fill=c,anchor='ls')
        p=max(0.0,min(1.0,(k-0.6)/0.6))
        if p>0:
            f.d.rectangle([62,1000,62+int(150*ease(p)),1008],fill=G)
            f.t(60,1070,'Y EL SURTIDOR ARGENTINO',BBo(52),W); f.t(60,1140,'NO SE MOVIÓ',BBo(52),W)
        f.sub('El barril se desplomó más de US$ 20|en dos semanas')
    elif i==1:
        f.t(60,170,'EL PETRÓLEO BRENT',BC(34),G)
        p=max(0.0,min(1.0,(k-0.4)/2.2)); v=118-(118-89.22)*ease(p)
        f.t(540,560,'US$ '+nf(v,2),BB(210),W if p<1 else G,'ma')
        f.t(540,840,'por barril',BS(44),M,'ma')
        f.rb(90,1000,900,130,CARD); f.d.rectangle([90,1000,101,1130],fill=M)
        f.t(136,1028,'US$ 118  ·  hace dos semanas',BBo(44),W)
        if k>2.3:
            f.rb(90,1160,900,130,CARD); f.d.rectangle([90,1160,101,1290],fill=G)
            f.t(136,1188,'US$ 89,22  ·  martes 10 de noviembre',BBo(44),W)
        f.sub('Pasó de US$ 118 a US$ 89,22|el barril')
    elif i==2:
        f.t(60,170,'EN EL SURTIDOR · MISIONES',BC(34),G)
        f.t(60,300,'SUBIÓ 1 %',BB(130),W); f.t(60,440,'EN NOVIEMBRE',BB(130),G)
        for j,(b,s2) in enumerate([('$ 2.275','la nafta súper por litro'),('$ 2.479','el gasoil común por litro'),('$ 2.685','el gasoil premium por litro')]):
            slide(f,j,k,3,90,640+j*230,900,200,b,s2)
        f.sub('En Misiones la nafta súper está|a $ 2.275 el litro')
    elif i==3:
        f.t(60,170,'LA FRONTERA',BC(34),G)
        f.t(60,300,'EL LITRO',BB(130),W); f.t(60,440,'EN DÓLARES',BB(130),G)
        f.t(330,640,'MISIONES',BBo(34),M,'ma'); f.t(790,640,'PARAGUAY',BBo(34),G,'ma')
        for j,(p,a1,b1) in enumerate([('DIÉSEL COMÚN','US$ 1,58','US$ 1,45'),('NAFTA SÚPER / 93','US$ 1,45','US$ 1,16')]):
            pr=max(0.0,min(1.0,(k-0.2*j)/0.55)); e=ease(pr)
            if pr<=0: continue
            y=700+j*300; off=int((1-e)*90)
            f.rb(90+off,y,900,250,CARD); f.d.rectangle([90+off,y,101+off,y+250],fill=G)
            f.t(136+off,y+28,p,BBo(40),M)
            f.t(330+off,y+100,a1,BB(88),W,'ma'); f.t(790+off,y+100,b1,BB(88),G,'ma')
        f.sub('El diésel común: US$ 1,58 en Misiones|y US$ 1,45 en Paraguay')
    else:
        p=max(0.0,min(1.0,k/0.6)); e=ease(p)
        f.t(60,int(520+(1-e)*50),'LA BRECHA',BB(140),W); f.t(60,int(680+(1-e)*50),'SE ABRIÓ',BB(140),G)
        if k>0.7:
            f.d.rectangle([62,860,212,868],fill=G)
            f.t(60,930,'Paraguay bajó el diésel.',BBo(50),W)
            f.t(60,1000,'La Argentina, no.',BBo(50),W)
        if k>1.4:
            f.rb(90,1180,900,150,G,22); f.t(540,1222,'SEGUINOS',BB(80),BG,'ma')
            f.t(540,1390,'Nota completa en energiaslatam.com',BBo(40),W,'ma')
        f.sub('Seguinos para la noticia del sector|todos los días')
    f.foot(); return f.im
if __name__=='__main__':
    O='/home/claude/chart/reel/ar15'; os.makedirs(O,exist_ok=True)
    if sys.argv[1:] and sys.argv[1]=='check':
        for n,t in enumerate([1.2,3.0,6.8,8.5,11.0,13.0,16.0,18.5,21.5]): draw(t).save(f'{O}/chk{n}.jpg',quality=90)
        print('check ok', T)
    else:
        N=int(T*30)
        for n in range(N): draw(n/30).save(f'{O}/f{n+1:05d}.jpg',quality=92)
        encode(O,'/home/claude/out/reel-ar15.mp4')
        print('listo',N,T)
