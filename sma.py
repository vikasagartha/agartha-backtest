from utils import destructure, sma

_sma20 = sma(20)
_sma50 = sma(50)

def sma5020(**kwargs):

    defaults = {
        'has_shares': False,
        'historical_price': [],
        'index': 0
    }
    
    defaults.update(kwargs)

    has_shares, historical_price, index = destructure(defaults, ('has_shares', 'historical_price', 'index'))

    sma20 = _sma20(historical_price)
    sma50 = _sma50(historical_price)

    return sma20[index] == sma50[index]
