# Reel del lanzamiento de Gulf: video real + audios de los discursos sobre fotos, con subtítulos quemados
import subprocess,textwrap
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter
A='/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/'; V='/mnt/user-data/uploads/IMG_6030.mov'
ID='2026-11-25-gulf-paraguay-lanzamiento-modelo-licencia-operadores'; S='/home/claude/larevista-notas/img/social/'; O='/home/claude/out/gu25/r2/'
A12=A+'5771d9c2-Nueva_grabacio_n_12.m4a'; A16=A+'6b471462-Nueva_grabacio_n_16.m4a'
BB=lambda z:ImageFont.truetype('BebasNeue-Regular.ttf',z); B=lambda z,w='SemiBold':ImageFont.truetype(f'Barlow-{w}.ttf',z); BC=lambda z:ImageFont.truetype('BarlowCondensed-Bold.ttf',z)
G='#6DBB78'; W_='#F4F6FA'; NV=(15,30,60)
def op(n): return ImageOps.exif_transpose(Image.open(A+n+'-image.jpg')).convert('RGB')
def cover(im,w,h,fx=.5,fy=.5):
    W,H=im.size; r=max(w/W,h/H); im=im.resize((int(W*r)+1,int(H*r)+1),Image.LANCZOS); W,H=im.size
    x=int((W-w)*fx); y=int((H-h)*fy); return im.crop((x,y,x+w,y+h))
