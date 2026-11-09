# Hand-written analysis content (Swedish). Levels derive from Yahoo Finance daily/weekly/monthly data, see build/screen scripts.
# wave: 1,2,3,4,5,A,B,C
S = {}

S['TSM'] = dict(
  name='TSMC (ADR)', exch='NYSE', wave='4', conf='Medel–hög', sector='Halvledare / foundry',
  why='Våg (4) nådde exakt 38,2 % av våg (3) på kapitulationsvolym den 5 nov. I dag +4,5 % till 392, men bekräftelsen (stängning över 405) saknas fortfarande. Värderingen är låg för tillväxten.',
  count='(1) okt 2022 ≈59 → 226,4 (24 jan 2025). (2) → 134,25 (7 apr 2025), 55 % retracement. (3) → 487,47 (5 okt 2026), 2,1 × våg (1). (4) pågår: botten hittills 351,19 (5 nov), vilket är 38,2 % av våg (3) (352,5).',
  alt='Toppen 487 avslutade hela uppgången från 2022 och fallet är en våg A. Det blir troligare om kursen stänger en vecka under 50 %-nivån 311.',
  support='351–353 (38,2 % och botten 5 nov)', resist='405 · 441 · 487', zone='352–380',
  confirm='Daglig stängning över 405 med en högre botten. Därefter veckostängning över 441.',
  inval='Veckostängning under 309, alltså under 50 % av våg (3). Absolut gräns 226,4: där överlappar våg 4 toppen på våg 1.',
  t1=487.47, t2=518, stop=309,
  t2txt='518 (våg 5 lika lång som våg 1)',
  fund='Q3 2026: omsättning 46,7 mdr USD, över guidningen, med bruttomarginal 66,4 %. Q4-guidning 52,3–54,3 mdr USD. Väntad omsättningstillväxt för helåret ca +44 % i USD. Framåtblickande P/E 16,1 och PEG 0,68. Stor nettokassa. EV/EBITDA är hämtat från den taiwanesiska noteringen 2330.TW (14,4), eftersom ADR-värdet blandar valutor.',
  psych='SOX föll 12,2 % den 5 nov, näst värsta dagen någonsin. TSM föll 10,8 % samma dag på 3,7 gånger normal volym. Fallet drevs av hedgefonders försäljning och oro för AI-investeringarna efter mellanårsvalet, inte av nyheter från bolaget. Mönstret liknar kapitulation i en intakt trend.',
  scores=(7,9,8,5,9))

S['BKNG'] = dict(
  name='Booking Holdings', exch='NASDAQ', wave='2', conf='Medel', sector='Konsument / resor',
  why='ABC-korrektionen ser avslutad ut nära 50 % av uppgången 2022–25. En första impulsvåg är gjord och kursen står nu i en våg 2-rekyl som hittills har hållit vid 49 %. Lägst framåtblickande P/E bland kvalitetsbolagen i urvalet.',
  count='Uppgången 2022 → ATH 233,58 (8 jul 2025). A → 150,62 (23 feb 2026). B → 217,32 (25 aug). C → 146,28 (28 okt), där C ≈ 0,86 × A och botten ligger nära 50 % av uppgången 2022–25. Ny våg 1: 146,28 → 174,30 (5 nov, efter Q3). Våg 2: rekylen gick till 160,67 den 6 nov, 49 % av våg 1. I dag 163,51 (+1,8 %), så den bottnen håller hittills. 61,8 %-nivån ligger på 157,0.',
  alt='Studsen är bara en B-våg inom en större korrektion, och C fortsätter mot 61,8 % av uppgången 2022–25 (≈130).',
  support='157 · 146,3', resist='174,3 · 217', zone='155–161',
  confirm='Stängning över 174,30 (toppen på våg 1). Det bekräftar att våg 3 har startat.',
  inval='Stängning under 146,28, startpunkten för våg 1.',
  t1=202, t2=217.32, stop=146.28,
  t2txt='217 (B-toppen)', t1txt='202 (våg 3 = 1,618 × våg 1)',
  fund='Q3 2026: justerad vinst per aktie 4,66 USD mot förväntade 4,48. Rumsnätter +7 % mot väntade 3–5 %. Guidningen för Q4 är svag: rumsnätter +1–3 %. Framåtblickande P/E 13,1, EV/EBITDA 12,7 och PEG 0,59. Rörelsemarginal 39 % och fritt kassaflöde 7,6 mdr USD. Yahoo anger omsättningstillväxten till −1 %, vilket inte går ihop med rumsnattstillväxten, så den siffran är inte verifierad. Kursserien är splitjusterad.',
  psych='Kursen föll 35 % på rädsla för att AI-agenter ska ta bort resesajternas roll som mellanhand. Q3-rapporten slog förväntningarna och analytikerkåren är fortfarande positiv. Pessimismen verkar redan prisad, men AI-risken är en verklig fundamental fråga och inte bara känslor.',
  scores=(8,8,9,7,8))

