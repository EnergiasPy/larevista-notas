<?php
/* Medidor propio de publicidad y páginas · energiaslatam.com
   POST /med.php  (lo envía adtrack.js con sendBeacon)
     t   = visto | click | pv
     an  = anunciante · ni = nivel · ub = ubicación · po = posición · ni = nivel
     pg  = página (ruta) · nid = id de nota
   GET  /med.php?ver=<clave>[&desde=AAAA-MM-DD&hasta=AAAA-MM-DD]  → tablero privado (clave en datos/ir.key)
   No guarda IP ni datos personales: fecha, tipo, anunciante, ubicación, página y dispositivo.
   Robots y vistas previas no se registran. */
date_default_timezone_set('America/Asuncion');
$dir = __DIR__ . '/datos';
if (!is_dir($dir)) { @mkdir($dir, 0750); @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }

function limpio($s, $n = 80) { $s = preg_replace('/[\x00-\x1F",;]+/u', ' ', (string)$s); return mb_substr(trim($s), 0, $n); }

// ---------- registro ----------
if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
  header('Cache-Control: no-store');
  $ua = (string)($_SERVER['HTTP_USER_AGENT'] ?? '');
  if ($ua === '' || preg_match('/bot|crawl|spider|slurp|preview|facebookexternalhit|facebot|whatsapp|telegram|skype|slack|discord|linkedin|twitter|curl|wget|python|headless|monitor|lighthouse/i', $ua)) { http_response_code(204); exit; }
  $ref = (string)($_SERVER['HTTP_ORIGIN'] ?? $_SERVER['HTTP_REFERER'] ?? '');
  if ($ref !== '' && !preg_match('#^https?://(www\.)?energiaslatam\.com#i', $ref)) { http_response_code(204); exit; }
  $raw = file_get_contents('php://input', false, null, 0, 4000);
  $p = json_decode($raw, true); if (!is_array($p)) $p = $_POST;
  $t = in_array($p['t'] ?? '', ['visto', 'click', 'pv'], true) ? $p['t'] : '';
  if ($t === '') { http_response_code(204); exit; }
  $dv = preg_match('/iphone|android.+mobile|mobile/i', $ua) ? 'celular' : (preg_match('/ipad|tablet|android/i', $ua) ? 'tablet' : 'compu');
  $fila = [date('Y-m-d H:i:s'), $t, limpio($p['an'] ?? ''), limpio($p['ni'] ?? '', 20), limpio($p['ub'] ?? '', 40), limpio($p['po'] ?? '', 40), limpio($p['pg'] ?? '', 120), limpio($p['nid'] ?? '', 80), $dv];
  @file_put_contents($dir . '/med-' . date('Y-m') . '.csv', implode(',', $fila) . "\n", FILE_APPEND | LOCK_EX);
  http_response_code(204); exit;
}

