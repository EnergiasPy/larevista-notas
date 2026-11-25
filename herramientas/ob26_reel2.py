# Version corta del reel de obra publica a partir del archivo de Diego (720x1280)
import subprocess
from PIL import Image, ImageDraw, ImageFont
SRC='/mnt/user-data/uploads/Reel_Paraguay_Infraestructura.mov'; O='/home/claude/out/ob26/w/'
B=lambda z,w='SemiBold':ImageFont.truetype(f'Barlow-{w}.ttf',z)
G='#6DBB78'; W='#F4F6FA'; M='#AEB8C8'
ENC=['-c:v','libx264','-crf','20','-preset','veryfast','-r','30','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-ar','44100','-ac','2']
def ov(lines,out):
    im=Image.new('RGBA',(720,1280),(0,0,0,0)); d=ImageDraw.Draw(im)
    y=940
    for l in lines: d.text((40,y),l,font=B(36,'Bold'),fill=W); y+=46
    d.text((40,max(y+16,1190)),'Pedro Alliana, presidente de la República',font=B(24,'Bold'),fill=G)
    im.save(out)
def seg(a,b,lines,i):
    ov(lines,O+f'z{i}.png')
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a),'-to',str(b),'-i',SRC,'-i',O+f'z{i}.png',
      '-filter_complex','[0:v]fps=30,format=yuv420p[v];[v][1:v]overlay=0:0[o]','-map','[o]','-map','0:a:0',
      '-af','loudnorm=I=-16:TP=-1.5']+ENC+[O+f'z{i}.mp4'],check=True)
