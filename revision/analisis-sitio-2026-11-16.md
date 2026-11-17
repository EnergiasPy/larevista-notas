# Análisis del sitio energiaslatam.com
Período medido: 26/10 al 16/11/2026 (medidor propio; notas leídas, origen y publicidad se miden desde el 1/11 a la noche).
Pruebas técnicas: 16/11/2026.

## 1. Tráfico

| | |
|---|---|
| Visitantes (suma diaria) | 6.279 |
| Páginas vistas | 10.006 |
| Páginas por visita | 1,6 |
| Notas leídas (30 s o 60 % del texto) | 325 |

Visitantes por día: pico del 2 al 9/11 con 441 por día de promedio; del 10 al 16/11, 200 por día. **Caída del 55 %.**
Las vistas de avisos siguen la misma curva: 2.149 el 8/11 contra 498–583 el 14, 15 y 16/11 (-73 %).

El pico coincide con el salto de seguidores de Instagram (16 a 612 entre el 27/10 y el 5/11), que por volumen no sale de los posteos orgánicos. **Falta confirmar si hubo pauta paga en esas fechas**: sin ese dato no se puede saber si la caída es fin de pauta o pérdida de interés.

## 2. De dónde viene la gente (desde el 1/11)

| Origen | Visitas | % |
|---|---|---|
| Facebook (utm:fb + utm:facebook + facebook) | 2.972 | 62,9 % |
| Instagram (utm:ig + instagram) | 1.260 | 26,7 % |
| instagram/facebook (sin distinguir) | 94 | 2,0 % |
| Directo | 302 | 6,4 % |
| Newsletter (utm:newsletter + utm:brevo) | 58 | 1,2 % |
| Google | 22 | 0,5 % |
| WhatsApp | 13 | 0,3 % |

**91,6 % del tráfico es Meta.** El sitio no tiene canal propio: si Facebook baja el alcance o se corta la pauta, el tráfico se cae.

Dispositivo: celular 96,4 % (4.436), computadora 3,3 %, tablet 0,3 %.

## 3. Qué se lee

- Portada: 4.283 vistas = **42,8 % de todas las páginas vistas**. /newsletter: 1.318 = 13,2 %.
- Notas leídas / visitantes (1 al 16/11): 325 sobre 5.220 = **6,2 %**.
- Tasa de lectura dentro de cada nota: Ueno 206 vistas / 93 leídas (45,1 %); Yambay–APESA 99/53 (53,5 %); biodiésel 30/17 (56,7 %); Ueno devolución 24/16 (66,7 %); Gulf 27/13 (48,1 %).

Conclusión: **la nota no es el problema, la entrada sí.** El que abre una nota la lee (45 a 67 %), pero sólo 1 de cada 16 visitantes abre alguna. El tráfico llega, mira la portada y se va: 1,6 páginas por visita.

## 4. Publicidad

17.448 vistas de avisos, 60 clics, 0,34 % de CTR, 27 anunciantes.

| Nivel | Vistas por anunciante | Clics |
|---|---|---|
| Sponsor (Shell 3.766, Nextar 3.765) | ~3.766 | 19 y 29 (80 % de todos los clics) |
| Oro (6 anunciantes) | 691 a 728 | 0 a 4 |
| Plata (5) | 482 a 530 | 0 a 1 |
| Bronce (12) | 237 a 285 | **0 en los 12** |

Los dos sponsors concentran el 43 % de las vistas. Los 12 bronce suman ~3.200 vistas y **cero clics en 21 días**.

Por ubicación, el CTR es mejor adentro que en la portada:
- Nextar · newsletter: 1,1 % · Nextar · nota: 0,9 % · Shell · nota: 0,8 %
- Shell · portada: 0,4 % · Nextar · portada: 0,7 %

Errores de datos a corregir: "Stein Maq S.A." (503 vistas) y "Stein Maq SA" (5) son el mismo anunciante; igual "Indega S.A." (259) e "Indega SA" (2).