S['GS'] = dict(
  name='Goldman Sachs', exch='NYSE', wave='4', conf='Medel', sector='Finans / investmentbank',
  why='Våg (4) bottnade vid 42 % av en kraftig våg (3), och i dag steg aktien 5 % till 909. Vinsten per aktie växer 39 % och P/E är 12. Efter dagens uppgång är risk/reward lägre än i fredags.',
  count='(1) okt 2023 ≈290 → 672,19 (18 feb 2025). (2) → 439,38 (7 apr 2025), 61 % retracement. (3) → 1153,99 (15 jul 2026), 1,87 × våg (1). (4) pågår: botten hittills 854,45 (5 nov), 41,9 % av våg (3). 38,2 %-nivån ligger på 881 och 50 %-nivån på 797.',
  alt='Toppen i juli var en cykeltopp för hela finanssektorn och fallet är en våg A, till exempel på grund av hårdare reglering efter valet.',
  support='854 · 797', resist='940 · 956 (200-dagars) · 1154', zone='855–910',
  confirm='Stängning över 940 och sedan över 200-dagarssnittet 956.',
  inval='Veckostängning under 790. Absolut gräns 672 (toppen på våg 1).',
  t1=1153.99, t2=1235, stop=790,
  t2txt='≈1235 (våg 5 lika lång som våg 1)',
  fund='Q3 2026: vinst per aktie 17,01 USD mot 12,25 året innan. Nettointäkter 18,7 mdr USD och avkastning på eget kapital 18,7 %. Global Banking & Markets växte 32 %. P/E 12,4, framåtblickande 11,7. Kvartalsutdelning 5,00 USD. EV-baserade nyckeltal är inte meningsfulla för en bank.',
  psych='Aktien föll trots en stark rapport. Det tyder på sektorrotation och politisk oro snarare än svagare fundamenta. Säljvolymen har inte varit extrem, så kapitulation är ännu inte synlig.',
  scores=(7,8,8,6,9))

S['ASML.AS'] = dict(
  name='ASML Holding', exch='Euronext Amsterdam', wave='4', conf='Medel', sector='Halvledarutrustning',
  why='Våg (4) står vid 38–43 % av våg (3). Efterfrågan på EUV-maskiner överstiger planerad kapacitet både 2027 och 2028.',
  count='(1) okt 2022 ≈398 → ≈1002 (jul 2024, veckostängning). (2) → 508,4 (7 apr 2025), en djup våg 2. (3) → 1741 (30 jun 2026), 2,0 × våg (1). (4) pågår: lägre toppar 1741 → 1621 → 1656 och botten 1210,6 (5 nov), 43 % av våg (3). 38,2 %-nivån ligger på 1270 och 50 %-nivån på 1125.',
  alt='Våg 4 utvecklas till en längre flat eller triangel som håller på in i 2027, eller så är toppen i juni en större våg A-topp.',
  support='1211 · 1125', resist='1396 (200-dagars) · 1515 · 1741', zone='1210–1300',
  confirm='Stängning över 1400 (200-dagarssnittet) och därefter över 1515.',
  inval='Veckostängning under 1120. Absolut gräns ≈1002 (toppen på våg 1).',
  t1=1741, t2=1815, stop=1120,
  t2txt='≈1815 (våg 5 lika lång som våg 1)',
  fund='Q3 2026: omsättning 11,7 mdr EUR och bruttomarginal 57,5 %. Q4-guidning 14,2–15,2 mdr EUR och helår 44–45 mdr EUR. Planerad kapacitet räcker inte för efterfrågan 2027 och 2028. Framåtblickande P/E 23,2, PEG 0,75 och EV/EBITDA 29,7. Nettokassa ≈10,8 mdr EUR. Värderingen är rimlig för tillväxten men inte låg.',
  psych='Aktien har fallit på samma AI- och valoro som resten av halvledarsektorn, medan bolagets egna besked var positiva. Kursen ligger strax under 200-dagarssnittet. Hela halvledarsektorn ligger nu i ett läge av rädsla.',
  scores=(7,9,6,5,9))

S['MYCR.ST'] = dict(
  name='Mycronic', exch='Nasdaq Stockholm', wave='2', conf='Medel', sector='Industriteknik / maskritare',
  why='Ett mindre bevakat svenskt kvalitetsbolag. Våg ii inom en större våg (3) har nått 50 %-nivån och 200-dagarssnittet. Bolaget har nettokassa och rekordstor orderstock.',
  count='Uppgången 2022 ≈63 → ≈250 (feb 2025) är våg (1). Våg (2) bildade en dubbelbotten 176,5 (jun 2025) och 183,32 (6 feb 2026). Inom våg (3): i 183,32 → 364,4 (6 okt 2026). ii pågår: botten 270,6 (6 nov), 51,6 %. 50 %-nivån ligger på 273,9 och 61,8 %-nivån på 252,5.',
  alt='Toppen 364 avslutade våg (3) och det här är en sidledes våg (4) mellan 250 och 364 som kan pågå i flera månader.',
  support='271 · 252', resist='284 (200-dagars) · 313 · 364', zone='253–280',
  confirm='Stängning över 313 (högsta nivån de senaste 10 dagarna) och tillbaka över 200-dagarssnittet 284.',
  inval='Stängning under 250. Absolut gräns 183,32 (start på våg i).',
  t1=364.4, t2=451, stop=250,
  t2txt='≈451 (våg iii lika lång som våg i)',
  fund='Q3 2026 enligt en sekundärkälla (Börsvärlden): orderingång 2 667 MSEK (+10 %), rekordstor orderstock 5 566 MSEK och omsättning 2 356 MSEK. Q2-rapporten innehöll höjd prognos. Framåtblickande P/E 17,2, EV/EBITDA 17,4, rörelsemarginal 26 %, nettokassa ≈2,9 mdr SEK och fritt kassaflöde 1,9 mdr SEK. Bara 4 analytiker följer aktien, med neutralt snittbetyg.',
  psych='Aktien har fallit med halvledarsektorn trots att orderingången växer. Få analytiker följer den, vilket ger utrymme för omvärdering. Det betyder också sämre likviditet och mer osäker information.',
  scores=(7,8,8,7,6))

