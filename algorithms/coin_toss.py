from numpy.random import rand, random_sample
from utils import destructure

def coin_toss(**kwargs):

    defaults = {
        'n_shares': 0,
        'historical_data': [],
        'index': 0
    }

    defaults.update(kwargs)

    n_shares, historical_data, index = destructure(defaults, ('n_shares',
        'historical_data', 'index'))

    x = random_sample()

    if x > 0.5: return n_shares+1
    elif n_shares>0: return n_shares-1 
    else: return n_shares
