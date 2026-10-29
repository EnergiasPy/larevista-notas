/* Recuadro "Informe mensual del MIC" al lado del título de La Estación del Futuro (#noticias).
   Pide el correo, lo manda por mail (form.php · tipo informe), lo suma al newsletter y descarga el PDF en el momento.
   El PDF se arma con /combustible/py (informe-mic.js) en un marco oculto. */
(function () {
  if (window.__infbox) return; window.__infbox = 1;
  var MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'diciembre'];
  var css = document.createElement('style');
  css.textContent = [
    '.ib-row{display:flex;gap:28px;align-items:stretch;justify-content:space-between}',
    '.ib-row>.masthead{flex:1 1 auto;min-width:0}',
    '.ib{flex:0 0 430px;box-sizing:border-box;background:#0F213D;color:#fff;border-radius:12px;border-top:4px solid #3A963E;padding:16px 18px 14px;font-family:Barlow,Arial,sans-serif;align-self:center}',
    '.ib-e{font:700 11px Barlow,Arial,sans-serif;letter-spacing:1.6px;text-transform:uppercase;color:#76C46E;margin:0 0 2px}',
    '.ib h3{font:400 26px/1.05 "Bebas Neue",Barlow,Arial,sans-serif;letter-spacing:.4px;margin:0 0 8px;color:#fff}',
    '.ib-k{display:flex;gap:16px;margin:0 0 10px}.ib-k div{flex:1;min-width:0}.ib-k b{display:block;font:400 28px/1 "Bebas Neue",Barlow,Arial,sans-serif;color:#76C46E}.ib-k span{display:block;font:600 11.5px/1.25 Barlow,Arial,sans-serif;color:#C9D6E3;margin-top:3px}',
    '.ib form{display:flex;gap:8px;margin:0}.ib input[type=email]{flex:1 1 auto;min-width:0;font:500 15px Barlow,Arial,sans-serif;padding:10px 11px;border:0;border-radius:7px;color:#0F213D}',
    '.ib button{flex:0 0 auto;border:0;border-radius:7px;background:#3A963E;color:#fff;font:700 14px Barlow,Arial,sans-serif;padding:10px 13px;cursor:pointer;white-space:nowrap}.ib button:disabled{opacity:.65}',
    '.ib small{display:block;font:500 11.5px/1.35 Barlow,Arial,sans-serif;color:#9FB3C8;margin-top:7px}.ib small a{color:#C9D6E3}',
    '.ib-m{font:600 13.5px/1.4 Barlow,Arial,sans-serif;margin-top:8px}.ib-m.er{color:#FF9C94}.ib-m.ok{color:#B9E4B4}',
    '.ib-dl{display:inline-block;margin-top:8px;background:#fff;color:#0F213D!important;text-decoration:none;font:700 14px Barlow,Arial,sans-serif;padding:9px 14px;border-radius:7px}',
    '.ib-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}',
    '@media(max-width:980px){.ib-row{flex-direction:column;gap:14px}.ib{flex:1 1 auto;width:100%;align-self:stretch}}',
    '@media(max-width:560px){.ib{padding:13px 14px 12px}.ib h3{font-size:22px}.ib-k b{font-size:24px}.ib input[type=email]{font-size:16px}}'
  ].join('\n');
  document.head.appendChild(css);

  function armar() {
    var sec = document.getElementById('v-noticias'); if (!sec) return false;
    var mh = sec.querySelector('.masthead'); if (!mh) return false;
    if (sec.querySelector('.ib')) return true;
    var row = document.createElement('div'); row.className = 'ib-row';
    mh.parentNode.insertBefore(row, mh); row.appendChild(mh);
    var b = document.createElement('aside'); b.className = 'ib'; b.setAttribute('aria-label', 'Informe mensual del mercado de combustibles');
    b.innerHTML = '<p class="ib-e">Datos del sector · Informe gratis</p><h3 class="ib-t">El mercado de combustibles en Paraguay</h3>' +
      '<div class="ib-k"><div><b class="ib-l">…</b><span class="ib-ll">litros vendidos en el último mes publicado por el MIC</span></div><div><b>2.883</b><span>estaciones de servicio en el registro del MIC</span></div></div>' +
      '<form novalidate><input type="email" name="Correo electrónico" placeholder="Tu email" autocomplete="email" inputmode="email" aria-label="Tu email"><div class="ib-hp" aria-hidden="true"><input name="hp_x" tabindex="-1" autocomplete="off"></div><button type="submit">Recibir el informe</button></form>' +
      '<small>Ranking por emblema, quién creció, precios, estaciones y GLP en PDF. Te lo mandamos por mail y te sumamos al newsletter semanal; te podés dar de baja cuando quieras. <a href="/privacidad">Privacidad</a></small><div class="ib-m" hidden></div>';
    row.appendChild(b);
    var T0 = Date.now();
    // dato del último mes
    var Y = new Date().getFullYear();
    fetch('/mic.php?y=' + Y).then(function (r) { return r.json(); }).then(function (j) {
      var tot = {}; (j.vp || []).forEach(function (r) { tot[r[0]] = (tot[r[0]] || 0) + r[3]; });
      var ms = Object.keys(tot).map(Number).sort(function (a, c) { return a - c; }); if (!ms.length) return;
      var m = ms[ms.length - 1];
      b.querySelector('.ib-l').textContent = (tot[m] / 1e6).toLocaleString('es-PY', { maximumFractionDigits: 1 }) + ' M';
      b.querySelector('.ib-ll').textContent = 'litros vendidos en ' + MESES[m - 1] + ' ' + Y + ' (último mes del MIC)';
      b.querySelector('.ib-e').textContent = 'Datos del sector · Informe ' + MESES[m - 1] + ' ' + Y;
    }).catch(function () {});
    var f = b.querySelector('form'), msg = b.querySelector('.ib-m'), bt = f.querySelector('button');
    function aviso(t, cl) { msg.className = 'ib-m ' + cl; msg.innerHTML = t; msg.hidden = false; }
    f.addEventListener('submit', function (e) {
      e.preventDefault(); msg.hidden = true;
      var m = f.elements['Correo electrónico'].value.trim();
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(m)) { aviso('Escribí un email válido.', 'er'); return; }
      bt.disabled = true; bt.textContent = 'Preparando…';
      var fd = new FormData(); fd.append('tipo', 'informe'); fd.append('el', Date.now() - T0); fd.append('hp_x', f.elements['hp_x'].value);
      fd.append('Correo electrónico', m); fd.append('Origen', 'informe_mic');
      fetch('/form.php', { method: 'POST', body: fd }).then(function (r) { return r.json(); }).then(function (j) {
        if (!j.ok) throw 0;
        try { if (typeof gtag === 'function') gtag('event', 'generate_lead', { form: 'informe_mic' }); } catch (x) {}
        aviso('¡Listo! Te lo mandamos a <b>' + m.replace(/[&<>"]/g, '') + '</b>. Estamos armando el PDF para que lo descargues ahora…', 'ok');
        pdf();
      }).catch(function () { bt.disabled = false; bt.textContent = 'Recibir el informe'; aviso('No se pudo enviar. Probá de nuevo o escribinos a <a href="mailto:info@energiaslatam.com" style="color:#fff">info@energiaslatam.com</a>.', 'er'); });
    });
    function pdf() {
      var fr = document.createElement('iframe'); fr.setAttribute('aria-hidden', 'true'); fr.tabIndex = -1;
      fr.style.cssText = 'position:absolute;left:-10000px;top:0;width:1200px;height:900px;border:0;opacity:0;pointer-events:none';
      fr.src = '/combustible/py?embed=1';
      var fin = function (ok, r) {
        bt.disabled = false; bt.textContent = 'Recibir el informe';
        if (!ok) { aviso('Te lo mandamos por mail. Si no llega en unos minutos, revisá Promociones o Spam. También podés <a class="ib-dl" href="/combustible/py?informe=1">descargarlo acá</a>', 'ok'); return; }
        var u = URL.createObjectURL(r.blob);
        aviso('¡Listo! También te lo mandamos por mail. <br><a class="ib-dl" href="' + u + '" download="' + r.nombre + '">⬇ Descargar el informe (PDF)</a>', 'ok');
        try { var a = document.createElement('a'); a.href = u; a.download = r.nombre; document.body.appendChild(a); a.click(); a.remove(); } catch (x) {}
        try { if (typeof gtag === 'function') gtag('event', 'file_download', { file_name: r.nombre, informe: 'mic' }); } catch (x) {}
        setTimeout(function () { fr.remove(); }, 1000);
      };
      fr.onload = function () {
        var w = fr.contentWindow, t = 0;
        (function esp() { if (w.informeMIC) { w.informeMIC().then(function (r) { fin(true, r); }).catch(function () { fin(false); }); } else if (++t < 40) setTimeout(esp, 250); else fin(false); })();
      };
      document.body.appendChild(fr);
    }
    return true;
  }
  var n = 0, iv = setInterval(function () { if (armar() || ++n > 40) clearInterval(iv); }, 300);
})();
