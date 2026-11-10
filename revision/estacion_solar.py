from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
W,H=1600,1067; F='/home/claude/chart/'
im=Image.new('RGB',(W,H)); d=ImageDraw.Draw(im)
for y in range(H):  # cielo
    t=y/H; c=(int(120+90*t),int(180+50*t),int(235+10*t)); d.line([(0,y),(W,y)],fill=c)
# sol
glow=Image.new('L',(W,H),0); g=ImageDraw.Draw(glow); g.ellipse([1180,60,1420,300],fill=255); glow=glow.filter(ImageFilter.GaussianBlur(60))
im=Image.composite(Image.new('RGB',(W,H),(255,236,170)),im,glow); d=ImageDraw.Draw(im)
d.ellipse([1240,120,1360,240],fill=(255,214,90))
# colinas
d.polygon([(0,720),(300,640),(620,690),(980,620),(1300,670),(1600,630),(1600,H),(0,H)],fill=(120,170,110))
# molinos de fondo
def molino(x,base,h,ang,s=1):
    d.polygon([(x-6*s,base),(x+6*s,base),(x+3*s,base-h),(x-3*s,base-h)],fill=(240,243,246))
    cx,cy=x,base-h
    for k in range(3):
        a=math.radians(ang+k*120); L=h*0.55
        ex,ey=cx+L*math.cos(a),cy+L*math.sin(a); px,py=-math.sin(a)*6*s,math.cos(a)*6*s
        d.polygon([(cx+px,cy+py),(cx-px,cy-py),(ex,ey)],fill=(245,247,250))
    d.ellipse([cx-8*s,cy-8*s,cx+8*s,cy+8*s],fill=(220,226,232))
molino(1080,650,230,-20); molino(1230,668,190,10,0.85); molino(1390,640,250,40)
# suelo / playa
d.rectangle([0,860,W,H],fill=(88,96,108)); d.rectangle([0,850,W,866],fill=(200,205,210))
for x in range(0,W,160): d.rectangle([x,955,x+80,962],fill=(235,235,235))
# tienda con paneles en techo
d.rectangle([980,640,1520,860],fill=(240,244,248)); d.rectangle([980,640,1520,668],fill=(12,26,41))
d.rectangle([1040,700,1240,860],fill=(160,200,230)); d.rectangle([1280,700,1460,800],fill=(160,200,230))
d.text((1225,642),'TIENDA',font=ImageFont.truetype(F+'BebasNeue-Regular.ttf',27),fill=(255,255,255))
def paneles(x0,y0,cols,rows,w,h,skew):
    for r in range(rows):
        for c in range(cols):
            x=x0+c*w+r*skew; y=y0+r*h
            d.polygon([(x,y),(x+w-4,y),(x+w-4+skew,y+h-4),(x+skew,y+h-4)],fill=(28,64,140),outline=(170,200,240))
            d.line([(x+w/2,y),(x+w/2+skew,y+h-4)],fill=(90,130,200),width=1)
paneles(990,596,9,2,58,22,-6)
d.rectangle([980,640,1520,668],fill=(12,26,41)); d.text((1225,642),'TIENDA',font=ImageFont.truetype(F+'BebasNeue-Regular.ttf',27),fill=(255,255,255))
# canopy con paneles
d.rectangle([90,470,900,520],fill=(12,26,41)); d.rectangle([90,520,900,540],fill=(58,125,68))
d.text((120,474),'LA ESTACIÓN DEL FUTURO',font=ImageFont.truetype(F+'BebasNeue-Regular.ttf',40),fill=(255,255,255))
paneles(100,400,13,3,61,23,-8)
for x in (230,760): d.rectangle([x-14,540,x+14,860],fill=(225,230,235))
# surtidores
for x in (360,600):
    d.rectangle([x-40,690,x+40,860],fill=(240,244,248),outline=(12,26,41),width=3)
    d.rectangle([x-28,705,x+28,745],fill=(30,40,55)); d.rectangle([x-40,830,x+40,860],fill=(58,125,68))
    d.line([(x+40,760),(x+60,800),(x+60,840)],fill=(30,30,30),width=5)
d.rectangle([300,860,660,872],fill=(180,186,192))
# rótulo
d.rounded_rectangle([40,960,720,1040],18,fill=(12,26,41))
d.text((64,976),'Ilustración: estación con paneles solares en el canopy y en la tienda',font=ImageFont.truetype(F+'Barlow-SemiBold.ttf',20),fill=(255,255,255))
d.text((64,1004),'energiaslatam.com',font=ImageFont.truetype(F+'Barlow-Bold.ttf',20),fill=(109,187,120))
im.save('/home/claude/larevista-notas/img/2026-11-10-mopc-registro-autogeneracion-renovable-2.jpg',quality=88); print('ok')
