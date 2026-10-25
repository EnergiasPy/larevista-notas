<?php
// mic-extra.php · precios, red de estaciones y GLP (fuente pública oficial) para /combustible/py
// Guarda una foto mensual de los precios para armar historial propio.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=3600');
$dir = __DIR__ . '/datos/mic'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = "$dir/extra.json";
if (is_file($cache) && empty($_GET['fresh']) && time() - filemtime($cache) < 6 * 3600) { readfile($cache); exit; }
function mic($p) {
  $ch = curl_init('https://gis.mic.gov.py/api/' . $p);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 60, CURLOPT_CONNECTTIMEOUT => 15, CURLOPT_USERAGENT => 'EnergiasLATAM/1.0 (+https://energiaslatam.com)']);
  $r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  return $c === 200 ? json_decode($r, true) : null;
}
$y = (int)date('Y');
$pr = mic('sales/by_price');
$es = mic('sales/by_estacion');
$co = mic('import/by_company/' . $y);
$gd = [$y => mic("sales/gas/by_destination/$y"), $y - 1 => mic('sales/gas/by_destination/' . ($y - 1))];
$gp = mic('sales/gas/by_price');
$gi = mic("import/gas/by_product/$y");
$gc = mic("sales/gas/by_category/$y");
if (!$pr && !$es) { if (is_file($cache)) { readfile($cache); exit; } http_response_code(502); echo '{"error":"fuente"}'; exit; }

// historial de precios: una foto por mes (la última del mes)
$hf = "$dir/precios-hist.json";
$hist = is_file($hf) ? (json_decode(file_get_contents($hf), true) ?: []) : [];
if ($pr && !empty($pr['data'])) { $hist[date('Y-m')] = ['f' => date('Y-m-d'), 'rows' => $pr['rows'], 'cols' => $pr['columns'], 'data' => $pr['data']]; ksort($hist); file_put_contents($hf, json_encode($hist)); }

$glp = [];
foreach ($gd as $yy => $j) if ($j && isset($j['data'])) foreach ($j['data'] as $r) $glp[] = [(int)$yy, (int)substr($r['fecha'], 5, 2), (int)$r['distribuidor'], $r['destino'], round((float)$r['volumen'])];
$gimp = [];
if ($gi && isset($gi['data'])) foreach ($gi['data'] as $r) $gimp[] = [(int)substr($r['fecha'], 5, 2), $r['pais'] ?? 'OTR', round((float)$r['volumen'])];
$out = [
  'upd' => date('c'),
  'names' => ($gc['distribuidor'] ?? []) + ($co['distribuidor'] ?? []),
  'precios' => $pr ? ['rows' => $pr['rows'], 'cols' => $pr['columns'], 'data' => $pr['data'], 'emb' => $pr['emblema'] ?? [], 'prod' => $pr['producto'] ?? []] : null,
  'precios_hist' => $hist,
  'estaciones' => $es ? array_map(function ($r) { return [(int)$r['distribuidor'], $r['departamento'], (int)$r['cantidad']]; }, $es['data']) : [],
  'glp' => $glp,
  'glp_precios' => $gp ? ['rows' => $gp['rows'], 'cols' => $gp['columns'], 'data' => $gp['data'], 'emb' => $gp['emblema'] ?? [], 'prod' => $gp['producto'] ?? []] : null,
  'glp_import' => $gimp,
  'paises' => ['AR' => 'Argentina', 'BO' => 'Bolivia', 'BR' => 'Brasil', 'US' => 'Estados Unidos', 'UY' => 'Uruguay', 'AE' => 'Emiratos Árabes', 'IN' => 'India', 'RU' => 'Rusia', 'OTR' => 'Otros'],
];
$j = json_encode($out, JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $j);
echo $j;
