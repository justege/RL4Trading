import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
### Create the Stacked LSTM model

key=""

df = pdr.DataReader("AAPL",
                       start='2010-12-1',
                       end='2022-05-14',
                       data_source='yahoo')

# generate descriptive statistics, e.g. central tendency and dispersion of the dataset
# (excl. NaN values)
print("Describe")
print(df.describe())


# prints a summary of the dataframe e.g. dtype, non-null values
print("Info")
print(df.info())

# print rows between two specific dates
print("print rows between two specific dates")
print(df.loc[pd.Timestamp('2020-07-01'):pd.Timestamp('2020-07-17')])

# Take 10 rows from the dataframe randomly
sample = df.sample(10)
print("Take 10 rows from the dataframe randomly")
print(sample)


"""
Pass the ‘Rule’ argument to the function, which determines by what interval the data will be resampled by. In the example above, ‘M’ means by month end frequency.
Decide how to reduce the old datapoints or fill in the new ones, by calling groupby aggregate functions including mean(), min(), max(), sum().
In the above example, as we are resampling that data to a wider time frame (from days to months), we are actually “downsampling” the data.

"""
monthly_aapl = df.resample('M').mean()
print("df.resample('M').mean()")
print(monthly_aapl)


"""
On the other hand, if we resample the data to a shorter time frame (from days to minutes), it will be called “upsampling”
ffill() ‘Forward filling’ or pad()‘padding’ — Use the last known value.
bfill() or backfill() ‘Backfilling’ — Use the next known value.
"""
# Resample to minutely level
print("Downsampling")
minutely_aapl = df.resample('T').ffill()
print(minutely_aapl)


daily_close = df[['Close']]
# Calculate daily returns
daily_pct_change = daily_close.pct_change()
# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)
# Inspect daily returns
print("Inspect")
print(daily_pct_change.head())


# Resample to business months, take last observation as value
monthly = df.resample('BM').apply(lambda x: x[-1])

# Calculate monthly percentage change
print("Calculate monthly percentage change")
print(monthly)
print(monthly.pct_change().tail())


# Resample to quarters, take the mean as value per quarter
quarter = df.resample("4M").mean()

# Calculate quarterly percentage change
print(quarter.pct_change().tail())

# Daily returns hardcoded
daily_pct_change = daily_close / daily_close.shift(1) - 1

# Print `daily_pct_change`
print(daily_pct_change.tail())

# Plot the closing prices for `aapl`
df['Close'].plot(grid=True)

# Show the line plot
plt.show()


# Plot the distribution of `daily_pct_c`
daily_pct_change.hist(bins=50)

# Show the plot
plt.show()

# Pull up summary statistics
print(daily_pct_change.describe())

# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_change).cumprod()

# Plot the cumulative daily returns
cum_daily_return.plot(figsize=(12,8))

# Show the plot
plt.show()

# Isolate the closing prices
close_px = df['Close']

# Calculate the moving average
moving_avg = close_px.rolling(window=40).mean()

# Inspect the result
print("Calculate the moving average")
print(moving_avg)
plt.plot(close_px)
plt.plot(moving_avg)
plt.show()

# Short moving window rolling mean
df['42'] = close_px.rolling(window=40).mean()

# Long moving window rolling mean
df['252'] = close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
df[['Close', '42', '252']].plot()

# Show plot
plt.show()