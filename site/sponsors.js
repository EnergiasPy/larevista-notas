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
    '.spof-in{max-width:1180px;margin:0 auto;padding:12px 16px}',
    '.spof-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}',
    '.spof-h span{font:700 12px Barlow,Arial,sans-serif;letter-spacing:2px;text-transform:uppercase;color:#0F213D}',
    '.spof-h small{font:600 11px Barlow,Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;color:#8A99A8}',
    '.spof-g{display:grid;grid-template-columns:1fr 1fr;gap:14px}',
    '.spof-i{display:flex;align-items:center;gap:16px;background:#fff;border:1px solid #DCE3EA;border-left:6px solid var(--bc);border-radius:10px;padding:12px 18px;text-decoration:none!important;color:#0F213D!important;box-shadow:0 2px 8px rgba(15,33,61,.06);transition:box-shadow .2s}',
    '.spof-i:hover{box-shadow:0 6px 18px rgba(15,33,61,.14)}',
    '.spof-i img{height:48px;width:auto;max-width:150px;object-fit:contain;flex:none}',
    '.spof-i b{display:block;font:400 26px/1 "Bebas Neue",sans-serif;letter-spacing:.5px}',
    '.spof-i em{display:block;font:600 13px Barlow,Arial,sans-serif;font-style:normal;color:#4A5B6C;margin-top:2px}',
    '.sp5{display:none!important}',
    '@media(max-width:560px){.spof-in{padding:10px 12px}.spof-g{gap:8px}.spof-i{flex-direction:column;align-items:flex-start;gap:6px;padding:10px 12px}.spof-i img{height:34px;max-width:110px}.spof-i b{font-size:20px}}',
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
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', poner); else poner();
})();