S['GOOGL'] = dict(
  name='Alphabet', exch='NASDAQ', wave='4', conf='Låg–medel', sector='Internet / moln',
  why='Kursen ligger mellan 38,2 % och 50 % av våg (3) efter det största endagsraset sedan börsnoteringen. Rekylen har en fundamental orsak: negativt fritt kassaflöde och en vinstmiss.',
  count='(1) 2022 ≈83 → 207,05 (4 feb 2025). (2) → 140,53 (7 apr 2025). (3) → 408,61 (18 maj 2026). (4) pågår: botten 276,92 (30 okt), 49 %.',
  alt='Det här är en våg A. Om marknaden ser kapitalutgifterna som värdeförstörande kan kursen gå mot 243 (61,8 %) eller lägre.',
  support='277 · 243', resist='326 · 340 (200-dagars) · 409', zone='275–300',
  confirm='Stängning över 326 och därefter över 340.',
  inval='Veckostängning under 243. Absolut gräns 207 (toppen på våg 1).',
  t1=408.61, t2=None, stop=243,
  fund='Q3 2026: omsättning 127,6 mdr USD (+25 %) och Cloud +103 %. Vinsten per aktie, 2,12 USD, missade konsensus 3,02 tydligt. Fritt kassaflöde var −9,1 mdr USD under kvartalet och kapitalutgifterna för 2026 väntas bli 195–205 mdr USD, med mer 2027. Framåtblickande P/E 18,5 och stor nettokassa.',
  psych='Kursen föll ungefär 13 % på en dag. Rapporten var en verklig besvikelse, så det är inte bara en överreaktion. Läget blir intressant först om marknaden börjar se kapitalutgifterna som en investering och inte som en kostnad.',
  scores=(6,7,7,7,9))

S['PWR'] = dict(
  name='Quanta Services', exch='NYSE', wave='4', conf='Låg–medel', sector='Elnät / infrastruktur',
  why='Rekordstor orderstock på 63,7 mdr USD och vinst per aktie +82 %, men våg 4 är djup (51 %) och P/E-talet högt.',
  count='(1) okt 2023 ≈165 → 365,88 (22 jan 2025). (2) → 227,08 (7 apr 2025). (3) → 788,75 (6 maj 2026). (4) pågår: botten 502,04 (5 nov), 51 %. 61,8 %-nivån ligger på 441,6.',
  alt='Uppgången 2025–26 var hela våg (5) och nu pågår en större korrektion.',
  support='502 · 442', resist='657 · 629 (200-dagars) · 789', zone='505–545',
  confirm='Stängning över 657 (högsta nivån de senaste 10 dagarna).',
  inval='Veckostängning under 441,6 (61,8 %). Absolut gräns 365,9 (toppen på våg 1).',
  t1=788.75, t2=None, stop=441.6,
  fund='Q3 2026: omsättning 12,0 mdr USD (+57 %), justerad vinst per aktie 6,06 USD mot 3,33 året innan och rekordstor orderstock på 63,7 mdr USD. En del av tillväxten kommer från förvärv. Framåtblickande P/E 25, rörelsemarginal 9 % och nettoskuld 5,2 mdr USD.',
  psych='Aktien drabbas direkt av oron för datacenterbyggandet efter valet, trots en mycket stark rapport.',
  scores=(6,8,6,7,8))

S['ISRG'] = dict(
  name='Intuitive Surgical', exch='NASDAQ', wave='1', conf='Medel', sector='Medicinteknik',
  why='En korrektion på 47 % har nått 61,8 %-nivån, och en kraftig ny våg 1 har startat. Bästa ingången kommer på en våg 2-rekyl, inte på nuvarande kurs.',
  count='Uppgången 2022 ≈180 → ATH 616 (23 jan 2025). Korrektionen → 328,57 (23 jul 2026), ca 63–65 %. Ny våg 1 → 485,85 (4 nov, efter Q3). Våg 2-zonen ligger vid 50 % (407) och 61,8 % (389).',
  alt='Uppgången från juli är en B-våg och en ny C-våg tar kursen tillbaka mot 330.',
  support='431 (200-dagars) · 407 · 389', resist='486 · 616', zone='389–410 (vänta)',
  confirm='Ett avslutat våg 2-mönster i köpzonen, följt av stängning över 485,85.',
  inval='Stängning under 328,57.',
  t1=616, t2=None, stop=328.57,
  fund='Q3 2026: omsättning 3,05 mdr USD (+22 %), ingrepp +15 % och justerad vinst per aktie 3,00 USD mot väntade 2,61. 546 sålda da Vinci-system. Ett engångsavdrag på 450 MUSD för en antitrustförlikning. Framåtblickande P/E 36 och PEG 2,0: premievärdering.',
  psych='Pessimismen under 2025–26 vände på en stark rapport. Kursen är redan +38 % från botten, så det är sent att köpa i den här vågen.',
  scores=(4,9,4,6,9))

S['ETN'] = dict(
  name='Eaton', exch='NYSE', wave='2', conf='Låg', sector='Elektrifiering',
  why='Kursen har gått tillbaka 62 % av uppgången 2025–26. Det passar en våg 2, men nettoskulden och den låga vinsttillväxten är svagheter.',
  count='Botten 231,85 (7 apr 2025) → 478 (12 aug 2026) är våg 1. Våg 2 pågår: botten 324,27 (5 nov), 62,4 %.',
  alt='En större ABC-korrektion som kan gå under 300.',
  support='324 · 300', resist='394 · 397 (200-dagars) · 478', zone='325–345',
  confirm='Stängning över 394.', inval='Veckostängning under 300.',
  t1=478, t2=None, stop=300,
  fund='Framåtblickande P/E 20,9, PEG 1,83, vinsttillväxt +7 % och omsättningstillväxt +28 %. Nettoskuld ≈20 mdr USD.',
  psych='Samma oro för datacenterbyggandet som för PWR och VRT.',
  scores=(6,7,6,6,8))

