# Newsletter N° 9 (sábado 21/11/2026). Toma el N° 8 como molde y cambia solo el contenido editorial:
# los bloques de anunciantes quedan exactamente igual.
# Uso: python3 herramientas/newsletter_n09.py   (desde la raiz del repo)
import json, re, html
R='/home/claude/larevista-notas/'
h=open(R+'site/newsletter-n8-1911.html',encoding='utf-8').read()
N={x['id']:x for x in json.load(open(R+'notas.json',encoding='utf-8'))}
UTM='n09'; NB=' '
def url(i): return f'https://energiaslatam.com/n/{i}?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign={UTM}'
def img(i,n=1): return f'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/img/{i}-{n}.jpg'
def esc(t): return html.escape(t,quote=False).replace(' %',NB+'%')
def sub1(pat,rep,s,flags=re.S):
    out,n=re.subn(pat,lambda m:rep,s,count=1,flags=flags)
    assert n==1, 'no encontre: '+pat[:60]
    return out

DEST='2026-11-21-media-hora-para-cargar-estaciones-cliente-electrico'
TAMBIEN=['2026-11-20-petropar-cargadores-electricos-estaciones-licitacion-dncp','2026-11-19-hay-petroleo-en-paraguay-petropar-cancela-consultoria-chaco',
         '2026-11-20-cuanto-cuesta-gasolina-bolivia-subsidio-9000-millones']
MAS=['2026-11-20-cuanto-gana-estacion-de-servicio-colombia-margen-minimo','2026-11-19-brasil-estaciones-biometano-camiones-ultragaz']
for i in [DEST]+TAMBIEN+MAS: assert N[i]['estado']=='publicada', i

# 1) encabezado
h=h.replace('<title>La Estación del Futuro · N° 8</title>','<title>La Estación del Futuro · N° 9</title>')
assert 'NEWSLETTER · N° 8 · JUEVES 19 DE NOVIEMBRE 2026' in h
h=h.replace('NEWSLETTER · N° 8 · JUEVES 19 DE NOVIEMBRE 2026','NEWSLETTER · N° 9 · SÁBADO 21 DE NOVIEMBRE 2026')
h=sub1(r'(?<=<div style="display:none;max-height:0;overflow:hidden">).*?(?=</div>)',
 f'Media hora para cargar un auto eléctrico: cuánto cuesta el cargador y qué tiene que ofrecer la tienda. Además, la licitación de Petropar y la gasolina en Bolivia.',h)
h=sub1(r'(?<=<p style="margin:0 0 6px 0;font-size:16px;line-height:1.55">).*?(?=</p></td></tr>)',
 'El cliente eléctrico llega, enchufa y tiene media hora por delante. Esta edición abre con esa media hora: cuánto dura la espera según el cargador, cuánto cuesta dar el primer paso y qué tiene que ofrecer la estación para que el cliente entre a la tienda y vuelva. La semana dejó además la licitación de cargadores de Petropar, frenada por Contrataciones Públicas, la cancelación del estudio para atraer exploración petrolera al Chaco y dos espejos de la región: lo que cuesta la gasolina en Bolivia y lo que gana una estación en Colombia.',h)

# 2) lo mas importante en 30 segundos
B=[('🔌','Cliente eléctrico:','sumar 30 kWh lleva unos <b>12 minutos</b> con 150 kW, <b>30</b> con 60 kW y más de una hora con 22 kW. La pregunta es qué le ofrece la tienda mientras espera.'),
   ('⚡','Petropar:','Contrataciones Públicas frenó la licitación de cargadores, de <b>G. 13.994 millones</b>, y ordenó corregir el pliego. Cada punto pide <b>90 kW</b> y transformador propio.'),
   ('🛢️','Petróleo:','Petropar canceló la consultoría de <b>USD 837.566</b> para atraer exploración al Chaco. Tiene seis bloques y <b>5,6 millones</b> de hectáreas sin un pozo perforado.'),
   ('🇧🇴','Bolivia:','la gasolina cuesta <b>Bs 6,96</b> por litro, casi la mitad que en Paraguay, y el techo del subsidio subió a <b>Bs 9.000 millones</b>. El diésel ya es más caro allá.'),
   ('🇨🇴','Colombia:',f'una estación gana <b>35 centavos</b> de dólar por galón y el gremio pide un piso del <b>90{NB}%</b>.'),
   ('🇧🇷','Brasil:','Ultragaz abrió dos estaciones de biometano para camiones y planea <b>20</b>: carga en 8 a 12 minutos, sin gasoducto.')]
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
def linea(i):
    n=N[i]
    return (f'<div style="padding:7px 0;border-bottom:1px solid #E3E8EE;font-size:15px;line-height:1.35"><a href="{url(i)}" style="color:#0F213D;text-decoration:none">'
            f'<b style="color:#3A963E;font-size:11px;letter-spacing:1px;text-transform:uppercase">{esc(n["cat"])}</b><br>{esc(n["titulo"])}</a></div>')
a=h.index(MASH)+len(MASH); b=h.index('</td></tr>',a)
h=h[:a]+''.join(linea(i) for i in MAS)+h[b:]

# 6) resto: utm, mapa y despedida
h=h.replace('utm_campaign=n08','utm_campaign='+UTM)
assert 'Hasta el sábado,' in h; h=h.replace('Hasta el sábado,','Hasta el lunes,')
open(R+'site/newsletter-n9-2111.html','w',encoding='utf-8').write(h)
print('ok', len(h),'bytes')

# 7) variante "sumate" para las listas que todavia no estan inscriptas (pedido de Diego 19/11):
#    mismo contenido + recuadro de invitacion arriba y otro antes del cierre, y pie sin la frase "te inscribiste".
CTA='https://energiaslatam.com/newsletter?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign=n09sumate'
caja=('\n<div style="margin:16px 0 4px 0;padding:18px 20px;background:#EAF6EA;border-left:4px solid #3A963E;border-radius:4px;font-family:Arial,Helvetica,sans-serif">\n'
 '<div style="font-size:18px;font-weight:bold;color:#0F213D;line-height:1.3">Sumate y no te lo pierdas</div>\n'
 '<div style="margin-top:8px;font-size:14px;line-height:1.55;color:#33475B">Esta es una edición de La Estación del Futuro, el newsletter del sector de combustibles y estaciones de servicio. Si querés recibirlo gratis cada lunes, jueves y sábado, anotate con un clic.</div>\n'
 f'<a href="{CTA}" style="display:inline-block;margin-top:14px;background:#3A963E;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:12px 22px;border-radius:4px">Quiero recibirlo gratis</a>\n</div>')
s=h
ancla='</p></td></tr>\n<tr><td style="padding:4px 28px 18px 28px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid #E3E8EE'
assert s.count(ancla)==1
s=s.replace(ancla,'</p>'+caja+ancla[4:])
# segundo llamado, justo antes de la despedida
desp='<tr><td style="padding:0 28px 26px 28px;font-size:15px;line-height:1.5">Hasta el lunes,'
assert s.count(desp)==1
s=s.replace(desp,'<tr><td style="padding:0 28px 22px 28px">'+caja.replace('margin:16px 0 4px 0','margin:0')+'</td></tr>\n'+desp)
pie='Recibís este mail porque te inscribiste en Energías Paraguay o en energiaslatam.com.'
assert s.count(pie)==1
s=s.replace(pie,'Recibís este mail porque tu contacto forma parte de la comunidad de Energías Paraguay.')
open(R+'site/newsletter-n9-2111-sumate.html','w',encoding='utf-8').write(s)
print('ok sumate', len(s),'bytes')
