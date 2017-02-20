def inputValidator(string):
	lenstr=len(string)
	if (lenstr>0 and lenstr<1000):
		alnumFlag=[s.isalnum() for s in string.split()]
		if all(alnumFlag):
			return True
	else:
		return False

def capitalize(string):
	output=""
	if inputValidator(string):
		dataList=string.split(" ")
		for s in dataList:
			if s.isalpha():
				output+=s.capitalize()+" "
			else:
				output+=s+" "	
		return  output.strip()
	else:
		return "invalid input"

print capitalize(raw_input())