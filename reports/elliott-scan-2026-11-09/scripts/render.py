import json, html, re
from content import S, TOP, WATCH, REJECTED, WATCHLIST
from lib import load
D = json.load(open('mapdata.json'))
E = html.escape

def sv(x, dec=1, sign=False):
    if x is None: return '–'
    s = f"{x:+,.{dec}f}" if sign else f"{x:,.{dec}f}"
    return s.replace(',', ' ').replace('.', ',').replace('-', '−')
def pxf(t):
    v = D[t]['px']; dec = 0 if v >= 10000 else 2
    return sv(v, dec)
def pct(x):
    if x is None: return '<span class="na">–</span>'
    cls = 'up' if x > 0 else 'dn' if x < 0 else ''
    return f'<span class="{cls}">{sv(x,1,True)} %</span>'
def sid(t): return 'a-' + re.sub(r'[^A-Za-z0-9]', '', t)
def big(x, cur):
    if x is None: return '–'
    a = abs(x)
    if a >= 1e12: s = sv(x/1e12, 2) + ' bn'
    elif a >= 1e9: s = sv(x/1e9, 1) + ' mdr'
    else: s = sv(x/1e6, 0) + ' mn'
    return f'{s} {cur}'
def num(x, dec=1):
    return '–' if x is None else sv(x, dec)
def pc(x):
    return '–' if x is None else sv(x*100, 0) + ' %'

WAVES = ['1','2','3','4','5','A','B','C']
WCOL = {'1':'w1','2':'w2','3':'w3','4':'w4','5':'w5','A':'wa','B':'wb','C':'wc'}
WNAME = {'1':'Våg 1','2':'Våg 2','3':'Våg 3','4':'Våg 4','5':'Våg 5','A':'Våg A','B':'Våg B','C':'Våg C'}

def comp(t): s = S[t]['scores']; return sum(s)/len(s)
def rr(t):
    s = S[t]; p = D[t]['px']
    if s.get('t1') is None or s.get('stop') is None: return None
    return (s['t1'] - p) / (p - s['stop'])
def up(t, k): v = S[t].get(k); return None if v is None else (v / D[t]['px'] - 1) * 100

# ---------- SVG map ----------
P = {'0':(40,560),'1':(190,400),'2':(290,500),'3':(560,170),'4':(680,320),'5':(850,110),'A':(980,380),'B':(1060,290),'C':(1190,540)}
seq = ['0','1','2','3','4','5','A','B','C']
segs = []
for a, b in zip(seq, seq[1:]):
    (x1,y1),(x2,y2) = P[a], P[b]
    segs.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="seg s{WCOL[b]}"/>')
labels = []
for k in seq[1:]:
    x, y = P[k]
    dy = -26 if k in '135B' else 30
    labels.append(f'<g class="node"><circle cx="{x}" cy="{y}" r="15" class="nd {WCOL[k]}"/><text x="{x}" y="{y+5}" class="ndt">{k}</text></g>')
place = {  # wave -> (x, y0) for pill stacks
  '1': (16, 220), '2': (200, 528), '3': (226, 112), '4': (590, 348), '5': (610, 18), 'A': (826, 408), 'C': (1034, 572)}
bywave = {}
for t, s in S.items(): bywave.setdefault(s['wave'], []).append(t)
for w in bywave: bywave[w].sort(key=lambda t: -comp(t))
pills = []
for w, ts in bywave.items():
    x0, y0 = place[w]
    for i, t in enumerate(ts):
        y = y0 + i * 46; d = D[t]; s = S[t]
        star = ' ★' if t in TOP else ''
        pills.append(
          f'<a href="#{sid(t)}" class="pill-a"><g class="pill {WCOL[w]}"><rect x="{x0}" y="{y}" width="200" height="40" rx="6" class="pr"/>'
          f'<text x="{x0+10}" y="{y+16}" class="pt1">{E(t)}{star}<tspan class="pt1b" dx="6">{pxf(t)} {E(d["cur"])}</tspan></text>'
          f'<text x="{x0+10}" y="{y+32}" class="pt2">i dag {sv(d["d1"],1,True)} % · 1 mån {sv(d["m1"],0,True)} %</text></g></a>')
