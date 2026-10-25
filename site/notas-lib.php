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
