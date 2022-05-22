**# RL4Trading
Implementing RL for Trading**

Step by step doing my own algotrading bot in python programming lanugage. 

**Start with BasicProcessing.py** which is a recap of preprocessing techniques for algotrading. It includes functions to 
- find moving average, 
- sample and resample the data,
- calculate cumulative return, 
- plot charts on top of each other. 
This introduction has been practiced from the well-written guide you should definetly check out. 
https://algo-trading.readthedocs.io/en/latest/data-science-basics.html#exploratory-data-analysis

**Continue with LocarithmicScale.py**

#Semi-logarithmic scaling
A semi-log plot is a graph where the data in one axis is on logarithmic scale (either x axis or y axis), and data in the other axis is on normal scale (i.e. linear scale).
**Key points**
-On a logarithmic scale, as the distance in the axis increases the corresponding value increases exponentially.
-With logarithmic scale, both smaller valued data and bigger valued data can be captured in the plot more accurately to provide a holistic view.
Therefore, semi-logarithmic charts can be of immense help especially when plotting long-term charts, or when the price points show significant volatility even in short-term charts. 
The underlying chart patterns will be revealed more clearly in semi-logarithmic scale charts.


#MovingAverage
**Continue with MovingAverage.py**
Exponential Moving Average (EMA) (a.k.a. exponentially weighted moving average) is a type of moving average (MA) that places a greater weight and significance on the most recent data points.

**Moving Average Convergence Divergence (MACD)**
The Moving Average Convergence Divergence (MACD) indicator is used to reveal changes in strength, direction, momentum and duration of a trend in a stock’s price.
**MACD=12-Period EMA−26-Period EMA**
One of the simplest strategy established with MACD, is to identify MACD crossovers. The rules are as follows.
Buy signal: MACD rises above the signal line
Sell signal: MACD falls below the signal line

**It also includes backtesting, model evaluation and sharpe ratio**


Portfolio_optimization.py calculates the Markowitz’ Efficient Frontier and shows the most risky symbols to be traded about. 
"This approach proposes a framework to evaluate the risk and returns of a portfolio.
Return of a portfolio is the mean returns per time step we can expect from that portfolio.
Risk is the standard deviation of the daily return. This gives a measure of volatility of the stock.
By plotting each portfolio in terms of its risk and return, asset managers can make informed decisions on the investment.
The line of efficient frontier shows the portfolios with highest returns for a given risk profile."
Source: https://medium.com/analytics-vidhya/portfolio-optimization-using-reinforcement-learning-1b5eba5db072


**Basic_Rule_based_Alpaca.py** 
This code come from the following source and is an introduction to paper trading.
https://www.qmr.ai/cryptocurrency-trading-bot-with-alpaca-in-python/