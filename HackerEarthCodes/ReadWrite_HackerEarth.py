class InvalidData(Exception):
	pass

def dataValidator(num,str):
	Flag=1
	str_len=len(str)
	if (num>=0 and num<=10) and (str_len>=1 and str_len<=15):
		return True
	else:	
		return False	
	
def dataOutput(num,str):
	print num*2
	print str
	
	
def dataInput():
	num=int(raw_input(""))
	str=raw_input("")
	try:
		if dataValidator(num,str):
			dataOutput(num,str)
		else:
			raise InvalidData	
	except InvalidData:
		print "Enter data properly"
				
		
if __name__=='__main__':
	dataInput()