

def p_decorator(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))
	return func_wrapper

@p_decorator
def get_text(name):
	return "how are you {0}".format(name)
	
	
#my_get_text=p_decorator(get_text)
print get_text("gandu")