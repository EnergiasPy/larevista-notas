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
