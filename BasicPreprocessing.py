import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
### Create the Stacked LSTM model

key=""

df = pdr.DataReader("AAPL",
                       start='2010-12-1',
                       end='2022-01-10',
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