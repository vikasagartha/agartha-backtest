import numpy as np
from backtest import backtest
from algorithms.sma import sma5020
from algorithms.coinToss import coinToss
from csv_writer import write_results
from fetch_data import Data

data = Data('TSLA')
quote_data = data.get_quote_historicals(interval='day', span='5year', bounds='extended')
times = list(map(lambda entry: entry['begins_at'], quote_data))
close_prices = list(map(lambda entry: float(entry['close_price']), quote_data))
portfolio = backtest(historical_price=close_prices, algo=sma5020)
write_results(portfolio, close_prices, times, 'results')
