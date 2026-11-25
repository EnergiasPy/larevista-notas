from ads25 import *
im,d=base(k='LA ESTACIÓN DEL FUTURO · NEWSLETTER'); d.text((66,170),'LUNES, JUEVES',font=BB(132),fill=W); d.text((66,298),'Y SÁBADOS',font=BB(132),fill=G); d.text((66,426),'EN TU MAIL',font=BB(132),fill=W)
d.text((66,590),'Las noticias de las estaciones de servicio,',font=B(36),fill=M); d.text((66,636),'tres veces por semana. Gratis.',font=B(36),fill=M)
for i,(dia,t) in enumerate([('LUN','Lunes'),('JUE','Jueves'),('SÁB','Sábado')]):
    x=66+i*322; d.rounded_rectangle([x,730,x+304,960],18,fill=NV2); d.rectangle([x,730,x+304,742],fill=G)
    d.text((x+152,826),dia,font=BB(120),fill=W,anchor='mm'); d.text((x+152,916),t,font=B(32),fill=G,anchor='mm')
d.text((66,1010),'Precios, mercado y qué significa para tu estación.',font=B(34,'Bold'),fill=W)
cta(d,1090,'Sumate gratis'); foot(d); im.save(O+'09-lunes-jueves-sabados.jpg',quality=92)
