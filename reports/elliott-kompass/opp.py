import json, html
E=html.escape
px=json.load(open('opp_px.json')); usd=px['USDSEK=X']['p']; eur=px['EURSEK=X']['p']
def sv(x,d=1,sign=False):
    s=f"{x:+,.{d}f}" if sign else f"{x:,.{d}f}"; return s.replace(',',' ').replace('.',',').replace('-','−')
# name, yahoo, cur, wave label, wavecls, prob, target, target label, stop, status(now/trigger/hold), trigger text
O=[('Volvo B', 'VOLV-B.ST', 'SEK', 'Slut våg 4', 'w4', 55, 371.5, '371,5 (toppen)', 300.0, 'now', 'Köp i zonen 310–326, gärna i två steg'), ('Meta', 'META', 'USD', 'Våg 4 (sidledes)', 'w4', 45, 626.7, '627 (38 % tillbaka)', 526.0, 'now', 'Köp i delar i zonen 550–561'), ('ASML', 'ASML', 'USD', 'Våg 4, vid 50 %', 'w4', 45, 1542.5, '1 542 (38 % tillbaka)', 1128.0, 'now', 'Köp i delar i zonen 1 190–1 266'), ('Broadcom', 'AVGO', 'USD', 'Våg 4, 50–62 %', 'w4', 45, 364.1, '364 (38 % tillbaka)', 274.0, 'now', 'Köp i delar i zonen 275–314'), ('TSMC', 'TSM', 'USD', 'Våg 4, vid 50 %', 'w4', 45, 382.5, '383 (38 % tillbaka)', 273.0, 'now', 'Köp i delar i zonen 300–319'), ('Alphabet (äger)', 'GOOGL', 'USD', 'Våg 4', 'w4', 45, 317.8, '318 (38 % tillbaka)', 243.0, 'hold', 'Behåll, köp inte mer · stöd 243'), ('Hansa Biopharma (äger)', 'HNSA.ST', 'SEK', 'Start våg 3', 'w3', 55, 67.1, '67,1 (våg 3)', 44.6, 'hold', 'Behåll · FDA 19 dec'), ('Beijer Ref (äger)', 'BEIJ-B.ST', 'SEK', 'Mitt i våg 3', 'w3', 60, 178.6, '178,6 (våg 3)', 155.3, 'hold', 'Behåll · pullback 146–150 är bättre ingång'), ('Elekta', 'EKTA-B.ST', 'SEK', 'Slut våg 2', 'w2', 50, 80.8, '80,8 (våg 3)', 59.0, 'trigger', 'Köp vid stängning > 63,25 · rapport 25 nov'), ('NIBE', 'NIBE-B.ST', 'SEK', 'Slut våg 2', 'w2', 40, 52.0, '52 (våg 3)', 43.1, 'trigger', 'Köp vid stängning > 46,5'), ('Mycronic', 'MYCR.ST', 'SEK', 'Tidig våg 3', 'w3', 50, 364.4, '364,4 (toppen)', 250.0, 'trigger', 'Köp ≤ 285 eller > 313'), ('Prysmian', 'PRY.MI', 'EUR', 'Slut våg 4', 'w4', 50, 131.4, '131,4 (B-toppen)', 97.0, 'trigger', 'Köp först när kursen är tillbaka > 105,6')]
rows=[]
for n,t,cur,wl,wc,pr,tg,tgl,st,status,trig in O:
    p=px[t]['p']; up=(tg/p-1)*100; dn=(st/p-1)*100; rr=up/-dn
    fx=usd if cur=='USD' else eur if cur=='EUR' else 1
    cost10=p*fx*10
    rows.append(dict(n=n,t=t,cur=cur,p=p,wl=wl,wc=wc,pr=pr,tg=tg,tgl=tgl,st=st,up=up,dn=dn,rr=rr,cost=cost10,status=status,trig=trig,ts=px[t]['ts']))
rows.sort(key=lambda r:(r['status']!='now',-(r['rr'] if -r['dn']>=3 else 0)))
# diverging bar chart
W=1000; L=330; Z=560; scale=7.0  # px per %
H=40+len(rows)*46+30
s=[f'<svg viewBox="0 0 {W} {H}" class="opp" role="img" aria-labelledby="ot od"><title id="ot">Möjligheter: uppsida mot nedsida</title><desc id="od">Uppsida till målet och nedsida till stoppnivån i procent för varje aktie, sorterat efter risk/reward.</desc>',f'<rect width="{W}" height="{H}" class="bg"/>']
for v in range(-20,61,10):
    x=Z+v*scale
    s.append(f'<line x1="{x}" x2="{x}" y1="28" y2="{H-24}" class="{"zero" if v==0 else "grid"}"/><text x="{x}" y="{H-8}" class="ax" text-anchor="middle">{"+" if v>0 else ""}{v} %</text>')
