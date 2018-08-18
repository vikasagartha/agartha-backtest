import numpy as np
from utils import destructure
from algorithms.identity import identity 

def backtest(**kwargs):

    defaults = {
        'initial_portfolio': [{'balance': 0, 'n_shares': 0}],
        'algo': identity,
        'historical_data': [],
    }

    defaults.update(kwargs)

    historical_data, algo, portfolio = destructure(defaults, ['historical_data', 'algo', 'initial_portfolio'])

    for i, x in np.ndenumerate(historical_data):
        new_portfolio = algo(historical_data=historical_data, index=i[0],
                portfolio_state=portfolio[-1])
        portfolio.append(new_portfolio)

    return portfolio
