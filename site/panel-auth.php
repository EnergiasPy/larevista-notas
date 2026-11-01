<?php
/* Acceso con contraseña a los tableros internos (med.php, ir.php).
   - La contraseña se guarda solo como hash en datos/panel.pass (nunca en texto).
   - "Olvidé / crear contraseña" manda un enlace de un solo uso, válido 30 minutos, SIEMPRE a info@energiaslatam.com.
   - La sesión es una cookie firmada de 30 días; al cambiar la contraseña se cierran todas las sesiones.
   Uso: require __DIR__ . '/panel-auth.php'; panel_requiere('Medidor del sitio'); */
if (realpath($_SERVER['SCRIPT_FILENAME'] ?? '') === __FILE__) { http_response_code(404); exit; }

const PANEL_MAIL = 'info@energiaslatam.com';
const PANEL_COOKIE = 'el_panel';
const PANEL_DIAS = 30;

function panel_dir() { $d = __DIR__ . '/datos'; if (!is_dir($d)) { @mkdir($d, 0750); @file_put_contents($d . '/.htaccess', "Require all denied\nDeny from all\n"); } return $d; }
function panel_secreto() { $f = panel_dir() . '/panel.secret'; $s = trim((string)@file_get_contents($f)); if (strlen($s) < 32) { $s = bin2hex(random_bytes(32)); @file_put_contents($f, $s, LOCK_EX); } return $s; }
function panel_hash() { return trim((string)@file_get_contents(panel_dir() . '/panel.pass')); }
function panel_firma($exp) { return hash_hmac('sha256', $exp . '|' . panel_hash(), panel_secreto()); }
function panel_ok() {
  $c = (string)($_COOKIE[PANEL_COOKIE] ?? ''); if (panel_hash() === '' || !preg_match('/^(\d+)\.([a-f0-9]{64})$/', $c, $m)) return false;
  return (int)$m[1] > time() && hash_equals(panel_firma($m[1]), $m[2]);
}
function panel_cookie($valor, $exp) { setcookie(PANEL_COOKIE, $valor, ['expires' => $exp, 'path' => '/', 'secure' => true, 'httponly' => true, 'samesite' => 'Strict']); }
function panel_entrar() { $exp = time() + PANEL_DIAS * 86400; panel_cookie($exp . '.' . panel_firma($exp), $exp); }
function panel_ipk() { return substr(hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . panel_secreto()), 0, 16); } // no se guarda la IP, solo un código
function panel_limite($tipo, $max, $seg, $sumar) {
  $f = panel_dir() . '/panel-limite.json'; $j = json_decode((string)@file_get_contents($f), true) ?: []; $ahora = time();
  foreach ($j as $k => $lista) { $j[$k] = array_values(array_filter($lista, function ($t) use ($ahora) { return $t > $ahora - 86400; })); if (!$j[$k]) unset($j[$k]); }
  $k = $tipo . ':' . ($tipo === 'mail' ? 'todos' : panel_ipk());
  $n = count(array_filter($j[$k] ?? [], function ($t) use ($ahora, $seg) { return $t > $ahora - $seg; }));
  if ($sumar) { $j[$k][] = $ahora; @file_put_contents($f, json_encode($j), LOCK_EX); }
  return $n < $max;
}
function panel_url() { return 'https://' . ($_SERVER['HTTP_HOST'] ?? 'energiaslatam.com') . strtok($_SERVER['REQUEST_URI'] ?? '/', '?'); }

