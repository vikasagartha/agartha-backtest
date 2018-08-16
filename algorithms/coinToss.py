from numpy.random import rand, random_sample
from utils import destructure

def coinToss(**kwargs):

    defaults = {
        'n_shares': 0,
        'historical_price': [],
        'index': 0
    }

    defaults.update(kwargs)

    n_shares, historical_price, index = destructure(defaults, ('n_shares', 'historical_price', 'index'))

    x = random_sample()

    if x > 0.5: return n_shares+1
    elif n_shares>0: return n_shares-1 
    else: return n_shares
