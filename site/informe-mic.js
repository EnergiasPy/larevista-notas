/* Informe mensual del mercado de combustibles (datos MIC) en PDF · energiaslatam.com
   Corre dentro de /combustible/py: arma el PDF con las mismas placas que se ven en la página
   (ranking, quién creció, precios) más estaciones y GLP, con logo y energiaslatam.com en todas las páginas.
   window.informeMIC() devuelve una promesa con { blob, nombre, mes }.
   /combustible/py?informe=1 lo descarga solo. */
(function () {
  if (window.informeMIC) return;
  var JSPDF = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
  var H2C = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
  function $(i) { return document.getElementById(i); }
  function esperar(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function cargar(src) { return new Promise(function (ok, ko) { var s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = ko; document.head.appendChild(s); }); }
  function img(src) { return new Promise(function (ok) { var i = new Image(); i.crossOrigin = 'anonymous'; i.onload = function () { ok(i); }; i.onerror = function () { ok(null); }; i.src = src; }); }
  function aDataURL(i, w, h, redondo) { var c = document.createElement('canvas'); c.width = w; c.height = h; var x = c.getContext('2d'); if (redondo) { x.beginPath(); x.arc(w / 2, h / 2, w / 2, 0, 7); x.fillStyle = '#fff'; x.fill(); x.clip(); x.drawImage(i, w * .04, h * .04, w * .92, h * .92); } else x.drawImage(i, 0, 0, w, h); return c.toDataURL('image/png'); }
  function snap(cv) { return cv.toDataURL('image/jpeg', 0.9); }
  function txt(id) { var e = $(id); return e ? e.textContent.replace(/\s+/g, ' ').trim() : ''; }
  // limpia caracteres que la fuente estándar del PDF no tiene
  function lat(s) { return String(s || '').replace(/▲/g, '+').replace(/▼/g, '-').replace(/[–—]/g, '-').replace(/[“”]/g, '"').replace(/[‘’]/g, "'").replace(/…/g, '...').replace(/[^\x00-\xFF]/g, ''); }
  // país de la página: /combustible/py (página propia) o /combustible/xx (pais.html)
  var PAIS = (location.pathname.match(/combustible\/([a-z]{2})/) || [])[1] || (new URLSearchParams(location.search).get('c')) || 'py';
  var CFG = {
    py: { n: 'Paraguay', src: 'el Ministerio de Industria y Comercio (MIC)', srcC: 'MIC', pie: 'Datos oficiales del Ministerio de Industria y Comercio (MIC).', intro: 'Ventas de combustibles por emblema, quién creció, precios por emblema y producto, red de estaciones y GLP, con los datos oficiales que las distribuidoras declaran ante el Ministerio de Industria y Comercio.', ent: 'emblema' },
    cl: { n: 'Chile', src: 'la Superintendencia de Electricidad y Combustibles (SEC)', srcC: 'SEC', pie: 'Datos oficiales de la Superintendencia de Electricidad y Combustibles (SEC).', intro: 'Ventas mensuales de combustibles líquidos por región y producto, con los datos oficiales de la SEC. La fuente no publica el dato por compañía.', ent: 'región' },
    pe: { n: 'Perú', src: 'Osinergmin', srcC: 'Osinergmin', pie: 'Datos oficiales de Osinergmin.', intro: 'Ventas mensuales de combustibles por departamento y producto, con los datos oficiales de Osinergmin. La fuente no publica el dato por empresa.', ent: 'departamento' },
    bo: { n: 'Bolivia', src: 'el INE de Bolivia, con datos de la Aduana Nacional y del Ministerio de Hidrocarburos y Energías', srcC: 'INE Bolivia', pie: 'Datos oficiales del INE de Bolivia (preliminares).', intro: 'Volumen mensual comercializado al mercado interno por producto, incluidas las importaciones privadas de diésel y gasolina, con los datos oficiales del INE. La fuente no publica el dato por departamento ni por empresa.', ent: 'producto' },
    uy: { n: 'Uruguay', src: 'el Ministerio de Industria, Energía y Minería (MIEM), con datos de ANCAP', srcC: 'MIEM · ANCAP', pie: 'Datos oficiales del MIEM, con información de ANCAP.', intro: 'Ventas mensuales de gasoil y gasolinas en estaciones de servicio por departamento, con los datos oficiales del MIEM y ANCAP. La fuente no publica el dato por distribuidora.', ent: 'departamento' }
  };
  var C = CFG[PAIS] || CFG.py, PY = PAIS === 'py';
  async function listo() {
    for (var i = 0; i < 80; i++) {
      var k = txt('kTot');
      if (k && k !== '…' && (PY ? ($('prChips') && $('prChips').children.length && txt('qcNota')) : ($('rMes') && $('rMes').options.length))) return true;
      await esperar(250);
    }
    return false;
  }
  async function clic(el, ms) { if (el) { el.click(); await esperar(ms || 700); } }

  window.informeMIC = async function () {
    if (!(await listo())) throw new Error('datos');
    if (!window.jspdf) await cargar(JSPDF);
    if (!window.html2canvas) { try { await cargar(H2C); } catch (e) {} }
    try { await document.fonts.ready; } catch (e) {}
    var mesTxt = lat(($('rMes').selectedOptions[0] || {}).textContent || '');
    var kTot = lat(txt('kTot')), kTotL = lat(txt('kTotL')), kVar = lat(txt('kVar')), kVarL = lat(txt('kVarL')), kTop = lat(txt('kTop'));
    var lg = await img('/logo-latam-v2-512.png'), LG = lg ? aDataURL(lg, 240, 240, true) : null;

    // estado inicial para dejar la página como estaba
    var prOn = PY ? ($('prChips').querySelector('.chip.on') || {}).dataset : null;
    var rOn = ($('rProd').querySelector('button.on') || {}).dataset;
    var qOn = PY ? ($('qcModo').querySelector('button.on') || {}).dataset : null;

    var pags = [];
    // ranking: todos, gasoil/diésel, naftas/gasolinas (los nombres salen de los botones de la página)
    var tR = PY ? 'Ranking de ventas por emblema' : 'Ranking de consumo por ' + C.ent;
    for (var v of ['all', 'G', 'N']) { var bv = $('rProd').querySelector('button[data-v="' + v + '"]'); if (!bv) continue; await clic(bv, 900); pags.push({ t: tR + ' · ' + (v === 'all' ? 'Todos los combustibles' : bv.textContent.trim()), im: snap($('placa')), w: 1080, h: 1350 }); }
    if (!PY) {
      // tabla dinámica del año, como se ve en la página
      var tt = $('tt'), secT = tt && (tt.closest('section') || tt.parentElement);
      if (secT && window.html2canvas) { try { var ct = await html2canvas(secT, { scale: 1.4, backgroundColor: '#ffffff', useCORS: true, logging: false, ignoreElements: function (e) { return e.tagName === 'BUTTON' && /CSV|Descargar/.test(e.textContent); } }); pags.push({ t: 'Litros por mes y por ' + C.ent, im: ct.toDataURL('image/jpeg', 0.88), w: ct.width, h: ct.height }); } catch (e) {} }
    }
    if (PY) {
    // quién creció: mes y acumulado
    var nomQ = { mes: 'Mismo mes del año anterior', ytd: 'Acumulado del año' };
    for (var q of ['mes', 'ytd']) { await clic($('qcModo').querySelector('button[data-v="' + q + '"]'), 700); var cq = $('qcPlaca'); pags.push({ t: '¿Quién creció? · ' + nomQ[q], im: snap(cq), w: cq.width, h: cq.height, nota: lat(txt('qcNota')) }); }
    // precios: cada producto
    // los botones se vuelven a dibujar en cada clic: se buscan de nuevo por su valor
    var prods = [].map.call($('prChips').querySelectorAll('.chip'), function (b) { return [b.dataset.v, b.textContent.trim()]; });
    for (var pv of prods) { await clic($('prChips').querySelector('.chip[data-v="' + pv[0] + '"]'), 700); var cp = $('prPlaca'); pags.push({ t: 'Precios por emblema · ' + pv[1], im: snap(cp), w: cp.width, h: cp.height, nota: lat(txt('prNota')) }); }
    // estaciones y GLP como se ven en la página
    if (window.html2canvas) {
      for (var sid of [['estaciones', 'Red de estaciones de servicio'], ['glp', 'GLP: ventas, precios e importaciones']]) {
        var sec = $(sid[0]); if (!sec) continue;
        try { var cs = await html2canvas(sec, { scale: 1.5, backgroundColor: '#ffffff', useCORS: true, logging: false, ignoreElements: function (e) { return e.tagName === 'BUTTON' && /Descargar/.test(e.textContent); } }); pags.push({ t: sid[1], im: cs.toDataURL('image/jpeg', 0.88), w: cs.width, h: cs.height }); } catch (e) {}
      }
    }
    }
    // vuelve la página a como estaba
    if (rOn) await clic($('rProd').querySelector('button[data-v="' + rOn.v + '"]'), 50);
    if (qOn) await clic($('qcModo').querySelector('button[data-v="' + qOn.v + '"]'), 50);
    if (prOn) await clic($('prChips').querySelector('.chip[data-v="' + prOn.v + '"]'), 50);

    // ---------- PDF ----------
    var pdf = new window.jspdf.jsPDF({ unit: 'mm', format: 'a4', compress: true });
    var W = 210, H = 297, NAVY = [15, 33, 61], VERDE = [58, 150, 62], VCLARO = [118, 196, 110], GRIS = [122, 138, 155];
    pdf.setProperties({ title: lat('Informe del mercado de combustibles · ' + C.n + ' · ') + mesTxt, author: 'Energías LATAM', subject: lat('Datos oficiales de ' + C.srcC + ' procesados por Energías LATAM'), creator: 'energiaslatam.com' });
    var total = pags.length + 2;
    function marco(n) {
      pdf.setFillColor.apply(pdf, NAVY); pdf.rect(0, 0, W, 20, 'F');
      pdf.setFillColor.apply(pdf, VERDE); pdf.rect(0, 20, W, 1.2, 'F');
      if (LG) pdf.addImage(LG, 'PNG', 10, 3.5, 13, 13);
      pdf.setFont('helvetica', 'bold'); pdf.setFontSize(11); pdf.setTextColor(255, 255, 255); pdf.text('ENERGÍAS', 26, 10); pdf.setTextColor.apply(pdf, VCLARO); pdf.text('LATAM', 26 + pdf.getTextWidth('ENERGÍAS '), 10);
      pdf.setFont('helvetica', 'normal'); pdf.setFontSize(7.5); pdf.setTextColor(159, 179, 200); pdf.text('LA ESTACIÓN DEL FUTURO', 26, 14.5);
      pdf.setFont('helvetica', 'bold'); pdf.setFontSize(10); pdf.setTextColor(255, 255, 255); pdf.textWithLink('energiaslatam.com', W - 10, 11.5, { align: 'right', url: 'https://energiaslatam.com/?utm_source=informe_mic&utm_medium=pdf' });
      // pie
      pdf.setDrawColor(227, 233, 240); pdf.setLineWidth(.3); pdf.line(10, H - 14, W - 10, H - 14);
      pdf.setFont('helvetica', 'normal'); pdf.setFontSize(7.5); pdf.setTextColor.apply(pdf, GRIS);
      pdf.text(lat(C.pie + ' Procesamiento y gráficos: Energías LATAM.'), 10, H - 9);
      pdf.setFont('helvetica', 'bold'); pdf.setTextColor.apply(pdf, VERDE); pdf.textWithLink('energiaslatam.com', 10, H - 5, { url: 'https://energiaslatam.com/combustible/' + PAIS + '?utm_source=informe_mic&utm_medium=pdf' });
      pdf.setFont('helvetica', 'normal'); pdf.setTextColor.apply(pdf, GRIS); pdf.text('Página ' + n + ' de ' + total, W - 10, H - 5, { align: 'right' });
    }
    // tapa
    pdf.setFillColor.apply(pdf, NAVY); pdf.rect(0, 0, W, H, 'F');
    pdf.setFillColor.apply(pdf, VERDE); pdf.rect(0, 0, W, 4, 'F');
    if (LG) pdf.addImage(LG, 'PNG', 20, 26, 30, 30);
    pdf.setFont('helvetica', 'bold'); pdf.setFontSize(18); pdf.setTextColor(255, 255, 255); pdf.text('ENERGÍAS', 56, 40); pdf.setTextColor.apply(pdf, VCLARO); pdf.text('LATAM', 56 + pdf.getTextWidth('ENERGÍAS '), 40);
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(10); pdf.setTextColor(159, 179, 200); pdf.text('LA ESTACIÓN DEL FUTURO · DE LOS CREADORES DE ENERGÍAS PARAGUAY', 56, 47);
    pdf.setFont('helvetica', 'bold'); pdf.setFontSize(12); pdf.setTextColor.apply(pdf, VCLARO); pdf.text('INFORME MENSUAL · DATOS DEL SECTOR', 20, 92);
    pdf.setFontSize(34); pdf.setTextColor(255, 255, 255); pdf.text('El mercado de', 20, 110); pdf.text('combustibles', 20, 124); pdf.setTextColor.apply(pdf, VCLARO); pdf.text(lat('en ' + C.n), 20, 138);
    pdf.setFontSize(16); pdf.setTextColor(201, 214, 227); pdf.text(mesTxt.toUpperCase(), 20, 152);
    // números clave
    var kp = [[kTot, kTotL], [kVar, kVarL], [kTop, PY ? 'lidera el ranking del mes' : lat(txt('kTopL')) || 'lidera el consumo del mes']];
    kp.forEach(function (k, i) { var x = 20 + i * 60; pdf.setFillColor(23, 46, 82); pdf.roundedRect(x, 168, 54, 34, 3, 3, 'F'); pdf.setFont('helvetica', 'bold'); pdf.setFontSize(17); pdf.setTextColor.apply(pdf, VCLARO); pdf.text(lat(k[0]).slice(0, 18), x + 5, 182); pdf.setFont('helvetica', 'normal'); pdf.setFontSize(8.5); pdf.setTextColor(201, 214, 227); pdf.text(pdf.splitTextToSize(lat(k[1]), 46), x + 5, 189); });
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(10.5); pdf.setTextColor(201, 214, 227);
    pdf.text(pdf.splitTextToSize(lat(C.intro), 170), 20, 220);
    pdf.setFillColor.apply(pdf, VERDE); pdf.roundedRect(20, 246, 90, 13, 2, 2, 'F'); pdf.setFont('helvetica', 'bold'); pdf.setFontSize(12); pdf.setTextColor(255, 255, 255); pdf.textWithLink('energiaslatam.com', 26, 254.5, { url: 'https://energiaslatam.com/?utm_source=informe_mic&utm_medium=pdf' });
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(8); pdf.setTextColor.apply(pdf, GRIS); pdf.text(lat('Datos oficiales de ' + C.srcC + '. Procesamiento y gráficos: Energías LATAM.  ·  Página 1 de ') + total, 20, H - 10);
    // páginas con placas
    pags.forEach(function (p, i) {
      pdf.addPage(); marco(i + 2);
      pdf.setFont('helvetica', 'bold'); pdf.setFontSize(14); pdf.setTextColor.apply(pdf, NAVY); pdf.text(lat(p.t), 10, 31);
      var top = 36, bottom = H - (p.nota ? 30 : 18), mw = W - 20, mh = bottom - top, r = Math.min(mw / p.w, mh / p.h), iw = p.w * r, ih = p.h * r;
      pdf.addImage(p.im, 'JPEG', (W - iw) / 2, top, iw, ih);
      if (p.nota) { pdf.setFont('helvetica', 'normal'); pdf.setFontSize(9.5); pdf.setTextColor(36, 56, 79); pdf.text(pdf.splitTextToSize(p.nota, W - 20), 10, top + ih + 6); }
    });
    // cierre
    pdf.addPage(); marco(total);
    pdf.setFont('helvetica', 'bold'); pdf.setFontSize(22); pdf.setTextColor.apply(pdf, NAVY); pdf.text('Seguí los datos todos los meses', 20, 60);
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(11.5); pdf.setTextColor(36, 56, 79);
    pdf.text(pdf.splitTextToSize(lat(PY ? 'En energiaslatam.com actualizamos el ranking, los precios y la red de estaciones cada vez que el MIC publica datos nuevos. Podés elegir el mes, filtrar por empresa y descargar cada placa para compartir.' : 'En energiaslatam.com actualizamos el ranking cada vez que ' + C.srcC + ' publica datos nuevos. Podés elegir el mes, filtrar por ' + C.ent + ' y producto, y descargar cada placa para compartir.'), 170), 20, 74);
    var ls = [['Datos del sector · ' + C.n, 'energiaslatam.com/combustible/' + PAIS, 'https://energiaslatam.com/combustible/' + PAIS + '?utm_source=informe_mic&utm_medium=pdf'], ['Noticias de las estaciones de servicio', 'energiaslatam.com', 'https://energiaslatam.com/?utm_source=informe_mic&utm_medium=pdf'], ['Newsletter semanal gratis', 'energiaslatam.com/newsletter', 'https://energiaslatam.com/newsletter?utm_source=informe_mic&utm_medium=pdf'], ['Publicidad y notas de marca', 'energiaslatam.com/media-kit', 'https://energiaslatam.com/media-kit?utm_source=informe_mic&utm_medium=pdf']];
    ls.forEach(function (l, i) { var y = 104 + i * 22; pdf.setFillColor(242, 248, 242); pdf.roundedRect(20, y, 170, 17, 2, 2, 'F'); pdf.setFont('helvetica', 'bold'); pdf.setFontSize(11.5); pdf.setTextColor.apply(pdf, NAVY); pdf.text(l[0], 26, y + 7); pdf.setFont('helvetica', 'normal'); pdf.setTextColor.apply(pdf, VERDE); pdf.textWithLink(l[1], 26, y + 13, { url: l[2] }); });
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(10); pdf.setTextColor(36, 56, 79);
    pdf.text('Contacto: info@energiaslatam.com · WhatsApp +595 984 040 224', 20, 206);
    pdf.setFontSize(8.5); pdf.setTextColor.apply(pdf, GRIS);
    pdf.text(pdf.splitTextToSize(lat(PY ? 'Los datos son los declarados por las distribuidoras ante el Ministerio de Industria y Comercio; los precios son promedios informados y pueden variar entre estaciones del mismo emblema. Energías LATAM procesa y grafica la información; no modifica los valores oficiales.' : 'Los datos son los publicados por ' + C.src + '. Energías LATAM procesa y grafica la información; no modifica los valores oficiales.'), 170), 20, 222);
    var mesArch = mesTxt.toLowerCase().replace(/\s+/g, '-').normalize('NFD').replace(/[̀-ͯ]/g, '');
    return { blob: pdf.output('blob'), nombre: 'informe-combustibles-' + C.n.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '') + '-' + mesArch + '-energiaslatam.pdf', mes: mesTxt, paginas: total };
  };
  window.informeMICdescargar = async function () {
    var r = await window.informeMIC(); var u = URL.createObjectURL(r.blob), a = document.createElement('a'); a.href = u; a.download = r.nombre; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(u); a.remove(); }, 4000);
    try { if (typeof gtag === 'function') gtag('event', 'file_download', { file_name: r.nombre, informe: 'mic' }); } catch (e) {}
    return r;
  };
  if (/[?&]informe=1/.test(location.search)) { var go = function () { window.informeMICdescargar().catch(function () {}); }; if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go(); }
})();
