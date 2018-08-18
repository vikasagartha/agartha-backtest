from utils import destructure, sma
from math import floor

fastDays = 20
slowDays = 50
_fast = sma(fastDays)
_slow = sma(slowDays)
delta = 0.1

def sma5020(**kwargs):

    defaults = {
        'n_shares': 0,
        'historical_data': [],
        'index': 0
    }

    defaults.update(kwargs)

    n_shares, historical_data, index = destructure(defaults, ('n_shares', 'historical_data', 'index'))

    closing_prices = [d['close_price'] for d in
            historical_data]
    fast = _fast(closing_prices)
    slow = _slow(closing_prices)

    fastindex = floor(index/fastDays)
    #TODO double check the max logic
    prevfastindex = max(0, floor((index-1)/fastDays))
    slowindex = floor(index/slowDays)

    if abs(fast[fastindex]-slow[slowindex]) < delta:
        if fast[prevfastindex] > fast[fastindex]:
            return 0
        else:
            return 1

    return n_shares
