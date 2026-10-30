<?php
/* Enlaces medidos · energiaslatam.com
   /ir.php?d=<destino>&o=<origen>  → cuenta el clic y redirige al destino (solo destinos de la lista)
   /ir.php?ver=<clave>             → resumen de clics (la clave está en datos/ir.key)
   No guarda IP ni datos personales: fecha, destino, origen y tipo de dispositivo. */
$DEST = [
  'gulf' => 'https://anjor.com.ar/invitacion_gulf/',
  'gulf-nota' => 'https://energiaslatam.com/n/2026-10-30-gulf-lanzamiento-paraguay',
];
$dir = __DIR__ . '/datos';
if (!is_dir($dir)) { @mkdir($dir, 0750); @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }
$log = $dir . '/clics.csv';

if (isset($_GET['ver'])) {
  $kf = $dir . '/ir.key';
  if (!is_file($kf)) @file_put_contents($kf, bin2hex(random_bytes(8)));
  $key = trim((string)@file_get_contents($kf));
  if ($key === '' || !hash_equals($key, (string)$_GET['ver'])) { http_response_code(404); exit('No encontrado'); }
  header('Content-Type: text/html; charset=utf-8'); header('Cache-Control: no-store'); header('X-Robots-Tag: noindex');
  $t = []; $o = []; $dia = []; $dev = []; $n = 0;
  foreach ((is_file($log) ? file($log, FILE_IGNORE_NEW_LINES) : []) as $l) {
    $c = str_getcsv($l); if (count($c) < 4) continue; $n++;
    $d = $c[1]; $t[$d] = ($t[$d] ?? 0) + 1;
    $o[$d . ' · ' . $c[2]] = ($o[$d . ' · ' . $c[2]] ?? 0) + 1;
    $dia[$d . ' · ' . substr($c[0], 0, 10)] = ($dia[$d . ' · ' . substr($c[0], 0, 10)] ?? 0) + 1;
    $dev[$d . ' · ' . $c[3]] = ($dev[$d . ' · ' . $c[3]] ?? 0) + 1;
  }
  $tb = function ($tit, $a) { ksort($a); $h = '<h2>' . $tit . '</h2><table>'; foreach ($a as $k => $v) $h .= '<tr><td>' . htmlspecialchars($k) . '</td><td><b>' . $v . '</b></td></tr>'; return $h . '</table>'; };
  echo '<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><title>Clics medidos</title><style>body{font:16px Arial,sans-serif;max-width:640px;margin:24px auto;padding:0 16px;color:#0F213D}table{border-collapse:collapse;width:100%}td{border-bottom:1px solid #DCE3EA;padding:6px 4px}td+td{text-align:right}h2{font-size:18px;margin-top:24px}</style>';
  $rb = []; $nr = 0; $rf = $dir . '/robots.csv';
  foreach ((is_file($rf) ? file($rf, FILE_IGNORE_NEW_LINES) : []) as $l) { $c = str_getcsv($l); if (count($c) < 4) continue; $nr++; $rb[$c[1] . ' · ' . $c[3]] = ($rb[$c[1] . ' · ' . $c[3]] ?? 0) + 1; }
  echo '<h1>Clics medidos</h1><p>Personas: <b>' . $n . '</b> · Robots y vistas previas: <b>' . $nr . '</b> · Total con todo: <b>' . ($n + $nr) . '</b></p><p style="font-size:13px;color:#4A5B6C">Robots y vistas previas se registran desde el 30/10 a la noche.</p>' . $tb('Por destino', $t) . $tb('Por origen', $o) . $tb('Por día', $dia) . $tb('Por dispositivo', $dev) . $tb('Robots y vistas previas', $rb);
  exit;
}

$d = isset($_GET['d']) ? strtolower(preg_replace('/[^a-z0-9_-]/i', '', $_GET['d'])) : '';
if (!isset($DEST[$d])) { header('Location: /', true, 302); exit; }
$orig = isset($_GET['o']) ? substr(strtolower(preg_replace('/[^a-z0-9_-]/i', '', $_GET['o'])), 0, 24) : '';
if ($orig === '') $orig = 'directo';
$ua = (string)($_SERVER['HTTP_USER_AGENT'] ?? '');
$robot = $ua === '' || preg_match('/bot|crawl|spider|slurp|preview|facebookexternalhit|facebot|whatsapp|telegram|skype|slack|discord|linkedin|twitter|curl|wget|python|headless|monitor/i', $ua)
  || (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'HEAD');
date_default_timezone_set('America/Asuncion');
if (!$robot) {
  $dv = preg_match('/iphone|android.+mobile|mobile/i', $ua) ? 'celular' : (preg_match('/ipad|tablet|android/i', $ua) ? 'tablet' : 'compu');
  @file_put_contents($log, date('Y-m-d H:i:s') . ',' . $d . ',' . $orig . ',' . $dv . "\n", FILE_APPEND | LOCK_EX);
} else {
  // robots y vistas previas (WhatsApp, Facebook, etc.) van aparte: no suman como clics de personas
  $q = 'otro'; foreach (['whatsapp','facebookexternalhit','facebot','telegram','twitter','linkedin','slack','discord','skype','googlebot','bingbot'] as $k) if (stripos($ua, $k) !== false) { $q = $k; break; }
  if ($ua === '') $q = 'sin-agente';
  @file_put_contents($dir . '/robots.csv', date('Y-m-d H:i:s') . ',' . $d . ',' . $orig . ',' . $q . "\n", FILE_APPEND | LOCK_EX);
}
header('Cache-Control: no-store'); header('X-Robots-Tag: noindex');
header('Location: ' . $DEST[$d], true, 302);
