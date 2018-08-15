import numpy as np
from utils import destructure
from identity import identity 

def backtest(**kwargs):

    defaults = {
        'initial_portfolio': [False],
        'algo': identity,
        'historical_price': [],
    }

    defaults.update(kwargs)

    historical_price, algo, portfolio = destructure(defaults, ['historical_price', 'algo', 'initial_portfolio'])

    for i, x in np.ndenumerate(historical_price):
        new_portfolio = algo(historical_price=historical_price, index=i[0], has_shares=portfolio[-1])
        portfolio.append(new_portfolio)

    return portfolio
