<?php
// cotiz.php · 1 dólar en monedas de la región + petróleo, con fuente, fecha del valor y hora de consulta por dato.
// Cada fuente guarda su último dato válido. Si una consulta falla se sigue mostrando ese dato, marcado como "sin actualizar".
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=600');
ini_set('serialize_precision', '-1');
date_default_timezone_set('America/Asuncion');
$dir = __DIR__ . '/datos/cotiz'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = "$dir/actual2.json";
if (is_file($cache) && empty($_GET['fresh']) && time() - filemtime($cache) < 900) { readfile($cache); exit; }

function g($u, $html = false) {
  $ch = curl_init($u);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 20, CURLOPT_CONNECTTIMEOUT => 8, CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_USERAGENT => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36',
    CURLOPT_HTTPHEADER => [$html ? 'Accept: text/html,application/xhtml+xml' : 'Accept: application/json, text/plain, */*']]);
  $r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  return $c === 200 ? $r : null;
}
function txt($h) { return preg_replace('/\s+/', ' ', html_entity_decode(strip_tags(preg_replace('#<(script|style)[^>]*>.*?</\1>#is', ' ', str_replace(['</td>', '</th>', '</div>', '</span>', '</p>'], ' | ', $h))))); }
// consulta una fuente cada $ttl segundos; guarda el último dato válido y la hora en que se consultó
function fuente($id, $ttl, $fn) {
  global $dir; $f = "$dir/f-$id.json";
  $prev = is_file($f) ? json_decode(file_get_contents($f), true) : null;
  $intentado = $prev['intento'] ?? 0;
  if (!$prev || time() - $intentado > $ttl) {
    $d = null; try { $d = $fn(); } catch (Throwable $e) { $d = null; }
    if ($d) { $prev = ['d' => $d, 'consultado' => date('c'), 'intento' => time(), 'ok' => true]; }
    elseif ($prev) { $prev['intento'] = time(); $prev['ok'] = false; }
    if ($prev) file_put_contents($f, json_encode($prev, JSON_UNESCAPED_UNICODE));
  }
  if (!$prev) return null;
  $r = $prev['d']; $r['consultado'] = $prev['consultado'];
  // sin actualizar: la última consulta falló o el dato tiene más de 2 días
  $r['sin_actualizar'] = !$prev['ok'] || (time() - strtotime($prev['consultado']) > 2 * 86400);
  return $r;
}
$items = [];

// Paraguay · Cambios Chaco, casa matriz (compra / venta)
$py = fuente('py', 1800, function () {
  $j = json_decode(g('https://www.cambioschaco.com.py/api/branch_office/1/exchange') ?: 'null', true);
  foreach (($j['items'] ?? []) as $it) if (($it['isoCode'] ?? '') === 'USD') return ['compra' => (float)$it['purchasePrice'], 'venta' => (float)$it['salePrice']];
  return null;
});
if ($py) $items[] = $py + ['id' => 'py', 'pais' => 'Paraguay', 'mon' => 'Gs', 'tipo' => 'Casa de cambio, compra y venta en efectivo', 'fuente' => 'Cambios Chaco (casa matriz)', 'url' => 'https://www.cambioschaco.com.py/', 'fecha_valor' => 'vigente al momento de la consulta'];

// Argentina · oficial y blue (paralelo)
$ar = fuente('ar', 1800, function () {
  $a = json_decode(g('https://dolarapi.com/v1/dolares') ?: 'null', true); $o = [];
  if (is_array($a)) foreach ($a as $d) if (in_array($d['casa'] ?? '', ['oficial', 'blue'], true)) $o[$d['casa']] = ['compra' => (float)$d['compra'], 'venta' => (float)$d['venta'], 'fecha' => $d['fechaActualizacion'] ?? ''];
  return isset($o['oficial']) ? $o : null;
});
if ($ar) $items[] = ['id' => 'ar', 'pais' => 'Argentina', 'mon' => '$ AR', 'tipo' => 'Oficial (Banco Nación) y paralelo (blue), venta', 'oficial' => $ar['oficial'], 'blue' => $ar['blue'] ?? null,
  'fecha_valor' => $ar['oficial']['fecha'], 'fuente' => 'DolarApi (cotizaciones del mercado argentino)', 'url' => 'https://dolarapi.com/', 'consultado' => $ar['consultado'], 'sin_actualizar' => $ar['sin_actualizar']];

