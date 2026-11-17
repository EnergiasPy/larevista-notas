import sys, os, math; sys.path.insert(0,'/home/claude/chart')
from reel_lib import *
FR=((213,43,30),(255,255,255),(0,56,168))   # franja Paraguay
SC=[4.0,5.0,4.5,4.5,4.0]; T=sum(SC)
def seg(t):
    a=0
    for i,d in enumerate(SC):
        if t<a+d or i==len(SC)-1: return i,(t-a),d
        a+=d
def slide(f,i,k,x,y,w,h,big,sub,col=G,fs=108,delay=0.16,start=0.0):
    p=max(0.0,min(1.0,(k-start-delay*i)/0.5)); e=ease(p)
    if p<=0: return
    off=int((1-e)*90)
    f.rb(x+off,y,w,h,CARD); f.d.rectangle([x+off,y,x+off+11,y+h],fill=col)
    f.t(x+off+46,y+26,big,BB(fs),W); f.t(x+off+48,y+26+fs*0.94,sub,BS(34),M)
def draw(t):
    i,k,d=seg(t); f=Frame(FR)
    if i==0:
        # gancho: el numero esta en pantalla desde el primer cuadro
        f.t(60,170,'LA ESTACIÓN DEL FUTURO · PARAGUAY',BC(34),G)
        f.t(60,420,'EL AUTOGAS',BB(126),W,'ls')
        p=max(0.0,min(1.0,k/0.45)); e=ease(p)
        f.t(60,int(620+(1-e)*40),'CAE',BB(126),W,'ls')
        f.t(430,620,'11 %',BB(220),RD,'ls')
        if k>0.5:
            f.d.rectangle([62,700,62+int(150*ease(min(1,(k-0.5)/0.5))),708],fill=G)
            f.t(60,790,'EN LAS ESTACIONES',BBo(54),W)
            f.t(60,862,'DE SERVICIO',BBo(54),W)
        if k>1.5:
            f.rb(90,1010,900,190,CARD); f.d.rectangle([90,1010,101,1200],fill=G)
            f.t(136,1046,'18.823 t',BB(96),W)
            f.t(138,1148,'contra 21.232 t del año pasado',BS(34),M)
        f.sub('El autogas cayó 11 % en las estaciones')
    elif i==1:
        f.t(60,170,'ADÓNDE FUE EL GAS',BC(34),G)
        f.t(60,320,'NO SE VENDE',BB(118),W,'ls')
        f.t(60,450,'MENOS GAS',BB(118),G,'ls')
        f.t(60,540,'Cambió quién lo compra',BS(42),M)
        for j,(b,s2,c) in enumerate([('−11,3 %','Estaciones de servicio',RD),('+14,7 %','Industrias',G),('−1,9 %','Garrafas',M)]):
            slide(f,j,k,90,640+j*250,900,215,b,s2,col=c,fs=116,start=0.3)
        if k>2.6:
            f.t(540,1420,'El mercado total cayó sólo 2,5 %',BBo(44),W,'ma')
        f.sub('Las estaciones cayeron 11,3 %|y las industrias crecieron 14,7 %')
    elif i==2:
        f.t(60,170,'EL SURTIDOR PIERDE PESO',BC(34),G)
        f.t(60,340,'TRES PUNTOS',BB(118),W,'ls')
        f.t(60,470,'DE MERCADO',BB(118),G,'ls')
        p=max(0.0,min(1.0,(k-0.3)/1.6)); v=34.3-(34.3-31.2)*ease(p)
        f.t(540,760,nf(v,1)+' %',BB(240),W if p<1 else RD,'ma')
        f.t(540,980,'lo que pesa el surtidor en el GLP del país',BS(40),M,'ma')
        if k>2.1:
            f.rb(90,1120,900,160,CARD); f.d.rectangle([90,1120,101,1280],fill=G)
            f.t(136,1152,'LA INDUSTRIA PASÓ A 18,6 %',BBo(48),W)
            f.t(138,1222,'y antes pesaba 15,8 %',BS(34),M)
        f.sub('El surtidor pasó de 34,3 % a 31,2 %')
    elif i==3:
        f.t(60,170,'DE DÓNDE VIENE',BC(34),G)
        f.t(60,360,'EL 99 % DEL GAS',BB(112),W,'ls')
        f.t(60,490,'ES ARGENTINO',BB(112),G,'ls')
        p=max(0.0,min(1.0,(k-0.2)/1.0)); e=ease(p)
        f.rb(90,660,900,86,CARD,14)
        f.d.rounded_rectangle([90,660,90+max(86,int(900*0.992*e)),746],14,fill=G)
        f.t(126,678,'ARGENTINA',BBo(44),BG)
        if e>0.55: f.t(954,678,nf(99.2*e,1)+' %',BBo(44),BG if 90+900*0.992*e>900 else W,'ra')
        if k>0.9:
            f.t(540,900,'61.665 t',BB(160),W,'ma')
            f.t(540,1030,'de las 62.166 que entraron en nueve meses',BS(38),M,'ma')
        if k>2.3:
            f.rb(90,1120,900,160,CARD); f.d.rectangle([90,1120,101,1280],fill=RD)
            f.t(136,1152,'PARAGUAY NO PRODUCE GLP',BBo(48),W)
            f.t(138,1222,'lo importa todo',BS(34),M)
        f.sub('El 99,2 % del gas entra desde la Argentina')
    else:
        p=max(0.0,min(1.0,k/0.55)); e=ease(p)
        f.t(60,int(540+(1-e)*50),'EL GAS SE VA',BB(132),W,'ls')
        f.t(60,int(690+(1-e)*50),'A LA FÁBRICA',BB(132),G,'ls')
        if k>0.65:
            f.d.rectangle([62,790,212,798],fill=G)
            f.t(60,870,'La industria es el cliente',BBo(50),W)
            f.t(60,940,'que está creciendo.',BBo(50),W)
        if k>1.3:
            f.rb(90,1150,900,150,G,22); f.t(540,1192,'SEGUINOS',BB(80),BG,'ma')
            f.t(540,1370,'Nota completa en energiaslatam.com',BBo(40),W,'ma')
        f.sub('Seguinos para la noticia del sector|todos los días')
    f.foot(); return f.im
if __name__=='__main__':
    O='/home/claude/chart/reel/gl17'; os.makedirs(O,exist_ok=True)
    if sys.argv[1:] and sys.argv[1]=='check':
        for n,t in enumerate([0.3,2.0,3.6,5.2,7.2,8.8,10.5,12.3,14.0,16.0,18.2,20.5]): draw(t).save(f'{O}/chk{n:02d}.jpg',quality=90)
        print('check ok · duracion', T)
    else:
        N=int(T*30)
        for n in range(N): draw(n/30).save(f'{O}/f{n+1:05d}.jpg',quality=92)
        encode(O,'/home/claude/out/reel-gl17.mp4')
        print('listo',N,T)
