import csv

def write_results(portfolio, prices, times, filename):
    with open(f'charts/{filename}.csv', 'w', newline='') as csvfile:
        fieldnames = ['time', 'n_shares', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(times)):
            time = str(times[i])
            n_shares = str(portfolio[i])
            d = prices[i]
            writer.writerow({'time': time, 'n_shares': n_shares, 'price': d})
