class Test:
	var=5
	"god is great"
	str="I am instance variable"
	#"god is great"
	def __init__(self):
		pass
		#self.__doc__="god is super great"
		
	def __del__(self):
		print "i am dying"
	def method_options(self):
		self.x=2
		x=3

object=Test()

print object.__dict__
object.method_options()
print object.__dict__
object.__dict__["social"]="Male"
print object.__dict__.keys()
print "===================="
print Test.__dict__.keys()

print "Class_doc:",Test.__doc__
print object.__doc__
