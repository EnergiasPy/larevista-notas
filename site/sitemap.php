<?php
// sitemap.php · se sirve como /sitemap.xml: portada + cada nota publicada
require __DIR__ . '/notas-lib.php';
header('Content-Type: application/xml; charset=utf-8');
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n" . '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
echo '  <url><loc>https://energiaslatam.com/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>' . "\n";
foreach (['', '/py', '/cl', '/pe'] as $c) echo '  <url><loc>https://energiaslatam.com/combustible' . $c . '</loc><changefreq>weekly</changefreq><priority>0.9</priority></url>' . "\n";
$ns = array_filter(notas_todas(), function ($n) { return ($n['estado'] ?? '') === 'publicada'; });
$ns = array_merge(array_values($ns), array_values(notas_estaticas()));
usort($ns, function ($a, $b) { return strcmp($b['fecha'], $a['fecha']); });
foreach ($ns as $n) echo '  <url><loc>https://energiaslatam.com/n/' . htmlspecialchars($n['id']) . '</loc><lastmod>' . htmlspecialchars($n['fecha']) . '</lastmod></url>' . "\n";
echo '</urlset>' . "\n";
