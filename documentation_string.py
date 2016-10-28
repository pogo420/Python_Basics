class a:
		pass

class b:
		pass


class Object_test(b,a):
	#"this class documentation:"
	a= 78
	def __init__(self):
		pass
	"this class documentation redefined:"


	
	
obj=Object_test()
print obj.__doc__
obj.__doc__="goat"
print obj.__doc__
print Object_test.__doc__
print Object_test.__dict__
print Object_test.__name__
print Object_test.__module__
print Object_test.__bases__



