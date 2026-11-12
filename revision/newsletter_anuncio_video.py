import subprocess, sys, os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from render import W, H, FPS, BB, BS, BBo, NV, NV2, GL, GR, W1, MU, ease, LOGO, SH, bg, center, tap

def back(t):  # ease con rebote
    t = max(0, min(1, t)); c = 1.70158; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2

def pop_text(im, s, font, color, cx, cy, t, dur=0.28):
    """Texto que entra con escala y rebote, centrado en (cx, cy)."""
    if t <= 0: return
    k = back(t / dur); a = min(1, t / (dur * 0.6))
    d0 = ImageDraw.Draw(im); l, u, r, b = d0.textbbox((0, 0), s, font=font)
    tw, th = r - l, b - u
    lay = Image.new('RGBA', (tw + 20, th + 20), (0, 0, 0, 0)); ImageDraw.Draw(lay).text((10 - l, 10 - u), s, font=font, fill=color + (int(255 * a),))
    if abs(k - 1) > 0.004: lay = lay.resize((max(1, int(lay.width * k)), max(1, int(lay.height * k))), Image.BILINEAR)
    im.paste(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)), lay)

def brand(im):
    d = ImageDraw.Draw(im); lg = LOGO.resize((84, int(84 * LOGO.height / LOGO.width))); im.paste(lg, (70, 296), lg)
    d.text((172, 304), 'LA ESTACIÓN', font=BB(52), fill=W1); d.text((172 + d.textlength('LA ESTACIÓN ', font=BB(52)), 304), 'DEL FUTURO', font=BB(52), fill=GL)
    d.text((174, 356), 'Newsletter gratis', font=BS(28), fill=MU)

def pills(im, cur):
    d = ImageDraw.Draw(im); x = W - 70 - 3 * 78
    for i in range(3):
        on = i + 1 <= cur; x0 = x + i * 78
        d.rounded_rectangle([x0, 312, x0 + 62, 374], 31, fill=GR if on else NV2, outline=GL if i + 1 == cur else None, width=4)
        s = str(i + 1); tw = d.textlength(s, font=BBo(34)); d.text((x0 + 31 - tw / 2, 322), s, font=BBo(34), fill=(255, 255, 255) if on else MU)

