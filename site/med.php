<?php
/* Medidor propio del sitio · energiaslatam.com
   POST /med.php  (lo envía adtrack.js con sendBeacon)
     t   = visto | click | pv | link | lee
     an  = anunciante o destino · ni = nivel · ub = ubicación/texto · po = posición
     pg  = página (ruta) · nid = id de nota · vid = visitante anónimo · src = de dónde viene
   GET  /med.php[?desde=AAAA-MM-DD&hasta=AAAA-MM-DD&an=...]  → tablero privado con contraseña (panel-auth.php; recuperación por mail a info@energiaslatam.com)
   No guarda IP, nombres ni mails. El visitante es un número al azar del navegador. Robots y vistas previas no se registran. */
date_default_timezone_set('America/Asuncion');
$dir = __DIR__ . '/datos';
if (!is_dir($dir)) { @mkdir($dir, 0750); @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }

function limpio($s, $n = 80) { $s = preg_replace('/[\x00-\x1F",;]+/u', ' ', (string)$s); return mb_substr(trim($s), 0, $n); }

// ---------- registro ----------
if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST' && !isset($_POST['acc'])) {
  header('Cache-Control: no-store');
  $ua = (string)($_SERVER['HTTP_USER_AGENT'] ?? '');
  if ($ua === '' || preg_match('/bot|crawl|spider|slurp|preview|facebookexternalhit|facebot|whatsapp|telegram|skype|slack|discord|linkedin|twitter|curl|wget|python|headless|monitor|lighthouse/i', $ua)) { http_response_code(204); exit; }
  $ref = (string)($_SERVER['HTTP_ORIGIN'] ?? $_SERVER['HTTP_REFERER'] ?? '');
  if ($ref !== '' && !preg_match('#^https?://(www\.)?energiaslatam\.com#i', $ref)) { http_response_code(204); exit; }
  $raw = file_get_contents('php://input', false, null, 0, 4000);
  $p = json_decode($raw, true); if (!is_array($p)) $p = $_POST;
  $t = in_array($p['t'] ?? '', ['visto', 'click', 'pv', 'link', 'lee'], true) ? $p['t'] : '';
  if ($t === '') { http_response_code(204); exit; }
  $dv = preg_match('/iphone|android.+mobile|mobile/i', $ua) ? 'celular' : (preg_match('/ipad|tablet|android/i', $ua) ? 'tablet' : 'compu');
  $fila = [date('Y-m-d H:i:s'), $t, limpio($p['an'] ?? '', 120), limpio($p['ni'] ?? '', 20), limpio($p['ub'] ?? '', 40), limpio($p['po'] ?? '', 40), limpio($p['pg'] ?? '', 120), limpio($p['nid'] ?? '', 80), $dv, preg_replace('/[^a-z0-9]/i', '', substr((string)($p['vid'] ?? ''), 0, 20)), limpio($p['src'] ?? '', 50)];
  @file_put_contents($dir . '/med-' . date('Y-m') . '.csv', implode(',', $fila) . "\n", FILE_APPEND | LOCK_EX);
  http_response_code(204); exit;
}

// ---------- tablero ----------
require __DIR__ . '/panel-auth.php';
panel_requiere('Medidor del sitio');
header('Content-Type: text/html; charset=utf-8'); header('Cache-Control: no-store'); header('X-Robots-Tag: noindex');

// títulos de las notas (copia local de notas.json, se renueva cada hora)
$tit = [];
$cf = $dir . '/notas-cache.json';
if (!is_file($cf) || filemtime($cf) < time() - 3600) { $j = @file_get_contents('https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/notas.json', false, stream_context_create(['http' => ['timeout' => 5]])); if ($j && json_decode($j)) @file_put_contents($cf, $j); }
foreach ((json_decode((string)@file_get_contents($cf), true) ?: []) as $nn) if (!empty($nn['id'])) $tit[$nn['id']] = $nn['titulo'] ?? $nn['id'];