def shade(c,start=1000,full=250):
    w,h=c.size; ov=Image.new('RGBA',c.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(h):
        a=int(150*(1-y/160)) if y<160 else 0
        if y>start: a=int(min(full,full*((y-start)/(h*0.22))))
        d.line([(0,y),(w,y)],fill=NV+(a,))
    for i,col in enumerate(['#D52B1E','#FFFFFF','#0038A8']): d.rectangle([0,i*6,w,i*6+6],fill=col)
    d.text((60,70),'LA ESTACIÓN DEL FUTURO',font=BC(34),fill=G); d.text((1020,1840),'energiaslatam.com',font=BC(34),fill=W_,anchor='ra')
    return ov
def bgphoto(n,blur=False,fx=.5,fy=.4):
    im=op(n)
    if blur:
        bg=cover(im,1080,1920).filter(ImageFilter.GaussianBlur(30)); r=1080/im.size[0]; fg=im.resize((1080,int(im.size[1]*r)),Image.LANCZOS); bg.paste(fg,(0,400)); return bg
    return cover(im,1080,1920,fx=fx,fy=fy)
def cue(bg,name,text,out):
    c=Image.alpha_composite(bg.convert('RGBA'),shade(bg)); d=ImageDraw.Draw(c)
    d.text((60,1240),name,font=B(36,'Bold'),fill=G); y=1300
    for l in textwrap.wrap(text,30): d.text((60,y),l,font=B(58,'Bold'),fill=W_); y+=68
    c.convert('RGB').save(out)
ENC=['-c:v','libx264','-crf','20','-preset','veryfast','-r','30','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-ar','44100','-ac','2']
def still(png,audio,ss,dur,out,af='loudnorm=I=-16:TP=-1.5'):
    if audio: a=['-ss',str(ss),'-t',str(dur),'-i',audio]
    else: a=['-f','lavfi','-t',str(dur),'-i','anullsrc=r=44100:cl=stereo']; af='anull'
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',str(dur),'-i',png]+a+['-af',af,'-shortest']+ENC+[O+'tmp.mp4'],check=True); subprocess.run(['mv',O+'tmp.mp4',out],check=True)
segs=[]
# 1 video real: la entrada del auto
ov=shade(Image.new('RGB',(1080,1920))); d=ImageDraw.Draw(ov)
d.text((60,1270),'ASÍ FUE EL LANZAMIENTO',font=BB(96),fill=W_); d.text((60,1368),'DE GULF EN PARAGUAY',font=BB(96),fill=G); d.text((60,1490),'Y la entrada de Lucas Velasco, presidente de ANJOR.',font=B(38),fill='#C9D2DE'); ov.save(O+'ov1.png')
subprocess.run(['ffmpeg','-v','error','-y','-ss','19.5','-t','8','-i',V,'-i',O+'ov1.png','-filter_complex','[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30[v];[v][1:v]overlay=0:0,fade=t=out:st=7.7:d=0.3[o]','-map','[o]','-map','0:a:1','-af','loudnorm=I=-20:TP=-2,afade=t=out:st=7.5:d=0.5']+ENC+[O+'tmp.mp4'],check=True); subprocess.run(['mv',O+'tmp.mp4',O+'s00.mp4']); segs.append('s00.mp4')
subprocess.run(['ffmpeg','-v','error','-y','-ss','25.5','-i',V,'-i',O+'ov1.png','-filter_complex','[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[v];[v][1:v]overlay=0:0','-frames:v','1',S+ID+'-reel-portada.jpg'],check=True)
# 2 discursos
LV='Lucas Velasco, presidente de ANJOR'; GM='Gastón Mienko, vicepresidente de Gulf Latam'
bgV=bgphoto('d7b1ca33',fx=.0); bgJ=bgphoto('d618cc7c',blur=True); bgM=bgphoto('1d1bf103',fx=.0,fy=.6)
cues=[(bgV,LV,A12,29.16,34.61,'«Ser independiente no significa tener que estar solos.»'),
      (bgV,LV,A12,34.61,41.07,'«En Paraguay son muchos los empresarios con esfuerzo, mucho talento…'),
      (bgV,LV,A12,41.07,43.90,'…pero esa fuerza está fragmentada.»'),
      (bgJ,LV,A12,83.79,87.45,'«…dejar de competir como negocios aislados…'),
      (bgJ,LV,A12,87.45,93.62,'…y sumar litros, estaciones, presencia y capacidad de negociación.'),
      (bgJ,LV,A12,93.62,97.58,'Cada uno es un negocio, pero todos jugando juntos.»'),
      (bgM,GM,A16,110.13,113.97,'«Lo más importante es que no operamos estaciones de servicio.'),
      (bgM,GM,A16,113.97,115.80,'Nos asociamos.'),
      (bgM,GM,A16,115.80,120.68,'Controlamos la marca, que es lo que sabemos hacer, pero necesitamos de los operadores locales.»')]
for i,(bg,nm,au,a,b,t) in enumerate(cues):
    cue(bg,nm,t,O+f'c{i}.png'); still(O+f'c{i}.png',au,a,round(b-a,2),O+f's{i+1:02d}.mp4'); segs.append(f's{i+1:02d}.mp4')
# 3 cierre
bg=bgphoto('82b1d8dc',fy=.5); c=Image.alpha_composite(bg.convert('RGBA'),shade(bg)); d=ImageDraw.Draw(c)
d.text((60,1270),'30 CAMBIOS DE EMBLEMA',font=BB(92),fill=W_); d.text((60,1365),'EN LA PRIMERA ETAPA',font=BB(92),fill=G)
d.text((60,1490),'Nota completa en energiaslatam.com',font=B(42,'Bold'),fill=W_); d.text((60,1550),'Seguinos para la noticia del sector todos los días.',font=B(34),fill='#C9D2DE'); c.convert('RGB').save(O+'end.png')
still(O+'end.png',None,0,4,O+'s99.mp4'); segs.append('s99.mp4')
open(O+'list.txt','w').write(''.join(f"file '{s}'\n" for s in segs))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',O+'list.txt','-c','copy','-movflags','+faststart',O+'tmp.mp4'],check=True); subprocess.run(['mv',O+'tmp.mp4',S+ID+'-reel.mp4'])
sh=Image.new('RGB',(270*6,480)); 
fr=[S+ID+'-reel-portada.jpg',O+'c0.png',O+'c4.png',O+'c6.png',O+'c8.png',O+'end.png']
for j,f in enumerate(fr): sh.paste(Image.open(f).convert('RGB').resize((270,480)),(j*270,0))
sh.save(O+'rev.jpg',quality=85)
