from numpy.random import rand, random_sample
from utils import destructure
from . import Choice

def coinToss(**kwargs):

    defaults = {
        'has_shares': False,
        'historical_price': [],
        'index': 0
    }

    defaults.update(kwargs)

    has_shares, historical_price, index = destructure(defaults, ('has_shares', 'historical_price', 'index'))

    x = random_sample()

    if x == 0.5: return Choice.STAY
    elif x > 0.5: return Choice.BUY
    else: return Choice.SELL