S['ABBN.SW'] = dict(
  name='ABB', exch='SIX Swiss', wave='4', conf='Låg–medel', sector='Elektrifiering / automation',
  why='Rekylen är 44 % av uppgången 2025–26. Strukturen är ren, men analytikerna är neutrala och vinsten växer inte.',
  count='Botten 37,25 (7 apr 2025) → 89,14 (22 jun 2026). Rekyl → 66,08 (6 nov), 44 %.',
  alt='Våg 2 av en ny impuls, med möjligt djupare fall mot 57 (61,8 %).',
  support='66 · 63', resist='73 · 76,6 (200-dagars) · 89', zone='63–68',
  confirm='Stängning över 73,1.', inval='Veckostängning under 57.',
  t1=89.14, t2=None, stop=57,
  fund='Framåtblickande P/E 22,1, EV/EBITDA 16,8, vinsttillväxt −1 % och analytikernas snittbetyg 2,7 (behåll).',
  psych='En lugn rekyl utan panik.',
  scores=(6,7,6,6,8))

S['SPGI'] = dict(
  name='S&P Global', exch='NYSE', wave='3', conf='Låg–medel', sector='Finansiell data',
  why='En tidig våg 3 efter en ABC-korrektion. Upptrenden är bekräftad, men kursen ligger redan långt från stödet.',
  count='Botten 379,38 (13 maj 2026), våg 1 → 462,02 (17 jul), djup våg 2 → 382,21 (2 okt), våg 3 → 485,99 (5 nov).',
  alt='Ett sidledes intervall mellan 380 och 527 sedan 2025.', support='460 · 416 (200-dagars) · 382', resist='486 · 527',
  zone='Vänta på rekyl', confirm='Bekräftad.', inval='Under 379.', t1=527, t2=None, stop=379.38,
  fund='Framåtblickande P/E 23,2, rörelsemarginal 48 % och omsättningstillväxt +7 %.', psych='Defensiv rotation in i kvalitetsbolag.',
  scores=(6,8,6,4,9))

S['MCO'] = dict(
  name="Moody's", exch='NYSE', wave='3', conf='Låg–medel', sector='Finansiell data',
  why='Våg 3 har startat från en högre botten och kursen ligger nära rekordnivån.',
  count='422,16 (12 mar 2026) → 520,67 (27 aug), våg 2 → 438,01 (2 okt), våg 3 → 533 (5 nov).',
  alt='Ett intervall mellan 420 och 540.', support='495 · 466 (200-dagars) · 438', resist='539', zone='Vänta på rekyl',
  confirm='Veckostängning över 539.', inval='Under 438.', t1=597, t2=None, stop=438,
  fund='Framåtblickande P/E 27,2: dyrt för omsättningstillväxten.', psych='Defensiv rotation.', scores=(5,8,5,5,9))

S['LLY'] = dict(
  name='Eli Lilly', exch='NYSE', wave='3', conf='Medel', sector='Läkemedel',
  why='En stark våg 3 till ny rekordnivå. Ingen rekyl att köpa i nu.',
  count='623,78 (8 aug 2025) → 1453 (5 nov 2026), +133 %.',
  alt='Våg 5 av en längre cykel.', support='1280 · 1116', resist='1453', zone='Vänta på våg 4',
  confirm='–', inval='Under 1116 bryts strukturen.', t1=None, t2=None, stop=1116,
  fund='Framåtblickande P/E 26,9, omsättningstillväxt +39 % och nettoskuld ≈45 mdr USD.', psych='Optimism och höga förväntningar.', scores=(3,9,5,4,9))

S['NVDA'] = dict(
  name='NVIDIA', exch='NASDAQ', wave='5', conf='Låg', sector='AI-halvledare',
  why='Mycket lågt framåtblickande P/E (11,7), men vågstrukturen ser mogen ut. I dag föll aktien 4,4 % medan resten av sektorn steg 7 %, och den bröt under botten från 5 nov (181,46) med ett dagslägsta på 170,24. Rapporten väntas runt 17 nov.',
  count='Från 2022: (3) → 2024, (4) → 86,62 (7 apr 2025), (5) pågår eller är klar vid 243,37 (6 okt 2026). Det breda intervallet kan vara en avslutande diagonal.',
  alt='Intervallet 164–243 är en våg 4-triangel, och ett brott över 243 startar en ny våg 5.',
  support='181,5 · 164,3', resist='205 (200-dagars) · 243', zone='–',
  confirm='Veckostängning över 243.', inval='Under 164,3 är ABC-scenariot bekräftat.', t1=243.37, t2=None, stop=164.27,
  fund='Omsättningstillväxt +106 %, rörelsemarginal 66 %, framåtblickande P/E 11,7 och PEG 0,23. Marknaden ifrågasätter hur länge vinstnivån håller.', psych='Rapporten blir avgörande för hela AI-sektorn.', scores=(5,9,8,5,9))

S['AMD'] = dict(
  name='AMD', exch='NASDAQ', wave='5', conf='Låg', sector='AI-halvledare',
  why='En utsträckt våg 5: +570 % från 2025 års botten. I dag +14,2 % efter en uppgradering från Oppenheimer, men P/E är 96–110 på historisk vinst.',
  count='76,48 (8 apr 2025) → 658,52 (6 okt 2026). Rekyl → 402,1 (5 nov).',
  alt='Våg 4 med ytterligare en topp senare.', support='402 · 416 (200-dagars)', resist='578 · 659', zone='–',
  confirm='–', inval='Under 402.', t1=None, t2=None, stop=402.1,
  fund='P/E 96 (historisk vinst), framåtblickande 25,4 och EV/EBITDA 65.', psych='Typiskt girighetsmönster.', scores=(3,7,3,4,9))

