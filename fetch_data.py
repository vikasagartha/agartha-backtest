import subprocess, json

class Data():  
    def __init__(self, stock):  
        self.stock = stock

    '''
    get_quote_historicals - get historical data for a particular security
    Params:
        - interval=week|day|10minute|5minute|null(all) 
        - span=day|week|year|5year|all
        - bounds=extended|regular|trading
    Returns:
        An array of dictionary entries containing relevant data:
        {
            "begins_at": <time in UTC>,
            "close_price": <Price in US Dollars>,
            "high_price": <Price in US Dollars>,
            "interpolated": <Boolean>,
            "low_price": <Price in US Dollars>,
            "open_price": <Price in US Dollars>,
            "session":
            "reg",
            "volume": <Volume traded>
        }
    '''
    def get_quote_historicals(self, interval='day', span='year', bounds='extended'):
        quote_command = f'curl -v https://api.robinhood.com/quotes/historicals/{self.stock}/?interval={interval}&span={span}&bounds={bounds}'
        p = subprocess.Popen(quote_command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
        out, err = p.communicate()
        parsed = json.loads(out)
        return parsed['historicals']
