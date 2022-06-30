# Load the necessary packages and modules
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Returns ATR values
def atr(high, low, close, n=14):
    tr = np.amax(np.vstack(((high - low).to_numpy(), (abs(high - close)).to_numpy(), (abs(low - close)).to_numpy())).T, axis=1)
    return pd.Series(tr).rolling(n).mean().to_numpy()

# Retrieve the Apple Inc. data from Yahoo finance
data = yf.download("AAPL", start="2010-01-01", end="2022-06-30")

data['ATR'] = atr(data['High'], data['Low'], data['Close'], 14)

# Plotting the Price Series chart and the ATR below
fig = plt.figure(figsize=(10, 7))

# Define position of 1st subplot
ax = fig.add_subplot(2, 1, 1)

# Set the title and axis labels
plt.title('Apple Price Chart')
plt.xlabel('Date')
plt.ylabel('Close Price')

plt.plot(data['Close'], label='Close price')

# Add a legend to the axis
plt.legend()

# Define position of 2nd subplot
bx = fig.add_subplot(2, 1, 2)

# Set the title and axis labels
plt.title('Average True Range')
plt.xlabel('Date')
plt.ylabel('ATR values')

plt.plot(data['ATR'] , 'm', label='ATR')

# Add a legend to the axis
plt.legend()

plt.tight_layout()
plt.show()