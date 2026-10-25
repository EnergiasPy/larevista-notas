// combustible-extra.js · Quién creció, precios, red de estaciones, GLP (usa funciones de combustible-py.html)
(function () {
  var X = null, MAPA = null;
  var EMB = { BR: 'Shell', PTBR: 'Petrobras', CPG: 'Copeg', TMG: '3MG', COR: 'Gas Corona', CPT: 'Copetrol', PCH: 'Petrochaco', PMX: 'Petromax', PSR: 'Petrosur', PUM: 'Puma', INT: 'Integral', AXN: 'Axion', CPA: 'Compasa', ECO: 'ECOP', FLP: 'Fuelpar', FRT: '3 Fronteras', HDN: 'Hidronorte', PTN: 'Petron', PTP: 'Petropar', ENX: 'Enex', EGS: 'Energy Gas', ARY: 'Acaray Gas', CSA: 'Copesa', GDE: 'Gas del Este', GTL: 'Gas Total', LGS: 'Lima Gas', MGS: 'Minga Gas', MAE: 'Monte Alegre', NGS: 'Norte Gas', PTG: 'Petrogas', PNR: 'Petronor', SLR: 'Solpar', SGS: 'Sugas', YGS: 'Yacyretá Gas' };
  var PROD = { GTI: 'Gasoil Tipo I', GTIII: 'Gasoil Tipo III', N85: 'Nafta 85', N90: 'Nafta 90', N95: 'Nafta 95', NA97: 'Nafta 97 c/ alcohol', NS97: 'Nafta 97 s/ alcohol' };
  var DEPN = { '00': 'Asunción', '01': 'Concepción', '02': 'San Pedro', '03': 'Cordillera', '04': 'Guairá', '05': 'Caaguazú', '06': 'Caazapá', '07': 'Itapúa', '08': 'Misiones', '09': 'Paraguarí', '10': 'Alto Paraná', '11': 'Central', '12': 'Ñeembucú', '13': 'Amambay', '14': 'Canindeyú', '15': 'Pdte. Hayes', '16': 'Alto Paraguay', '17': 'Boquerón' };
  var GLPN = { 'GAS CORONA SAECA': 'Gas Corona', 'GAS TOTAL SA': 'Gas Total', 'MINGA GAS SA': 'Minga Gas', 'YACYRETA GAS SRL': 'Yacyretá Gas', 'ACARAY GAS SRL': 'Acaray Gas', 'GAS DEL ESTE': 'Gas del Este', 'LIMA GAS SA': 'Lima Gas', 'SUGAS SA': 'Sugas', 'PETROGAS': 'Petrogas', 'NORTE GAS SA': 'Norte Gas', 'ENERGY GAS': 'Energy Gas', 'FAMILY GLOBAL S.A. (GAS-PAR)': 'Gas-Par', 'GAS PORA': 'Gas Porá', 'DASGAS EAS': 'Dasgas', 'SOLPAR': 'Solpar', 'COPESA': 'Copesa', 'PETRONOR': 'Petronor' };
  function $(i) { return document.getElementById(i); }
  function gs(v) { return 'Gs ' + Math.round(v).toLocaleString('es-PY'); }
  function n0(v) { return Math.round(v).toLocaleString('es-PY'); }
  function p1(v) { return (v * 100).toLocaleString('es-PY', { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + '%'; }
  function nomD(id) { var n = X && X.names[id]; return GLPN[n] || nom(n); }
  function lg(n, cls) { return LOGO[n] ? '<span class="lgo' + (n === 'Energy' ? ' dk' : '') + (cls ? ' ' + cls : '') + '"><img src="' + logoUrl(n) + '" alt=""></span>' : '<i class="dot" style="background:' + colorDe(n) + '"></i>'; }
  function seg2(id, cb) { $(id).addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; [].forEach.call(this.children, function (x) { x.classList.toggle('on', x === b); }); cb(b.dataset.v); }); }
  function descargar(cv, nombre) { var a = document.createElement('a'); a.download = nombre; a.href = cv.toDataURL('image/png'); a.click(); try { gtag('event', 'placa_descarga', { placa: nombre }); } catch (e) {} }

  /* ---------- placa horizontal (quién creció / precios) ---------- */
  function fondo(c, W, H) {
    var g = c.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#0A1730'); g.addColorStop(1, '#0F213D'); c.fillStyle = g; c.fillRect(0, 0, W, H);
    var rg = c.createRadialGradient(930, 140, 10, 930, 140, 620); rg.addColorStop(0, 'rgba(118,196,110,.28)'); rg.addColorStop(1, 'rgba(118,196,110,0)'); c.fillStyle = rg; c.fillRect(0, 0, W, H);
    c.save(); c.globalAlpha = .05; c.strokeStyle = '#fff'; c.lineWidth = 2; for (var i = -H; i < W; i += 46) { c.beginPath(); c.moveTo(i, H); c.lineTo(i + H, 0); c.stroke(); } c.restore();
    c.fillStyle = '#3A963E'; c.fillRect(0, 0, W, 12);
    if (logo.complete && logo.naturalWidth) { c.save(); c.beginPath(); c.arc(104, 104, 44, 0, 7); c.fillStyle = '#fff'; c.fill(); c.clip(); c.drawImage(logo, 60, 60, 88, 88); c.restore(); }
    c.textAlign = 'left'; c.fillStyle = '#76C46E'; c.font = '700 22px Barlow'; c.fillText('ENERGÍAS LATAM', 168, 98);
    c.fillStyle = '#9FB3C8'; c.font = '600 20px Barlow'; c.fillText('LA ESTACIÓN DEL FUTURO', 168, 126);
  }
  function pie(c, W, H, txt) {
    c.fillStyle = '#D52B1E'; c.fillRect(0, 1262, W, 6); c.fillStyle = '#fff'; c.fillRect(0, 1268, W, 6); c.fillStyle = '#0038A8'; c.fillRect(0, 1274, W, 6);
    c.textAlign = 'left'; c.fillStyle = '#fff'; c.font = '400 40px "Bebas Neue"'; c.fillText('ENERGIASLATAM.COM', 60, 1326);
    c.textAlign = 'right'; c.fillStyle = '#9FB3C8'; c.font = '600 18px Barlow'; c.fillText(txt, 1020, 1320); c.textAlign = 'left';
  }
  function logoTile(c, n, x, y, w, h) {
    rr(c, x, y, w, h, 10); c.fillStyle = n === 'Energy' ? '#0F213D' : '#fff'; c.fill();
    var im = logoDe(n);
    if (im && (im.tagName === 'CANVAS' || (im.complete && im.naturalWidth))) { var sc = Math.min((w - 14) / im.naturalWidth, (h - 12) / im.naturalHeight), iw = im.naturalWidth * sc, ih = im.naturalHeight * sc; c.drawImage(im, x + (w - iw) / 2, y + (h - ih) / 2, iw, ih); }
    else { c.textAlign = 'center'; c.fillStyle = colorDe(n); c.font = '400 26px "Bebas Neue"'; c.fillText(n.toUpperCase().slice(0, 9), x + w / 2, y + h / 2 + 9); c.textAlign = 'left'; }
  }

  /* ---------- QUIÉN CRECIÓ ---------- */
  var QC = { modo: 'mes', mes: null };
  function crecio() {
    if (!QC.mes) return;
    var k = QC.mes.split('-'), y = +k[0], m = +k[1], j = D[y], jp = D[y - 1]; if (!j || !jp) { $('qcNota').textContent = 'Para comparar hace falta el año anterior.'; return; }
    var cur = {}, prev = {};
    if (QC.modo === 'mes') { cur = agg(j, 'vp', m, 'all', 'all'); prev = agg(jp, 'vp', m, 'all', 'all'); }
    else { for (var i = 1; i <= m; i++) { var a = agg(j, 'vp', i, 'all', 'all'), b = agg(jp, 'vp', i, 'all', 'all'), q; for (q in a) cur[q] = (cur[q] || 0) + a[q]; for (q in b) prev[q] = (prev[q] || 0) + b[q]; } }
    var tc = 0, tp = 0, q2; for (q2 in cur) tc += cur[q2]; for (q2 in prev) tp += prev[q2];
    var rows = Object.keys(cur).filter(function (n) { return prev[n] > 0 && cur[n] > tc * .008; }).map(function (n) { return { n: n, v: cur[n], p: prev[n], d: (cur[n] - prev[n]) / prev[n] }; }).sort(function (a, b) { return b.d - a.d; }).slice(0, 14);
    var cv = $('qcPlaca'), c = cv.getContext('2d'), W = 1080, H = 1350; fondo(c, W, H);
    c.fillStyle = '#fff'; c.font = '400 104px "Bebas Neue"'; c.fillText('¿QUIÉN CRECIÓ?', 60, 256);
    c.fillStyle = '#C9D6E3'; c.font = '700 26px Barlow';
    var per = QC.modo === 'mes' ? (MESES[m - 1] + ' ' + y + ' vs. ' + MESES[m - 1] + ' ' + (y - 1)) : ('Enero–' + MESES[m - 1] + ' ' + y + ' vs. mismo período ' + (y - 1));
    c.fillText(per.toUpperCase() + '  ·  PARAGUAY', 62, 304);
    var dm = (tc - tp) / tp; rr(c, 60, 326, 520, 58, 29); c.fillStyle = 'rgba(118,196,110,.16)'; c.fill();
    c.fillStyle = '#9FB3C8'; c.font = '700 18px Barlow'; c.fillText('MERCADO', 86, 362); c.fillStyle = dm >= 0 ? '#8FD786' : '#FF8A80'; c.font = '400 40px "Bebas Neue"'; c.fillText((dm >= 0 ? '▲ ' : '▼ ') + p1(Math.abs(dm)) + '  ·  ' + fmtM(tc) + ' M DE LITROS', 190, 369);
    var top = 418, rh = Math.min(58, (1236 - top) / Math.max(rows.length, 1)), cx = 650, mx = 0; rows.forEach(function (r) { mx = Math.max(mx, Math.abs(r.d)); }); mx = mx || 1;
    c.strokeStyle = 'rgba(255,255,255,.25)'; c.lineWidth = 2; c.beginPath(); c.moveTo(cx, top - 6); c.lineTo(cx, top + rh * rows.length); c.stroke();
    rows.forEach(function (r, i) {
      var yy = top + i * rh, cy = yy + rh / 2, bh = Math.min(30, rh * .55), w = Math.max(4, 300 * Math.abs(r.d) / mx);
      logoTile(c, r.n, 60, cy - rh * .42, 132, rh * .84);
      c.fillStyle = '#fff'; c.font = '600 24px Barlow'; var nm = r.n; while (c.measureText(nm).width > 170 && nm.length > 3) nm = nm.slice(0, -2) + '…'; c.fillText(nm, 208, cy + 8);
      var up = r.d >= 0, gx = up ? cx : cx - w, gr = c.createLinearGradient(gx, 0, gx + w, 0);
      if (up) { gr.addColorStop(0, '#2E7D32'); gr.addColorStop(1, '#8FD786'); } else { gr.addColorStop(0, '#FF8A80'); gr.addColorStop(1, '#C0252D'); }
      rr(c, gx, cy - bh / 2, w, bh, bh / 2); c.fillStyle = gr; c.fill();
      c.font = '400 32px "Bebas Neue"'; c.fillStyle = up ? '#8FD786' : '#FF8A80';
      var t = (up ? '+' : '−') + p1(Math.abs(r.d)); if (up) { c.textAlign = 'left'; c.fillText(t, cx + w + 12, cy + 11); } else { c.textAlign = 'right'; c.fillText(t, cx - w - 12, cy + 11); }
      c.textAlign = 'left';
    });
    pie(c, W, H, 'Variación de litros vendidos por emblema · datos oficiales MIC');
    var best = rows[0], worst = rows[rows.length - 1];
    $('qcNota').innerHTML = best ? ('<b>' + best.n + '</b> fue el que más creció (' + p1(best.d) + ')' + (worst && worst.d < 0 ? '; <b>' + worst.n + '</b> el que más cayó (' + p1(worst.d) + ')' : '') + '. El mercado ' + (dm >= 0 ? 'subió ' : 'bajó ') + p1(Math.abs(dm)) + '.') : '';
  }

  /* ---------- PRECIOS ---------- */
  var PR = { prod: 'GTIII' };
  function precioRows(prod) {
    var P = X.precios; if (!P) return [];
    var ri = P.rows.indexOf(prod); if (ri < 0) return [];
    return P.cols.map(function (cd, ci) { return { n: EMB[cd] || cd, v: P.data[ri][ci] }; }).filter(function (r) { return r.v > 0; }).sort(function (a, b) { return a.v - b.v; });
  }
  function precios() {
    var P = X.precios; if (!P) { $('prBox').innerHTML = '<p class="note">Precios no disponibles en este momento.</p>'; return; }
    $('prChips').innerHTML = P.rows.map(function (r) { return '<button class="chip' + (r === PR.prod ? ' on' : '') + '" data-v="' + r + '">' + (PROD[r] || r) + '</button>'; }).join('');
    var rows = precioRows(PR.prod), avg = rows.reduce(function (s, r) { return s + r.v; }, 0) / (rows.length || 1);
    var cv = $('prPlaca'), c = cv.getContext('2d'), W = 1080, H = 1350; fondo(c, W, H);
    c.fillStyle = '#fff'; c.font = '400 92px "Bebas Neue"'; c.fillText('¿DÓNDE CARGAR', 60, 240); c.fillStyle = '#76C46E'; c.fillText('MÁS BARATO?', 60, 328);
    var hoy = X.precios_hist && Object.keys(X.precios_hist).length ? X.precios_hist[Object.keys(X.precios_hist).pop()].f : '';
    c.fillStyle = '#C9D6E3'; c.font = '700 26px Barlow'; c.fillText(((PROD[PR.prod] || PR.prod) + '  ·  GUARANÍES POR LITRO  ·  PARAGUAY').toUpperCase(), 62, 376);
    var top = 412, rh = Math.min(56, (1236 - top) / Math.max(rows.length, 1)), mn = rows.length ? rows[0].v : 0, mxv = rows.length ? rows[rows.length - 1].v : 1, base = mn * .9, bx = 360, bw = 520;
    rows.forEach(function (r, i) {
      var cy = top + i * rh + rh / 2, bh = Math.min(28, rh * .55), w = Math.max(10, bw * (r.v - base) / (mxv - base || 1)), col = colorDe(r.n);
      logoTile(c, r.n, 60, cy - rh * .42, 132, rh * .84);
      c.fillStyle = '#fff'; c.font = '600 22px Barlow'; var nm = r.n; while (c.measureText(nm).width > 140 && nm.length > 3) nm = nm.slice(0, -2) + '…'; c.fillText(nm, 206, cy + 8);
      rr(c, bx, cy - bh / 2, bw, bh, bh / 2); c.fillStyle = 'rgba(255,255,255,.06)'; c.fill();
      var gr = c.createLinearGradient(bx, 0, bx + w, 0); gr.addColorStop(0, sh(col, -.25)); gr.addColorStop(1, col); rr(c, bx, cy - bh / 2, w, bh, bh / 2); c.fillStyle = gr; c.fill();
      c.textAlign = 'right'; c.fillStyle = r.v === mn ? '#8FD786' : '#fff'; c.font = '400 34px "Bebas Neue"'; c.fillText(n0(r.v), 1020, cy + 12); c.textAlign = 'left';
      if (r.v === mn) { c.fillStyle = '#8FD786'; c.font = '700 16px Barlow'; c.fillText('MÁS BARATO', bx + w + 10, cy + 6); }
    });
    pie(c, W, H, 'Precio promedio informado' + (hoy ? ' al ' + hoy.split('-').reverse().join('/') : '') + ' · datos oficiales MIC');
    // tabla completa
    var h = '<table class="mx"><thead><tr><th>Emblema</th>' + P.rows.map(function (r) { return '<th>' + (PROD[r] || r) + '</th>'; }).join('') + '</tr></thead><tbody>';
    var mins = P.rows.map(function (r, i) { var v = P.data[i].filter(function (x) { return x > 0; }); return v.length ? Math.min.apply(null, v) : 0; });
    var maxs = P.rows.map(function (r, i) { var v = P.data[i].filter(function (x) { return x > 0; }); return v.length ? Math.max.apply(null, v) : 0; });
    var ord = P.cols.map(function (cd, ci) { return { cd: cd, ci: ci, n: EMB[cd] || cd }; }).sort(function (a, b) { return a.n.localeCompare(b.n); });
    ord.forEach(function (o) { h += '<tr><td>' + lg(o.n) + o.n + '</td>' + P.rows.map(function (r, i) { var v = P.data[i][o.ci]; return '<td class="' + (v && v === mins[i] ? 'min' : v && v === maxs[i] ? 'max' : '') + '">' + (v ? n0(v) : '–') + '</td>'; }).join('') + '</tr>'; });
    $('prTabla').innerHTML = h + '</tbody></table>';
    $('prNota').innerHTML = rows.length ? ('<b>' + rows[0].n + '</b> tiene el ' + (PROD[PR.prod] || PR.prod).toLowerCase() + ' más barato (' + gs(rows[0].v) + ' por litro) y <b>' + rows[rows.length - 1].n + '</b> el más caro (' + gs(rows[rows.length - 1].v) + '). Diferencia: ' + gs(rows[rows.length - 1].v - rows[0].v) + ' por litro; en un tanque de 50 litros son ' + gs(50 * (rows[rows.length - 1].v - rows[0].v)) + '. Promedio: ' + gs(avg) + '.') : '';
  }

  /* ---------- RED DE ESTACIONES ---------- */
  var RE = { vista: 'cant', emb: '', dep: '' };
  function estaciones() {
    var E = X.estaciones; if (!E || !E.length) return;
    var porEmb = {}, porDep = {}, tot = 0;
    E.forEach(function (r) { var n = nomD(r[0]); porEmb[n] = (porEmb[n] || 0) + r[2]; tot += r[2]; if (!RE.emb || RE.emb === n) porDep[r[1]] = (porDep[r[1]] || 0) + r[2]; });
    // litros por estación del último mes
    var lm = lastMonth(D[Y]), vol = agg(D[Y], 'vp', lm, 'all', 'all');
    var rows = Object.keys(porEmb).map(function (n) { return { n: n, e: porEmb[n], l: vol[n] ? vol[n] / porEmb[n] : 0 }; });
    var key = RE.vista === 'cant' ? 'e' : 'l'; rows = rows.filter(function (r) { return r[key] > 0; }).sort(function (a, b) { return b[key] - a[key]; });
    var mx = rows.length ? rows[0][key] : 1;
    $('reTot').textContent = n0(tot);
    $('reLista').innerHTML = rows.map(function (r, i) {
      return '<li class="' + (RE.emb === r.n ? 'on' : '') + '" data-n="' + r.n + '"><span class="rk">' + (i + 1) + '</span>' + lg(r.n) + '<span class="nm">' + r.n + '</span><span class="br"><i style="width:' + (100 * r[key] / mx).toFixed(1) + '%;background:' + colorDe(r.n) + '"></i></span><span class="vl">' + (key === 'e' ? n0(r.e) : n0(r.l / 1000) + ' mil L') + '</span></li>';
    }).join('');
    $('reNota').textContent = RE.vista === 'cant' ? 'Estaciones de servicio y puestos de carga habilitados por emblema. Tocá un emblema para ver dónde están sus estaciones.' : 'Litros vendidos en ' + MESES[lm - 1].toLowerCase() + ' divididos por la cantidad de estaciones de cada emblema: cuánto vende, en promedio, cada estación.';
    // mapa
    if (!MAPA) return;
    var mxd = 0, d; for (d in porDep) mxd = Math.max(mxd, porDep[d]);
    var s = '<svg viewBox="0 0 ' + MAPA.w + ' ' + MAPA.h + '" role="img" aria-label="Mapa de estaciones por departamento">';
    var col = RE.emb ? colorDe(RE.emb) : '#2E7D32';
    for (d in MAPA.dep) { var v = porDep[d] || 0, a = mxd ? .12 + .88 * Math.sqrt(v / mxd) : 0; s += '<path d="' + MAPA.dep[d].d + '" data-d="' + d + '" fill="' + col + '" fill-opacity="' + (v ? a.toFixed(2) : .04) + '" stroke="#fff" stroke-width="1.5" class="' + (RE.dep === d ? 'sel' : '') + '"/>'; }
    for (d in MAPA.dep) { if (d === '00' || d === '11') continue; var cc = MAPA.dep[d].c; s += '<text x="' + cc[0] + '" y="' + cc[1] + '" text-anchor="middle" font-size="15" font-weight="700" fill="#0F213D" pointer-events="none">' + n0(porDep[d] || 0) + '</text>'; }
    var ct = MAPA.dep['11'].c; s += '<text x="' + (ct[0] + 70) + '" y="' + (ct[1] + 40) + '" font-size="14" font-weight="700" fill="#0F213D" pointer-events="none">Central ' + n0(porDep['11'] || 0) + ' · Asunción ' + n0(porDep['00'] || 0) + '</text>';
    s += '</svg>';
    $('reMapa').innerHTML = s + '<div class="tip" id="reTip"></div><p class="lgnd">' + (RE.emb ? 'Estaciones de <b>' + RE.emb + '</b> por departamento · <a href="#" id="reAll">ver todas</a>' : 'Estaciones de todos los emblemas por departamento') + '</p>';
    var svg = $('reMapa').querySelector('svg'), tip = $('reTip');
    svg.addEventListener('mousemove', function (e) {
      var p = e.target.closest('path'); if (!p) { tip.style.opacity = 0; return; }
      var dd = p.dataset.d, r = $('reMapa').getBoundingClientRect(), lst = {};
      E.forEach(function (x) { if (x[1] === dd) { var n = nomD(x[0]); lst[n] = (lst[n] || 0) + x[2]; } });
      var top3 = Object.keys(lst).sort(function (a, b) { return lst[b] - lst[a]; }).slice(0, 4).map(function (n) { return n + ': ' + lst[n]; }).join('<br>');
      tip.innerHTML = '<b>' + DEPN[dd] + '</b> · ' + n0(porDep[dd] || 0) + ' estaciones<br>' + top3; tip.style.opacity = 1;
      tip.style.left = Math.min(r.width - 190, e.clientX - r.left + 14) + 'px'; tip.style.top = (e.clientY - r.top + 14) + 'px';
    });
    svg.addEventListener('mouseleave', function () { tip.style.opacity = 0; });
    var al = $('reAll'); if (al) al.onclick = function (e) { e.preventDefault(); RE.emb = ''; estaciones(); };
  }

  /* ---------- GLP ---------- */
  function glp() {
    var G = X.glp; if (!G || !G.length) return;
    var y = 0, m = 0; G.forEach(function (r) { if (r[0] * 12 + r[1] > y * 12 + m) { y = r[0]; m = r[1]; } });
    var por = {}, tot = 0, DST = { VES: 'Estaciones', VBR: 'Garrafas', VIN: 'Industrias' }, CD = { VES: '#3FA9F5', VBR: '#F5B82E', VIN: '#9AA8B6' };
    var prevT = 0; G.forEach(function (r) { if (r[0] === y - 1 && r[1] === m) prevT += r[4]; if (r[0] !== y || r[1] !== m) return; var n = nomD(r[2]); por[n] = por[n] || { t: 0 }; por[n][r[3]] = (por[n][r[3]] || 0) + r[4]; por[n].t += r[4]; tot += r[4]; });
    var rows = Object.keys(por).map(function (n) { return { n: n, o: por[n] }; }).sort(function (a, b) { return b.o.t - a.o.t; }).slice(0, 12), mx = rows.length ? rows[0].o.t : 1;
    $('glpMes').textContent = MESES[m - 1] + ' ' + y; $('glpTot').textContent = n0(tot / 1e6) + ' mil toneladas';
    $('glpVar').textContent = prevT ? ((tot >= prevT ? '▲ ' : '▼ ') + p1(Math.abs((tot - prevT) / prevT)) + ' vs. ' + MESES[m - 1].toLowerCase() + ' ' + (y - 1)) : '';
    $('glpLista').innerHTML = rows.map(function (r, i) {
      return '<li><span class="rk">' + (i + 1) + '</span><span class="nm">' + r.n + '</span><span class="br st">' + ['VBR', 'VES', 'VIN'].map(function (k) { return r.o[k] ? '<i title="' + DST[k] + ': ' + n0(r.o[k] / 1000) + ' t" style="width:' + (100 * r.o[k] / mx).toFixed(2) + '%;background:' + CD[k] + '"></i>' : ''; }).join('') + '</span><span class="vl">' + n0(r.o.t / 1000) + ' t</span></li>';
    }).join('');
    $('glpLeyenda').innerHTML = ['VBR', 'VES', 'VIN'].map(function (k) { return '<span><i style="background:' + CD[k] + '"></i>' + DST[k] + '</span>'; }).join('');
    // precios garrafa
    var GP = X.glp_precios;
    if (GP) {
      var ri = GP.rows.indexOf('GR10'), r13 = GP.rows.indexOf('GR13'), re = GP.rows.indexOf('GES');
      var pr = GP.cols.map(function (cd, ci) { return { n: EMB[cd] || cd, g10: ri >= 0 ? GP.data[ri][ci] : 0, g13: r13 >= 0 ? GP.data[r13][ci] : 0, es: re >= 0 ? GP.data[re][ci] : 0 }; }).filter(function (x) { return x.g10 || x.g13 || x.es; }).sort(function (a, b) { return (a.g10 || 9e9) - (b.g10 || 9e9); });
      var m10 = Math.min.apply(null, pr.map(function (x) { return x.g10 || 9e9; })), m13 = Math.min.apply(null, pr.map(function (x) { return x.g13 || 9e9; })), me = Math.min.apply(null, pr.map(function (x) { return x.es || 9e9; }));
      $('glpPrecios').innerHTML = '<table class="mx"><thead><tr><th>Empresa</th><th>Garrafa 10 kg</th><th>Garrafa 13 kg</th><th>En estaciones (Gs/L)</th></tr></thead><tbody>' + pr.map(function (x) { return '<tr><td>' + x.n + '</td><td class="' + (x.g10 === m10 ? 'min' : '') + '">' + (x.g10 ? n0(x.g10) : '–') + '</td><td class="' + (x.g13 === m13 ? 'min' : '') + '">' + (x.g13 ? n0(x.g13) : '–') + '</td><td class="' + (x.es === me ? 'min' : '') + '">' + (x.es ? n0(x.es) : '–') + '</td></tr>'; }).join('') + '</tbody></table>';
    }
    // origen importaciones GLP (año en curso)
    var I = X.glp_import || [], o = {}, it = 0; I.forEach(function (r) { o[r[1]] = (o[r[1]] || 0) + r[2]; it += r[2]; });
    var orr = Object.keys(o).sort(function (a, b) { return o[b] - o[a]; }), om = orr.length ? o[orr[0]] : 1, im2 = 0; I.forEach(function (r) { if (r[0] > im2) im2 = r[0]; });
    $('glpOrigen').innerHTML = orr.length ? ('<p class="sub">Importaciones de GLP de enero a ' + MESES[im2 - 1].toLowerCase() + ': ' + n0(it / 1e6) + ' mil toneladas</p><ul class="bars">' + orr.map(function (k) { return '<li><span class="nm">' + (X.paises[k] || k) + '</span><span class="br"><i style="width:' + (100 * o[k] / om).toFixed(1) + '%;background:#2E7D32"></i></span><span class="vl">' + p1(o[k] / it) + '</span></li>'; }).join('') + '</ul>') : '';
  }

  /* ---------- arranque ---------- */
  function listo() {
    // meses para quién creció
    var s = $('qcMes'), op = []; [Y].forEach(function (y) { var j = D[y]; if (!j) return; for (var m = lastMonth(j); m >= 1; m--) op.push('<option value="' + y + '-' + m + '">' + MESES[m - 1] + ' ' + y + '</option>'); });
    s.innerHTML = op.join(''); QC.mes = s.value; crecio(); estaciones(); precios(); glp();
  }
  window.EXTRA_INIT = function () {
    Promise.all([
      fetch('/mic-extra.php').then(function (r) { return r.json(); }).catch(function () { return null; }),
      fetch('/img/py-mapa.json').then(function (r) { return r.json(); }).catch(function () { return null; })
    ]).then(function (a) { X = a[0]; MAPA = a[1]; if (!X) return; listo(); });
  };
  window.EXTRA_REDRAW = function () { if (X) { crecio(); precios(); } };
  $('qcMes').onchange = function () { QC.mes = this.value; crecio(); };
  seg2('qcModo', function (v) { QC.modo = v; crecio(); });
  $('qcDesc').onclick = function () { descargar($('qcPlaca'), 'quien-crecio-' + QC.mes + '.png'); };
  $('prChips').addEventListener('click', function (e) { var b = e.target.closest('.chip'); if (!b) return; PR.prod = b.dataset.v; precios(); });
  $('prDesc').onclick = function () { descargar($('prPlaca'), 'precios-' + PR.prod.toLowerCase() + '.png'); };
  seg2('reVista', function (v) { RE.vista = v; estaciones(); });
  $('reLista').addEventListener('click', function (e) { var li = e.target.closest('li'); if (!li) return; RE.emb = RE.emb === li.dataset.n ? '' : li.dataset.n; estaciones(); });
})();
