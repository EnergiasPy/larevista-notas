from ads25 import *
def chips(d,x0,y,items,maxw=948):
    f=B(30,'SemiBold'); x=x0
    for t in items:
        w=d.textlength(t,font=f)+44
        if x+w>x0+maxw: x=x0; y+=74
        d.rounded_rectangle([x,y,x+w,y+58],29,fill=NV2,outline='#2B4560',width=2); d.text((x+22,y+29),t,font=f,fill=W,anchor='lm'); x+=w+14
    return y+58
# 6 Guía para el dueño de estación
im,d=base(k='LA ESTACIÓN DEL FUTURO · GUÍA DE PROVEEDORES'); d.text((66,170),'TODO PARA',font=BB(120),fill=W); d.text((66,286),'TU ESTACIÓN,',font=BB(120),fill=W); d.text((66,402),'EN UN SOLO LUGAR',font=BB(104),fill=G)
d.text((66,540),'La guía de proveedores del sector, ordenada por rubro.',font=B(34),fill=M)
y=chips(d,66,620,['Surtidores y equipos','Tanques','Imagen y señalética','Obras civiles','Medios de pago','Tiendas de conveniencia','Iluminación','Café','Mantenimiento','Cisternas','Seguridad vial','Emblemas'])
d.text((66,y+50),'Buscá por rubro y contactá directo.',font=B(36,'Bold'),fill=W)
cta(d,y+130,'Ver la guía'); foot(d,t='energiaslatam.com'); d.rectangle([900,1270,1014,1320],fill=NV); im.save(O+'07-guia-proveedores.jpg',quality=92)
# 7 Guía para el proveedor
im,d=base(k='LA ESTACIÓN DEL FUTURO · GUÍA DE PROVEEDORES'); d.text((66,170),'¿LE VENDÉS A',font=BB(120),fill=W); d.text((66,286),'ESTACIONES',font=BB(120),fill=W); d.text((66,402),'DE SERVICIO?',font=BB(120),fill=G)
d.text((66,548),'Sumá tu empresa a la guía de proveedores.',font=B(36),fill=M)
for i,(a,b) in enumerate([('Te encuentran por rubro','20 rubros del sector'),('Te ven quienes deciden la compra','Dueños y operadores de estaciones'),('Mostrás lo que ofrecés','Productos y servicios de tu empresa')]): card(d,66,630+i*128,948,108,a,b)
cta(d,1050,'Sumá tu empresa'); foot(d,t='energiaslatam.com'); d.rectangle([900,1270,1014,1320],fill=NV); im.save(O+'08-guia-sumate.jpg',quality=92)
sh=Image.new('RGB',(864,540)); sh.paste(Image.open(O+'07-guia-proveedores.jpg').resize((432,540)),(0,0)); sh.paste(Image.open(O+'08-guia-sumate.jpg').resize((432,540)),(432,0)); sh.save(O+'rev2.jpg',quality=85)
