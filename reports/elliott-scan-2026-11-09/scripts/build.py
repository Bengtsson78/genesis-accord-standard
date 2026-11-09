import json; from lib import *
F={}; [F.update(json.load(open(f))) for f in ['fund1.json','fund2.json','fund3.json']]
MAP=['ISRG','BKNG','MYCR.ST','ETN','SPGI','MCO','LLY','TSM','ASML.AS','GS','GOOGL','PWR','6501.T','ABBN.SW','NVDA','AMD','MU','000660.KS','CAT','VRT','RHM.DE','KLAC']
EU=('.AS','.ST','.DE','.SW','.PA','.MI','.CO','.OL','.L')
out={}
for t in MAP:
    d,m=load(t,'d'); mo,_=load(t,'m'); intr=None
    if t.endswith(EU) and d.index[-1].date().isoformat()=='2026-11-09':
        intr=float(d.c.iloc[-1]); d=d.iloc[:-1]
    c=d.c; p=float(c.iloc[-1]); last=c.index[-1]
    def ch(days):
        ref=c[c.index<=last-pd.Timedelta(days=days)]; return round((p/ref.iloc[-1]-1)*100,1)
    f=F.get(t,{})
    out[t]=dict(name=f.get('longName'),cur=m.get('currency'),px=round(p,2),date=str(last.date()),intraday=intr,
      w1=ch(7),m1=ch(30),m3=ch(91),m6=ch(182),y1=ch(365),hist=int(mo.index[0].year),
      mcap=f.get('marketCap'),pe=f.get('trailingPE'),fpe=f.get('forwardPE'),evebitda=f.get('enterpriseToEbitda'),evs=f.get('enterpriseToRevenue'),
      peg=f.get('trailingPegRatio'),revg=f.get('revenueGrowth'),epsg=f.get('earningsGrowth'),gm=f.get('grossMargins'),om=f.get('operatingMargins'),
      fcf=f.get('freeCashflow'),debt=f.get('totalDebt'),cash=f.get('totalCash'),rec=f.get('recommendationMean'),n=f.get('numberOfAnalystOpinions'),tgt=f.get('targetMeanPrice'),fcur=f.get('financialCurrency'))
json.dump(out,open('mapdata.json','w'),indent=1)
for t,v in out.items(): print(t,v['px'],v['date'],v['intraday'],v['w1'],v['m1'],v['m3'],v['m6'],v['y1'],v['mcap'],v['fcur'])
