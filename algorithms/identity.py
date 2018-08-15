from . import Choice

def identity(**kwargs):
    return Choice.BUY if kwargs['has_shares'] else Choice.SELL
