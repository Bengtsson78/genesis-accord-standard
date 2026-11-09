import json, pandas as pd, numpy as np
def load(t,suf):
    j=json.load(open(f'data/{t}_{suf}.json'))['chart']['result'][0]
    q=j['indicators']['quote'][0]
    adj=j['indicators'].get('adjclose',[{}])[0].get('adjclose', q['close'])
    df=pd.DataFrame({'o':q['open'],'h':q['high'],'l':q['low'],'c':q['close'],'a':adj,'v':q['volume']},
        index=pd.to_datetime(j['timestamp'],unit='s')).dropna(subset=['c'])
    # split-adjusted high/low via ratio a/c (also div-adjusts) -> use close-ratio only for splits: yahoo c is split-adjusted already
    if suf in ('w','m') and len(df)>2 and (df.index[-1]-df.index[-2]).days<6: df=df.iloc[:-1]
    return df, j['meta']
def zigzag(s, th):
    piv=[(s.index[0],s.iloc[0],'?')]; trend=1; ext_i=s.index[0]; ext=s.iloc[0]
    for i,x in s.items():
        if trend>=0:
            if x>ext: ext,ext_i=x,i
            elif x<ext*(1-th) :
                piv.append((ext_i,ext,'H')); trend=-1; ext,ext_i=x,i; continue
        if trend<=0:
            if x<ext: ext,ext_i=x,i
            elif x>ext*(1+th):
                piv.append((ext_i,ext,'L')); trend=1; ext,ext_i=x,i
    piv.append((ext_i,ext,'H*' if trend>0 else 'L*'))
    return piv[1:]
