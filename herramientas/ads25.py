# Creativos para anuncios de la revista y del newsletter (1080x1350) + video "cómo inscribirse" (1080x1920)
import subprocess, math
from PIL import Image, ImageDraw, ImageFont
O='/home/claude/out/ads/'; LOGO='/home/claude/larevista-notas/site/logo-latam-v2-512.png'
NV='#0C1A29'; NV2='#14273B'; G='#6DBB78'; GD='#3A7D44'; W='#F4F6FA'; M='#AEB8C8'; RD='#C0252D'; BG='#F0F4F8'
BB=lambda z:ImageFont.truetype('BebasNeue-Regular.ttf',z); B=lambda z,w='SemiBold':ImageFont.truetype(f'Barlow-{w}.ttf',z); BC=lambda z:ImageFont.truetype('BarlowCondensed-Bold.ttf',z)
logo=Image.open(LOGO).convert('RGBA')
def base(w=1080,h=1350,k='LA ESTACIÓN DEL FUTURO'):
    im=Image.new('RGB',(w,h),NV); d=ImageDraw.Draw(im)
    d.rectangle([0,0,w,10],fill=G); d.text((66,60),k,font=BC(32),fill=G)
    lg=logo.resize((96,96)); im.paste(lg,(w-66-96,36),lg)
    return im,d
def cta(d,y,t,w=1080,x=66):
    f=B(40,'Bold'); tw=d.textlength(t,font=f); d.rounded_rectangle([x,y,x+tw+80,y+92],46,fill=G); d.text((x+40,y+46),t,font=f,fill=NV,anchor='lm')
def foot(d,h=1350,w=1080,t='energiaslatam.com/newsletter'):
    d.text((66,h-70),t,font=BC(36),fill=W); d.text((w-66,h-70),'Gratis',font=BC(36),fill=G,anchor='ra')
def card(d,x,y,w,h,title,sub,col=G):
    d.rounded_rectangle([x,y,x+w,y+h],14,fill=NV2); d.rectangle([x,y,x+8,y+h],fill=col)
    d.text((x+34,y+h/2-(22 if sub else 0)),title,font=B(36,'Bold'),fill=W,anchor='lm')
    if sub: d.text((x+34,y+h/2+26),sub,font=B(27,'Regular'),fill=M,anchor='lm')
def phone(im,x,y,w,h,draw_screen):
    d=ImageDraw.Draw(im); d.rounded_rectangle([x,y,x+w,y+h],56,fill='#05090F'); sx,sy,sw,sh=x+16,y+16,w-32,h-32
    sc=Image.new('RGB',(sw,sh),'white'); draw_screen(sc,ImageDraw.Draw(sc),sw,sh)
    mask=Image.new('L',(sw,sh),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,sw,sh],42,fill=255); im.paste(sc,(sx,sy),mask)
def form(sc,d,sw,sh,name='',mail='',pressed=False,done=False,cur=None,s=1.0):
    F=lambda z,w='SemiBold':B(int(z*s),w); p=int(40*s)
    d.rectangle([0,0,sw,int(84*s)],fill='#E9EEF3'); d.rounded_rectangle([p,int(18*s),sw-p,int(66*s)],int(24*s),fill='white'); d.text((p+int(20*s),int(42*s)),'energiaslatam.com/newsletter',font=F(24,'Regular'),fill='#4A5868',anchor='lm')
    y=int(120*s); d.text((p,y),'ENERGÍAS LATAM',font=BC(int(30*s)),fill=GD); y+=int(52*s)
    d.text((p,y),'Newsletter',font=BB(int(84*s)),fill=NV); y+=int(96*s)
    d.text((p,y),'Lo más importante del sector de',font=F(27,'Regular'),fill='#4A5868'); y+=int(36*s); d.text((p,y),'estaciones de servicio, en tu mail.',font=F(27,'Regular'),fill='#4A5868'); y+=int(64*s)
    if done:
        d.rounded_rectangle([p,y,sw-p,y+int(300*s)],int(18*s),fill='#E7F4EA'); d.text((sw/2,y+int(100*s)),'¡Listo!',font=BB(int(110*s)),fill=GD,anchor='mm'); d.text((sw/2,y+int(200*s)),'Ya estás en la lista.',font=F(34),fill=NV,anchor='mm'); return
    for lab,val,key in [('Nombre',name,'n'),('Tu email',mail,'m'),('Empresa o estación (opcional)','', 'e')]:
        d.text((p,y),lab,font=F(26,'Bold'),fill=NV); y+=int(40*s)
        d.rounded_rectangle([p,y,sw-p,y+int(76*s)],int(12*s),outline=GD if cur==key else '#C9D2DE',width=3 if cur==key else 2,fill='white')
        d.text((p+int(22*s),y+int(38*s)),val+('|' if cur==key else ''),font=F(30,'Regular'),fill=NV,anchor='lm'); y+=int(104*s)
    d.rounded_rectangle([p,y,sw-p,y+int(88*s)],int(14*s),fill=GD if pressed else '#3A7D44'); 
    if pressed: d.rounded_rectangle([p-6,y-6,sw-p+6,y+int(88*s)+6],int(18*s),outline=G,width=6)
    d.text((sw/2,y+int(44*s)),'Quiero recibirlo',font=F(34,'Bold'),fill='white',anchor='mm')
