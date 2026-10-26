<?php
header('Content-Type: text/plain; charset=utf-8');
$ch=curl_init('https://altercambio.com.uy/');curl_setopt_array($ch,[CURLOPT_RETURNTRANSFER=>true,CURLOPT_TIMEOUT=>25,CURLOPT_FOLLOWLOCATION=>true,CURLOPT_USERAGENT=>'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/130 Safari/537.36',CURLOPT_HTTPHEADER=>['Accept: text/html']]);$h=(string)curl_exec($ch);$c=curl_getinfo($ch,CURLINFO_HTTP_CODE);$e=curl_error($ch);curl_close($ch);
echo "$c $e len ",strlen($h),"\n";$t=preg_replace('/\s+/',' ',html_entity_decode(strip_tags(preg_replace('#<(script|style)[^>]*>.*?</\1>#is',' ',str_replace(['</td>','</div>','</span>','</p>'],' | ',$h)))));
foreach(['Dólar','DÓLAR','Dolar','USD','Compra','Venta'] as $k){$p=0;$n=0;while(($p=strpos($t,$k,$p))!==false&&$n<2){echo "[$k] ",substr($t,max(0,$p-60),220),"\n";$p+=strlen($k);$n++;}}
if(preg_match_all('#["\'](https?://[^"\']*(api|cotiz|rates|json)[^"\']*)#i',$h,$m))echo "LINKS ",implode(' ; ',array_slice(array_unique(array_map(function($u){return preg_replace('/\?.*/','',$u);},$m[1])),0,10)),"\n";
