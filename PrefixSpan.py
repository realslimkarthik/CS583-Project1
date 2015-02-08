from __future__ import division
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
    items = []
    count = 1
    for i in inputData:
        line = i.split('=')[-1].strip()
        # items[str(count)] = OrderedDict()
        items.append(float(line))
        count += 1
    return items

def generateItems(dataBase, misVals=[]):
    itemDictionary = OrderedDict()
    present = {}
    for i in dataBase:                                                        # iterate through each sequence in the database
        for j in i:                                                            # iterate through each itemset in a sequence
            for k in j:                                                        # iterate through each item in an itemset
                if k not in present:                                            # Check if item is in the itemDictionary
                    if k not in itemDictionary:                                    # if item not added in the itemDictionary
                        itemDictionary[k] = {}                                    # initialize particular object for that key
                        itemDictionary[k]['actualSupport'] = 1
                        if len(misVals) != 0:
                            itemDictionary[k]['minimumSupport'] = misVals[k - 1]
                    else:                                                        # else if item present in itemDictionary
                        itemDictionary[k]['actualSupport'] += 1                    # increment count of item in the database
                    present[k] = True
        present = {}
    #sort itemDictionary based on minimum support
    if len(misVals) != 0:
        itemDictionary = OrderedDict(sorted(itemDictionary.items(), key=lambda t: t[1]['minimumSupport']))
    return itemDictionary

def frequentItems(dataBase, itemDictionary):
    newItemDict = OrderedDict()
    totalRecords = len(dataBase)
    for (key, val) in itemDictionary.items():
        actualSup = val['actualSupport'] / totalRecords
        if actualSup >= val['minimumSupport']:
            newItemDict[key] = {}
            newItemDict[key]['minimumSupport'] = itemDictionary[key]['minimumSupport']
            newItemDict[key]['actualSupport'] = actualSup
        else:
            continue
    newItemDict = OrderedDict(sorted(newItemDict.items(), key=lambda t: t[1]['minimumSupport']))
    return newItemDict

def generateDatabase(dataBase, item, itemDictionary, SDC=0):
    newDb = []
    flag = False
    for i in dataBase:
        for j in i:
            for k in j:
                flag = (k == item)
                if flag == True:
                    newDb.append(i)
                    break
            if flag == True:
                break
        flag = False
    if SDC != 0:
        for i in newDb:
            for j in i:
                for k in j:
                    if abs(itemDictionary[k]['actualSupport'] - itemDictionary[item]['actualSupport']) > 0:
                        j.remove(k)
    return newDb

def rPrefixSpan(item, dataBase, count):
    # print dataBase
    itemDictionary = generateItems(dataBase)
    print itemDictionary

if __name__ == "__main__":
    f = open(sys.argv[1])
    dataBase = parseInput(f.readlines())
    f.close()
    f = open(sys.argv[2])
    items = parseMis(f.readlines())
    SDC = items[-1]
    print SDC
    f.close()
    itemDictionary = generateItems(dataBase, items)
    # for (key, val) in itemDictionary.items():
    #     print str(key) + ' ' + str(val['actualSupport']) + ' ' + str(val['minimumSupport'])
    newItemDict = frequentItems(dataBase, itemDictionary)
    # for (key, val) in newItemDict.items():
    #     print str(key) + ' ' + str(val['actualSupport']) + ' ' + str(val['minimumSupport'])
    # newDb = generateDatabase(dataBase, 45, itemDictionary, SDC)
    # print newDb
    for (key, val) in newItemDict.items():
        newDb = generateDatabase(dataBase, key, itemDictionary, SDC)
        rPrefixSpan(key, newDb, len(newDb))
