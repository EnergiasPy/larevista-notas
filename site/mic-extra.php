<?php
// mic-extra.php · precios, red de estaciones y GLP (fuente pública oficial) para /combustible/py y /estaciones
// Guarda una foto mensual de los precios para armar historial propio.
// La caché la maneja micache.php: el lector nunca espera a la API.
require __DIR__ . '/micache.php';

$cache = mic_dir() . '/extra.json';
$y = (int)date('Y');

$build = function () use ($y, $cache) {
  $dir = mic_dir();
  $pr = mic_get('sales/by_price');
  $es = mic_get('sales/by_estacion');
  if (!$pr && !$es) return null;                  // sin precios ni red no hay nada que armar
  $co = mic_get('import/by_company/' . $y);
  $gc = mic_get("sales/gas/by_category/$y");
  $gd = [$y => mic_get("sales/gas/by_destination/$y"), $y - 1 => mic_get('sales/gas/by_destination/' . ($y - 1))];
  $gp = mic_get('sales/gas/by_price');
  $gi = mic_get("import/gas/by_product/$y");

  // historial de precios: una foto por mes (la última del mes)
  $hf = "$dir/precios-hist.json";
  $hist = is_file($hf) ? (json_decode(file_get_contents($hf), true) ?: []) : [];
  if ($pr && !empty($pr['data'])) {
    $hist[date('Y-m')] = ['f' => date('Y-m-d'), 'rows' => $pr['rows'], 'cols' => $pr['columns'], 'data' => $pr['data']];
    ksort($hist);
    file_put_contents($hf, json_encode($hist));
  }

  $glp = [];
  foreach ($gd as $yy => $j) {
    if ($j && isset($j['data'])) foreach ($j['data'] as $r) {
      $glp[] = [(int)$yy, (int)substr($r['fecha'], 5, 2), (int)$r['distribuidor'], $r['destino'], round((float)$r['volumen'])];
    }
  }
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
  // los bloques que la fuente no devolvió se completan con lo ya guardado
  mic_keep($out, $cache, ['names', 'precios', 'estaciones', 'glp', 'glp_precios', 'glp_import']);
  return json_encode($out, JSON_UNESCAPED_UNICODE);
};

mic_serve('extra', $cache, 6 * 3600, $build);
