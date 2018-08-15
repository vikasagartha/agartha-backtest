from numpy.random import rand, random_sample
from utils import destructure

def coinToss(**kwargs):

    defaults = {
        'has_shares': False,
        'historical_price': [],
        'index': 0
    }

    defaults.update(kwargs)

    has_shares, historical_price, index = destructure(defaults, ('has_shares', 'historical_price', 'index'))

    return random_sample() > 0.5 
