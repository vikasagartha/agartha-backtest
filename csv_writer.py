import csv
import json
from datetime import datetime

def write_results(portfolio, prices, times, filename):
    with open(f'charts/{filename}.csv', 'w', newline='') as csvfile:
        fieldnames = ['time', 'balance', 'n_shares', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(times)):
            time = str(times[i])
            balance = str(portfolio[i]['balance'])
            n_shares = str(portfolio[i]['n_shares'])
            d = prices[i]
            writer.writerow({'time': time, 'balance': balance, 'n_shares': n_shares, 'price': d})
    with open(f'charts/{filename}.meta', 'w', newline='') as metafile:
        meta = {
                'name': 'Unknown',
                'creation_time': datetime.now().strftime('%s')
        }
        json.dump(meta, metafile)
