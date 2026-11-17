<?php
// mic.php · datos de ventas e importaciones de combustibles por empresa (fuente pública oficial)
// Devuelve un JSON compacto y cacheado para /combustible y la portada. Uso: /mic.php?y=2026
// La caché la maneja micache.php: el lector nunca espera a la API.
require __DIR__ . '/micache.php';

$y = isset($_GET['y']) ? (int)$_GET['y'] : (int)date('Y');
if ($y < 2020 || $y > (int)date('Y')) {
  http_response_code(400);
  header('Content-Type: application/json; charset=utf-8');
  echo '{"error":"anio"}'; exit;
}

$cache = mic_dir() . '/' . $y . '.json';
$ttl = ($y < (int)date('Y')) ? 30 * 86400 : 6 * 3600;

$build = function () use ($y, $cache) {
  $sp = mic_get('sales/by_product/' . $y);
  if (!$sp || !isset($sp['data'])) return null;          // sin ventas no hay nada que armar
  $ip = mic_get('import/by_product/' . $y);
  $co = mic_get('import/by_company/' . $y);

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
  $pack = function ($a) {
    $o = [];
    foreach ($a as $k => $v) { $p = explode('|', $k); $o[] = [(int)$p[0], (int)$p[1], $p[2], round($v)]; }
    return $o;
  };
  $out = [
    'y' => $y, 'upd' => date('c'),
    'names' => $co['distribuidor'] ?? [],
    'prods' => $sp['producto'] ?? [],
    'vp' => $pack($vp), 'vd' => $pack($vd), 'im' => $pack($im),
  ];
  // si importaciones o nombres no llegaron, se conserva lo que ya estaba
  mic_keep($out, $cache, ['names', 'prods', 'im']);
  return json_encode($out, JSON_UNESCAPED_UNICODE);
};

mic_serve((string)$y, $cache, $ttl, $build);
