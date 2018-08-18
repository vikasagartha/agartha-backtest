import numpy as np
from backtest import backtest
from algorithms.sma import sma5020
from algorithms.coin_toss import coin_toss
from csv_writer import write_results
from fetch_data import Data

data = Data('TSLA')
quote_data = data.get_quote_historicals(interval='day', span='5year', bounds='extended')
historical_data = list(map(lambda entry: {'date': entry['begins_at'], 'close_price': float(entry['close_price'])}, quote_data))
portfolio = backtest(historical_data=historical_data, algo=sma5020)

close_prices = [d['close_price'] for d in historical_data]
times = [d['date'] for d in historical_data]
write_results(portfolio, close_prices, times, 'results')