$re = '/^\d{4}-\d{2}-\d{2}$/';
$hoy = date('Y-m-d');
$desde = preg_match($re, $_GET['desde'] ?? '') ? $_GET['desde'] : date('Y-m-d', strtotime('-13 days'));
$hasta = preg_match($re, $_GET['hasta'] ?? '') ? $_GET['hasta'] : $hoy;
$filtroAn = limpio($_GET['an'] ?? '', 120);

$A = []; $AU = []; $P = []; $D = []; $DV = []; $L = []; $LG = []; $NV = []; $NL = []; $SRC = []; $VIS = []; $VISD = []; $VHOY = [];
$tot = ['visto' => 0, 'click' => 0, 'pv' => 0, 'link' => 0, 'lee' => 0];
foreach (glob($dir . '/med-*.csv') as $f) {
  $m = substr(basename($f), 4, 7); if ($m < substr($desde, 0, 7) || $m > substr($hasta, 0, 7)) continue;
  foreach (file($f, FILE_IGNORE_NEW_LINES) as $l) {
    $c = explode(',', $l); if (count($c) < 9) continue;
    $dia = substr($c[0], 0, 10); if ($dia < $desde || $dia > $hasta) continue;
    [$ts, $t, $an, $ni, $ub, $po, $pg, $nid, $dv] = $c; $vid = $c[9] ?? ''; $src = $c[10] ?? '';
    if (!isset($D[$dia])) $D[$dia] = [];
    if ($t === 'pv') {
      if ($filtroAn !== '') continue;
      $tot['pv']++; $k = $nid !== '' ? '/n/' . $nid : ($pg ?: '/');
      $P[$k] = ($P[$k] ?? 0) + 1; $D[$dia]['pv'] = ($D[$dia]['pv'] ?? 0) + 1;
      if ($nid !== '') $NV[$nid] = ($NV[$nid] ?? 0) + 1;
      if ($vid === '') continue; $vk = $vid; // filas viejas sin visitante: cuentan como página vista, no como visitante
      $VIS[$vk] = 1; $VISD[$dia][$vk] = 1; if ($dia === $hoy) $VHOY[$vk] = 1;
      if (!isset($DV[$dv])) $DV[$dv] = []; $DV[$dv][$vk] = 1;
      if ($src !== '') { $s2 = strpos($src, 'otro: ') === 0 ? 'otros sitios' : $src; if (!isset($SRC[$s2])) $SRC[$s2] = []; $SRC[$s2][$vk] = 1; }
      continue;
    }
    if ($t === 'lee') { if ($filtroAn !== '') continue; $tot['lee']++; $NL[$nid] = ($NL[$nid] ?? 0) + 1; $D[$dia]['lee'] = ($D[$dia]['lee'] ?? 0) + 1; continue; }
    if ($t === 'link') {
      if ($filtroAn !== '') continue;
      $tot['link']++; $L[$an] = ($L[$an] ?? 0) + 1;
      $grp = strpos($an, ':') !== false ? trim(substr($an, 0, strpos($an, ':'))) : $an; $LG[$grp] = ($LG[$grp] ?? 0) + 1;
      $D[$dia]['link'] = ($D[$dia]['link'] ?? 0) + 1; continue;
    }
    if ($filtroAn !== '' && $an !== $filtroAn) continue;
    $tot[$t]++;
    $ka = $an ?: '(sin nombre)';
    $A[$ka]['ni'] = $ni; $A[$ka][$t] = ($A[$ka][$t] ?? 0) + 1;
    $ku = $ka . ' · ' . ($ub ?: '-') . ($po ? ' · ' . $po : '');
    $AU[$ku][$t] = ($AU[$ku][$t] ?? 0) + 1;
    $D[$dia][$t] = ($D[$dia][$t] ?? 0) + 1;
  }
}
for ($d = $desde; $d <= $hasta; $d = date('Y-m-d', strtotime($d . ' +1 day'))) { if (!isset($D[$d])) $D[$d] = []; if (count($D) > 400) break; }
ksort($D);
// días anteriores al medidor de visitantes: datos diarios de Google Analytics (datos/historico.json)
$HV = []; $HIST = json_decode((string)@file_get_contents($dir . '/historico.json'), true) ?: [];
if ($filtroAn === '') foreach (($HIST['dias'] ?? []) as $dia => $r) {
  if ($dia < $desde || $dia > $hasta) continue;
  $tot['pv'] += (int)($r['pv'] ?? 0) - (int)($D[$dia]['pv'] ?? 0); $D[$dia]['pv'] = (int)($r['pv'] ?? 0);
  $HV[$dia] = (int)($r['vis'] ?? 0); unset($VISD[$dia]);
}

