from numpy.random import rand, random_sample
from utils import destructure

def coin_toss(**kwargs):

    defaults = {
        'portfolio_state': {'balance': 0, 'n_shares': 0},
        'historical_data': [],
        'index': 0
    }

    defaults.update(kwargs)

    portfolio_state, historical_data, index = destructure(defaults, ('portfolio_state',
        'historical_data', 'index'))

    print(portfolio_state)

    x = random_sample()

    balance = portfolio_state['balance']
    n_shares = portfolio_state['n_shares']
    close_price = historical_data[index]['close_price']
    sufficient_funds = balance > close_price

    buy = x > 0.5

    if buy and sufficient_funds:
        portfolio_state = {'balance': balance - close_price, 'n_shares': n_shares+1}
    elif buy and not sufficient_funds:
        pass
    elif not buy and n_shares > 0:
        portfolio_state = {'balance': balance + close_price, 'n_shares': n_shares-1}
    elif not buy and n_shares <= 0:
        pass

    return portfolio_state
