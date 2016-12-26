
def tag(tag_nam):
	def deco(func):
		def wrap(name):
			return "{1}{0}{1}".format(func(name),tag_nam)
		return wrap
	return deco
'''
@tag('^^')
@tag('**')
'''

def data(name):
	return name

print id(data)
data=tag('^^')(tag('**')(data))

print id(data)

print data("pox")


	
		

		
