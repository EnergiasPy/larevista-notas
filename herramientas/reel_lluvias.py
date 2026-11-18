#!/usr/bin/env python3
# reel_lluvias.py · reel "Cuidá tu combustible" para @energiaslatam
# Video de apertura generado con IA + fotos reales de instalación + locución de Diego.
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

D='/home/claude/chart/'
A='/mnt/user-data/attachments/ba48a484-4b4b-549d-9611-4438eea46fb5/'
OUT='/home/claude/out/'
W,H=1080,1920
BG=(15,33,61); WH=(244,246,249); M=(159,179,200); G=(118,196,110); RD=(226,72,79); DARK=(10,22,42)
F=lambda n,s: ImageFont.truetype(D+n,s)
BB=lambda s: F('BebasNeue-Regular.ttf',s)
BS=lambda s: F('Barlow-SemiBold.ttf',s)
BBo=lambda s: F('Barlow-Bold.ttf',s)
BC=lambda s: F('BarlowCondensed-Bold.ttf',s)

VID=A+'0b8e204c-gemini_generated_video_6A07A7D5.mp4'
FOTOS=[A+'ec450038-image.jpg', A+'232967c9-image.jpg', A+'2bde8d2f-image.jpg',
       A+'c03cdb93-image.jpg', A+'228a3579-image.jpg']
PASTA_GRAL='/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/pasta_gral.jpg'
PASTA_ZOOM='/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/pasta_zoom.jpg'
VOZ='/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/voz_final.mp3'
LOGO='/home/claude/larevista-notas/site/brand/logo-latam-v2-512.png'

def logo_redondo(px):
    """El logo recortado en círculo, al tamaño pedido."""
    lg=Image.open(LOGO).convert('RGBA')
    mk=Image.new('L',lg.size,0); ImageDraw.Draw(mk).ellipse((6,6,lg.size[0]-6,lg.size[1]-6),fill=255)
    lg.putalpha(mk)
    return lg.resize((px,px),Image.LANCZOS)

# ---- escenas, alineadas con las pausas de la locución -----------------------
SC=[
 dict(t=0.00, d=9.75, src=VID,      kind='video', kicker=None,
      title=['EL AGUA NO ENTRA','POR EL TECHO:','ENTRA POR LA TAPA'], ia=True),
 dict(t=9.75, d=4.25, src=FOTOS[0], kind='foto', kicker='UNO', title=['TAPAS','HERMÉTICAS'],
      pie='Que cierren herméticas, no apoyadas.'),
 dict(t=14.00,d=4.66, src=FOTOS[1], kind='foto', kicker='UNO', title=['REVISÁ','LA JUNTA'],
      pie='Si está dura o cortada, no sella.'),
 dict(t=18.66,d=3.79, src=FOTOS[2], kind='foto', kicker='DOS', title=['LA CÁMARA','SECA'],
      pie='Sin agua acumulada adentro.'),
 dict(t=22.45,d=4.45, src=FOTOS[3], kind='foto', kicker='DOS', title=['SI JUNTA','AGUA...'],
      pie='Al abrir la tapa, se va derecho al tanque.'),
 dict(t=26.90,d=4.55, src=PASTA_GRAL, kind='foto', kicker='TRES', title=['MEDÍ EL AGUA','DE FONDO'],
      pie='Con pasta, antes y después de la lluvia.'),
 dict(t=31.45,d=2.48, src=PASTA_ZOOM, kind='foto', kicker='TRES', title=['SI SUBIÓ,','YA SABÉS'],
      pie='Por dónde entró.'),
 dict(t=33.93,d=2.91, src=None,     kind='cierre'),
]

