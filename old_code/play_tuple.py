a=('a',12,12.56,[1,2,'vb'],{"one":1,"two":2})
print type(a)
print a
for i in a:
	print "type:",type(i),"value",i

b=('abc',12)
c=(12,'abc')

print cmp(b,c)	
