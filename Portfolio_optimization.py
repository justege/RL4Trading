from binance import Client
import pandas as pd
import numpy as np
from pypfopt import EfficientFrontier, risk_models, expected_returns, plotting
import matplotlib.pyplot as plt

client = Client()

# get data
def getdailydata(symbol):
    frame = pd.DataFrame(client.get_historical_klines(symbol,
                                                      '1d',
                                                      '3 years ago UTC'
                                                      ))
    frame = frame[[0,4]]
    frame.columns = ['Timestamp', symbol]
    frame = frame.set_index('Timestamp')
    frame = frame.astype(float)

    return frame


# Define Symbols
symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT']

prices = []

# Get all Symbol data
for symbol in symbols:
    prices.append(getdailydata(symbol))


# Concatenate into one dataframe
df = pd.concat(prices, axis=1)
print(df)


mu = expected_returns.mean_historical_return(df, frequency=365)
print(mu)


S = risk_models.sample_cov(df, frequency=365)
print(S)


ef = EfficientFrontier(mu,S)

# Y axis = Containing returns, X Axis = volatility


# Get ticker names  ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT']

fix, ax = plt.subplots()

plotting.plot_efficient_frontier(ef, ax=ax, show_assets=True)

for i, txt in enumerate(ef.tickers):
    ax.annotate(txt, ((np.diag(ef.cov_matrix)**(1/2))[i], ef.expected_returns[i]))



ef = EfficientFrontier(mu,S)

# Do the portfolio optimization according to maximum sharpe ratio
weights = ef.max_sharpe()
print(weights)