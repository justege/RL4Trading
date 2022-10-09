from pandas_datareader import data as web
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# Commodity Channel Index 
def CCI(data, ndays): 
    TP = (data['High'] + data['Low'] + data['Close']) / 3
    CCI = pd.Series((TP - TP.rolling(ndays).mean()) / (0.015*TP.rolling(ndays).mean()),
    name = 'CCI')
    data = data.join(CCI)
    return data

# Retrieve the Nifty data from Yahoo finance:
data = yf.download("SONY", start="2020-01-01", end="2022-10-06")
data = pd.DataFrame(data)

# Compute the Commodity Channel Index(CCI) for NIFTY based on the 20-day Moving average
n = 20
NI = CCI(data, n)
CCI = NI['CCI']

# Plotting the Price Series chart and the Commodity Channel index below
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(2, 1, 1)
ax.set_xticklabels([])
plt.plot(data['Close'],lw=1)
plt.title('AAPL Price Chart')
plt.ylabel('Close Price')
plt.grid(True)
bx = fig.add_subplot(2, 1, 2)
plt.plot(CCI,'k',lw=0.75,linestyle='-',label='CCI')
plt.legend(loc=2,prop={'size':9.5})
plt.ylabel('CCI values')
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()