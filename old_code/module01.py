#dummy module
def func_test(ip):
	print ip*2
	print type(ip) 

print "i am inside module"

if (__name__=="__main__"):
	#only if executed as a script
	import sys
	func_test(sys.argv[1])