import json, os, time, urllib.request, sys
from universe import TICKERS
os.makedirs('data', exist_ok=True)
H={'User-Agent':'Mozilla/5.0'}
def get(t, rng, iv):
    url=f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range={rng}&interval={iv}&events=div,split"
    r=urllib.request.urlopen(urllib.request.Request(url,headers=H),timeout=30)
    return json.load(r)
fail=[]
for t in TICKERS:
    for rng,iv,suf in [('max','1wk','w'),('2y','1d','d')]:
        fn=f'data/{t}_{suf}.json'
        if os.path.exists(fn): continue
        try:
            j=get(t,rng,iv); json.dump(j,open(fn,'w'))
        except Exception as e:
            fail.append((t,suf,str(e)))
        time.sleep(0.15)
print(len(TICKERS),'tickers; fails:',fail)
