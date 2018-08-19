from utils import destructure, sma
from math import floor, isnan

def sma_fast_slow(**kwargs):

    defaults = {
        'fast_rate': 20,
        'slow_rate': 50,
        'portfolio_state': {'balance': 0, 'n_shares': 0},
        'historical_data': [],
        'index': 0
    }

    defaults.update(kwargs)

    portfolio_state, historical_data, index, fast_rate, slow_rate = destructure(defaults, ('portfolio_state',
        'historical_data', 'index', 'fast_rate', 'slow_rate'))

    _fast = sma(fast_rate)
    _slow = sma(slow_rate)

    if index == 0: return portfolio_state 

    closing_prices = [d['close_price'] for d in
            historical_data]
    fast = _fast(closing_prices)
    slow = _slow(closing_prices)

    balance = portfolio_state['balance']
    n_shares = portfolio_state['n_shares']
    close_price = historical_data[index]['close_price']
    sufficient_funds = balance > close_price

    a = fast[index-1]
    b = fast[index]

    c = slow[index-1]
    d = slow[index]

    if isnan(c): return portfolio_state

    if a/c<1 and b/d>1 and sufficient_funds:
        portfolio_state = {'balance': balance - close_price, 'n_shares': 1}
    elif a/c>1 and b/d<1 and n_shares > 0:
        portfolio_state = {'balance': balance + close_price, 'n_shares': 0}
    else:
        pass

    return portfolio_state 
