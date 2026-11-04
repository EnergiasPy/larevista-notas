<?php
// sitemap-noticias.php · se sirve como /sitemap-noticias.xml: sitemap para Google Noticias
// (solo notas publicadas en los últimos 2 días, sin contenido patrocinado)
require __DIR__ . '/notas-lib.php';
header('Content-Type: application/xml; charset=utf-8');
date_default_timezone_set('America/Asuncion');
$lim = date('Y-m-d', strtotime('-2 days'));
$ns = array_filter(notas_todas(), function ($n) use ($lim) {
  return ($n['estado'] ?? '') === 'publicada' && ($n['fecha'] ?? '') >= $lim && stripos($n['cat'] ?? '', 'patrocinado') === false;
});
usort($ns, function ($a, $b) { return strcmp($b['fecha'], $a['fecha']); });
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">' . "\n";
foreach ($ns as $n) {
  $t = htmlspecialchars(trim(strip_tags($n['titulo'] ?? '')), ENT_XML1 | ENT_QUOTES, 'UTF-8');
  echo '  <url><loc>https://energiaslatam.com/n/' . htmlspecialchars($n['id'], ENT_XML1) . '</loc><news:news><news:publication><news:name>Energías LATAM</news:name><news:language>es</news:language></news:publication><news:publication_date>' . htmlspecialchars($n['fecha'], ENT_XML1) . '</news:publication_date><news:title>' . $t . '</news:title></news:news></url>' . "\n";
}
echo '</urlset>' . "\n";