function panel_mail_enlace($tok, $nuevo) {
  $link = panel_url() . '?clave=' . $tok;
  $tit = $nuevo ? 'Crear la contraseña del tablero' : 'Cambiar la contraseña del tablero';
  $html = '<div style="font:16px Arial,sans-serif;color:#0F213D;max-width:520px"><h2 style="font-size:20px">' . $tit . '</h2><p>Alguien pidió ' . ($nuevo ? 'crear' : 'cambiar') . ' la contraseña del tablero interno de energiaslatam.com (' . htmlspecialchars(panel_url()) . ').</p><p><a href="' . htmlspecialchars($link) . '" style="display:inline-block;background:#3A963E;color:#fff;padding:12px 20px;border-radius:6px;text-decoration:none;font-weight:bold">Elegir contraseña</a></p><p style="font-size:13px;color:#4A5B6C">El enlace sirve una sola vez y vence en 30 minutos. Si no fueron ustedes, ignoren este mail: la contraseña actual no cambia.</p></div>';
  $kf = panel_dir() . '/brevo.key'; $key = trim((string)@file_get_contents($kf));
  if ($key !== '') {
    $data = ['sender' => ['name' => 'Energías LATAM', 'email' => PANEL_MAIL], 'to' => [['email' => PANEL_MAIL]], 'subject' => $tit, 'htmlContent' => $html];
    $ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 8, 'ignore_errors' => true, 'header' => "api-key: $key\r\nContent-Type: application/json\r\nAccept: application/json\r\n", 'content' => json_encode($data, JSON_UNESCAPED_UNICODE)]]);
    @file_get_contents('https://api.brevo.com/v3/smtp/email', false, $ctx);
    $code = isset($http_response_header[0]) && preg_match('/\s(\d{3})\s?/', $http_response_header[0], $m) ? (int)$m[1] : 0;
    if ($code >= 200 && $code < 300) return true;
  }
  if (function_exists('mail')) return @mail(PANEL_MAIL, '=?UTF-8?B?' . base64_encode($tit) . '?=', $html, "MIME-Version: 1.0\r\nContent-Type: text/html; charset=UTF-8\r\nFrom: Energías LATAM <" . PANEL_MAIL . ">\r\n", '-f' . PANEL_MAIL);
  return false;
}

