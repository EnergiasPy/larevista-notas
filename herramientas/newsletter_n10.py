# Newsletter N° 10 (lunes 23/11/2026). Toma el N° 9 como molde y cambia solo el contenido editorial:
# los bloques de anunciantes quedan exactamente igual.
# Uso: python3 herramientas/newsletter_n10.py   (desde la raiz del repo)
import json, re, html
R='/home/claude/larevista-notas/'
h=open(R+'site/newsletter-n9-2111.html',encoding='utf-8').read()
N={x['id']:x for x in json.load(open(R+'notas.json',encoding='utf-8'))}
UTM='n10'; NB=' '
def url(i): return f'https://energiaslatam.com/n/{i}?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign={UTM}'
def img(i,n=1): return f'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/img/{i}-{n}.jpg'
def esc(t): return html.escape(t,quote=False).replace(' %',NB+'%')
def sub1(pat,rep,s,flags=re.S):
    out,n=re.subn(pat,lambda m:rep,s,count=1,flags=flags)
    assert n==1, 'no encontre: '+pat[:60]
    return out

DEST='2026-11-21-ranking-ventas-combustibles-octubre-2026'
TAMBIEN=['2026-11-23-bajara-el-combustible-en-paraguay-petroleo-dolar','2026-11-22-cuantos-litros-vende-estacion-de-servicio-paraguay',
         '2026-11-21-cuanto-le-cuesta-al-estado-la-baja-del-diesel']
MAS=['2026-11-21-cuanto-gana-estacion-de-servicio-argentina-margen','2026-11-22-cuanto-gana-estacion-de-servicio-chile-margen']
for i in [DEST]+TAMBIEN+MAS: assert N[i]['estado']=='publicada', i

# 1) encabezado
h=h.replace('<title>La Estación del Futuro · N° 9</title>','<title>La Estación del Futuro · N° 10</title>')
assert 'NEWSLETTER · N° 9 · SÁBADO 21 DE NOVIEMBRE 2026' in h
h=h.replace('NEWSLETTER · N° 9 · SÁBADO 21 DE NOVIEMBRE 2026','NEWSLETTER · N° 10 · LUNES 23 DE NOVIEMBRE 2026')
h=sub1(r'(?<=<div style="display:none;max-height:0;overflow:hidden">).*?(?=</div>)',
 f'Ranking de octubre: Petropar lidera y el gasoil cayó 15 % en un mes. Además, por qué el dólar frena la baja de diciembre y cuántos litros vende una estación paraguaya.',h)
h=sub1(r'(?<=<p style="margin:0 0 6px 0;font-size:16px;line-height:1.55">).*?(?=</p></td></tr>)',
 'Octubre dejó dos datos para mirar con lupa: el gasoil cayó 15 % en un solo mes y, de las cinco marcas que más venden, solo Petropar despachó más que hace un año. Esta edición abre con el ranking completo del MIC y sigue con una cuenta que sale de esos mismos números: cuántos litros vende, en promedio, cada estación del país. También va la pregunta de la semana, si el combustible baja en diciembre: el petróleo cayó 21 %, pero el dólar volvió a subir. Y, además, el costo fiscal de la baja del diésel y cuánto le queda por litro a una estación en la Argentina y en Chile.',h)

# 2) lo mas importante en 30 segundos
B=[('📊','Ranking de octubre:',f'se vendieron <b>300,5 millones</b> de litros, 6,8{NB}% menos que en septiembre. Petropar lideró con <b>21,6{NB}%</b> del mercado y el gasoil tipo III cayó <b>15,1{NB}%</b> en un mes.'),
   ('💵','¿Baja en diciembre?:',f'el petróleo cayó <b>21{NB}%</b> desde fin de octubre, pero el dólar pasó de G. 6.200 a <b>G. 6.390</b> en diez días. El barril en guaraníes bajó solo <b>12{NB}%</b>.'),
   ('⛽','Litros por estación:','una estación paraguaya vende en promedio unos <b>104.000 litros</b> por mes; una de Petropar, unos <b>215.000</b>. La cuenta, emblema por emblema.'),
   ('💰','Diésel:','la rebaja del impuesto le cuesta al Estado unos <b>US$ 9,5 millones</b> en dos meses. Rige hasta el 31 de diciembre: sin prórroga, en enero el impuesto vuelve a subir <b>G. 340</b> por litro.'),
   ('🇦🇷','Argentina:',f'a la estación le queda cerca del <b>8{NB}%</b> del surtidor, y los gremios dicen que hoy hacen falta unos <b>350.000 litros</b> para cubrir los costos.'),
   ('🇨🇱','Chile:','el margen de comercialización es de <b>75 pesos</b> por litro de gasolina en Santiago, y el último dato oficial es de agosto de 2024.')]
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
h=h.replace('utm_campaign=n09','utm_campaign='+UTM)
assert 'Hasta el lunes,' in h; h=h.replace('Hasta el lunes,','Hasta el jueves,')
open(R+'site/newsletter-n10-2311.html','w',encoding='utf-8').write(h)
print('ok', len(h),'bytes')

# 7) variante "sumate" para las listas que todavia no estan inscriptas (pedido de Diego 19/11):
#    mismo contenido + recuadro de invitacion arriba y otro antes del cierre, y pie sin la frase "te inscribiste".
CTA='https://energiaslatam.com/newsletter?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign=n10sumate'
caja=('\n<div style="margin:16px 0 4px 0;padding:18px 20px;background:#EAF6EA;border-left:4px solid #3A963E;border-radius:4px;font-family:Arial,Helvetica,sans-serif">\n'
 '<div style="font-size:18px;font-weight:bold;color:#0F213D;line-height:1.3">Sumate y no te lo pierdas</div>\n'
 '<div style="margin-top:8px;font-size:14px;line-height:1.55;color:#33475B">Esta es una edición de La Estación del Futuro, el newsletter del sector de combustibles y estaciones de servicio. Si querés recibirlo gratis cada lunes, jueves y sábado, anotate con un clic.</div>\n'
 f'<a href="{CTA}" style="display:inline-block;margin-top:14px;background:#3A963E;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:12px 22px;border-radius:4px">Quiero recibirlo gratis</a>\n</div>')
s=h
ancla='</p></td></tr>\n<tr><td style="padding:4px 28px 18px 28px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid #E3E8EE'
assert s.count(ancla)==1
s=s.replace(ancla,'</p>'+caja+ancla[4:])
# segundo llamado, justo antes de la despedida
desp='<tr><td style="padding:0 28px 26px 28px;font-size:15px;line-height:1.5">Hasta el jueves,'
assert s.count(desp)==1
s=s.replace(desp,'<tr><td style="padding:0 28px 22px 28px">'+caja.replace('margin:16px 0 4px 0','margin:0')+'</td></tr>\n'+desp)
pie='Recibís este mail porque te inscribiste en Energías Paraguay o en energiaslatam.com.'
assert s.count(pie)==1
s=s.replace(pie,'Recibís este mail porque tu contacto forma parte de la comunidad de Energías Paraguay.')
open(R+'site/newsletter-n10-2311-sumate.html','w',encoding='utf-8').write(s)
print('ok sumate', len(s),'bytes')
