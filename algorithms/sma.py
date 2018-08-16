from utils import destructure, sma

_sma20 = sma(20)
_sma50 = sma(50)

def sma5020(**kwargs):

    defaults = {
        'n_shares': 0,
        'historical_price': [],
        'index': 0
    }
    
    defaults.update(kwargs)

    n_shares, historical_price, index = destructure(defaults, ('n_shares', 'historical_price', 'index'))

    sma20 = _sma20(historical_price)
    sma50 = _sma50(historical_price)

    if len(sma20)>index and len(sma50)>index:
        # If there is a crossover, we want to buy
        if sma20[index] == sma50[index]: return n_shares+1
        # If short sma is greater than long sma, we want to stay
        elif sma20[index] > sma50[index]: return n_shares
        # If long sma is greater than short sma, we want to sell
        elif n_shares>0: return n_shares-1

    return n_shares
