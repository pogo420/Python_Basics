class ScopeTest:
	str="this is class"
	
	def __init__(self):
		str="this is init"
		print str
	
	print str 		

obj=ScopeTest()