S['MU'] = dict(
  name='Micron', exch='NASDAQ', wave='A', conf='Medel', sector='Minneskretsar',
  why='En parabolisk rörelse på 20 gånger. Framåtblickande P/E 3,3 är ett klassiskt tecken på toppen i en vinstcykel.',
  count='61,54 (7 apr 2025) → 1255 (25 jun 2026). Våg A → 650 (5 nov), −48 %.',
  alt='En våg 4 inom en fortsatt supercykel.', support='650 · 532', resist='757 (200-dagars) · 1097', zone='–',
  confirm='–', inval='–', t1=None, t2=None, stop=None,
  fund='Omsättningstillväxt +379 % och rörelsemarginal 81 %: toppmarginaler i cykeln.', psych='Girigheten har vänt till rädsla.', scores=(3,7,6,4,8))

S['000660.KS'] = dict(
  name='SK hynix', exch='KRX', wave='A', conf='Medel', sector='Minneskretsar',
  why='Kursen steg 18 gånger och har sedan fallit 64 %, i linje med Micron.',
  count='162 700 (9 apr 2025) → 2 987 000 (25 jun 2026). Våg A → 1 089 000 (6 nov).',
  alt='Våg 4.', support='1,09 mn · 0,96 mn', resist='1,51 mn (200-dagars)', zone='–', confirm='–', inval='–', t1=None, t2=None, stop=None,
  fund='Framåtblickande P/E 2,1. Historiskt P/E och fritt kassaflöde saknas hos Yahoo.', psych='Koreaindexet KOSPI ligger 46 % under toppen.', scores=(3,7,6,4,6))

S['CAT'] = dict(
  name='Caterpillar', exch='NYSE', wave='A', conf='Medel', sector='Maskiner',
  why='Kursen fyrdubblades på 15 månader och har nu fallit 48 %. Veckans RSI är 26 (översålt), men strukturen är en A-våg.',
  count='267,3 (7 apr 2025) → 1073,46 (30 jun 2026). Våg A → 550,81 (5 nov), 65 % retracement.',
  alt='En djup våg 4.', support='551 · 537', resist='808 (200-dagars)', zone='–', confirm='–', inval='–', t1=None, t2=None, stop=None,
  fund='Framåtblickande P/E 17,3 och nettoskuld 38 mdr USD.', psych='Kapitulationsliknande säljtryck.', scores=(3,7,5,4,9))

S['VRT'] = dict(
  name='Vertiv', exch='NYSE', wave='A', conf='Låg–medel', sector='Datacenterinfrastruktur',
  why='Kursen har fallit 55 % från toppen och brutit uppgångens struktur. Värderingen (framåtblickande P/E 18,6) är dock rimlig.',
  count='53,6 (7 apr 2025) → 379,93 (14 maj 2026) → 170,8 (5 nov), 64 % retracement.',
  alt='En djup våg 2 av en ny cykel.', support='171 · 148', resist='271 (200-dagars)', zone='–', confirm='Stängning över 254.', inval='–', t1=None, t2=None, stop=None,
  fund='Omsättningstillväxt +61 %, framåtblickande P/E 18,6, PEG 0,54 och nettokassa.', psych='Aktien är i centrum för AI-oron.', scores=(4,8,6,5,8))

S['RHM.DE'] = dict(
  name='Rheinmetall', exch='XETRA', wave='C', conf='Låg–medel', sector='Försvar',
  why='En korrektion på 60 % från 2008 som sannolikt är en C-våg. Den är nära en möjlig botten, men ingen vändning är bekräftad.',
  count='ATH 2008 (3 okt 2025). A → 1120 (maj 2026). B → 1293. C pågår → 792,6 (9 nov).',
  alt='Kursen faller vidare om fredsoptimismen håller i sig.', support='793', resist='1090 · 1241 (200-dagars)', zone='–',
  confirm='Stängning över 1090.', inval='–', t1=None, t2=None, stop=None,
  fund='Framåtblickande P/E 16, PEG 0,32 och omsättningstillväxt +36 %.', psych='Försvarssektorn har gått från eufori till likgiltighet.', scores=(3,7,7,4,8))

S['KLAC'] = dict(
  name='KLA', exch='NASDAQ', wave='A', conf='Låg–medel', sector='Halvledarutrustning',
  why='Kursen har gått tillbaka 71 % av uppgången 2025–26, vilket är för djupt för en normal våg 4.',
  count='55,13 (7 apr 2025) → 307,37 (30 jun 2026) → 128,17 (5 nov).',
  alt='En djup våg 2.', support='128 · 107', resist='182 (200-dagars)', zone='–', confirm='–', inval='–', t1=None, t2=None, stop=None,
  fund='Framåtblickande P/E 19,5, EV/EBITDA 27,6. Kursserien är splitjusterad (10:1, 2026).', psych='Panikförsäljning.', scores=(3,8,5,4,9))

TOP = ['BKNG','NFLX','TSM','GS','MYCR.ST']
WATCH = ['ASML.AS','UBER','GOOGL','ISRG']

