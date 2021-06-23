#testing and making hand dirty with command line argument 
#sys module has an array argv
import sys

for i in sys.argv:	#using for loop(array version)
	print i

print len(sys.argv) #without sys referene it can't use argv array
print "type(sys.argv):",type(sys.argv) # 
print "type(sys):", type(sys)
