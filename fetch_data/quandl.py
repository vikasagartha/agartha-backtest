import subprocess, json

class QuandlData():  
    def __init__(self, stock):  
        self.stock = stock
        with open('config.json') as f:
            config = json.load(f)
            self.api_key = config['QUANDL_API_KEY']
    '''
    get_time_series - get time series data for a particular security
    Params:
    Returns:
        Dataset containing the following columns for all relevant dates:
        ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ex-Dividend', 'Split
        Ratio', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj.
        Volume']
    '''
    def get_time_series(self):
        time_series_command = f'curl "https://www.quandl.com/api/v3/datasets/WIKI/{self.stock}/data.json?api_key={self.api_key}"'
        p = subprocess.Popen(time_series_command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
        out, err = p.communicate()
        parsed = json.loads(out)
        return parsed
