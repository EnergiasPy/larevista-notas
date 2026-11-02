<?php
/* Guía de proveedores · aprobación de altas · energiaslatam.com
   GET  /guia.php?json   → lista pública de fichas aprobadas (la usa el sitio para sumarlas a la guía)
   GET  /guia.php        → panel con contraseña (panel-auth.php): altas pendientes, aprobar / rechazar / quitar
   Las altas llegan desde el formulario de la guía (form.php → datos/proveedor.csv). */
date_default_timezone_set('America/Asuncion');
$dir = __DIR__ . '/datos';
$fA = $dir . '/guia-aprobados.json';   // fichas publicadas
$fD = $dir . '/guia-decisiones.json';  // clave de cada alta → aprobado | rechazado
$A = json_decode((string)@file_get_contents($fA), true) ?: [];
$Dc = json_decode((string)@file_get_contents($fD), true) ?: [];

if (isset($_GET['json'])) {
  header('Content-Type: application/json; charset=utf-8'); header('Cache-Control: public, max-age=120'); header('Access-Control-Allow-Origin: https://energiaslatam.com');
  $out = [];
  foreach ($A as $p) $out[] = ['n' => $p['n'], 't' => $p['t'], 'o' => $p['o'], 'z' => $p['z'] ?: 'Paraguay', 'tel' => $p['tel'], 'mail' => $p['mail'], 'web' => $p['web'], 'f' => !empty($p['f'])];
  echo json_encode($out, JSON_UNESCAPED_UNICODE); exit;
}

require __DIR__ . '/panel-auth.php';
panel_requiere('Guía de proveedores');

$TYPES = ['Obras civiles', 'Instalaciones eléctricas', 'Tanques y cañerías', 'Surtidores y equipos', 'Imagen y señalética', 'Mantenimiento', 'Sistemas y medios de pago', 'Seguridad y ambiente', 'Tienda de conveniencia', 'Otro'];
$h = function ($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); };
$cl = function ($s, $n = 300) { return mb_substr(trim(preg_replace('/\s+/u', ' ', (string)$s)), 0, $n); };
$guardar = function () use ($fA, $fD, &$A, &$Dc) { file_put_contents($fA, json_encode(array_values($A), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT), LOCK_EX); file_put_contents($fD, json_encode($Dc, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT), LOCK_EX); };

// altas recibidas (planilla del formulario)
$P = [];
$csv = $dir . '/proveedor.csv';
if (is_file($csv) && ($fh = fopen($csv, 'r'))) {
  $cab = fgetcsv($fh);
  while (($r = fgetcsv($fh)) !== false) {
    if (!$cab || count($r) < 2) continue;
    $x = []; foreach ($cab as $i => $c) $x[mb_strtolower(trim($c))] = $r[$i] ?? '';
    $get = function ($claves) use ($x) { foreach ($x as $k => $v) foreach ($claves as $c) if (strpos($k, $c) !== false && $v !== '') return $v; return ''; };
    $p = ['fecha' => $x['fecha'] ?? '', 'n' => $get(['empresa', 'nombre']), 't' => $get(['tipo', 'rubro']), 'tel' => $get(['tel']), 'mail' => $get(['mail', 'correo']), 'o' => $get(['ofrece', 'servicio', 'producto'])];
    $p['k'] = substr(sha1($p['fecha'] . '|' . $p['n'] . '|' . $p['mail']), 0, 12);
    $P[$p['k']] = $p;
  }
  fclose($fh);
}

$msg = '';
if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
  $acc = $_POST['a'] ?? ''; $k = preg_replace('/[^a-f0-9]/', '', $_POST['k'] ?? '');
  if ($acc === 'aprobar' && $k !== '') {
    $f = ['k' => $k, 'n' => $cl($_POST['n'] ?? '', 90), 't' => in_array($_POST['t'] ?? '', $TYPES, true) ? $_POST['t'] : 'Otro', 'o' => $cl($_POST['o'] ?? '', 320), 'z' => $cl($_POST['z'] ?? 'Paraguay', 60), 'tel' => $cl($_POST['tel'] ?? '', 40), 'mail' => $cl($_POST['mail'] ?? '', 90), 'web' => preg_replace('#^https?://#', '', $cl($_POST['web'] ?? '', 120)), 'f' => !empty($_POST['f']), 'aprobado' => date('Y-m-d H:i')];
    if ($f['n'] === '') $msg = 'Falta el nombre de la empresa.';
    else { $A = array_values(array_filter($A, function ($x) use ($k) { return $x['k'] !== $k; })); $A[] = $f; $Dc[$k] = 'aprobado'; $guardar(); $msg = 'Publicada en la guía: ' . $f['n'] . '. Aparece en el sitio en unos 2 minutos.'; }
  } elseif ($acc === 'rechazar' && $k !== '') { $Dc[$k] = 'rechazado'; $guardar(); $msg = 'Alta rechazada (no se publica).'; }
  elseif ($acc === 'quitar' && $k !== '') { $A = array_values(array_filter($A, function ($x) use ($k) { return $x['k'] !== $k; })); $Dc[$k] = 'quitado'; $guardar(); $msg = 'Ficha quitada de la guía.'; }
  elseif ($acc === 'volver' && $k !== '') { unset($Dc[$k]); $guardar(); $msg = 'El alta volvió a pendientes.'; }
}

$pend = array_filter($P, function ($p) use ($Dc) { return !isset($Dc[$p['k']]); });
$rech = array_filter($P, function ($p) use ($Dc) { return in_array($Dc[$p['k']] ?? '', ['rechazado', 'quitado'], true); });
krsort($pend);

