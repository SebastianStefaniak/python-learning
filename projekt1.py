import pandas as pd
import numpy as np 
import yfinance as yf
import matplotlib.pyplot as plt
import math


stocks = ["ABPL.WA", "EAT.WA", "ASB.WA", "ACP.WA", "ASE.WA", "APR.WA", "BHW.WA", "MIL.WA",
    "BFT.WA", "BNP.WA", "CRI.WA", "CBF.WA", "CPS.WA", "DVL.WA", "DIA.WA", "DOM.WA",
    "ENA.WA", "EUR.WA", "GPW.WA", "ATT.WA", "CAR.WA", "JSW.WA", "LBW.WA", "MRB.WA",
    "MBR.WA", "NEU.WA", "NWG.WA", "OPL.WA", "PEP.WA", "PXM.WA", "RBW.WA", "SNT.WA",
    "TEN.WA", "TXT.WA", "VRC.WA", "VOX.WA", "WPL.WA", "XTB.WA", "GRE.WA", "GPP.WA"
]

data = yf.download(stocks,start='2020-01-01', end='2026-04-01')['Close']
data=data.drop(columns=['CBF.WA','CRI.WA','DIA.WA','GPP.WA','ABPL.WA','VRC.WA'], axis=1,errors='ignore')
data = data.replace(0,np.nan).dropna(how= 'all')

returns=data.pct_change()
mean_returns=returns.mean()

var_95 = returns.quantile(0.05)
cvar_95=returns[returns<=var_95].mean()
results = pd.DataFrame({
    'Średni zwrot (%)': (mean_returns * 100).round(4),
    'Var 95 (%)' : (var_95*100).round(4),
    'Cvar 95 (%)' :(cvar_95*100).round(4)
})
results = results.sort_values(by='Średni zwrot (%)',ascending=False)

print(results[(results['Średni zwrot (%)']>0.2) & (results['Var 95 (%)']>-4)])


