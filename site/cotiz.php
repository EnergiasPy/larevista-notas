<?php
// cotiz.php · 1 dólar en monedas de la región + petróleo. Fuentes de mercado en tiempo real, cache 30 min.
// Paraguay: casa de cambios local (compra/venta). Argentina: oficial y blue. Resto: cotización de mercado en vivo.
header('Content-Type: application/json; charset=utf-8');
ini_set('serialize_precision', '-1');
header('Cache-Control: public, max-age=900');
$dir = __DIR__ . '/datos/cotiz'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = "$dir/actual.json";
if (is_file($cache) && empty($_GET['fresh']) && time() - filemtime($cache) < 1800) { readfile($cache); exit; }
function g($u, $html = false) {
  $ch = curl_init($u);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 20, CURLOPT_CONNECTTIMEOUT => 8, CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_USERAGENT => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36', CURLOPT_HTTPHEADER => [$html ? 'Accept: text/html,application/xhtml+xml' : 'Accept: application/json, text/plain, */*']]);
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

// Bolivia · Banco Central de Bolivia, tipo de cambio oficial (Bs por US$)
$bo = "$dir/bo.json";
if (!is_file($bo) || time() - filemtime($bo) > 6 * 3600) {
  $h = g('https://www.bcb.gob.bo/', true);
  if ($h) { $t = preg_replace('/\s+/', ' ', html_entity_decode(strip_tags($h)));
    if (preg_match('/Tipo de cambio oficial.{0,120}?VIGENTE PARA (.{5,80}?\d{4}).{0,40}?(\d{1,2},\d{2})/iu', $t, $m)) file_put_contents($bo, json_encode(['v' => (float)str_replace(',', '.', $m[2]), 'vigencia' => trim($m[1])])); }
}
if (is_file($bo) && time() - filemtime($bo) < 48 * 3600) { $out['bo'] = json_decode(file_get_contents($bo), true); $out['fuentes'][] = 'bo:bcb'; }
// Chile · dólar observado del Banco Central de Chile (vía mindicador.cl)
$cl = json_decode(g('https://mindicador.cl/api/dolar') ?: 'null', true);
if (!empty($cl['serie'][0]['valor'])) { $out['cl'] = ['v' => (float)$cl['serie'][0]['valor'], 'fecha' => substr($cl['serie'][0]['fecha'], 0, 10), 'prev' => (float)($cl['serie'][1]['valor'] ?? 0)]; $out['fuentes'][] = 'cl:bcch'; }

// Perú · Kambista (casa de cambio online, compra / venta en soles por US$)
$pe = "$dir/pe.json";
if (!is_file($pe) || time() - filemtime($pe) > 3600) {
  $h = g('https://kambista.com/', true);
  if ($h) { $t = preg_replace('/\s+/', ' ', html_entity_decode(strip_tags(preg_replace('#<(script|style)[^>]*>.*?</\1>#is', ' ', $h))));
    if (preg_match('/Compra[^0-9]{0,40}(\d\.\d{2,4})/iu', $t, $c1) && preg_match('/Venta[^0-9]{0,40}(\d\.\d{2,4})/iu', $t, $v1)) {
      $c = (float)$c1[1]; $v = (float)$v1[1];
      if ($c > 2 && $c < 6 && $v >= $c && $v < 6) file_put_contents($pe, json_encode(['compra' => $c, 'venta' => $v, 'fecha' => date('c')])); } }
}
if (is_file($pe) && time() - filemtime($pe) < 48 * 3600) { $out['pe'] = json_decode(file_get_contents($pe), true); $out['fuentes'][] = 'pe:kambista'; }

// Uruguay · Altercambio (casa de cambio, compra / venta en pesos uruguayos por US$)
$uy = "$dir/uy.json";
if (!is_file($uy) || time() - filemtime($uy) > 3600) {
  $h = g('https://altercambio.com.uy/', true);
  if ($h) { $t = preg_replace('/\s+/', ' ', html_entity_decode(strip_tags(preg_replace('#<(script|style)[^>]*>.*?</\1>#is', ' ', str_replace(['</td>', '</div>', '</span>'], ' | ', $h)))));
    if (preg_match('/Dolar USA[\s|]*([\d]+[.,]\d{2})[\s|]*([\d]+[.,]\d{2})/iu', $t, $m)) {
      $c = (float)str_replace(',', '.', $m[1]); $v = (float)str_replace(',', '.', $m[2]);
      if ($c > 20 && $c < 80 && $v >= $c && $v < 80) file_put_contents($uy, json_encode(['compra' => $c, 'venta' => $v, 'fecha' => date('c')])); } }
}
if (is_file($uy) && time() - filemtime($uy) < 48 * 3600) { $out['uy'] = json_decode(file_get_contents($uy), true); $out['fuentes'][] = 'uy:altercambio'; }

// Petróleo y diésel · precios spot oficiales de la EIA (EE. UU.), publicación semanal con datos diarios
$eia = "$dir/eia.json";
if (!is_file($eia) || time() - filemtime($eia) > 6 * 3600) {
  $h = g('https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm', true);
  if ($h) {
    $fechas = []; $res = [];
    foreach (preg_split('#<tr#i', $h) as $tr) {
      $t = ltrim(trim(preg_replace('/\s+/', ' ', html_entity_decode(strip_tags(str_replace(['</td>', '</th>'], ' | ', $tr))))), '> |');
      if (!$fechas && preg_match_all('#\b(\d{2}/\d{2}/\d{2})\b#', $t, $m) && count($m[1]) >= 3) $fechas = $m[1];
      foreach (['wti' => 'WTI - Cushing', 'brent' => 'Brent - Europe', 'diesel_golfo' => 'ULSD - U.S. Gulf Coast'] as $k => $lab)
        if (!isset($res[$k]) && stripos($t, $lab) === 0 && preg_match_all('#\|\s*([\d]+\.[\d]+)#', $t, $v)) $res[$k] = array_map('floatval', $v[1]);
    }
    if ($res) file_put_contents($eia, json_encode(['fechas' => $fechas, 'v' => $res]));
  }
}
if (is_file($eia) && time() - filemtime($eia) < 14 * 86400) {
  $e = json_decode(file_get_contents($eia), true); $f = $e['fechas'] ?? [];
  foreach (($e['v'] ?? []) as $k => $vals) { $n = count($vals); if (!$n) continue;
    $out['oil'][$k] = ['usd' => $vals[$n - 1], 'prev' => $n > 1 ? $vals[$n - 2] : 0, 'fecha' => $f[min($n, count($f)) - 1] ?? '', 'unidad' => $k === 'diesel_golfo' ? 'galón' : 'barril']; }
}
if ($out['oil']) $out['fuentes'][] = 'oil:eia';
// Cierre diario más reciente · EIA "Today in Energy · Prices" (se actualiza cada día hábil)
$tie = "$dir/eia-hoy.json";
if (!is_file($tie) || time() - filemtime($tie) > 3 * 3600) {
  $h = g('https://www.eia.gov/todayinenergy/prices.php', true);
  if ($h) {
    $t = preg_replace('/\s+/', ' ', html_entity_decode(strip_tags(str_replace(['</td>', '</th>', '</tr>'], ' | ', $h))));
    $r = [];
    if (preg_match('#Spot Petroleum Prices,\s*(\d{1,2}/\d{1,2}/\d{2})\s*Close#i', $t, $m)) {
      $fe = vsprintf('%02d/%02d/%s', explode('/', $m[1])); $num = '\|?\s*([\d]+\.[\d]+)\s*\|?\s*([-+]?[\d]+\.?[\d]*)';
      $ci = stripos($t, 'Crude Oil', stripos($t, $m[0]));
      if ($ci !== false) { $seg = substr($t, $ci, 600);
        if (preg_match('#WTI\s*' . $num . '#', $seg, $q)) $r['wti'] = [(float)$q[1], (float)$q[2]];
        if (preg_match('#Brent\s*' . $num . '#', $seg, $q)) $r['brent'] = [(float)$q[1], (float)$q[2]]; }
      $di = stripos($t, 'Low-Sulfur Diesel', stripos($t, $m[0]));
      if ($di !== false && preg_match('#Gulf Coast\s*' . $num . '#', substr($t, $di, 400), $q)) $r['diesel_golfo'] = [(float)$q[1], (float)$q[2]];
      if ($r) file_put_contents($tie, json_encode(['fecha' => $fe, 'v' => $r]));
    }
  }
}
if (is_file($tie) && time() - filemtime($tie) < 7 * 86400) {
  $e = json_decode(file_get_contents($tie), true); $fe = $e['fecha'] ?? '';
  $iso = function ($f) { $p = explode('/', $f); return count($p) === 3 ? '20' . $p[2] . $p[0] . $p[1] : ''; };
  foreach (($e['v'] ?? []) as $k => $v) {
    $ant = $out['oil'][$k] ?? null;
    if ($ant && $iso($ant['fecha'] ?? '') >= $iso($fe)) continue; // el dato semanal ya es igual o más nuevo
    $out['oil'][$k] = ['usd' => $v[0], 'prev' => $v[1] != -100 ? round($v[0] / (1 + $v[1] / 100), 2) : 0, 'fecha' => $fe, 'unidad' => $k === 'diesel_golfo' ? 'galón' : 'barril'];
  }
  if ($e['v'] ?? null) $out['fuentes'][] = 'oil:eia-hoy';
}


// foto diaria (para variación propia de Paraguay)
$hf = "$dir/hist.json"; $h = is_file($hf) ? (json_decode(file_get_contents($hf), true) ?: []) : [];
$hoy = date('Y-m-d'); if ($out['py']) { $h[$hoy] = $out['py']; ksort($h); $h = array_slice($h, -60, null, true); file_put_contents($hf, json_encode($h)); }
foreach (array_reverse(array_keys($h)) as $d) if ($d < $hoy) { $out['py_prev'] = $h[$d]; break; }

if (!$out['py'] && !$out['mk'] && is_file($cache)) { readfile($cache); exit; }
$js = json_encode($out, JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $js);
echo $js;
