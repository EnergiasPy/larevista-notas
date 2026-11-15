# reel_lib.py · reels verticales 1080x1920 de placas animadas para @energiaslatam
from PIL import Image, ImageDraw, ImageFont
import os, math, subprocess
D='/home/claude/chart/'
BG=(15,33,61); W=(244,246,249); M=(159,179,200); G=(118,196,110); CARD=(23,48,90); RD=(226,72,79)
F=lambda n,s: ImageFont.truetype(D+n,s)
BB=lambda s: F('BebasNeue-Regular.ttf',s); BS=lambda s: F('Barlow-SemiBold.ttf',s); BBo=lambda s: F('Barlow-Bold.ttf',s); BC=lambda s: F('BarlowCondensed-Bold.ttf',s)
def ease(t): return 1-(1-t)**3
def nf(v,dec=0):
    s=f'{v:,.{dec}f}'.replace(',','.') if dec==0 else f'{v:,.{dec}f}'.replace(',','X').replace('.',',').replace('X','.')
    return s
class Frame:
    def __init__(s,franja):
        s.im=Image.new('RGB',(1080,1920),BG); s.d=ImageDraw.Draw(s.im)
        for i,c in enumerate(franja): s.d.rectangle([0,i*9,1080,i*9+9],fill=c)
    def rb(s,x,y,w,h,c,r=18): s.d.rounded_rectangle([x,y,x+w,y+h],r,fill=c)
    def t(s,x,y,txt,f,c,anchor='la'): s.d.text((x,y),txt,font=f,fill=c,anchor=anchor)
    def foot(s,n=None):
        s.d.rectangle([0,1820,1080,1920],fill=(10,22,42))
        s.t(60,1855,'LA ESTACIÓN',BB(46),W); s.t(300,1855,'DEL FUTURO',BB(46),G)
        s.t(1020,1862,'energiaslatam.com',BBo(26),W,'ra')
    def sub(s,txt):
        if not txt: return
        f=BBo(40); lines=txt.split('|')
        h=len(lines)*56+28; y0=1660-h
        wmax=max(s.d.textlength(l,font=f) for l in lines)
        s.rb(540-wmax/2-28,y0,wmax+56,h,(10,22,42),16)
        for i,l in enumerate(lines): s.t(540,y0+22+i*56,l,f,W,'ma')
def encode(frames_dir,out,fps=30):
    subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-framerate',str(fps),'-i',frames_dir+'/f%05d.jpg',
      '-c:v','libx264','-crf','19','-preset','veryfast','-pix_fmt','yuv420p','-movflags','+faststart',out+'.tmp.mp4'],check=True)
    os.replace(out+'.tmp.mp4',out)
