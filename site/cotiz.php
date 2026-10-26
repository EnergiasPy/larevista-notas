<?php
// cotiz.php · 1 dólar en monedas de la región + petróleo. Cache 3 h y foto diaria para la variación.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=1800');
$dir = __DIR__ . '/datos/cotiz'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = "$dir/actual.json";
if (is_file($cache) && empty($_GET['fresh']) && time() - filemtime($cache) < 3 * 3600) { readfile($cache); exit; }
function g($u) {
  $ch = curl_init($u);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 25, CURLOPT_CONNECTTIMEOUT => 10, CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'Mozilla/5.0 (EnergiasLATAM)']);
  $r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  return $c === 200 ? $r : null;
}
$out = ['upd' => date('c'), 'usd' => [], 'ar' => null, 'oil' => []];
// tipos de cambio de referencia (1 USD = X)
$j = json_decode(g('https://open.er-api.com/v6/latest/USD') ?: 'null', true);
if ($j && ($j['result'] ?? '') === 'success') foreach (['PYG', 'ARS', 'BRL', 'CLP', 'UYU', 'BOB', 'PEN', 'COP', 'MXN', 'EUR'] as $m) if (isset($j['rates'][$m])) $out['usd'][$m] = $j['rates'][$m];
// Argentina: oficial y blue
$a = json_decode(g('https://dolarapi.com/v1/dolares') ?: 'null', true);
if (is_array($a)) foreach ($a as $d) if (in_array($d['casa'] ?? '', ['oficial', 'blue'], true)) $out['ar'][$d['casa']] = ['compra' => $d['compra'], 'venta' => $d['venta']];
// petróleo (US$ por barril)
foreach (['brent' => 'cb.f', 'wti' => 'cl.f'] as $k => $s) {
  $csv = g("https://stooq.com/q/l/?s=$s&f=sd2t2ohlc&h&e=csv");
  if ($csv && preg_match('/\n[^,]+,([\d-]+),[^,]*,[^,]*,[^,]*,[^,]*,([\d.]+)/', $csv, $m)) $out['oil'][$k] = ['fecha' => $m[1], 'usd' => (float)$m[2]];
}
// foto diaria para calcular la variación contra el día anterior
$hf = "$dir/hist.json"; $h = is_file($hf) ? (json_decode(file_get_contents($hf), true) ?: []) : [];
$hoy = date('Y-m-d');
if ($out['usd']) { $h[$hoy] = ['usd' => $out['usd'], 'oil' => $out['oil']]; ksort($h); $h = array_slice($h, -60, null, true); file_put_contents($hf, json_encode($h)); }
$dias = array_keys($h); $prev = null; foreach (array_reverse($dias) as $d) if ($d < $hoy) { $prev = $h[$d]; $out['prev_fecha'] = $d; break; }
$out['prev'] = $prev;
if (!$out['usd'] && is_file($cache)) { readfile($cache); exit; }
$js = json_encode($out, JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $js);
echo $js;
