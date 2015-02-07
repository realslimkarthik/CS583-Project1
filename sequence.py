#import required modules
import itemset as element

#Sequence class holds ordered collection of ItemSets
class Sequence:
	#initializer
	def __init__(self):
		self.elementList = []
	#string format of sequence
	#enclosed in <> and itemsets seperated by , 
	def __str__(self):
		outStr = []
		for itemset in self.elementList:
			outStr.append(str(itemset))
		return '<' + ','.join(outStr) + '>'