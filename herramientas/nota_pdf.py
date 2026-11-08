# Uso: python3 nota_pdf.py <id> [salida.pdf]  → PDF A4 de la nota con el estilo de La Estación del Futuro
import json, sys, subprocess, os, datetime
ID=sys.argv[1]; R='/home/claude/larevista-notas/'
OUT=sys.argv[2] if len(sys.argv)>2 else f'/tmp/claude-0/-home-claude/ba48a484-4b4b-549d-9611-4438eea46fb5/scratchpad/Nota_{ID}.pdf'
n=[x for x in json.load(open(R+'notas.json')) if x['id']==ID][0]
body=open(f'{R}notas/{ID}.html').read().replace('src="img/',f'src="file://{R}img/')
M=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
y,m,d=map(int,n['fecha'].split('-')); fecha=f'{d} de {M[m-1]} de {y}'
F='file:///home/claude/chart/'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Bebas;src:url({F}BebasNeue-Regular.ttf)}}
@font-face{{font-family:Barlow;src:url({F}Barlow-Regular.ttf)}}
@font-face{{font-family:Barlow;font-weight:600;src:url({F}Barlow-SemiBold.ttf)}}
@font-face{{font-family:Barlow;font-weight:700;src:url({F}Barlow-Bold.ttf)}}
body{{font:400 11.5pt/1.55 Barlow,sans-serif;color:#1B2B40}}
.top{{border-top:5px solid #0F213D;padding-top:6px;display:flex;justify-content:space-between;font:400 15pt Bebas;color:#0F213D}} .top b{{color:#3A7D44;font-weight:400}}
.cat{{display:inline-block;margin-top:14px;font:700 9pt Barlow;letter-spacing:1.5px;text-transform:uppercase;color:#3A7D44}}
h1{{font:400 30pt/1.02 Bebas;color:#0F213D;margin:6px 0 8px}}
.bajada{{font-size:13pt;color:#4A5B6C;margin:0 0 6px}}
.by{{font-size:9.5pt;color:#6A7B8C;border-bottom:1px solid #DCE3EA;padding-bottom:10px;margin-bottom:14px}}
h2{{font:400 17pt Bebas;color:#0F213D;margin:16px 0 4px}}
figure{{margin:12px 0;break-inside:avoid}} figure img{{max-width:100%;max-height:82mm;display:block;margin:0 auto;border-radius:4px}} figcaption{{font-size:9pt;color:#6A7B8C;margin-top:4px}}
blockquote{{margin:12px 0;padding:6px 14px;border-left:4px solid #C0252D;font-size:13pt;color:#0F213D}} blockquote cite{{display:block;font-size:9pt;color:#6A7B8C;font-style:normal}}
.datos{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0;break-inside:avoid}}
.datos div{{background:#F0F4F8;border-left:4px solid #3A7D44;padding:8px 10px}} .datos b{{display:block;font:400 20pt Bebas;color:#0F213D}} .datos span{{font-size:9.5pt;color:#4A5B6C}}
.foot{{margin-top:18px;border-top:1px solid #DCE3EA;padding-top:6px;font-size:8.5pt;color:#8A99A8}}
</style></head><body>
<div class="top"><span>LA ESTACIÓN <b>DEL FUTURO</b></span><span style="font:600 9pt Barlow;color:#6A7B8C;align-self:center">energiaslatam.com</span></div>
<span class="cat">{n["cat"]}</span><h1>{n["titulo"]}</h1><p class="bajada">{n["bajada"]}</p>
<p class="by">Por {n["autor"]} · {fecha}</p>
{body}
<p class="foot">La Estación del Futuro · Energías LATAM · energiaslatam.com/n/{ID}</p></body></html>'''
tmp=OUT.replace('.pdf','.html'); open(tmp,'w').write(html)
js=f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://{tmp}');await p.waitForTimeout(800);await p.pdf({{path:'{OUT}',format:'A4',printBackground:true,margin:{{top:'16mm',bottom:'18mm',left:'16mm',right:'16mm'}}}});await b.close();}})()"
subprocess.run(['node','-e',js],check=True,cwd='/home/claude/adtest'); os.remove(tmp); print(OUT)
