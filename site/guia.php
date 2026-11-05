<?php
/* Guía de proveedores · administración · energiaslatam.com
   GET  /guia.php?json   → guía completa publicada (la usa el sitio para dibujar la guía)
   GET  /guia.php        → panel con contraseña (panel-auth.php):
                           altas pendientes (desde el formulario del sitio), todas las empresas de la guía,
                           destacada / básica (con fecha de vencimiento), editar, agregar y quitar. */
date_default_timezone_set('America/Asuncion');
$dir = __DIR__ . '/datos';
$fA = $dir . '/guia-aprobados.json';   // guía completa: {"v":2,"items":[...]}
$fD = $dir . '/guia-decisiones.json';  // altas del formulario: clave → aprobado | rechazado | quitado
$G = json_decode((string)@file_get_contents($fA), true) ?: [];
if (!isset($G['v'])) { // primera vez: se importan las empresas que ya estaban en la guía del sitio
  $old = isset($G[0]) ? $G : [];
  $G = ['v' => 2, 'items' => []];
  foreach ((json_decode((string)@file_get_contents($dir . '/guia-import.json'), true) ?: []) as $p) {
    $G['items'][] = ['k' => substr(sha1('imp|' . $p['n']), 0, 12), 'n' => $p['n'], 'ts' => $p['ts'] ?: ['Otro'], 'o' => $p['o'] ?? '', 'z' => $p['z'] ?? 'Paraguay', 'tel' => $p['tel'] ?? '', 'mail' => $p['mail'] ?? '', 'web' => $p['web'] ?? '', 'wa' => $p['wa'] ?? '', 'l' => $p['l'] ?? '', 'f' => !empty($p['f']), 'hasta' => '', 'alta' => 'guía original'];
  }
  foreach ($old as $p) $G['items'][] = ['k' => $p['k'], 'n' => $p['n'], 'ts' => [$p['t'] ?? 'Otro'], 'o' => $p['o'] ?? '', 'z' => $p['z'] ?? 'Paraguay', 'tel' => $p['tel'] ?? '', 'mail' => $p['mail'] ?? '', 'web' => $p['web'] ?? '', 'wa' => '', 'l' => '', 'f' => !empty($p['f']), 'hasta' => '', 'alta' => $p['aprobado'] ?? ''];
  if ($G['items']) @file_put_contents($fA, json_encode($G, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT), LOCK_EX);
}
$Dc = json_decode((string)@file_get_contents($fD), true) ?: [];
$hoy = date('Y-m-d');
$activa = function ($p) use ($hoy) { return !empty($p['f']) && (empty($p['hasta']) || $p['hasta'] >= $hoy); };

if (isset($_GET['json'])) {
  header('Content-Type: application/json; charset=utf-8'); header('Cache-Control: no-cache, max-age=60');
  $out = [];
  foreach ($G['items'] as $p) { $f = $activa($p); $out[] = ['n' => $p['n'], 'ts' => array_values($p['ts']), 'o' => $p['o'], 'z' => $p['z'] ?: 'Paraguay', 'tel' => $p['tel'], 'mail' => $p['mail'], 'web' => $p['web'], 'wa' => $p['wa'], 'l' => $f ? $p['l'] : '', 'f' => $f]; }
  echo json_encode(['completo' => true, 'items' => $out], JSON_UNESCAPED_UNICODE); exit;
}

require __DIR__ . '/panel-auth.php';
panel_requiere('Guía de proveedores');

