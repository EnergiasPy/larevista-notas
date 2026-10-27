/* Pie del sitio: créditos + Política editorial en ventana de lectura */
(function () {
  if (window.__pie) return; window.__pie = 1;
  var CRED = '<span class="pie-cr"><b>Producción general:</b> Amigos Camioneros</span>' +
    '<span class="pie-cr"><b>Gestión comercial:</b> Savia – Gente &amp; Gestión</span>' +
    '<span class="pie-cr"><b>Asesoría técnica y contenidos:</b> Arq. Diego Alejandro Pérez, a título personal.</span>' +
    '<span class="pie-lk"><a href="/privacidad" style="color:inherit">Política de privacidad</a> · <a href="#politica-editorial" class="pie-ed" style="color:inherit">Política editorial</a></span>';
  var POL = '<h2>Política editorial</h2>' +
    '<p>Energías LATAM es un medio especializado abierto a todos los actores del sector energético y de las estaciones de servicio.</p>' +
    '<p>Elegimos los contenidos por su relevancia y utilidad para nuestros lectores. La contratación de publicidad no garantiza cobertura editorial ni trato preferencial.</p>' +
    '<p>Identificamos los contenidos patrocinados y distinguimos la información de las opiniones.</p>' +
    '<p>La asesoría técnica contribuye al rigor de las publicaciones y no otorga privilegios a ninguna empresa.</p>' +
    '<p>Cuando exista una relación comercial o profesional relevante para una nota, la informaremos en esa publicación.</p>' +
    '<p>Corregimos los errores comprobados de forma clara.</p>';
  var css = document.createElement('style');
  css.textContent = [
    '.cred5 .pie-cr,.cred5 .pie-lk{display:inline-block;margin-right:14px}',
    '.cred5 .pie-lk{white-space:nowrap}',
    '.pie-md{position:fixed;inset:0;z-index:9999;background:rgba(12,26,41,.6);display:flex;align-items:center;justify-content:center;padding:16px}',
    '.pie-md[hidden]{display:none}',
    '.pie-bx{background:#fff;color:#0F213D;max-width:640px;width:100%;max-height:85vh;overflow:auto;border-radius:12px;border-top:6px solid #0F213D;box-shadow:0 18px 50px rgba(0,0,0,.3);padding:28px 30px 24px;position:relative;font:400 16px/1.6 Barlow,Arial,sans-serif}',
    '.pie-bx h2{font:400 34px/1 "Bebas Neue",sans-serif;letter-spacing:.5px;margin:0 0 14px;color:#0F213D}',
    '.pie-bx p{margin:0 0 12px;color:#25384F}',
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
    if (!c) { var ft = document.querySelector('footer'); if (!ft) return false; c = document.createElement('p'); c.className = 'cred5'; ft.appendChild(c); }
    if (c.getAttribute('data-pie') !== '1') { c.innerHTML = CRED; c.setAttribute('data-pie', '1'); }
    return true;
  }
  var n = 0, t = setInterval(function () { poner(); if (++n > 12) clearInterval(t); }, 500);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', poner); else poner();
})();
