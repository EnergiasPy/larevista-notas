<?php
// form.php · La Estación del Futuro (energiaslatam.com)
// Recibe newsletter, guía de proveedores y pre-registro; avisa por mail y guarda copia.
header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }

$DEST = ['info@energiasparaguay.com.py', 'info@energiaslatam.com'];
function smtp_local($to_list, $from, $subject, $body, $replyTo) {
  $fp = @fsockopen('127.0.0.1', 25, $en, $es, 8);
  if (!$fp) return 'noconn ' . $es;
  $rd = function () use ($fp) { $d = ''; while (($l = fgets($fp, 515)) !== false) { $d .= $l; if (isset($l[3]) && $l[3] === ' ') break; } return $d; };
  $cmd = function ($c) use ($fp, $rd) { fwrite($fp, $c . "\r\n"); return $rd(); };
  $rd();
  $cmd('EHLO energiaslatam.com');
  $r = $cmd('MAIL FROM:<' . $from . '>'); if (substr($r, 0, 3) !== '250') { fclose($fp); return 'from ' . trim($r); }
  foreach ($to_list as $t) { $r = $cmd('RCPT TO:<' . $t . '>'); if (substr($r, 0, 2) !== '25') { fclose($fp); return 'rcpt ' . trim($r); } }
  $r = $cmd('DATA'); if (substr($r, 0, 3) !== '354') { fclose($fp); return 'data ' . trim($r); }
  $msg = "From: La Estacion del Futuro <$from>\r\nTo: " . implode(', ', $to_list) . "\r\nSubject: $subject\r\nDate: " . date('r') . "\r\nMessage-ID: <" . uniqid('', true) . "@energiaslatam.com>\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";
  if ($replyTo) $msg .= "Reply-To: $replyTo\r\n";
  $msg .= "\r\n" . str_replace("\n.", "\n..", str_replace(["\r\n", "\n"], ["\n", "\r\n"], $body));
  $r = $cmd($msg . "\r\n."); $cmd('QUIT'); fclose($fp);
  return substr($r, 0, 3) === '250' ? true : 'end ' . trim($r);
}

// Alta automática en Brevo (lista "Newsletter La Estación del Futuro" #4).
// La clave se guarda en datos/brevo.key (carpeta protegida); si no está, se omite.
const BREVO_LISTA = 4;
function brevo_alta($email, $campos) {
  $kf = __DIR__ . '/datos/brevo.key';
  $key = is_file($kf) ? trim(file_get_contents($kf)) : '';
  if ($key === '') return 'sin-clave';
  $attr = [];
  foreach ($campos as $k => $v) {
    if (preg_match('/^nombre/iu', $k) && !isset($attr['FIRSTNAME'])) $attr['FIRSTNAME'] = $v;
    elseif (preg_match('/empresa|estaci/iu', $k) && !isset($attr['COMPANY'])) $attr['COMPANY'] = $v;
  }
  $call = function ($data) use ($key) {
    $ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 8, 'ignore_errors' => true,
      'header' => "api-key: $key\r\nContent-Type: application/json\r\nAccept: application/json\r\n",
      'content' => json_encode($data, JSON_UNESCAPED_UNICODE)]]);
    $r = @file_get_contents('https://api.brevo.com/v3/contacts', false, $ctx);
    $code = 0; if (isset($http_response_header[0]) && preg_match('/\s(\d{3})\s?/', $http_response_header[0], $m)) $code = (int)$m[1];
    return [$code, (string)$r];
  };
  $base = ['email' => $email, 'listIds' => [BREVO_LISTA], 'updateEnabled' => true];
  [$c, $r] = $call($attr ? $base + ['attributes' => $attr] : $base);
  if ($c >= 400 && $attr) [$c, $r] = $call($base); // por si algún atributo no existe
  return ($c >= 200 && $c < 300) ? true : ('brevo ' . $c . ' ' . substr($r, 0, 200));
}

// ¿El mail ya está en la lista del newsletter? (si Brevo no responde, se sigue como alta normal)
function brevo_ya_suscripto($email) {
  $kf = __DIR__ . '/datos/brevo.key';
  $key = is_file($kf) ? trim(file_get_contents($kf)) : '';
  if ($key === '') return false;
  $ctx = stream_context_create(['http' => ['timeout' => 6, 'ignore_errors' => true, 'header' => "api-key: $key\r\nAccept: application/json\r\n"]]);
  $r = @file_get_contents('https://api.brevo.com/v3/contacts/' . rawurlencode($email), false, $ctx);
  $code = 0; if (isset($http_response_header[0]) && preg_match('/\s(\d{3})\s?/', $http_response_header[0], $m)) $code = (int)$m[1];
  if ($code !== 200) return false;
  $j = json_decode((string)$r, true);
  return is_array($j) && empty($j['emailBlacklisted']) && in_array(BREVO_LISTA, $j['listIds'] ?? [], false);
}

