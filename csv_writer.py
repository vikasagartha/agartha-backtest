import csv

def write_results(portfolio, data, filename):
    with open(f'{filename}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Transaction', 'Data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, max(len(portfolio), len(data))):
            try:
                transaction = portfolio[i]
            except:
                transaction = 'No transaction'
            try:
                _data = data[i]
            except:
                _data = 'No data' 
            writer.writerow({'Transaction': transaction, 'Data': _data})
