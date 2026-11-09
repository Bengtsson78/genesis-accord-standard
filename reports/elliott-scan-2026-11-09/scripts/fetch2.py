import json, os, time, urllib.request, urllib.parse, glob
H={'User-Agent':'Mozilla/5.0'}
ts=sorted({os.path.basename(f)[:-7] for f in glob.glob('data/*_d.json')})
for t in ts:
    for rng,iv,suf in [('max','1mo','m'),('10y','1wk','w')]:
        u=f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(t)}?range={rng}&interval={iv}&events=div,split"
        try: json.dump(json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30)),open(f'data/{t}_{suf}.json','w'))
        except Exception as e: print(t,e)
        time.sleep(0.1)
print(len(ts))