REJECTED = [
 ('Samsung Electronics (005930.KS)','Minnescykeln: +575 % och sedan −46 %. A-våg och toppmarginaler, ingen köpsignal.'),
 ('Lam Research, Applied Materials, Tokyo Electron, BE Semi, Disco','Rekylerna är 57–73 %, för djupa för en ren våg 4. Det kan vara början på en större korrektion. Strukturen är OKLAR.'),
 ('ASM International (ASM.AS)','Rekyl på 58 % och vinsttillväxt −20 %. Varken struktur eller fundamenta är tydliga nog.'),
 ('Broadcom (AVGO)','Stegvis lägre toppar sedan maj och kraftigt brott under 200-dagarssnittet (−20 %). Ingen tydlig vågräkning (OKLAR).'),
 ('Advantest (6857.T)','Kursen sjudubblades på ett och ett halvt år: utsträckt våg 5. Hög risk för en större ABC-korrektion.'),
 ('MediaTek (2454.TW)','P/E 61 på historisk vinst och en rörelse på +195 % senaste året.'),
 ('Hitachi (6501.T)','Ny 52-veckorsbotten (4301) bara veckor efter rekordnivån, vilket bryter strukturen. Sidledes intervall sedan 2025 (OKLAR).'),
 ('Oracle (ORCL)','−54 % från toppen och fortsatt nedåtgående. Oron gäller lånefinansierade AI-investeringar, alltså fundamenta.'),
 ('Axon (AXON)','−60 % från toppen och trendbrott. Ingen korrektionsstruktur i en upptrend.'),
 ('Palo Alto Networks (PANW)','P/E 785 på historisk vinst och EV/Sales 22: orimlig värdering.'),
 ('Novo Nordisk (NOVO-B.CO)','En flerårig nedtrend med fundamentala orsaker. Ingen etablerad upptrend.'),
 ('Southern Copper (SCCO)','EV/Sales 8,4 och analytikernas snittbetyg 3,8 (sälj).'),
 ('Saab (SAAB-B.ST) och Kongsberg (KOG.OL)','Sidledes intervall och framåtblickande P/E 30–62. Inget tydligt köpläge.'),
 ('NKT (NKT.CO)','Motstridiga nyckeltal hos Yahoo (börsvärde 0, EV/EBITDA 64). Datakraven är inte uppfyllda.'),
 ('Howmet (HWM) och Safran (SAF.PA)','Djupa rekyler (57–58 %) efter värderingskompression. P/E 24–31 lämnar liten säkerhetsmarginal.'),
 ('Roche (ROG.SW) och Schneider (SCHN)','Kursdata kunde inte hämtas (fel ticker eller ingen data). Datakraven är inte uppfyllda.'),
]

# ---- Nya bolag från användarens bevakningslista (9 nov kväll) ----
S['NFLX'] = dict(
  name='Netflix', exch='NASDAQ', wave='C', conf='Medel', sector='Media / streaming',
  why='En ABC-korrektion har nått exakt 61,8 % av uppgången 2022–25, samtidigt som framåtblickande P/E är 17 och det fria kassaflödet 25 mdr USD. Marknaden har blivit mycket pessimistisk, men ingen vändning är bekräftad än.',
  count='Uppgången 2022 ≈16,3 → ATH 134,12 (30 jun 2025). A → 75,01 (23 feb 2026). B → 108,95 (16 apr). C → 61,39 (29 okt), där C ≈ 0,8 × A. 61,8 % av uppgången 2022–25 ligger på 61,3, alltså precis vid botten.',
  alt='C-vågen förlängs mot 1,0 × A (≈50) eller ännu lägre om tillväxten fortsätter att besvika.',
  support='61,4 · 58', resist='66,4 · 72,6 · 81 (200-dagars)', zone='61–66',
  confirm='Stängning över 72,6 (toppen 15 okt). Det bryter serien av lägre toppar.',
  inval='Stängning under 58, alltså tydligt under 61,8 %-nivån.',
  t1=81, t2=108.95, stop=58, t1txt='81 (200-dagarssnittet)', t2txt='109 (B-toppen)',
  fund='Framåtblickande P/E 16,9, EV/EBITDA 16,9, rörelsemarginal 35 % och fritt kassaflöde 25,5 mdr USD (12 mån). Omsättningstillväxt +12 % och vinsttillväxt +48 %. Under 2026 har aktien fallit på alla fyra rapporterna och på ett misslyckat bud på Warner Bros. Kursserien är splitjusterad (10:1).',
  psych='Ett kvalitetsbolag har värderats ned från tillväxtpremie till P/E 17. Det är just den typ av pessimism som kan vara överdriven. Säljtrycket har ännu inte vänt.',
  scores=(6,8,9,7,8))

S['UBER'] = dict(
  name='Uber', exch='NYSE', wave='1', conf='Låg–medel', sector='Transport / plattform',
  why='En ABC-korrektion på 37 % verkar avslutad med en trippelbotten runt 64–65. Kursen har stigit 9 % på en vecka. En möjlig våg 1 har startat men är obekräftad.',
  count='ATH 101,99 (22 sep 2025). A → 65,41 (27 jul 2026). B → 82,36 (26 aug). C → 64,04 (29 okt), en flat där C slutar strax under A. Ny våg 1 pågår från 64,04.',
  alt='Ett sidledes intervall mellan 60 och 100 sedan 2024 som kan pågå ett år till.',
  support='66 · 64,0', resist='72,9 (200-dagars) · 82,4 · 102', zone='66–71',
  confirm='Stängning över 72,9 och därefter över 82,36 (B-toppen).',
  inval='Stängning under 64,04.', t1=82.36, t2=101.99, stop=64.04, t1txt='82,4 (B-toppen)', t2txt='102 (ATH)',
  fund='Framåtblickande P/E 16,2 (Avanza visar P/E 41,9 på historisk vinst, som påverkas av en engångsskatteeffekt året innan). Fritt kassaflöde 7,4 mdr USD och nettoskuld 7,7 mdr USD.',
  psych='Oron för robotaxi som ska göra plattformen överflödig har pressat aktien. Trippelbotten är ett tecken på att säljarna börjar ta slut.',
  scores=(6,7,8,6,9))

