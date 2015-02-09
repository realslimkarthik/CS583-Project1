#ItemSet class holds set of item objects
class ItemSet:
	# initializer
	def __init__(self):
		self.itemset = set()

	# function to add item to the set
	def addItem(self,item):
		self.itemset.add(item)

	# function to remove element from set
	def removeItem(self,item):
		self.itemset.remove(item)

	# get item with value
	def getItem(self,integer):
		for i in self.itemset:
			if integer == i.name:
				return i

	# check existence of itemList
	def isListPresent(self,itemList):
		return self.itemset.isSubset(itemList)

	# check if element exists
	def isItemPresent(self,item):
		return item in self.itemset

	#check if itemSet is empty
	def isEmpty(self):
		if len(self.itemset) == 0:
			return True
		else:
			return False

	# sort items lexicographically
	def sortItemSet(self):
		self.itemset = sorted(self.itemset,key=lambda x: x.name)

	# string format of itemset
	# each itemset is enclosed by {} and values(keys) seperated by ,
	def __str__(self):
		outStr = []
		for value in self.itemset:
			outStr.append(str(value))
		return '{' + ','.join(outStr) + '}'