/* Sponsors oficiales · la misma franja en todas las páginas de energiaslatam.com */
(function () {
  var SP = [
    { n: 'Shell', url: 'https://www.shell.com.py', logo: '/img/logos/shell.png', c: '#FBCE07' },
    { n: 'Nextar', url: 'https://www.nextar.com.py', logo: '/img/logos/nextar.png', c: '#1B4F9C' }
  ];
  if (document.getElementById('spOf')) return;
  var css = document.createElement('style');
  css.textContent = [
    '.spof{background:#F4F6F9;border-bottom:1px solid #E3E9F0}',
    '.spof-in{max-width:1180px;margin:0 auto;padding:16px 16px 18px}',
    '.spof-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}',
    '.spof-h span{font:700 12px Barlow,Arial,sans-serif;letter-spacing:2px;text-transform:uppercase;color:#0F213D}',
    '.spof-h small{font:600 11px Barlow,Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;color:#8A99A8}',
    '.spof-g{display:grid;grid-template-columns:1fr 1fr;gap:18px}',
    '.spof-i{display:flex;align-items:center;gap:16px;background:#fff;border:1px solid #DCE3EA;border-left:10px solid var(--bc);border-bottom:4px solid var(--bc);border-radius:10px;min-height:170px;padding:20px 32px;text-decoration:none!important;color:#0F213D!important;box-shadow:0 2px 8px rgba(15,33,61,.06);transition:box-shadow .2s}',
    '.spof-i:hover{box-shadow:0 6px 18px rgba(15,33,61,.14)}',
    '.spof-i img{height:120px;width:auto;max-width:260px;object-fit:contain;flex:none}',
    '.spof-i b{display:block;font:400 46px/1 "Bebas Neue",sans-serif;letter-spacing:.5px}',
    '.spof-i em{display:block;font:700 14px Barlow,Arial,sans-serif;font-style:normal;letter-spacing:1px;text-transform:uppercase;color:#4A5B6C;margin-top:4px}',
    '.sp5{display:none!important}',
    '@media(max-width:860px){.spof-i{min-height:120px;padding:14px 18px}.spof-i img{height:70px;max-width:170px}.spof-i b{font-size:32px}}',
    '@media(max-width:560px){.spof-in{padding:10px 12px}.spof-g{gap:8px}.spof-i{flex-direction:column;align-items:flex-start;gap:6px;min-height:0;padding:12px}.spof-i img{height:50px;max-width:130px}.spof-i b{font-size:24px}.spof-i em{font-size:11px}}',
    '.apb{background:#F4F6F9;border-bottom:1px solid #E3E9F0}',
    '.apb-in{max-width:1180px;margin:0 auto;padding:0 16px 18px}',
    '.apb-a{position:relative;display:flex;align-items:center;gap:28px;background:#fff;border:1px solid #DCE3EA;border-left:10px solid #3B4BA0;border-bottom:4px solid #D7263D;border-radius:10px;padding:18px 28px;text-decoration:none!important;color:#0F213D!important;box-shadow:0 2px 8px rgba(15,33,61,.06);transition:box-shadow .2s}',
    '.apb-a:hover{box-shadow:0 6px 18px rgba(15,33,61,.14)}',
    '.apb-a img{height:96px;width:auto;max-width:300px;object-fit:contain;flex:none}',
    '.apb-t{flex:1;min-width:0}',
    '.apb-t b{display:block;font:400 44px/1 "Bebas Neue",sans-serif;letter-spacing:.5px}.apb-t b span{color:#D7263D}',
    '.apb-t em{display:block;font:700 14px/1.35 Barlow,Arial,sans-serif;font-style:normal;letter-spacing:1px;text-transform:uppercase;color:#4A5B6C;margin-top:6px}',
    '.apb-c{flex:none;background:#3A963E;color:#fff;font:700 17px Barlow,Arial,sans-serif;padding:14px 24px;border-radius:6px;white-space:nowrap}',
    '.apb-g{position:absolute;top:6px;right:10px;font:600 10px Barlow,Arial,sans-serif;letter-spacing:1.5px;text-transform:uppercase;color:#8A99A8}',
    '@media(max-width:860px){.apb-a{gap:16px;padding:14px 18px}.apb-a img{height:64px;max-width:190px}.apb-t b{font-size:32px}.apb-t em{font-size:12px}.apb-c{font-size:15px;padding:11px 16px}}',
    '@media(max-width:560px){.apb-in{padding:0 12px 10px}.apb-a{flex-direction:column;align-items:flex-start;gap:8px;padding:14px 12px}.apb-a img{height:48px;max-width:160px}.apb-t b{font-size:26px}.apb-t em{font-size:11px}.apb-c{width:100%;text-align:center}}',
    '@media print{.apb{display:none}}',
    '@media print{.spof{display:none}}'
  ].join('\n');
  document.head.appendChild(css);
  function poner() {
    if (document.getElementById('spOf')) return;
    var s = document.createElement('section');
    s.className = 'spof'; s.id = 'spOf'; s.setAttribute('aria-label', 'Sponsors oficiales');
    s.innerHTML = '<div class="spof-in"><div class="spof-h"><span>Sponsors oficiales</span><small>Publicidad</small></div><div class="spof-g">' +
      SP.map(function (x) { return '<a class="spof-i" href="' + x.url + '" target="_blank" rel="noopener sponsored" style="--bc:' + x.c + '"><img src="' + x.logo + '" alt="' + x.n + '"><span><b>' + x.n + '</b><em>Sponsor oficial</em></span></a>'; }).join('') +
      '</div></div>';
    var ref = document.getElementById('cz2') || document.querySelector('header.top') || document.querySelector('header');
    if (ref && ref.parentNode) ref.parentNode.insertBefore(s, ref.nextSibling); else document.body.insertBefore(s, document.body.firstChild);
    s.addEventListener('click', function (e) { var a = e.target.closest('a'); if (!a) return; try { gtag('event', 'sponsor_click', { sponsor: a.querySelector('b').textContent }); } catch (x) {} });
  }
  function apesa() {
    if (document.getElementById('apB') || location.pathname.indexOf('/apesa') === 0) return;
    var sp = document.getElementById('spOf'); if (!sp) return;
    var b = document.createElement('section');
    b.className = 'apb'; b.id = 'apB'; b.setAttribute('aria-label', 'Espacio institucional: APESA');
    b.innerHTML = '<div class="apb-in"><a class="apb-a" href="/apesa.html"><span class="apb-g">Institucional</span><img src="/img/apesa-logo.jpg" alt="APESA"><span class="apb-t"><b>Asociate y sé parte de <span>APESA</span></b><em>Asociación de Propietarios y Operadores de Estaciones de Servicios y Afines</em></span><span class="apb-c">Quiero asociarme</span></a></div>';
    sp.parentNode.insertBefore(b, sp.nextSibling);
    b.addEventListener('click', function () { try { gtag('event', 'apesa_banner_click'); } catch (x) {} });
  }
  // Medición de publicidad (clicks, impresiones y UTM) en todas las páginas
  if (!document.querySelector('script[src*="adtrack.js"]')) { var at = document.createElement('script'); at.src = '/adtrack.js?v=8'; at.defer = true; document.head.appendChild(at); }
  if (!document.querySelector('script[src*="pie.js"]')) { var pj = document.createElement('script'); pj.src = '/pie.js?v=3'; pj.defer = true; document.head.appendChild(pj); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { poner(); apesa(); }); else { poner(); apesa(); }
})();
