# ===== IMPORTY =====
import pandas as pd                      # praca z danymi (DataFrame)
import yfinance as yf                   # pobieranie danych giełdowych
import matplotlib.pyplot as plt         # wykresy
import numpy as np                      # matematyka / wektory
from scipy import optimize              # optymalizacja

# ===== PARAMETRY =====
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']  # akcje
start_date = '2010-01-01'
end_date = '2017-01-01'
trading_days = 252                      # dni giełdowe w roku
num_portfolios = 10000                 # liczba losowych portfeli
risk_free_rate = 0.02                  # stopa wolna od ryzyka (2%)

# ===== POBIERANIE DANYCH =====
data = yf.download(stocks, start=start_date, end=end_date)['Close']

# usuwamy brakujące dane (ważne!)
data = data.dropna()

# ===== FUNKCJA: LICZENIE ZWROTÓW =====
def calculate_returns(data):
    # logarytmiczne zwroty (standard w finansach)
    return np.log(data / data.shift(1)).dropna()

# ===== FUNKCJA: STATYSTYKI PORTFELA =====
def portfolio_statistics(weights, returns):

    # oczekiwany roczny zwrot
    portfolio_returns = np.sum(returns.mean() * weights) * trading_days

    # zmienność (ryzyko)
    portfolio_volatility = np.sqrt(
        np.dot(weights.T, np.dot(returns.cov() * trading_days, weights))
    )

    # Sharpe ratio
    sharpe = (portfolio_returns - risk_free_rate) / portfolio_volatility

    return portfolio_returns, portfolio_volatility, sharpe

# ===== FUNKCJA: LOSOWE PORTFELE =====
def generate_random_portfolios(returns, num_portfolios):

    all_weights = []   # zapis wag
    ret_arr = []       # zwroty
    vol_arr = []       # zmienność

    for _ in range(num_portfolios):

        # losowe wagi
        w = np.random.random(len(stocks))

        # normalizacja (suma = 1)
        w /= np.sum(w)

        # statystyki
        ret, vol, _ = portfolio_statistics(w, returns)

        all_weights.append(w)
        ret_arr.append(ret)
        vol_arr.append(vol)

    return np.array(all_weights), np.array(ret_arr), np.array(vol_arr)

# ===== OBLICZENIA =====
returns = calculate_returns(data)

# generujemy portfele
weights, ret_arr, vol_arr = generate_random_portfolios(returns, num_portfolios)

# Sharpe ratio dla każdego portfela
sharpe_arr = (ret_arr - risk_free_rate) / vol_arr

# ===== NAJLEPSZY LOSOWY PORTFEL =====
max_sharpe_idx = sharpe_arr.argmax()

rand_best_return = ret_arr[max_sharpe_idx]
rand_best_vol = vol_arr[max_sharpe_idx]
rand_best_weights = weights[max_sharpe_idx]

# ===== OPTYMALIZACJA (SCIPY) =====

# funkcja celu: minimalizujemy -Sharpe (czyli maksymalizujemy Sharpe)
def negative_sharpe(weights, returns):
    return -portfolio_statistics(weights, returns)[2]

# ograniczenie: suma wag = 1
constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

# ograniczenia wag: 0–1 (long only)
bounds = tuple((0, 1) for _ in range(len(stocks)))

# start: równy podział
init_guess = len(stocks) * [1. / len(stocks)]

# optymalizacja
opt_results = optimize.minimize(
    negative_sharpe,
    init_guess,
    args=(returns,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

# wynik
opt_weights = opt_results.x
opt_return, opt_vol, opt_sharpe = portfolio_statistics(opt_weights, returns)

# ===== WYNIKI =====
print("=== LOSOWY NAJLEPSZY PORTFEL ===")
print("Zwrot:", rand_best_return)
print("Zmienność:", rand_best_vol)
print("Wagi:", rand_best_weights)

print("\n=== OPTYMALNY PORTFEL (SCIPY) ===")
print("Zwrot:", opt_return)
print("Zmienność:", opt_vol)
print("Sharpe:", opt_sharpe)
print("Wagi:", opt_weights)

# ===== WYKRES =====
plt.figure(figsize=(10, 6))

# wszystkie portfele
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')

# najlepszy losowy
plt.scatter(rand_best_vol, rand_best_return, c='red', s=50, label='Random Max Sharpe')

# optymalny
plt.scatter(opt_vol, opt_return, c='black', s=80, label='Optimized (Scipy)')

plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Efficient Frontier')
plt.legend()
plt.show()