# 1 Newsletter: propuesta
im,d=base(); d.text((66,170),'LAS NOTICIAS DE',font=BB(112),fill=W); d.text((66,278),'LAS ESTACIONES,',font=BB(112),fill=W); d.text((66,386),'EN TU MAIL',font=BB(112),fill=G)
for i,(a,b) in enumerate([('Precios y mercado','Qué se mueve y por qué'),('Las notas, resumidas','Para leer en cinco minutos'),('Qué significa para tu estación','Lo que conviene revisar')]): card(d,66,560+i*128,560,108,a,b)
phone(im,680,520,340,640,lambda sc,dd,sw,sh:form(sc,dd,sw,sh,s=0.62))
d.text((66,960),'Lunes, jueves y sábados.',font=B(34,'Bold'),fill=W); cta(d,1030,'Sumate gratis'); foot(d); im.save(O+'01-newsletter.jpg',quality=92)
# 2 Serie cuánto gana
im,d=base(k='LA ESTACIÓN DEL FUTURO · REGIÓN'); d.text((66,170),'¿CUÁNTO GANA',font=BB(120),fill=W); d.text((66,286),'UNA ESTACIÓN',font=BB(120),fill=W); d.text((66,402),'DE SERVICIO?',font=BB(120),fill=G)
d.text((66,548),'Lo contamos país por país, con los números del sector.',font=B(34),fill=M)
for i,(a,b) in enumerate([('Argentina','8 % del surtidor'),('Chile','75 pesos por litro'),('Colombia','35 centavos por galón'),('Ecuador','12 centavos por galón'),('México','1,50 pesos brutos por litro de diésel')]): card(d,66,620+i*104,948,88,a,b)
d.text((66,1170),'Leé las notas en energiaslatam.com',font=B(36,'Bold'),fill=G); foot(d,t='energiaslatam.com'); im.save(O+'02-cuanto-gana.jpg',quality=92)
# 3 Datos Paraguay
im,d=base(k='LA ESTACIÓN DEL FUTURO · PARAGUAY'); d.text((66,170),'LOS NÚMEROS',font=BB(120),fill=W); d.text((66,286),'DEL SURTIDOR',font=BB(120),fill=G)
for i,(n,u,t) in enumerate([('2.880','estaciones','habilitadas en el país'),('300,5','millones de litros','vendidos en octubre'),('104.000','litros','vende por mes la estación promedio')]):
    y=470+i*200; d.rounded_rectangle([66,y,1014,y+176],14,fill=NV2); d.rectangle([66,y,74,y+176],fill=G)
    d.text((104,y+62),n,font=BB(100),fill=W,anchor='lm'); x=104+d.textlength(n,font=BB(100))+18; d.text((x,y+72),u,font=B(40,'Bold'),fill=G,anchor='lm'); d.text((104,y+138),t,font=B(28,'Regular'),fill=M,anchor='lm')
