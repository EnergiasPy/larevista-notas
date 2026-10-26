<?php
// cotiz.php · 1 dólar en monedas de la región + petróleo. Fuentes de mercado en tiempo real, cache 30 min.
// Paraguay: casa de cambios local (compra/venta). Argentina: oficial y blue. Resto: cotización de mercado en vivo.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=900');
$dir = __DIR__ . '/datos/cotiz'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = "$dir/actual.json";
if (is_file($cache) && empty($_GET['fresh']) && time() - filemtime($cache) < 1800) { readfile($cache); exit; }
function g($u) {
  $ch = curl_init($u);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 20, CURLOPT_CONNECTTIMEOUT => 8, CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_USERAGENT => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36', CURLOPT_HTTPHEADER => ['Accept: application/json, text/plain, */*']]);
  $r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  return $c === 200 ? $r : null;
}
$out = ['upd' => date('c'), 'py' => null, 'ar' => null, 'mk' => [], 'oil' => [], 'fuentes' => []];

// Paraguay · Cambios Chaco (compra / venta, casa matriz)
$j = json_decode(g('https://www.cambioschaco.com.py/api/branch_office/1/exchange') ?: 'null', true);
if (isset($j['items'])) foreach ($j['items'] as $it) {
  $iso = $it['isoCode'] ?? '';
  if (in_array($iso, ['USD', 'BRL', 'ARS', 'EUR'], true)) $out['py'][$iso] = ['compra' => (float)$it['purchasePrice'], 'venta' => (float)$it['salePrice']];
}
if ($out['py']) $out['fuentes'][] = 'py:chaco';

// Argentina · oficial y blue
$a = json_decode(g('https://dolarapi.com/v1/dolares') ?: 'null', true);
if (is_array($a)) foreach ($a as $d) if (in_array($d['casa'] ?? '', ['oficial', 'blue'], true)) $out['ar'][$d['casa']] = ['compra' => (float)$d['compra'], 'venta' => (float)$d['venta'], 'fecha' => $d['fechaActualizacion'] ?? ''];
if ($out['ar']) $out['fuentes'][] = 'ar:dolarapi';

// Resto de la región · mercado en vivo (1 USD = X)
$pairs = 'USD-BRL,USD-CLP,USD-UYU,USD-BOB,USD-PEN,USD-PYG,USD-ARS,EUR-USD';
$m = json_decode(g("https://economia.awesomeapi.com.br/json/last/$pairs") ?: 'null', true);
if (is_array($m)) foreach ($m as $k => $v) $out['mk'][substr($k, 0, 3) === 'USD' ? substr($k, 3) : $k] = ['bid' => (float)$v['bid'], 'ask' => (float)$v['ask'], 'pct' => (float)($v['pctChange'] ?? 0), 'fecha' => $v['create_date'] ?? ''];
if ($out['mk']) $out['fuentes'][] = 'mk:awesomeapi';

// Petróleo y diésel · precios spot oficiales de la EIA (EE. UU.), publicación semanal con datos diarios
$eia = "$dir/eia.json";
if (!is_file($eia) || time() - filemtime($eia) > 6 * 3600) {
  $h = g('https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm');
  if ($h) {
    $fechas = []; $res = [];
    foreach (preg_split('#<tr#i', $h) as $tr) {
      $t = trim(preg_replace('/\s+/', ' ', html_entity_decode(strip_tags(str_replace(['</td>', '</th>'], ' | ', $tr)))));
      if (!$fechas && preg_match_all('#\b(\d{2}/\d{2}/\d{2})\b#', $t, $m) && count($m[1]) >= 3) $fechas = $m[1];
      foreach (['wti' => 'WTI - Cushing', 'brent' => 'Brent - Europe', 'diesel_golfo' => 'ULSD - U.S. Gulf Coast'] as $k => $lab)
        if (!isset($res[$k]) && stripos($t, $lab) === 0 && preg_match_all('#\|\s*([\d]+\.[\d]+)#', $t, $v)) $res[$k] = array_map('floatval', $v[1]);
    }
    if ($res) file_put_contents($eia, json_encode(['fechas' => $fechas, 'v' => $res]));
  }
}
if (is_file($eia)) {
  $e = json_decode(file_get_contents($eia), true); $f = $e['fechas'] ?? [];
  foreach (($e['v'] ?? []) as $k => $vals) { $n = count($vals); if (!$n) continue;
    $out['oil'][$k] = ['usd' => $vals[$n - 1], 'prev' => $n > 1 ? $vals[$n - 2] : 0, 'fecha' => $f[min($n, count($f)) - 1] ?? '', 'unidad' => $k === 'diesel_golfo' ? 'galón' : 'barril']; }
}
if ($out['oil']) $out['fuentes'][] = 'oil:eia';

// foto diaria (para variación propia de Paraguay)
$hf = "$dir/hist.json"; $h = is_file($hf) ? (json_decode(file_get_contents($hf), true) ?: []) : [];
$hoy = date('Y-m-d'); if ($out['py']) { $h[$hoy] = $out['py']; ksort($h); $h = array_slice($h, -60, null, true); file_put_contents($hf, json_encode($h)); }
foreach (array_reverse(array_keys($h)) as $d) if ($d < $hoy) { $out['py_prev'] = $h[$d]; break; }

if (!$out['py'] && !$out['mk'] && is_file($cache)) { readfile($cache); exit; }
$js = json_encode($out, JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $js);
echo $js;
