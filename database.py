#Database class holds list of sequences
class Database:
	# Initializer
	def __init__(self):
		self.sequenceList = []
	
	# generate Sk database 
	#def generateSubDatabase(self,itemSet):

	# generate projected database
	
	# String format of object
	# each sequence is printed in a new line
	def __str__(self):
		outStr = []
		for sequence in self.sequenceList:
			outStr.append(str(sequence))
		return '\n'.join(outStr)