d.text((66,1100),'Ranking de ventas, precios y red, todos los meses.',font=B(34,'Bold'),fill=W); d.text((66,1150),'Datos del Ministerio de Industria y Comercio.',font=B(28,'Regular'),fill=M)
foot(d,t='energiaslatam.com'); im.save(O+'03-datos-paraguay.jpg',quality=92)
# 4 Qué significa para la estación
im,d=base(); d.text((66,170),'NO SOLO LA NOTICIA:',font=BB(104),fill=W); d.text((66,272),'QUÉ SIGNIFICA',font=BB(104),fill=G); d.text((66,374),'PARA TU ESTACIÓN',font=BB(104),fill=G)
d.text((66,520),'Cada nota cierra con lo que conviene revisar.',font=B(34),fill=M)
for i,(a,b) in enumerate([('Precios e impuestos','Cuánto cambia el litro y desde cuándo'),('Márgenes y volumen','Cuántos litros hacen falta para empatar'),('Emblemas y contratos','Qué mirar antes de cambiar de bandera'),('Tienda y servicios','Lo que suma cuando el litro aprieta')]): card(d,66,600+i*124,948,104,a,b)
cta(d,1120,'Recibilo en tu mail'); foot(d); im.save(O+'04-que-significa.jpg',quality=92)
# 5 Cómo inscribirse
im,d=base(); d.text((66,170),'SUMATE EN',font=BB(120),fill=W); d.text((66,286),'TRES PASOS',font=BB(120),fill=G)
for i,(a,b) in enumerate([('1. Entrá','energiaslatam.com/newsletter'),('2. Dejá tu nombre y tu mail','La empresa es opcional'),('3. Tocá «Quiero recibirlo»','Listo: te llega a tu mail')]): card(d,66,470+i*128,560,108,a,b)
phone(im,680,440,340,640,lambda sc,dd,sw,sh:form(sc,dd,sw,sh,name='Diego',mail='tu@correo.com',pressed=True,s=0.62))
d.text((66,870),'Llega lunes, jueves y sábados.',font=B(34,'Bold'),fill=W); d.text((66,916),'Gratis. Te das de baja con un clic.',font=B(30,'Regular'),fill=M)
cta(d,1010,'Quiero recibirlo'); foot(d); im.save(O+'05-como-inscribirse.jpg',quality=92)
# Video
NAME='Juan'; MAIL='juan@miestacion.com'
def frame(t):
    im=Image.new('RGB',(1080,1920),NV); d=ImageDraw.Draw(im); d.rectangle([0,0,1080,10],fill=G); d.text((60,70),'LA ESTACIÓN DEL FUTURO',font=BC(36),fill=G); lg=logo.resize((100,100)); im.paste(lg,(920,44),lg)
    def head(a,b,sub=None):
        d.text((60,190),a,font=BB(104),fill=W); d.text((60,292),b,font=BB(104),fill=G)
        if sub: d.text((60,410),sub,font=B(38),fill=M)
    px,py,pw,ph=170,520,740,1240
    if t<3.5:
        d.text((60,560),'LAS NOTICIAS DE',font=BB(130),fill=W); d.text((60,690),'LAS ESTACIONES',font=BB(130),fill=W); d.text((60,820),'DE SERVICIO,',font=BB(130),fill=W); d.text((60,950),'EN TU MAIL',font=BB(130),fill=G)
        d.text((60,1130),'Lunes, jueves y sábados. Gratis.',font=B(44),fill=M)
    elif t<7:
        head('PASO 1','ENTRÁ A LA PÁGINA','energiaslatam.com/newsletter'); phone(im,px,py,pw,ph,lambda sc,dd,sw,sh:form(sc,dd,sw,sh,s=1.3))
    elif t<14:
        head('PASO 2','NOMBRE Y MAIL','La empresa es opcional.'); u=t-7
        n=NAME[:max(0,min(len(NAME),int(u/0.3)))]; mstart=1.8; m=MAIL[:max(0,min(len(MAIL),int((u-mstart)/0.2)))] if u>mstart else ''
        cur='n' if u<mstart else ('m' if u<mstart+len(MAIL)*0.2+0.6 else None)
        phone(im,px,py,pw,ph,lambda sc,dd,sw,sh:form(sc,dd,sw,sh,name=n,mail=m,cur=cur,s=1.3))
    elif t<18:
        head('PASO 3','«QUIERO RECIBIRLO»','Un toque y listo.'); u=t-14
        phone(im,px,py,pw,ph,lambda sc,dd,sw,sh:form(sc,dd,sw,sh,name=NAME,mail=MAIL,pressed=(0.8<u<2),done=u>=2,s=1.3))
    else:
        d.text((60,560),'LISTO.',font=BB(170),fill=G); d.text((60,750),'TE LLEGA A TU MAIL',font=BB(118),fill=W)
        for i,l in enumerate(['Lunes, jueves y sábados. Gratis.','Te das de baja cuando quieras, con un clic.']): d.text((60,930+i*60),l,font=B(42),fill=M)
        cta(d,1120,'energiaslatam.com/newsletter',x=60)
    return im
if __name__=='__main__':
    T=22.0; fps=30
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r',str(fps),'-i','-','-i','/home/claude/out/gu25/r2/music.wav','-t',str(T),'-af',f'volume=0.7,afade=t=in:d=1,afade=t=out:st={T-1.8}:d=1.8','-c:v','libx264','-crf','20','-preset','veryfast','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart',O+'tmp.mp4'],stdin=subprocess.PIPE)
    last=None; lastim=None
    for i in range(int(T*fps)):
        t=i/fps; key=round(t*10) if 7<=t<18 else int(t>=3.5)+int(t>=7)+int(t>=18)
        if key!=last: lastim=frame(t).tobytes(); last=key
        p.stdin.write(lastim)
    p.stdin.close(); p.wait(); subprocess.run(['mv',O+'tmp.mp4',O+'06-como-inscribirse-video.mp4'])
    sh=Image.new('RGB',(432*5,540+480),'white')
    for i,f in enumerate(['01-newsletter','02-cuanto-gana','03-datos-paraguay','04-que-significa','05-como-inscribirse']): sh.paste(Image.open(O+f+'.jpg').resize((432,540)),(i*432,0))
    for i,t in enumerate([1,5,10,13,15.5,17,20]): sh.paste(frame(t).resize((270,480)),(i*270,540))
    sh.save(O+'rev.jpg',quality=85)
