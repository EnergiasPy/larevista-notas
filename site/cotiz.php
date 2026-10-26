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

// Petróleo (US$ por barril) · futuros Brent y WTI
foreach (['brent' => 'BZ=F', 'wti' => 'CL=F'] as $k => $s) {
  $y = json_decode(g('https://query1.finance.yahoo.com/v8/finance/chart/' . rawurlencode($s) . '?interval=1d&range=5d') ?: 'null', true);
  $mt = $y['chart']['result'][0]['meta'] ?? null;
  if ($mt && isset($mt['regularMarketPrice'])) $out['oil'][$k] = ['usd' => (float)$mt['regularMarketPrice'], 'prev' => (float)($mt['chartPreviousClose'] ?? 0), 'fecha' => date('c', (int)($mt['regularMarketTime'] ?? time()))];
}
if (!$out['oil']) foreach (['brent' => 'cb.f', 'wti' => 'cl.f'] as $k => $s) {
  $csv = g("https://stooq.com/q/l/?s=$s&f=sd2t2ohlcp&h&e=csv");
  if ($csv) { $l = explode("\n", trim($csv)); $c = isset($l[1]) ? str_getcsv($l[1]) : []; if (count($c) >= 8 && is_numeric($c[6])) $out['oil'][$k] = ['usd' => (float)$c[6], 'prev' => is_numeric($c[7]) ? (float)$c[7] : 0, 'fecha' => $c[1] . ' ' . $c[2]]; }
}
if ($out['oil']) $out['fuentes'][] = 'oil:mercado';

// foto diaria (para variación propia de Paraguay)
$hf = "$dir/hist.json"; $h = is_file($hf) ? (json_decode(file_get_contents($hf), true) ?: []) : [];
$hoy = date('Y-m-d'); if ($out['py']) { $h[$hoy] = $out['py']; ksort($h); $h = array_slice($h, -60, null, true); file_put_contents($hf, json_encode($h)); }
foreach (array_reverse(array_keys($h)) as $d) if ($d < $hoy) { $out['py_prev'] = $h[$d]; break; }

if (!$out['py'] && !$out['mk'] && is_file($cache)) { readfile($cache); exit; }
$js = json_encode($out, JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $js);
echo $js;
