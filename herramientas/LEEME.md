# Herramientas de diseño de La Estación del Futuro

Scripts base para que todas las notas salgan con el mismo diseño.

Preparación (los scripts esperan estas rutas):

    mkdir -p /home/claude/chart /home/claude/out
    cp herramientas/* /home/claude/chart/
    pip install matplotlib pillow --break-system-packages

Las tipografías (Bebas Neue, Barlow, Barlow Condensed) están en esta carpeta: registralas con
matplotlib.font_manager.fontManager.addfont(...) si el script no lo hace solo.

- ueno08.py: ejemplo de placa web 1600×1067 (img/<id>-1.jpg) con franja "LA ESTACIÓN DEL FUTURO · energiaslatam.com".
- rentab_carr.py: funciones base del carrusel de Instagram 1080×1350 (base, title, cards, save). ue8_carr.py es un ejemplo completo de 6 placas que las usa.
- story.py: historia 1080×1920 con el formato aprobado (contenido centrado, recuadro verde "LEÉ LA NOTA COMPLETA", mano 👇 centrada y espacio para el sticker de link). Usa mano.png.
- nota_pdf.py: PDF de la nota (usa playwright vía node; ajustá cwd si no existe /home/claude/adtest).

Copiá el ejemplo, cambiá textos y datos, y revisá cada imagen antes de usarla (que no se superpongan ni se corten los textos).
