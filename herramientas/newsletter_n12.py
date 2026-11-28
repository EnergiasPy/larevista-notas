# Newsletter N° 12 (sábado 28/11/2026). Toma el N° 11 como molde.
# los bloques de anunciantes quedan exactamente igual.
# Uso: python3 herramientas/newsletter_n12.py   (desde la raiz del repo)
import json, re, html
R='/home/claude/larevista-notas/'
h=open(R+'site/newsletter-n11-2611.html',encoding='utf-8').read()
N={x['id']:x for x in json.load(open(R+'notas.json',encoding='utf-8'))}
UTM='n12'; NB=' '
def url(i): return f'https://energiaslatam.com/n/{i}?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign={UTM}'
def img(i,n=1): return f'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/img/{i}-{n}.jpg'
def esc(t): return html.escape(t,quote=False).replace(' %',NB+'%')
def sub1(pat,rep,s,flags=re.S):
    out,n=re.subn(pat,lambda m:rep,s,count=1,flags=flags)
    assert n==1, 'no encontre: '+pat[:60]
    return out

DEST='2026-11-27-baja-el-gas-de-garrafa-paraguay-petropar-nande-gas'
TAMBIEN=['2026-11-27-b100-biodiesel-puro-barcazas-paraguay-resolucion-908',
         '2026-11-27-gasoducto-bioceanico-vaca-muerta-chaco-paraguay-milei',
         '2026-11-26-paro-nacional-transporte-bolivia-lunes-diesel']
MAS=['2026-11-26-autodespacho-uruguay-estaciones-cargar-uno-mismo']
# si Diego publica Caacupé antes del envío, se agrega acá:
CAACUPE='2026-11-27-restricciones-ruta-2-caacupe-camiones-combustible'
if N[CAACUPE]['estado']=='publicada': MAS.insert(0,CAACUPE)
PEND=[i for i in [DEST]+TAMBIEN+MAS if N[i]['estado']!='publicada']
if PEND: print('OJO, todavia en borrador:',PEND)

# 1) encabezado
h=h.replace('<title>La Estación del Futuro · N° 11</title>','<title>La Estación del Futuro · N° 12</title>')
assert 'NEWSLETTER · N° 11 · JUEVES 26 DE NOVIEMBRE 2026' in h
h=h.replace('NEWSLETTER · N° 11 · JUEVES 26 DE NOVIEMBRE 2026','NEWSLETTER · N° 12 · SÁBADO 28 DE NOVIEMBRE 2026')
h=sub1(r'(?<=<div style="display:none;max-height:0;overflow:hidden">).*?(?=</div>)',
 'Baja el gas de garrafa de Petropar y vienen más anuncios de precios el lunes o el martes. Además, Paraguay habilitó el biodiésel puro B100 para las barcazas.',h)
h=sub1(r'(?<=<p style="margin:0 0 6px 0;font-size:16px;line-height:1.55">).*?(?=</p></td></tr>)',
 'Semana corta y movida. El viernes bajó el gas de garrafa de Petropar, G. 600 por kilo, y el presidente avisó que esa no va a ser la última rebaja: los anuncios que importan para el surtidor quedaron para el lunes o el martes. En el medio, una medida que abre un mercado nuevo para el biodiésel paraguayo, el B100 para embarcaciones, y dos cosas que pasan del otro lado de la frontera: el paro del transporte boliviano desde el lunes y el autodespacho uruguayo, que acá ya funciona y pocos saben.',h)

# 2) lo mas importante en 30 segundos
B=[('⛽','Gas de garrafa:','Petropar bajó <b>G. 600 por kilo</b> el Ñande Gas, <b>G. 6.000</b> la garrafa de 10 kilos. Naftas y diésel no entraron en el anuncio.'),
   ('🗓️','Lo que viene:','Alliana dijo que la rebaja <b>"no va a ser la última"</b> y prometió nuevos anuncios de precios para el <b>lunes o el martes</b>.'),
   ('🚢','B100:','el MIC habilitó el <b>biodiésel puro</b> para abastecer embarcaciones, con puestos de suministro en muelles y atracaderos. La mezcla del surtidor no cambia: B7 hasta el 31 de diciembre.'),
   ('🇦🇷','Gas argentino:','tras la visita de Milei, Paraguay puso sobre la mesa dos proyectos: un gasoducto de <b>1.050 km</b> y <b>USD 2.000 millones</b> por el Chaco, y una conexión desde Formosa. De ninguno se anunció el inicio de obras.'),
   ('🇧🇴','Bolivia:','la Confederación de Choferes anunció <b>paro nacional indefinido desde las 00:00 del lunes 30</b> por la suba del diésel a Bs 20,57. No se anunciaron bloqueos ni cierres de pasos.'),
   ('🇺🇾','Autodespacho:','avanza en Uruguay y en Paraguay ya funciona en <b>más de seis estaciones</b> de Petrosur, con tarjeta en el surtidor, sin aplicación y <b>G. 400 menos</b> por litro.')]
bul=''.join(f'<div style="margin-top:{8 if k==0 else 6}px">{e} <b>{t}</b> {x}</div>' for k,(e,t,x) in enumerate(B))
h=sub1(r'(?<=LO MÁS IMPORTANTE EN 30 SEGUNDOS</b>\n).*?(?=\n</td></tr></table></td></tr>\n<tr><td style="padding:0 28px"><div[^>]*>LA NOTA DESTACADA)',bul,h)

