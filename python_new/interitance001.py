class A:
	a="A"
	def methA(self):
		print "i am in class a"
	def comm(self):
		print "i am in class a"

class B:
	a="B"
	def methB(self):
		print "i am in class b"
	def comm(self):
		print "i am in class b"

class Main(B,A,object):
	def comm1(self):
		print "i am in class main"
		print super(Main,self).a
		

obj=Main()
obj.comm1()