S['NIBE-B.ST'] = dict(
  name='NIBE', exch='Nasdaq Stockholm', wave='2', conf='Låg–medel', sector='Värmepumpar / klimat',
  why='En ny upptrend efter en björnmarknad på 77 %. Bottnarna stiger (31,2 → 31,9 → 34,5) och kursen står precis under utbrottsnivån 46,5. Ett utbrott skulle bekräfta våg 3.',
  count='Björnmarknad 136,8 (2021) → 31,21 (21 nov 2025). Dubbelbotten 31,93 (19 mar 2026). Våg 1 → 42,7 (maj). Våg 2 → 34,53 (23 jun). Våg 3 testar nu toppen 46,47 (4 nov).',
  alt='Uppgången är bara en B-våg i en längre bottenbildning, och kursen faller tillbaka mot 35.',
  support='42,7 · 39,7 (200-dagars) · 34,5', resist='46,5', zone='42–45',
  confirm='Veckostängning över 46,5.', inval='Stängning under 34,53.',
  t1=52, t2=71.5, stop=34.53, t1txt='52 (våg 3 = 1,618 × våg 1)', t2txt='71,5 (38,2 % av björnmarknaden)',
  fund='Framåtblickande P/E 26,5, EV/EBITDA 19,2, rörelsemarginal 11 % och vinsttillväxt +53 % från låg nivå. Nettoskuld ≈18 mdr SEK. Värderingen förutsätter fortsatt återhämtning.',
  psych='Ett tidigare favoritbolag som de flesta har gett upp. Vändningen sker i stillhet utan hype.',
  scores=(6,6,5,6,8))

S['OKTA'] = dict(
  name='Okta', exch='NASDAQ', wave='2', conf='Medel', sector='Cybersäkerhet / identitet',
  why='En kraftig ny våg 1 (+275 %) följd av en våg 2 på 41 % efter inkluderingen i S&P 500. Strukturen är tydlig, men värderingen är hög.',
  count='Botten 62,66 (10 apr 2026), våg 1 → 235,00 (12 okt). Våg 2 pågår: botten 164,18 (6 nov) = 41 %. 50 %-nivån ligger på 148,8 och 61,8 %-nivån på 128,5.',
  alt='Uppgången var en hel spekulativ impuls, nu följd av en djupare ABC mot 128–149.',
  support='164 · 149 · 128', resist='187 · 226 · 235', zone='149–175',
  confirm='Stängning över 187 och därefter över 226.', inval='Stängning under 128,5 (61,8 %).',
  t1=235, t2=336, stop=128.5, t1txt='235 (toppen på våg 1)', t2txt='≈336 (våg 3 lika lång som våg 1)',
  fund='P/E 107 på historisk vinst och 40,5 framåtblickande. Omsättningstillväxt bara +11 %, rörelsemarginal 13 %, nettokassa 2,2 mdr USD. Inkluderades i S&P 500 den 4 nov, och rekylen kom efter att indexköpen var klara.',
  psych='Hype kring säkerhet för AI-agenter och indexköp drev uppgången. När köpen var klara kom vinsthemtagning.',
  scores=(6,7,3,6,9))

S['SPOT'] = dict(
  name='Spotify', exch='NYSE', wave='3', conf='Medel', sector='Media / ljud',
  why='En våg 3 har startat efter en dubbelbotten (405/411). Kursen ligger över toppen på våg 1 men 20 % under ATH.',
  count='ATH 785 (27 jun 2025). Korrektion → 405 (5 feb 2026). Våg 1 → 570,64. Våg 2 → 411,24 (6 maj, dubbelbotten). Våg 3 → 635 (5 nov).',
  alt='Uppgången är en B-våg och toppen bildas nära 640.', support='571 · 538 · 500 (200-dagars)', resist='635 · 785',
  zone='Rekyl mot 571', confirm='Bekräftad över 570,6.', inval='Under 538 försvagas bilden.', t1=785, t2=None, stop=538,
  fund='Framåtblickande P/E 35, nettokassa 6,6 mdr EUR, omsättningstillväxt +16 %.', psych='Förtroendet har kommit tillbaka.', scores=(6,8,4,5,9))

S['CEG'] = dict(
  name='Constellation Energy', exch='NASDAQ', wave='C', conf='Låg–medel', sector='Kärnkraft / el',
  why='En flat-korrektion med dubbelbotten (228,6/231,3) efter ett fall på 45 %. Kursen steg 10,7 % i dag. Analysen kräver bekräftelse eftersom det fria kassaflödet är negativt.',
  count='ATH 412,7 (15 okt 2025). A → 228,63 (1 jul 2026). B → 309,8 (6 okt). C → 231,3 (5 nov), dubbelbotten med A.',
  alt='Ett brott under 228 öppnar för en förlängd C-våg.', support='231 · 228,6', resist='279 (200-dagars) · 309,8 · 412,7',
  zone='240–270', confirm='Stängning över 309,8.', inval='Stängning under 228,6.', t1=309.8, t2=412.7, stop=228.63,
  t1txt='309,8 (B-toppen)', t2txt='412,7 (ATH)',
  fund='Framåtblickande P/E 20,6 och EV/EBITDA 14,2. Fritt kassaflöde −6,6 mdr USD och nettoskuld 24 mdr USD.', psych='Aktien är i centrum för oron kring elförsörjningen till datacenter.', scores=(5,6,6,6,8))

S['BE'] = dict(
  name='Bloom Energy', exch='NYSE', wave='A', conf='Låg', sector='Bränsleceller',
  why='Kursen steg 23 gånger på 14 månader och har sedan fallit 56 %. Fallet är för djupt och värderingen för hög för en ren våg 4.',
  count='15,15 (9 apr 2025) → 351,28 (25 jun 2026) → 156,0 (5 nov), 58 % retracement.',
  alt='En djup våg 4 som har avslutats vid 156.', support='156', resist='223 (200-dagars) · 296', zone='–', confirm='–', inval='–',
  t1=None, t2=None, stop=None, fund='P/E 118, EV/Sales 13,5, omsättningstillväxt +138 %.', psych='Spekulativt, med stora svängningar. Kursen steg 12,4 % i dag.', scores=(3,6,2,3,7))