$h = function ($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); };
$pct = function ($c, $v) { return $v ? number_format(100 * $c / $v, 1, ',', '.') . ' %' : '–'; };
$n = function ($x) { return number_format((int)$x, 0, ',', '.'); };
$RK = ['sponsor' => 0, 'oro' => 1, 'plata' => 2, 'bronce' => 3];
uasort($A, function ($a, $b) use ($RK) { return [($RK[$a['ni'] ?? ''] ?? 9), -($a['visto'] ?? 0)] <=> [($RK[$b['ni'] ?? ''] ?? 9), -($b['visto'] ?? 0)]; });
uasort($AU, function ($a, $b) { return ($b['visto'] ?? 0) <=> ($a['visto'] ?? 0); });
arsort($P); arsort($L); arsort($LG); arsort($NV);
$SRCc = array_map('count', $SRC); arsort($SRCc);
$DVc = array_map('count', $DV); arsort($DVc);
$nVis = count($VIS);
$VM = []; foreach ($VISD as $vv) $VM += $vv; $nVisK = $HV ? count($VM) + array_sum($HV) : $nVis; // con días de Analytics se suman los visitantes de cada día
$vHoy = isset($HV[$hoy]) ? $HV[$hoy] : count($VHOY);

function grafico($D, $serie, $color, $titulo, $VISD = null) {
  global $HV;
  $vals = []; foreach ($D as $dia => $r) $vals[$dia] = $serie === 'vis' ? (isset($HV[$dia]) ? $HV[$dia] : count($VISD[$dia] ?? [])) : ($r[$serie] ?? 0);
  $max = max(1, max($vals ?: [1])); $n = count($vals); $W = 860; $H = 240; $pl = 44; $pb = 38; $bw = $n ? ($W - $pl - 10) / $n : 10;
  $o = '<svg viewBox="0 0 ' . $W . ' ' . $H . '" width="100%" role="img" aria-label="' . htmlspecialchars($titulo) . '" style="display:block;background:#fff">';
  for ($g = 0; $g <= 4; $g++) { $y = 28 + ($H - $pb - 28) * $g / 4; $v = round($max * (4 - $g) / 4); $o .= '<line x1="' . $pl . '" x2="' . ($W - 6) . '" y1="' . $y . '" y2="' . $y . '" stroke="#E3E9F0"/><text x="' . ($pl - 6) . '" y="' . ($y + 6) . '" font-size="17" text-anchor="end" fill="#8A99A8">' . $v . '</text>'; }
  $i = 0;
  foreach ($vals as $dia => $v) {
    $bh = ($H - $pb - 28) * $v / $max; $x = $pl + $i * $bw + 2; $y = $H - $pb - $bh;
    $o .= '<rect x="' . round($x, 1) . '" y="' . round($y, 1) . '" width="' . max(1, round($bw - 4, 1)) . '" height="' . round($bh, 1) . '" fill="' . $color . '"' . (isset($HV[$dia]) && in_array($serie, ['vis', 'pv'], true) ? ' fill-opacity=".55"' : '') . ' rx="2"><title>' . $dia . ': ' . $v . '</title></rect>';
    if ($v > 0 && $bw > 30) $o .= '<text x="' . round($x + ($bw - 4) / 2, 1) . '" y="' . round($y - 4, 1) . '" font-size="17" text-anchor="middle" fill="#0F213D">' . $v . '</text>';
    if ($n <= 10 || $i % ceil($n / 8) === 0) $o .= '<text x="' . round($x + ($bw - 4) / 2, 1) . '" y="' . ($H - 12) . '" font-size="17" text-anchor="middle" fill="#4A5B6C">' . substr($dia, 8, 2) . '/' . substr($dia, 5, 2) . '</text>';
    $i++;
  }
  return $o . '</svg>';
}