// ---------- tablero ----------
if (isset($_GET['ver'])) {
  $key = trim((string)@file_get_contents($dir . '/ir.key'));
  if ($key === '' || !hash_equals($key, (string)$_GET['ver'])) { http_response_code(404); exit('No encontrado'); }
  header('Content-Type: text/html; charset=utf-8'); header('Cache-Control: no-store'); header('X-Robots-Tag: noindex');
  $re = '/^\d{4}-\d{2}-\d{2}$/';
  $desde = preg_match($re, $_GET['desde'] ?? '') ? $_GET['desde'] : date('Y-m-01');
  $hasta = preg_match($re, $_GET['hasta'] ?? '') ? $_GET['hasta'] : date('Y-m-d');
  $filtroAn = limpio($_GET['an'] ?? '');
  $A = []; $AU = []; $P = []; $D = []; $DV = []; $tot = ['visto' => 0, 'click' => 0, 'pv' => 0];
  foreach (glob($dir . '/med-*.csv') as $f) {
    $m = substr(basename($f), 4, 7); if ($m < substr($desde, 0, 7) || $m > substr($hasta, 0, 7)) continue;
    foreach (file($f, FILE_IGNORE_NEW_LINES) as $l) {
      $c = explode(',', $l); if (count($c) < 9) continue;
      $dia = substr($c[0], 0, 10); if ($dia < $desde || $dia > $hasta) continue;
      [$ts, $t, $an, $ni, $ub, $po, $pg, $nid, $dv] = $c;
      if ($t === 'pv') {
        if ($filtroAn !== '') continue;
        $tot['pv']++; $k = $nid !== '' ? '/n/' . $nid : ($pg ?: '/');
        $P[$k] = ($P[$k] ?? 0) + 1; $D[$dia]['pv'] = ($D[$dia]['pv'] ?? 0) + 1; $DV[$dv] = ($DV[$dv] ?? 0) + 1; continue;
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
  $h = function ($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); };
  $pct = function ($c, $v) { return $v ? number_format(100 * $c / $v, 1, ',', '.') . ' %' : '–'; };
  $n = function ($x) { return number_format((int)$x, 0, ',', '.'); };
  uasort($A, function ($a, $b) { return ($b['visto'] ?? 0) <=> ($a['visto'] ?? 0); });
  uasort($AU, function ($a, $b) { return ($b['visto'] ?? 0) <=> ($a['visto'] ?? 0); });
  arsort($P); ksort($D);
  $k = $h($_GET['ver']);
  echo '<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Medidor de publicidad</title><style>
body{font:15px Arial,sans-serif;max-width:900px;margin:20px auto;padding:0 14px;color:#0F213D;background:#fff}
h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:26px 0 8px;border-bottom:2px solid #3A963E;padding-bottom:4px}
.sub{color:#4A5B6C;font-size:13px;margin:0 0 14px}form{display:flex;flex-wrap:wrap;gap:8px;align-items:end;background:#F4F6F9;padding:10px;border-radius:8px}
label{font-size:12px;color:#4A5B6C;display:flex;flex-direction:column;gap:2px}input,select{font:14px Arial;padding:6px;border:1px solid #C9D3DE;border-radius:6px}
button{font:bold 14px Arial;padding:8px 14px;border:0;border-radius:6px;background:#3A963E;color:#fff}
.k{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:16px 0}.k div{background:#F4F6F9;border-left:4px solid #3A963E;padding:10px;border-radius:6px}.k b{display:block;font-size:24px}.k span{font-size:12px;color:#4A5B6C}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:6px 8px;border-bottom:1px solid #E3E9F0;text-align:right}th:first-child,td:first-child{text-align:left}th{background:#F4F6F9;font-size:12px;text-transform:uppercase;letter-spacing:.5px}
.wrap{overflow-x:auto}@media(max-width:600px){.k{grid-template-columns:1fr 1fr}}a{color:#0F213D}
</style><h1>Medidor de publicidad y páginas</h1><p class="sub">Solo uso interno. Sin robots ni vistas previas. "Vistas" = el aviso estuvo al menos 50 % en pantalla durante 1 segundo.</p>';
  echo '<form method="get"><input type="hidden" name="ver" value="' . $k . '"><label>Desde<input type="date" name="desde" value="' . $h($desde) . '"></label><label>Hasta<input type="date" name="hasta" value="' . $h($hasta) . '"></label><label>Anunciante<select name="an"><option value="">Todos</option>';
  foreach (array_keys($A) as $an) echo '<option' . ($an === $filtroAn ? ' selected' : '') . '>' . $h($an) . '</option>';
  if ($filtroAn !== '' && !isset($A[$filtroAn])) echo '<option selected>' . $h($filtroAn) . '</option>';
  echo '</select></label><button>Ver</button></form>';
  echo '<div class="k"><div><b>' . $n($tot['visto']) . '</b><span>vistas de avisos</span></div><div><b>' . $n($tot['click']) . '</b><span>clics en avisos</span></div><div><b>' . $pct($tot['click'], $tot['visto']) . '</b><span>porcentaje de clics</span></div><div><b>' . ($filtroAn === '' ? $n($tot['pv']) : '–') . '</b><span>páginas vistas</span></div></div>';
  echo '<h2>Por anunciante</h2><div class="wrap"><table><tr><th>Anunciante</th><th>Nivel</th><th>Vistas</th><th>Clics</th><th>% clics</th></tr>';
  foreach ($A as $an => $r) echo '<tr><td><a href="?ver=' . $k . '&desde=' . $h($desde) . '&hasta=' . $h($hasta) . '&an=' . urlencode($an) . '">' . $h($an) . '</a></td><td>' . $h($r['ni'] ?? '') . '</td><td>' . $n($r['visto'] ?? 0) . '</td><td>' . $n($r['click'] ?? 0) . '</td><td>' . $pct($r['click'] ?? 0, $r['visto'] ?? 0) . '</td></tr>';
  if (!$A) echo '<tr><td colspan="5">Todavía no hay datos en este período.</td></tr>';
  echo '</table></div><h2>Por anunciante y ubicación</h2><div class="wrap"><table><tr><th>Anunciante · página · posición</th><th>Vistas</th><th>Clics</th><th>% clics</th></tr>';
  foreach (array_slice($AU, 0, 60, true) as $kk => $r) echo '<tr><td>' . $h($kk) . '</td><td>' . $n($r['visto'] ?? 0) . '</td><td>' . $n($r['click'] ?? 0) . '</td><td>' . $pct($r['click'] ?? 0, $r['visto'] ?? 0) . '</td></tr>';
  echo '</table></div>';
  if ($filtroAn === '') {
    echo '<h2>Páginas más vistas</h2><div class="wrap"><table><tr><th>Página</th><th>Vistas</th></tr>';
    foreach (array_slice($P, 0, 40, true) as $pg => $v) echo '<tr><td>' . $h($pg) . '</td><td>' . $n($v) . '</td></tr>';
    echo '</table></div><h2>Por dispositivo</h2><div class="wrap"><table><tr><th>Dispositivo</th><th>Páginas vistas</th></tr>';
    foreach ($DV as $dv => $v) echo '<tr><td>' . $h($dv) . '</td><td>' . $n($v) . '</td></tr>';
    echo '</table></div>';
  }
  echo '<h2>Por día</h2><div class="wrap"><table><tr><th>Día</th><th>Vistas de avisos</th><th>Clics</th>' . ($filtroAn === '' ? '<th>Páginas vistas</th>' : '') . '</tr>';
  foreach ($D as $dia => $r) echo '<tr><td>' . $h($dia) . '</td><td>' . $n($r['visto'] ?? 0) . '</td><td>' . $n($r['click'] ?? 0) . '</td>' . ($filtroAn === '' ? '<td>' . $n($r['pv'] ?? 0) . '</td>' : '') . '</tr>';
  echo '</table></div><p class="sub" style="margin-top:20px">Energías LATAM · medidor propio, complementario a Google Analytics.</p>';
  exit;
}
http_response_code(404); echo 'No encontrado';
