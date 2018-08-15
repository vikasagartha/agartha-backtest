import numpy as np
from backtest import backtest
from coinToss import coinToss

data = np.random.rand(100)
portfolio = backtest(historical_price=data, algo=coinToss)
#portfolio = backtest(historical_price=data)
print('Final portfolio:\n',portfolio, '\nHistorical data:\n', data)
