/* Dentro de cada nota: "Leé también", "Hoy en La Estación", Oro en la columna (PC) y "Notas relacionadas".
   No cambia el texto de la nota ni los avisos Plata/Bronce. */
(function () {
  if (window.__notaExtra) return; window.__notaExtra = 1;
  var RAW = 'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/';
  var STOP = ' de la el los las y en a con por para del que se un una su al lo como mas más ya o es son sus hasta desde sobre entre tras pero sin cada este esta estos estas ese esa hoy '.split(' ');
  function esc(s) { return String(s || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function img(n) { var i = n.img_portada || n.img || ''; return /^https?:/.test(i) ? i : RAW + i; }
  function kw(n) { var o = {}; ((n.titulo || '') + ' ' + (n.bajada || '')).toLowerCase().replace(/[^a-záéíóúñü0-9 ]/g, ' ').split(/\s+/).forEach(function (w) { if (w.length > 3 && STOP.indexOf(w) < 0) o[w] = 1; }); return o; }
  function fch(f) { var p = (f || '').split('-'); return p.length === 3 ? p[2] + '/' + p[1] : ''; }

  var css = document.createElement('style');
  css.textContent = [
    '.nx-lt{border-left:4px solid #3A963E;background:#F2F8F2;padding:12px 16px;margin:6px 0 20px;border-radius:0 8px 8px 0}',
    '.nx-lt b{display:block;font:700 11px Barlow,Arial,sans-serif;letter-spacing:1.6px;text-transform:uppercase;color:#3A963E;margin-bottom:4px}',
    '.nx-lt a{font:700 17px/1.3 Barlow,Arial,sans-serif;color:#0F213D!important;text-decoration:none}',
    '.nx-h{font:400 24px/1 "Bebas Neue",sans-serif;letter-spacing:.5px;color:#0F213D;border-top:3px solid #0F213D;padding-top:8px;margin:0 0 10px}',
    '.nx-si{display:grid;grid-template-columns:96px 1fr;gap:10px;padding:10px 0;border-bottom:1px solid #E3E9F0;color:inherit;text-decoration:none}',
    '.nx-si img{width:96px;height:64px;object-fit:cover;object-position:left top;border-radius:6px;background:#EEF2F6}',
    '.nx-c{display:block;font:700 10.5px Barlow,Arial,sans-serif;letter-spacing:1.4px;color:#3A963E;text-transform:uppercase}',
    '.nx-si strong{font:700 14.5px/1.3 Barlow,Arial,sans-serif;color:#0F213D}',
    '.nx-all{display:block;margin:10px 0 0;font:700 14px Barlow,Arial,sans-serif;color:#2E7D32!important;text-decoration:none}',
    '.nx-side{display:none}',
    '.nx-oro{margin-top:22px}.nx-oro .nx-oh{display:flex;justify-content:space-between;font:700 10.5px Barlow,Arial,sans-serif;letter-spacing:1.6px;color:#B08500;margin-bottom:8px}.nx-oro .nx-oh span{color:#8A99A8}',
    '.nx-oro .r5i{display:flex!important;flex-direction:column;align-items:center;justify-content:center;gap:6px;position:relative!important;opacity:1!important;inset:auto!important;height:140px;margin:0 0 10px;border:1px solid #DCE3EA;border-bottom:4px solid #D4A017;border-radius:8px;text-align:center;padding:14px;text-decoration:none!important}',
    '.nx-oro .r5i img{max-height:60px!important;max-width:200px!important;width:auto!important;height:auto!important;object-fit:contain}',
    '.nx-oro .r5i .lgw{height:auto!important;margin:0!important}.nx-oro .r5i b{font:400 21px/1.1 "Bebas Neue",sans-serif!important;letter-spacing:.5px}.nx-oro .r5i small{font:600 12.5px Barlow,Arial,sans-serif;opacity:.8}',
    '.nx-oro .r5i .tag5{position:absolute;top:6px;right:10px;font-size:9px}',
    '.nx-rel{margin:30px 0 10px}.nx-rg{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}',
    '.nx-rc{color:inherit;text-decoration:none}.nx-rc img{width:100%;aspect-ratio:3/2;object-fit:cover;object-position:left top;border-radius:8px;display:block;background:#EEF2F6;margin-bottom:8px}',
    '.nx-rc strong{display:block;font:700 16.5px/1.3 Barlow,Arial,sans-serif;color:#0F213D;margin-top:3px}.nx-rc small{color:#7A8A9B;font:600 12.5px Barlow,Arial,sans-serif}',
    '.nx-hoy-m{margin:26px 0 0}',
    '@media(min-width:1100px){',
    '  .nx-grid{display:grid!important;grid-template-columns:minmax(0,760px) 1fr;gap:40px;align-items:start}',
    '  .nx-side{display:block;align-self:stretch}.nx-oro{position:sticky;top:120px}',
    '  .nx-hoy-m{display:none}',
    '  .nx-grid .nota-body .oroh5.mid5{display:none!important}',
    '}',
    '@media(max-width:1099px){.nx-oro{display:none}}',
    '@media(max-width:820px){.nx-rg{grid-template-columns:1fr;gap:14px}.nx-rc{display:grid;grid-template-columns:110px 1fr;gap:12px}.nx-rc img{aspect-ratio:1/1;margin:0}}'
  ].join('\n');
  document.head.appendChild(css);

  function armar(notas) {
    var art = document.getElementById('gh-art'); if (!art || art.getAttribute('data-nx')) return false;
    var nb0 = art.querySelector('.nota-body'); if (!nb0 || nb0.querySelectorAll(':scope > p').length < 3 || !art.querySelector('.tail5')) return false;
    var id = window.NOTA_ID || (location.pathname.match(/^\/n\/([a-z0-9-]+)/) || [])[1]; if (!id) return false;
    var pub = (notas || []).filter(function (n) { return n.estado === 'publicada'; }).sort(function (a, b) { return a.fecha < b.fecha ? 1 : a.fecha > b.fecha ? -1 : 0; });
    var cur = pub.filter(function (n) { return n.id === id; })[0]; if (!cur) return false;
    art.setAttribute('data-nx', '1');
    var K = kw(cur), otras = pub.filter(function (n) { return n.id !== id; });
    function score(n) { var s = n.cat === cur.cat ? 3 : 0, k = kw(n); for (var w in k) if (K[w]) s++; return s; }
    var rel = otras.map(function (n) { return [score(n), n.cat === cur.cat ? 1 : 0, n.fecha, n]; })
      .sort(function (a, b) { return b[0] - a[0] || b[1] - a[1] || (a[2] < b[2] ? 1 : a[2] > b[2] ? -1 : 0); })
      .slice(0, 3).map(function (x) { return x[3]; });
    var relIds = rel.map(function (n) { return n.id; });
    var hoy = otras.filter(function (n) { return n.fecha === cur.fecha; });
    var ult = otras.filter(function (n) { return n.fecha !== cur.fecha; });
    var lista = hoy.concat(ult).slice(0, 4);
    function si(n) { return '<a class="nx-si" href="/n/' + esc(n.id) + '"><img src="' + esc(img(n)) + '" alt="" loading="lazy"><span><span class="nx-c">' + esc(n.cat) + '</span><strong>' + esc(n.titulo) + '</strong></span></a>'; }

    // 1 · Leé también, después del segundo párrafo
    var nb = art.querySelector('.nota-body'), ps = nb ? nb.querySelectorAll(':scope > p') : [];
    if (rel[0] && ps.length > 2) ps[1].insertAdjacentHTML('afterend', '<aside class="nx-lt"><b>Leé también</b><a href="/n/' + esc(rel[0].id) + '">' + esc(rel[0].titulo) + '</a></aside>');

    // 2 · Notas relacionadas, antes del pie de Bronce
    var relH = '<section class="nx-rel" aria-label="Notas relacionadas"><h3 class="nx-h">Notas relacionadas</h3><div class="nx-rg">' +
      rel.map(function (n) { return '<a class="nx-rc" href="/n/' + esc(n.id) + '"><img src="' + esc(img(n)) + '" alt="" loading="lazy"><span><span class="nx-c">' + esc(n.cat) + '</span><strong>' + esc(n.titulo) + '</strong><small>' + fch(n.fecha) + '</small></span></a>'; }).join('') + '</div></section>';
    var tail = art.querySelector('.tail5');
    if (tail) tail.insertAdjacentHTML('beforebegin', relH); else art.insertAdjacentHTML('beforeend', relH);

    // 3 · Hoy en La Estación: en celular, después de las relacionadas (máx. 3)
    var hm = '<section class="nx-hoy-m" aria-label="Más notas"><h3 class="nx-h">Hoy en La Estación</h3>' + lista.slice(0, 3).map(si).join('') + '<a class="nx-all" href="/#noticias">Ver todas las notas →</a></section>';
    art.querySelector('.nx-rel').insertAdjacentHTML('afterend', hm);

    // 4 · Columna derecha (PC): Hoy en La Estación + Proveedores Oro
    var wrap = art.parentElement; wrap.classList.add('nx-grid');
    var side = document.createElement('aside'); side.className = 'nx-side'; side.setAttribute('aria-label', 'Hoy en La Estación');
    side.innerHTML = '<h3 class="nx-h">Hoy en La Estación</h3>' + lista.map(si).join('') + '<a class="nx-all" href="/#noticias">Ver todas las notas →</a>';
    wrap.appendChild(side);
    var mid = nb && nb.querySelector('.oroh5.mid5');
    if (mid) {
      var vistos = {}, items = [];
      [].forEach.call(mid.querySelectorAll('.r5i'), function (a) { var h = a.getAttribute('href'); if (h && !vistos[h]) { vistos[h] = 1; items.push(a); } });
      if (items.length) {
        var box = document.createElement('div'); box.className = 'nx-oro lat5';
        box.innerHTML = '<div class="nx-oh">PROVEEDORES ORO<span>PUBLICIDAD</span></div><div class="nx-ol"></div>';
        side.appendChild(box);
        var ol = box.querySelector('.nx-ol'), k = 0;
        function mostrar() {
          ol.innerHTML = '';
          for (var j = 0; j < Math.min(3, items.length); j++) { var or = items[(k + j) % items.length], c = or.cloneNode(true), cs = getComputedStyle(or); c.classList.remove('on'); if (cs.backgroundColor && cs.backgroundColor !== 'rgba(0, 0, 0, 0)') c.style.setProperty('background', cs.backgroundColor, 'important'); c.style.setProperty('color', cs.color, 'important'); ol.appendChild(c); }
        }
        mostrar();
        if (items.length > 3) setInterval(function () { if (document.hidden) return; k = (k + 3) % items.length; mostrar(); }, 8000);
      }
    }
    return true;
  }
  var datos = fetch(RAW + 'notas.json', { cache: 'no-store' }).then(function (r) { return r.json(); }).catch(function () { return []; });
  function go() { datos.then(function (n) {
    var t = 0, iv = setInterval(function () {
      var art = document.getElementById('gh-art');
      // si el lector volvió a dibujar la nota, se arma de nuevo
      if (art && art.getAttribute('data-nx') && !art.querySelector('.nx-rel')) { art.removeAttribute('data-nx'); var o = document.querySelector('.nx-side'); if (o) o.remove(); }
      armar(n); if (++t > 60) clearInterval(iv);
    }, 500); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
})();

/* Escuchar la nota: lectura en voz alta con la voz en español del celular o la compu (sin archivos ni costo) */
(function () {
  if (window.__notaVoz || !('speechSynthesis' in window) || typeof SpeechSynthesisUtterance === 'undefined') return; window.__notaVoz = 1;
  var S = window.speechSynthesis, voz = null, cola = [], i = 0, estado = 'parado', btn = null, stopB = null, artAct = null;
  var css = document.createElement('style');
  css.textContent = '.vz5{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:14px 0 18px}' +
    '.vz5 button{display:inline-flex;align-items:center;gap:8px;border:0;border-radius:24px;cursor:pointer;font:700 15px Barlow,Arial,sans-serif}' +
    '.vz5 .vz-p{background:#0F213D;color:#fff;padding:10px 18px}.vz5 .vz-p:hover{background:#17305A}' +
    '.vz5 .vz-s{background:#EEF2F6;color:#0F213D;padding:10px 14px}.vz5 small{font:500 13px Barlow,Arial,sans-serif;color:#4A5B6C}' +
    '.vz5 svg{width:18px;height:18px;fill:currentColor}.vz-on{background:#FFF7E0;border-radius:4px}';
  document.head.appendChild(css);
  var IC = { play: '<svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3A4.5 4.5 0 0 0 14 8v8a4.5 4.5 0 0 0 2.5-4zM14 3.2v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6z"/></svg>', pause: '<svg viewBox="0 0 24 24"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>' };
  function elegir() {
    var V = S.getVoices().filter(function (v) { return /^es/i.test(v.lang) && !/eddy|flo\b|grandma|grandpa|reed|rocko|sandy|shelley|news|bells|boing|bubbles|jester|organ|whisper|zarvox|trinoids|wobble|albert|cellos|superstar|junior|ralph|fred|kathy/i.test(v.name); }); if (!V.length) return null;
    var pref = ['es-PY', 'es-AR', 'es-UY', 'es-419', 'es-US', 'es-MX', 'es-CL', 'es-CO', 'es-ES'];
    var nota = function (v) { var n = (v.name || '').toLowerCase(), p = pref.indexOf(v.lang.replace('_', '-')); return (p < 0 ? 20 : p) - (/natural|neural|online|google|premium|enhanced|mejorad/.test(n) ? 10 : 0); };
    return V.sort(function (a, b) { return nota(a) - nota(b); })[0];
  }
  function limpiar(t) {
    return t.replace(/\s+/g, ' ')
      .replace(/G\.\s?([\d.,]+)/g, '$1 guaraníes').replace(/US\$\s?([\d.,]+)/g, '$1 dólares').replace(/\$\s?([\d.,]+)/g, '$1 pesos')
      .replace(/\bNdR\b/g, 'Nota de redacción').replace(/\bEESS\b/g, 'estaciones de servicio').replace(/\bkWh\b/g, 'kilovatios hora').replace(/≈\s?/g, 'unos ').replace(/·/g, ',');
  }
  function textos(art) {
    var out = [], h = art.querySelector('h1'), b = art.querySelector('.bajada, .lead, h1 + p');
    if (h) out.push({ t: h.textContent }); if (b && b !== h) out.push({ t: b.textContent });
    var nb = art.querySelector('.nota-body'); if (!nb) return out;
    [].forEach.call(nb.querySelectorAll(':scope > p, :scope > h2, :scope > h3, :scope > ul > li, :scope > ol > li, :scope > blockquote'), function (el) {
      if (el.closest('.oroh5, .nx-lt, .nx-rel, .vz5, figure')) return; var t = el.textContent.trim(); if (t) out.push({ t: t, el: el });
    });
    return out;
  }
  function trozos(L) {
    var c = []; L.forEach(function (x) { limpiar(x.t).replace(/([.!?:;])\s+(?=[A-ZÁÉÍÓÚÑ¿¡"«0-9])/g, '$1\u0001').split('\u0001').forEach(function (s) { if (s.trim()) c.push({ t: s.trim(), el: x.el }); }); }); return c;
  }
  function marcar(el) { document.querySelectorAll('.vz-on').forEach(function (e) { e.classList.remove('vz-on'); }); if (el) el.classList.add('vz-on'); }
  function pintar() {
    if (!btn) return;
    btn.innerHTML = (estado === 'leyendo' ? IC.pause + 'Pausar' : IC.play + (estado === 'pausa' ? 'Seguir escuchando' : 'Escuchar la nota'));
    if (stopB) stopB.hidden = estado === 'parado';
  }
  function hablar() {
    if (i >= cola.length) { detener(); return; }
    var u = new SpeechSynthesisUtterance(cola[i].t); if (voz) { u.voice = voz; u.lang = voz.lang; } else u.lang = 'es-419';
    u.rate = 1.02; u.pitch = 1;
    u.onstart = function () { marcar(cola[i] && cola[i].el); };
    u.onend = function () { if (estado !== 'leyendo') return; i++; hablar(); };
    u.onerror = function () { if (estado === 'leyendo') { i++; hablar(); } };
    S.speak(u);
  }
  function detener() { estado = 'parado'; i = 0; S.cancel(); marcar(null); pintar(); }
  function alternar() {
    var art = document.getElementById('gh-art'); if (!art) return;
    if (estado === 'leyendo') { estado = 'pausa'; S.cancel(); pintar(); return; } // pausa = se corta y sigue desde la misma frase
    if (estado === 'parado') { voz = voz || elegir(); cola = trozos(textos(art)); i = 0; try { if (typeof gtag === 'function') gtag('event', 'escuchar_nota', { nota: (location.pathname.split('/n/')[1] || '') }); } catch (e) {} }
    estado = 'leyendo'; S.cancel(); pintar(); setTimeout(hablar, 80);
  }
  function poner() {
    var art = document.getElementById('gh-art'); if (!art) return;
    if (artAct && artAct !== art) detener();
    if (art.querySelector('.vz5')) { artAct = art; return; }
    var nb = art.querySelector('.nota-body'); if (!nb || nb.querySelectorAll(':scope > p').length < 2) return;
    artAct = art;
    var w = document.createElement('div'); w.className = 'vz5';
    w.innerHTML = '<button type="button" class="vz-p" aria-label="Escuchar la nota en voz alta"></button><button type="button" class="vz-s" hidden>Detener</button><small>Lectura con la voz de tu dispositivo</small>';
    nb.parentNode.insertBefore(w, nb);
    btn = w.querySelector('.vz-p'); stopB = w.querySelector('.vz-s');
    btn.addEventListener('click', alternar); stopB.addEventListener('click', detener);
    estado = 'parado'; pintar();
  }
  if (S.onvoiceschanged !== undefined) S.onvoiceschanged = function () { voz = elegir(); };
  window.addEventListener('pagehide', function () { S.cancel(); });
  window.addEventListener('hashchange', function () { if (estado !== 'parado') detener(); });
  setInterval(poner, 700);
})();