def phone2(im, shot, top, ph, t, zoom=(1.0, 1.06), focus=(0.5, 0.5), zt=2.2):
    sw, shh = shot.size; pw = int(ph * sw / shh); x = (W - pw) // 2
    a = back(min(1, t / 0.4)); y = top + int(300 * (1 - a))
    z = zoom[0] + (zoom[1] - zoom[0]) * ease(t / zt)
    cw, ch = sw / z, shh / z; cx = focus[0] * sw; cy = focus[1] * shh
    l = max(0, min(sw - cw, cx - cw / 2)); u = max(0, min(shh - ch, cy - ch / 2))
    crop = shot.crop((int(l), int(u), int(l + cw), int(u + ch))).resize((pw, ph), Image.BILINEAR)
    bez, R = 22, 64
    sh = Image.new('RGBA', (pw + 2 * bez + 80, ph + 2 * bez + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([40, 50, pw + 2 * bez + 40, ph + 2 * bez + 50], R + bez, fill=(0, 0, 0, 130))
    sh = sh.filter(ImageFilter.GaussianBlur(20)); im.paste(sh, (x - bez - 40, y - bez - 40), sh)
    body = Image.new('RGBA', (pw + 2 * bez, ph + 2 * bez), (0, 0, 0, 0)); db = ImageDraw.Draw(body)
    db.rounded_rectangle([0, 0, pw + 2 * bez - 1, ph + 2 * bez - 1], R + bez, fill=(10, 14, 22, 255), outline=(70, 86, 110, 255), width=3)
    m = Image.new('L', (pw, ph), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, pw - 1, ph - 1], R, fill=255)
    body.paste(crop, (bez, bez), m); im.paste(body, (x - bez, y - bez), body)
    return (x, y, pw / cw, l, u)

def head(im, big, sub, t, num=None):
    """Título grande (y≈470) y bajada (y≈590), dentro de la zona segura."""
    x = 70
    if num:
        k = back(min(1, t / 0.3)); r = int(62 * k); d = ImageDraw.Draw(im)
        d.ellipse([x + 62 - r, 492 - r, x + 62 + r, 492 + r], fill=GR)
        if k > 0.6: s = str(num); tw = d.textlength(s, font=BB(96)); d.text((x + 62 - tw / 2, 492 - 50), s, font=BB(96), fill=(255, 255, 255))
        x += 150
    d = ImageDraw.Draw(im); f = BB(132); tw = d.textlength(big, font=f)
    pop_text(im, big, f, W1, x + tw / 2, 492, t - 0.08)
    a = ease((t - 0.3) / 0.3)
    if a > 0:
        lay = Image.new('RGBA', (W, 70), (0, 0, 0, 0)); ImageDraw.Draw(lay).text((72, 6), sub, font=BS(44), fill=GL + (int(255 * a),))
        im.paste(lay, (int(-40 * (1 - a)), 588), lay)

def hook(t):
    im = bg(); brand(im)
    pop_text(im, '¿TENÉS UNA', BB(150), W1, W / 2, 640, t - 0.05)
    pop_text(im, 'ESTACIÓN', BB(300), GL, W / 2, 860, t - 0.35)
    pop_text(im, 'DE SERVICIO?', BB(190), W1, W / 2, 1080, t - 0.65)
    a = ease((t - 1.1) / 0.3)
    if a > 0:
        d = ImageDraw.Draw(im); bw, bh = 720, 104; bx = (W - bw) // 2; by = 1220 + int(40 * (1 - a))
        d.rounded_rectangle([bx, by, bx + bw, by + bh], 52, fill=GR); center(d, by + 24, 'Esto es para vos', BBo(52), (255, 255, 255))
    return im

def mail(t):
    im = bg(); brand(im)
    pop_text(im, 'TODO EL SECTOR,', BB(132), W1, 70 + ImageDraw.Draw(im).textlength('TODO EL SECTOR,', font=BB(132)) / 2, 480, t - 0.05)
    pop_text(im, 'EN TU MAIL', BB(132), GL, 70 + ImageDraw.Draw(im).textlength('EN TU MAIL', font=BB(132)) / 2, 600, t - 0.25)
    a = ease((t - 0.5) / 0.3)
    if a > 0: ImageDraw.Draw(im).text((72, 680), 'Precios, notas y datos. Gratis.', font=BS(44), fill=MU)
    p = ease(max(0, t - 0.5) / 1.9); y = int(60 + 2100 * p)
    phone2(im, SH['N4'].crop((0, y, 742, y + 1608)), 800, 1500, t - 0.15, (1.0, 1.0))
    return im

SH['N2c'] = SH['N2'].crop((0, 420, 742, 1608))
def step(num, big, sub, key, zoom, focus, taps=(), confetti=False, ph=1500):
    def f(t):
        im = bg(); brand(im); pills(im, num); head(im, big, sub, t, num)
        m = phone2(im, SH[key], 720, ph, t - 0.1, zoom, focus)
        for (sx, sy, t0) in taps: tap(im, int(m[0] + (sx - m[3]) * m[2]), int(m[1] + (sy - m[4]) * m[2]), t - t0)
        if confetti and t > 0.45:
            rnd = random.Random(7); d = ImageDraw.Draw(im, 'RGBA'); tt = t - 0.45
            for i in range(70):
                ang = rnd.uniform(-math.pi, 0); v = rnd.uniform(500, 1500); cx = W / 2 + math.cos(ang) * v * tt; cy = 900 + math.sin(ang) * v * tt + 900 * tt * tt
                s = rnd.randint(12, 24); col = rnd.choice([GL, (255, 255, 255), (245, 184, 46), GR]); al = int(255 * max(0, 1 - tt / 1.5))
                d.rectangle([cx, cy, cx + s, cy + s * 0.6], fill=col + (al,))
        return im
    return f

def outro(t):
    im = bg(); d = ImageDraw.Draw(im)
    lg = LOGO.resize((170, int(170 * LOGO.height / LOGO.width))); im.paste(lg, ((W - 170) // 2, 320), lg)
    pop_text(im, 'SUSCRIBITE', BB(230), W1, W / 2, 660, t - 0.05)
    pop_text(im, 'GRATIS', BB(300), GL, W / 2, 880, t - 0.3)
    a = ease((t - 0.6) / 0.3)
    if a > 0:
        center(d, 1030, 'El newsletter de las estaciones de servicio', BS(42), MU)
        pul = 1 + 0.035 * math.sin((t - 0.6) * 2 * math.pi * 2)
        bw, bh = int(860 * pul), int(132 * pul); bx = (W - bw) // 2; by = 1180 - bh // 2
        d.rounded_rectangle([bx, by, bx + bw, by + bh], 36, fill=GR, outline=GL, width=4)
        center(d, 1180 - 30, 'energiaslatam.com/newsletter', BBo(52), (255, 255, 255))
    b = ease((t - 1.0) / 0.3)
    if b > 0:
        center(d, 1300, 'Tocá el botón y sumate', BBo(46), W1)
        yb = 1390 + int(18 * abs(math.sin(t * 2 * math.pi * 1.0)))
        d.polygon([(W / 2 - 46, yb), (W / 2 + 46, yb), (W / 2, yb + 56)], fill=GL)
    return im

SC = [
    ('hook', hook, 2.0),
    ('mail', mail, 2.5),
    ('p1', step(1, 'ENTRÁ', 'energiaslatam.com/newsletter', 'N1', (1.0, 1.08), (0.5, 0.35)), 2.0),
    ('p2', step(2, 'DEJÁ TU MAIL', 'Nombre y correo. Nada más.', 'N2c', (1.0, 1.0), (0.5, 0.5), [(371, 284, 0.6), (371, 442, 1.1), (371, 733, 1.7)], ph=1300), 2.5),
    ('p3', step(3, '¡LISTO!', 'Ya estás suscripto', 'N3', (1.0, 1.1), (0.5, 0.42), confetti=True), 2.0),
    ('outro', outro, 3.5),
]
TR = 0.2
def render_scene(i):
    name, fn, dur = SC[i]; prev = SC[i - 1][1](SC[i - 1][2]) if i else None
    tmp = f'tmp_{name}.mp4'
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
    for k in range(int(round(dur * FPS))):
        t = k / FPS; fr = fn(t)
        if prev is not None and t < TR:  # empuje hacia la izquierda
            e = ease(t / TR); off = int(W * e); c = Image.new('RGB', (W, H)); c.paste(prev, (-off, 0)); c.paste(fr, (W - off, 0)); fr = c
        p.stdin.write(fr.tobytes())
    p.stdin.close()
    if p.wait() == 0: os.replace(tmp, f'sc_{name}.mp4')
    else: sys.exit('fallo ' + name)

if __name__ == '__main__':
    if sys.argv[1] == 'stills':
        pts = [(0, 1.6), (1, 1.5), (2, 1.2), (3, 1.9), (4, 1.0), (5, 2.2)]
        ims = [SC[i][1](t).resize((360, 640)) for i, t in pts]
        s = Image.new('RGB', (360 * 6, 640)); [s.paste(im, (k * 360, 0)) for k, im in enumerate(ims)]; s.save(sys.argv[2], quality=88)
    elif sys.argv[1] == 'scene':
        for i in map(int, sys.argv[2:]): render_scene(i); print('ok', SC[i][0])
