
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

preprocessed_path = "0000_test.csv"

data = pd.read_csv(preprocessed_path, index_col=0)

unique_trade_date = data[(data.datadate > 20171001)].datadate.unique()
# print(unique_trade_date)


def data_split(df, start, end):
    """
    split the dataset into training or testing using date
    :param data: (df) pandas dataframe, start, end
    :return: (df) pandas dataframe
    """
    data = df[(df.datadate >= start) & (df.datadate < end)]
    data = data.sort_values(['datadate','tic'], ignore_index=True)


    # data  = data[final_columns]
    #data.index = data.datadate.factorize()[0]


    return data

train = data_split(data, start=20170101, end=20221009)


#train[train.index % 3 == 0]  # Ex
Stock_Close1 = train[train.index % 3 == 0]['close']
Stock_Close2 = train[train.index % 3 == 1]['close']
Stock_Close3 = train[train.index % 3 == 2]['close']

timeframe = pd.to_datetime(train[train.index % 3 == 0]['datadate'], format='%Y%m%d', errors='ignore')

fig = plt.figure(figsize=(5, 2))
# Define position of 1st subplot

# Set the title and axis labels
plt.title('Price Chart')
plt.xlabel('Date')
plt.ylabel('Close Price')


plt.plot(timeframe,Stock_Close1,label='AAPL')
plt.plot(timeframe,Stock_Close2, label='SONY')
plt.plot(timeframe,Stock_Close3, label='TSLA')
plt.grid()
plt.legend()
plt.show()
