<?php
// cotiz-ver.php · prueba temporal de lectura de fuentes oficiales de tipo de cambio
header('Content-Type: text/plain; charset=utf-8');
function g($u){$ch=curl_init($u);curl_setopt_array($ch,[CURLOPT_RETURNTRANSFER=>true,CURLOPT_TIMEOUT=>25,CURLOPT_FOLLOWLOCATION=>true,CURLOPT_SSL_VERIFYPEER=>true,CURLOPT_USERAGENT=>'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/130 Safari/537.36']);$r=curl_exec($ch);$c=curl_getinfo($ch,CURLINFO_HTTP_CODE);$e=curl_error($ch);curl_close($ch);return [$c,$e,(string)$r];}
$u=['bo'=>'https://www.bcb.gob.bo/','pe'=>'https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx','pe2'=>'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04639PD-PD04640PD/json/2026-10-15/2026-10-25'][$_GET['s']??'bo'];
[$c,$e,$h]=g($u);echo "$c $e len ".strlen($h)."\n";if(strlen($h)<3000){echo substr(strip_tags($h),0,1200),"\n";}
$t=preg_replace('/\s+/',' ',html_entity_decode(strip_tags(preg_replace('#<(script|style)[^>]*>.*?</\1>#is',' ',str_replace(['</td>','</th>','</div>','</span>','</p>'],' | ',$h)))));
foreach(['cambio','Cambio','Dólar','DOLAR','Dolar','Compra','Venta','Fecha'] as $k){$p=0;$n=0;while(($p=strpos($t,$k,$p))!==false&&$n<3){echo "[$k] ",substr($t,max(0,$p-80),260),"\n";$p+=strlen($k);$n++;}}
