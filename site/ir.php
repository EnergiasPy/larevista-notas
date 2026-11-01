<?php
/* Enlaces medidos · energiaslatam.com
   /ir.php?d=<destino>&o=<origen>  → cuenta el clic y redirige al destino (solo destinos de la lista)
   /ir.php?ver                     → lleva al medidor (med.php, con contraseña), que muestra estos clics
   No guarda IP ni datos personales: fecha, destino, origen y tipo de dispositivo. */
$DEST = [
  'gulf' => 'https://energiaslatam.com/n/2026-10-30-gulf-lanzamiento-paraguay', // registro cerrado el 31/10: lleva a la nota
  'gulf-nota' => 'https://energiaslatam.com/n/2026-10-30-gulf-lanzamiento-paraguay',
];
$dir = __DIR__ . '/datos';
if (!is_dir($dir)) { @mkdir($dir, 0750); @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }
$log = $dir . '/clics.csv';

if (isset($_GET['ver'])) { header('Location: /med.php', true, 303); exit; } // el resumen ahora está en el medidor, con contraseña

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
