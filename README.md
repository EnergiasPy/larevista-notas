# La Estación del Futuro · notas

Contenido de la revista de Energías Paraguay (energiasparaguay.com.py/larevista).

- `notas.json`: índice de notas. `estado`: `borrador` (solo vista previa) o `publicada` (aparece en la revista).
- `notas/<id>.html`: cuerpo de cada nota.
- `img/`: imágenes de las notas.

Flujo: la nota diaria entra como `borrador` → vista previa en
`https://energiasparaguay.com.py/larevista/#nota/<id>` → con el OK se pasa a `publicada`.

## Cambios en el servidor del 19/11/2026 (SEO)
Aplicados por Webuzo con backup `*.bak-20261119.*` en la misma carpeta:
- nota.php, notas-lib.php, sitemap-noticias.php y autor.php: iguales a los de `site/`.
- .htaccess: regla `^autor/([a-z0-9-]+)/?$ autor.php?a=$1` (ver `site/htaccess-rules.txt`).
- index.html (solo en el servidor): título de las notas termina en "· Energías LATAM" y se declara el medio (NewsMediaOrganization + WebSite).
- estaciones.html, combustible.html y newsletter.html: títulos nuevos; newsletter dice "lunes, jueves y sábado". En el servidor combustible.html, newsletter.html y sitemap.php son más nuevos que las copias de `site/`.
- sitemap.php (servidor): suma las páginas de autor.
- nota-v2.php y sitemap-noticias-v2.php: archivos de prueba, neutralizados con respuesta 404.

## Cambios en el servidor del 20/11/2026
Con backup en la misma carpeta (`*.bak-20261120*`):
- form.php y guia.php: iguales a los de `site/` (cada dato del formulario va a su columna; fecha en hora de Paraguay).
- index.html: el campo "Qué ofrece" del alta de proveedores admite hasta 320 caracteres.
- Píxel de Meta 1448149717477443 (cuenta de Energías LATAM, pedido por Paymedia) antes de `</head>` en: index.html, estaciones.html,
  combustible.html, combustible-py.html, pais.html, newsletter.html, suscripto.html, politica-editorial.html, privacidad.html,
  media-kit.html, apesa.html y autor.php. En index.html cuenta además una vista por cada cambio de sección. Sin la parte `<noscript>`.
  Una página nueva tiene que llevar el mismo bloque.
- privacidad.html: menciona el píxel de Meta (sección de datos, proveedores y cookies) y lleva fecha 20/11/2026.

## Cambios en el servidor del 26/11/2026
Con backup en la misma carpeta (`med.php.bak-20261126`):
- med.php: igual al de `site/`. Arregla el conteo de inscriptos al newsletter. El `totalSubscribers` que
  devuelve Brevo YA viene sin los dados de baja y el panel les restaba además `totalBlacklisted`: mostraba
  172 en vez de 177. Ahora los activos se cuentan contacto por contacto sobre la lista #4 y el pie aclara
  la diferencia entre contactos de la lista (182), activos (177), destinatarios de una campaña y entregados.
  La caché `datos/newsletter-cache.json` se regenera sola por el campo `v` (versión 2).
- cotiz.php, cotiz2.php y estaciones.php: iguales a los de `site/`. Suman `X-Robots-Tag: noindex` porque son
  endpoints JSON, no paginas, y Search Console los marcaba como "Rastreada: actualmente sin indexar".
  Webuzo dejo el respaldo con `~` al final del nombre (`cotiz~.php`, `cotiz2~.php`, `estaciones~.php`).
- .htaccess: dos redirecciones 301 para URLs viejas que Google sigue pidiendo, ANTES de las reglas genericas
  de `/n/` y `/autor/`, que llevan `[L]`: `/autor/redaccion-la-estacion-del-futuro` -> `/autor/redaccion` y
  `/nota.html?id=<id>` -> `/n/<id>`. Backup en `.htaccess.bak-20261126`.
- Queda en la carpeta un `med copy 1.php` del 01/11 (10 KB, copia vieja del panel) que conviene borrar.
