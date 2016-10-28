dict01={1:"Arnab",
		2:"Ram",
		3:"Sam",
		4:"Sud"}

# prints all keys in a list
print "dict01.keys():",dict01.keys()

# prints all values in a list
print "dict01.values():",dict01.values()

# prints all items in a list(each element of list is a tuple 
#containing key value pair separated by comma)
print "dict01.items():",dict01.items()

#checks for a particular key in a dictionary
print "dict01.has_key(5):",dict01.has_key(5)
print "dict01.has_key(5):",dict01.has_key(2)

dict01["Dog"]="Pig"
print "dict01.keys():",dict01.keys()
print "dict01.values():",dict01.values()
print "dict01.items():",dict01.items()

#deleting a single index<=>value

del(dict01[1])

print "del dict01[1]:"

print "dict01.keys():",dict01.keys()
print "dict01.values():",dict01.values()
print "dict01.items():",dict01.items()

print "del dict01:"

#deleting the complete dictionary

del(dict01)
print "dict01.keys():",dict01.keys()
print "dict01.values():",dict01.values()
print "dict01.items():",dict01.items()
