/* Portada v2 · actualidad arriba, suscripción como acción principal.
   Reacomoda los bloques existentes de index.html sin borrar contenido ni compromisos comerciales. */
(function () {
  var RAW = 'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/';
  var FREQ = 'todos los lunes';
  function $(s, c) { return (c || document).querySelector(s); }
  function el(h) { var d = document.createElement('div'); d.innerHTML = h.trim(); return d.firstChild; }
  function esc(s) { return String(s || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fecha(f) { var p = (f || '').split('-'); var M = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']; return p.length === 3 ? (+p[2]) + ' de ' + M[+p[1] - 1] + ' de ' + p[0] : ''; }
  function img(n) { if (n.img_abs) return n.img_abs; if (!n.img) return ''; return /^https?:/.test(n.img) ? n.img : RAW + n.img; }

  var css = document.createElement('style');
  css.textContent = [
    '.pv-flag{background:#F5B82E;color:#0F213D;text-align:center;font:700 13px Barlow,Arial,sans-serif;padding:6px 10px;letter-spacing:.3px}',
    '.pv-mast{background:#fff;border-bottom:1px solid #E3E9F0}',
    '.pv-mast .wrap{display:flex;align-items:center;gap:18px;flex-wrap:wrap;padding-top:14px;padding-bottom:14px}',
    '.pv-mast h1{margin:0;font:400 40px/1 "Bebas Neue",sans-serif;color:#0F213D;letter-spacing:.5px}.pv-mast h1 span{color:#3A963E}',
    '.pv-mast p{margin:0;flex:1;min-width:240px;color:#4A5B6C;font:500 16px/1.4 Barlow,Arial,sans-serif}',
    '.pv-btn{display:inline-block;background:#3A963E;color:#fff!important;font:700 15px Barlow,Arial,sans-serif;padding:11px 18px;border-radius:8px;text-decoration:none;white-space:nowrap}',
    '.pv-btn:hover{background:#2E7D32}.pv-btn2{background:transparent;color:#0F213D!important;border:2px solid #0F213D}',
    '.pv-spon{margin:22px 0 0}.pv-spon-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}.pv-spon-h span{font:700 12px Barlow,Arial,sans-serif;letter-spacing:2px;text-transform:uppercase;color:#0F213D}.pv-spon-h small{font:600 11px Barlow,Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;color:#9FB3C8}',
    '.pv-spon-g{display:grid;grid-template-columns:1fr 1fr;gap:14px}',
    '.pv-spon-i{display:flex;align-items:center;gap:16px;background:#fff;border:1px solid #DCE3EA;border-left:6px solid var(--bc);border-radius:10px;padding:14px 18px;text-decoration:none;color:#0F213D;box-shadow:0 2px 8px rgba(15,33,61,.06);transition:box-shadow .2s}',
    '.pv-spon-i:hover{box-shadow:0 6px 18px rgba(15,33,61,.14)}.pv-spon-i img{height:52px;width:auto;max-width:150px;object-fit:contain;flex:none}',
    '.pv-spon-i b{display:block;font:400 26px/1 "Bebas Neue",sans-serif;letter-spacing:.5px}.pv-spon-i small{display:block;color:#4A5B6C;font:600 13px Barlow,Arial,sans-serif;margin-top:2px}',
    '@media(max-width:560px){.pv-spon-g{gap:8px}.pv-spon-i{flex-direction:column;align-items:flex-start;gap:8px;padding:10px 12px}.pv-spon-i img{height:36px;max-width:110px}.pv-spon-i b{font-size:20px}}',
    '.pv-news{min-height:420px;display:grid;grid-template-columns:1.55fr 1fr;gap:28px;margin:22px 0 30px}',
    '.pv-lead a{color:inherit;text-decoration:none}.pv-lead img{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:10px;display:block;background:#EEF2F6}',
    '.pv-cat{display:inline-block;color:#3A963E;font:700 12px Barlow,Arial,sans-serif;letter-spacing:1.5px;text-transform:uppercase;margin:14px 0 6px}',
    '.pv-lead h2{margin:0 0 8px;font:700 32px/1.12 Barlow,Arial,sans-serif;color:#0F213D}.pv-lead p{margin:0 0 8px;color:#4A5B6C;font:500 17px/1.45 Barlow,Arial,sans-serif}',
    '.pv-by{color:#6F849A;font:600 13px Barlow,Arial,sans-serif}',
    '.pv-sec{display:flex;flex-direction:column;gap:16px}.pv-sec a{display:grid;grid-template-columns:120px 1fr;gap:12px;color:inherit;text-decoration:none;border-bottom:1px solid #E3E9F0;padding-bottom:14px}',
    '.pv-sec img{width:120px;height:80px;object-fit:cover;border-radius:8px;background:#EEF2F6}.pv-sec .pv-cat{margin:0 0 4px}',
    '.pv-sec strong{display:block;font:700 17px/1.25 Barlow,Arial,sans-serif;color:#0F213D}',
    '.pv-all{font:700 15px Barlow,Arial,sans-serif;color:#2E7D32!important;text-decoration:none}',
    '#suscribite{scroll-margin-top:150px}.pv-row{display:grid;grid-template-columns:1.2fr 1fr;gap:22px;margin:0 0 30px}',
    '.pv-box{border-radius:12px;padding:22px}.pv-data{background:#0F213D;color:#fff}.pv-data h3,.pv-sub h3{margin:0 0 6px;font:400 30px/1.05 "Bebas Neue",sans-serif;letter-spacing:.5px}',
    '.pv-data p{margin:0 0 14px;color:#C9D6E3;font:500 15px/1.45 Barlow,Arial,sans-serif}',
    '.pv-kpi{display:flex;gap:22px;flex-wrap:wrap;margin:0 0 16px}.pv-kpi b{display:block;font:400 40px/1 "Bebas Neue",sans-serif;color:#76C46E}.pv-kpi span{color:#C9D6E3;font:500 13px/1.3 Barlow,Arial,sans-serif}',
    '.pv-chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}.pv-chips a{background:#1E3A66;color:#fff!important;text-decoration:none;font:700 14px Barlow,Arial,sans-serif;padding:8px 12px;border-radius:999px}',
    '.pv-chips a:hover{background:#3A963E}.pv-src{color:#9FB3C8;font:500 12.5px/1.4 Barlow,Arial,sans-serif}.pv-src a{color:#C9D6E3}',
    '.pv-sub{background:#EEF6EE;border:2px solid #3A963E;color:#0F213D}.pv-sub h3{color:#0F213D}',
    '.pv-sub ul{margin:6px 0 12px;padding-left:18px;font:500 15px/1.5 Barlow,Arial,sans-serif;color:#24384F}',
    '.pv-sub form{display:flex;gap:8px;flex-wrap:wrap}.pv-sub input[type=email]{flex:1;min-width:180px;padding:11px 12px;border:1px solid #9FB3C8;border-radius:8px;font:500 15px Barlow,Arial,sans-serif}',
    '.pv-sub small{display:block;margin-top:8px;color:#4A5B6C;font:500 12.5px/1.4 Barlow,Arial,sans-serif}.pv-sub small a{color:#2E7D32;font-weight:700}',
    '.pv-h{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin:34px 0 12px;border-top:4px solid #0F213D;padding-top:10px}',
    '.pv-h h3{margin:0;font:400 30px/1 "Bebas Neue",sans-serif;color:#0F213D;letter-spacing:.5px}.pv-h span{color:#6F849A;font:600 14px Barlow,Arial,sans-serif}',
    '.pv-foro{display:grid;grid-template-columns:1.5fr 1fr;gap:22px;align-items:start}.pv-foro .oroh5{display:none}',
    '.pv-brands{background:#F4F6F9;border-top:1px solid #E3E9F0}.pv-brands .wrap{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding-top:22px;padding-bottom:22px}',
    '.pv-brands b{display:block;font:400 22px/1 "Bebas Neue",sans-serif;color:#0F213D;letter-spacing:.5px;margin-bottom:4px}.pv-brands p{margin:0;color:#4A5B6C;font:500 14px/1.45 Barlow,Arial,sans-serif}',
    '@media(max-width:860px){.pv-news,.pv-row,.pv-foro,.pv-brands .wrap{grid-template-columns:1fr}.pv-lead h2{font-size:26px}.pv-mast h1{font-size:32px}}',
    '@media(max-width:420px){.pv-sec a{grid-template-columns:96px 1fr}.pv-sec img{width:96px;height:64px}}'
  ].join('\n');
  document.head.appendChild(css);

  function armar() {
    var inicio = $('#v-inicio'), main = $('#v-inicio main.wrap');
    if (!inicio || !main) return;
    var hero = $('.rv-hero', inicio), strip = $('a.guide-strip', inicio);
    var sp5 = $('.sp5', main), grid = $('.home-grid', main), pb5 = $('.pb5', main), vids = $('section.vids', main), foro27 = $('section.foro27', main), two = $('.two', main);
    var lead = grid && $('article.lead', grid), oro = grid && $('aside .oro5', grid), oroh = grid && $('.oroh5', grid);
    var ds2 = $('section.ds2');

    // 1 · aviso de vista previa

    // 2 · encabezado: la acción principal pasa a ser la suscripción
    var pre = Array.prototype.find.call(document.querySelectorAll('header.top a'), function (a) { return /PRE-REGISTRO/i.test(a.textContent); });
    if (pre) { pre.textContent = 'Suscribite gratis'; pre.setAttribute('href', '#suscribite'); pre.style.background = '#3A963E'; }

    // 3 · presentación compacta en lugar del bloque grande y la franja de la guía
    var mast = el('<section class="pv-mast"><div class="wrap"><h1>La Estación <span>del Futuro</span></h1><p>Noticias, datos y protagonistas de las estaciones de servicio. Publicación de Energías LATAM.</p><a class="pv-btn" href="#suscribite">Suscribite gratis</a></div></section>');
    if (hero) { hero.style.display = 'none'; inicio.insertBefore(mast, hero); }
    if (strip) strip.style.display = 'none';

    // 4 · actualidad arriba: 1 principal + 3 secundarias
    var news = el('<section class="pv-news" aria-label="Últimas noticias"></section>');
    main.insertBefore(news, main.firstChild);
    window.__pvNews = news;

    // 5 · datos del sector + suscripción, lado a lado
    var row = el('<div class="pv-row" id="suscribite"></div>');
    row.appendChild(el('<section class="pv-box pv-data"><h3>Datos del sector</h3><p>Ventas de combustibles por emblema, precios, red de estaciones y GLP en Paraguay, con datos oficiales del MIC. Cada gráfico indica su fecha y unidad.</p><div class="pv-kpi" id="pvKpi"></div><div class="pv-chips"><a href="/combustible/py#ranking">Ranking mensual</a><a href="/combustible/py#precios">Precios por emblema</a><a href="/combustible/py#estaciones">Estaciones</a><a href="/combustible/py#glp">GLP</a><a href="/combustible">Otros países</a></div><div class="pv-src">Fuente: <a href="https://www.mic.gov.py/" target="_blank" rel="noopener">Observatorio de Combustibles del MIC</a>. Chile y Perú con datos oficiales de cada país; el resto, en preparación.</div></section>'));
    var sub = el('<section class="pv-box pv-sub"><h3>Suscribite gratis</h3><div style="font:600 15px Barlow,Arial,sans-serif;color:#24384F">Recibí La Estación del Futuro ' + FREQ + ' en tu correo:</div><ul><li>Las noticias que mueven al sector, con qué significan para una estación.</li><li>El ranking mensual de ventas por emblema y los precios.</li><li>Novedades de proveedores y del Foro &amp; Expo.</li></ul></section>');
    var form = two && two.querySelector('form');
    if (form) { form.style.margin = '0'; sub.appendChild(form); }
    var nota = el('<small>Es gratis y te podés dar de baja cuando quieras.</small>'); sub.appendChild(nota);
    fetch('/newsletter-01.html', { method: 'HEAD' }).then(function (r) { if (r.ok) nota.insertAdjacentHTML('beforeend', ' <a href="/newsletter-01.html" target="_blank" rel="noopener">Ver una edición de muestra →</a>'); }).catch(function () {});
    row.appendChild(sub);
    main.insertBefore(row, news.nextSibling);
    var Y = new Date().getFullYear();
    fetch('/mic.php?y=' + Y).then(function (r) { return r.json(); }).then(function (j) {
      var tot = {}; (j.vp || []).forEach(function (r) { tot[r[0]] = (tot[r[0]] || 0) + r[3]; });
      var ms = Object.keys(tot).map(Number).sort(function (a, b) { return a - b; }); if (!ms.length) return;
      var m = ms[ms.length - 1], M = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
      var k = document.getElementById('pvKpi'); if (!k) return;
      k.innerHTML = '<div><b>' + (tot[m] / 1e6).toLocaleString('es-PY', { maximumFractionDigits: 1 }) + ' M</b><span>litros vendidos en ' + M[m - 1] + ' ' + Y + '<br>(último mes publicado por el MIC)</span></div><div><b>2.883</b><span>estaciones de servicio<br>en el registro del MIC</span></div>';
    }).catch(function () {});

    // 6 · publicidad: el sponsor oficial y los proveedores oro siguen en la portada, después de la actualidad
    if (sp5) sp5.style.display = 'none'; // los sponsors oficiales van en la franja común (sponsors.js)
    if (oroh) { var oh = el('<div style="margin:0 0 24px"></div>'); oh.appendChild(oroh); main.insertBefore(oh, row.nextSibling); }
    if (oro) oro.style.display = 'none'; // Bancard ya figura en la fila de proveedores oro

    // 7 · bloques diferenciados: guía, videos, foro
    var after = oroh ? oroh.parentNode : row;
    var hG = el('<div class="pv-h"><h3>Guía de proveedores</h3><span>Contratistas y proveedores de estaciones de servicio</span></div>');
    main.insertBefore(hG, after.nextSibling);
    if (two) { main.insertBefore(two, hG.nextSibling); var p2 = two.children[1]; if (p2 && !p2.querySelector('form')) p2.style.display = 'none'; two.style.gridTemplateColumns = '1fr'; }
    if (pb5) main.insertBefore(pb5, (two || hG).nextSibling);
    var hV = el('<div class="pv-h"><h3>Videos</h3><span>Charlas completas del Foro 2026</span></div>');
    main.insertBefore(hV, (pb5 || two || hG).nextSibling);
    if (vids) { main.insertBefore(vids, hV.nextSibling); var vh = vids.querySelector('.vids-head'); if (vh) vh.style.display = 'none'; }
    var hF = el('<div class="pv-h"><h3>Foro &amp; Expo Energías Paraguay</h3><span>El encuentro del sector, organizado por los creadores de este medio</span></div>');
    main.insertBefore(hF, (vids || hV).nextSibling);
    if (lead) { var fx = el('<div class="pv-foro"></div>'); var col = lead.querySelector('.collage'); if (col) { col.style.maxHeight = '320px'; col.style.overflow = 'hidden'; } fx.appendChild(lead); if (foro27) fx.appendChild(foro27); main.insertBefore(fx, hF.nextSibling); var h1 = lead.querySelector('h1'); if (h1) { var h2 = document.createElement('h2'); h2.innerHTML = h1.innerHTML; h2.className = h1.className; h1.parentNode.replaceChild(h2, h1); } }
    if (grid) grid.style.display = 'none';
    if (ds2) ds2.style.display = 'none'; // reemplazado por el bloque de datos de arriba

    // 8 · qué es cada marca
    var foot = $('footer.foot');
    document.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('a[href="#suscribite"]'); if (!a) return; e.preventDefault(); var t = document.getElementById('suscribite'); if (!t) return; var hd = document.querySelector('header.top'), off = 16; if (hd && /sticky|fixed/.test(getComputedStyle(hd).position)) off += hd.getBoundingClientRect().height; window.scrollTo({ top: t.getBoundingClientRect().top + window.pageYOffset - off, behavior: 'smooth' }); });
    if (foot) foot.parentNode.insertBefore(el('<section class="pv-brands" aria-label="Nuestras marcas"><div class="wrap"><div><b>Energías LATAM</b><p>El medio especializado en estaciones de servicio, combustibles e infraestructura energética. Hoy con base en Paraguay y datos en expansión a la región.</p></div><div><b>La Estación del Futuro</b><p>La publicación de Energías LATAM: notas, datos del sector y el newsletter.</p></div><div><b>Energías Paraguay</b><p>El Foro &amp; Expo del sector, que reúne a operadores, petroleras, autoridades y proveedores.</p></div></div></section>'), foot);
  }

  function noticias(notas) {
    var news = window.__pvNews; if (!news) return;
    var pub = (notas || []).filter(function (n) { return n.estado === 'publicada'; }).sort(function (a, b) { return a.fecha < b.fecha ? 1 : a.fecha > b.fecha ? -1 : 0; });
    var n0 = pub[0], sec = pub.slice(1, 4); if (!n0) return;
    news.appendChild(el('<article class="pv-lead"><a href="/n/' + esc(n0.id) + '"><img src="' + esc(img(n0)) + '" alt="" loading="eager"><span class="pv-cat">' + esc(n0.cat) + '</span><h2>' + esc(n0.titulo) + '</h2><p>' + esc(n0.bajada) + '</p><span class="pv-by">Por ' + esc(n0.autor) + ' · ' + fecha(n0.fecha) + '</span></a></article>'));
    var s = el('<div class="pv-sec"></div>');
    sec.forEach(function (n) { s.appendChild(el('<a href="/n/' + esc(n.id) + '"><img src="' + esc(img(n)) + '" alt="" loading="lazy"><span><span class="pv-cat">' + esc(n.cat) + '</span><strong>' + esc(n.titulo) + '</strong><span class="pv-by">' + fecha(n.fecha) + '</span></span></a>')); });
    s.appendChild(el('<a class="pv-all" href="#noticias" style="display:block;border:0">Ver todas las notas →</a>'));
    news.appendChild(s);
  }
  var datos = fetch(RAW + 'notas.json', { cache: 'no-store' }).then(function (r) { return r.json(); }).catch(function () { return []; });
  function go() { armar(); datos.then(noticias); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
})();
