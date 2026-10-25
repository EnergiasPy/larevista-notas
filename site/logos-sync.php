<?php
// logos-sync.php · copia los logos de los emblemas al servidor (img/emb/<slug>.png). Correr una vez o al sumar emblemas.
header('Content-Type: text/plain; charset=utf-8');
$dir = __DIR__ . '/img/emb'; if (!is_dir($dir)) @mkdir($dir, 0755, true);
function bajar($u) {
  $ch = curl_init($u);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 40, CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'Mozilla/5.0 (EnergiasLATAM)']);
  $r = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  return ($c === 200 && $r && strlen($r) > 300) ? $r : null;
}
$MIC = ['petropar' => 'PTP', 'copetrol' => 'CPT', 'petrobras' => 'PTBR', 'puma' => 'PUM', 'ecop' => 'ECO', 'petrosur' => 'PSR', 'petrochaco' => 'PCH',
  'petromax' => 'PMX', 'compasa' => 'CPA', 'enex' => 'ENX', 'fuelpar' => 'FLP', 'integral' => 'INT', 'hidronorte' => 'HDN', '3-fronteras' => 'FRT',
  'copeg' => 'CPG', '3mg' => '3MG', 'gas-corona' => 'COR', 'petron' => 'PTN'];
foreach ($MIC as $slug => $code) {
  $b = bajar("https://gis.mic.gov.py/static/img/emb/$code.png") ?: bajar("https://gis.mic.gov.py/static/img/emb/{$code}_64.png");
  echo $slug, ': ', $b ? (file_put_contents("$dir/$slug.png", $b) . ' bytes') : 'no', "\n";
}
// Logos actualizados desde la web de cada empresa (más nuevos que los del registro oficial)
$WEB = ['fuelpar' => 'https://static.wixstatic.com/media/4dc28d_7a54a5c8b69348e59b6f5a4f899355b8~mv2.png',
  'petrobras' => 'https://www.petrobrasdistribucion.com.py/static/img/logo.png'];
foreach ($WEB as $slug => $u) { $b = bajar($u); echo $slug, ' (web): ', $b ? (file_put_contents("$dir/$slug.png", $b) . ' bytes') : 'no', "\n"; }
// Shell: logo propio sin fondo
if (is_file(__DIR__ . '/img/logos/shell.png')) { copy(__DIR__ . '/img/logos/shell.png', "$dir/shell.png"); echo "shell: copiado\n"; }
// Energy: logo desde su web
$h = bajar('https://energygas.com.py/');
if ($h && preg_match_all('#<img[^>]+src="([^"]+)"[^>]*>#i', $h, $m)) {
  foreach ($m[1] as $u) if (stripos($u, 'logo') !== false) { $b = bajar($u); if ($b) { $ext = strtolower(pathinfo(parse_url($u, PHP_URL_PATH), PATHINFO_EXTENSION)); file_put_contents("$dir/energy.$ext", $b); echo "energy: $ext ", strlen($b), " bytes (", basename(parse_url($u, PHP_URL_PATH)), ")\n"; break; } }
} else echo "energy: no\n";
// Recorta márgenes vacíos (blancos o transparentes) para que todos los logos se vean del mismo tamaño
if (function_exists('imagecropauto')) foreach (glob("$dir/*.png") as $f) {
  $im = @imagecreatefrompng($f); if (!$im) continue; imagesavealpha($im, true);
  $c = @imagecropauto($im, IMG_CROP_TRANSPARENT); if ($c) { imagedestroy($im); $im = $c; }
  $c = @imagecropauto($im, IMG_CROP_THRESHOLD, 0.15, 0xFFFFFF); if ($c) { imagedestroy($im); $im = $c; }
  imagesavealpha($im, true); imagepng($im, $f); echo 'recorte ', basename($f), ' ', imagesx($im), 'x', imagesy($im), "\n"; imagedestroy($im);
}