$TYPES = ['Alimentos y bebidas', 'Automotriz', 'Café', 'Cajas de seguridad', 'Catering', 'Cañerías y productos electromecánicos', 'Cisternas y semirremolques', 'Emblemas', 'Filtros para tanques', 'Iluminación', 'Imagen y señalética', 'Medios de pago', 'Metalmecánica', 'Obras civiles', 'Seguridad vial', 'Surtidores y equipos', 'Tanques', 'Tiendas de conveniencia', 'Venta de materiales', 'Mantenimiento', 'Otro'];
foreach ($G['items'] as $p) foreach ($p['ts'] as $t) if (!in_array($t, $TYPES, true)) $TYPES[] = $t;
$h = function ($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); };
$cl = function ($s, $n = 300) { return mb_substr(trim(preg_replace('/\s+/u', ' ', (string)$s)), 0, $n); };
$guardar = function () use ($fA, $fD, &$G, &$Dc) { file_put_contents($fA, json_encode($G, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT), LOCK_EX); file_put_contents($fD, json_encode($Dc, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT), LOCK_EX); };
$web = function ($u) use ($cl) { $u = $cl($u, 160); if ($u === '') return ''; return preg_match('#^https?://#i', $u) ? $u : 'https://' . $u; };
$ficha = function ($k, $alta) use ($cl, $web) {
  $ts = array_values(array_filter(array_map('trim', preg_split('/[·,;\/]+/u', (string)($_POST['ts'] ?? ''))))); if (!$ts) $ts = ['Otro'];
  $hasta = preg_match('/^\d{4}-\d{2}-\d{2}$/', $_POST['hasta'] ?? '') ? $_POST['hasta'] : '';
  return ['k' => $k, 'n' => $cl($_POST['n'] ?? '', 90), 'ts' => array_slice($ts, 0, 4), 'o' => $cl($_POST['o'] ?? '', 320), 'z' => $cl($_POST['z'] ?? 'Paraguay', 60) ?: 'Paraguay', 'tel' => $cl($_POST['tel'] ?? '', 40), 'mail' => $cl($_POST['mail'] ?? '', 90), 'web' => $web($_POST['web'] ?? ''), 'wa' => preg_replace('/\D/', '', $_POST['wa'] ?? ''), 'l' => $cl($_POST['l'] ?? '', 160), 'f' => !empty($_POST['f']), 'hasta' => $hasta, 'alta' => $alta];
};
$idx = function ($k) use (&$G) { foreach ($G['items'] as $i => $p) if ($p['k'] === $k) return $i; return -1; };

// altas recibidas por el formulario del sitio
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
  if (in_array($acc, ['aprobar', 'guardar', 'nueva'], true)) {
    if ($acc === 'nueva') $k = substr(sha1('man|' . microtime(true) . mt_rand()), 0, 12);
    $i = $idx($k);
    $f = $ficha($k, $i >= 0 ? $G['items'][$i]['alta'] : date('Y-m-d H:i'));
    if ($f['n'] === '') $msg = 'Falta el nombre de la empresa.';
    elseif ($f['f'] && $f['hasta'] !== '' && $f['hasta'] < $hoy) $msg = 'La fecha "destacada hasta" ya pasó: poné una fecha futura o dejala vacía.';
    else {
      if ($i >= 0) $G['items'][$i] = $f; else $G['items'][] = $f;
      if ($acc === 'aprobar') $Dc[$k] = 'aprobado';
      $guardar(); $msg = ($acc === 'guardar' ? 'Cambios guardados: ' : 'Publicada en la guía: ') . $f['n'] . '. Se ve en el sitio en 1 o 2 minutos.';
    }
  } elseif ($acc === 'basica' && ($i = $idx($k)) >= 0) { $G['items'][$i]['f'] = false; $G['items'][$i]['hasta'] = ''; $guardar(); $msg = $G['items'][$i]['n'] . ' pasó a ficha básica (sin logo ni destacado).'; }
  elseif ($acc === 'quitar' && ($i = $idx($k)) >= 0) { $n = $G['items'][$i]['n']; array_splice($G['items'], $i, 1); if (isset($P[$k])) $Dc[$k] = 'quitado'; $guardar(); $msg = $n . ' salió de la guía.'; }
  elseif ($acc === 'rechazar' && $k !== '') { $Dc[$k] = 'rechazado'; $guardar(); $msg = 'Alta rechazada (no se publica).'; }
  elseif ($acc === 'volver' && $k !== '') { unset($Dc[$k]); $guardar(); $msg = 'El alta volvió a pendientes.'; }
}

$pend = array_filter($P, function ($p) use ($Dc) { return !isset($Dc[$p['k']]); }); krsort($pend);
$rech = array_filter($P, function ($p) use ($Dc) { return in_array($Dc[$p['k']] ?? '', ['rechazado', 'quitado'], true); });
$items = $G['items'];
usort($items, function ($a, $b) use ($activa) { return [$activa($b) ? 1 : 0, mb_strtolower($a['n'])] <=> [$activa($a) ? 1 : 0, mb_strtolower($b['n'])]; });
$nDest = count(array_filter($items, $activa));

