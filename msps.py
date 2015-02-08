#import required modules
import sys,getopt as options
import itemset as element
import sequence as seq
import database as db
import utility as util

# main function definition
def main(argv):
	# print welcome note
	print 'Welcome!!'
	# read arguments and load files
	dataFile, misFile = readArguments(argv)
	# load data from file into memory
	itemDictionary, supportDifferenceConstraint = util.parseMisFile(misFile)
	# generate initial databse from file
	initialDatabase = util.parseDataFile(dataFile,itemDictionary)
	print initialDatabase
	# print goodbye note
	print 'Bye!!'

# function to read files from disk 
def readArguments(argv):
	# try to get args else throw error msg
	try:
		opts, args = options.getopt(argv,'d:m:')
	except options.GetoptError as e:
		print (str(e))
		print 'msps.py -d <datafile> -m <misfile>'
		sys.exit(2)
	# if no error, parse args and proceed  
	for opt, arg in opts:
		# store data filename
		if opt == '-d':
			dataFile = arg
		# store mis filename
		elif opt == '-m':
			misFile = arg
	return dataFile, misFile

# if the function is the main function start executing
# pass user given args
if __name__ == '__main__':    
	main(sys.argv[1:])