## 5. Clics en el sitio (1.015 en total)

Botón 382 · Interno 375 · Nota 160 · WhatsApp 52 · Suscribirse 23 · Externo 13 · Redes 10.

Lo más clickeado:
- "Quiero recibirlo" 59 + "Suscribirse" 23 = **82 intentos de suscripción** en 21 días.
- /med.php 52 (son nuestros propios clics: hay que excluirlos de la medición).
- #noticias 51, #inicio 45, /combustible 39, /estaciones 33.
- "Escuchar la nota en voz alta" 31 → el audio se usa.
- WhatsApp 52 · "Descargar placa" 15 · "Recibir PDF" 10.
- /apesa.html: 1 clic (por eso movimos el recuadro adentro de la nota de Yambay).

## 6. Estado técnico (medido el 16/11)

Páginas HTML, todas rápidas: portada 834 ms · nota 706 ms · /estaciones 431 ms · /combustible 728 ms · /combustible/py 814 ms · /newsletter 711 ms.

Problemas:

1. **Datos del MIC.** `mic.php` tarda **10,5 s** y devuelve caché del 14/11 08:04. `mic-extra.php` tarda **25,0 s** (en una prueba anterior pasó los 2 minutos sin responder) y devuelve caché del 13/11 17:51. `mic-extra.php` alimenta /combustible (todos los países): eso explica que no cargue. La API del MIC (gis.mic.gov.py) no responde al servidor.
2. **Imágenes sin carga diferida.** Portada: 192 kB de HTML, 142 etiquetas `<img>`, sólo 15 con `loading="lazy"`. Nota: 199 kB, 144 `<img>`, 15 lazy. Con 96,4 % de celular, esto es lo más caro que paga el lector.
3. **SEO sin trabajar.** robots.txt y sitemap.xml están bien (75 URLs, lastmod 16/11), las notas tienen canonical, Open Graph y JSON-LD. Pero Google trae 22 visitas en 22 días (0,5 %) y no hay Search Console dado de alta. La portada no tiene JSON-LD.
4. **Medición contaminada** por los clics propios a /med.php.

## 7. Qué hacer, por orden

**Hoy / esta semana**
1. Arreglar `mic.php` y `mic-extra.php`: servir primero la caché, refrescar en segundo plano, bajar el timeout de 60 a 15 s. El cambio está preparado; falta probarlo juntos y subirlo.
2. Agregar `loading="lazy"` y `width`/`height` a todo lo que no sea la foto principal, en portada y en notas (cambio en el generador, no en cada nota).
3. Excluir /med.php de "Clics en el sitio" y unificar los nombres de Stein Maq e Indega.

**Esta semana**
4. Atacar el 6,2 %: la portada se come el 43 % de las vistas y la gente no baja. Propuesta: bloque "Lo más leído" arriba y 3 notas destacadas con bajada; y que el link de la bio de Instagram vaya a una página con las 3 notas del día, no a la portada entera.
5. Mover los avisos bronce de la portada a la franja dentro de la nota, donde el CTR es el doble (0,8–0,9 % contra 0,4 %). Son 12 anunciantes con cero clics en 21 días.
6. Confirmar si hubo pauta entre el 27/10 y el 9/11, para saber qué fue la caída del 55 %.

**Este mes**
7. Canal propio: hay 82 intentos de suscripción en 21 días y el newsletter trae apenas el 1,2 % del tráfico. Falta medir cuántos de esos 82 terminaron suscriptos y, si el embudo pierde gente, simplificarlo. Un canal de difusión de WhatsApp es el canal propio más natural para este público (52 clics al botón).
8. Dar de alta Search Console y publicar una nota evergreen por semana (precios, mapa de estaciones) para que Google empiece a traer tráfico. Hoy trae 0,5 %.
9. Agregar JSON-LD a la portada.