svg = f'''<svg viewBox="0 0 1240 800" role="img" aria-labelledby="maptitle mapdesc" class="map">
<title id="maptitle">Elliott-karta</title><desc id="mapdesc">Elliott-cykeln våg 1 till 5 och A till C med varje godkänd aktie placerad vid sin bedömda våg.</desc>
<rect x="0" y="0" width="1240" height="800" class="mapbg"/>
<g class="grid">{''.join(f'<line x1="0" y1="{y}" x2="1240" y2="{y}"/>' for y in range(80,800,80))}</g>
<text x="20" y="788" class="axis">Tid →</text>
<text x="1220" y="788" class="axis" text-anchor="end">Impuls 1–5 · korrektion A–B–C</text>
{''.join(segs)}
<line x1="{P['0'][0]}" y1="{P['0'][1]}" x2="{P['0'][0]}" y2="{P['0'][1]}" />
{''.join(labels)}
{''.join(pills)}
</svg>'''

# ---------- Top cards ----------
def scorebar(lbl, v):
    return f'<div class="sc"><span>{lbl}</span><span class="bar"><i style="width:{v*10}%"></i></span><b>{v}</b></div>'
SC = ['Teknisk timing','Fundamental kvalitet','Värdering','Risk/reward','Datatillförlitlighet']
def card(t, rank):
    s = S[t]; d = D[t]; w = s['wave']
    t1 = up(t,'t1'); t2 = up(t,'t2'); dn = (s['stop']/d['px']-1)*100
    intr = f'<span class="intr">Intradag 9 nov ≈12:10 CET: {sv(d["intraday"],2)}</span>' if d.get('intraday') else ''
    t1txt = s.get('t1txt', f'{sv(s["t1"],2)} (tidigare topp)')
    rows = [
      ('Köpzon', s['zone']), ('Bekräftelse', s['confirm']), ('Ogiltig om', s['inval']),
      ('Mål 1', f'{t1txt} → <b class="up">{sv(t1,1,True)} %</b>'),
    ]
    if t2 is not None: rows.append(('Mål 2', f'{s["t2txt"]} → <b class="up">{sv(t2,1,True)} %</b>'))
    rows.append(('Nedsida till stopp', f'{sv(s["stop"],2)} → <b class="dn">{sv(dn,1,True)} %</b>'))
    rows.append(('Risk/reward (mål 1)', f'<b>{sv(rr(t),1)} : 1</b>'))
    return f'''<article class="top" id="top-{sid(t)}">
<header><span class="rank">{rank}</span><div class="tt"><h3>{E(s["name"])}</h3><p class="meta">{E(t)} · {E(s["exch"])} · {E(s["sector"])}</p></div>
<span class="chip {WCOL[w]}">{WNAME[w]}</span></header>
<div class="pxrow"><span class="px">{pxf(t)} <small>{E(d["cur"])}</small></span><span class="pd">Kurs 9 nov kl. 21:48 (USA: under handel; Europa/Asien: stängning)</span>{intr}</div>
<p class="why">{E(s["why"])}</p>
<dl class="lv">{''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a,b in rows)}</dl>
<div class="scores">{''.join(scorebar(l,v) for l,v in zip(SC,s["scores"]))}<div class="sc tot"><span>Sammanvägt</span><span></span><b>{sv(comp(t),1)}</b></div></div>
<p class="conf">Tillförlitlighet i vågräkningen: <b>{E(s["conf"])}</b> · <a href="#{sid(t)}">Full analys ↓</a></p>
</article>'''
tops = ''.join(card(t, i+1) for i, t in enumerate(TOP))
watch = ''.join(f'''<div class="wcard"><span class="chip {WCOL[S[t]["wave"]]}">{WNAME[S[t]["wave"]]}</span><h4>{E(S[t]["name"])} <small>{E(t)}</small></h4>
<p>{E(S[t]["why"])}</p><p class="small">Köpzon: {E(S[t]["zone"])} · Ogiltig: {E(S[t]["inval"])} · Sammanvägt {sv(comp(t),1)}</p></div>''' for t in WATCH)

