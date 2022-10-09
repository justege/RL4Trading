
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

for Stock_Number in ['AAPL','MSFT','TSLA','CL=F','GC=F']:
    #train[train.index % 3 == 0]  # Ex
    Stock_Close = train[train.tic  == Stock_Number]['close']
    Stock_Volume = train[train.tic == Stock_Number]['volume']
    Stock_MACD = train[train.tic == Stock_Number]['macd']
    Stock_rsi = train[train.tic== Stock_Number]['rsi']
    Stock_cci = train[train.tic == Stock_Number]['cci']
    Stock_adx = train[train.tic == Stock_Number]['adx']
    timeframe = pd.to_datetime(train[train.tic == Stock_Number]['datadate'], format='%Y%m%d', errors='ignore')

    fig = plt.figure(figsize=(10, 7))
    # Define position of 1st subplot
    ax = fig.add_subplot(4, 1, 1)


    # Set the title and axis labels
    plt.title(Stock_Number+' Charts')
    plt.xlabel('Date')
    plt.ylabel('Close Price')


    plt.plot(timeframe,Stock_Close, label='Close price')
    plt.grid()
    plt.legend()
    # Add a legend to the axis
    # Define position of 2nd subplot
    bx = fig.add_subplot(4, 1, 2)

    # Set the title and axis labels
    plt.xlabel('Date')

    plt.plot(timeframe,Stock_rsi, label='rsi')
    plt.plot(timeframe,Stock_adx,  label='adx')
    plt.grid()
    plt.legend()
    #plt.plot(AAPL_DF['turbulence'], label='turbulence')

    bx = fig.add_subplot(4, 1, 3)
    plt.xlabel('Date')

    plt.plot(timeframe,Stock_MACD, label='macd')
    plt.grid()
    plt.legend()


    bx = fig.add_subplot(4, 1, 4)
    plt.plot(timeframe,Stock_cci,  label='cci')
    plt.xlabel('Date')


    #AAPL_DF['rsi'].plot(grid=True, label='rsi')
    #AAPL_DF['adx'].plot(grid=True, label='adx')
    #AAPL_DF['cci'].plot(grid=True, label='cci')
    #AAPL_DF['turbulence'].plot(grid=True, label='turbulence')
    plt.grid()
    plt.legend()
    plt.show()
