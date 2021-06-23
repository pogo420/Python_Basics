import sys


def function1(x=10):
	print "you got",x,"chocolate"


def function2():
		str1="abc12efg"
		y = "x" in str1
		print y
	
	
if (len(sys.argv) == 2):
	#print len(sys.argv)
	function1(sys.argv[1])


else:
	function2()
	


