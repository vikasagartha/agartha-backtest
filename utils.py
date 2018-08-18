def destructure(obj, tup):
    return [obj[k] for k in tup]

def sma(window=3):
    # split data into window sized chunks and compute average of each chunk
    return lambda data: list(map(lambda sublist: sum(sublist)/len(sublist),
        [data[i:i+window] for i in range(0, len(data))]))

def sma(window=3):
    # split data into window sized chunks and compute average of each chunk
    def make_sma(data):
        sma = [float('nan')]*window
        for i in range(window, len(data)):
            sublist = data[i-window:i]
            sma.append(sum(sublist)/window)
        return sma
    return make_sma
