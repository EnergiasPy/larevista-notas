# Newsletter N° 8 (jueves 19/11/2026). Toma el N° 7 como molde y cambia solo el contenido editorial:
# los bloques de anunciantes quedan exactamente igual.
# Uso: python3 herramientas/newsletter_n08.py   (desde la raiz del repo)
import json, re, html
R='/home/claude/larevista-notas/'
h=open(R+'site/newsletter-n7-1611.html',encoding='utf-8').read()
N={x['id']:x for x in json.load(open(R+'notas.json',encoding='utf-8'))}
UTM='n08'; NB=' '
def url(i): return f'https://energiaslatam.com/n/{i}?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign={UTM}'
def img(i,n=1): return f'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/img/{i}-{n}.jpg'
def esc(t): return html.escape(t,quote=False).replace(' %',NB+'%')
def sub1(pat,rep,s,flags=re.S):
    out,n=re.subn(pat,lambda m:rep,s,count=1,flags=flags)
    assert n==1, 'no encontre: '+pat[:60]
    return out

DEST='2026-11-19-donde-cargan-buses-electricos-san-lorenzo'
TAMBIEN=['2026-11-17-cuantas-estaciones-hay-paraguay-red-emblemas','2026-11-18-itaipu-tarifa-vence-31-diciembre-anexo-c',
         '2026-11-18-cuida-tu-combustible-tapas-agua-lluvias','2026-11-17-autogas-cae-estaciones-industria-glp']
MAS=['2026-11-18-ecuador-margen-estacion-congelado','2026-11-17-peru-grifos-inventario-diario-osinergmin-sunat','2026-11-16-uruguay-unvenu-impuestos-autoservicio']
for i in [DEST]+TAMBIEN+MAS: assert N[i]['estado']=='publicada', i

# 1) encabezado
h=h.replace('<title>La Estación del Futuro · N° 7</title>','<title>La Estación del Futuro · N° 8</title>')
h=h.replace('NEWSLETTER · N° 7 · LUNES 16 DE NOVIEMBRE 2026','NEWSLETTER · N° 8 · JUEVES 19 DE NOVIEMBRE 2026')
h=sub1(r'(?<=<div style="display:none;max-height:0;overflow:hidden">).*?(?=</div>)',
 f'Seis cargadores de 180 kW para treinta buses, 2.880 estaciones en el registro del MIC y la tarifa de Itaipú, que vence el 31 de diciembre.',h)
h=sub1(r'(?<=<p style="margin:0 0 6px 0;font-size:16px;line-height:1.55">).*?(?=</p></td></tr>)',
 'Treinta colectivos, seis cargadores rápidos de 180 kW y 1.500 kW de infraestructura eléctrica en un solo predio: esta edición abre con la base donde cargan los buses eléctricos del Estado, y con lo que ese número le dice a cualquier estación que piense en vender energía. Además, procesamos el registro del MIC para ver cómo se reparte la red de 2.880 estaciones, repasamos qué se juega con la tarifa de Itaipú antes de fin de año y dejamos una guía corta para que las lluvias no te metan agua en el tanque.',h)

# 2) lo mas importante en 30 segundos
B=[('🔌','Buses eléctricos:',f'la base de San Lorenzo tiene seis cargadores rápidos de <b>180 kW</b> y <b>1.500 kW</b> de infraestructura. Cada unidad rinde <b>60 km</b>: por eso carga varias veces por día.'),
   ('🗺️','La red:',f'<b>2.880</b> estaciones habilitadas y ninguna sin bandera. Cinco marcas tienen el <b>51,3{NB}%</b> y todo el Chaco suma 90 bocas.'),
   ('⚡','Itaipú:','la tarifa de <b>US$ 19,28</b> por kilovatio-mes vence el 31 de diciembre, y Brasil ya anticipó que quiere una considerablemente menor.'),
   ('💧','Lluvias:','el agua no entra por el techo, entra por la tapa del tanque. Tres verificaciones de menos de media hora.'),
   ('🔥','GLP:',f'el autogas cae <b>11{NB}%</b> en las estaciones mientras la industria compra <b>15{NB}%</b> más gas.'),
   ('🌎','Región:','en Ecuador el margen del diésel es de <b>12 centavos</b> por galón, congelado hace 23 años; en Perú, el grifo que no declara su stock no puede comprar.')]
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
h=h.replace('utm_campaign=n07','utm_campaign='+UTM)
h=h.replace('las 2.883 del país','las 2.880 del país')
assert 'Hasta el jueves,' in h; h=h.replace('Hasta el jueves,','Hasta el sábado,')
open(R+'site/newsletter-n8-1911.html','w',encoding='utf-8').write(h)
print('ok', len(h),'bytes')
