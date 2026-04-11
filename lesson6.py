import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

stock='AAPL'
market='^GSPC'
risk_free_rate=0.03


data=yf.download([stock,market],start='2020-01-01',end='2025-12-31')['Close'].dropna()
returns=data.pct_change().dropna()

cov_matrix=returns.cov()
beta=cov_matrix.loc[stock,market]/cov_matrix.loc[market,market]
print('Beta:',beta)

market_return=returns[market].mean()*252
expected_return=risk_free_rate+beta*(market_return-risk_free_rate)

print('Expected return:',round(expected_return,2))

plt.scatter(returns[market],returns[stock],alpha=0.5)

slope=beta
intercept=returns[market].mean()-beta*returns[market].mean()

x=np.linspace(returns[market].min(), returns[market].max(),100)
y=intercept+slope*x

plt.plot(x,y,color='red')
plt.xlabel('Market Returns')
plt.ylabel('Stock returns')
plt.title('CAPM regression')
plt.show()