import numpy as np
from backtest import backtest
from algorithms.sma import sma5020
from algorithms.coinToss import coinToss
from csv_writer import write_results

data = np.random.rand(100)
portfolio = backtest(historical_price=data, algo=coinToss)
write_results(portfolio, data, 'results')

