# Newsletter N° 11 (jueves 26/11/2026). Toma el N° 10 como molde.
# los bloques de anunciantes quedan exactamente igual.
# Uso: python3 herramientas/newsletter_n10.py   (desde la raiz del repo)
import json, re, html
R='/home/claude/larevista-notas/'
h=open(R+'site/newsletter-n10-2311.html',encoding='utf-8').read()
N={x['id']:x for x in json.load(open(R+'notas.json',encoding='utf-8'))}
UTM='n11'; NB=' '
def url(i): return f'https://energiaslatam.com/n/{i}?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign={UTM}'
def img(i,n=1): return f'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/img/{i}-{n}.jpg'
def esc(t): return html.escape(t,quote=False).replace(' %',NB+'%')
def sub1(pat,rep,s,flags=re.S):
    out,n=re.subn(pat,lambda m:rep,s,count=1,flags=flags)
    assert n==1, 'no encontre: '+pat[:60]
    return out

DEST='2026-11-26-300-millones-obras-publicas-diciembre-estaciones'
TAMBIEN=['2026-11-25-gulf-paraguay-lanzamiento-modelo-licencia-operadores','2026-11-24-cuanto-cuesta-el-diesel-en-bolivia-sube-a-bs-20-57',
         '2026-11-24-cuanto-gana-una-gasolinera-en-mexico-margen']
MAS=['2026-11-24-gulf-paraguay-30-estaciones-anjor-lanzamiento','2026-11-25-shell-cinco-anos-paraguay-290-estaciones']
PEND=[i for i in [DEST]+TAMBIEN+MAS if N[i]['estado']!='publicada']
if PEND: print('OJO, todavia en borrador:',PEND)

# 1) encabezado
h=h.replace('<title>La Estación del Futuro · N° 10</title>','<title>La Estación del Futuro · N° 11</title>')
assert 'NEWSLETTER · N° 10 · LUNES 23 DE NOVIEMBRE 2026' in h
h=h.replace('NEWSLETTER · N° 10 · LUNES 23 DE NOVIEMBRE 2026','NEWSLETTER · N° 11 · JUEVES 26 DE NOVIEMBRE 2026')
h=sub1(r'(?<=<div style="display:none;max-height:0;overflow:hidden">).*?(?=</div>)',
 f'Hasta US$ 300 millones para obras viales en diciembre y US$ 931 millones previstos para 2027. Además, Gulf se presentó en Paraguay y el diésel boliviano ya es más caro que el nuestro.',h)
h=sub1(r'(?<=<p style="margin:0 0 6px 0;font-size:16px;line-height:1.55">).*?(?=</p></td></tr>)',
 'La obra pública vuelve a moverse, y eso se siente en el surtidor: el Gobierno anunció hasta US$ 300 millones para el sector vial en diciembre, con la mitad sujeta a que el Congreso apruebe un crédito, y prevé US$ 931 millones para 2027, con prioridad en el mantenimiento de rutas. Esta edición abre con eso y con lo que puede significar para una estación cerca de una obra parada. Sigue con el desembarco de Gulf, que ya se presentó en Asunción y le habló a los operadores independientes, y con dos datos de la región: el diésel boliviano, que subió 14,6 % en una noche y hoy es más caro que el paraguayo, y cuánto le queda por litro a una gasolinera mexicana.',h)

