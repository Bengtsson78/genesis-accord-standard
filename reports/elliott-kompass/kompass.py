import html
E=html.escape
# path points
P={'0':(70,560),'1':(250,360),'2':(360,470),'3':(680,120),'4':(800,290),'5':(980,80),'A':(1100,340),'B':(1170,260),'C':(1290,500)}
seq=['0','1','2','3','4','5','A','B','C']
COL={'1':'w1','2':'w2','3':'w3','4':'w4','5':'w5','A':'wa','B':'wb','C':'wc'}
def pt(seg,t):
    i=seq.index(seg); a=P[seq[i-1]]; b=P[seg]
    return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
SIG={'buy':('Köpläge','sig-buy'),'hold':('Behåll','sig-hold'),'wait':('Avvakta','sig-wait'),'avoid':('Undvik','sig-avoid')}
# name, ticker, price, wave, seg, t, prob, signal, action, levels, why
S=[('Uber', 'UBER', '63,47 USD (20/11, −3,2 %)', 'Räkning bruten', '1', 0.1, 30, 'avoid', 'Stopp utlöst', 'Stängde under stoppet 64 · ny bedömning först över 72,9', 'Stoppet 64 bröts på fredagen.'), ('Constellation', 'CEG', '237,41 USD (20/11, −5,8 %)', 'Slut C / tidig 1', '1', 0.2, 40, 'wait', 'Avvakta, nära stopp', 'Bekräftelse > 309,8 · stopp < 228,6', 'Föll 5,8 % till 237,41, 3,7 % över stoppet 228,6.'), ('Okta', 'OKTA', '191,46 USD (20/11, −7,4 %)', 'Start våg 3', '3', 0.2, 50, 'wait', 'Avvakta', 'Våg 3 bekräftad > 187 · mål 235 / 336 · stopp < 164', 'Föll 7,4 % men håller över 187. Stoppet 164.'), ('Munters', 'MTRS', '130,75 kr (+3,0 % i dag)', 'Våg 2 (alt. C)', '2', 0.76, 45, 'hold', 'Behåll, köp ej fler', 'Bekräftelse > 143,9 · stopp < 123,7', 'Studsar +3,0 % från 126,90. Dubbelbotten 126–127 håller. Bekräftelsen 143,9 saknas.'), ('Booking', 'BKNG', '144,91 USD (20/11, −1,6 %)', 'Räkning bruten', '2', 0.84, 30, 'avoid', 'Stopp utlöst', 'Stängde under gränsen 146,28 · ny bedömning först efter högre botten', 'Vågräkningen blev fel på fredagen. Vänta på en ny botten.'), ('Elekta', 'EKTA B', '61,15 kr (+0,9 % i dag)', 'Slut våg 2', '2', 0.91, 50, 'buy', 'Köp vid utbrott', 'Köpsignal vid stängning > 63,25 · utbrott > 66,70 · stopp < 59 · rapport 25 nov', 'Stiger 0,9 % till 61,15, men under köpsignalen 63,25. Rapport 25 nov.'), ('NIBE', 'NIBE B', '43,64 kr (+0,8 % i dag)', 'Slut våg 2', '2', 0.97, 40, 'buy', 'Köp vid utbrott', 'Köp vid stängning > 46,5 · stopp < 43,1', '43,64 kr, bara 1,3 % över stoppet 43,1.'), ('B2Gold', 'BTG', '4,12 USD (20/11, −5,3 %)', 'Våg 2, djupare', '2', 0.7, 40, 'avoid', 'Stopp utlöst', 'Stoppet 4,55 bröts · ny bedömning först över 5,0 · helt fel under 3,57', 'Föll 5,3 % till 4,12. Helt-fel-nivån 3,57 är 13 % lägre.'), ('Hansa Biopharma', 'HNSA', '45,94 kr (+1,8 % i dag)', 'Start våg 3', '3', 0.07, 55, 'hold', 'Du äger: behåll', 'Stopp: stängning < 44,6 · mål 53,8 / 67,1 · FDA 19 dec', 'Stiger 1,8 % till 45,94, strax under din köpkurs 46,66. Senaste toppen 49,56 (16 nov). Stoppet 44,6.'), ('Mycronic', 'MYCR', '291,40 kr (+3,0 % i dag)', 'Tidig våg 3', '3', 0.14, 50, 'wait', 'Nära köpzon', 'Köp ≤ 285 eller > 313 · stopp < 250', 'Studsar +3,0 % till 291,40, strax över köpzonen ≤ 285.'), ('Spotify', 'SPOT', '577,03 USD (20/11, −1,2 %)', 'Våg 3', '3', 0.36, 55, 'wait', 'Nära köpzon', 'Rekyl mot 571 · stopp < 538 · mål 785', '577,03 USD, 1 % över köpzonen 571. Stoppet 538.'), ('Beijer Ref', 'BEIJ B', '157,40 kr (+1,3 % i dag)', 'Mitt i våg 3', '3', 0.47, 60, 'hold', 'Behåll', 'Varning vid stängning < 155,3 · mål 173,6–178,6', 'Studsar 1,3 % till 157,40, 1,3 % över varningsnivån. Pullback till 146–150 vore en bättre ingång.'), ('Sobi', 'SOBI', '468,00 kr (+0,9 % i dag)', 'Våg 3, rekyl', '3', 0.58, 35, 'avoid', 'Stopp utlöst', 'Under stoppet 469 · ny bedömning > 490', 'Våg 3-bilden bröts den 19 nov och har inte återtagits.'), ('Alphabet', 'GOOGL', '265,29 USD (20/11, −2,7 %)', 'Våg 4', '4', 0.7, 45, 'hold', 'Behåll, köp ej mer', 'Köpzon 243–265 · bekräftelse > 340 · stopp < 243 · mål 318 / 334', 'Föll 2,7 % och bröt 50 %-nivån 273,7. Nästa stöd 243 (62 %).'), ('Meta', 'META', '560,84 USD (20/11)', 'Våg 4 (sidledes)', '4', 0.78, 45, 'buy', 'Köp i delar', 'Köpzon 550–561 · stopp < 526 · mål 627 / 689', '29 % under toppen, stöd 550 (79 %).'), ('TSMC', 'TSM', '318,71 USD (20/11, −9,5 %)', 'Våg 4, vid 50 %', '4', 0.6, 45, 'buy', 'Köp i delar', 'Köpzon 300–319 · stopp < 273 · mål 383 / 402', 'Föll 9,5 % till 50 %-nivån 313,6. Förra bedömningen (våg A nedåt) är omtolkad. Ingen bekräftad botten, så köp i delar.'), ('ASML', 'ASML', '1 266,22 USD (20/11)', 'Våg 4, vid 50 %', '4', 0.74, 45, 'buy', 'Köp i delar', 'Köpzon 1 190–1 266 · stopp < 1 128 · mål 1 542 / 1 628', 'Vid 50 %-nivån 1 292, 36 % under toppen.'), ('Broadcom', 'AVGO', '304,41 USD (20/11)', 'Våg 4, 50–62 %', '4', 0.66, 45, 'buy', 'Köp i delar', 'Köpzon 275–314 · stopp < 274 · mål 364 / 387', 'Mellan 50 % (314) och 62 % (274).'), ('Volvo B', 'VOLV B', '315,70 kr (+0,6 % i dag)', 'Slut våg 4', '4', 0.82, 55, 'buy', 'Köpläge (i zonen)', 'Köpzon 310–326 · stopp < 300 · mål 371,5', 'Fortfarande i köpzonen, 5 % över stoppet. Köp i två steg.'), ('Prysmian', 'PRY', '103,80 EUR (+3,3 % i dag)', 'Slut våg 4', '4', 0.87, 50, 'wait', 'Avvakta', 'Under stödet 105,6 · köp igen > 105,6 · stopp < 97', 'Studsar 3,3 % till 103,80, men under stödet 105,6.'), ('Goldman Sachs', 'GS', '790,69 USD (20/11, −6,7 %)', 'Slut våg 4', '4', 0.92, 40, 'wait', 'Vid stoppet', 'Bekräftelse > 940 · stopp < 790', 'Föll 6,7 % till 790,69, bara 0,1 % över stoppet 790.'), ('Morgan Stanley', 'MS', '165,67 USD (20/11, −5,3 %)', 'Räkning bruten', '4', 0.96, 30, 'avoid', 'Stopp utlöst', 'Stängde under stoppet 172 · ny bedömning först över 194', 'Stoppet 172 bröts på fredagen.'), ('NVIDIA', 'NVDA', '125,53 USD (20/11, −14,0 %)', 'Våg A nedåt', 'A', 0.55, 75, 'avoid', 'Undvik', 'Under 164,27 bekräftad · ingen botten ännu', 'Föll 14 % på en dag, RSI 15. Extremt översåld men ingen botten ännu.'), ('Netflix', 'NFLX', '56,73 USD (20/11, −3,0 %)', 'Räkning bruten', 'C', 0.9, 30, 'avoid', 'Stopp utlöst', 'Stängde under stoppet 58 · ny bedömning först över 61,4', 'Stoppet 58 bröts på fredagen.')]
# clusters -> callout box position
CL=[(['UBER', 'CEG'], (30, 235), '1'), (['BTG', 'MTRS', 'BKNG', 'EKTA B', 'NIBE B'], (300, 520), '2'), (['OKTA', 'HNSA', 'MYCR'], (470, 400), '3'), (['SPOT', 'BEIJ B', 'SOBI'], (310, 95), '3'), (['GOOGL', 'META', 'TSM', 'ASML', 'AVGO', 'VOLV B', 'PRY', 'GS', 'MS'], (765, 330), '4'), (['NVDA'], (1050, 520), 'A'), (['NFLX'], (1050, 640), 'C')]
by={s[1]:s for s in S}
svg=[]
svg.append('<svg viewBox="0 0 1340 730" class="map" role="img" aria-labelledby="mt md"><title id="mt">Elliott-kartan med föreslagna aktier</title><desc id="md">Vågorna 1 till 5 och A till C med varje aktie markerad där den bedöms ligga, med sannolikhet i procent.</desc>')
svg.append('<rect width="1340" height="730" class="bg"/>')
for y in range(90,730,100): svg.append(f'<line x1="0" x2="1340" y1="{y}" y2="{y}" class="grid"/>')
# zones
def zone(x,y,w,h,cls,label,lx,ly):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="zone {cls}"/><text x="{lx}" y="{ly}" class="zl {cls}-t">{label}</text>')
zone(300,430,120,80,'zbuy','KÖPZON',236,476)
zone(740,250,120,80,'zbuy','KÖPZON',868,300)
zone(1235,455,100,80,'zbuy','KÖPZON',1250,552)
zone(925,40,110,80,'zsell','TA HEM VINST',922,35)
zone(1035,200,165,190,'zavoid','UNDVIK',1050,195)
for a,b in zip(seq,seq[1:]):
    (x1,y1),(x2,y2)=P[a],P[b]
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="seg s{COL[b]}"/>')
# stock dots
for s in S:
    x,y=pt(s[4],s[5]); sigc=SIG[s[7]][1]
    svg.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" class="dot {sigc}"/>')
