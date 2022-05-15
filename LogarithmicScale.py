import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
### Create the Stacked LSTM model
import mpl_finance
import matplotlib.dates as mdates
from mpl_finance import candlestick_ochl as candlestick
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU # for locator


key=""

df = pdr.DataReader("AAPL",
                       start='2010-12-1',
                       end='2022-05-14',
                       data_source='yahoo')

df.index = mdates.date2num(df.index)
data = df.reset_index().values # Convert dataframe into 2-D list

plt.style.use('ggplot')

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_size_inches(18.5, 7.0)

### Subplot 1 - Semi-logarithmic ###
plt.subplot(121)
plt.grid(True, which="both")

# Linear X axis, Logarithmic Y axis
plt.semilogy(df.index, df['Close'], 'r')
plt.ylim([10,500])

plt.xlabel("Date")
plt.title('Semi-logarithmic scale')
fig.autofmt_xdate()

### Subplot 2 - Arithmetic ###
plt.subplot(122)

plt.plot(df.index, df['Close'], 'b')

plt.xlabel("Date")
plt.title('Arithmetic scale')
fig.autofmt_xdate()

# show plot
plt.show()