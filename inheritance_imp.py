class Test_A:
	def func(self):
		print "i am in A"

class Test_B:
	def func(self):
		print "i am in B"

class Test(Test_B,Test_A):
	#def func(self):
	#	print " i am in Test"
	pass	

obj=Test()
obj.func()