$qs = function ($extra = []) use ($desde, $hasta) { return '?' . http_build_query(array_merge(['desde' => $desde, 'hasta' => $hasta], $extra)); };
$rq = function ($d1, $d2) { return '?' . http_build_query(['desde' => $d1, 'hasta' => $d2]); };
echo '<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Medidor del sitio</title><style>
body{font:15px Arial,sans-serif;max-width:920px;margin:20px auto;padding:0 14px;color:#0F213D;background:#fff}
h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:28px 0 8px;border-bottom:2px solid #3A963E;padding-bottom:4px}
.sub{color:#4A5B6C;font-size:13px;margin:0 0 14px}form{display:flex;flex-wrap:wrap;gap:8px;align-items:end;background:#F4F6F9;padding:10px;border-radius:8px}
label{font-size:12px;color:#4A5B6C;display:flex;flex-direction:column;gap:2px}input,select{font:14px Arial;padding:6px;border:1px solid #C9D3DE;border-radius:6px;max-width:100%}
button{font:bold 14px Arial;padding:8px 14px;border:0;border-radius:6px;background:#3A963E;color:#fff}.rap a{display:inline-block;margin:6px 8px 0 0;font-size:13px}
.k{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:14px 0}.k div{background:#F4F6F9;border-left:4px solid #3A963E;padding:10px;border-radius:6px}.k b{display:block;font-size:24px}.k span{font-size:12px;color:#4A5B6C}
.k.ad div{border-left-color:#B8901A}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:6px 8px;border-bottom:1px solid #E3E9F0;text-align:right}th:first-child,td:first-child{text-align:left}th{background:#F4F6F9;font-size:12px;text-transform:uppercase;letter-spacing:.5px}
.wrap{overflow-x:auto}.g{border:1px solid #E3E9F0;border-radius:8px;padding:8px;margin:8px 0}.leg{font-size:12px;color:#4A5B6C;margin:0 0 4px}
@media(max-width:640px){.k{grid-template-columns:1fr 1fr}}a{color:#0F213D}
</style><div style="float:right;margin:4px 0;font-size:13px;display:flex;gap:10px;align-items:center"><form method="post" style="all:unset"><input type="hidden" name="acc" value="olvide"><button style="all:unset;cursor:pointer;text-decoration:underline">Cambiar contraseña</button></form><a href="?salir=1">Salir</a></div><h1>Medidor del sitio</h1><p class="sub">Visitantes, notas leídas, páginas, publicidad y clics. Solo uso interno. Sin robots ni vistas previas. No guarda datos personales: cada visitante es un número al azar de su navegador.</p>';
echo '<form method="get"><label>Desde<input type="date" name="desde" value="' . $h($desde) . '"></label><label>Hasta<input type="date" name="hasta" value="' . $h($hasta) . '"></label><label>Anunciante<select name="an"><option value="">Todo el sitio</option>';
foreach (array_keys($A) as $an) echo '<option' . ($an === $filtroAn ? ' selected' : '') . '>' . $h($an) . '</option>';
if ($filtroAn !== '' && !isset($A[$filtroAn])) echo '<option selected>' . $h($filtroAn) . '</option>';
echo '</select></label><button>Ver</button></form>';
echo '<div class="rap"><a href="' . $h($rq($hoy, $hoy)) . '">Hoy</a><a href="' . $h($rq(date('Y-m-d', strtotime('-6 days')), $hoy)) . '">Últimos 7 días</a><a href="' . $h($rq(date('Y-m-d', strtotime('-29 days')), $hoy)) . '">Últimos 30 días</a><a href="' . $h($rq(date('Y-m-01'), $hoy)) . '">Este mes</a></div>';

if ($filtroAn === '') {
  echo '<h2>Visitantes y lectura</h2><div class="k"><div><b>' . $n($nVisK) . '</b><span>' . ($HV ? 'visitantes (suma de cada día)' : 'visitantes únicos en el período') . '</span></div><div><b>' . $n($vHoy) . '</b><span>visitantes hoy</span></div><div><b>' . $n($tot['pv']) . '</b><span>páginas vistas</span></div><div><b>' . $n($tot['lee']) . '</b><span>notas leídas (30 s o 60 % del texto)</span></div></div>';
  echo '<div class="g"><p class="leg">Visitantes únicos por día</p>' . grafico($D, 'vis', '#3A963E', 'Visitantes por día', $VISD) . '</div>';
  if ($HV) echo '<p class="sub">Barras más claras: días anteriores al medidor de visitantes, con datos diarios de Google Analytics (visitantes y páginas vistas). Notas leídas, origen y publicidad se miden desde el 1/11/2026 a la noche.</p>';
  echo '<div class="g"><p class="leg">Páginas vistas por día</p>' . grafico($D, 'pv', '#0F213D', 'Páginas vistas por día') . '</div>';
  echo '<div class="g"><p class="leg">Notas leídas por día</p>' . grafico($D, 'lee', '#C0252D', 'Notas leídas por día') . '</div>';

  // ---- Newsletter semanal (lista #4 de Brevo), copia local que se renueva cada 10 minutos ----
  $NLF = $dir . '/newsletter-cache.json'; $NLD = json_decode((string)@file_get_contents($NLF), true) ?: [];
  if (empty($NLD['ts']) || $NLD['ts'] < time() - 600) {
    $bk = trim((string)@file_get_contents($dir . '/brevo.key'));
    if ($bk !== '') {
      $bg = function ($u) use ($bk) { $c = stream_context_create(['http' => ['timeout' => 8, 'ignore_errors' => true, 'header' => "api-key: $bk\r\nAccept: application/json\r\n"]]); return json_decode((string)@file_get_contents('https://api.brevo.com/v3' . $u, false, $c), true); };
      $li = $bg('/contacts/lists/4');
      if (isset($li['totalSubscribers'])) {
        $altas = []; $off = 0;
        do { $cs = $bg('/contacts/lists/4/contacts?limit=500&offset=' . $off); $lote = $cs['contacts'] ?? []; foreach ($lote as $ct) if (empty($ct['emailBlacklisted'])) { $f = substr(date('Y-m-d', strtotime($ct['createdAt'] ?? 'now')), 0, 10); $altas[$f] = ($altas[$f] ?? 0) + 1; } $off += 500; } while (count($lote) === 500 && $off < 20000);
        $NLD = ['ts' => time(), 'total' => (int)$li['totalSubscribers'], 'bajas' => (int)($li['totalBlacklisted'] ?? 0), 'altas' => $altas];
        @file_put_contents($NLF, json_encode($NLD), LOCK_EX);
      }
    }
  }
  if (!empty($NLD['ts'])) {
    $act = max(0, $NLD['total'] - $NLD['bajas']); $nuevosP = 0; $nuevosH = $NLD['altas'][$hoy] ?? 0; $DN = [];
    foreach ($D as $dia => $r) { $v = $NLD['altas'][$dia] ?? 0; $DN[$dia] = ['nl' => $v]; $nuevosP += $v; }
    echo '<h2>Newsletter semanal</h2><div class="k"><div><b>' . $n($act) . '</b><span>inscriptos activos</span></div><div><b>' . $n($nuevosP) . '</b><span>nuevos en el período</span></div><div><b>' . $n($nuevosH) . '</b><span>nuevos hoy</span></div><div><b>' . $n($NLD['bajas']) . '</b><span>dados de baja</span></div></div>';
    echo '<div class="g"><p class="leg">Inscriptos nuevos por día</p>' . grafico($DN, 'nl', '#1F6FB2', 'Inscriptos nuevos por día') . '</div>';
    echo '<p class="sub">Lista "Newsletter" de Brevo, actualizada ' . date('d/m H:i', $NLD['ts']) . '. "Nuevos" cuenta la fecha en que cada contacto entró a Brevo.</p>';
  }

  echo '<h2>Notas más leídas</h2><div class="wrap"><table><tr><th>Nota</th><th>Vistas</th><th>Leídas</th><th>% que la leyó</th></tr>';
  $ids = array_unique(array_merge(array_keys($NV), array_keys($NL)));
  usort($ids, function ($a, $b) use ($NL, $NV) { return [($NL[$b] ?? 0), ($NV[$b] ?? 0)] <=> [($NL[$a] ?? 0), ($NV[$a] ?? 0)]; });
  foreach (array_slice($ids, 0, 40) as $id) echo '<tr><td><a href="https://energiaslatam.com/n/' . $h($id) . '" target="_blank">' . $h($tit[$id] ?? $id) . '</a></td><td>' . $n($NV[$id] ?? 0) . '</td><td>' . $n($NL[$id] ?? 0) . '</td><td>' . $pct(min($NL[$id] ?? 0, $NV[$id] ?? 0), $NV[$id] ?? 0) . '</td></tr>';
  if (!$ids) echo '<tr><td colspan="4">Todavía no hay datos en este período.</td></tr>';
  echo '</table></div>';

  echo '<h2>De dónde vienen</h2><div class="wrap"><table><tr><th>Origen</th><th>Visitantes</th><th>% del total</th></tr>';
  foreach ($SRCc as $s => $v) echo '<tr><td>' . $h($s) . '</td><td>' . $n($v) . '</td><td>' . $pct($v, $nVis) . '</td></tr>';
  if (!$SRCc) echo '<tr><td colspan="3">Todavía no hay datos (se mide desde el 1/11 a la noche).</td></tr>';
  echo '</table></div>';

  echo '<h2>Páginas más vistas</h2><div class="wrap"><table><tr><th>Página</th><th>Vistas</th></tr>';
  foreach (array_slice($P, 0, 30, true) as $pg => $v) { $nid = strpos($pg, '/n/') === 0 ? substr($pg, 3) : ''; echo '<tr><td>' . $h($nid !== '' ? ($tit[$nid] ?? $pg) : ($pg === '/' ? 'Portada' : $pg)) . '</td><td>' . $n($v) . '</td></tr>'; }
  echo '</table></div>';

  echo '<h2>Por dispositivo</h2><div class="wrap"><table><tr><th>Dispositivo</th><th>Visitantes</th><th>% del total</th></tr>';
  foreach ($DVc as $dv => $v) echo '<tr><td>' . $h($dv) . '</td><td>' . $n($v) . '</td><td>' . $pct($v, $nVis) . '</td></tr>';
  echo '</table></div>';
}

echo '<h2>Publicidad' . ($filtroAn !== '' ? ': ' . $h($filtroAn) : '') . '</h2><div class="k ad"><div><b>' . $n($tot['visto']) . '</b><span>vistas de avisos</span></div><div><b>' . $n($tot['click']) . '</b><span>clics en avisos</span></div><div><b>' . $pct($tot['click'], $tot['visto']) . '</b><span>porcentaje de clics</span></div><div><b>' . $n(count($A)) . '</b><span>anunciantes con vistas</span></div></div>';
echo '<div class="g"><p class="leg">Vistas de avisos por día</p>' . grafico($D, 'visto', '#B8901A', 'Vistas de avisos por día') . '</div>';
echo '<div class="wrap"><table><tr><th>Anunciante</th><th>Nivel</th><th>Vistas</th><th>Clics</th><th>% clics</th></tr>';
foreach ($A as $an => $r) echo '<tr><td><a href="' . $h($qs(['an' => $an])) . '">' . $h($an) . '</a></td><td>' . $h($r['ni'] ?? '') . '</td><td>' . $n($r['visto'] ?? 0) . '</td><td>' . $n($r['click'] ?? 0) . '</td><td>' . $pct($r['click'] ?? 0, $r['visto'] ?? 0) . '</td></tr>';
if (!$A) echo '<tr><td colspan="5">Todavía no hay datos en este período.</td></tr>';
echo '</table></div><h2>Publicidad por ubicación</h2><div class="wrap"><table><tr><th>Anunciante · página · posición</th><th>Vistas</th><th>Clics</th><th>% clics</th></tr>';
foreach (array_slice($AU, 0, 60, true) as $kk => $r) echo '<tr><td>' . $h($kk) . '</td><td>' . $n($r['visto'] ?? 0) . '</td><td>' . $n($r['click'] ?? 0) . '</td><td>' . $pct($r['click'] ?? 0, $r['visto'] ?? 0) . '</td></tr>';
echo '</table></div>';

if ($filtroAn === '') {
  echo '<h2>Clics en el sitio</h2><div class="wrap"><table><tr><th>Tipo</th><th>Clics</th></tr>';
  foreach ($LG as $g => $v) echo '<tr><td>' . $h($g) . '</td><td>' . $n($v) . '</td></tr>';
  if (!$LG) echo '<tr><td colspan="2">Todavía no hay datos en este período.</td></tr>';
  echo '</table></div><h2>Clics en el sitio · detalle</h2><div class="wrap"><table><tr><th>Destino</th><th>Clics</th></tr>';
  foreach (array_slice($L, 0, 50, true) as $g => $v) { $lab = strpos($g, 'Nota: ') === 0 && isset($tit[substr($g, 6)]) ? 'Nota: ' . $tit[substr($g, 6)] : $g; echo '<tr><td>' . $h($lab) . '</td><td>' . $n($v) . '</td></tr>'; }
  echo '</table></div>';
}

if ($filtroAn === '') {
  $IR = []; $IRR = 0;
  foreach ((is_file($dir . '/clics.csv') ? file($dir . '/clics.csv', FILE_IGNORE_NEW_LINES) : []) as $l) { $c = explode(',', $l); if (count($c) < 4) continue; $dia = substr($c[0], 0, 10); if ($dia < $desde || $dia > $hasta) continue; $kk = $c[1] . ' · ' . $c[2]; $IR[$kk] = ($IR[$kk] ?? 0) + 1; }
  foreach ((is_file($dir . '/robots.csv') ? file($dir . '/robots.csv', FILE_IGNORE_NEW_LINES) : []) as $l) { $dia = substr($l, 0, 10); if ($dia >= $desde && $dia <= $hasta) $IRR++; }
  arsort($IR);
  echo '<h2>Enlaces medidos (ir.php)</h2><div class="wrap"><table><tr><th>Destino · origen</th><th>Clics de personas</th></tr>';
  foreach ($IR as $kk => $v) echo '<tr><td>' . $h($kk) . '</td><td>' . $n($v) . '</td></tr>';
  if (!$IR) echo '<tr><td colspan="2">Sin clics en este período.</td></tr>';
  echo '</table></div><p class="sub">Robots y vistas previas de enlaces en el período (no suman): ' . $n($IRR) . '</p>';
}

echo '<h2>Por día</h2><div class="wrap"><table><tr><th>Día</th>' . ($filtroAn === '' ? '<th>Visitantes</th><th>Páginas vistas</th><th>Notas leídas</th>' : '') . '<th>Vistas de avisos</th><th>Clics en avisos</th>' . ($filtroAn === '' ? '<th>Clics en el sitio</th>' : '') . '</tr>';
foreach (array_reverse($D, true) as $dia => $r) echo '<tr><td>' . $h($dia) . '</td>' . ($filtroAn === '' ? '<td>' . $n(isset($HV[$dia]) ? $HV[$dia] : count($VISD[$dia] ?? [])) . '</td><td>' . $n($r['pv'] ?? 0) . '</td><td>' . $n($r['lee'] ?? 0) . '</td>' : '') . '<td>' . $n($r['visto'] ?? 0) . '</td><td>' . $n($r['click'] ?? 0) . '</td>' . ($filtroAn === '' ? '<td>' . $n($r['link'] ?? 0) . '</td>' : '') . '</tr>';
echo '</table></div><p class="sub" style="margin-top:20px">Energías LATAM · medidor propio, complementario a Google Analytics. Visitantes y origen se miden desde el 1/11/2026 a la noche.</p>';
