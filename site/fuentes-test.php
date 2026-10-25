<?php
// fuentes-test.php · prueba de acceso a fuentes oficiales de combustibles (temporal)
header('Content-Type: text/plain; charset=utf-8');
function g($u, $n = 600) {
  $ch = curl_init($u);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 40, CURLOPT_CONNECTTIMEOUT => 15, CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_USERAGENT => 'Mozilla/5.0 (EnergiasLATAM datos; +https://energiaslatam.com)']);
  $r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); $e = curl_error($ch); curl_close($ch);
  return [$c, $e, $r === false ? '' : $r];
}
$t = $_GET['t'] ?? 'all';
$out = [];
if ($t === 'all' || $t === 'ar') {
  [$c, $e, $r] = g('https://datos.energia.gob.ar/api/3/action/package_show?id=refinacion-y-comercializacion-de-petroleo-gas-y-derivados-tablas-dinamicas');
  $out[] = "AR energia CKAN: $c $e len=" . strlen($r);
  $j = json_decode($r, true);
  if ($j) foreach ($j['result']['resources'] as $x) $out[] = '  - ' . $x['name'] . ' | ' . basename(parse_url($x['url'], PHP_URL_PATH)) . ' | ' . substr($x['last_modified'] ?? $x['created'] ?? '', 0, 10) . ' | id ' . $x['id'];
  [$c, $e, $r] = g('https://datos.gob.ar/api/3/action/package_search?q=ventas+combustibles+empresa&rows=8');
  $out[] = "AR datos.gob CKAN search: $c $e len=" . strlen($r);
  $j = json_decode($r, true);
  if ($j) foreach ($j['result']['results'] as $p) $out[] = '  * ' . $p['name'] . ' (' . count($p['resources']) . ' rec)';
}
if ($t === 'all' || $t === 'cl') {
  [$c, $e, $r] = g('https://www.sec.cl/venta-mensual-combustibles-liquidos-y-gas-licuado-de-petroleo/');
  $out[] = "CL SEC page: $c $e len=" . strlen($r);
  if (preg_match_all('#https?://[^"\']+\.xlsx#i', $r, $m)) foreach (array_unique($m[0]) as $u) $out[] = '  - ' . basename(parse_url($u, PHP_URL_PATH)) . ' @ ' . dirname(parse_url($u, PHP_URL_PATH));
}
if ($t === 'all' || $t === 'uy') {
  [$c, $e, $r] = g('https://catalogodatos.gub.uy/api/3/action/package_show?id=ancap-cantidad-ventas-combustibles');
  $out[] = "UY Ancap CKAN: $c $e len=" . strlen($r);
  $j = json_decode($r, true);
  if ($j) foreach ($j['result']['resources'] as $x) $out[] = '  - ' . $x['name'] . ' | ' . substr($x['last_modified'] ?? $x['created'] ?? '', 0, 10);
}
if ($t === 'all' || $t === 'pe') {
  [$c, $e, $r] = g('https://dassem.osinergmin.gob.pe/files/MNHL7-VentasCombustibles.xlsx');
  $out[] = "PE DASSEM xlsx: $c $e len=" . strlen($r) . ' zip=' . (substr($r, 0, 2) === 'PK' ? 'si' : 'no');
}
if ($t === 'all' || $t === 'bo') {
  [$c, $e, $r] = g('https://consulta.ypfb.gob.bo/');
  $out[] = "BO YPFB: $c $e len=" . strlen($r);
  if (preg_match_all('#(fetch|axios\.\w+|url\s*:)\s*\(?\s*[\'"`]([^\'"`]+)#', $r, $m)) foreach (array_unique($m[2]) as $u) $out[] = '  api: ' . $u;
  if (preg_match_all('#<script[^>]+src="([^"]+)"#', $r, $m)) foreach ($m[1] as $u) $out[] = '  js: ' . $u;
}
echo implode("\n", $out), "\n";