// Brasil y euro · mercado (tipo de cambio comercial)
$mk = fuente('mk', 1800, function () {
  $m = json_decode(g('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-USD') ?: 'null', true);
  return (is_array($m) && isset($m['USDBRL'])) ? ['brl' => ['v' => (float)$m['USDBRL']['ask'], 'pct' => (float)$m['USDBRL']['pctChange'], 'fecha' => $m['USDBRL']['create_date']],
    'eur' => isset($m['EURUSD']) ? ['v' => 1 / (float)$m['EURUSD']['bid'], 'pct' => -(float)$m['EURUSD']['pctChange'], 'fecha' => $m['EURUSD']['create_date']] : null] : null;
});
if ($mk) {
  $items[] = ['id' => 'br', 'pais' => 'Brasil', 'mon' => 'R$', 'tipo' => 'Dólar comercial (mercado), venta', 'v' => $mk['brl']['v'], 'pct' => $mk['brl']['pct'], 'fecha_valor' => str_replace(' ', 'T', $mk['brl']['fecha']) . '-03:00', 'fuente' => 'AwesomeAPI (mercado de cambios)', 'url' => 'https://economia.awesomeapi.com.br/', 'consultado' => $mk['consultado'], 'sin_actualizar' => $mk['sin_actualizar']];
  if ($mk['eur']) $items[] = ['id' => 'eu', 'pais' => 'Euro', 'mon' => '€', 'tipo' => 'Mercado internacional', 'v' => $mk['eur']['v'], 'pct' => $mk['eur']['pct'], 'fecha_valor' => str_replace(' ', 'T', $mk['eur']['fecha']) . '-03:00', 'fuente' => 'AwesomeAPI (mercado de cambios)', 'url' => 'https://economia.awesomeapi.com.br/', 'consultado' => $mk['consultado'], 'sin_actualizar' => $mk['sin_actualizar']];
}

// Chile · dólar observado del Banco Central de Chile (publicado vía mindicador.cl)
$cl = fuente('cl', 3600, function () {
  $c = json_decode(g('https://mindicador.cl/api/dolar') ?: 'null', true);
  return !empty($c['serie'][0]['valor']) ? ['v' => (float)$c['serie'][0]['valor'], 'prev' => (float)($c['serie'][1]['valor'] ?? 0), 'fecha_valor' => substr($c['serie'][0]['fecha'], 0, 10)] : null;
});
if ($cl) $items[] = $cl + ['id' => 'cl', 'pais' => 'Chile', 'mon' => '$ CL', 'tipo' => 'Dólar observado (oficial)', 'fuente' => 'Banco Central de Chile, vía mindicador.cl', 'url' => 'https://www.bcentral.cl/'];

// Uruguay · Altercambio (compra / venta)
$uy = fuente('uy', 3600, function () {
  $h = g('https://altercambio.com.uy/', true); if (!$h) return null;
  if (preg_match('/Dolar USA[\s|]*([\d]+[.,]\d{2})[\s|]*([\d]+[.,]\d{2})/iu', txt($h), $m)) { $c = (float)str_replace(',', '.', $m[1]); $v = (float)str_replace(',', '.', $m[2]);
    if ($c > 20 && $c < 80 && $v >= $c && $v < 80) return ['compra' => $c, 'venta' => $v]; }
  return null;
});
if ($uy) $items[] = $uy + ['id' => 'uy', 'pais' => 'Uruguay', 'mon' => '$ UY', 'tipo' => 'Casa de cambio, compra y venta', 'fuente' => 'Altercambio', 'url' => 'https://altercambio.com.uy/', 'fecha_valor' => 'vigente al momento de la consulta'];

