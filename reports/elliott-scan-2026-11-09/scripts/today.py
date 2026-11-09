from lib import *; from universe import TICKERS, USER
import json
IDX=['^GSPC','^NDX','^SOX','^STOXX','^N225','^KS11','^TWII','^OMX','^VIX','^NSEI','^HSI','^TNX']
rows=[]
for t in TICKERS+IDX:
    try: d,m=load(t,'d')
    except Exception: continue
    c=d.c
    if len(c)<3: continue
    p=c.iloc[-1]; prev=c.iloc[-2]
    rows.append(dict(t=t,date=str(c.index[-1].date()),p=round(p,2),d1=round((p/prev-1)*100,2),hi52=round((p/d.h.iloc[-252:].max()-1)*100,1)))
df=pd.DataFrame(rows)
pd.set_option('display.width',200,'display.max_rows',400)
print(df[df.t.isin(IDX)].to_string(index=False))
print(df[df.t.isin(USER)].sort_values('d1').to_string(index=False))
s=df[~df.t.isin(IDX)].sort_values('d1')
print('TOP up'); print(s.tail(25).to_string(index=False)); print('DOWN'); print(s.head(8).to_string(index=False))
print('dates', df.date.value_counts().to_dict())
