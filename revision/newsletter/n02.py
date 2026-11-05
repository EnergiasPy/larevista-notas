from gen import make
U=lambda p:f'https://energiaslatam.com/{p}?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign=n02'
make(2,'NEWSLETTER · N° 2 · JUEVES 5 DE NOVIEMBRE 2026',
 'Deflación en octubre, pero el gasoil subió 5,4 %. Petropar congela el diésel, el petróleo en baja y el nuevo mapa de estaciones.',
 'Desde hoy, <b>La Estación del Futuro</b> te llega tres veces por semana: <b>lunes, jueves y sábado</b>, con la nota destacada y lo más importante del sector.',
 ['📉 Octubre cerró con <b>deflación de 0,1 %</b>, pero el gasoil común <b>subió 5,4 %</b> en el mes.',
  '⛽ Petropar mantiene el diésel <b>sin cambios hasta fin de noviembre</b>: el Porã sigue a G. 9.285.',
  '🛢️ El petróleo <b>cayó casi 9 % en dos días</b>; la baja todavía no llega al surtidor.',
  '🗺️ <b>Nuevo:</b> el mapa interactivo con las <b>2.883 estaciones</b> del país.'],
 '2026-11-05-deflacion-octubre-gasoil',
 ['2026-11-03-petropar-congela-diesel-noviembre','2026-11-04-petroleo-cae-dos-dias-diesel','2026-11-04-cada-cliente-oportunidad'],
 ['2026-11-03-ueno-estaciones-cobros','2026-11-02-camioneros-flete-ventas-diesel'],
 f'🗺️ <b>Nuevo: mapa interactivo de estaciones.</b> Las 2.883 del país, por emblema, departamento y ciudad. <a href="{U("estaciones")}" style="color:#0F213D;font-weight:bold">Abrir el mapa</a><br>📄 <b>Informe del MIC gratis:</b> ranking por emblema, precios, estaciones y GLP, en PDF. <a href="{U("combustible/py")}" style="color:#0F213D;font-weight:bold">Pedilo acá</a><br>📊 <b>Datos del sector</b> de Paraguay, Uruguay, Chile, Perú y Bolivia. <a href="{U("combustible")}" style="color:#0F213D;font-weight:bold">Ver los datos</a>',
 'Hasta el sábado,','n02','/home/claude/larevista-notas/site/newsletter-n2-0511.html')
