import numpy as np
from utils import destructure
from coinToss import coinToss

def backtest(**kwargs):

    defaults = {
        'initial_portfolio': [False],
        'algo': coinToss,
        'historical_price': [],
    }

    defaults.update(kwargs)

    historical_price, algo, portfolio = destructure(defaults, ['historical_price', 'algo', 'initial_portfolio'])

    for i, x in np.ndenumerate(historical_price):
        new_portfolio = algo(historical_price=historical_price, index=i[0], has_shares=portfolio[:-1])
        portfolio.append(new_portfolio)

    print('Final portfolio:\n',portfolio, '\nHistorical data:\n', historical_price)

backtest(historical_price=np.random.rand(100))
