class Test:
	var_count=5
	def __init__(self):
		#pure class variable :It changes every time we create a object(In the case below)
		#Test.var_count+=1
		self.var_count+=1
		self.x=5
			
obj=Test()
obj1=Test()
#obj.var_count+=10

print "obj.var_count",obj.var_count
print "obj1.var_count",obj1.var_count
print "Test.var_count",Test.var_count
print "obj.x",obj.x 
#print "Test.x",Test.x #x is not a class variable as it is declared inside method

