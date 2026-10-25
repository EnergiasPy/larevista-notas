<?php
// mic.php · datos de ventas e importaciones de combustibles por empresa (fuente pública oficial)
// Devuelve un JSON compacto y cacheado para /combustible. Uso: /mic.php?y=2026
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=3600');
$y = isset($_GET['y']) ? (int)$_GET['y'] : (int)date('Y');
if ($y < 2020 || $y > (int)date('Y')) { http_response_code(400); echo '{"error":"anio"}'; exit; }
$dir = __DIR__ . '/datos/mic';
if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = $dir . '/' . $y . '.json';
$ttl = ($y < (int)date('Y')) ? 30 * 86400 : 6 * 3600;
if (is_file($cache) && empty($_GET['fresh']) && (time() - filemtime($cache) < $ttl)) { readfile($cache); exit; }

function mic_get($path) {
  $ch = curl_init('https://gis.mic.gov.py/api/' . $path);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 60, CURLOPT_CONNECTTIMEOUT => 15,
    CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'EnergiasLATAM/1.0 (+https://energiaslatam.com)']);
  $r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  if ($c !== 200 || !$r) return null;
  return json_decode($r, true);
}

$sp = mic_get('sales/by_product/' . $y);
$ip = mic_get('import/by_product/' . $y);
$co = mic_get('import/by_company/' . $y);
if (!$sp || !isset($sp['data'])) {
  if (is_file($cache)) { readfile($cache); exit; }
  http_response_code(502); echo '{"error":"fuente"}'; exit;
}
$names = $co['distribuidor'] ?? [];
$prods = $sp['producto'] ?? [];
// cubos: ventas mes·empresa·producto, ventas mes·empresa·departamento, importación mes·empresa·producto
$vp = []; $vd = []; $im = [];
foreach ($sp['data'] as $r) {
  $m = (int)substr($r['fecha'], 5, 2); $d = (int)$r['distribuidor']; $v = (float)$r['volumen'];
  $k = "$m|$d|{$r['producto']}"; $vp[$k] = ($vp[$k] ?? 0) + $v;
  $k = "$m|$d|" . ($r['departamento'] ?? ''); $vd[$k] = ($vd[$k] ?? 0) + $v;
}
foreach (($ip['data'] ?? []) as $r) {
  $m = (int)substr($r['fecha'], 5, 2); $d = (int)$r['distribuidor'];
  $k = "$m|$d|{$r['producto']}"; $im[$k] = ($im[$k] ?? 0) + (float)$r['volumen'];
}
$pack = function ($a) { $o = []; foreach ($a as $k => $v) { $p = explode('|', $k); $o[] = [(int)$p[0], (int)$p[1], $p[2], round($v)]; } return $o; };
$out = ['y' => $y, 'upd' => date('c'), 'names' => $names, 'prods' => $prods,
  'vp' => $pack($vp), 'vd' => $pack($vd), 'im' => $pack($im)];
$j = json_encode($out, JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $j);
echo $j;
