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
  function lat(s) { return String(s || '').replace(/[–—]/g, '-').replace(/[“”]/g, '"').replace(/[‘’]/g, "'").replace(/…/g, '...').replace(/[^\x00-\xFF]/g, ''); }
  async function listo() {
    for (var i = 0; i < 80; i++) { var k = txt('kTot'); if (k && k !== '…' && $('prChips') && $('prChips').children.length && txt('qcNota')) return true; await esperar(250); }
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
    var prOn = ($('prChips').querySelector('.chip.on') || {}).dataset;
    var rOn = ($('rProd').querySelector('button.on') || {}).dataset;
    var qOn = ($('qcModo').querySelector('button.on') || {}).dataset;

    var pags = [];
    // ranking: todos, gasoil, naftas
    var nomR = { all: 'Todos los combustibles', G: 'Gasoil', N: 'Naftas' };
    for (var v of ['all', 'G', 'N']) { await clic($('rProd').querySelector('button[data-v="' + v + '"]'), 900); pags.push({ t: 'Ranking de ventas por emblema · ' + nomR[v], im: snap($('placa')), w: 1080, h: 1350 }); }
    // quién creció: mes y acumulado
    var nomQ = { mes: 'Mismo mes del año anterior', ytd: 'Acumulado del año' };
    for (var q of ['mes', 'ytd']) { await clic($('qcModo').querySelector('button[data-v="' + q + '"]'), 700); var cq = $('qcPlaca'); pags.push({ t: '¿Quién creció? · ' + nomQ[q], im: snap(cq), w: cq.width, h: cq.height, nota: lat(txt('qcNota')) }); }
    // precios: cada producto
    var chips = [].slice.call($('prChips').querySelectorAll('.chip'));
    for (var c of chips) { await clic(c, 600); var cp = $('prPlaca'); pags.push({ t: 'Precios por emblema · ' + c.textContent.trim(), im: snap(cp), w: cp.width, h: cp.height, nota: lat(txt('prNota')) }); }
    // estaciones y GLP como se ven en la página
    if (window.html2canvas) {
      for (var sid of [['estaciones', 'Red de estaciones de servicio'], ['glp', 'GLP: ventas, precios e importaciones']]) {
        var sec = $(sid[0]); if (!sec) continue;
        try { var cs = await html2canvas(sec, { scale: 1.5, backgroundColor: '#ffffff', useCORS: true, logging: false, ignoreElements: function (e) { return e.tagName === 'BUTTON' && /Descargar/.test(e.textContent); } }); pags.push({ t: sid[1], im: cs.toDataURL('image/jpeg', 0.88), w: cs.width, h: cs.height }); } catch (e) {}
      }
    }
    // vuelve la página a como estaba
    if (rOn) await clic($('rProd').querySelector('button[data-v="' + rOn.v + '"]'), 50);
    if (qOn) await clic($('qcModo').querySelector('button[data-v="' + qOn.v + '"]'), 50);
    if (prOn) await clic($('prChips').querySelector('.chip[data-v="' + prOn.v + '"]'), 50);

    // ---------- PDF ----------
    var pdf = new window.jspdf.jsPDF({ unit: 'mm', format: 'a4', compress: true });
    var W = 210, H = 297, NAVY = [15, 33, 61], VERDE = [58, 150, 62], VCLARO = [118, 196, 110], GRIS = [122, 138, 155];
    pdf.setProperties({ title: 'Informe del mercado de combustibles · Paraguay · ' + mesTxt, author: 'Energías LATAM', subject: 'Datos oficiales del MIC procesados por Energías LATAM', creator: 'energiaslatam.com' });
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
      pdf.text('Datos oficiales del Ministerio de Industria y Comercio (MIC). Procesamiento y gráficos: Energías LATAM.', 10, H - 9);
      pdf.setFont('helvetica', 'bold'); pdf.setTextColor.apply(pdf, VERDE); pdf.textWithLink('energiaslatam.com', 10, H - 5, { url: 'https://energiaslatam.com/combustible/py?utm_source=informe_mic&utm_medium=pdf' });
      pdf.setFont('helvetica', 'normal'); pdf.setTextColor.apply(pdf, GRIS); pdf.text('Página ' + n + ' de ' + total, W - 10, H - 5, { align: 'right' });
    }
    // tapa
    pdf.setFillColor.apply(pdf, NAVY); pdf.rect(0, 0, W, H, 'F');
    pdf.setFillColor.apply(pdf, VERDE); pdf.rect(0, 0, W, 4, 'F');
    if (LG) pdf.addImage(LG, 'PNG', 20, 26, 30, 30);
    pdf.setFont('helvetica', 'bold'); pdf.setFontSize(18); pdf.setTextColor(255, 255, 255); pdf.text('ENERGÍAS', 56, 40); pdf.setTextColor.apply(pdf, VCLARO); pdf.text('LATAM', 56 + pdf.getTextWidth('ENERGÍAS '), 40);
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(10); pdf.setTextColor(159, 179, 200); pdf.text('LA ESTACIÓN DEL FUTURO · DE LOS CREADORES DE ENERGÍAS PARAGUAY', 56, 47);
    pdf.setFont('helvetica', 'bold'); pdf.setFontSize(12); pdf.setTextColor.apply(pdf, VCLARO); pdf.text('INFORME MENSUAL · DATOS DEL SECTOR', 20, 92);
    pdf.setFontSize(34); pdf.setTextColor(255, 255, 255); pdf.text('El mercado de', 20, 110); pdf.text('combustibles', 20, 124); pdf.setTextColor.apply(pdf, VCLARO); pdf.text('en Paraguay', 20, 138);
    pdf.setFontSize(16); pdf.setTextColor(201, 214, 227); pdf.text(mesTxt.toUpperCase(), 20, 152);
    // números clave
    var kp = [[kTot, kTotL], [kVar, kVarL], [kTop, 'lidera el ranking del mes']];
    kp.forEach(function (k, i) { var x = 20 + i * 60; pdf.setFillColor(23, 46, 82); pdf.roundedRect(x, 168, 54, 34, 3, 3, 'F'); pdf.setFont('helvetica', 'bold'); pdf.setFontSize(17); pdf.setTextColor.apply(pdf, VCLARO); pdf.text(lat(k[0]).slice(0, 18), x + 5, 182); pdf.setFont('helvetica', 'normal'); pdf.setFontSize(8.5); pdf.setTextColor(201, 214, 227); pdf.text(pdf.splitTextToSize(lat(k[1]), 46), x + 5, 189); });
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(10.5); pdf.setTextColor(201, 214, 227);
    pdf.text(pdf.splitTextToSize('Ventas de combustibles por emblema, quién creció, precios por emblema y producto, red de estaciones y GLP, con los datos oficiales que las distribuidoras declaran ante el Ministerio de Industria y Comercio.', 170), 20, 220);
    pdf.setFillColor.apply(pdf, VERDE); pdf.roundedRect(20, 246, 90, 13, 2, 2, 'F'); pdf.setFont('helvetica', 'bold'); pdf.setFontSize(12); pdf.setTextColor(255, 255, 255); pdf.textWithLink('energiaslatam.com', 26, 254.5, { url: 'https://energiaslatam.com/?utm_source=informe_mic&utm_medium=pdf' });
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(8); pdf.setTextColor.apply(pdf, GRIS); pdf.text('Datos oficiales del MIC. Procesamiento y gráficos: Energías LATAM.  ·  Página 1 de ' + total, 20, H - 10);
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
    pdf.text(pdf.splitTextToSize('En energiaslatam.com actualizamos el ranking, los precios y la red de estaciones cada vez que el MIC publica datos nuevos. Podés elegir el mes, filtrar por empresa y descargar cada placa para compartir.', 170), 20, 74);
    var ls = [['Datos del sector', 'energiaslatam.com/combustible/py', 'https://energiaslatam.com/combustible/py?utm_source=informe_mic&utm_medium=pdf'], ['Noticias de las estaciones de servicio', 'energiaslatam.com', 'https://energiaslatam.com/?utm_source=informe_mic&utm_medium=pdf'], ['Newsletter semanal gratis', 'energiaslatam.com/newsletter', 'https://energiaslatam.com/newsletter?utm_source=informe_mic&utm_medium=pdf'], ['Publicidad y notas de marca', 'energiaslatam.com/media-kit', 'https://energiaslatam.com/media-kit?utm_source=informe_mic&utm_medium=pdf']];
    ls.forEach(function (l, i) { var y = 104 + i * 22; pdf.setFillColor(242, 248, 242); pdf.roundedRect(20, y, 170, 17, 2, 2, 'F'); pdf.setFont('helvetica', 'bold'); pdf.setFontSize(11.5); pdf.setTextColor.apply(pdf, NAVY); pdf.text(l[0], 26, y + 7); pdf.setFont('helvetica', 'normal'); pdf.setTextColor.apply(pdf, VERDE); pdf.textWithLink(l[1], 26, y + 13, { url: l[2] }); });
    pdf.setFont('helvetica', 'normal'); pdf.setFontSize(10); pdf.setTextColor(36, 56, 79);
    pdf.text('Contacto: info@energiaslatam.com · WhatsApp +595 984 040 224', 20, 206);
    pdf.setFontSize(8.5); pdf.setTextColor.apply(pdf, GRIS);
    pdf.text(pdf.splitTextToSize('Los datos son los declarados por las distribuidoras ante el Ministerio de Industria y Comercio; los precios son promedios informados y pueden variar entre estaciones del mismo emblema. Energías LATAM procesa y grafica la información; no modifica los valores oficiales.', 170), 20, 222);
    var mesArch = mesTxt.toLowerCase().replace(/\s+/g, '-').normalize('NFD').replace(/[̀-ͯ]/g, '');
    return { blob: pdf.output('blob'), nombre: 'informe-combustibles-paraguay-' + mesArch + '-energiaslatam.pdf', mes: mesTxt, paginas: total };
  };
  window.informeMICdescargar = async function () {
    var r = await window.informeMIC(); var u = URL.createObjectURL(r.blob), a = document.createElement('a'); a.href = u; a.download = r.nombre; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(u); a.remove(); }, 4000);
    try { if (typeof gtag === 'function') gtag('event', 'file_download', { file_name: r.nombre, informe: 'mic' }); } catch (e) {}
    return r;
  };
  if (/[?&]informe=1/.test(location.search)) { var go = function () { window.informeMICdescargar().catch(function () {}); }; if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go(); }
})();
