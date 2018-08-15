import subprocess

def login(username, password):  
    command = 'curl -v https://api.robinhood.com/api-token-auth/ -H "Accept: application/json" -d "username='+username+'&password='+password+'"'  
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
    out, err = p.communicate()  
    if len(out) < 1:  
        print 'Error connecting to server:'  
        print err  
    else:  
        print 'Connection successful.'  
    return out

def logout(token):  
    command = 'curl -v https://api.robinhood.com/api-token-logout/ -H "Accept: application/json" -H "Authorization: Token '+token+'" -d ""'  
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
    out, err = p.communicate()


def accountInfo(token):  
    command = 'curl -v https://api.robinhood.com/accounts/ -H "Accept: application/json" -H "Authorization: Token '+token+'"'  
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
    out, err = p.communicate()  
    return out

def main():  
    print 'Logging in...'  
    token = login('vikasagartha', '482Agartha7975')  
    token = token[10:-2]  
    print 'token: ', token  
    print 'Grabbing account information...'  
    account_info = accountInfo(token)  
    print account_info  
    print 'Logging out...'  
    logout(token)

