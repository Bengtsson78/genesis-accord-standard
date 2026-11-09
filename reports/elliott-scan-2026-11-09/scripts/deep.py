import sys; from lib import *
def rsi(s,n=14):
    d=s.diff(); u=d.clip(lower=0).ewm(alpha=1/n).mean(); v=(-d.clip(upper=0)).ewm(alpha=1/n).mean(); return 100-100/(1+u/v)
f=lambda x: f"{x:.4g}"
for t in sys.argv[1:]:
    mo,meta=load(t,'m'); w,_=load(t,'w'); d,_=load(t,'d'); p=d.c.iloc[-1]
    zm=zigzag(mo.c,0.30); zw=zigzag(w.c[w.index>="2023-06-01"],0.14); zd=zigzag(d.c.iloc[-90:],0.07)
    S=lambda z,fmt: ' '.join(f"{k[0]}{f(v)}({i.strftime(fmt)})" for i,v,k in z)
    print(f"\n## {t} {meta.get('currency')} p={f(p)} hist={mo.index[0].year}\n M30: {S(zm[-7:],'%y%m')}\n W14: {S(zw,'%y%m%d')}\n D7: {S(zd,'%m%d')}")
    print(f" RSIm={rsi(mo.c).iloc[-1]:.0f} RSIw={rsi(w.c).iloc[-1]:.0f} RSId={rsi(d.c).iloc[-1]:.0f} vol5/50={d.v.iloc[-5:].mean()/d.v.iloc[-50:].mean():.2f} sma200d={f(d.c.rolling(200).mean().iloc[-1])} sma40w={f(w.c.rolling(40).mean().iloc[-1])} 52wL={f(d.l.iloc[-252:].min())} 5dL={f(d.l.iloc[-5:].min())}")
