import yfinance as yf, json, sys, time
K=['longName','currency','currentPrice','marketCap','trailingPE','forwardPE','enterpriseToEbitda','enterpriseToRevenue','trailingPegRatio','revenueGrowth','earningsGrowth','grossMargins','operatingMargins','freeCashflow','totalDebt','totalCash','ebitda','sharesPercentSharesOut','recommendationMean','numberOfAnalystOpinions','targetMeanPrice','targetLowPrice','targetHighPrice','mostRecentQuarter','sector','industry','fiftyTwoWeekHigh','fiftyTwoWeekLow','returnOnEquity','debtToEquity','financialCurrency']
out={}
for t in sys.argv[1:]:
    try:
        i=yf.Ticker(t).info; out[t]={k:i.get(k) for k in K}
    except Exception as e: out[t]={'err':str(e)}
    time.sleep(0.3)
json.dump(out,open('fund.json','w'),indent=0,default=str)
for t,v in out.items():
    if 'err' in v: print(t,v); continue
    mc=(v['marketCap'] or 0)/1e9; nd=((v['totalDebt'] or 0)-(v['totalCash'] or 0))/1e9; fcf=(v['freeCashflow'] or 0)/1e9
    g=lambda k,m=1,dg=1: '-' if v.get(k) is None else f"{v[k]*m:.{dg}f}"
    print(f"{t:10} {str(v['longName'])[:22]:22} mc={mc:.0f} {v['financialCurrency']} PE={g('trailingPE')} fPE={g('forwardPE')} EV/EBITDA={g('enterpriseToEbitda')} EV/S={g('enterpriseToRevenue')} PEG={g('trailingPegRatio',1,2)} revG={g('revenueGrowth',100,0)}% epsG={g('earningsGrowth',100,0)}% GM={g('grossMargins',100,0)}% OM={g('operatingMargins',100,0)}% FCF={fcf:.1f}B ND={nd:.1f}B rec={g('recommendationMean')} n={v['numberOfAnalystOpinions']} tgt={g('targetMeanPrice',1,0)} MRQ={v['mostRecentQuarter']}")
