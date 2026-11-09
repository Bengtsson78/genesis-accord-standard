from lib import *; from universe import TICKERS
rows=[]
for t in TICKERS:
    try: w,m=load(t,'w'); d,_=load(t,'d'); mo,_=load(t,'m')
    except Exception: continue
    c=d.c; p=c.iloc[-1]; last=c.index[-1]
    def ch(days):
        ref=c[c.index<=last-pd.Timedelta(days=days)]; return (p/ref.iloc[-1]-1)*100 if len(ref) else np.nan
    # major leg: peak = max close last 15 months; origin = min close in the 30 months before the peak
    rec=w.c[w.index>=last-pd.Timedelta(days=455)]; Hi=rec.idxmax(); H=rec.max()
    pre=w.c[(w.index<Hi)&(w.index>=Hi-pd.Timedelta(days=900))]
    L=pre.min() if len(pre) else np.nan; Li=pre.idxmin() if len(pre) else None
    retr=(H-p)/(H-L)*100 if H>L else np.nan
    p5=mo.c[mo.index<=last-pd.Timedelta(days=5*365)]
    rows.append(dict(t=t,p=round(p,2),cur=m.get('currency'),yrs=mo.index[0].year,m1=ch(30),m3=ch(91),y1=ch(365),
      ddH=(p/H-1)*100,retr=retr,L=L,Ld=Li.strftime('%y%m') if Li is not None else '',H=H,Hd=Hi.strftime('%y%m'),
      cagr5=((p/p5.iloc[-1])**0.2-1)*100 if len(p5) else np.nan, vs200=(p/c.rolling(200).mean().iloc[-1]-1)*100))
df=pd.DataFrame(rows).round(1); df.to_csv('screen2.csv',index=False)
pd.set_option('display.width',250,'display.max_rows',400)
f=df[(df.retr>=30)&(df.retr<=85)&(df.cagr5>3)]
print(f.sort_values('retr').to_string(index=False))
