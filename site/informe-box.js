/* Recuadro "Informe mensual del MIC" en la portada, al lado del título La Estación del Futuro (.pv-mast).
   Compacto: una sola línea, no más alto que el título.
   Pide el correo, lo manda por mail (form.php · tipo informe), lo suma al newsletter y descarga el PDF en el momento.
   El PDF se arma con /combustible/py (informe-mic.js) en un marco oculto. */
(function () {
  if (window.__infbox) return; window.__infbox = 1;
  var MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'diciembre'];
  var css = document.createElement('style');
  css.textContent = [
    '.ib{flex:0 1 520px;min-width:0;box-sizing:border-box;display:flex;align-items:center;gap:10px;background:#0F213D;border-radius:10px;border-left:4px solid #3A963E;padding:6px 6px 6px 12px;font-family:Barlow,Arial,sans-serif;height:46px}',
    '.ib-t{flex:0 0 auto;color:#fff;font:700 13px/1.15 Barlow,Arial,sans-serif;white-space:nowrap}.ib-t b{display:block;color:#76C46E;font:700 10.5px Barlow,Arial,sans-serif;letter-spacing:1.4px;text-transform:uppercase}',
    '.ib form{flex:1 1 auto;display:flex;gap:6px;margin:0;min-width:0}',
    '.ib input[type=email]{flex:1 1 auto;min-width:0;font:500 14px Barlow,Arial,sans-serif;padding:0 10px;height:34px;border:0;border-radius:6px;color:#0F213D;box-sizing:border-box}',
    '.ib button{flex:0 0 auto;height:34px;border:0;border-radius:6px;background:#3A963E;color:#fff;font:700 13.5px Barlow,Arial,sans-serif;padding:0 12px;cursor:pointer;white-space:nowrap}.ib button:disabled{opacity:.65}',
    '.ib-m{flex:1 1 auto;min-width:0;color:#B9E4B4;font:600 13px/1.25 Barlow,Arial,sans-serif;overflow:hidden}.ib-m.er{color:#FF9C94}',
    '.ib-dl{display:inline-block;background:#fff;color:#0F213D!important;text-decoration:none;font:700 13px Barlow,Arial,sans-serif;padding:7px 11px;border-radius:6px;white-space:nowrap;margin-left:6px}',
    '.ib-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}',
    '.ib-i{position:relative;flex:0 0 auto;width:20px;height:20px;border-radius:50%;border:0;background:rgba(255,255,255,.14);color:#C9D6E3;font:700 12px/20px Arial,sans-serif;text-align:center;cursor:help;padding:0}',
    '.ib-i:hover:after,.ib-i:focus:after{content:attr(data-tip);position:absolute;right:0;top:26px;width:260px;z-index:20;background:#0F213D;color:#fff;font:500 12px/1.35 Barlow,Arial,sans-serif;text-align:left;padding:9px 11px;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.25)}',
    '@media(max-width:560px){.ib{flex:1 1 100%;padding:5px 5px 5px 10px;height:44px}.ib-t{display:none}.ib input[type=email]{font-size:16px}}'
  ].join('\n');
  document.head.appendChild(css);

  var TIP = 'Informe en PDF con datos oficiales del MIC: ranking por emblema, quién creció, precios, estaciones y GLP. Te lo mandamos por mail y te sumamos al newsletter semanal; te podés dar de baja cuando quieras.';
  function armar() {
    var w = document.querySelector('.pv-mast .wrap'); if (!w) return false;
    if (w.querySelector('.ib')) return true;
    var b = document.createElement('div'); b.className = 'ib'; b.setAttribute('role', 'group'); b.setAttribute('aria-label', 'Informe mensual del mercado de combustibles');
    b.innerHTML = '<span class="ib-t"><b class="ib-e">Informe MIC</b>Combustibles en PDF</span>' +
      '<form novalidate><input type="email" name="Correo electrónico" placeholder="Tu email" autocomplete="email" inputmode="email" aria-label="Tu email para recibir el informe del MIC"><div class="ib-hp" aria-hidden="true"><input name="hp_x" tabindex="-1" autocomplete="off"></div><button type="submit">Recibir PDF</button></form>' +
      '<div class="ib-m" hidden></div><button type="button" class="ib-i" aria-label="' + TIP + '" data-tip="' + TIP + '">i</button>';
    w.appendChild(b);
    try { if (matchMedia('(max-width:560px)').matches) b.querySelector('input[type=email]').placeholder = 'Informe MIC: tu email'; } catch (x) {}
    var T0 = Date.now(), Y = new Date().getFullYear();
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
      bt.disabled = true; bt.textContent = 'Enviando…';
      var fd = new FormData(); fd.append('tipo', 'informe'); fd.append('el', Date.now() - T0); fd.append('hp_x', f.elements['hp_x'].value);
      fd.append('Correo electrónico', m); fd.append('Origen', 'informe_mic');
      fetch('/form.php', { method: 'POST', body: fd }).then(function (r) { return r.json(); }).then(function (j) {
        if (!j.ok) throw 0;
        try { if (typeof gtag === 'function') gtag('event', 'generate_lead', { form: 'informe_mic' }); } catch (x) {}
        f.style.display = 'none'; aviso('✓ Te lo mandamos por mail. Armando el PDF…');
        pdf();
      }).catch(function () { bt.disabled = false; bt.textContent = 'Recibir PDF'; f.style.display = 'none'; aviso('No se pudo enviar. <a href="#" class="ib-re" style="color:#fff">Probá de nuevo</a>', 'er'); msg.querySelector('.ib-re').onclick = function (ev) { ev.preventDefault(); msg.hidden = true; f.style.display = ''; }; });
    });
    function pdf() {
      var fr = document.createElement('iframe'); fr.setAttribute('aria-hidden', 'true'); fr.tabIndex = -1;
      fr.style.cssText = 'position:absolute;left:-10000px;top:0;width:1200px;height:900px;border:0;opacity:0;pointer-events:none';
      fr.src = '/combustible/py?embed=1';
      var fin = function (ok, r) {
        if (!ok) { aviso('✓ Te lo mandamos por mail.<a class="ib-dl" href="/combustible/py?informe=1">⬇ PDF</a>'); return; }
        var u = URL.createObjectURL(r.blob);
        aviso('✓ Te lo mandamos por mail.<a class="ib-dl" href="' + u + '" download="' + r.nombre + '">⬇ Descargar PDF</a>');
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
