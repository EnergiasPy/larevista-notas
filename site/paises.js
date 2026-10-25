// paises.js · banderas y selector de país para "El combustible en números"
(function () {
  var F = {
    py: '<rect width="30" height="20" fill="#fff"/><rect width="30" height="6.67" fill="#D52B1E"/><rect y="13.33" width="30" height="6.67" fill="#0038A8"/><circle cx="15" cy="10" r="2.6" fill="none" stroke="#0038A8" stroke-width=".8"/><circle cx="15" cy="10" r="1" fill="#F5D000"/>',
    ar: '<rect width="30" height="20" fill="#74ACDF"/><rect y="6.67" width="30" height="6.67" fill="#fff"/><circle cx="15" cy="10" r="2.2" fill="#F6B40E"/>',
    cl: '<rect width="30" height="20" fill="#fff"/><rect y="10" width="30" height="10" fill="#D52B1E"/><rect width="10" height="10" fill="#0039A6"/><path d="M5 2.6l1 3h3.1l-2.5 1.9.9 3-2.5-1.8-2.5 1.8.9-3L.9 5.6H4z" fill="#fff"/>',
    pe: '<rect width="30" height="20" fill="#fff"/><rect width="10" height="20" fill="#D91023"/><rect x="20" width="10" height="20" fill="#D91023"/>',
    uy: '<rect width="30" height="20" fill="#fff"/><g fill="#0038A8"><rect y="2.2" width="30" height="2.2"/><rect y="6.7" width="30" height="2.2"/><rect y="11.1" width="30" height="2.2"/><rect y="15.6" width="30" height="2.2"/></g><rect width="12" height="11.1" fill="#fff"/><circle cx="6" cy="5.5" r="3" fill="#FCD116"/>',
    bo: '<rect width="30" height="6.67" fill="#D52B1E"/><rect y="6.67" width="30" height="6.67" fill="#F9E300"/><rect y="13.33" width="30" height="6.67" fill="#007934"/>'
  };
  var N = { py: 'Paraguay', ar: 'Argentina', cl: 'Chile', pe: 'Perú', uy: 'Uruguay', bo: 'Bolivia' };
  var ORD = ['py', 'ar', 'cl', 'pe', 'uy', 'bo'];
  function flag(c, w) { return '<svg viewBox="0 0 30 20" width="' + (w || 30) + '" height="' + Math.round((w || 30) * 2 / 3) + '" aria-hidden="true" style="border-radius:3px;box-shadow:0 0 0 1px rgba(15,33,61,.15);flex:none">' + F[c] + '</svg>'; }
  window.PAISES = { F: F, N: N, ORD: ORD, flag: flag };
  var el = document.getElementById('paises');
  if (!el) return;
  var cur = el.getAttribute('data-actual') || '';
  el.innerHTML = '<a href="/combustible" class="ps-all">Todos</a>' + ORD.map(function (c) {
    return '<a href="/combustible/' + c + '" class="ps-it' + (c === cur ? ' on' : '') + '">' + flag(c, 26) + '<span>' + N[c] + '</span></a>';
  }).join('');
  var st = document.createElement('style');
  st.textContent = '#paises{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}#paises a{display:inline-flex;align-items:center;gap:8px;padding:7px 12px;border-radius:999px;background:#fff;border:1.5px solid #D5DEE8;color:#0F213D;text-decoration:none;font:600 14px Barlow,Arial,sans-serif}#paises a.on{background:#0F213D;border-color:#0F213D;color:#fff}#paises a:hover{border-color:#3A963E}';
  document.head.appendChild(st);
})();
