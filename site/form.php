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

$FROM = 'info@energiaslatam.com';
$TIPOS = ['newsletter' => 'Suscripción al newsletter', 'proveedor' => 'Alta en la guía de proveedores', 'preregistro' => 'Pre-registro Foro & Expo 2027'];

// Antispam: campo trampa y tiempo mínimo
if (!empty($_POST['web'])) { echo '{"ok":true}'; exit; }
$t = isset($_POST['t']) ? (int)$_POST['t'] : 0;
if ($t > 0 && (time() * 1000 - $t) < 2500) { echo '{"ok":true}'; exit; }

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
  if (in_array($k, ['tipo', 'web', 't'], true)) continue;
  $v = trim(mb_substr(str_replace(["\r", "\n"], ' ', (string)$v), 0, 500));
  $k = trim(mb_substr(preg_replace('/[^\p{L}\p{N} _\-\/().]/u', '', (string)$k), 0, 60));
  if ($k !== '' && $v !== '') $campos[$k] = $v;
}
if (!$campos) { http_response_code(400); echo '{"ok":false,"error":"vacio"}'; exit; }

$mail = '';
foreach ($campos as $v) { if (filter_var($v, FILTER_VALIDATE_EMAIL)) { $mail = $v; break; } }
if ($tipo === 'newsletter' && !$mail) { http_response_code(400); echo '{"ok":false,"error":"mail"}'; exit; }

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

// Copia en planilla (CSV) por tipo
$csv = $dir . '/' . $tipo . '.csv';
$nuevo = !file_exists($csv);
$fh = @fopen($csv, 'a');
if ($fh) {
  if ($nuevo) fputcsv($fh, array_merge(['fecha'], array_keys($campos)));
  fputcsv($fh, array_merge([$fecha], array_values($campos)));
  fclose($fh);
}
echo json_encode(['ok' => true, 'mail' => $enviado === true]);