$form = function ($p, $acc, $boton) use ($h, $TYPES) {
  $o = '<form method="post" class="ed"><input type="hidden" name="k" value="' . $h($p['k'] ?? '') . '"><div class="g">';
  $o .= '<div><label>Empresa</label><input name="n" value="' . $h($p['n'] ?? '') . '" required></div>';
  $o .= '<div><label>Rubros (separados con ·)</label><input name="ts" list="rubros" value="' . $h(implode(' · ', $p['ts'] ?? [])) . '"></div>';
  $o .= '<div><label>Teléfono</label><input name="tel" value="' . $h($p['tel'] ?? '') . '"></div><div><label>WhatsApp (solo números, con 595)</label><input name="wa" value="' . $h($p['wa'] ?? '') . '" placeholder="595981123456"></div>';
  $o .= '<div><label>Mail</label><input name="mail" value="' . $h($p['mail'] ?? '') . '"></div><div><label>Sitio web</label><input name="web" value="' . $h($p['web'] ?? '') . '" placeholder="empresa.com.py"></div>';
  $o .= '<div><label>Zona</label><input name="z" value="' . $h($p['z'] ?? 'Paraguay') . '"></div><div><label>Logo (ruta en el sitio, solo se muestra si es destacada)</label><input name="l" value="' . $h($p['l'] ?? '') . '" placeholder="img/logos/empresa.png"></div></div>';
  $o .= '<label>Qué ofrece</label><textarea name="o">' . $h($p['o'] ?? '') . '</textarea>';
  $o .= '<div class="row dest"><label class="chk"><input type="checkbox" name="f" value="1"' . (!empty($p['f']) ? ' checked' : '') . '> Destacada (plan pago)</label><label class="chk">hasta <input type="date" name="hasta" value="' . $h($p['hasta'] ?? '') . '"></label><span class="sub">Vacía = sin vencimiento. Al vencer pasa sola a básica.</span></div>';
  $o .= '<div class="row"><span style="flex:1"></span>' . $boton . '<button class="ok" name="a" value="' . $acc . '">' . ($acc === 'guardar' ? 'Guardar cambios' : ($acc === 'nueva' ? 'Agregar a la guía' : 'Aprobar y publicar')) . '</button></div></form>';
  return $o;
};

