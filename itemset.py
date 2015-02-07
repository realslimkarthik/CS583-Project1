#import required modules
from collections import OrderedDict
import item

#ItemSet class holds dictionary of items and their mis 
#sorted in ascending order of mis values
class ItemSet:
	# initializer
	def __init__(self,minimumSupport,actualSupport):
		self.itemList = OrderedDict()
		self.minimumSupport = minimumSupport
		self.actualSupport = actualSupport
	# function to add item to the ordered dictionary
	def addItem(self,item):
		self.itemList[item.name] = item
	# function to sort items based on mis
	def sortItemSet(self):
		self.itemList = OrderedDict(sorted(self.itemList.items(), key=lambda t: t[1].minimumSupport))
	# check to see if actual supp > minsupp
	def isfrequent(self):
		if self.actualSupport > self.minimumSupport: 
			return True
		else: 
			return False
	# check for supportDifferenceConstraint
	# def employsupportDifferenceConstraint(self,supportDifferenceConstraint):
	# 	for value in self.itemList:

	# string format of itemset
	# each item set is enclosed by {} and values(keys) seperated by ,
	def __str__(self):
		outStr = []
		for value in list(self.itemList.keys()):
			outStr.append(str(value))
		return '{' + ','.join(outStr) + '}'