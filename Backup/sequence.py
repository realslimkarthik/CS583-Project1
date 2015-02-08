#import required modules
import itemset as element
import copy

#Sequence class holds ordered collection of ItemSets
class Sequence:
	#initializer
	def __init__(self):
		self.elementList = []

	# function to add itemset to the sequence
	def addItemSet(self,itemset):
		self.elementList.append(itemset)

	# function to remove itemset from sequeence
	def removeItemSet(self,itemset):
		self.elementList.remove(itemset)

	# subsequence generation
	def generateSubsequence(self,itemK):
		# create a new sequence
		newSequence = copy.deepcopy(self)
		for itemSet in newSequence.elementList:
			for item in itemSet.itemset:
				if(item != itemK):
					itemSet.removeItem(item)
				else:
					return newSequence
			if itemSet.isEmpty():
				newSequence.removeItemSet(itemSet)
		return newSequence

	# SDC employ for the sequence
	def employSDC(self,itemK,sdc):
		for itemSet in self.elementList:
			for item in itemSet.itemset:
				if((item.actualSupport - itemK.actualSupport) > sdc):
					itemSet.remove(item)

	#string format of sequence
	#enclosed in <> and itemsets seperated by , 
	def __str__(self):
		outStr = []
		for itemset in self.elementList:
			outStr.append(str(itemset))
		return '<' + ','.join(outStr) + '>'