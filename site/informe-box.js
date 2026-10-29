/* Recuadro "Informe mensual del MIC" en la portada, al lado del título La Estación del Futuro (.pv-mast).
   Compacto: una sola línea, no más alto que el título.
   Pide el correo, lo manda por mail (form.php · tipo informe), lo suma al newsletter y descarga el PDF en el momento.
   El PDF se arma con /combustible/py (informe-mic.js) en un marco oculto. */
(function () {
  if (window.__infbox) return; window.__infbox = 1;
  var MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'diciembre'];
  var css = document.createElement('style');
  css.textContent = [
    '.pv-mast p{min-width:200px!important}',
    '.pv-mast .ib{flex:0 1 470px;min-width:340px;box-sizing:border-box;display:flex;align-items:center;gap:12px;height:52px;margin:0;padding:0 7px 0 14px;background:#F2F8F2;border:1px solid #CFE3CF;border-radius:12px;font-family:Barlow,Arial,sans-serif}',
    '.pv-mast .ib-t{flex:0 0 auto;margin:0;color:#0F213D;font:700 14px/1.15 Barlow,Arial,sans-serif;white-space:nowrap}.pv-mast .ib-t b{display:block;margin:0 0 1px;color:#3A963E;font:700 10.5px/1.2 Barlow,Arial,sans-serif;letter-spacing:1.3px;text-transform:uppercase}',
    '.pv-mast .ib form{flex:1 1 auto;display:flex;align-items:stretch;gap:0;margin:0;padding:0;min-width:0;height:38px}',
    '.pv-mast .ib input[type=email]{flex:1 1 auto;min-width:0;width:auto;height:38px!important;min-height:0!important;margin:0!important;padding:0 11px!important;box-sizing:border-box;border:1px solid #C9D3DE!important;border-right:0!important;border-radius:8px 0 0 8px!important;background:#fff!important;box-shadow:none!important;color:#0F213D;font:500 14.5px/36px Barlow,Arial,sans-serif!important;outline:0}',
    '.pv-mast .ib input[type=email]:focus{border-color:#3A963E!important}',
    '.pv-mast .ib form button{flex:0 0 auto;height:38px!important;min-height:0!important;margin:0!important;padding:0 14px!important;box-sizing:border-box;border:0!important;border-radius:0 8px 8px 0!important;background:#3A963E!important;box-shadow:none!important;transform:none!important;color:#fff!important;font:700 14px/38px Barlow,Arial,sans-serif!important;letter-spacing:.2px;white-space:nowrap;cursor:pointer}',
    '.pv-mast .ib form button:hover{background:#2E7D32!important}.pv-mast .ib form button:disabled{opacity:.7}',
    '.pv-mast .ib-m{flex:1 1 auto;min-width:0;margin:0;color:#2E7D32;font:700 13.5px/1.2 Barlow,Arial,sans-serif;display:flex;align-items:center;justify-content:space-between;gap:8px;white-space:nowrap;overflow:hidden}.pv-mast .ib-m.er{color:#B3261E}',
    '.pv-mast .ib-dl{flex:0 0 auto;display:inline-block;margin:0;background:#3A963E;color:#fff!important;text-decoration:none;font:700 13.5px/38px Barlow,Arial,sans-serif;height:38px;padding:0 14px;border-radius:8px;white-space:nowrap}',
    '.ib-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}',
    '.pv-mast .ib-i{position:relative;flex:0 0 auto;width:22px!important;height:22px!important;min-height:0!important;min-width:0!important;margin:0!important;padding:0!important;border:1.5px solid #9FB3C8!important;border-radius:50%!important;background:transparent!important;box-shadow:none!important;color:#7A8A9B!important;font:700 12px/19px Georgia,serif!important;text-align:center;cursor:help}',
    '.pv-mast .ib-i:hover:after,.pv-mast .ib-i:focus:after{content:attr(data-tip);position:absolute;right:-6px;top:30px;width:270px;z-index:30;background:#0F213D;color:#fff;font:500 12.5px/1.4 Barlow,Arial,sans-serif;text-align:left;padding:10px 12px;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.25);white-space:normal}',
    '@media(max-width:560px){.pv-mast .ib{flex:1 1 100%;min-width:0;height:50px;padding:0 6px 0 6px;gap:8px}.pv-mast .ib-t{display:none}.pv-mast .ib input[type=email]{font-size:16px!important}}'
  ].join('\n');
  document.head.appendChild(css);

  var TIP = 'Informe en PDF con datos oficiales del MIC: ranking por emblema, quién creció, precios, estaciones y GLP. Al pedirlo, tu mail queda registrado para recibir el newsletter y noticias de Energías LATAM; te podés dar de baja cuando quieras.';
  // ventana emergente: aviso de registro antes de enviar, y agradecimiento si ya estaba registrado
  var cssV = document.createElement('style');
  cssV.textContent = '.ibv{position:fixed;inset:0;z-index:100001;background:rgba(10,22,40,.62);display:flex;align-items:center;justify-content:center;padding:16px}' +
    '.ibv-b{position:relative;width:100%;max-width:420px;background:#fff;border-radius:14px;border-top:5px solid #3A963E;box-shadow:0 20px 60px rgba(0,0,0,.35);padding:24px 22px 20px;font-family:Barlow,Arial,sans-serif;color:#0F213D;box-sizing:border-box;text-align:center}' +
    '.ibv-b h3{font:400 30px/1.05 "Bebas Neue",Barlow,Arial,sans-serif;letter-spacing:.4px;margin:0 0 10px}.ibv-b p{font:500 15.5px/1.45 Barlow,Arial,sans-serif;color:#24384F;margin:0 0 16px}' +
    '.ibv-b .ibv-k{width:52px;height:52px;border-radius:50%;background:#E8F4E8;color:#3A963E;font:700 28px/52px Arial,sans-serif;margin:0 auto 10px}' +
    '.ibv-a{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}.ibv-a button{border:0;border-radius:8px;font:700 15px Barlow,Arial,sans-serif;padding:12px 18px;cursor:pointer}' +
    '.ibv-ok{background:#3A963E;color:#fff}.ibv-no{background:#EEF2F6;color:#24384F}.ibv-b small{display:block;margin-top:12px;font:500 12px Barlow,Arial,sans-serif;color:#7A8A9B}.ibv-b small a{color:#2E7D32}';
  document.head.appendChild(cssV);
  function ventana(html, botones) {
    var v = document.createElement('div'); v.className = 'ibv'; v.setAttribute('role', 'dialog'); v.setAttribute('aria-modal', 'true');
    v.innerHTML = '<div class="ibv-b">' + html + '<div class="ibv-a">' + botones.map(function (b, i) { return '<button type="button" class="' + b[1] + '" data-i="' + i + '">' + b[0] + '</button>'; }).join('') + '</div></div>';
    function cerrar() { v.remove(); document.removeEventListener('keydown', esc); }
    function esc(e) { if (e.key === 'Escape') cerrar(); }
    v.addEventListener('click', function (e) { var b = e.target.closest('button[data-i]'); if (b) { cerrar(); var fn = botones[+b.dataset.i][2]; if (fn) fn(); } else if (e.target === v) cerrar(); });
    document.addEventListener('keydown', esc); document.body.appendChild(v);
    setTimeout(function () { var b = v.querySelector('.ibv-ok'); if (b) b.focus(); }, 30);
  }
  function limpio(m) { return m.replace(/[&<>"]/g, ''); }
  function confirmar(m, si) {
    ventana('<p class="ib-e2" style="font:700 11px Barlow,Arial,sans-serif;letter-spacing:1.6px;text-transform:uppercase;color:#3A963E;margin:0 0 4px">Informe del mercado de combustibles</p><h3>Antes de enviarlo</h3>' +
      '<p>Al solicitar este informe, tu mail <b>' + limpio(m) + '</b> queda registrado automáticamente para recibir el newsletter y las noticias de Energías LATAM.</p>',
      [['Sí, quiero el informe', 'ibv-ok', si], ['Cancelar', 'ibv-no', null]]);
    var v = document.querySelector('.ibv-b'); if (v) v.insertAdjacentHTML('beforeend', '<small>Te podés dar de baja cuando quieras. <a href="/privacidad" target="_blank" rel="noopener">Política de privacidad</a></small>');
  }
  function gracias(m) {
    ventana('<div class="ibv-k">✓</div><h3>¡Gracias por confiar en Energías LATAM!</h3><p>Tu mail <b>' + limpio(m) + '</b> ya estaba registrado. Igual te mandamos el informe por mail y lo estamos preparando para que lo descargues ahora.</p>',
      [['Seguir', 'ibv-ok', null]]);
  }
  function armar() {
    var w = document.querySelector('.pv-mast .wrap'); if (!w) return false;
    if (w.querySelector('.ib')) return true;
    var b = document.createElement('div'); b.className = 'ib'; b.setAttribute('role', 'group'); b.setAttribute('aria-label', 'Informe mensual del mercado de combustibles');
    b.innerHTML = '<span class="ib-t"><b class="ib-e">Informe MIC</b>Combustibles en PDF</span>' +
      '<form novalidate><input type="email" name="Correo electrónico" placeholder="Tu email" autocomplete="email" inputmode="email" aria-label="Tu email para recibir el informe del MIC"><div class="ib-hp" aria-hidden="true"><input name="hp_x" tabindex="-1" autocomplete="off"></div><button type="submit">Recibir PDF</button></form>' +
      '<div class="ib-m" hidden></div><button type="button" class="ib-i" aria-label="' + TIP + '" data-tip="' + TIP + '">i</button>';
    w.appendChild(b);
    try { if (matchMedia('(max-width:560px)').matches) b.querySelector('input[type=email]').placeholder = 'Informe MIC: tu email'; } catch (x) {}
    var T0 = Date.now(), Y = new Date().getFullYear(), YA = false;
    fetch('/mic.php?y=' + Y).then(function (r) { return r.json(); }).then(function (j) {
      var m = 0; (j.vp || []).forEach(function (r) { if (r[0] > m) m = r[0]; }); if (!m) return;
      var M = MESES[m - 1]; b.querySelector('.ib-e').textContent = 'Informe MIC · ' + M.charAt(0).toUpperCase() + M.slice(1) + ' ' + Y;
    }).catch(function () {});
    var f = b.querySelector('form'), msg = b.querySelector('.ib-m'), bt = f.querySelector('button'), inp = f.querySelector('input[type=email]');
    function aviso(t, cl) { msg.className = 'ib-m' + (cl ? ' ' + cl : ''); msg.innerHTML = t; msg.hidden = false; }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var m = inp.value.trim();
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(m)) { inp.focus(); inp.setCustomValidity('Escribí un email válido'); inp.reportValidity(); setTimeout(function () { inp.setCustomValidity(''); }, 2500); return; }
      confirmar(m, function () { enviar(m); });
    });
    function enviar(m) {
      bt.disabled = true; bt.textContent = 'Enviando…';
      var fd = new FormData(); fd.append('tipo', 'informe'); fd.append('el', Date.now() - T0); fd.append('hp_x', f.elements['hp_x'].value);
      fd.append('Correo electrónico', m); fd.append('Origen', 'informe_mic');
      fetch('/form.php', { method: 'POST', body: fd }).then(function (r) { return r.json(); }).then(function (j) {
        if (!j.ok) throw 0;
        try { if (typeof gtag === 'function') gtag('event', 'generate_lead', { form: 'informe_mic' }); } catch (x) {}
        f.style.display = 'none'; YA = !!j.ya; aviso('✓ Enviado a tu mail. Armando el PDF…');
        if (YA) gracias(m);
        pdf();
      }).catch(function () { bt.disabled = false; bt.textContent = 'Recibir PDF'; f.style.display = 'none'; aviso('No se pudo enviar. <a href="#" class="ib-re" style="color:#fff">Probá de nuevo</a>', 'er'); msg.querySelector('.ib-re').onclick = function (ev) { ev.preventDefault(); msg.hidden = true; f.style.display = ''; }; });
    }
    function pdf() {
      var fr = document.createElement('iframe'); fr.setAttribute('aria-hidden', 'true'); fr.tabIndex = -1;
      fr.style.cssText = 'position:absolute;left:-10000px;top:0;width:1200px;height:900px;border:0;opacity:0;pointer-events:none';
      fr.src = '/combustible/py?embed=1';
      var fin = function (ok, r) {
        var pre = '<span>✓ Enviado a tu mail</span>';
        if (!ok) { aviso(pre + '<a class="ib-dl" href="/combustible/py?informe=1">⬇ PDF</a>'); return; }
        var u = URL.createObjectURL(r.blob);
        aviso(pre + '<a class="ib-dl" href="' + u + '" download="' + r.nombre + '">⬇ Descargar PDF</a>');
        try { var a = document.createElement('a'); a.href = u; a.download = r.nombre; document.body.appendChild(a); a.click(); a.remove(); } catch (x) {}
        try { if (typeof gtag === 'function') gtag('event', 'file_download', { file_name: r.nombre, informe: 'mic' }); } catch (x) {}
        setTimeout(function () { fr.remove(); }, 1000);
      };
      fr.onload = function () {
        var w2 = fr.contentWindow, t = 0;
        (function esp() { if (w2.informeMIC) { w2.informeMIC().then(function (r) { fin(true, r); }).catch(function () { fin(false); }); } else if (++t < 40) setTimeout(esp, 250); else fin(false); })();
      };
      document.body.appendChild(fr);
    }
    return true;
  }
  var n = 0, iv = setInterval(function () { if (armar() || ++n > 40) clearInterval(iv); }, 300);
})();
