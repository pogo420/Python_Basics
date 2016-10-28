class Test:
	def __init__(self):
		print "i am in init method"
	
	def __add__(self,a):
		print "i am __lobo__ method"
		
	def __eq__(self,a):
		print "i am __eq__ method"
	
obj=Test()
obj1=Test()
obj+obj1
obj==obj1

