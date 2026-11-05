import json, re, sys, html
REPO='/home/claude/larevista-notas/'
T=open(REPO+'site/newsletter-n1-0211.html').read()
N={x['id']:x for x in json.load(open(REPO+'notas.json'))}
e=html.escape
def url(i,c): return f'https://energiaslatam.com/n/{i}?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign={c}'
def img(i): return f'https://raw.githubusercontent.com/EnergiasPy/larevista-notas/main/{N[i]["img"]}'
def cut(s,a,b):
    i=s.index(a); j=s.index(b,i); return i,j
def make(num,kicker,pre,intro,bullets,feat,tamb,mas,extra,cierre,camp,out):
    s=T
    s=s.replace('<title>La Estación del Futuro · N° 1</title>',f'<title>La Estación del Futuro · N° {num}</title>')
    i,j=cut(s,'<div style="display:none;max-height:0;overflow:hidden">','</div>'); s=s[:i]+'<div style="display:none;max-height:0;overflow:hidden">'+e(pre)+s[j:]
    s=s.replace('NEWSLETTER SEMANAL · N° 1 · 26 DE OCTUBRE AL 1 DE NOVIEMBRE 2026',kicker)
    i,j=cut(s,'Esta es la primera edición','</p>'); s=s[:i]+intro+s[j:]
    s=s.replace('LA SEMANA EN 30 SEGUNDOS','LO MÁS IMPORTANTE EN 30 SEGUNDOS')
    a='LO MÁS IMPORTANTE EN 30 SEGUNDOS</b>\n'; i=s.index(a)+len(a); j=s.index('\n</td></tr></table></td></tr>',i)
    s=s[:i]+''.join(f'<div style="margin-top:{8 if k==0 else 6}px">{b}</div>' for k,b in enumerate(bullets))+s[j:]
    s=s.replace('LA NOTA DE LA SEMANA','LA NOTA DESTACADA')
    # destacada
    a='LA NOTA DESTACADA</div></td></tr>\n'; i=s.index(a)+len(a); j=s.index('<tr><td style="height:22px"></td></tr>',i)
    f=N[feat]; U=url(feat,camp)
    s=s[:i]+f'''<tr><td style="padding:16px 28px 6px 28px"><a href="{U}"><img src="{img(feat)}" width="544" alt="" style="display:block;width:100%;height:auto;border:0;border-radius:4px"></a>
<div style="margin-top:12px;font-size:11px;font-weight:bold;letter-spacing:1.5px;color:#3A963E;text-transform:uppercase">{e(f["cat"])}</div>
<a href="{U}" style="display:block;margin-top:4px;font-size:22px;line-height:1.25;font-weight:bold;color:#0F213D;text-decoration:none">{e(f["titulo"])}</a>
<p style="margin:8px 0 14px 0;font-size:15px;line-height:1.55;color:#33475B">{e(f["bajada"])}</p>
<a href="{U}" style="display:inline-block;background:#3A963E;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:12px 22px;border-radius:4px">Leer la nota completa</a></td></tr>
'''+s[j:]
    # también
    s=s.replace('TAMBIÉN ESTA SEMANA','TAMBIÉN EN ESTA EDICIÓN')
    a='TAMBIÉN EN ESTA EDICIÓN</div></td></tr>\n'; i=s.index(a)+len(a); j=s.index('<tr><td style="padding:0 28px 18px 28px"><div style="font-size:12px;font-weight:bold;letter-spacing:2px;color:#0F213D;padding-bottom:6px">',i)
    blk=''
    for t in tamb:
        x=N[t]; U=url(t,camp)
        blk+=f'''<tr><td style="padding:0 28px 18px 28px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
<td width="150" valign="top" style="padding-right:16px"><a href="{U}"><img src="{img(t)}" width="150" alt="" style="display:block;width:150px;height:auto;border:0;border-radius:4px"></a></td>
<td valign="top" style="font-family:Arial,Helvetica,sans-serif"><div style="font-size:11px;font-weight:bold;letter-spacing:1.5px;color:#3A963E;text-transform:uppercase">{e(x["cat"])}</div>
<a href="{U}" style="display:block;margin-top:4px;font-size:17px;line-height:1.3;font-weight:bold;color:#0F213D;text-decoration:none">{e(x["titulo"])}</a>
<a href="{U}" style="display:inline-block;margin-top:6px;font-size:14px;color:#3A963E;font-weight:bold;text-decoration:none">Leer →</a></td></tr></table></td></tr>'''
    s=s[:i]+blk+'\n'+s[j:]
    # más notas
    a='padding-bottom:6px">MÁS NOTAS DE LA SEMANA</div>'; i=s.index(a); j=s.index('</td></tr>',i)
    if mas:
        lst=''.join(f'<div style="padding:7px 0;border-bottom:1px solid #E3E8EE;font-size:15px;line-height:1.35"><a href="{url(m,camp)}" style="color:#0F213D;text-decoration:none"><b style="color:#3A963E;font-size:11px;letter-spacing:1px;text-transform:uppercase">{e(N[m]["cat"])}</b><br>{e(N[m]["titulo"])}</a></div>' for m in mas)
        s=s[:i]+'padding-bottom:6px">MÁS NOTAS</div>'+lst+s[j:]
    else:
        k=s.rindex('<tr>',0,i); s=s[:k]+s[s.index('</td></tr>',i)+len('</td></tr>'):]
    # caja datos
    a='<td style="padding:14px 16px;font-size:15px;line-height:1.5">'; i=s.index(a)+len(a); j=s.index('</td></tr></table></td></tr>',i)
    s=s[:i]+extra+s[j:]
    s=s.replace('Hasta el próximo lunes,',cierre)
    s=s.replace('utm_campaign=n01','utm_campaign='+camp)
    assert 'n01' not in s and 'primera edición' not in s and 'LA SEMANA EN 30' not in s
    open(out,'w').write(s); print('ok',out,len(s))
