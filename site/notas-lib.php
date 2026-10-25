<?php
// notas-lib.php · lee notas.json y los cuerpos desde GitHub, con caché local de 5 minutos
const GH_RAW = 'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/';
const GH_API = 'https://api.github.com/repos/EnergiasPy/larevista-notas/contents/';
function gh_get($path, $ttl = 300) {
  $dir = __DIR__ . '/datos/cache';
  if (!is_dir($dir)) { @mkdir(__DIR__ . '/datos', 0750); @file_put_contents(__DIR__ . '/datos/.htaccess', "Require all denied\nDeny from all\n"); @mkdir($dir, 0750, true); }
  $f = $dir . '/' . preg_replace('/[^a-z0-9.\-]/i', '_', $path);
  if (is_file($f) && (time() - filemtime($f)) < $ttl) return file_get_contents($f);
  $ctx = stream_context_create(['http' => ['timeout' => 6, 'header' => "User-Agent: energiaslatam\r\nAccept: application/vnd.github.raw\r\n"]]);
  $d = @file_get_contents(GH_API . $path . '?ref=main', false, $ctx);
  if ($d === false) $d = @file_get_contents(GH_RAW . $path . '?t=' . time(), false, stream_context_create(['http' => ['timeout' => 6]]));
  if ($d !== false && $d !== '') { @file_put_contents($f, $d); return $d; }
  return is_file($f) ? file_get_contents($f) : '';
}
function notas_todas() { $j = json_decode(gh_get('notas.json'), true); return is_array($j) ? $j : []; }
function nota_por_id($id) { foreach (notas_todas() as $n) if (($n['id'] ?? '') === $id) return $n; return null; }
function nota_cuerpo($id) { return gh_get('notas/' . $id . '.html', 3600); }

// Notas originales escritas dentro de index.html (section data-view="nota-<slug>")
function notas_estaticas() {
  static $cache = null; if ($cache !== null) return $cache;
  $H = @file_get_contents(__DIR__ . '/index.html'); $cache = [];
  if ($H === false) return $cache;
  $img = [];
  if (preg_match_all('/h:[\'"]#nota-([a-z0-9-]+)[\'"]\s*,\s*img:[\'"]([^\'"]+)[\'"]/', $H, $m, PREG_SET_ORDER)) foreach ($m as $x) $img[$x[1]] = $x[2];
  $MES = ['enero'=>1,'febrero'=>2,'marzo'=>3,'abril'=>4,'mayo'=>5,'junio'=>6,'julio'=>7,'agosto'=>8,'septiembre'=>9,'setiembre'=>9,'octubre'=>10,'noviembre'=>11,'diciembre'=>12];
  if (!preg_match_all('/<section[^>]*data-view="nota-([a-z0-9-]+)"[^>]*>([\s\S]*?)<\/section>/', $H, $S, PREG_SET_ORDER)) return $cache;
  foreach ($S as $s) {
    $slug = $s[1]; $b = $s[2];
    $t = preg_match('/<h1[^>]*>([\s\S]*?)<\/h1>/', $b, $q) ? trim(html_entity_decode(strip_tags($q[1]), ENT_QUOTES, 'UTF-8')) : '';
    if ($t === '') continue;
    $d = preg_match('/<p[^>]*class="bajada"[^>]*>([\s\S]*?)<\/p>/', $b, $q) ? trim(html_entity_decode(strip_tags($q[1]), ENT_QUOTES, 'UTF-8')) : '';
    $by = preg_match('/<p[^>]*class="byline"[^>]*>([\s\S]*?)<\/p>/', $b, $q) ? html_entity_decode(strip_tags($q[1]), ENT_QUOTES, 'UTF-8') : '';
    $autor = preg_match('/Por\s+([^·]+)/u', $by, $q) ? trim($q[1]) : 'La Estación del Futuro';
    $fecha = '2026-10-19';
    if (preg_match('/(\d{1,2}) de ([a-záéíóú]+) de (\d{4})/iu', $by, $q) && isset($MES[mb_strtolower($q[2])])) $fecha = sprintf('%04d-%02d-%02d', $q[3], $MES[mb_strtolower($q[2])], $q[1]);
    $cache[$slug] = ['id' => $slug, 'titulo' => $t, 'bajada' => $d, 'autor' => $autor, 'fecha' => $fecha, 'estado' => 'publicada', 'img_abs' => isset($img[$slug]) ? 'https://energiaslatam.com/' . $img[$slug] : '', 'estatica' => true];
  }
  return $cache;
}