for k in seq[1:]:
    x,y=P[k]
    svg.append(f'<circle cx="{x}" cy="{y}" r="17" class="nd {COL[k]}"/><text x="{x}" y="{y+6}" class="ndt">{k}</text>')
# callouts
for ticks,(bx,by_),w in CL:
    rows=len(ticks); h=16+rows*34; bw=270
    # leader from box to first stock
    for t in ticks:
        s=by[t]; x,y=pt(s[4],s[5])
        cx=bx+bw/2 if abs(x-(bx+bw/2))<bw/2 else (bx if x<bx else bx+bw)
        cy=by_ if y<by_ else (by_+h if y>by_+h else y)
        svg.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{cx:.0f}" y2="{cy:.0f}" class="lead"/>')
    svg.append(f'<rect x="{bx}" y="{by_}" width="{bw}" height="{h}" rx="10" class="box b{COL[w]}"/>')
    for i,t in enumerate(ticks):
        s=by[t]; yy=by_+30+i*34; sigl,sigc=SIG[s[7]]
        svg.append(f'<a href="#k-{t.replace(" ","")}"><circle cx="{bx+18}" cy="{yy-5}" r="6" class="dot {sigc}"/>'
                   f'<text x="{bx+32}" y="{yy}" class="bn">{E(s[0])}</text>'
                   f'<text x="{bx+bw-14}" y="{yy}" class="bp" text-anchor="end">{s[6]} %</text></a>')
