
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
Stock_Close1 = train[train.tic == 'AAPL']['close']
Stock_Close2 = train[train.tic == 'GC=F']['close']
Stock_Close3 = train[train.tic == 'CL=F']['close']
Stock_Close4 = train[train.tic == 'MSFT']['close']
Stock_Close5 = train[train.tic == 'TSLA']['close']

timeframe = pd.to_datetime(train[train.index % 5 == 0]['datadate'], format='%Y%m%d', errors='ignore')


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
# Define position of 1st subplot

# Set the title and axis labels
plt.title('Price Chart')
plt.xlabel('Date')
plt.ylabel('GC=F', color = 'y')


lns1 = ax1.plot(timeframe,Stock_Close1,label='AAPL',color='r')


lns2 = ax1.plot(timeframe,Stock_Close3, label='CL=F', color='b')
lns3 = ax1.plot(timeframe,Stock_Close4, label='MSFT',color='g')
lns4 = ax1.plot(timeframe,Stock_Close5, label='TSLA',color='m')




lns5 = ax2.plot(timeframe,Stock_Close2, label='GC=F',color='y')
plt.grid()

lns = lns1+lns2+lns3+lns4 + lns5
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)
ax1.spines['right'].set_color('yellow')
plt.show()
