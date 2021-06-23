#function creating lambda generator
def increment_creator(n):
	print type(lambda x: x + n)	# it returns a function
	return lambda x: x + n
#g=lambda x:x+6	
g=increment_creator(6)

#h=lambda x:x+2
h=increment_creator(2)

print "g(45):",g(45)
print "h(45):",h(45)

#applying map,filter and reduce
seq=list(range(1,50,1))

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "seq:",seq
print "filter(lambda x:x%3==0,seq):",filter(lambda x:x%3==0,seq)
print "map(lambda x:x*10,filter(lambda x:x%3==0,seq))",map(lambda x:x*10,filter(lambda x:x%3==0,seq))
print "reduce(lambda x,y:x+y,map(lambda x:x*10,filter(lambda x:x%3==0,seq)))",reduce(lambda x,y:x+y,map(lambda x:x*10,filter(lambda x:x%3==0,seq)))