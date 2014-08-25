def read(fn):
    with open(fn) as f:
        return f.read()
def readCSV(fn): # project euler's CSV with quoted words
    return [w.strip(' "\'') for w in read(fn).split(',')]
