/* Pie del sitio: créditos + Política editorial en ventana de lectura */
(function () {
  if (window.__pie) return; window.__pie = 1;
  var CRED = '<span class="pie-lk"><a href="/privacidad" style="color:inherit">Política de privacidad</a> · <a href="#politica-editorial" class="pie-ed" style="color:inherit">Política editorial</a> · <a href="/med.php" rel="nofollow" class="pie-ad" style="color:inherit;opacity:.7">Admin</a></span>';
  var POL = '<h2>Política editorial</h2>' +
    '<p>Energías LATAM es un medio especializado abierto a todos los actores del sector energético y de las estaciones de servicio.</p>' +
    '<p>Elegimos los contenidos por su relevancia y utilidad para nuestros lectores. La contratación de publicidad no garantiza cobertura editorial ni trato preferencial.</p>' +
    '<p>Identificamos los contenidos patrocinados y distinguimos la información de las opiniones.</p>' +
    '<p>La asesoría técnica contribuye al rigor de las publicaciones y no otorga privilegios a ninguna empresa.</p>' +
    '<p>Cuando exista una relación comercial o profesional relevante para una nota, la informaremos en esa publicación.</p>' +
    '<p>Corregimos los errores comprobados de forma clara.</p>' +
    '<h3>Créditos</h3>' +
    '<p class="pie-cd"><b>Producción general:</b> Amigos Camioneros<br><b>Gestión comercial:</b> Savia – Gente &amp; Gestión<br><b>Asesoría técnica y contenidos:</b> Arq. Diego Alejandro Pérez, a título personal.</p>';
  var css = document.createElement('style');
  css.textContent = [
        '.cred5 .pie-lk{white-space:nowrap}',
    '.pie-md{position:fixed;inset:0;z-index:9999;background:rgba(12,26,41,.6);display:flex;align-items:center;justify-content:center;padding:16px}',
    '.pie-md[hidden]{display:none}',
    '.pie-bx{background:#fff;color:#0F213D;max-width:640px;width:100%;max-height:85vh;overflow:auto;border-radius:12px;border-top:6px solid #0F213D;box-shadow:0 18px 50px rgba(0,0,0,.3);padding:28px 30px 24px;position:relative;font:400 16px/1.6 Barlow,Arial,sans-serif}',
    '.pie-bx h2{font:400 34px/1 "Bebas Neue",sans-serif;letter-spacing:.5px;margin:0 0 14px;color:#0F213D}',
    '.pie-bx p{margin:0 0 12px;color:#25384F}',
    '.pie-bx h3{font:400 22px/1 "Bebas Neue",sans-serif;letter-spacing:.5px;margin:22px 0 10px;padding-top:16px;border-top:1px solid #E3E9F0;color:#0F213D}',
    '.pie-bx .pie-cd{font-size:15px;line-height:1.75}',
    '.pie-x{position:absolute;top:10px;right:12px;border:0;background:transparent;font:400 30px/1 Barlow,Arial,sans-serif;color:#4A5B6C;cursor:pointer;padding:4px 8px}',
    '.pie-x:hover{color:#C0252D}',
    '@media(max-width:560px){.pie-bx{padding:22px 18px 16px}.pie-bx h2{font-size:28px}}'
  ].join('\n');
  document.head.appendChild(css);

  var md, last;
  function abrir(e) {
    if (e) e.preventDefault();
    if (!md) {
      md = document.createElement('div'); md.className = 'pie-md'; md.hidden = true;
      md.innerHTML = '<div class="pie-bx" role="dialog" aria-modal="true" aria-labelledby="pie-t" tabindex="-1"><button class="pie-x" type="button" aria-label="Cerrar">×</button>' + POL.replace('<h2>', '<h2 id="pie-t">') + '</div>';
      document.body.appendChild(md);
      md.addEventListener('click', function (ev) { if (ev.target === md || ev.target.closest('.pie-x')) cerrar(); });
    }
    last = document.activeElement; md.hidden = false; document.documentElement.style.overflow = 'hidden';
    md.querySelector('.pie-bx').focus();
  }
  function cerrar() { if (!md || md.hidden) return; md.hidden = true; document.documentElement.style.overflow = ''; if (last && last.focus) last.focus(); }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') cerrar(); });
  document.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('a.pie-ed'); if (a) abrir(e); });
  if (location.hash === '#politica-editorial') setTimeout(abrir, 300);

  function poner() {
    var c = document.querySelector('.cred5');
    if (!c) {
      // Páginas secundarias: pie simple (p.ft) con el link de privacidad → se agrega el de Política editorial al lado
      var pf = document.querySelector('p.ft'), pr = pf && pf.querySelector('a[href*="privacidad"]');
      if (pr) { if (!pf.querySelector('a.pie-ed')) pr.insertAdjacentHTML('afterend', ' · <a href="#politica-editorial" class="pie-ed" style="color:inherit">Política editorial</a> · <a href="/med.php" rel="nofollow" class="pie-ad" style="color:inherit;opacity:.7">Admin</a>'); return true; }
      var ft = document.querySelector('footer'); if (!ft) return false; c = document.createElement('p'); c.className = 'cred5'; ft.appendChild(c); }
    if (c.getAttribute('data-pie') !== '1') { c.innerHTML = CRED; c.setAttribute('data-pie', '1'); }
    return true;
  }
  var n = 0, t = setInterval(function () { poner(); if (++n > 12) clearInterval(t); }, 500);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', poner); else poner();
})();
/* Guía de proveedores: la lista sale del panel de administración (guia.php) */
(function () {
  if (window.__guiaExtra) return; window.__guiaExtra = 2;
  var n = 0, t = setInterval(function () {
    n++;
    var pl = document.getElementById('p-list');
    if (!pl || typeof PROV === 'undefined' || (PROV.length <= 5 && n < 12)) { if (n > 40) clearInterval(t); return; }
    clearInterval(t);
    fetch('/guia.php?json', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (J) {
      if (!J || !J.completo || !J.items || J.items.length < 5) return;
      var L = J.items;
      var E = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
      var shown = function (u) { return String(u).replace(/^https?:\/\//, '').replace(/^www\./, '').replace(/\/$/, ''); };
      var tl = function (x) { var d = x.replace(/\D/g, ''); if (/^0/.test(d)) d = '595' + d.slice(1); return d.indexOf('0800') === 0 ? d : '+' + d; };
      var qi = document.getElementById('p-q'), sel = document.getElementById('p-type'), ct = document.getElementById('p-count');
      if (qi) { var q2 = qi.cloneNode(true); qi.replaceWith(q2); qi = q2; }
      if (sel) { var s2 = sel.cloneNode(false); s2.innerHTML = '<option value="">Todos los tipos</option>'; sel.replaceWith(s2); sel = s2; }
      var ts = []; L.forEach(function (p) { (p.ts || []).forEach(function (x) { if (ts.indexOf(x) < 0) ts.push(x); }); }); ts.sort();
      ts.forEach(function (x) { var o = document.createElement('option'); o.textContent = x; sel && sel.appendChild(o); });
      function card(p) {
        var c = [];
        if (p.tel) c.push('<div><span><a href="tel:' + E(tl(p.tel)) + '">Tel.: ' + E(p.tel) + '</a>' + (p.wa ? ' · <a class="wa5" href="https://wa.me/' + E(p.wa) + '" target="_blank" rel="noopener">WhatsApp</a>' : '') + '</span><button class="copy" type="button" data-copy="' + E(p.tel) + '">Copiar</button></div>');
        else if (p.wa) c.push('<div><span><a class="wa5" href="https://wa.me/' + E(p.wa) + '" target="_blank" rel="noopener">WhatsApp</a></span></div>');
        if (p.mail) c.push('<div><span><a href="mailto:' + E(p.mail) + '">' + E(p.mail) + '</a></span><button class="copy" type="button" data-copy="' + E(p.mail) + '">Copiar</button></div>');
        if (p.web) c.push('<div><span><a href="' + E(p.web) + '" target="_blank" rel="noopener">' + E(shown(p.web)) + ' ↗</a></span></div>');
        if (!p.f) {
          var cs = []; if (p.tel) cs.push('<a href="tel:' + E(tl(p.tel)) + '">Tel.: ' + E(p.tel) + '</a>'); if (p.wa) cs.push('<a class="wa5" href="https://wa.me/' + E(p.wa) + '" target="_blank" rel="noopener">WhatsApp</a>'); if (p.mail) cs.push('<a href="mailto:' + E(p.mail) + '">' + E(p.mail) + '</a>');
          return '<article class="prov basic5" data-lk="1"><h3>' + E(p.n) + '</h3><span class="c5">' + E((p.ts || []).join(' · ')) + '</span>' + (p.web ? '<a class="w5" href="' + E(p.web) + '" target="_blank" rel="noopener">' + E(shown(p.web)) + ' ↗</a>' : '') +
            (cs.length ? '<button type="button" class="vc5" aria-expanded="false">Ver contacto</button><div class="ct5" hidden>' + cs.join(' · ') + '</div>' : '') + '</article>';
        }
        return '<article class="prov feat" data-lk="1"><header><span class="cat">' + E((p.ts || []).join(' · ')) + '</span><span class="badge">DESTACADO</span></header>' +
          (p.l ? '<img class="plogo" src="' + E(p.l) + '" alt="">' : '') + '<h3>' + E(p.n) + '</h3><p>' + E(p.o) + '</p><p style="font-size:14px">Zona: ' + E(p.z || 'Paraguay') + '</p>' + (c.length ? '<div class="contact">' + c.join('') + '</div>' : '') + '</article>';
      }
      function draw() {
        var q = (qi ? qi.value : '').trim().toLowerCase(), ty = sel ? sel.value : '';
        var R = L.filter(function (p) { return (!ty || (p.ts || []).indexOf(ty) >= 0) && (!q || (p.n + ' ' + (p.ts || []).join(' ') + ' ' + p.o).toLowerCase().indexOf(q) >= 0); })
          .sort(function (a, b) { return (b.f ? 1 : 0) - (a.f ? 1 : 0); });
        if (ct) ct.textContent = R.length + (R.length === 1 ? ' empresa' : ' empresas');
        pl.innerHTML = R.length ? R.map(card).join('') : '<p style="padding:20px 52px">No hay empresas para esa búsqueda. Probá con otro tipo o palabra.</p>';
      }
      if (qi) qi.addEventListener('input', draw); if (sel) sel.addEventListener('change', draw);
      draw();
    }).catch(function () {});
  }, 250);
})();
