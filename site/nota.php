<?php
// nota.php · página propia de cada nota (energiaslatam.com/n/<id>)
// Toma index.html y le pone título, descripción, imagen y link propios de la nota,
// para que Google la indexe sola y WhatsApp/Facebook/LinkedIn muestren su foto al compartir.
require __DIR__ . '/notas-lib.php';

$id = isset($_GET['id']) ? preg_replace('/[^a-z0-9\-]/', '', strtolower($_GET['id'])) : '';
$n = $id ? nota_por_id($id) : null;
if (!$n && $id) { $E = notas_estaticas(); if (isset($E[$id])) $n = $E[$id]; }
if (!$n) { header('Location: /', true, 302); exit; }

$H = @file_get_contents(__DIR__ . '/index.html');
if ($H === false) { header('Location: /#n/' . $id, true, 302); exit; }

$e = function ($s) { return htmlspecialchars(strip_tags((string)$s), ENT_QUOTES, 'UTF-8'); };
$url = 'https://energiaslatam.com/n/' . $id;
$tit = $e($n['titulo']) . ' · La Estación del Futuro';
$des = $e($n['bajada']);
$img = !empty($n['img_abs']) ? $n['img_abs'] : (!empty($n['img']) ? GH_RAW . $n['img'] : 'https://energiaslatam.com/img/og-energiaslatam.jpg');
$est = !empty($n['estatica']);

$rep = [
  '/<title>.*?<\/title>/s' => '<title>' . $tit . '</title>',
  '/<meta name="description" content="[^"]*">/' => '<meta name="description" content="' . $des . '">',
  '/<meta property="og:type" content="[^"]*">/' => '<meta property="og:type" content="article">',
  '/<meta property="og:title" content="[^"]*">/' => '<meta property="og:title" content="' . $e($n['titulo']) . '">',
  '/<meta property="og:description" content="[^"]*">/' => '<meta property="og:description" content="' . $des . '">',
  '/<meta property="og:url" content="[^"]*">/' => '<meta property="og:url" content="' . $url . '">',
  '/<meta property="og:image" content="[^"]*">/' => '<meta property="og:image" content="' . $img . '">',
  '/<meta property="og:image:secure_url" content="[^"]*">/' => '<meta property="og:image:secure_url" content="' . $img . '">',
  '/<meta name="twitter:title" content="[^"]*">/' => '<meta name="twitter:title" content="' . $e($n['titulo']) . '">',
  '/<meta name="twitter:description" content="[^"]*">/' => '<meta name="twitter:description" content="' . $des . '">',
  '/<meta name="twitter:image" content="[^"]*">/' => '<meta name="twitter:image" content="' . $img . '">',
];
foreach ($rep as $re => $to) $H = preg_replace($re, str_replace('$', '\$', $to), $H, 1);
// las medidas de la imagen genérica no aplican a la foto de la nota
$H = preg_replace('/<meta property="og:image:(width|height)" content="[^"]*">\s*/', '', $H);

$ld = [
  '@context' => 'https://schema.org', '@type' => 'NewsArticle',
  'headline' => strip_tags($n['titulo']), 'description' => strip_tags($n['bajada']),
  'image' => [$img], 'datePublished' => $n['fecha'], 'dateModified' => $n['fecha'],
  'author' => ['@type' => ($n['autor'] === 'NdR' ? 'Organization' : 'Person'), 'name' => ($n['autor'] === 'NdR' ? 'La Estación del Futuro' : $n['autor'])],
  'publisher' => ['@type' => 'Organization', 'name' => 'Energías LATAM', 'logo' => ['@type' => 'ImageObject', 'url' => 'https://energiaslatam.com/android-chrome-512x512.png']],
  'mainEntityOfPage' => $url,
];
$head = '<base href="/">' . "\n"
  . '<link rel="canonical" href="' . $url . '">' . "\n"
  . '<meta property="article:published_time" content="' . $e($n['fecha']) . '">' . "\n"
  . ($n['estado'] !== 'publicada' ? '<meta name="robots" content="noindex,nofollow">' . "\n" : '')
  . ($est
      ? '<script>if(!location.hash)history.replaceState(null,"","/n/' . $id . '#nota-' . $id . '");</script>' . "\n"
      : '<script>window.NOTA_ID=' . json_encode($id) . ';</script>' . "\n")
  . '<script type="application/ld+json">' . json_encode($ld, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . '</script>' . "\n";
$H = preg_replace('/<meta charset="utf-8">/', '<meta charset="utf-8">' . "\n" . $head, $H, 1);

// Texto de la nota dentro del HTML (para buscadores); el lector lo reemplaza al cargar
$body = $est ? '' : nota_cuerpo($id);
if ($body !== '') {
  $body = preg_replace('/src="img\//', 'src="' . GH_RAW . 'img/', $body);
  $pre = '<article class="nota" id="pre-nota" style="max-width:760px;margin:24px auto;padding:0 16px"><h1>' . $e($n['titulo']) . '</h1><p class="bajada">' . $des . '</p><p class="byline">Por <b>' . $e($n['autor']) . '</b> · ' . $e($n['fecha']) . '</p><div class="nota-body">' . $body . '</div></article>'
    . '<script>(function(){var p=document.getElementById("pre-nota");if(p)p.remove();})();</script>';
  $H = preg_replace('/<\/body>(?![\s\S]*<\/body>)/', $pre . "\n</body>", $H, 1);
}
header('Content-Type: text/html; charset=utf-8');
header('Cache-Control: public, max-age=300');
echo $H;
