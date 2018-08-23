from fetch_data import robinhood, quandl
from datetime import datetime

class DataAggregator():
    def __init__(self, stock):  
        self.stock = stock

    def get_data(self):
        r = robinhood.RobinhoodData(self.stock) 
        q = quandl.QuandlData(self.stock)

        data = []

        robinhood_data = r.get_quote_historicals()
        quandl_data = q.get_time_series()
        for d in quandl_data['dataset_data']['data']:
            date = datetime.strptime(d[0], '%Y-%m-%d')
            data.append({'date': date, 'open_price': float(d[1]),
                'close_price': float(d[4]), 'high_price': float(d[2]),
                'low_price': float(d[3]), 'volume':
                int(d[5])})

        for d in robinhood_data:
            date = datetime.strptime(d['begins_at'], '%Y-%m-%dT%H:%M:%SZ')
            aggregated = False
            for _d in data:
                if date==_d['date']:
                    aggregated = True
            if not aggregated:
                data.append({'date': date, 'open_price': float(d['open_price']),
                    'close_price': float(d['close_price']), 'high_price':
                    float(d['high_price']), 'low_price': float(d['low_price']), 'volume':
                    int(d['volume'])})
        return data

d = DataAggregator('AAPL')

data = d.get_data()

for d in data:
    print(d)
