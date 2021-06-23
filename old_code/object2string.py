class Object_test:
	
	def __repr__(self):
		return "i am repr method"
		
	def __str__(self):
		return "i am str method"
	
obj=Object_test()

print obj

print repr(obj)

print str(obj)
