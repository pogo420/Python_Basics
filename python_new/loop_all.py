#function definition
import inspect 
str="Hello123"
def separator():
	print "#"*20

def selector(arr):
	#print arr[1]
	if arr[1] == "1" :
		separator()
		for_test()
	elif arr[1] == "2":
		separator()
		while_test()
	else :
	 print "wrong output"

def for_test():
 print "initiating",inspect.stack()[0][3]
 
 for i in str :
	if i == "1" :
		#break;
		#continue
		pass
		print i
	else :
		print i

 
	
def while_test():
 print "initiating",inspect.stack()[0][3]
 
 
 