S['MRVL'] = dict(
  name='Marvell', exch='NASDAQ', wave='A', conf='Låg–medel', sector='AI-halvledare',
  why='Rekylen är 70 % av uppgången 2025–26, och aktien föll 43 % på en månad på köpet av Lumentum, som betalas med egna aktier.',
  count='47,09 (7 apr 2025) → 329,88 (18 jun 2026) → 132,54 (5 nov).',
  alt='En mycket djup våg 2.', support='132,5', resist='185 (200-dagars)', zone='–', confirm='Stängning över 185.', inval='–',
  t1=None, t2=None, stop=None, fund='Framåtblickande P/E 21, EV/Sales 13. Köpet av Lumentum späder ut ägandet.', psych='Kursen steg 10 % i dag efter kapitulationen.', scores=(3,7,6,4,8))

REJECTED += [
 ('CoreWeave (CRWV), Nebius (NBIS), SoundHound (SOUN), NIO','Nedåtgående trender med lägre toppar och lägre bottnar (−53 till −73 % från toppen). CoreWeave och Nebius har negativt fritt kassaflöde (−9 till −10 mdr USD) och CoreWeave en nettoskuld på 46 mdr USD.'),
 ('Cerebras (CBRS)','Börsnoterades i maj 2026, så historiken är för kort för en vågräkning (krav: minst 2–3 år). Kursen ligger 75 % under toppen.'),
 ('Robinhood (HOOD), DoorDash (DASH), Take-Two (TTWO), Addtech (ADDT B), Rusta, Svolder, Caledonia (CMCL)','Sidledes intervall utan tydlig impuls eller avslutad korrektion (OKLAR). Take-Two: dubbelbotten 190 som kan bli intressant. Addtech: möjlig våg 4-triangel mellan 280 och 358.'),
 ('Nike (NKE)','En möjlig C-botten vid 31,97, men omsättningen minskar (−4 %), analytikernas snittbetyg är 2,9 och kursmålet ligger under kursen. Fallet har fundamentala orsaker.'),
 ('ARKG, TQQQ, IWM (fonder)','Fonder och hävstångsprodukter ingår inte i bolagsanalysen. TQQQ är tredubbelt hävstångad, och dess värde krymper när marknaden svänger utan riktning.'),
]

WATCHLIST = [  # (ticker, kort bedömning) – användarens sökningar
 ('AMD','Våg 5, eller en studs i våg 4. P/E 96–110 på historisk vinst. Inget köpläge.'),
 ('MRVL','Våg A. Studsen kom efter kapitulation och köpet av Lumentum späder ut ägandet. Vänta.'),
 ('LRCX','Rekylen är 57 % av uppgången, för djupt för en ren våg 4. OKLAR, och studsen är inte en bekräftelse.'),
 ('MU','Våg A efter en uppgång på 20 gånger. Framåtblickande P/E 3,3 är ett tecken på toppen i vinstcykeln.'),
 ('SKHY','Samma struktur som SK hynix i Seoul: våg A.'),
 ('TSM','Topplistan, nr 1. Våg 4 vid 38,2 %. Bekräftelse kräver stängning över 405.'),
 ('ORCL','Nedtrend, −52 % från toppen. Oron gäller lånefinansierade AI-investeringar. Bortsorterad.'),
 ('CEG','Möjlig avslutad C-våg (dubbelbotten 229/231). Bekräftas över 309,8.'),
 ('BE','Parabolisk uppgång (23 gånger) och sedan −56 %. Våg A. Spekulativ.'),
 ('NBIS','Rekyl 82 %, negativt fritt kassaflöde. Bortsorterad.'),
 ('CRWV','Nedtrend och nettoskuld 46 mdr USD. Bortsorterad.'),
 ('CBRS','För kort historik (börsnoterad maj 2026). Bortsorterad.'),
 ('UBER','Möjlig avslutad ABC och ny våg 1. Bekräftas över 82,4.'),
 ('HOOD','Sidledes, med lägre toppar. OKLAR.'),
 ('OKTA','Våg 2 efter en kraftig våg 1. Dyr värdering.'),
 ('SPOT','Våg 3 har startat, dubbelbotten 405/411.'),
 ('NFLX','C-vågen kan vara slut vid 61,8 % och P/E är 17. Bevakning med hög potential.'),
 ('LLY','Våg 3, ny rekordnivå i dag. Inget rekylläge.'),
 ('NOVO-B.CO','Flerårig nedtrend. Bortsorterad.'),
 ('NKE','Möjlig C-botten, men fundamenta försämras. Vänta.'),
 ('DASH','Sidledes intervall. OKLAR.'),
 ('TTWO','Dubbelbotten vid 190, i övrigt sidledes. OKLAR.'),
 ('SOUN','Nedtrend. Bortsorterad.'),
 ('NIO','Nedtrend. Bortsorterad.'),
 ('CMCL','Sidledes. OKLAR.'),
 ('BESI.AS','Rekyl 73 %. OKLAR.'),
 ('NIBE-B.ST','Ny upptrend. Våg 3 bekräftas vid veckostängning över 46,5.'),
 ('ADDT-B.ST','Intervall 280–358, möjlig triangel. OKLAR.'),
 ('SVOL-B.ST','Investmentbolag nära toppen. Analyseras via innehaven.'),
 ('RUSTA.ST','Sidledes. OKLAR.'),
]
