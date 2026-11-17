<?php
// micache.php · caché resistente para los datos públicos del MIC (gis.mic.gov.py).
//
// Regla: el lector nunca espera a la API. Si hay una copia guardada se le entrega
// al instante, fresca o vieja, y el refresco ocurre después de cerrarle la conexión,
// uno a la vez y con un presupuesto de tiempo acotado. Si la API falló hace poco,
// no se vuelve a intentar hasta pasado el enfriamiento.

if (!defined('MIC_API')) define('MIC_API', 'https://gis.mic.gov.py/api/');
define('MIC_DIR', __DIR__ . '/datos/mic');
define('MIC_TIMEOUT', 15);        // máximo por llamada
define('MIC_CONNECT', 8);         // máximo para conectar
define('MIC_BUDGET_BG', 150);     // presupuesto total con la conexión ya cerrada
define('MIC_BUDGET_FG', 20);      // presupuesto total si el lector está esperando
define('MIC_COOLDOWN', 900);      // 15 min de enfriamiento si la fuente falló

function mic_dir() { if (!is_dir(MIC_DIR)) @mkdir(MIC_DIR, 0755, true); return MIC_DIR; }

// ---- presupuesto de tiempo ------------------------------------------------
function mic_budget($seconds) { $GLOBALS['mic_deadline'] = microtime(true) + $seconds; }
function mic_left() {
  if (empty($GLOBALS['mic_deadline'])) return MIC_TIMEOUT;
  return max(0, $GLOBALS['mic_deadline'] - microtime(true));
}

// ---- una llamada a la API -------------------------------------------------
function mic_get($path) {
  $left = mic_left();
  if ($left < 2) return null;                       // sin tiempo: no se intenta
  $t = (int)max(2, min(MIC_TIMEOUT, ceil($left)));
  $ch = curl_init(MIC_API . $path);
  curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => $t,
    CURLOPT_CONNECTTIMEOUT => (int)min(MIC_CONNECT, $t),
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_USERAGENT => 'EnergiasLATAM/1.0 (+https://energiaslatam.com)',
  ]);
  $r = curl_exec($ch);
  $c = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);
  if ($c !== 200 || !$r) return null;
  $j = json_decode($r, true);
  return is_array($j) ? $j : null;
}

// ---- candado y enfriamiento ----------------------------------------------
function mic_lock($key) {
  $h = @fopen(mic_dir() . "/.lock-$key", 'c');
  if (!$h) return false;
  if (!flock($h, LOCK_EX | LOCK_NB)) { fclose($h); return false; }
  $GLOBALS['mic_locks'][$key] = $h;
  return true;
}
function mic_unlock($key) {
  if (empty($GLOBALS['mic_locks'][$key])) return;
  flock($GLOBALS['mic_locks'][$key], LOCK_UN);
  fclose($GLOBALS['mic_locks'][$key]);
  unset($GLOBALS['mic_locks'][$key]);
}
function mic_cooling($key) {
  $f = mic_dir() . "/.fail-$key";
  return is_file($f) && (time() - filemtime($f) < MIC_COOLDOWN);
}
function mic_fail($key) { @touch(mic_dir() . "/.fail-$key"); }
function mic_ok($key)   { @unlink(mic_dir() . "/.fail-$key"); }

// ---- entrega sin hacer esperar -------------------------------------------
// Manda el cuerpo con su largo exacto para que el navegador cierre, e intenta
// además liberar el worker si el hosting lo permite.
function mic_send($body, $state, $age) {
  while (ob_get_level()) ob_end_clean();
  @ini_set('zlib.output_compression', 'Off');   // el largo que anunciamos es el del cuerpo sin comprimir
  header('Content-Type: application/json; charset=utf-8');
  header('Cache-Control: public, max-age=1800');
  header('X-Mic-Cache: ' . $state . '; age=' . (int)$age . '; sapi=' . php_sapi_name());
  header('Content-Length: ' . strlen($body));
  echo $body;
  flush();
  ignore_user_abort(true);
  if (function_exists('fastcgi_finish_request')) @fastcgi_finish_request();
}

// ---- flujo principal ------------------------------------------------------
// $key:   nombre corto para el candado ("2026", "extra")
// $cache: archivo de la copia guardada
// $ttl:   segundos que la copia se considera fresca
// $build: función que devuelve el JSON nuevo (string) o null si la fuente no respondió
function mic_serve($key, $cache, $ttl, $build) {
  $has   = is_file($cache);
  $age   = $has ? time() - filemtime($cache) : 0;
  $stale = !$has || $age >= $ttl;
  $forced = !empty($_GET['fresh']);

  // 1. Con copia guardada el lector recibe los datos ya, vieja o no.
  if ($has && !$forced) {
    mic_send(file_get_contents($cache), $stale ? 'stale' : 'fresh', $age);
    if (!$stale || mic_cooling($key) || !mic_lock($key)) exit;   // nada que refrescar, o ya lo hace otro
    @set_time_limit(MIC_BUDGET_BG + 30);
    mic_budget(MIC_BUDGET_BG);
    $j = $build();
    if ($j !== null) { file_put_contents($cache, $j); mic_ok($key); } else { mic_fail($key); }
    mic_unlock($key);
    exit;
  }

  // 2. Sin copia guardada: no hay más remedio que esperar, con presupuesto corto.
  if (!$forced && mic_cooling($key)) {
    http_response_code(503); header('Retry-After: 300');
    header('Content-Type: application/json; charset=utf-8');
    echo '{"error":"fuente"}'; exit;
  }
  if (!mic_lock($key)) {
    http_response_code(503); header('Retry-After: 20');
    header('Content-Type: application/json; charset=utf-8');
    echo '{"error":"preparando"}'; exit;
  }
  @set_time_limit(MIC_BUDGET_FG + 30);
  mic_budget($forced ? MIC_BUDGET_BG : MIC_BUDGET_FG);
  $j = $build();
  if ($j === null) {
    mic_fail($key); mic_unlock($key);
    if ($has) { mic_send(file_get_contents($cache), 'stale-fallback', $age); exit; }
    http_response_code(502);
    header('Content-Type: application/json; charset=utf-8');
    echo '{"error":"fuente"}'; exit;
  }
  file_put_contents($cache, $j); mic_ok($key); mic_unlock($key);
  mic_send($j, 'fresh', 0);
  exit;
}

// Completa los bloques que la fuente no devolvió con lo que ya había guardado,
// para que un refresco a medias nunca empobrezca la página.
function mic_keep(&$out, $cache, $claves) {
  if (!is_file($cache)) return;
  $prev = json_decode(file_get_contents($cache), true);
  if (!is_array($prev)) return;
  foreach ($claves as $k) if (empty($out[$k]) && !empty($prev[$k])) $out[$k] = $prev[$k];
}
