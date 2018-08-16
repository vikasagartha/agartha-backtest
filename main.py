import numpy as np
from backtest import backtest
from algorithms.sma import sma5020
from algorithms.coinToss import coinToss
from csv_writer import write_results
from fetch_data import Data

data = Data('AAPL')
quote_data = data.get_quote_historicals()
close_prices = list(map(lambda entry: float(entry['close_price']), quote_data))
portfolio = backtest(historical_price=close_prices, algo=coinToss)
write_results(portfolio, close_prices, 'results')
