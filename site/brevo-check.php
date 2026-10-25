<?php
// brevo-check.php · comprueba que la clave de Brevo funcione (no muestra la clave)
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
$kf = __DIR__ . '/datos/brevo.key';
$key = is_file($kf) ? trim(file_get_contents($kf)) : '';
if ($key === '') { echo '{"clave":false,"ok":false}'; exit; }
$ctx = stream_context_create(['http' => ['timeout' => 8, 'ignore_errors' => true, 'header' => "api-key: $key\r\nAccept: application/json\r\n"]]);
$r = @file_get_contents('https://api.brevo.com/v3/contacts/lists/4', false, $ctx);
$code = 0; if (isset($http_response_header[0]) && preg_match('/\s(\d{3})\s?/', $http_response_header[0], $m)) $code = (int)$m[1];
$j = json_decode((string)$r, true);
echo json_encode(['clave' => true, 'ok' => $code === 200, 'codigo' => $code, 'lista' => $j['name'] ?? null, 'suscriptos' => $j['uniqueSubscribers'] ?? ($j['totalSubscribers'] ?? null)], JSON_UNESCAPED_UNICODE);