# 2) lo mas importante en 30 segundos
B=[('🛣️','Obras viales:',f'el Gobierno anunció <b>hasta US$ 300 millones</b> para diciembre: <b>US$ 150 millones</b> ya disponibles y otros <b>US$ 150 millones</b> sujetos a que el Congreso apruebe un crédito.'),
   ('🏗️','2027:','la inversión prevista en obras sube a <b>US$ 931 millones</b>, contra US$ 570 millones este año, con prioridad en la reparación y el mantenimiento de rutas.'),
   ('⛽','Gulf:','la marca se presentó en Asunción y prevé <b>30 cambios de emblema</b> en la primera etapa. No opera estaciones ni fija precios: la operación es de ANJOR.'),
   ('🇧🇴','Bolivia:',f'el diésel subió <b>14,6{NB}%</b> en una noche, a <b>Bs 20,57</b> por litro (unos USD 1,75). Ya es más caro que el paraguayo y el transporte evalúa un paro.'),
   ('🇲🇽','México:','a una gasolinera le queda un margen bruto de <b>1,50 pesos</b> por litro de diésel, y el punto de equilibrio promedio se estima en <b>390.000 litros</b> por mes.'),
   ('📉','Gasoil:',f'en octubre el tipo III cayó <b>15,1{NB}%</b> en un mes. Si los pagos permiten retomar obras, las estaciones cercanas podrían recuperar ventas a las flotas.')]
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
PATROCINADAS={'2026-11-25-shell-cinco-anos-paraguay-290-estaciones':'CONTENIDO PATROCINADO POR SHELL'}
def linea(i):
    n=N[i]; k=PATROCINADAS.get(i,n['cat'])
    return (f'<div style="padding:7px 0;border-bottom:1px solid #E3E8EE;font-size:15px;line-height:1.35"><a href="{url(i)}" style="color:#0F213D;text-decoration:none">'
            f'<b style="color:#3A963E;font-size:11px;letter-spacing:1px;text-transform:uppercase">{esc(k)}</b><br>{esc(n["titulo"])}</a></div>')
a=h.index(MASH)+len(MASH); b=h.index('</td></tr>',a)
h=h[:a]+''.join(linea(i) for i in MAS)+h[b:]

# 6) resto: utm, mapa y despedida
h=h.replace('utm_campaign=n10','utm_campaign='+UTM)
assert 'Hasta el jueves,' in h; h=h.replace('Hasta el jueves,','Hasta el sábado,')
open(R+'site/newsletter-n11-2611.html','w',encoding='utf-8').write(h)
print('ok', len(h),'bytes')

# 7) variante "sumate" para las listas que todavia no estan inscriptas (pedido de Diego 19/11):
#    mismo contenido + recuadro de invitacion arriba y otro antes del cierre, y pie sin la frase "te inscribiste".
CTA='https://energiaslatam.com/newsletter?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign=n11sumate'
caja=('\n<div style="margin:16px 0 4px 0;padding:18px 20px;background:#EAF6EA;border-left:4px solid #3A963E;border-radius:4px;font-family:Arial,Helvetica,sans-serif">\n'
 '<div style="font-size:18px;font-weight:bold;color:#0F213D;line-height:1.3">Sumate y no te lo pierdas</div>\n'
 '<div style="margin-top:8px;font-size:14px;line-height:1.55;color:#33475B">Esta es una edición de La Estación del Futuro, el newsletter del sector de combustibles y estaciones de servicio. Si querés recibirlo gratis cada lunes, jueves y sábado, anotate con un clic.</div>\n'
 f'<a href="{CTA}" style="display:inline-block;margin-top:14px;background:#3A963E;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:12px 22px;border-radius:4px">Quiero recibirlo gratis</a>\n</div>')
s=h
ancla='</p></td></tr>\n<tr><td style="padding:4px 28px 18px 28px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid #E3E8EE'
assert s.count(ancla)==1
s=s.replace(ancla,'</p>'+caja+ancla[4:])
# segundo llamado, justo antes de la despedida
desp='<tr><td style="padding:0 28px 26px 28px;font-size:15px;line-height:1.5">Hasta el sábado,'
assert s.count(desp)==1
s=s.replace(desp,'<tr><td style="padding:0 28px 22px 28px">'+caja.replace('margin:16px 0 4px 0','margin:0')+'</td></tr>\n'+desp)
pie='Recibís este mail porque te inscribiste en Energías Paraguay o en energiaslatam.com.'
assert s.count(pie)==1
s=s.replace(pie,'Recibís este mail porque tu contacto forma parte de la comunidad de Energías Paraguay.')
open(R+'site/newsletter-n11-2611-sumate.html','w',encoding='utf-8').write(s)
print('ok sumate', len(s),'bytes')
