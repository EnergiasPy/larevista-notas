<?php
// datos-pais.php · ventas oficiales de combustibles normalizadas por país (Chile, Perú)
// Salida: {pais, upd, ent, unidad_origen, prods:{}, rows:[[anio, mes, entidad, producto, litros]]}
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=3600');
require __DIR__ . '/xlsx-lib.php';
$c = $_GET['c'] ?? '';
if (!in_array($c, ['cl', 'pe'], true)) { http_response_code(400); echo '{"error":"pais"}'; exit; }
$dir = __DIR__ . '/datos/fuentes'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$cache = "$dir/$c.json";
if (is_file($cache) && empty($_GET['fresh']) && time() - filemtime($cache) < 12 * 3600) { readfile($cache); exit; }

function bajar($url, $dest) {
  $tmp = $dest . '.tmp'; $fp = fopen($tmp, 'w'); $ch = curl_init($url);
  curl_setopt_array($ch, [CURLOPT_FILE => $fp, CURLOPT_TIMEOUT => 180, CURLOPT_CONNECTTIMEOUT => 20, CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'Mozilla/5.0 (EnergiasLATAM datos; +https://energiaslatam.com)']);
  curl_exec($ch); $code = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch); fclose($fp);
  if ($code === 200 && filesize($tmp) > 1000) { rename($tmp, $dest); return true; }
  @unlink($tmp); return is_file($dest);
}
function texto($url) {
  $ch = curl_init($url);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 40, CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'Mozilla/5.0 (EnergiasLATAM datos)']);
  $r = curl_exec($ch); curl_close($ch); return $r ?: '';
}
$MESES = ['ENERO' => 1, 'FEBRERO' => 2, 'MARZO' => 3, 'ABRIL' => 4, 'MAYO' => 5, 'JUNIO' => 6, 'JULIO' => 7, 'AGOSTO' => 8, 'SEPTIEMBRE' => 9, 'SETIEMBRE' => 9, 'OCTUBRE' => 10, 'NOVIEMBRE' => 11, 'DICIEMBRE' => 12];
$agg = []; $out = null;

if ($c === 'cl') {
  // Chile · SEC: un Excel por año con hoja "Detalle a nivel comunal" (m3)
  $page = texto('https://www.sec.cl/venta-mensual-combustibles-liquidos-y-gas-licuado-de-petroleo/');
  preg_match_all('#https?://[^"\']+/ESTADISTICAS-DE-VENTAS-CL-ENERO-[A-Z]+-(\d{4})\.xlsx#i', $page, $m, PREG_SET_ORDER);
  $porAnio = []; foreach ($m as $x) { $y = (int)$x[1]; if (!isset($porAnio[$y])) $porAnio[$y] = $x[0]; }
  krsort($porAnio); $porAnio = array_slice($porAnio, 0, 3, true);
  foreach ($porAnio as $y => $url) {
    $f = "$dir/cl-$y.xlsx";
    $viejo = !is_file($f) || ($y >= (int)date('Y') - 1 && filemtime($f) < time() - 86400 * 3);
    if ($viejo) bajar($url, $f);
    if (!is_file($f)) continue;
    [$z, $ss, $sheets] = xlsx_sheets($f);
    $p = null; foreach ($sheets as $n => $pp) if (stripos($n, 'comunal') !== false) $p = $pp;
    if (!$p) continue;
    $rows = xlsx_rows($z, $ss, $p); $hdr = null;
    foreach ($rows as $r) {
      if ($hdr === null) { if (in_array('Combustible', array_map('trim', $r), true)) $hdr = array_flip(array_map('trim', $r)); continue; }
      $mes = $MESES[strtoupper(trim($r[$hdr['MES'] ?? 4] ?? ''))] ?? 0; if (!$mes) continue;
      $an = (int)($r[$hdr['AÑO'] ?? 5] ?? $y) ?: $y;
      $reg = trim($r[$hdr['Nombre región'] ?? 1] ?? ''); $prod = trim($r[$hdr['Combustible'] ?? 6] ?? '');
      $v = (float)($r[$hdr['Total de Ventas'] ?? 13] ?? 0) * 1000; // m3 -> litros
      if ($reg === '' || $prod === '' || $v <= 0) continue;
      $k = "$an|$mes|$reg|$prod"; $agg[$k] = ($agg[$k] ?? 0) + $v;
    }
  }
  $out = ['pais' => 'cl', 'ent' => 'Región', 'unidad_origen' => 'm³'];
}

if ($c === 'pe') {
  // Perú · Osinergmin DASSEM: ventas por departamento y producto (galones)
  $f = "$dir/pe.xlsx";
  if (!is_file($f) || filemtime($f) < time() - 86400 * 3) bajar('https://dassem.osinergmin.gob.pe/files/MNHL7-VentasCombustibles.xlsx', $f);
  if (is_file($f)) {
    [$z, $ss, $sheets] = xlsx_sheets($f);
    $rows = xlsx_rows($z, $ss, reset($sheets)); $hdr = null;
    foreach ($rows as $r) {
      if ($hdr === null) { $hdr = array_flip(array_map('trim', $r)); continue; }
      $d = $r[$hdr['FCHA_DESPACHO'] ?? 0] ?? '';
      if (is_numeric($d)) { $ts = ((float)$d - 25569) * 86400; $an = (int)gmdate('Y', (int)$ts); $mes = (int)gmdate('n', (int)$ts); }
      elseif (preg_match('#(\d{4})-(\d{2})#', $d, $mm)) { $an = (int)$mm[1]; $mes = (int)$mm[2]; }
      elseif (preg_match('#\d{1,2}/(\d{1,2})/(\d{4})#', $d, $mm)) { $an = (int)$mm[2]; $mes = (int)$mm[1]; }
      else continue;
      $dep = ucwords(mb_strtolower(trim($r[$hdr['DEPARTAMENTO'] ?? 1] ?? ''), 'UTF-8')); $prod = trim($r[$hdr['EQ_PRODUCTO'] ?? 2] ?? '');
      $v = (float)($r[$hdr['GALONES'] ?? 3] ?? 0) * 3.78541;
      if ($dep === '' || $v <= 0) continue;
      $k = "$an|$mes|$dep|$prod"; $agg[$k] = ($agg[$k] ?? 0) + $v;
    }
  }
  $out = ['pais' => 'pe', 'ent' => 'Departamento', 'unidad_origen' => 'galones'];
}

if (!$agg) { if (is_file($cache)) { readfile($cache); exit; } http_response_code(502); echo '{"error":"fuente"}'; exit; }
$rows = []; $prods = [];
foreach ($agg as $k => $v) { $p = explode('|', $k); $rows[] = [(int)$p[0], (int)$p[1], $p[2], $p[3], round($v)]; $prods[$p[3]] = 1; }
$out['upd'] = date('c'); $out['prods'] = array_keys($prods); $out['rows'] = $rows;
$j = json_encode($out, JSON_UNESCAPED_UNICODE);
file_put_contents($cache, $j);
echo $j;
