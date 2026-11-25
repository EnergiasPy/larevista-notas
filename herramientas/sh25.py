import subprocess,json,re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ID='2026-11-25-shell-cinco-anos-paraguay-290-estaciones'; R='/home/claude/larevista-notas/'; I=R+'img/'; S=I+'social/'; O='/home/claude/out/sh25/'; SRC=O+'src/'
h=open('gu24.py').read().split("fig,ax=hdr(")[0].replace('2026-11-24-gulf-paraguay-30-estaciones-anjor-lanzamiento',ID)
exec(h)
fig,ax=hdr('CONTENIDO PATROCINADO POR SHELL · PARAGUAY','SHELL CUMPLE CINCO AÑOS EN PARAGUAY','El recorrido de la marca en el país, según la compañía')
tiles=[('5','años','De presencia en Paraguay',RD),('2021','','Abrió la primera estación',NV),('200','estaciones','Al año siguiente de la apertura',NV),('+290','estaciones','La red de hoy, en todo el país',GR)]
for i,(big,uni,sub,col) in enumerate(tiles):
    x=80+(i%2)*735; y=290+(i//2)*222
    rb(ax,x,y,705,200,SO,10); ax.add_patch(Rectangle((x,y),8,200,color=col))
    num(fig,ax,x+40,y+82,big,uni,86,col,ufs=36,dy=10)
    ax.text(x+42,y+158,sub,fontfamily=B,fontweight='semibold',fontsize=21,color=MU,va='center')
rb(ax,80,742,1440,62,NV,10)
ax.text(120,773,'LA CELEBRACIÓN FUE EN EL PUERTO DE ASUNCIÓN',fontfamily=BB,fontsize=36,color='#6DBB78',va='center')
foot(fig,ax,'Datos: Shell Paraguay.','-1.jpg',ysrc=878)
BBf=lambda z:ImageFont.truetype('BebasNeue-Regular.ttf',z); Bf=lambda z,w='SemiBold':ImageFont.truetype(f'Barlow-{w}.ttf',z); BC=lambda z:ImageFont.truetype('BarlowCondensed-Bold.ttf',z)
G='#6DBB78'; W_='#F4F6FA'; NVt=(15,30,60); M_='#C9D2DE'
def cover(im,w,h,fx=.5,fy=.5):
    W,H=im.size; r=max(w/W,h/H); im=im.resize((int(W*r)+1,int(H*r)+1),Image.LANCZOS); W,H=im.size
    x=int((W-w)*fx); y=int((H-h)*fy); return im.crop((x,y,x+w,y+h))
A=Image.open(SRC+'CE_07341.jpg.jpeg').convert('RGB'); Bv=Image.open(SRC+'CE_07118.jpg.jpeg').convert('RGB')
cover(A,1600,1067,fy=.5).save(I+ID+'-2.jpg',quality=85); cover(Bv,1600,1067,fy=.36).save(I+ID+'-3.jpg',quality=85)
def slide(bg,lines,out,small=None,start=1000):
    c=bg.convert('RGBA'); ov=Image.new('RGBA',c.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(1920):
        a=int(240*(1-y/280)) if y<280 else 0
        if y>start: a=int(min(250,250*((y-start)/420)))
        d.line([(0,y),(1080,y)],fill=NVt+(a,))
    c=Image.alpha_composite(c,ov); d=ImageDraw.Draw(c)
    for i,col in enumerate(['#D52B1E','#FFFFFF','#0038A8']): d.rectangle([0,i*6,1080,i*6+6],fill=col)
    d.text((60,60),'LA ESTACIÓN DEL FUTURO',font=BC(34),fill=G); d.text((60,104),'Contenido patrocinado por Shell',font=Bf(28),fill=W_)
    y=1290
    for t,f,col in lines: d.text((60,y),t,font=f,fill=col); y+=int(f.size*1.1)
    if small:
        for s in small: d.text((60,y+14),s,font=Bf(36),fill=M_); y+=48
    d.text((1020,1840),'energiaslatam.com',font=BC(34),fill=W_,anchor='ra'); c.convert('RGB').save(out)
def blurbg(im,top=420):
    bg=cover(im,1080,1920).filter(ImageFilter.GaussianBlur(30)); r=1080/im.size[0]; fg=im.resize((1080,int(im.size[1]*r)),Image.LANCZOS); bg.paste(fg,(0,top)); return bg
H=BBf(120); T=Bf(54,'Bold'); bgA=blurbg(A); bgB=cover(Bv,1080,1920,fy=.3); bgA2=cover(A,1080,1920,fx=.38)
slide(bgA,[('SHELL CUMPLE',H,W_),('CINCO AÑOS',H,G),('EN PARAGUAY',H,W_)],O+'f1.png',start=980)
slide(bgB,[('2021:',H,G),('LA PRIMERA ESTACIÓN',BBf(100),W_)],O+'f2.png',small=['Así empezó la red en el país.'])
slide(bgB,[('200 ESTACIONES',H,W_),('AL AÑO SIGUIENTE',BBf(100),G)],O+'f3.png',small=['Según la compañía.'])
slide(bgA2,[('MÁS DE 290',H,G),('ESTACIONES HOY',H,W_)],O+'f4.png',small=['En todo el país.'])
slide(bgB,[('«Se gana un lugar',T,W_),('cada día, en cada',T,W_),('estación.»',T,W_)],O+'f5.png',small=['Néstor Visendaz, CEO de Raízen,','licenciataria de Shell en Paraguay'])
slide(bgA,[('La celebración fue en el',T,W_),('Puerto de Asunción, con',T,W_),('operadores de todo el país.',T,G)],O+'f6.png')
slide(bgA2,[('NOTA COMPLETA EN',BBf(88),W_),('ENERGIASLATAM.COM',BBf(88),G)],O+'f7.png',small=['Fotos: gentileza Shell.'])
Image.open(O+'f1.png').save(S+ID+'-reel-portada.jpg',quality=90)
D=4.6; X=0.5; n=7; args=[]
for i in range(1,n+1): args+=['-loop','1','-framerate','30','-t',str(D),'-i',O+f'f{i}.png']
F='[0:v]format=yuv420p[v0]'; prev='v0'
for i in range(1,n): F+=f';[{i}:v]format=yuv420p[s{i}];[{prev}][s{i}]xfade=transition=fade:duration={X}:offset={round((D-X)*i,2)}[x{i}]'; prev=f'x{i}'
T_=round(D*n-X*(n-1),2)
subprocess.run(['ffmpeg','-v','error','-y']+args+['-i','/home/claude/out/gu25/r2/music.wav','-filter_complex',F,'-map',f'[{prev}]','-map',f'{n}:a','-t',str(T_),'-af',f'volume=0.7,afade=t=in:d=1,afade=t=out:st={T_-1.8}:d=1.8','-c:v','libx264','-crf','20','-preset','veryfast','-r','30','-c:a','aac','-b:a','128k','-movflags','+faststart',O+'tmp.mp4'],check=True)
subprocess.run(['mv',O+'tmp.mp4',S+ID+'-reel.mp4']); print(T_)
d=json.load(open('/home/claude/larevista-notas/notas.json'));L=d if isinstance(d,list) else d['notas']
L[:]=[x for x in L if x['id']!=ID]
L.append({"id":ID,"estado":"borrador","fecha":"2026-11-25","pais":"py","cat":"Novedades de la industria","titulo":"Shell cumple cinco años en Paraguay: de una estación en 2021 a más de 290","bajada":"Contenido patrocinado por Shell. La marca celebró su aniversario en el Puerto de Asunción con operadores de todo el país. Su licenciataria, Raízen, repasó el crecimiento de la red y agradeció a quienes la sostienen.","autor":"Ana Paula Scacciaferro","img":"img/"+ID+"-2.jpg"})
json.dump(d,open('/home/claude/larevista-notas/notas.json','w'),ensure_ascii=False,indent=1)
print(len(re.sub('<[^>]+>',' ',open(f'/home/claude/larevista-notas/notas/{ID}.html').read()).split()))
sh=Image.new('RGB',(270*7,480+540))
for i in range(7): sh.paste(Image.open(O+f'f{i+1}.png').resize((270,480)),(i*270,0))
sh.paste(Image.open(I+ID+'-1.jpg').resize((810,540)),(0,480)); sh.paste(Image.open(I+ID+'-3.jpg').resize((810,540)),(810,480)); sh.save(O+'rev.jpg',quality=85)