svg.append('<text x="20" y="716" class="ax">Tid →</text><text x="1320" y="716" class="ax" text-anchor="end">Impuls 1–5 · korrektion A–B–C</text>')
svg.append('</svg>')

WAVES=[
 ('1','w1','Våg 1: den första uppgången','Kursen vänder upp efter en lång nedgång. De flesta tror fortfarande att det bara är en tillfällig studs.','Svår att se i förväg. Kursen bryter en fallande trend, ofta på hög volym.','Bevaka. Köp gärna först i våg 2.'),
 ('2','w2','Våg 2: rekylen som skrämmer','Kursen tar tillbaka en stor del av våg 1, ofta 50–61,8 %. Pessimismen kommer tillbaka.','Går aldrig under starten på våg 1. Det är den viktigaste regeln och därmed din stoppnivå.','Köpzon. Lägst risk i hela cykeln.'),
 ('3','w3','Våg 3: den starka vågen','Den längsta och snabbaste vågen. Nyheterna blir bättre och alla vill köpa.','Ofta 1,618 gånger våg 1 eller mer. Får aldrig vara den kortaste av vågorna 1, 3 och 5.','Köp när utbrottet bekräftas. Behåll.'),
 ('4','w4','Våg 4: andningspausen','Kursen vilar eller går sidledes efter den kraftiga uppgången. Många säljer för tidigt.','Tar oftast tillbaka 23,6–50 % av våg 3. Ska inte gå ned i våg 1:s kursområde.','Köpzon inför våg 5, med en nära stoppnivå.'),
 ('5','w5','Våg 5: den sista uppgången','Optimismen är som störst och kursen når ny topp, men med allt mindre kraft. Det syns som att RSI sjunker trots nya toppar.','Ofta lika lång som våg 1, eller 0,618 gånger våg 1 + våg 3.','Ta hem vinst. Köp inte nytt.'),
 ('A','wa','Våg A: första fallet','Det första fallet efter toppen. Marknaden tror att det är en vanlig rekyl.','Bryter oftast trendlinjen och 200-dagarssnittet.','Undvik. Sälj det du har kvar.'),
 ('B','wb','Våg B: falskt hopp','En studs som lurar många att köpa igen. Den slår sällan den förra toppen.','Ofta 50–78,6 % av våg A.','Undvik. Studsen är ett tillfälle att sälja.'),
 ('C','wc','Våg C: den sista nedgången','Ett brett fall med rädsla och kapitulation. Den bästa köpzonen kommer i slutet av C.','Ofta lika lång som A, eller slutar vid 50–61,8 % av hela förra uppgången.','Köpzon när C är slut och en ny våg 1 startar.'),
]
wcards=''.join(f'''<article class="wcard {c}"><header><span class="wn {c}">{n}</span><h3>{E(h)}</h3></header>
<p>{E(a)}</p><p class="rule"><b>Kännetecken:</b> {E(b)}</p><p class="act {c}"><b>Gör:</b> {E(d)}</p></article>''' for n,c,h,a,b,d in WAVES)

rows=''.join(f'''<tr id="k-{s[1].replace(" ","")}"><th scope="row">{E(s[0])}<span class="sub">{E(s[1])}</span></th><td class="n">{E(s[2])}</td>
<td><span class="chip {COL[s[4]]}">{E(s[3])}</span></td><td class="n"><span class="prob"><i style="width:{s[6]}%"></i></span><b>{s[6]} %</b></td>
<td><span class="sig {SIG[s[7]][1]}">{E(s[8])}</span></td><td>{E(s[9])}</td><td class="why">{E(s[10])}</td></tr>''' for s in S)

tpl=open('kompass_tpl.html').read()
open('/home/user/genesis-accord-standard/reports/elliott-kompass/elliott-kompass.html','w').write(tpl.replace('{{SVG}}',''.join(svg)).replace('{{WAVES}}',wcards).replace('{{ROWS}}',rows).replace('{{OPP}}',open('opp_section.html').read()))
print('ok')
