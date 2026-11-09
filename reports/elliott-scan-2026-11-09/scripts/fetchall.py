import json, os, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from universe import TICKERS
IDX=['^GSPC','^NDX','^SOX','^STOXX','^N225','^KS11','^TWII','^OMX','^VIX','^NSEI','^HSI','^TNX']
H={'User-Agent':'Mozilla/5.0'}
def job(t):
    errs=[]
    for rng,iv,suf in [('max','1mo','m'),('10y','1wk','w'),('2y','1d','d')]:
        u=f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(t)}?range={rng}&interval={iv}&events=div,split"
        for k in range(3):
            try:
                j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30))
                json.dump(j,open(f'data/{t}_{suf}.json','w')); break
            except Exception as e:
                if k==2: errs.append((t,suf,str(e)))
                time.sleep(1)
    return errs
with ThreadPoolExecutor(6) as ex: res=list(ex.map(job, TICKERS+IDX))
print(len(TICKERS),'fails',[e for r in res for e in r])