def overlay(sc, path):
    """Capa de textos transparente para una escena."""
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    # franja tricolor
    for i,c in enumerate([(213,43,30),(255,255,255),(0,56,168)]):
        d.rectangle([0,i*9,W,i*9+9],fill=c+(255,))
    if sc['kind']=='cierre':
        d.rectangle([0,0,W,H],fill=BG+(255,))
        lg=logo_redondo(340); im.paste(lg,(W//2-170,420),lg)
        d=ImageDraw.Draw(im)
        d.text((W//2,900),'CUIDÁ',font=BB(170),fill=WH,anchor='ms')
        d.text((W//2,1060),'TU COMBUSTIBLE',font=BB(124),fill=G,anchor='ms')
        d.rectangle([W//2-110,1120,W//2+110,1130],fill=G+(255,))
        d.text((W//2,1290),'energiaslatam.com',font=BBo(52),fill=WH,anchor='ms')
        d.text((W//2,1370),'Seguinos para la noticia del sector',font=BS(38),fill=M,anchor='ms')
        im.save(path); return
    # degradado inferior para que el texto se lea sobre la foto
    grad=Image.new('L',(1,H),0); gd=ImageDraw.Draw(grad)
    for y in range(H):
        if y<620: a=0
        elif y<980: a=int(215*(y-620)/360)
        else: a=215
        gd.point((0,y),fill=a)
    im.paste(Image.new('RGBA',(W,H),DARK+(255,)), (0,0), grad.resize((W,H)))
    # degradado superior suave
    gt=Image.new('L',(1,H),0); td=ImageDraw.Draw(gt)
    for y in range(H): td.point((0,y),fill=max(0,int(170*(1-y/420))) if y<420 else 0)
    im.paste(Image.new('RGBA',(W,H),DARK+(255,)), (0,0), gt.resize((W,H)))
    # logo arriba a la izquierda
    lg=logo_redondo(104); im.paste(lg,(56,70),lg)
    d=ImageDraw.Draw(im)
    d.text((178,128),'ENERGÍAS',font=BB(52),fill=WH,anchor='ls')
    d.text((178,176),'LATAM',font=BB(52),fill=G,anchor='ls')
    if sc.get('ia'):
        d.text((W-60,128),'IMAGEN GENERADA CON IA',font=BC(30),fill=M,anchor='rs')
    else:
        d.text((W-60,128),'FOTO: ENERGÍAS LATAM',font=BC(30),fill=M,anchor='rs')
    y=1060
    if sc.get('kicker'):
        tw=d.textlength(sc['kicker'],font=BC(44))
        d.rounded_rectangle([60,y-62,60+tw+54,y+6],14,fill=G+(255,))
        d.text((87,y-14),sc['kicker'],font=BC(44),fill=BG,anchor='ls')
        y+=40
    for i,l in enumerate(sc['title']):
        d.text((58,y+i*106+70),l,font=BB(96),fill=WH if i<len(sc['title'])-1 else G,anchor='ls')
    y2=y+len(sc['title'])*106+120
    if sc.get('pie'):
        d.text((60,y2),sc['pie'],font=BBo(44),fill=WH,anchor='ls')
    # pie de marca
    d.rectangle([0,H-96,W,H],fill=DARK+(255,))
    lp=logo_redondo(58); im.paste(lp,(56,H-77),lp)
    d=ImageDraw.Draw(im)
    d.text((132,H-36),'LA ESTACIÓN',font=BB(44),fill=WH,anchor='ls')
    d.text((360,H-36),'DEL FUTURO',font=BB(44),fill=G,anchor='ls')
    d.text((W-60,H-40),'energiaslatam.com',font=BBo(26),fill=WH,anchor='rs')
    im.save(path)

def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode!=0:
        print('ERROR:', ' '.join(cmd[:12]), '\n', r.stderr[-900:]); sys.exit(1)

def main():
    tmp='/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/rl'
    os.makedirs(tmp,exist_ok=True); os.makedirs(OUT,exist_ok=True)
    partes=[]
    for i,sc in enumerate(SC):
        ov=f'{tmp}/ov{i}.png'; overlay(sc,ov)
        out=f'{tmp}/s{i}.mp4'; d=sc['d']
        if sc['kind']=='video':
            vf=(f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                f"fps=30,setsar=1[v];[v][1:v]overlay=0:0,format=yuv420p")
            run(['ffmpeg','-y','-v','error','-ss','0','-t',str(d),'-i',sc['src'],'-i',ov,
                 '-filter_complex',vf,'-an','-r','30',
                 '-c:v','libx264','-crf','19','-preset','veryfast','-pix_fmt','yuv420p',out+'.tmp.mp4'])
        elif sc['kind']=='foto':
            z=f"1+0.05*on/{int(d*30)}" if i%2 else f"1.05-0.05*on/{int(d*30)}"
            vf=(f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
                f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(d*30)}:s={W}x{H}:fps=30,"
                f"setsar=1[v];[v][1:v]overlay=0:0,format=yuv420p")
            run(['ffmpeg','-y','-v','error','-loop','1','-i',sc['src'],'-i',ov,
                 '-filter_complex',vf,'-frames:v',str(int(d*30)),'-r','30',
                 '-c:v','libx264','-crf','19','-preset','veryfast','-pix_fmt','yuv420p',out+'.tmp.mp4'])
        else:
            run(['ffmpeg','-y','-v','error','-loop','1','-i',ov,
                 '-vf',f'scale={W}:{H},fps=30,setsar=1,format=yuv420p','-frames:v',str(int(d*30)),'-r','30',
                 '-c:v','libx264','-crf','19','-preset','veryfast','-pix_fmt','yuv420p',out+'.tmp.mp4'])
        os.replace(out+'.tmp.mp4',out); partes.append(out)
    lst=f'{tmp}/list.txt'
    open(lst,'w').write(''.join(f"file '{p}'\n" for p in partes))
    mudo=f'{tmp}/mudo.mp4'
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,'-c','copy',mudo])
    final=OUT+'reel-lluvias.mp4'
    run(['ffmpeg','-y','-v','error','-i',mudo,'-i',VOZ,'-map','0:v','-map','1:a',
         '-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',final+'.tmp.mp4'])
    os.replace(final+'.tmp.mp4',final)
    print('listo', final)

if __name__=='__main__': main()
