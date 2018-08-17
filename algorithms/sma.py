from utils import destructure, sma

_sma20 = sma(20)
_sma50 = sma(50)
delta = 10.0

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

    try:
        # check if there is a crossover
        if abs(sma20[index]-sma50[index]) < delta:
            if sma20[index+1] > sma50[index+1]:
                return n_shares+1
            elif n_shares>0:
                return n_shares-1
    except:
        pass
    return n_shares
