<?php
// estaciones.php · estaciones de servicio de Paraguay con ubicación (fuente pública: mapa del MIC, gis.mic.gov.py)
// Devuelve una lista compacta para el mapa de /estaciones. No incluye el nombre del operador.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=3600');
$dir = __DIR__ . '/datos/mic'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = "$dir/estaciones-mapa.json";
if (is_file($cache) && empty($_GET['fresh']) && time() - filemtime($cache) < 24 * 3600) { readfile($cache); exit; }
$ch = curl_init('https://gis.mic.gov.py/features/estaciones/');
curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 60, CURLOPT_CONNECTTIMEOUT => 15,
  CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'EnergiasLATAM/1.0 (+https://energiaslatam.com)']);
$r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
$j = ($c === 200 && $r) ? json_decode($r, true) : null;
if (!$j || empty($j['features'])) {
  if (is_file($cache)) { readfile($cache); exit; }
  http_response_code(502); echo '{"error":"fuente"}'; exit;
}
$t = function ($s) { return trim(preg_replace('/\s+/', ' ', (string)$s)); };
$rows = [];
foreach ($j['features'] as $f) {
  $g = $f['geometry']['coordinates'] ?? null; $p = $f['properties'] ?? [];
  if (!$g || !is_numeric($g[0]) || !is_numeric($g[1])) continue;
  $rows[] = [round((float)$g[1], 6), round((float)$g[0], 6), $t($p['marker-icon'] ?? ''), $t($p['departamento'] ?? ''),
    $t($p['distrito'] ?? ''), $t($p['direccion'] ?? ''), (($p['tipo'] ?? '') === 'Puesto de Consumo Propio') ? 1 : 0, $t($p['distribuidor'] ?? '')];
}
$out = json_encode(['upd' => date('c'), 'fuente' => 'Ministerio de Industria y Comercio (gis.mic.gov.py)',
  'campos' => ['lat', 'lng', 'emblema', 'departamento', 'distrito', 'direccion', 'consumo_propio', 'distribuidor'], 'data' => $rows], JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $out);
echo $out;