function panel_pagina($titulo, $cuerpo) {
  header('Content-Type: text/html; charset=utf-8'); header('Cache-Control: no-store'); header('X-Robots-Tag: noindex'); header('X-Frame-Options: DENY');
  echo '<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>' . htmlspecialchars($titulo) . '</title><style>
body{font:16px Arial,sans-serif;color:#0F213D;background:#F4F6F9;margin:0;padding:16px}.c{max-width:380px;margin:8vh auto;background:#fff;border-radius:10px;padding:24px;box-shadow:0 2px 10px rgba(15,33,61,.08)}
h1{font-size:20px;margin:0 0 6px}p{font-size:14px;color:#4A5B6C;line-height:1.45}label{display:block;font-size:13px;color:#4A5B6C;margin:14px 0 4px}
input{width:100%;box-sizing:border-box;font:16px Arial;padding:10px;border:1px solid #C9D3DE;border-radius:6px}button{width:100%;margin-top:16px;font:bold 16px Arial;padding:12px;border:0;border-radius:6px;background:#3A963E;color:#fff;cursor:pointer}
.l{background:none;color:#0F213D;text-decoration:underline;font:14px Arial;padding:6px;margin-top:10px}.e{background:#FDECEC;color:#8A1C1C;padding:10px;border-radius:6px;font-size:14px}.ok{background:#E8F4E8;color:#1F5E22;padding:10px;border-radius:6px;font-size:14px}
</style><div class="c">' . $cuerpo . '</div>';
  exit;
}

function panel_requiere($titulo) {
  $h = function ($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); };
  $nuevo = panel_hash() === '';
  $acc = (string)($_POST['acc'] ?? '');
  $msg = '';

  if (isset($_GET['salir'])) { panel_cookie('', time() - 3600); header('Location: ' . panel_url(), true, 303); exit; }

  // enlace del mail: elegir contraseña
  $tok = preg_replace('/[^a-f0-9]/', '', (string)($_POST['clave'] ?? $_GET['clave'] ?? ''));
  if ($tok !== '') {
    $tf = panel_dir() . '/panel.reset'; $r = json_decode((string)@file_get_contents($tf), true) ?: [];
    $valido = !empty($r['h']) && ($r['exp'] ?? 0) > time() && hash_equals($r['h'], hash('sha256', $tok));
    if (!$valido) panel_pagina($titulo, '<h1>Enlace vencido</h1><p>Este enlace ya se usó o pasaron más de 30 minutos.</p><p><a href="' . $h(panel_url()) . '">Pedir uno nuevo</a></p>');
    if ($acc === 'nueva') {
      $p1 = (string)($_POST['p1'] ?? ''); $p2 = (string)($_POST['p2'] ?? '');
      if (mb_strlen($p1) < 8) $msg = 'La contraseña tiene que tener al menos 8 caracteres.';
      elseif ($p1 !== $p2) $msg = 'Las dos contraseñas no coinciden.';
      else {
        @file_put_contents(panel_dir() . '/panel.pass', password_hash($p1, PASSWORD_DEFAULT), LOCK_EX);
        @file_put_contents($tf, '{}', LOCK_EX);
        panel_entrar(); header('Location: ' . panel_url(), true, 303); exit;
      }
    }
    panel_pagina($titulo, '<h1>' . ($nuevo ? 'Crear contraseña' : 'Nueva contraseña') . '</h1><p>' . $h($titulo) . ' · energiaslatam.com</p>' . ($msg ? '<p class="e">' . $h($msg) . '</p>' : '') . '<form method="post" autocomplete="off"><input type="hidden" name="acc" value="nueva"><input type="hidden" name="clave" value="' . $h($tok) . '"><label>Contraseña (mínimo 8 caracteres)<input type="password" name="p1" required minlength="8" autocomplete="new-password"></label><label>Repetir contraseña<input type="password" name="p2" required minlength="8" autocomplete="new-password"></label><button>Guardar y entrar</button></form>');
  }

  if ($acc === 'olvide') {
    if (!panel_limite('mail', 1, 120, false) || !panel_limite('mail', 6, 86400, false)) $msg = 'Ya se mandó un enlace hace poco. Revisen ' . PANEL_MAIL . ' (también la carpeta de spam) o esperen 2 minutos.';
    else {
      panel_limite('mail', 1, 120, true);
      $t = bin2hex(random_bytes(24));
      @file_put_contents(panel_dir() . '/panel.reset', json_encode(['h' => hash('sha256', $t), 'exp' => time() + 1800]), LOCK_EX);
      $env = panel_mail_enlace($t, $nuevo);
      panel_pagina($titulo, $env ? '<h1>Revisen el mail</h1><p class="ok">Mandamos un enlace a <b>' . PANEL_MAIL . '</b>. Sirve una vez y vence en 30 minutos. Si no llega en unos minutos, miren en spam.</p><p><a href="' . $h(panel_url()) . '">Volver</a></p>' : '<h1>No se pudo mandar</h1><p class="e">No se pudo mandar el mail. Prueben de nuevo en unos minutos.</p><p><a href="' . $h(panel_url()) . '">Volver</a></p>');
    }
  }

  if (panel_ok()) return;

  if ($acc === 'entrar' && !$nuevo) {
    if (!panel_limite('login', 8, 900, false)) $msg = 'Demasiados intentos. Esperen 15 minutos o usen "Olvidé mi contraseña".';
    elseif (password_verify((string)($_POST['p'] ?? ''), panel_hash())) {
      if (password_needs_rehash(panel_hash(), PASSWORD_DEFAULT)) @file_put_contents(panel_dir() . '/panel.pass', password_hash((string)$_POST['p'], PASSWORD_DEFAULT), LOCK_EX);
      panel_entrar(); header('Location: ' . panel_url(), true, 303); exit;
    } else { panel_limite('login', 8, 900, true); usleep(400000); $msg = 'Contraseña incorrecta.'; }
  }

  http_response_code(401);
  $olv = '<form method="post"><input type="hidden" name="acc" value="olvide"><button class="l">' . ($nuevo ? 'Crear la contraseña (llega un enlace a ' . PANEL_MAIL . ')' : 'Olvidé mi contraseña') . '</button></form>';
  if ($nuevo) panel_pagina($titulo, '<h1>' . $h($titulo) . '</h1><p>Todavía no hay contraseña. Tocá el botón y llega un enlace a <b>' . PANEL_MAIL . '</b> para elegirla.</p>' . ($msg ? '<p class="e">' . $h($msg) . '</p>' : '') . str_replace('class="l"', '', $olv));
  panel_pagina($titulo, '<h1>' . $h($titulo) . '</h1><p>Acceso solo para el equipo de Energías LATAM.</p>' . ($msg ? '<p class="e">' . $h($msg) . '</p>' : '') . '<form method="post"><input type="hidden" name="acc" value="entrar"><label>Contraseña<input type="password" name="p" required autofocus autocomplete="current-password"></label><button>Entrar</button></form>' . $olv);
}
