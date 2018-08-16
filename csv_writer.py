import csv

def write_results(portfolio, data, times, filename):
    with open(f'charts/{filename}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Time', 'Transaction', 'Data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(times)):
            time = str(times[i])
            transaction = str(portfolio[i])
            d = data[i]
            writer.writerow({'Time': time, 'Transaction': transaction, 'Data': d})
