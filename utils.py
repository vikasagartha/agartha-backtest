def destructure(obj, tup):
    return [obj[k] for k in tup]

def sma(window=3):
    # split data into window sized chunks
    stratified_data = [data[i:i+window] for i in range(0, len(data), window)]
    # compute average of each chunk
    return lambda data: list(map(lambda sublist: sum(sublist)/len(sublist),
        stratified_data))
