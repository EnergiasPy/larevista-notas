<?php
// fuentes-ver.php · inspecciona la estructura de los Excel oficiales (temporal)
header('Content-Type: text/plain; charset=utf-8');
require __DIR__ . '/xlsx-lib.php';
if (!class_exists('ZipArchive')) { echo "sin ZipArchive\n"; exit; }
$t = $_GET['t'] ?? 'cl';
$src = [
  'cl' => 'https://www.sec.cl/sitio-web/wp-content/uploads/2026/10/ESTADISTICAS-DE-VENTAS-CL-ENERO-AGOSTO-2026.xlsx',
  'pe' => 'https://dassem.osinergmin.gob.pe/files/MNHL7-VentasCombustibles.xlsx',
][$t];
$dir = __DIR__ . '/datos/fuentes'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
$f = "$dir/$t.xlsx";
if (!is_file($f) || filemtime($f) < time() - 86400) {
  $ch = curl_init($src); $fp = fopen($f, 'w');
  curl_setopt_array($ch, [CURLOPT_FILE => $fp, CURLOPT_TIMEOUT => 120, CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'Mozilla/5.0 (EnergiasLATAM datos)']);
  curl_exec($ch); curl_close($ch); fclose($fp);
}
echo "size ", filesize($f), "\n";
[$z, $ss, $sheets] = xlsx_sheets($f);
$n = (int)($_GET['n'] ?? 8); $only = $_GET['s'] ?? null;
foreach ($sheets as $name => $p) {
  if ($only !== null && $only !== $name) continue;
  $rows = xlsx_rows($z, $ss, $p, $only !== null ? 0 : $n);
  echo "== HOJA $name (" . ($only !== null ? count($rows) . ' filas' : 'muestra') . ")\n";
  foreach (array_slice($rows, 0, $n) as $r) echo '  ', mb_substr(implode(' | ', $r), 0, 260), "\n";
  if ($only !== null) {
    $c = (int)($_GET['c'] ?? -1);
    if ($c >= 0) { $u = []; foreach ($rows as $r) { $k = $r[$c] ?? ''; $u[$k] = ($u[$k] ?? 0) + 1; } arsort($u); echo "  valores col $c: "; foreach (array_slice($u, 0, 60, true) as $k => $v) echo "$k($v); "; echo "\n"; }
  }
}