# ---------- Table ----------
order = sorted(S, key=lambda t: (WAVES.index(S[t]['wave']), -comp(t)))
trs = []
for t in order:
    d = D[t]; s = S[t]
    evb = d['evebitda']; evs = d['evs']
    if t == 'TSM': evb, evs = 14.4, 10.6
    nd = None if d['debt'] is None or d['cash'] is None else d['debt'] - d['cash']
    if t == 'GS': nd = None
    trs.append(f'''<tr><th scope="row"><a href="#{sid(t)}">{E(t)}</a><span class="sub">{E(s["name"])}</span></th>
<td><span class="chip sm {WCOL[s["wave"]]}">{s["wave"]}</span></td><td class="n">{pxf(t)} <span class="sub">{E(d["cur"])} · {d["date"][5:]}</span></td>
<td class="n">{pct(d["w1"])}</td><td class="n">{pct(d["m1"])}</td><td class="n">{pct(d["m3"])}</td><td class="n">{pct(d["m6"])}</td><td class="n">{pct(d["y1"])}</td>
<td class="n">{big(d["mcap"], d["cur"])}</td><td class="n">{num(d["pe"])}</td><td class="n">{num(d["fpe"])}</td><td class="n">{num(evb)}</td><td class="n">{num(evs)}</td><td class="n">{num(d["peg"],2)}</td>
<td class="n">{pc(d["revg"])}</td><td class="n">{pc(d["epsg"])}</td><td class="n">{pc(d["gm"])}</td><td class="n">{pc(d["om"])}</td><td class="n">{big(d["fcf"], d["fcur"])}</td><td class="n">{big(nd, d["fcur"])}</td>
<td class="n">{num(d["rec"],1)} <span class="sub">n={d["n"]}</span></td><td class="n">{d["hist"]}</td></tr>''')
table = ''.join(trs)

# ---------- Analyses ----------
ans = []
for t in order:
    s = S[t]; d = D[t]
    lv = []
    if s.get('t1') is not None: lv.append(f'Mål 1: {sv(s["t1"],2)} ({sv(up(t,"t1"),1,True)} %)')
    if s.get('t2') is not None: lv.append(f'Mål 2: {sv(s["t2"],2)} ({sv(up(t,"t2"),1,True)} %)')
    if s.get('stop') is not None: lv.append(f'Ogiltig/stopp: {sv(s["stop"],2)} ({sv((s["stop"]/d["px"]-1)*100,1,True)} %)')
    r = rr(t)
    if r is not None: lv.append(f'R/R ≈ {sv(r,1)} : 1')
    ans.append(f'''<details class="an" id="{sid(t)}" {"open" if t in TOP else ""}><summary><span class="chip sm {WCOL[s["wave"]]}">{s["wave"]}</span><b>{E(s["name"])}</b> <span class="sub">{E(t)} · {pxf(t)} {E(d["cur"])}</span><span class="cs">{sv(comp(t),1)}</span></summary>
<div class="ab"><dl class="lv">
<dt>Huvudscenario</dt><dd>{E(s["count"])}</dd><dt>Alternativ</dt><dd>{E(s["alt"])}</dd>
<dt>Stöd</dt><dd>{E(s["support"])}</dd><dt>Motstånd</dt><dd>{E(s["resist"])}</dd>
<dt>Köpzon</dt><dd>{E(s["zone"])}</dd><dt>Bekräftelse</dt><dd>{E(s["confirm"])}</dd><dt>Ogiltigförklaring</dt><dd>{E(s["inval"])}</dd>
<dt>Nivåer</dt><dd>{" · ".join(lv) if lv else "–"}</dd>
<dt>Fundamenta</dt><dd>{E(s["fund"])}</dd><dt>Psykologi</dt><dd>{E(s["psych"])}</dd>
<dt>Betyg</dt><dd>Timing {s["scores"][0]} · Fundamenta {s["scores"][1]} · Värdering {s["scores"][2]} · R/R {s["scores"][3]} · Data {s["scores"][4]} · <b>Sammanvägt {sv(comp(t),1)}</b> · Tillförlitlighet: {E(s["conf"])}</dd>
</dl></div></details>''')
analyses = ''.join(ans)

