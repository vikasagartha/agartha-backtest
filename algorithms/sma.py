from utils import destructure, sma
from math import floor, isnan

fastDays = 20
slowDays = 50
_fast = sma(fastDays)
_slow = sma(slowDays)

def sma5020(**kwargs):

    defaults = {
        'portfolio_state': {'balance': 0, 'n_shares': 0},
        'historical_data': [],
        'index': 0
    }

    defaults.update(kwargs)

    portfolio_state, historical_data, index = destructure(defaults, ('portfolio_state',
        'historical_data', 'index'))

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