// Bolivia · Banco Central de Bolivia, tipo de cambio oficial
$bo = fuente('bo', 6 * 3600, function () {
  $h = g('https://www.bcb.gob.bo/', true); if (!$h) return null;
  if (preg_match('/Tipo de cambio oficial.{0,120}?VIGENTE PARA (.{5,80}?\d{4}).{0,40}?(\d{1,2},\d{2})/iu', txt($h), $m)) return ['v' => (float)str_replace(',', '.', $m[2]), 'fecha_valor' => 'vigente para ' . mb_strtolower(trim($m[1]))];
  return null;
});
if ($bo) $items[] = $bo + ['id' => 'bo', 'pais' => 'Bolivia', 'mon' => 'Bs', 'tipo' => 'Tipo de cambio oficial', 'fuente' => 'Banco Central de Bolivia', 'url' => 'https://www.bcb.gob.bo/'];

// Perú · Kambista (compra / venta)
$pe = fuente('pe', 3600, function () {
  $h = g('https://kambista.com/', true); if (!$h) return null; $t = txt($h);
  if (preg_match('/Compra[^0-9]{0,40}(\d\.\d{2,4})/iu', $t, $a) && preg_match('/Venta[^0-9]{0,40}(\d\.\d{2,4})/iu', $t, $b)) { $c = (float)$a[1]; $v = (float)$b[1];
    if ($c > 2 && $c < 6 && $v >= $c && $v < 6) return ['compra' => $c, 'venta' => $v]; }
  return null;
});
if ($pe) $items[] = $pe + ['id' => 'pe', 'pais' => 'Perú', 'mon' => 'S/', 'tipo' => 'Casa de cambio online, compra y venta', 'fuente' => 'Kambista', 'url' => 'https://kambista.com/', 'fecha_valor' => 'vigente al momento de la consulta'];

// Petróleo · precios de contado (spot) publicados por la EIA de EE. UU.
$eia = fuente('eia', 6 * 3600, function () {
  $h = g('https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm', true); if (!$h) return null; $fechas = []; $res = [];
  foreach (preg_split('#<tr#i', $h) as $tr) {
    $t = ltrim(trim(preg_replace('/\s+/', ' ', html_entity_decode(strip_tags(str_replace(['</td>', '</th>'], ' | ', $tr))))), '> |');
    if (!$fechas && preg_match_all('#\b(\d{2}/\d{2}/\d{2})\b#', $t, $m) && count($m[1]) >= 3) $fechas = $m[1];
    foreach (['wti' => 'WTI - Cushing', 'brent' => 'Brent - Europe'] as $k => $lab)
      if (!isset($res[$k]) && stripos($t, $lab) === 0 && preg_match_all('#\|\s*([\d]+\.[\d]+)#', $t, $v)) $res[$k] = array_map('floatval', $v[1]);
  }
  if (!$res || !$fechas) return null;
  $o = []; foreach ($res as $k => $vals) { $n = count($vals); $fd = $fechas[min($n, count($fechas)) - 1];
    $o[$k] = ['v' => $vals[$n - 1], 'prev' => $n > 1 ? $vals[$n - 2] : 0, 'fecha_valor' => '20' . substr($fd, 6, 2) . '-' . substr($fd, 0, 2) . '-' . substr($fd, 3, 2)]; }
  return $o;
});
if ($eia) foreach (['brent' => ['Brent', 'Brent, Europa'], 'wti' => ['WTI', 'WTI, Cushing (Oklahoma)']] as $k => $nm) if (isset($eia[$k]))
  $items[] = $eia[$k] + ['id' => $k, 'pais' => 'Petróleo ' . $nm[0], 'mon' => 'US$', 'unidad' => 'barril', 'tipo' => 'Precio de contado (spot) ' . $nm[1] . ', no futuros. Publicación semanal', 'fuente' => 'EIA, Administración de Información Energética de EE. UU.', 'url' => 'https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm', 'consultado' => $eia['consultado'], 'sin_actualizar' => $eia['sin_actualizar']];

$js = json_encode(['generado' => date('c'), 'items' => $items], JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $js);
echo $js;
