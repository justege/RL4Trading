import backtrader as bt
import datetime
import matplotlib
import yfinance as yf
#%matplotlib inline

cerebro = bt.Cerebro()

df = yf.download('AAPL', start = '2010-01-01')
print(df)



class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,  # period for the fast moving average
        pslow=30   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position



cerebro.addstrategy(SmaCross)

cerebro.addsizer(bt.sizers.PercentSizer, percents=50)


feed = bt.feeds.PandasData(dataname=df)
cerebro.adddata(feed)
cerebro.run()
cerebro.plot(iplot=False)


