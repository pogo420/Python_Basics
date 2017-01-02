class InvalidData(Exception):
	pass

def outData(hash):
	for i in sorted(hash.keys()):
		print "{0} {1}".format(i,hash[i])


def countDigit(string):
	hash={"0":0,
		  "1":0,
		  "2":0,
		  "3":0,
		  "4":0,
		  "5":0,
		  "6":0,
		  "7":0,
		  "8":0,
		  "9":0}
	
	for i in string:
		try:
			int(i)
			hash[i]+=1
			
		except ValueError:
			pass
	
	outData(hash)

def inputData():
	try:
		string=raw_input()
		string_len=len(string)
		if (string_len>=1 and string_len<=100):
			countDigit(string)
		else:
			raise InvalidData
	
	except InvalidData:
		print "Invalid data"
	
	
if __name__=='__main__':
	inputData()