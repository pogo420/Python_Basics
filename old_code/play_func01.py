def test_func(age,name):
	print "age:",age,"name",name

	
def default_func(age,sex="M"):
		print "age:",age,"sex:",sex

def var_func(arg1=1,*var_tup):
	print type(var_tup)
	print arg1
	for i in var_tup:
			print i
	
print """Actual definition:test_func(age,name)"""
	
print """test_func(25,"Arnab")"""
test_func(25,"Arnab")

print """test_func("Arnab",25)"""
test_func("Arnab",25)

print """test_func(age=25,name="Arnab")"""
test_func(age=25,name="Arnab")

print """test_func(age="Arnab",name=25)"""
test_func(age="Arnab",name=25)

print """test_func(name=25,age="Arnab")"""
test_func(name=25,age="Arnab")

print """test_func(name="Arnab",age=25)"""
test_func(name="Arnab",age=25)

#default variable function:
print "\nDefault function parameter value:"

print "Default function:"
default_func("F") 

print "Change function:"
default_func(22,"F") 

#variable argument 
print "######################################"
var_func()
print "######################################"
var_func(23)
print "######################################"
var_func(23,45,67,21,10,5,3,1)

