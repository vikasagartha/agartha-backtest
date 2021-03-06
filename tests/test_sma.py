import sys
import unittest
from math import isnan
from datetime import datetime, timedelta
from random import uniform

class TestSMA(unittest.TestCase):
    def test_sma_util(self):
        size = 100
        low = 1
        high = 10000
        # generate list of size random floats between low and high
        l = [uniform(low, high) for _ in range(0, size)]
        for w in range(1, size):
            sma_w = sma(w)(l)
            for i in range(0, len(sma_w)):
                # confirm sma_w starts with window nan's
                if i<w:
                    self.assertTrue(isnan(sma_w[i]))
                # confirm rest of items
                else:
                    self.assertEqual(sma_w[i], sum(l[i-w:i])/w)

    def test_sma5020(self):
        l = [1, 2, 3, 4, 3, 2, 1, 8, 6, 1, 3, 4, 1, 2, 4, 6, 4, 5,
                4, 3]

        historical_data = []
        date = datetime.today()
        for i in range(0, len(l)):
            date_str = date.strftime('%Y-%m-%d %H:%M:%S')
            historical_data.append({'date': date_str, 'close_price': float(l[i])})
            date = date-timedelta(days=i)

        closing_prices = [d['close_price'] for d in
                historical_data]

        sma2 = sma(2)(closing_prices)
        sma4 = sma(4)(closing_prices)

        # To confirm crossover points and buys
        '''
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot(list(range(0, len(sma2))), sma2)
        plt.plot(list(range(0, len(sma4))), sma4)
        for xy in zip(list(range(0, len(sma2))), sma2):                                       # <--
            ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--
        plt.show()
        '''

        initial_balance = 1000000

        portfolio = backtest(historical_data=historical_data,
                algo=sma_fast_slow(2, 4),
                initial_portfolio=[{'balance': initial_balance, 'n_shares': 0}])

        # confirm 2 buy and 2 sell points
        self.assertEqual(portfolio[9], {
            'balance': initial_balance-closing_prices[8],
            'n_shares': 1
            })

        self.assertEqual(portfolio[11], {
            'balance': initial_balance-closing_prices[8]+closing_prices[10]
            , 'n_shares': 0})

        self.assertEqual(portfolio[16], {
            'balance':
            initial_balance-closing_prices[8]+closing_prices[10]-closing_prices[15]
            , 'n_shares': 1})

        self.assertEqual(portfolio[19], {
            'balance':
            initial_balance-closing_prices[8]+closing_prices[10]-closing_prices[15]+closing_prices[18]
            , 'n_shares': 0})

if __name__ == '__main__':
    sys.path.append('..')
    from backtest import backtest
    from algorithms.sma import sma_fast_slow
    from utils import sma
    unittest.main()
