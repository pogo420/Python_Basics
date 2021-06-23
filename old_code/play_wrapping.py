def func_outer(name):
	def func_inner():
		return "Hello "
	inner_op=func_inner()+name
	return inner_op

#sending a function as an 	
def func_macker(func):
	return func("Gandu")

# assigning a function to a variable
func_var= func_macker
#print func_var("Gandu")

print func_var(func_outer)

