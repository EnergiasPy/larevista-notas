/* Medición de publicidad · energiaslatam.com
   - aviso_click: cada click en un aviso (sponsor, oro, plata, bronce)
   - aviso_visto: cada aviso visto (≥50 % en pantalla durante ≥1 s), una vez por aviso y lugar por página vista
   - UTM en los links salientes, para que el anunciante vea el tráfico en su propio Analytics
   No cambia nada visible del sitio. */
(function () {
  if (window.__adtrack) return; window.__adtrack = { log: [] };
  var SEL = '.spof-i, .r5i, .brl5 a';

  // medidor propio (med.php): misma información, guardada en nuestro servidor
  // visitante anónimo (número al azar guardado en este navegador; no identifica a la persona)
  var VID = '';
  try { VID = localStorage.getItem('el_vid') || ''; if (!VID) { VID = Math.random().toString(36).slice(2, 12) + Date.now().toString(36).slice(-4); localStorage.setItem('el_vid', VID); } } catch (e) {}
  function fuente() {
    var q = location.search, r = document.referrer || '';
    var u = (q.match(/[?&]utm_source=([^&]+)/) || [])[1];
    if (u) return 'utm:' + decodeURIComponent(u).toLowerCase().slice(0, 30);
    if (/fbclid|igshid/.test(q)) return 'instagram/facebook';
    if (!r || /energiaslatam\.com/i.test(r)) return 'directo';
    if (/instagram/i.test(r)) return 'instagram'; if (/facebook|fb\./i.test(r)) return 'facebook';
    if (/google\./i.test(r)) return 'google'; if (/bing\.|yahoo|duckduckgo/i.test(r)) return 'otros buscadores';
    if (/whatsapp|wa\.me/i.test(r)) return 'whatsapp'; if (/mail|brevo|sendibt/i.test(r)) return 'email';
    if (/linkedin/i.test(r)) return 'linkedin';
    return 'otro: ' + r.replace(/^https?:\/\/(www\.)?/i, '').split(/[\/?#]/)[0].slice(0, 40);
  }
  var FUENTE = fuente();
  function med(o) {
    o.vid = VID; o.src = FUENTE;
    try {
      var b = JSON.stringify(o);
      if (navigator.sendBeacon) navigator.sendBeacon('/med.php', new Blob([b], { type: 'application/json' }));
      else fetch('/med.php', { method: 'POST', body: b, keepalive: true, headers: { 'Content-Type': 'application/json' } });
    } catch (e) {}
  }
  function send(ev, p) {
    window.__adtrack.log.push([ev, p]);
    try { if (typeof gtag === 'function') gtag('event', ev, p); } catch (e) {}
    if ((ev === 'aviso_click' || ev === 'aviso_visto') && p.anunciante) med({ t: ev === 'aviso_click' ? 'click' : 'visto', an: p.anunciante, ni: p.nivel, ub: p.ubicacion, po: p.posicion, pg: location.pathname, nid: p.nota_id });
  }
  function txt(n) { return n ? (n.textContent || '').replace(/\s+/g, ' ').trim() : ''; }
  function nombre(a) {
    // el nombre se fija la primera vez (antes de que el traductor del navegador lo cambie) y el aviso no se traduce
    if (a.dataset && a.dataset.an5) return a.dataset.an5;
    try { a.setAttribute('translate', 'no'); } catch (e) {}
    var b = a.querySelector('.spof-i b, h4, b');
    var im = a.querySelector('img');
    var n = (a.classList.contains('spof-i') && txt(a.querySelector('b'))) ||
            (im && im.getAttribute('alt')) || txt(a.querySelector('h4')) || txt(b) || a.getAttribute('title') || txt(a);
    n = n.replace(/ · Sponsor oficial$/, '').slice(0, 80);
    if (/[\u3000-\u9fff\uac00-\ud7af]/.test(n)) return ''; // nombre ya traducido (chino, japonés, coreano): no se registra
    if (a.dataset) a.dataset.an5 = n;
    return n;
  }
  function nivel(a) {
    if (a.closest('.spof, .sp5')) return 'sponsor';
    if (a.closest('.brl5, .bronce')) return 'bronce';
    if (a.closest('.plata')) return 'plata';
    if (a.closest('.oro5, .oroh5, .nx-oro')) return 'oro';
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
    if (a.closest('.nx-oro')) return 'nota-lateral-' + ([].indexOf.call(a.parentNode.children, a) + 1);
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
    send('aviso_click', d);
  }
  document.addEventListener('click', onClick, true);

  // todos los demás clics del sitio (menú, notas, botones, suscripción, WhatsApp, redes, links externos)
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a,button'); if (!a || a.closest(SEL)) return;
    var h = a.getAttribute('href') || '', txt = (a.getAttribute('aria-label') || a.textContent || a.title || '').replace(/\s+/g, ' ').trim().slice(0, 60);
    var dest;
    if (/wa\.me|whatsapp/i.test(h)) dest = 'WhatsApp';
    else if (/instagram|facebook|linkedin|youtube|tiktok|x\.com|twitter/i.test(h)) dest = 'Redes: ' + (h.match(/instagram|facebook|linkedin|youtube|tiktok|x\.com|twitter/i) || [''])[0].toLowerCase();
    else if (/^https?:\/\//i.test(h) && !/energiaslatam\.com/i.test(h)) dest = 'Externo: ' + h.replace(/^https?:\/\/(www\.)?/i, '').split(/[\/?#]/)[0];
    else if (/newsletter|suscrib/i.test(h + ' ' + txt)) dest = 'Suscribirse';
    else if (/^\/n\/|#n\//.test(h)) dest = 'Nota: ' + h.replace(/^.*(\/n\/|#n\/)/, '').split(/[?#]/)[0];
    else if (h) dest = 'Interno: ' + (h.replace(/^https?:\/\/(www\.)?energiaslatam\.com/i, '').split('?')[0] || '/');
    else dest = 'Botón: ' + (txt || 'sin texto');
    med({ t: 'link', an: dest, ub: txt, pg: location.pathname, nid: notaId() });
  }, true);

  // páginas vistas (también en la navegación interna por #)
  var pvPrev = '';
  function pv() { var k = location.pathname + location.hash; if (k === pvPrev) return; pvPrev = k; med({ t: 'pv', pg: location.pathname.replace(/\.html$/, '') || '/', nid: notaId() }); }
  pv(); window.addEventListener('hashchange', function () { setTimeout(pv, 200); });

  // nota leída: 30 segundos con la nota abierta y visible, o bajar hasta el 60 % del texto
  var leidas = {}, seg = 0;
  setInterval(function () {
    var id = notaId(); if (!id || document.hidden) return;
    seg++;
    var art = document.querySelector('.nota-body') || document.querySelector('article') || document.body;
    var r = art.getBoundingClientRect(), vista = r.height > 0 ? (innerHeight - r.top) / r.height : 0;
    if (!leidas[id] && (seg >= 30 || vista >= 0.6)) { leidas[id] = 1; med({ t: 'lee', nid: id, pg: location.pathname, ub: seg >= 30 ? '30s' : 'scroll' }); }
  }, 1000);
  window.addEventListener('hashchange', function () { seg = 0; });
  document.addEventListener('auxclick', onClick, true);

  // Impresiones: aviso visible ≥50 % durante ≥1 s, una vez por aviso y lugar por página vista
  if (!('IntersectionObserver' in window)) return;
  var visibles = new Set(), vistos = {}, previos = {}, pagina = location.pathname + location.hash;
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (en) { if (en.intersectionRatio >= 0.5) visibles.add(en.target); else visibles.delete(en.target); });
  }, { threshold: [0, 0.5, 1] });
  var observados = new WeakSet();
  function escanear() {
    document.querySelectorAll('.r5, .spof-i, .brl5 a, .nx-oro .r5i').forEach(function (n) {
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
        if (previos[k] && !vistos[k]) { vistos[k] = 1; send('aviso_visto', d); }
      });
    });
    previos = actuales;
  }, 1000);
  escanear();
  var tm; new MutationObserver(function () { clearTimeout(tm); tm = setTimeout(escanear, 300); }).observe(document.body || document.documentElement, { childList: true, subtree: true });
})();
/* fija el nombre de cada aviso apenas carga, antes de que el traductor del navegador lo cambie */
(function () { var S = '.spof-i, .r5i, .brl5 a'; function fijar() { try { document.querySelectorAll(S).forEach(function (a) { if (a.dataset.an5) return; a.setAttribute('translate', 'no'); var im = a.querySelector('img'), b = a.querySelector('.spof-i b, h4, b'); var n = ((a.classList.contains('spof-i') && b && b.textContent) || (im && im.getAttribute('alt')) || (b && b.textContent) || a.getAttribute('title') || a.textContent || '').replace(/\s+/g, ' ').trim().replace(/ · Sponsor oficial$/, '').slice(0, 80); if (n && !/[　-鿿가-힯]/.test(n)) a.dataset.an5 = n; }); } catch (e) {} } [300, 1200, 3000, 6000].forEach(function (t) { setTimeout(fijar, t); }); })();
