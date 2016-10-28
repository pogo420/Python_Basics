# value of mutable objects can be changed
def add(str):
	str.append(" god")
	print str
	return
	 
str=["str"]
add(str)
print str