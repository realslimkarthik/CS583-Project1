#Database class holds list of sequences
class Database:
	# Initializer
	def __init__(self):
		self.sequenceList = []
	
	# function to add sequence to the db
	def addSequence(self,sequence):
		self.sequenceList.append(sequence)

	# function to remove sequence from db
	def removeSequence(self,sequence):
		self.sequenceList.remove(sequence)

	# get a sequence based on index
	def getSequence(self,index):
		return self.sequenceList[index]

	#sub database generation
	def generateSubDatabase(self,itemK):
		newDb = Database()
		for seq in self.sequenceList:
			if seq.isItemPresent(itemK):
				newDb.addSequence(seq)
		return newDb

	# String format of object
	# each sequence is printed in a new line
	def __str__(self):
		outStr = []
		for sequence in self.sequenceList:
			outStr.append(str(sequence))
		return '\n'.join(outStr)