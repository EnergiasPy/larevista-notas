<?php
header('Content-Type: text/plain; charset=utf-8');
function g($u){$ch=curl_init($u);curl_setopt_array($ch,[CURLOPT_RETURNTRANSFER=>true,CURLOPT_TIMEOUT=>25,CURLOPT_FOLLOWLOCATION=>true,CURLOPT_USERAGENT=>'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/130 Safari/537.36',CURLOPT_HTTPHEADER=>['Accept: application/json, text/html']]);$r=(string)curl_exec($ch);$c=curl_getinfo($ch,CURLINFO_HTTP_CODE);curl_close($ch);return [$c,$r];}
[$c,$h]=g('https://kambista.com/');echo "home $c len ",strlen($h),"\n";
$t=preg_replace('/\s+/',' ',html_entity_decode(strip_tags(preg_replace('#<(script|style)[^>]*>.*?</\1>#is',' ',$h))));
if(preg_match_all('/(Compra|Venta)[^0-9]{0,40}(\d\.\d{2,4})/iu',$t,$m,PREG_SET_ORDER))foreach(array_slice($m,0,4) as $x)echo "TXT ",$x[0],"\n";
if(preg_match_all('#https?://[a-z0-9.-]*kambista[a-z0-9.-]*/[^"\'\s<>)]*#i',$h,$m))echo "URLS ",implode(' ; ',array_slice(array_unique(array_map(function($u){return preg_replace('/\?.*/','',$u);},$m[0])),0,15)),"\n";
foreach(['https://api.kambista.com/v1/exchange/calculates?originCurrency=USD&destinationCurrency=PEN&active=S&amount=1','https://api.kambista.com/v1/exchange/kambista/current'] as $u){[$c2,$r2]=g($u);echo "API $c2 ",substr(preg_replace('/\s+/',' ',$r2),0,300),"\n";}
