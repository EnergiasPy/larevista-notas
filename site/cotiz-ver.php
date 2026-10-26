<?php
// cotiz-ver.php · prueba temporal de lectura de fuentes oficiales de tipo de cambio
header('Content-Type: text/plain; charset=utf-8');
function g($u){$ch=curl_init($u);curl_setopt_array($ch,[CURLOPT_RETURNTRANSFER=>true,CURLOPT_TIMEOUT=>25,CURLOPT_FOLLOWLOCATION=>true,CURLOPT_USERAGENT=>'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/130 Safari/537.36']);$r=curl_exec($ch);$c=curl_getinfo($ch,CURLINFO_HTTP_CODE);$e=curl_error($ch);curl_close($ch);return [$c,$e,(string)$r];}
$u=['uy'=>'https://www.bcu.gub.uy/Paginas/Default.aspx','cl'=>'https://www.bcentral.cl/es/areas/estadisticas/tipos-de-cambios-y-paridades','cl2'=>'https://www.bcentral.cl/'][$_GET['s']??'uy'];
[$c,$e,$h]=g($u);echo "$c $e len ".strlen($h)."\n";if(strlen($h)<3000){echo substr(strip_tags($h),0,800),"\n";}
$t=preg_replace('/\s+/',' ',html_entity_decode(strip_tags(preg_replace('#<(script|style)[^>]*>.*?</\1>#is',' ',str_replace(['</td>','</th>','</div>','</span>','</p>','</li>'],' | ',$h)))));
foreach(['Dólar','DÓLAR','Dolar','DOLAR','USD','observado','Observado','Cotizaci'] as $k){$p=0;$n=0;while(($p=strpos($t,$k,$p))!==false&&$n<2){echo "[$k] ",substr($t,max(0,$p-80),240),"\n";$p+=strlen($k);$n++;}}
if(preg_match_all('#(https?://[^"\']*(cotiz|Cotiz|api|json)[^"\']*)#',$h,$m))echo "LINKS: ",implode(' ; ',array_slice(array_unique($m[1]),0,12)),"\n";