# ---------- ranking ----------
rk = sorted(S, key=lambda t: -comp(t))
rank_rows = ''.join(f'<tr><td class="n">{i+1}</td><th scope="row"><a href="#{sid(t)}">{E(S[t]["name"])}</a> <span class="sub">{E(t)}</span></th><td><span class="chip sm {WCOL[S[t]["wave"]]}">{S[t]["wave"]}</span></td>'
    + ''.join(f'<td class="n">{v}</td>' for v in S[t]['scores']) + f'<td class="n"><b>{sv(comp(t),1)}</b></td><td>{E(S[t]["conf"])}</td></tr>' for i, t in enumerate(rk))
rejected = ''.join(f'<li><b>{E(a)}</b> {E(b)}</li>' for a, b in REJECTED)

# ---------- today / watchlist ----------
def quick(t):
    d,m=load(t,'d'); c=d.c; p=float(c.iloc[-1]); last=c.index[-1]
    ref=c[c.index<=last-pd.Timedelta(days=7)]
    return p, (p/float(c.iloc[-2])-1)*100, (p/float(ref.iloc[-1])-1)*100, (p/float(d.h.iloc[-252:].max())-1)*100, m.get('currency'), str(last.date())
import pandas as pd
wl=[]
for t,txt in sorted(WATCHLIST, key=lambda x: -quick(x[0])[1]):
    p,d1,w1,hi,cur,dt=quick(t)
    w=S[t]['wave'] if t in S else None
    chip=f'<span class="chip sm {WCOL[w]}">{w}</span>' if w else '<span class="chip sm na-c">–</span>'
    name=f'<a href="#{sid(t)}">{E(t)}</a>' if t in S else E(t)
    wl.append(f'<tr><th scope="row">{name}</th><td class="n">{sv(p,2)} <span class="sub">{cur}</span></td><td class="n">{pct(d1)}</td><td class="n">{pct(w1)}</td><td class="n">{pct(hi)}</td><td>{chip}</td><td>{E(txt)}</td></tr>')
IDXN=[('^SOX','SOX halvledare'),('^NDX','Nasdaq-100'),('^GSPC','S&P 500'),('^STOXX','STOXX 600'),('^OMX','OMXS30'),('^N225','Nikkei 225'),('^TWII','Taiwan'),('^KS11','KOSPI'),('^VIX','VIX')]
ctx=[]
for t,n in IDXN:
    p,d1,w1,hi,cur,dt=quick(t)
    ctx.append(f'<div><span>{n}</span><b class="{"up" if d1>0 else "dn"}">{sv(d1,1,True)} %</b><span>i dag · {sv(hi,1,True)} % från 52-v-topp</span></div>')
tpl = open('template.html').read()
out = (tpl.replace('{{SVG}}', svg).replace('{{TOPS}}', tops).replace('{{WATCH}}', watch).replace('{{TABLE}}', table)
          .replace('{{ANALYSES}}', analyses).replace('{{RANK}}', rank_rows).replace('{{REJECTED}}', rejected).replace('{{WL}}', ''.join(wl)).replace('{{CTX}}', ''.join(ctx)))
open('elliott-scan.html', 'w').write(out)
print('ok', len(out))