// Manda el informe al mail de la persona (Brevo, mail transaccional)
function brevo_informe($email, $nombre) {
  $kf = __DIR__ . '/datos/brevo.key';
  $key = is_file($kf) ? trim(file_get_contents($kf)) : '';
  if ($key === '') return 'sin-clave';
  $u = 'https://energiaslatam.com/combustible/py?informe=1&utm_source=mail_informe&utm_medium=email';
  $hola = $nombre !== '' ? 'Hola ' . htmlspecialchars($nombre, ENT_QUOTES, 'UTF-8') . ',' : 'Hola,';
  $html = '<div style="font-family:Arial,Helvetica,sans-serif;max-width:560px;margin:0 auto;color:#0F213D">'
    . '<div style="background:#0F213D;padding:18px 22px;border-bottom:4px solid #3A963E"><img src="https://energiaslatam.com/logo-latam-v2-512.png" width="44" height="44" alt="" style="vertical-align:middle;border-radius:50%;background:#fff"> '
    . '<span style="color:#fff;font-weight:bold;font-size:18px;vertical-align:middle;margin-left:8px">ENERGÍAS <span style="color:#76C46E">LATAM</span></span></div>'
    . '<div style="padding:24px 22px"><p style="font-size:16px">' . $hola . '</p>'
    . '<p style="font-size:16px;line-height:1.5">Acá tenés el <b>informe del mercado de combustibles de Paraguay</b> con los últimos datos oficiales del MIC: ranking de ventas por emblema, quién creció, precios por emblema y producto, red de estaciones y GLP.</p>'
    . '<p style="text-align:center;margin:28px 0"><a href="' . $u . '" style="background:#3A963E;color:#fff;text-decoration:none;font-weight:bold;font-size:16px;padding:14px 26px;border-radius:8px;display:inline-block">Descargar el informe (PDF)</a></p>'
    . '<p style="font-size:14px;color:#24384F;line-height:1.5">Al abrir el enlace se arma y se descarga el PDF con el último mes publicado. Todos los lunes te llega además La Estación del Futuro, el newsletter del sector; te podés dar de baja cuando quieras.</p>'
    . '<p style="font-size:14px"><a href="https://energiaslatam.com/?utm_source=mail_informe&utm_medium=email" style="color:#2E7D32;font-weight:bold">energiaslatam.com</a> · info@energiaslatam.com</p></div></div>';
  $data = ['sender' => ['name' => 'Energías LATAM', 'email' => 'info@energiaslatam.com'], 'to' => [['email' => $email]], 'replyTo' => ['email' => 'info@energiaslatam.com'],
    'subject' => 'Tu informe del mercado de combustibles · Paraguay', 'htmlContent' => $html, 'tags' => ['informe-mic']];
  $ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 8, 'ignore_errors' => true,
    'header' => "api-key: $key\r\nContent-Type: application/json\r\nAccept: application/json\r\n", 'content' => json_encode($data, JSON_UNESCAPED_UNICODE)]]);
  $r = @file_get_contents('https://api.brevo.com/v3/smtp/email', false, $ctx);
  $code = 0; if (isset($http_response_header[0]) && preg_match('/\s(\d{3})\s?/', $http_response_header[0], $m)) $code = (int)$m[1];
  return ($code >= 200 && $code < 300) ? true : ('informe ' . $code . ' ' . substr((string)$r, 0, 200));
}

$FROM = 'info@energiaslatam.com';
$TIPOS = ['newsletter' => 'Suscripción al newsletter', 'proveedor' => 'Alta en la guía de proveedores', 'preregistro' => 'Pre-registro Foro & Expo 2027', 'informe' => 'Descarga del informe mensual del MIC'];

// Antispam: campo trampa y tiempo mínimo
// Antispam: campo trampa y tiempo que tardó en completar (medido en el propio navegador).
// Lo descartado queda anotado en datos/descartes.log para poder recuperarlo.
$descartar = function ($motivo) {
  $d = __DIR__ . '/datos'; if (!is_dir($d)) @mkdir($d, 0750);
  $resto = $_POST; unset($resto['hp_x'], $resto['web']);
  @file_put_contents($d . '/descartes.log', date('c') . ' ' . $motivo . ' ' . json_encode($resto, JSON_UNESCAPED_UNICODE) . "\n", FILE_APPEND);
  echo '{"ok":true}'; exit;
};
if (!empty($_POST['hp_x'])) $descartar('trampa');
$el = isset($_POST['el']) ? (int)$_POST['el'] : -1;
if ($el >= 0 && $el < 1200) $descartar('rapido ' . $el . 'ms');

