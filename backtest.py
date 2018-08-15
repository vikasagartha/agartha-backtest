import numpy as np
from utils import destructure
from algorithms.identity import identity 
from algorithms import Choice

def backtest(**kwargs):

    defaults = {
        'initial_portfolio': [Choice.STAY],
        'algo': identity,
        'historical_price': [],
    }

    defaults.update(kwargs)

    historical_price, algo, portfolio = destructure(defaults, ['historical_price', 'algo', 'initial_portfolio'])

    for i, x in np.ndenumerate(historical_price):
        new_portfolio = algo(historical_price=historical_price, index=i[0], has_shares=portfolio[-1])
        portfolio.append(new_portfolio)

    return portfolio
