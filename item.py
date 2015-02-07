#Item class holds an item
class Item:
	# Initializer
	# ech item has a name, minsup and actual sup
	def __init__(self, name, minimumSupport, actualSupport):
		self.name = name
		self.minimumSupport = minimumSupport
		self.actualSupport = actualSupport
	# check to see if actual supp > minsupp
	def isfrequent(self):
		if self.actualSupport > self.minimumSupport: 
			return True
		else: 
			return False
	# each sequence is printed in a new line
	def __str__(self):
		outStr = []
		for sequence in self.sequenceList:
			outStr.append(str(sequence))
		return '\n'.join(outStr)