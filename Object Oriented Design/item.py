#Item class holds an item
class Item:
	# Initializer
	# each item has a name, minsup and actual sup
	def __init__(self, name, minimumSupport, actualSupport = 0):
		self.name = name
		self.minimumSupport = minimumSupport
		self.actualSupport = actualSupport

	# check to see if actual support > minsupp
	def isFrequent(self):
		if self.actualSupport >= self.minimumSupport: 
			return True
		else: 
			return False

	# display item details 
	def printItemDetails(self):
		print str(self.name) + ' mis: ' + str(self.minimumSupport) + ' supp: ' + str(self.actualSupport)
		
	# hash for set
	def __hash__(self):
		return self.name * 2 

	#eq for object
	def __eq__(self,other):
		return self.name == other.name
	
	# return name as string for printing object
	def __str__(self):
		return str(self.name)