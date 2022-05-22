# Source https://www.youtube.com/watch?v=M64KcWgNfJg

from binance import Client
import pandas as pd
import numpy as np
from pypfopt import EfficientFrontier, risk_models, expected_returns, plotting
import matplotlib.pyplot as plt

client = Client()

info = client.get_exchange_info()

symbols = [x['symbol'] for x in info['symbols']]

relevant = [symbol for symbol in symbols if symbol.endswith('USDT')]

def getdailydata(symbol):
    frame = pd.DataFrame(client.get_historical_klines(symbol,
                                                      '1d',
                                                      '3 years ago UTC'))

    if len(frame)>0:
        frame = frame.iloc[:,:5]
        frame.columns = ['Time','Open','High','Low','Close']
        frame = frame.set_index('Time')
        frame.index = pd.to_datetime(frame.index, unit='ms')
        frame = frame.astype(float)
        return frame


dfs = []
for coin in relevant:
    dfs.append(getdailydata(coin))


# Concatenates symbol names with the getdailydata matrixß
mergedf = pd.concat(dict(zip(relevant,dfs)),axis=1)


# Brings only matrix with close prices.
closesdf = mergedf.loc[:, mergedf.columns.get_level_values(1).isin(['Close'])]

logret = np.log(closesdf.pct_change + 1)

correlation_matrix = logret.corr()

import seaborn as sns

sns.set(rc = {'figure.figsize':(50,30)})
sns.heatmap(logret.corr())

smaller_corr_matrix = logret[['BTCUSDT','ETHUSDT','ADAUSDT']].corr()

smaller_corr_matrix.nsmallest(30)

exclude = ['UP','DOWN']

non_level = [symbol for symbol in symbols if all(excludes not in symbol for excludes in exclude)]

stacked = filtered_correlation_data = correlation_matrix.filter(non_level, axis=1).filter(non_level, axis=0)

unstacked = stacked.unstack()





