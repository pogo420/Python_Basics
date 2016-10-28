def wrapper1(func):
	def wrapper_engine():
		return "-------{0}-------".format(func())
	return wrapper_engine

def wrapper2(func):
	def wrapper_engine():
		return "######{0}######".format(func())
	return wrapper_engine
	
@wrapper1
@wrapper2
def get_text():
	return "Hello"

print get_text()