header('Content-Type: text/html; charset=utf-8'); header('Cache-Control: no-store'); header('X-Robots-Tag: noindex');
?><!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Guía de proveedores · admin</title><style>
body{font:15px Arial,sans-serif;max-width:920px;margin:20px auto;padding:0 14px;color:#0F213D;background:#fff}h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:28px 0 10px;border-bottom:2px solid #3A963E;padding-bottom:4px}
.sub{color:#4A5B6C;font-size:13px}.msg{background:#E8F4E8;color:#1F5E22;padding:10px;border-radius:6px}.err{background:#FDECEC;color:#8A1C1C}
.card{border:1px solid #DCE3EA;border-radius:10px;padding:14px;margin:0 0 14px;background:#FAFBFC}.meta{font-size:12px;color:#4A5B6C;margin-bottom:8px}
label{display:block;font-size:12px;color:#4A5B6C;margin:8px 0 3px}input,select,textarea{width:100%;box-sizing:border-box;font:15px Arial;padding:8px;border:1px solid #C9D3DE;border-radius:6px}textarea{min-height:64px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}.row{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;align-items:center}
button{font:bold 14px Arial;padding:9px 14px;border:0;border-radius:6px;cursor:pointer}.ok{background:#3A963E;color:#fff}.no{background:#fff;color:#C0252D;border:1px solid #C0252D}.gr{background:#fff;color:#0F213D;border:1px solid #9FB3C8}
.chk{display:flex;gap:6px;align-items:center;font-size:14px;color:#0F213D;margin:0}.chk input{width:auto}.dest{background:#FFF7E0;padding:8px;border-radius:6px}
details{border:1px solid #DCE3EA;border-radius:10px;margin:0 0 8px;background:#fff}summary{cursor:pointer;padding:10px 12px;display:flex;gap:10px;align-items:center;list-style:none}summary::-webkit-details-marker{display:none}
summary b{flex:1}.tag{font-size:12px;font-weight:bold;padding:3px 8px;border-radius:20px;white-space:nowrap}.td{background:#B8901A;color:#fff}.tb{background:#E3E9F0;color:#4A5B6C}.tv{background:#FDECEC;color:#C0252D}
details .ed{padding:0 12px 12px}.kp{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px 0}.kp div{background:#F4F6F9;border-left:4px solid #3A963E;padding:10px;border-radius:6px}.kp b{display:block;font-size:22px}
@media(max-width:600px){.g{grid-template-columns:1fr}.kp{grid-template-columns:1fr}}
</style><datalist id="rubros"><?php foreach ($TYPES as $t) echo '<option value="' . $h($t) . '">'; ?></datalist>
<p style="float:right;font-size:13px"><a href="/" style="font-weight:bold">← Ir a la revista</a> · <a href="/med.php">Medidor</a> · <a href="/?r=<?= time() ?>#proveedores" target="_blank">Ver la guía</a> · <a href="?salir=1">Salir</a></p>
<h1>Guía de proveedores · admin</h1><p class="sub">Todas las empresas de la guía. Destacada = plan pago: sale primera, con logo, sello y contacto a la vista. Si deja de pagar, tocá "Pasar a básica" (sigue en la guía, sin logo ni destacado) o poné una fecha de vencimiento y baja sola.</p>
<?php if ($msg) echo '<p class="msg' . (strpos($msg, 'Falta') === 0 || strpos($msg, 'La fecha') === 0 ? ' err' : '') . '">' . $h($msg) . '</p>'; ?>
<div class="kp"><div><b><?= count($items) ?></b><span class="sub">empresas en la guía</span></div><div><b><?= $nDest ?></b><span class="sub">destacadas (pagas)</span></div><div><b><?= count($pend) ?></b><span class="sub">inscripciones por aprobar</span></div></div>

<h2>Inscripciones por aprobar (<?= count($pend) ?>)</h2>
<?php if (!$pend) echo '<p class="sub">No hay inscripciones nuevas.</p>';
foreach ($pend as $p) { echo '<div class="card"><div class="meta">Recibida el ' . $h($p['fecha']) . ' desde el formulario del sitio</div>' . $form(['k' => $p['k'], 'n' => $p['n'], 'ts' => [$p['t'] ?: 'Otro'], 'tel' => $p['tel'], 'mail' => $p['mail'], 'o' => $p['o'], 'wa' => preg_replace('/\D/', '', $p['tel']) ? '595' . ltrim(preg_replace('/^595/', '', preg_replace('/\D/', '', $p['tel'])), '0') : ''], 'aprobar', '<button class="no" name="a" value="rechazar" formnovalidate>Rechazar</button>') . '</div>'; } ?>

<h2>Empresas en la guía (<?= count($items) ?>)</h2>
<?php foreach ($items as $p) { $act = $activa($p); $venc = !empty($p['f']) && !$act;
  echo '<details><summary><b>' . $h($p['n']) . '</b><span class="sub">' . $h(implode(' · ', $p['ts'])) . '</span>';
  echo $act ? '<span class="tag td">DESTACADA' . ($p['hasta'] ? ' · hasta ' . $h(date('d/m/Y', strtotime($p['hasta']))) : '') . '</span>' : ($venc ? '<span class="tag tv">VENCIDA · básica</span>' : '<span class="tag tb">Básica</span>');
  echo '</summary>';
  $extra = ($act || $venc ? '<button class="gr" name="a" value="basica" formnovalidate>Pasar a básica</button>' : '') . '<button class="no" name="a" value="quitar" formnovalidate onclick="return confirm(\'¿Sacar a ' . $h(addslashes($p['n'])) . ' de la guía?\')">Quitar de la guía</button>';
  echo $form($p, 'guardar', $extra) . '</details>'; } ?>

<h2>Agregar una empresa a mano</h2>
<details><summary><b>+ Nueva empresa</b></summary><?= $form(['ts' => [], 'z' => 'Paraguay'], 'nueva', '') ?></details>

<?php if ($rech) { ?><h2>Inscripciones rechazadas o quitadas (<?= count($rech) ?>)</h2><?php foreach ($rech as $p) echo '<div class="row"><span style="flex:1">' . $h($p['n']) . ' <span class="sub">' . $h($p['fecha']) . '</span></span><form method="post"><input type="hidden" name="k" value="' . $h($p['k']) . '"><button class="gr" name="a" value="volver">Volver a pendientes</button></form></div>'; } ?>
</html>
