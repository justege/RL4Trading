import pandas_datareader as pdr
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


key=""

df = pdr.DataReader("AAPL",
                       start='2010-12-1',
                       end='2022-05-14',
                       data_source='yahoo')

#df.index = mdates.date2num(df.index)
#data = df.reset_index().values # Convert dataframe into 2-D list

# Get adjusted close column
# Initialize the short and long windows
short_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)


signals['signal'].to_csv("PreDiff.csv")
# Generate trading orders
signals['positions'] = signals['signal'].diff()

signals['positions'].to_csv("PostDiff.csv")

# Print `signals`
print(signals.tail())

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')

# Plot the closing price
df['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

positions = (signals.positions).to_numpy()
short_mavg = (signals.short_mavg).to_numpy()
long_mavg = (signals.long_mavg).to_numpy()



# Plot the buy signals
ax1.plot(signals.loc[positions == 1.0].index,
         short_mavg[positions == 1.0],
         '^', markersize=10, color='m')

# Plot the sell signals
ax1.plot(signals.loc[positions == -1.0].index,
         long_mavg[positions == -1.0],
         'v', markersize=10, color='k')

# Show the plot
plt.show()

# Set the initial capital
initial_capital = float(100000.0)

# Create a DataFrame `positions`
positions = pd.DataFrame(index=signals.index).fillna(0.0)

# Buy a 100 shares
positions['AAPL'] = 100 * signals['signal']

# Initialize the portfolio with value owned
portfolio = positions.multiply(df['Close'], axis=0)

# Store the difference in shares owned
pos_diff = positions.diff()

pos_diff.to_csv('pos_diff.csv')

# Add `holdings` to portfolio
portfolio['holdings'] = (positions.multiply(df['Close'], axis=0)).sum(axis=1)

# Add `cash` to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(df['Close'], axis=0)).sum(axis=1).cumsum()

# Add `total` to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']

# Add `returns` to portfolio
portfolio['returns'] = portfolio['total'].pct_change()

# Print the last lines of `portfolio`
portfolio.to_csv('portfolio.csv')

# Create a figure
fig = plt.figure()

ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')

# Plot the equity curve in dollars
portfolio['total'].plot(ax=ax1, lw=2.)

positions = signals.positions.to_numpy()

ax1.plot(portfolio.loc[positions == 1.0].index,
         portfolio.total[positions == 1.0],
         '^', markersize=10, color='m')
ax1.plot(portfolio.loc[positions == -1.0].index,
         portfolio.total[positions == -1.0],
         'v', markersize=10, color='k')

# Show the plot
plt.show()

# Isolate the returns of your strategy
returns = portfolio['returns']

# annualized Sharpe ratio
sharpe_ratio = np.sqrt(252) * (returns.mean() / returns.std())

# Print the Sharpe ratio
print(sharpe_ratio)

# Define a trailing 252 trading day window
window = 252

# Calculate the max drawdown in the past window days for each day
rolling_max = df['Close'].rolling(window, min_periods=1).max()
daily_drawdown = df['Close']/rolling_max - 1.0

# Calculate the minimum (negative) daily drawdown
max_daily_drawdown = daily_drawdown.rolling(window, min_periods=1).min()

# Plot the results
daily_drawdown.plot()
max_daily_drawdown.plot()

# Show the plot
plt.show()