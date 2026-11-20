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
S=[('Uber', 'UBER', '65,60 USD (19/11, −4,6 %)', 'Slut C / tidig 1', '1', 0.1, 40, 'avoid', 'Undvik', 'Bekräftelse > 72,9 · stopp < 64', 'Föll 4,6 % till 65,60, nära stoppet 64.'), ('Constellation', 'CEG', '252,03 USD (19/11, −4,1 %)', 'Slut C / tidig 1', '1', 0.2, 45, 'wait', 'Avvakta', 'Bekräftelse > 309,8 · stopp < 228,6', 'Föll 4,1 % till 252. Stoppet 228,6.'), ('Okta', 'OKTA', '206,85 USD (19/11, +5,7 %)', 'Start våg 3', '3', 0.2, 60, 'wait', 'Bekräftad, men dyr', 'Våg 3 bekräftad > 187 · mål 235 / 336 · stopp < 164', 'Den enda starka aktien: +5,8 % i går mot en fallande marknad. Våg 3 pågår. Dyr.'), ('Munters', 'MTRS', '132,45 kr (−3,7 % i dag)', 'Våg 2 (alt. C)', '2', 0.76, 45, 'hold', 'Behåll, köp ej fler', 'Bekräftelse > 143,9 · stopp < 123,7', 'Vände ned från 145,15 till 132,45. Bekräftelsen misslyckades. Stoppet 123,7 gäller.'), ('Booking', 'BKNG', '147,32 USD (19/11, −3,9 %)', 'Slut våg 2', '2', 0.84, 45, 'wait', 'Avvakta, vid gränsen', 'Helt fel vid stängning < 146,28 · bekräftelse > 174,30', 'Stängde 147,32, bara 0,7 % över gränsen 146,28 där vågräkningen blir fel.'), ('Elekta', 'EKTA B', '60,85 kr (−1,9 % i dag)', 'Slut våg 2', '2', 0.91, 50, 'buy', 'Köp vid utbrott', 'Köpsignal vid stängning > 63,25 · utbrott > 66,70 · stopp < 59 · rapport 25 nov', 'Föll till 60,85. Ingen köpsignal (63,25). Rapport 25 nov.'), ('NIBE', 'NIBE B', '43,64 kr (−2,3 % i dag)', 'Slut våg 2', '2', 0.97, 40, 'buy', 'Köp vid utbrott', 'Köp vid stängning > 46,5 · stopp < 43,1 · rapport 17 nov', 'Föll till 43,64 efter rapporten. Under stigande bottnar-linjen, svagare.'), ('B2Gold', 'BTG', '4,35 USD (19/11, −3,3 %)', 'Våg 2, djupare', '2', 0.7, 45, 'avoid', 'Stopp utlöst', 'Stoppet 4,55 bröts 18 nov · ny bedömning först över 5,0 · helt fel under 3,57', 'Guldet har fallit till 3 590 USD. B2Gold 4,35 USD.'), ('Hansa Biopharma', 'HNSA', '46,50 kr (−1,7 % i dag)', 'Start våg 3', '3', 0.07, 55, 'hold', 'Du äger: behåll', 'Stopp: stängning < 44,6 · mål 53,8 / 67,1 · FDA 19 dec', '46,50 kr, strax under din köpkurs. Dagslägsta 45,78. Stoppet 44,6 gäller.'), ('Mycronic', 'MYCR', '290,40 kr (−3,7 % i dag)', 'Tidig våg 3', '3', 0.14, 50, 'wait', 'Nära köpzon', 'Köp ≤ 285 eller > 313 · stopp < 250', 'Föll 3,7 % i dag. Köpzonen ≤ 285 är nära igen.'), ('Spotify', 'SPOT', '583,85 USD (19/11, −3,6 %)', 'Våg 3', '3', 0.36, 55, 'wait', 'Köp på rekyl', 'Rekyl mot 571 · stopp < 538 · mål 785', 'Rekyl till 583,85. Köpzon mot 571, stopp 538.'), ('Beijer Ref', 'BEIJ B', '157,50 kr (−1,8 % i dag)', 'Mitt i våg 3', '3', 0.47, 60, 'hold', 'Behåll', 'Varning vid stängning < 155,3 · mål 173,6–178,6', '157,50 kr, 1,4 % över varningsnivån. Marknaden drar ned allt.'), ('Sobi', 'SOBI', '466,80 kr (−0,2 % i dag)', 'Våg 3, rekyl', '3', 0.58, 35, 'avoid', 'Stopp utlöst', 'Stängde 467,80 under stoppet 469 · ny bedömning > 490', 'Våg 3-bilden bröts den 19 nov.'), ('Alphabet', 'GOOGL', '272,66 USD (19/11, −3,5 %)', 'Våg 4', '4', 0.7, 45, 'hold', 'Behåll', 'Bekräftelse > 340 · stopp < 243', 'Föll 3,5 %. Stoppet 243 långt bort.'), ('TSMC', 'TSM', '352,09 USD (19/11, −2,9 %)', 'Våg A nedåt', 'A', 0.3, 55, 'avoid', 'Undvik', 'Stopp 352 bryts i förhandeln (345)', 'Taiwanbörsen −6,2 % i dag och −18 % på två veckor.'), ('Volvo B', 'VOLV B', '312,80 kr (−2,3 % i dag)', 'Slut våg 4', '4', 0.82, 55, 'buy', 'Köpläge (i zonen)', 'Köpzon 310–326 · stopp < 300 · mål 371,5', 'Fortfarande i köpzonen och 4 % över stoppet. Hög risk i hela marknaden, så köp gärna i två steg.'), ('Prysmian', 'PRY', '102,95 EUR (−4,0 % i dag)', 'Slut våg 4', '4', 0.87, 50, 'wait', 'Avvakta', 'Under stödet 105,6 · köp igen > 105,6 · stopp < 97', 'Föll 4 % i dag och bröt stödet 105,6. Dubbelbotten 97–100 är nästa stöd.'), ('Goldman Sachs', 'GS', '847,53 USD (19/11, −2,9 %)', 'Slut våg 4', '4', 0.92, 55, 'wait', 'Dyr per aktie', 'Bekräftelse > 940 · stopp < 790', '847,53 USD. Stoppet 790 långt bort.'), ('Morgan Stanley', 'MS', '174,98 USD (19/11, −3,4 %)', 'Slut våg 4', '4', 0.96, 50, 'wait', 'Köp vid > 194', 'Köp vid stängning > 194 · stopp < 172', '174,98 USD, 1,7 % över stoppet 172.'), ('NVIDIA', 'NVDA', '145,98 USD (19/11, −3,3 %)', 'Våg A nedåt', 'A', 0.55, 75, 'avoid', 'Undvik', 'Under 164,27: större korrektion bekräftad', 'Fallet fortsätter, 145,98 USD. Bra rapport hjälpte inte.'), ('Netflix', 'NFLX', '58,46 USD (19/11, −2,3 %)', 'Slut våg C', 'C', 0.9, 40, 'avoid', 'Undvik', 'Stopp 58 nästan nått (dagslägsta 58,19)', 'Bottnen 61,39 är bruten och kursen ligger 0,8 % över stoppet.')]
# clusters -> callout box position
CL=[(['UBER', 'CEG'], (30, 235), '1'), (['BTG', 'MTRS', 'BKNG', 'EKTA B', 'NIBE B'], (300, 520), '2'), (['OKTA', 'HNSA', 'MYCR'], (470, 400), '3'), (['SPOT', 'BEIJ B', 'SOBI'], (310, 95), '3'), (['GOOGL', 'VOLV B', 'PRY', 'GS', 'MS'], (765, 350), '4'), (['NVDA', 'TSM'], (1050, 520), 'A'), (['NFLX'], (1050, 640), 'C')]
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