# 3) nota destacada
n=N[DEST]
dest=(f'<tr><td style="padding:16px 28px 6px 28px"><a href="{url(DEST)}"><img src="{img(DEST)}" width="544" alt="" style="display:block;width:100%;height:auto;border:0;border-radius:4px"></a>\n'
 f'<div style="margin-top:12px;font-size:11px;font-weight:bold;letter-spacing:1.5px;color:#3A963E;text-transform:uppercase">{esc(n["cat"])}</div>\n'
 f'<a href="{url(DEST)}" style="display:block;margin-top:4px;font-size:22px;line-height:1.25;font-weight:bold;color:#0F213D;text-decoration:none">{esc(n["titulo"])}</a>\n'
 f'<p style="margin:8px 0 14px 0;font-size:15px;line-height:1.55;color:#33475B">{esc(n["bajada"])}</p>\n'
 f'<a href="{url(DEST)}" style="display:inline-block;background:#3A963E;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:12px 22px;border-radius:4px">Leer la nota completa</a></td></tr>')
h=sub1(r'<tr><td style="padding:16px 28px 6px 28px"><a href=.*?Leer la nota completa</a></td></tr>',dest,h)

# 4) tambien en esta edicion (con miniatura)
def item(i):
    n=N[i]
    return ('<tr><td style="padding:0 28px 18px 28px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>\n'
     f'<td width="150" valign="top" style="padding-right:16px"><a href="{url(i)}"><img src="{img(i)}" width="150" alt="" style="display:block;width:150px;height:auto;border:0;border-radius:4px"></a></td>\n'
     f'<td valign="top" style="font-family:Arial,Helvetica,sans-serif"><div style="font-size:11px;font-weight:bold;letter-spacing:1.5px;color:#3A963E;text-transform:uppercase">{esc(n["cat"])}</div>\n'
     f'<a href="{url(i)}" style="display:block;margin-top:4px;font-size:17px;line-height:1.3;font-weight:bold;color:#0F213D;text-decoration:none">{esc(n["titulo"])}</a>\n'
     f'<a href="{url(i)}" style="display:inline-block;margin-top:6px;font-size:14px;color:#3A963E;font-weight:bold;text-decoration:none">Leer →</a></td></tr></table></td></tr>')
MASH='<tr><td style="padding:0 28px 18px 28px"><div style="font-size:12px;font-weight:bold;letter-spacing:2px;color:#0F213D;padding-bottom:6px">MÁS NOTAS</div>'
a=h.index('TAMBIÉN EN ESTA EDICIÓN</div></td></tr>')+len('TAMBIÉN EN ESTA EDICIÓN</div></td></tr>')
b=h.index(MASH)
h=h[:a]+'\n'+''.join(item(i) for i in TAMBIEN)+'\n'+h[b:]

# 5) mas notas (solo texto)
PATROCINADAS={}
def linea(i):
    n=N[i]; k=PATROCINADAS.get(i,n['cat'])
    return (f'<div style="padding:7px 0;border-bottom:1px solid #E3E8EE;font-size:15px;line-height:1.35"><a href="{url(i)}" style="color:#0F213D;text-decoration:none">'
            f'<b style="color:#3A963E;font-size:11px;letter-spacing:1px;text-transform:uppercase">{esc(k)}</b><br>{esc(n["titulo"])}</a></div>')
a=h.index(MASH)+len(MASH); b=h.index('</td></tr>',a)
h=h[:a]+''.join(linea(i) for i in MAS)+h[b:]

# 6) resto: utm, mapa y despedida
h=h.replace('utm_campaign=n11','utm_campaign='+UTM)
assert 'Hasta el sábado,' in h; h=h.replace('Hasta el sábado,','Hasta el lunes,')
open(R+'site/newsletter-n12-2811.html','w',encoding='utf-8').write(h)
print('ok', len(h),'bytes')

# 7) variante "sumate" para las listas que todavia no estan inscriptas (pedido de Diego 19/11)
CTA='https://energiaslatam.com/newsletter?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign=n12sumate'
caja=('\n<div style="margin:16px 0 4px 0;padding:18px 20px;background:#EAF6EA;border-left:4px solid #3A963E;border-radius:4px;font-family:Arial,Helvetica,sans-serif">\n'
 '<div style="font-size:18px;font-weight:bold;color:#0F213D;line-height:1.3">Sumate y no te lo pierdas</div>\n'
 '<div style="margin-top:8px;font-size:14px;line-height:1.55;color:#33475B">Esta es una edición de La Estación del Futuro, el newsletter del sector de combustibles y estaciones de servicio. Si querés recibirlo gratis cada lunes, jueves y sábado, anotate con un clic.</div>\n'
 f'<a href="{CTA}" style="display:inline-block;margin-top:14px;background:#3A963E;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:12px 22px;border-radius:4px">Quiero recibirlo gratis</a>\n</div>')
s=h
ancla='</p></td></tr>\n<tr><td style="padding:4px 28px 18px 28px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid #E3E8EE'
assert s.count(ancla)==1
s=s.replace(ancla,'</p>'+caja+ancla[4:])
desp='<tr><td style="padding:0 28px 26px 28px;font-size:15px;line-height:1.5">Hasta el lunes,'
assert s.count(desp)==1
s=s.replace(desp,'<tr><td style="padding:0 28px 22px 28px">'+caja.replace('margin:16px 0 4px 0','margin:0')+'</td></tr>\n'+desp)
pie='Recibís este mail porque te inscribiste en Energías Paraguay o en energiaslatam.com.'
assert s.count(pie)==1
s=s.replace(pie,'Recibís este mail porque tu contacto forma parte de la comunidad de Energías Paraguay.')
open(R+'site/newsletter-n12-2811-sumate.html','w',encoding='utf-8').write(s)
print('ok sumate', len(s),'bytes')
