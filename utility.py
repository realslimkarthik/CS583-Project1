#import required modules
from collections import OrderedDict
import re
import item
import itemset as element
import sequence as seq
import database as db

#function to parse mis file
# returns itemDictionary, supportDifferenceConstraint
def parseMisFile(misFileName):
	# build an item dictionary from mis File
	# it holds item number as key and mis as value
	itemDictionary = OrderedDict()
	# mis key start value
	itemNumber = 0
	# read supportDifferenceConstraint
	supportDifferenceConstraint = 0
	# open mis file handle
	misFile = open(misFileName, 'r')
	try:
		# for each line ending with newline char
		for line in misFile.readlines():
			#split the string on whitespace, return a list of tokens
			tokens = line.split()
			# extract float value from tokens
			floatValue = float(tokens[2])
			#increment key value
			itemNumber += 1
			#add itemNumber key and float value into dictionary
			itemDictionary[itemNumber] = floatValue
	# else throw IOError
	except IOError as e:
		print (str(e))
		sys.exit(2)
	finally:
		misFile.close()
	# add support diff from last item
	supportDifferenceConstraint = itemDictionary[itemNumber]
	# delete last entry
	del itemDictionary[itemNumber]
	# sort dictionary 
	itemDictionary = OrderedDict(sorted(itemDictionary.items(), key=lambda t: t[1]))
	# return values
	return itemDictionary,supportDifferenceConstraint

#function to parse data file
# returns sequence list
def parseDataFile(dataFileName, misValueDictionary):
	# database object
	database = db.Database()
	dataFile = open(dataFileName, 'r')
	try:
		# for each line ending with newline char
		for line in dataFile.readlines():
			# get sequence string
			sequenceString = getStringBetween(line,'<','>')
			# get all itemset strings
			itemsetStrings = re.findall('{([^{]*)}',sequenceString)
			# create sequence object
			sequenceObject = seq.Sequence()
			# create itemset objects and append to sequence object
			for itemset in itemsetStrings:
				tokens = itemset.split(',')
				intValues = [int(x) for x in tokens]
				temp = element.ItemSet(0,0)
				# add items and mis into itemset
				[temp.addItem(item.Item(x,misValueDictionary[x],0)) for x in intValues]
				# sort items based on mis values
				temp.sortItemSet()
				# add itemset to a sequence
				sequenceObject.elementList.append(temp)
			# append sequence to database 
			database.sequenceList.append(sequenceObject)
	# else throw IOError
	except IOError as e:
		print (str(e))
		sys.exit(2)
	finally:
		dataFile.close()
	return database

# get string between <> or {}
def getStringBetween( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""