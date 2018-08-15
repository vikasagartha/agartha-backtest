from utils import destructure, sma
from . import Choice

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

    if len(sma20)>index and len(sma50)>index:
        # If there is a crossover, we want to buy
        if sma20[index] == sma50[index]: return Choice.BUY
        # If short sma is greater than long sma, we want to stay
        elif sma20[index] > sma50[index]: return Choice.STAY
        # If long sma is greater than short sma, we want to sell
        else: return Choice.SELL
    return Choice.STAY
