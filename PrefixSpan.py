import sys
from collections import OrderedDict

def parseInput(inputData):
    cleanData = []
    for i in inputData:
        line = i.strip().strip('<').strip('>').strip('{').strip('}')
        cleanLine = line.split('}{')
        transaction = []
        for j in cleanLine:
            sequence = map(lambda x: int(x), j.split(','))
            transaction.append(sequence)
        cleanData.append(transaction)
    return cleanData

def parseMis(inputData):
    items = OrderedDict()
    count = 1
    for i in inputData:
        line = i.split('=')[-1].strip()
        items[str(count)] = OrderedDict()
        items[str(count)]['mis'] = float(line)
        items[str(count)]['count'] = 0
        count += 1
    return items

if __name__ == "__main__":
    f = open(sys.argv[1])
    cleanData = parseInput(f.readlines())
    f.close()
    f = open(sys.argv[2])
    items = parseMis(f.readlines())
    f.close()
    