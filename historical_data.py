import subprocess, json

class data():  
    def __init__(self, stock):  
        self.stock = stock  
        parameter_list = ['open', 'high', 'low', 'volume', 'average_volume', 'last_trade_price', 'previous_close']  
        command_list = ['curl -v https://api.robinhood.com/quotes/'+self.stock+'/ -H "Accept: application/json"',  
                     'curl -v https://api.robinhood.com/fundamentals/'+self.stock+'/ -H "Accept: application/json"']

        for commands in command_list:  
            command = commands  
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
            out, err = p.communicate()

            string = out  

APPL = data('AAPL')

command = 'curl -v https://api.robinhood.com/quotes/historicals/AAPL/?interval=day&span=year&bounds=extended'

p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
out, err = p.communicate()
parsed = json.loads(out)
print(len(parsed['historicals']))
print(json.dumps(parsed, indent=4, sort_keys=True))
