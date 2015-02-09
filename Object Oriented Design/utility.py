#import required modules
import sys,re
import item
import itemset as element
import sequence as seq
import database as db

REGEX_IS = "{([^{]*)}";
REGEX_MIS = "[-+]?\d*\.\d+|\d+"

# get frequent items from database
def getFrequentItems(itemList,database):
	frequentList = element.ItemSet()
	lengthOfDatabse = len(database.sequenceList)
	for item in itemList.itemset:
		for sequence in database.sequenceList:
			if sequence.isItemPresent(item):
				item.actualSupport += 1.0
		item.actualSupport /= lengthOfDatabse
		if item.isFrequent():
			frequentList.addItem(item)
	return itemList,frequentList

# subsequence generation
def generateSubsequence(sequence, itemK, itemList):
	string = getStringBetween(str(sequence), '<', '>')
	string = '{' + string[string.find(str(itemK)) : len(string)]
	itemsetStrings = re.findall(REGEX_IS, string)
	# create sequence object
	sequenceObject = seq.Sequence()
	# create itemset objects and append to sequence object
	for itemset in itemsetStrings:
		tokens = itemset.split(',')
		intValues = [int(x) for x in tokens]
		# create a new ItemSet object
		temp = element.ItemSet()
		# add items and mis into itemset
		[temp.addItem(itemList.getItem(x)) for x in intValues]
		# add itemset to a sequence
		sequenceObject.addItemSet(temp)
	return sequenceObject

# database projection using an itemSet
def projectDatabase(currentDatabase,item):
	newDatabase = db.Database()

	return newDatabase

#function to parse mis file
# returns itemList, supportDifferenceConstraint
def parseMisFile(misFileName):
	# build an item dictionary from mis File
	# it holds item number as key and mis as value
	itemList = element.ItemSet()
	itemNumber = 0
	# open mis file handle
	misFile = open(misFileName, 'r')
	try:
		# for each line ending with newline char
		for line in misFile.readlines():
			t = re.findall(REGEX_MIS,line)
			if len(t) < 2:
				supportDifferenceConstraint = t[0]
			else:
				itemList.addItem(item.Item(int(t[0]),float(t[1])))
	# else throw IOError
	except IOError as e:
		print (str(e))
		sys.exit(2)
	finally:
		misFile.close()
	return itemList,supportDifferenceConstraint

#function to parse data file
# returns sequence list
def parseDataFile(dataFileName, itemList):
	# database object
	database = db.Database()
	dataFile = open(dataFileName, 'r')
	try:
		# for each line ending with newline char
		for line in dataFile.readlines():
			# get sequence string
			sequenceString = getStringBetween(line,'<','>')
			# get all itemset strings
			itemsetStrings = re.findall(REGEX_IS,sequenceString)
			# create sequence object
			sequenceObject = seq.Sequence()
			# create itemset objects and append to sequence object
			for itemset in itemsetStrings:
				tokens = itemset.split(',')
				intValues = [int(x) for x in tokens]
				# create a new ItemSet object
				temp = element.ItemSet()
				# add items and mis into itemset
				[temp.addItem(itemList.getItem(x)) for x in intValues]
				# sort items based on mis values
				temp.sortItemSet()
				# add itemset to a sequence
				sequenceObject.addItemSet(temp)
			# append sequence to database 
			database.addSequence(sequenceObject)
	# else throw IOError
	except IOError as e:
		print (str(e))
		sys.exit(2)
	finally:
		dataFile.close()
		var = generateSubsequence(database.getSequence(1),itemList.getItem(40),itemList)
		print var
	return database

# get string between <> or {}
def getStringBetween( s, first, last ):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""