s.append(f'<text x="{Z-6}" y="18" class="ax" text-anchor="end">← nedsida till stopp</text><text x="{Z+6}" y="18" class="ax">uppsida till mål →</text>')
for i,r in enumerate(rows):
    y=40+i*46
    st={'now':'Köpläge nu','trigger':'Vänta på signal','hold':'Behåll'}[r['status']]
    s.append(f'<a href="#k-opp-{i}"><text x="12" y="{y+15}" class="on">{E(r["n"])}</text></a><text x="12" y="{y+32}" class="os">{E(r["wl"])} · {r["pr"]} % · {st}</text>')
    up=min(r['up'],60); dn=max(r['dn'],-20)
    s.append(f'<rect x="{Z+dn*scale:.1f}" y="{y+4}" width="{-dn*scale:.1f}" height="26" rx="4" class="bdn"/>')
    s.append(f'<rect x="{Z}" y="{y+4}" width="{up*scale:.1f}" height="26" rx="4" class="bup {r["status"]}"/>')
    s.append(f'<text x="{Z+dn*scale-6:.1f}" y="{y+22}" class="bv" text-anchor="end">{sv(r["dn"],0,True)} %</text>')
    s.append(f'<text x="{Z+up*scale+6:.1f}" y="{y+22}" class="bv">{sv(r["up"],0,True)} %</text>')
    s.append(f'<text x="{W-12}" y="{y+22}" class="rr" text-anchor="end">R/R {(sv(r["rr"],1) if -r["dn"]>=3 else "–")}</text>')
s.append('</svg>')
svg=''.join(s)
tr=''.join(f'''<tr id="k-opp-{i}"><th scope="row">{E(r["n"])}</th><td class="n">{sv(r["p"],2)} {r["cur"]}<span class="sub">{r["ts"]}</span></td><td><span class="chip {r["wc"]}">{E(r["wl"])}</span></td><td class="n">{r["pr"]} %</td>
<td class="n">{E(r["tgl"])}<span class="sub up">{sv(r["up"],1,True)} %</span></td><td class="n">{sv(r["st"],2)}<span class="sub dn">{sv(r["dn"],1,True)} %</span></td><td class="n"><b>{(sv(r["rr"],1) if -r["dn"]>=3 else "– (vid stopp)")}</b></td><td class="n">{sv(r["cost"],0)} kr</td><td>{E(r["trig"])}</td></tr>''' for i,r in enumerate(rows))
sec=f'''<section aria-labelledby="h-opp">
  <span class="eyebrow">Måndag 23 nov kl. 11:30</span>
  <h2 id="h-opp">Möjligheter just nu</h2>
  <p>Varje stapel visar hur mycket aktien kan stiga till sitt Elliott-mål (grönt) och hur mycket den kan falla till stoppnivån (rött). Längst upp: aktier i köpläge nu, sorterade efter risk/reward. Längre ned: aktier som väntar på en köpsignal. Klicka på ett namn för detaljerna.</p>
  <div class="mapbox">{svg}</div>
  <div class="tbl"><table class="ot"><thead><tr><th>Aktie</th><th>Kurs</th><th>Våg</th><th>Sannolikhet</th><th>Mål</th><th>Stopp</th><th>R/R</th><th>10 aktier</th><th>Gör</th></tr></thead><tbody>{tr}</tbody></table></div>
  <p class="small">Måndag 23 nov 2026 kl. 11:30 svensk tid: Stockholm och Milano under handel, USA stängning fredag 20 nov. Booking, Netflix, Morgan Stanley och Uber är borttagna eftersom deras stopp bröts. Valuta: 1 USD = {sv(usd,2)} kr, 1 EUR = {sv(eur,2)} kr. R/R = uppsida delat med nedsida. Mål och stopp kommer enbart från vågstrukturen, inte från analytiker. Procenttalet anger hur sannolikt det är att vågplaceringen stämmer, inte chansen att tjäna pengar.</p>
</section>'''
open('opp_section.html','w').write(sec)
for r in rows: print(r['n'],round(r['p'],2),round(r['up'],1),round(r['dn'],1),round(r['rr'],1),round(r['cost']))
