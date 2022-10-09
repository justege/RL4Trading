# Source https://www.youtube.com/watch?v=M64KcWgNfJg

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

from binance import Client
import pandas as pd
import numpy as np
from pypfopt import EfficientFrontier, risk_models, expected_returns, plotting
import matplotlib.pyplot as plt

preprocessed_path = "/Users/egemenokur/PycharmProjects/RL4Trading/DataSets/CSVs/Close_Of_Stocks.csv"
data = pd.read_csv(preprocessed_path, index_col=0)


import seaborn as sns

plt.title('Correlation of Price')

sns.heatmap(data.corr(),
        xticklabels=data.columns,
        yticklabels=data.columns)

plt.show()

