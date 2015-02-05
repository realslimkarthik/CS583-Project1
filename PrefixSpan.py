import sys

def parse(inputData):
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

if __name__ == "__main__":
    f = open(sys.argv[1])
    cleanData = parse(f.readlines())
    f.close()
    print cleanData
