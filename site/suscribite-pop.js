/* Ventana emergente de suscripción al newsletter · energiaslatam.com
   Se abre con cualquier botón o enlace "Suscribite" (#suscribite, /newsletter, /newsletter#nl, la franja beta y el botón verde).
   Envía los mismos datos que la página /newsletter (form.php, tipo newsletter). */
(function () {
  if (window.__supop) return; window.__supop = 1;
  var css = document.createElement('style');
  css.textContent = [
    '.sp-ov{position:fixed;inset:0;z-index:100000;background:rgba(10,22,40,.62);display:flex;align-items:center;justify-content:center;padding:16px;opacity:0;transition:opacity .18s}',
    '.sp-ov.on{opacity:1}',
    '.sp-bx{position:relative;width:100%;max-width:440px;max-height:calc(100vh - 32px);overflow:auto;background:#fff;border-radius:14px;border-top:5px solid #3A963E;box-shadow:0 20px 60px rgba(0,0,0,.35);padding:26px 24px 20px;font-family:Barlow,Arial,sans-serif;color:#0F213D;box-sizing:border-box}',
    '.sp-x{position:absolute;top:8px;right:10px;width:38px;height:38px;border:0;background:none;font-size:28px;line-height:1;color:#7A8A9B;cursor:pointer}',
    '.sp-e{font:700 11px Barlow,Arial,sans-serif;letter-spacing:1.6px;text-transform:uppercase;color:#3A963E;margin:0 0 4px}',
    '.sp-bx h2{font:400 32px/1 "Bebas Neue",Barlow,Arial,sans-serif;letter-spacing:.5px;margin:0 0 6px;color:#0F213D}',
    '.sp-bx p{font:500 15px/1.4 Barlow,Arial,sans-serif;margin:0 0 14px;color:#24384F}',
    '.sp-bx label{display:block;font:700 13px Barlow,Arial,sans-serif;margin:0 0 4px;color:#24384F}',
    '.sp-bx input[type=text],.sp-bx input[type=email]{display:block;width:100%;box-sizing:border-box;font:500 16px Barlow,Arial,sans-serif;padding:11px 12px;border:1px solid #C9D3DE;border-radius:8px;margin:0 0 10px;color:#0F213D;background:#fff}',
    '.sp-bx input:focus{outline:2px solid #3A963E;outline-offset:0;border-color:#3A963E}',
    '.sp-bx button.sp-go{display:block;width:100%;margin:4px 0 0;padding:13px;border:0;border-radius:8px;background:#3A963E;color:#fff;font:700 16px Barlow,Arial,sans-serif;letter-spacing:.5px;cursor:pointer}',
    '.sp-bx button.sp-go:disabled{opacity:.6}',
    '.sp-er{color:#B3261E;font:600 13.5px Barlow,Arial,sans-serif;margin:8px 0 0}',
    '.sp-sm{display:block;font:500 12.5px Barlow,Arial,sans-serif;color:#7A8A9B;margin:10px 0 0;text-align:center}',
    '.sp-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}',
    '.sp-ok{text-align:center;padding:8px 0 4px}.sp-ok .sp-ck{width:54px;height:54px;border-radius:50%;background:#E8F4E8;color:#3A963E;font:700 30px/54px Arial,sans-serif;margin:0 auto 10px}',
    'body.sp-lock{overflow:hidden}'
  ].join('\n');
  document.head.appendChild(css);

  var ov = null, T0 = 0;
  function abrir(origen) {
    if (ov) return;
    T0 = Date.now();
    ov = document.createElement('div'); ov.className = 'sp-ov'; ov.setAttribute('role', 'dialog'); ov.setAttribute('aria-modal', 'true'); ov.setAttribute('aria-label', 'Suscribite al newsletter');
    ov.innerHTML = '<div class="sp-bx"><button type="button" class="sp-x" aria-label="Cerrar">×</button>' +
      '<div class="sp-in"><p class="sp-e">Newsletter semanal · Gratis</p><h2>Suscribite a La Estación del Futuro</h2>' +
      '<p>Todos los lunes, lo más importante del sector de estaciones de servicio en tu correo.</p>' +
      '<form novalidate><label for="sp-n">Nombre</label><input id="sp-n" name="Nombre" type="text" autocomplete="given-name">' +
      '<label for="sp-m">Tu email</label><input id="sp-m" name="Correo electrónico" type="email" autocomplete="email" inputmode="email" placeholder="nombre@empresa.com.py">' +
      '<label for="sp-c">Empresa o estación <span style="font-weight:400;color:#7A8A9B">(opcional)</span></label><input id="sp-c" name="Empresa" type="text" autocomplete="organization">' +
      '<div class="sp-hp" aria-hidden="true"><input name="hp_x" tabindex="-1" autocomplete="off"></div>' +
      '<button type="submit" class="sp-go">Quiero recibirlo</button><div class="sp-er" hidden></div></form>' +
      '<small class="sp-sm">Es gratis y te podés dar de baja cuando quieras.</small></div></div>';
    document.body.appendChild(ov); document.body.classList.add('sp-lock');
    requestAnimationFrame(function () { ov.classList.add('on'); });
    var f = ov.querySelector('form'), er = ov.querySelector('.sp-er');
    setTimeout(function () { try { ov.querySelector('#sp-n').focus(); } catch (x) {} }, 60);
    ov.addEventListener('click', function (e) { if (e.target === ov || e.target.closest('.sp-x') || e.target.closest('.sp-cerrar')) cerrar(); });
    f.addEventListener('submit', function (e) {
      e.preventDefault(); er.hidden = true;
      var n = f.elements['Nombre'].value.trim(), m = f.elements['Correo electrónico'].value.trim();
      if (!n || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(m)) { er.textContent = 'Completá tu nombre y un email válido.'; er.hidden = false; return; }
      var b = f.querySelector('button'); b.disabled = true; b.textContent = 'Enviando…';
      var fd = new FormData(); fd.append('tipo', 'newsletter'); fd.append('el', Date.now() - T0); fd.append('hp_x', f.elements['hp_x'].value);
      fd.append('Nombre', n); fd.append('Correo electrónico', m); var em = f.elements['Empresa'].value.trim(); if (em) fd.append('Empresa', em);
      fd.append('Origen', origen || 'ventana');
      fetch('/form.php', { method: 'POST', body: fd }).then(function (r) { return r.json(); }).then(function (j) {
        if (!j.ok) throw 0;
        try { if (typeof gtag === 'function') gtag('event', 'sign_up', { method: 'ventana_' + (origen || 'web') }); } catch (x) {}
        ov.querySelector('.sp-in').innerHTML = '<div class="sp-ok"><div class="sp-ck">✓</div><h2>¡Ya estás suscripto!</h2><p>Gracias por sumarte. Todos los lunes te llega La Estación del Futuro.</p><p style="font-size:13.5px">Para no perderte ninguna edición, agregá <b>info@energiaslatam.com</b> a tus contactos.</p><button type="button" class="sp-go sp-cerrar">Seguir leyendo</button></div>';
      }).catch(function () {
        er.innerHTML = 'No se pudo enviar. Probá de nuevo o escribinos a <a href="mailto:info@energiaslatam.com">info@energiaslatam.com</a>.'; er.hidden = false; b.disabled = false; b.textContent = 'Quiero recibirlo';
      });
    });
    document.addEventListener('keydown', esc);
  }
  function esc(e) { if (e.key === 'Escape') cerrar(); }
  function cerrar() { if (!ov) return; document.removeEventListener('keydown', esc); document.body.classList.remove('sp-lock'); ov.remove(); ov = null; }
  window.abrirSuscripcion = abrir;

  // cualquier botón o enlace de suscripción abre la ventana (en captura, antes que el resto del sitio)
  var SEL = 'a[href="#suscribite"], a[href="/newsletter"], a[href="/newsletter#nl"], a[href="/newsletter.html"], a[href="https://energiaslatam.com/newsletter"]';
  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var a = e.target.closest && e.target.closest(SEL); if (!a) return;
    e.preventDefault(); e.stopPropagation(); if (e.stopImmediatePropagation) e.stopImmediatePropagation();
    var o = a.closest('.betabar, [class*="beta"]') ? 'franja_beta' : a.closest('header') ? 'boton_header' : 'boton';
    abrir(o);
  }, true);
})();
