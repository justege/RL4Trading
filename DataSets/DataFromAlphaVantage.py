import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# replace with your own API key
key = "open('../1-alphavantage.txt').read()"
key = "SIBWEH64IZ824T8X"

ts = TimeSeries(key, output_format='pandas')
data, meta = ts.get_intraday('TSLA', interval='1min', outputsize='full')

columns = ['open', 'high', 'low', 'close', 'volume']
data.columns = columns

data['TradeDate'] = data.index.date
data['time'] = data.index.time

market = data.between_time('09:30:00', '16:00:00').copy()
market.sort_index(inplace=True)
market.info()


market.groupby('TradeDate').agg({'low':min, 'high':max})


market.loc[market.groupby('TradeDate')['low'].idxmin()]

print(market)

market.loc[market.groupby('TradeDate')['high'].idxmax()]