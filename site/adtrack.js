/* Medición de publicidad · energiaslatam.com
   - ad_click: cada click en un aviso (sponsor, oro, plata, bronce)
   - ad_impression: cada aviso visto (≥50 % en pantalla durante ≥1 s), una vez por aviso y lugar por página vista
   - UTM en los links salientes, para que el anunciante vea el tráfico en su propio Analytics
   No cambia nada visible del sitio. */
(function () {
  if (window.__adtrack) return; window.__adtrack = { log: [] };
  var SEL = '.spof-i, .r5i, .brl5 a';

  function send(ev, p) {
    window.__adtrack.log.push([ev, p]);
    try { if (typeof gtag === 'function') gtag('event', ev, p); } catch (e) {}
  }
  function txt(n) { return n ? (n.textContent || '').replace(/\s+/g, ' ').trim() : ''; }
  function nombre(a) {
    var b = a.querySelector('.spof-i b, h4, b');
    var im = a.querySelector('img');
    var n = (a.classList.contains('spof-i') && txt(a.querySelector('b'))) ||
            (im && im.getAttribute('alt')) || txt(a.querySelector('h4')) || txt(b) || a.getAttribute('title') || txt(a);
    return n.replace(/ · Sponsor oficial$/, '').slice(0, 80);
  }
  function nivel(a) {
    if (a.closest('.spof, .sp5')) return 'sponsor';
    if (a.closest('.brl5, .bronce')) return 'bronce';
    if (a.closest('.plata')) return 'plata';
    if (a.closest('.oro5, .oroh5')) return 'oro';
    return 'otro';
  }
  function notaId() {
    var m = location.pathname.match(/^\/n\/([^\/?#]+)/) || location.hash.match(/^#n\/([^\/?#]+)/);
    return m ? decodeURIComponent(m[1]) : '';
  }
  function ubicacion(a) {
    if (notaId()) return 'nota';
    var v = a.closest('section[data-view]');
    var vista = v ? v.getAttribute('data-view') : '';
    if (/^nota/.test(vista)) return 'nota';
    var p = location.pathname.replace(/\/+$/, '').replace(/\.html$/, '');
    if (p === '' || p === '/index') return vista && vista !== 'inicio' ? vista : 'portada';
    return p.replace(/^\//, '');
  }
  function posicion(a) {
    var box = a.closest('.r5, .spof-g, .brl5 .grid');
    if (!box) return '';
    var fila = box.parentNode, i = 1;
    if (box.classList.contains('r5') && fila) {
      var hermanos = [].filter.call(fila.children, function (x) { return x.classList && x.classList.contains('r5'); });
      i = hermanos.indexOf(box) + 1;
    } else {
      i = [].indexOf.call(box.querySelectorAll(':scope > a'), a) + 1;
    }
    var zona = a.closest('.nt5') ? 'nota-arriba' : a.closest('.brl5') ? 'nota-abajo' : a.closest('.spof') ? 'franja-sponsors' :
               a.closest('.oroh5') ? 'oro-horizontal' : a.closest('.pb5') ? 'plata-bronce' : a.closest('.oro5') ? 'oro' : 'otro';
    return zona + '-' + i;
  }
  function datos(a) {
    return { anunciante: nombre(a), nivel: nivel(a), ubicacion: ubicacion(a), nota_id: notaId(), posicion: posicion(a) };
  }

  // UTM en links salientes (se agrega justo antes de abrir el link)
  function utm(a) {
    var h = a.getAttribute('href') || '';
    if (!/^https?:\/\//i.test(h) || /energiaslatam\.com/i.test(h) || /[?&]utm_source=/.test(h)) return;
    var d = datos(a);
    var q = 'utm_source=energiaslatam&utm_medium=banner&utm_campaign=' + encodeURIComponent(d.nivel) + '&utm_content=' + encodeURIComponent(d.ubicacion);
    var hash = '', k = h.indexOf('#');
    if (k >= 0) { hash = h.slice(k); h = h.slice(0, k); }
    a.setAttribute('href', h + (h.indexOf('?') >= 0 ? '&' : '?') + q + hash);
  }
  ['mousedown', 'touchstart', 'keydown'].forEach(function (t) {
    document.addEventListener(t, function (e) { var a = e.target.closest && e.target.closest(SEL); if (a) utm(a); }, { capture: true, passive: true });
  });
  function onClick(e) {
    var a = e.target.closest && e.target.closest(SEL); if (!a) return;
    utm(a);
    var d = datos(a); d.link_url = a.getAttribute('href') || ''; d.transport_type = 'beacon';
    send('ad_click', d);
  }
  document.addEventListener('click', onClick, true);
  document.addEventListener('auxclick', onClick, true);

  // Impresiones: aviso visible ≥50 % durante ≥1 s, una vez por aviso y lugar por página vista
  if (!('IntersectionObserver' in window)) return;
  var visibles = new Set(), vistos = {}, previos = {}, pagina = location.pathname + location.hash;
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (en) { if (en.intersectionRatio >= 0.5) visibles.add(en.target); else visibles.delete(en.target); });
  }, { threshold: [0, 0.5, 1] });
  var observados = new WeakSet();
  function escanear() {
    document.querySelectorAll('.r5, .spof-i, .brl5 a').forEach(function (n) {
      if (!observados.has(n)) { observados.add(n); io.observe(n); }
    });
  }
  function mostrados(n) {
    if (n.classList.contains('r5')) { var on = n.querySelector(':scope > .r5i.on') || (n.querySelectorAll(':scope > .r5i').length === 1 ? n.querySelector(':scope > .r5i') : null); return on ? [on] : []; }
    return [n];
  }
  setInterval(function () {
    if (document.hidden) return;
    var ahora = location.pathname + location.hash;
    if (ahora !== pagina) { pagina = ahora; vistos = {}; previos = {}; }
    var actuales = {};
    visibles.forEach(function (n) {
      if (!n.isConnected || !n.offsetParent) return;
      mostrados(n).forEach(function (a) {
        var d = datos(a), k = d.anunciante + '|' + d.nivel + '|' + d.posicion;
        actuales[k] = 1;
        if (previos[k] && !vistos[k]) { vistos[k] = 1; send('ad_impression', d); }
      });
    });
    previos = actuales;
  }, 1000);
  escanear();
  var tm; new MutationObserver(function () { clearTimeout(tm); tm = setTimeout(escanear, 300); }).observe(document.body || document.documentElement, { childList: true, subtree: true });
})();
