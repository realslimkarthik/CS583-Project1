#import required modules
import itemset as element

#Sequence class holds ordered collection of ItemSets
class Sequence:
	#initializer
	def __init__(self):
		self.elementList = []

	# function to add itemset to the sequence
	def addItem(self,itemset):
		self.elementList.add(itemset)

	# function to remove itemset from sequeence
	def removeItem(self,itemset):
		self.elementList.remove(itemet)
		
	# subsequence
	# SDC employ
	#	

	#string format of sequence
	#enclosed in <> and itemsets seperated by , 
	def __str__(self):
		outStr = []
		for itemset in self.elementList:
			outStr.append(str(itemset))
		return '<' + ','.join(outStr) + '>'