header('Content-Type: text/html; charset=utf-8'); header('Cache-Control: no-store'); header('X-Robots-Tag: noindex');
?><!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Guía de proveedores · aprobación</title><style>
body{font:15px Arial,sans-serif;max-width:900px;margin:20px auto;padding:0 14px;color:#0F213D;background:#fff}h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:28px 0 10px;border-bottom:2px solid #3A963E;padding-bottom:4px}
.sub{color:#4A5B6C;font-size:13px}.msg{background:#E8F4E8;color:#1F5E22;padding:10px;border-radius:6px}.card{border:1px solid #DCE3EA;border-radius:10px;padding:14px;margin:0 0 14px;background:#FAFBFC}
.card .meta{font-size:12px;color:#4A5B6C;margin-bottom:8px}label{display:block;font-size:12px;color:#4A5B6C;margin:8px 0 3px}input,select,textarea{width:100%;box-sizing:border-box;font:15px Arial;padding:8px;border:1px solid #C9D3DE;border-radius:6px}
textarea{min-height:70px}.g{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}.row{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;align-items:center}
button{font:bold 14px Arial;padding:9px 14px;border:0;border-radius:6px;cursor:pointer}.ok{background:#3A963E;color:#fff}.no{background:#fff;color:#C0252D;border:1px solid #C0252D}.lnk{background:none;color:#0F213D;text-decoration:underline;padding:4px}
table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:7px;border-bottom:1px solid #E3E9F0;text-align:left;vertical-align:top}th{background:#F4F6F9;font-size:12px;text-transform:uppercase}
.chk{display:flex;gap:6px;align-items:center;font-size:14px;color:#0F213D}.chk input{width:auto}@media(max-width:600px){.g{grid-template-columns:1fr}}
</style>
<p style="float:right;font-size:13px"><a href="/med.php">Medidor</a> · <a href="?salir=1">Salir</a></p>
<h1>Guía de proveedores · aprobación</h1><p class="sub">Las empresas que se inscriben en el sitio quedan acá hasta que las aprobás. Podés corregir los datos antes de publicar. Al aprobar, la ficha aparece en la guía de energiaslatam.com en unos 2 minutos.</p>
<?php if ($msg) echo '<p class="msg">' . $h($msg) . '</p>'; ?>
<h2>Pendientes de aprobación (<?= count($pend) ?>)</h2>
<?php if (!$pend) echo '<p class="sub">No hay altas nuevas.</p>';
foreach ($pend as $p) { ?>
<form method="post" class="card"><input type="hidden" name="k" value="<?= $h($p['k']) ?>">
<div class="meta">Recibida el <?= $h($p['fecha']) ?></div>
<div class="g"><div><label>Empresa</label><input name="n" value="<?= $h($p['n']) ?>" required></div>
<div><label>Rubro</label><select name="t"><?php foreach ($TYPES as $t) echo '<option' . ($t === $p['t'] ? ' selected' : '') . '>' . $h($t) . '</option>'; ?></select></div>
<div><label>Teléfono</label><input name="tel" value="<?= $h($p['tel']) ?>"></div><div><label>Mail</label><input name="mail" value="<?= $h($p['mail']) ?>"></div>
<div><label>Sitio web (opcional)</label><input name="web" placeholder="empresa.com.py"></div><div><label>Zona</label><input name="z" value="Paraguay"></div></div>
<label>Qué ofrece</label><textarea name="o"><?= $h($p['o']) ?></textarea>
<div class="row"><label class="chk"><input type="checkbox" name="f" value="1"> Destacada (plan pago)</label>
<span style="flex:1"></span><button class="no" name="a" value="rechazar" formnovalidate>Rechazar</button><button class="ok" name="a" value="aprobar">Aprobar y publicar</button></div></form>
<?php } ?>
<h2>Publicadas desde este panel (<?= count($A) ?>)</h2>
<?php if (!$A) echo '<p class="sub">Todavía no aprobaste ninguna. (Las 25 empresas que ya estaban en la guía se manejan aparte.)</p>'; else { ?>
<div style="overflow-x:auto"><table><tr><th>Empresa</th><th>Rubro</th><th>Contacto</th><th>Aprobada</th><th></th></tr>
<?php foreach (array_reverse($A) as $p) echo '<tr><td><b>' . $h($p['n']) . '</b>' . (!empty($p['f']) ? ' <span style="color:#B8901A;font-weight:bold">· DESTACADA</span>' : '') . '<br><span class="sub">' . $h($p['o']) . '</span></td><td>' . $h($p['t']) . '</td><td>' . $h($p['tel']) . '<br>' . $h($p['mail']) . '</td><td>' . $h($p['aprobado']) . '</td><td><form method="post"><input type="hidden" name="k" value="' . $h($p['k']) . '"><button class="lnk" name="a" value="quitar" onclick="return confirm(\'¿Quitar esta ficha de la guía?\')">Quitar</button></form></td></tr>'; ?>
</table></div><?php } ?>
<?php if ($rech) { ?><h2>Rechazadas o quitadas (<?= count($rech) ?>)</h2><table><?php foreach ($rech as $p) echo '<tr><td>' . $h($p['n']) . '</td><td class="sub">' . $h($p['fecha']) . '</td><td><form method="post"><input type="hidden" name="k" value="' . $h($p['k']) . '"><button class="lnk" name="a" value="volver">Volver a pendientes</button></form></td></tr>'; ?></table><?php } ?>
</html>