$tipo = isset($_POST['tipo']) && isset($TIPOS[$_POST['tipo']]) ? $_POST['tipo'] : '';
if (!$tipo) { http_response_code(400); echo '{"ok":false,"error":"tipo"}'; exit; }

// Límite simple: 8 envíos por IP cada 10 minutos
$dir = __DIR__ . '/datos';
if (!is_dir($dir)) { @mkdir($dir, 0750); @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }
$ip = $_SERVER['REMOTE_ADDR'] ?? '';
$rl = $dir . '/rl-' . md5($ip) . '.txt';
$hits = array_filter(explode("\n", @file_get_contents($rl) ?: ''), function ($x) { return $x && (time() - (int)$x) < 600; });
if (count($hits) >= 8) { http_response_code(429); echo '{"ok":false,"error":"limite"}'; exit; }
$hits[] = time(); @file_put_contents($rl, implode("\n", $hits));

$campos = [];
foreach ($_POST as $k => $v) {
  if (in_array($k, ['tipo', 'web', 't', 'el', 'hp_x'], true)) continue;
  $v = trim(mb_substr(str_replace(["\r", "\n"], ' ', (string)$v), 0, 500));
  $k = trim(mb_substr(preg_replace('/[^\p{L}\p{N} _\-\/().]/u', '', (string)$k), 0, 60));
  if ($k !== '' && $v !== '') $campos[$k] = $v;
}
if (!$campos) { http_response_code(400); echo '{"ok":false,"error":"vacio"}'; exit; }

$mail = '';
foreach ($campos as $v) { if (filter_var($v, FILTER_VALIDATE_EMAIL)) { $mail = $v; break; } }
if (($tipo === 'newsletter' || $tipo === 'informe') && !$mail) { http_response_code(400); echo '{"ok":false,"error":"mail"}'; exit; }
// Si ya está suscripto, no se repite el alta ni el aviso por mail
if ($tipo === 'newsletter' && brevo_ya_suscripto($mail)) { echo '{"ok":true,"ya":true}'; exit; }

$fecha = date('d/m/Y H:i');
$cuerpo = $TIPOS[$tipo] . " · energiaslatam.com\n" . str_repeat('-', 40) . "\n";
foreach ($campos as $k => $v) $cuerpo .= $k . ': ' . $v . "\n";
$cuerpo .= "\nFecha: " . $fecha . "\n";

$asunto = '=?UTF-8?B?' . base64_encode('[La Estación del Futuro] ' . $TIPOS[$tipo]) . '?=';
$h = "From: La Estacion del Futuro <$FROM>\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\n";
if ($mail) $h .= "Reply-To: $mail\r\n";
if (function_exists('mail')) { $enviado = @mail(implode(', ', $DEST), $asunto, $cuerpo, $h, '-f' . $FROM); }
else { $enviado = smtp_local($DEST, $FROM, $asunto, $cuerpo, $mail); }
if ($enviado !== true) @file_put_contents($dir . '/errores.log', date('c') . ' ' . print_r($enviado, true) . "\n", FILE_APPEND);

$brevo = null;
$informe = null;
if ($tipo === 'informe' && $mail) { $nm = ''; foreach ($campos as $k => $v) if (preg_match('/^nombre/iu', $k)) { $nm = $v; break; } $informe = brevo_informe($mail, $nm); if ($informe !== true) @file_put_contents($dir . '/errores.log', date('c') . ' ' . $informe . "\n", FILE_APPEND); }
if (($tipo === 'newsletter' || $tipo === 'informe') && $mail) { $brevo = brevo_alta($mail, $campos); if ($brevo !== true && $brevo !== 'sin-clave') @file_put_contents($dir . '/errores.log', date('c') . ' ' . $brevo . "\n", FILE_APPEND); }

// Copia en planilla (CSV) por tipo
$csv = $dir . '/' . $tipo . '.csv';
$nuevo = !file_exists($csv);
$fh = @fopen($csv, 'a');
if ($fh) {
  if ($nuevo) fputcsv($fh, array_merge(['fecha'], array_keys($campos)));
  fputcsv($fh, array_merge([$fecha], array_values($campos)));
  fclose($fh);
}
echo json_encode(['ok' => true, 'informe' => $informe === true ? true : ($informe === null ? null : false), 'mail' => $enviado === true, 'brevo' => $brevo === true ? true : ($brevo === null ? null : false)]);
