<?php
// autor.php · se sirve como /autor/<slug>: página de cada firma con sus notas publicadas
require __DIR__ . '/notas-lib.php';
$slug = isset($_GET['a']) ? preg_replace('/[^a-z0-9\-]/', '', strtolower($_GET['a'])) : '';
$ns = array_filter(notas_todas(), function ($n) use ($slug) {
  return ($n['estado'] ?? '') === 'publicada' && autor_slug($n['autor'] ?? '') === $slug;
});
if ($slug === '' || !$ns) { http_response_code(404); header('Content-Type: text/html; charset=utf-8'); echo '<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><title>No encontrado</title><p>No encontramos esa página. <a href="/">Volver a la portada</a></p>'; exit; }
usort($ns, function ($a, $b) { return strcmp($b['fecha'] . ($b['hora'] ?? ''), $a['fecha'] . ($a['hora'] ?? '')); });
$first = reset($ns); $au = autor_info($first['autor'] ?? ''); $red = ($slug === 'redaccion');
$e = function ($s) { return htmlspecialchars(strip_tags((string)$s), ENT_QUOTES, 'UTF-8'); };
$nombre = $au['nombre']; $url = $au['url']; $cant = count($ns);
$desc = $red
  ? 'Notas firmadas por la redacción de Energías LATAM: combustibles, estaciones de servicio y energía en Paraguay y la región.'
  : 'Notas de ' . $nombre . ' en Energías LATAM: combustibles, estaciones de servicio y energía en Paraguay y la región.';
$M = ['', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
$fecha = function ($f) use ($M) { $p = explode('-', $f); return count($p) === 3 ? ((int)$p[2]) . ' de ' . $M[(int)$p[1]] . ' de ' . $p[0] : $f; };
$ld = ['@context' => 'https://schema.org', '@type' => 'ProfilePage', 'mainEntity' => [
  '@type' => $au['tipo'], 'name' => $nombre, 'url' => $url,
  ] + ($au['tipo'] === 'Person' ? [] : ($red ? ['parentOrganization' => ['@type' => 'NewsMediaOrganization', 'name' => 'Energías LATAM', 'url' => 'https://energiaslatam.com/']] : []))];
header('Content-Type: text/html; charset=utf-8');
header('Cache-Control: public, max-age=300');
?><!doctype html>
<html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title><?= $e($red ? 'Redacción' : $nombre) ?> · Energías LATAM</title>
<meta name="description" content="<?= $e($desc) ?>">
<link rel="canonical" href="<?= $url ?>">
<meta property="og:type" content="profile"><meta property="og:site_name" content="Energías LATAM">
<meta property="og:title" content="<?= $e($nombre) ?> · Energías LATAM"><meta property="og:description" content="<?= $e($desc) ?>">
<meta property="og:url" content="<?= $url ?>"><meta property="og:image" content="https://energiaslatam.com/img/og-energiaslatam.jpg">
<link rel="icon" href="/favicon.ico?v=2" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=2"><link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;600;700&display=swap" rel="stylesheet">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VHN1X44JV1"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-VHN1X44JV1');</script>
<script type="application/ld+json"><?= json_encode($ld, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) ?></script>
<style>
:root{--nv:#0F213D;--gr:#3A963E;--gl:#76C46E;--mu:#4A5B6C;--bg:#EEF2F6}
*{box-sizing:border-box}body{margin:0;background:var(--bg);font-family:Barlow,Arial,sans-serif;color:var(--nv)}
.top{height:6px;background:var(--nv)}.top2{height:4px;background:var(--gr)}
header{background:var(--nv);color:#fff;padding:20px 16px}
.hw{max-width:820px;margin:0 auto;display:flex;align-items:center;gap:14px}.hw img{width:52px;height:52px;border-radius:50%;background:#fff}
.hw a{color:#fff;text-decoration:none}.hw b{font:400 28px/1 'Bebas Neue',sans-serif;letter-spacing:1px}.hw b span{color:var(--gl)}.hw small{display:block;color:#B0C2D4;font-size:12px;letter-spacing:2px;text-transform:uppercase;margin-top:3px}
main{max-width:820px;margin:24px auto;background:#fff;border-radius:8px;padding:32px 28px 36px;box-shadow:0 2px 10px rgba(15,33,61,.06)}
.k{font-size:13px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gr);margin:0 0 4px}
h1{font:400 clamp(38px,6vw,56px)/1 'Bebas Neue',sans-serif;margin:0 0 8px}
.upd{color:var(--mu);font-size:16px;line-height:1.5;margin:0 0 22px}
.n{display:block;padding:16px 0;border-top:1px solid #E3E8EE;text-decoration:none;color:var(--nv)}
.n small{display:block;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--gr)}
.n b{display:block;font-size:20px;line-height:1.3;margin:4px 0}
.n span{display:block;font-size:14px;color:var(--mu)}
.n:hover b{color:#2E7D32}
a{color:#2E7D32}
.ft{text-align:center;color:var(--mu);font-size:14px;padding:0 16px 40px}.ft a{color:var(--nv)}
@media(max-width:560px){main{margin:0;border-radius:0;padding:24px 18px}}
</style></head>
<body><div class="top"></div><div class="top2"></div>
<header><div class="hw"><a href="/"><img src="/logo-latam-v2-512.png" alt="Energías LATAM"></a><a href="/"><b>ENERGÍAS <span>LATAM</span></b><small>De los creadores de Energías Paraguay</small></a></div></header>
<main>
<p class="k"><?= $red ? 'Redacción' : ($au['tipo'] === 'Person' ? 'Firma' : 'Contenido de marca') ?></p>
<h1><?= $e($nombre) ?></h1>
<p class="upd"><?= $red ? 'Notas firmadas por la redacción (NdR) de La Estación del Futuro, la revista de Energías LATAM.' : ($au['tipo'] === 'Person' ? 'Escribe en La Estación del Futuro, la revista de Energías LATAM.' : 'Contenido publicado en La Estación del Futuro, la revista de Energías LATAM.') ?> <?= $cant ?> <?= $cant === 1 ? 'nota publicada' : 'notas publicadas' ?>. Cómo trabajamos: <a href="/politica-editorial">política editorial</a>.</p>
<?php foreach ($ns as $n): ?>
<a class="n" href="/n/<?= $e($n['id']) ?>"><small><?= $e($n['cat'] ?? '') ?></small><b><?= $e($n['titulo']) ?></b><span><?= $e($fecha($n['fecha'])) ?></span></a>
<?php endforeach; ?>
</main>
<p class="ft"><a href="/">← Volver a la portada</a> · <a href="/politica-editorial">Política editorial</a></p>
<script src="/adtrack.js?v=2" defer></script>
</body></html>
