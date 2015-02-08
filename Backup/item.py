#Item class holds an item
class Item:
	# Initializer
	# each item has a name, minsup and actual sup
	def __init__(self, name, minimumSupport, actualSupport = 0):
		self.name = name
		self.minimumSupport = minimumSupport
		self.actualSupport = actualSupport

	# check to see if actual supp > minsupp
	def isfrequent(self):
		if self.actualSupport > self.minimumSupport: 
			return True
		else: 
			return False

	# display item details 
	def printItemDetails(self):
		print name + ' mis: ' + minimumSupport + ' supp: ' + actualSupport
		
	# check for equality of item objects
	def __eq__(self, other): 
		return self.name == other.name

	# return name as string for printing object
	def __str__(self):
		return str(self.name)

	# define hash to use woth sets
	def __hash__(self):
		return hash(self.name) * hash(self.minimumSupport)